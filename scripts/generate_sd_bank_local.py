"""Author, check, and publish the 85-subchapter SD bank entirely offline."""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import re
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.ingestion.question_sync import load_sources,report_catalog,coverage
from app.presentation.latex import normalize_document,math_spans,MATH,COMMANDS
from app.services.exercise.workflow import atomic_json,batch_lock,digest,safe_asset
from app.services.exercise.schema import ExerciseFile,Soal
from app.services.exercise.replenishment_math import m
from app.services.exercise.options import susun

RUN=ROOT/'runs/sd_bank_local_v1'
SCHEMA='codex-local-sd-bank-v1'
LEVELS=('easy','medium','hard')
SCORES={'easy':600,'medium':1000,'hard':1400}
EXPECTED={1:25,2:20,3:18,4:22}


def load(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def fingerprint(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
def resolve(path):return ROOT/path
def rel(path):return Path(path).relative_to(ROOT).as_posix()


def protected_files():
    files=list((ROOT/'output/pretest').rglob('*'))
    for base in (ROOT/'output/exercise').glob('kelas*'):
        if base.name not in {'kelas1','kelas2','kelas3','kelas4'}:files.extend(base.rglob('*'))
    return {rel(p):digest(p) for p in files if p.is_file() and p.name!='.workflow.lock' and not p.name.endswith('.tmp')}


def prepare():
    """Freeze actual catalogue and primary, active pretest references, not samples."""
    RUN.mkdir(parents=True,exist_ok=True)
    path=RUN/'plan.json'
    if path.exists():
        plan=load(path);assert fingerprint({k:v for k,v in plan.items() if k!='planHash'})==plan['planHash'],'Frozen generation plan changed'
        assert digest(RUN/'pretest_blueprints.json')==plan['referenceHash']
        return plan
    catalog=[r for r in report_catalog(ROOT/'API_DOCUMENTATION/Pesan_eror.md') if r['class_key'] in {'kelas1','kelas2','kelas3','kelas4'}]
    assert Counter(r['class_key'] for r in catalog)=={'kelas'+str(k):v for k,v in EXPECTED.items()}
    references=[]
    for source in load_sources(ROOT/'output'):
        if source.kind!='pretest' or source.class_key not in {'kelas1','kelas2','kelas3','kelas4'} or source.item.get('status')!='active':continue
        row=source.item;key=next(o['text'] for o in row['options'] if o['option_id']==row['jawaban'])
        references.append({'id':row['_id'],'class':source.class_key,'chapter':source.chapter_no,'code':source.code,'topic':row['subbab_id'],'text':row['soal_text'],'answer':key,'source':source.source,'imageRefs':row.get('image_url',[]),'row':row})
    assert references
    atomic_json(RUN/'pretest_blueprints.json',{'references':references,'newApiCalls':0})
    atomic_json(RUN/'protected_inputs.json',protected_files())
    plan={'schemaVersion':SCHEMA,'catalog':catalog,'targetQuestions':2550,'questionsPerLevel':10,'visualPerLevel':7,'textPerLevel':3,'apiCalls':0,'sessions':1,'referenceHash':digest(RUN/'pretest_blueprints.json')}
    plan['planHash']=fingerprint(plan);atomic_json(path,plan)
    return plan


# Only use concepts explicitly represented in the primary pretest bank.
ADAPTATIONS={
 (4,1,'A'):(3,1,'A'),(4,1,'B'):(3,1,'B'),(4,1,'C'):(3,1,'C'),
 (4,1,'D'):(3,1,'B'),(4,1,'E'):(3,1,'D'),(4,1,'F'):(3,1,'E'),
 (4,1,'G'):(3,1,'F'),(4,1,'H'):(3,1,'G'),
 (4,2,'A'):(2,5,'C'),(4,2,'B'):(2,5,'C'),(4,2,'C'):(2,5,'A'),
 (4,2,'D'):(4,2,'E'),(4,3,'A'):(2,4,'B'),(4,4,'A'):(3,1,'F'),
 (4,5,'A'):(3,4,'A'),(4,6,'A'):(2,8,'B'),
}


def reference_pool(job,refs):
    grade=int(job['class_key'][5:]);identity=(grade,job['chapter_no'],job['code'])
    def match(identity):
        g,b,c=identity
        return [r for r in refs if (r['class'],r['chapter'],r['code'])==('kelas'+str(g),b,c)]
    pool=match(identity)
    if pool:return pool,False
    assert identity in ADAPTATIONS,('No source-concept mapping',identity)
    pool=match(ADAPTATIONS[identity]);assert pool,('Adaptation reference unavailable',identity,ADAPTATIONS[identity])
    return pool,True


def solve(cert):
    if cert['type'].startswith('sd_review'):
        from app.services.exercise.sd_review_additions import solve_certificate
        return solve_certificate(cert)
    from app.services.exercise import sd_bank_low,sd_bank_high
    if cert['type'].startswith('sd_low'):return sd_bank_low.solve_certificate(cert)
    return sd_bank_high.solve_certificate(cert)


def answer_identity(text):
    """Detect equivalent numeric options, including fractions in KaTeX."""
    import sympy as s
    value=text.strip().strip('$').replace(r'\,','').replace(r'\ ','')
    value=re.sub(r'\\(?:text|mathrm)\{[^{}]*\}','',value)
    for _ in range(3):value=re.sub(r'\\(?:dfrac|tfrac|frac)\{([^{}]+)\}\{([^{}]+)\}',r'((\1)/(\2))',value)
    value=value.replace(r'\times','*').replace(r'\div','/').replace('^','**').replace('−','-')
    value=value.replace('{,}','.').replace(',','.')
    if re.fullmatch(r'[0-9+*/(). \-]+',value):
        try:return 'number:'+str(s.simplify(s.sympify(value,rational=True)))
        except Exception:pass
    return 'text:'+re.sub(r'\s+','',text).casefold()


def path_value(scene,path):
    value=scene
    for key in path:value=value[key]
    return value


def visual_check(model):
    """Test pivotal visible facts through the independently retained local model."""
    if not model['scene']:return {'status':'text_question'}
    cert=model['certificate'];inputs=cert.get('inputs',cert.get('variables',cert));bindings=cert.get('visual_bindings',[])
    passed=[];original=solve(cert)
    for binding in bindings:
        name=binding['input'];visible=path_value(model['scene'],binding['path']);input_path=binding.get('input_path',[])
        expected=path_value(inputs[name],input_path)
        assert visible==expected or answer_identity(str(visible))==answer_identity(str(expected)),('Scene/model disagreement',name,visible,expected)
        alternatives=binding.get('alternatives',[])
        if isinstance(visible,(int,float)):alternatives=[visible+1,visible-1,*alternatives]
        for changed in alternatives:
            altered=deepcopy(cert);altered_inputs=altered.get('inputs',altered.get('variables',altered))
            if input_path:
                cursor=altered_inputs[name]
                for key in input_path[:-1]:cursor=cursor[key]
                cursor[input_path[-1]]=changed
            else:altered_inputs[name]=changed
            changed_scene=deepcopy(model['scene']);cursor=changed_scene
            for key in binding['path'][:-1]:cursor=cursor[key]
            cursor[binding['path'][-1]]=changed
            from app.services.exercise.sd_bank_visuals import validate_scene
            try:validate_scene(changed_scene)
            except (ValueError,AssertionError,KeyError,TypeError):continue
            try:new_value=solve(altered)
            except (ValueError,AssertionError,ZeroDivisionError,TypeError,KeyError):continue
            if new_value!=original:
                assert fingerprint(changed_scene)!=fingerprint(model['scene'])
                passed.append({'input':name,'path':binding['path'],'originalFact':visible,'counterfactualFact':changed,'originalResult':str(original),'counterfactualResult':str(new_value),'counterfactualSceneHash':fingerprint(changed_scene)})
                break
    assert passed,('Visual has no tested pivotal fact',model['kind'],bindings)
    return {'status':'local_semantic_counterfactual_pass','checks':passed,'independentVisionValidation':False}


def factory(grade,bab,code,level,r,visual,index):
    if grade<=2:
        from app.services.exercise.sd_bank_low import generate
    else:
        from app.services.exercise.sd_bank_high import generate
    return generate(grade,bab,code,level,r,visual,index)


def base_for(grade):return ROOT/'output/exercise'/('kelas'+str(grade))/'batch01'


def generate_file(job,level,plan):
    grade=int(job['class_key'][5:]);base=base_for(grade);target=base/f"bab{job['chapter_no']:02d}"/f"{job['code']}_{level}.json"
    checkpoint=base/'local_generation_checkpoint.json';state=load(checkpoint) if checkpoint.exists() else {'planHash':plan['planHash'],'files':{}}
    assert state['planHash']==plan['planHash']
    key=target.relative_to(base).as_posix()
    if key in state['files']:
        assert digest(target)==state['files'][key]['sha256'];ExerciseFile.model_validate(load(target))
        return False
    refs=load(base/'reference_blueprints.json')['references'];pool,adapted=reference_pool(job,refs)
    raw={'book':job['class_key'],'bab_no':job['chapter_no'],'subbab':job['code'],'level':level,'batch':1,'skill_versi':'v1','generator':'codex:sd-local-bank-v1','soal':[]}
    proofs=[];identities=set()
    for previous in base.glob('bab*/*_*.json'):
        if previous==target or not re.fullmatch(r'[A-Z]_(easy|medium|hard)\.json',previous.name):continue
        for q in load(previous)['soal']:
            identities.add(fingerprint({'text':q['pertanyaan'],'scene':(q.get('visual_spec') or {}).get('scene')}))
    from app.services.exercise.sd_bank_visuals import render_scene
    for index in range(1,11):
        visual=index<=7;work=f"{job['class_key']}-b{job['chapter_no']:02d}-{job['code'].lower()}-{level}-bt01-{index:03d}"
        rng=random.Random(int(hashlib.sha256(work.encode()).hexdigest()[:16],16))
        for attempt in range(300):
            model=factory(grade,job['chapter_no'],job['code'],level,rng,visual,index);model=normalize_document(model)
            identity=fingerprint({'text':model['question'],'scene':model['scene']})
            if identity not in identities:break
        else:raise ValueError('Variation capacity exhausted: '+work)
        identities.add(identity)
        assert model['steps']>={'easy':1,'medium':2,'hard':3}[level]
        assert len(model['wrong'])==3 and len({answer_identity(v) for v in [model['answer'],*model['wrong']]})==4,(work,model['answer'],model['wrong'])
        value=solve(model['certificate']);assert answer_identity(m(value) if not isinstance(value,str) else value)==answer_identity(model['answer']),(work,value,model['answer'])
        essential=visual_check(model)
        images=[];provenance={}
        if visual:
            assert model['scene'];asset,provenance=render_scene(model['scene'],base);images=['exercise_assets/'+job['class_key']+'/batch01/'+asset]
        else:assert model['scene'] is None
        reference=rng.choice(pool);snapshot=base/'reference_blueprints.json'
        q={'id':work,'tipe_generate':'variasi','variasi_cara':'angka' if index%2 else 'konteks',
           'acuan':{'sumber':'pretest_validated','id':reference['id'],'teks':reference['text'],'jawaban':reference['answer'],'snapshot':rel(snapshot),'source_sha256':plan['referenceHash']},
           'cognitive_c':{'easy':'C2','medium':'C3','hard':'C4'}[level],'jumlah_langkah':model['steps'],'jenis_soal':model['kind'][:60],
           'alasan_level':model['rationale'],'stimulus':None,'pertanyaan':model['question'],'jawaban_benar':model['answer'],'alasan_benar':model['explanation'],
           'distraktor':[{'teks':v,'alasan':(model.get('wrong_reasons') or [f'Pilihan ini tidak memenuhi seluruh informasi dan langkah pada soal; hasil yang sesuai adalah {model["answer"]}.']*3)[i]} for i,v in enumerate(model['wrong'])],
           'pembahasan':model['explanation'],'catatan':'Variasi konsep pretest; pemeriksaan lokal Codex, tanpa API. Confidence belum diukur.'}
        if visual:q.update(gambar=images,deskripsi_gambar=model.get('description') or 'Data yang terlihat pada gambar: '+json.dumps(model['scene'],ensure_ascii=False),visual_spec={'kind':'sd_scene','scene':model['scene']})
        Soal.model_validate(q);raw['soal'].append(q)
        proofs.append({'workingId':work,'rawHash':fingerprint(q),'certificate':model['certificate'],'expected':str(value),'visualCheck':essential,'visualProvenance':provenance,
                       'sourceClass':reference['class'],'sourceChapter':reference['chapter'],'sourceCode':reference['code'],'conceptAdaptation':adapted,
                       'targetTopic':job['name'],'targetClass':job['class_key'],'assessedLevel':level,'assessmentRationale':model['rationale'],'apiCalls':0})
    ExerciseFile.model_validate(raw)
    # Commit proof first, then candidate; only a matching pair is resumable.
    proof_path=RUN/'checks'/job['class_key']/f"{job['chapter_no']:02d}_{job['code']}_{level}.json"
    atomic_json(proof_path,{'items':proofs,'rawHash':fingerprint(raw),'apiCalls':0});atomic_json(target,raw)
    state['files'][key]={'sha256':digest(target),'proof':rel(proof_path),'proofSha256':digest(proof_path),'questions':10,'visual':7}
    atomic_json(checkpoint,state)
    return True


def initialize(grade,plan):
    base=base_for(grade);base.mkdir(parents=True,exist_ok=True)
    reference=base/'reference_replenishment_state.json'
    if not reference.exists():
        assert not (base/'hasil_validasi').exists() and not (base/'soal_exercise_db.json').exists()
        atomic_json(reference,{'schemaVersion':SCHEMA,'class':'kelas'+str(grade),'batch':'batch01','phase':'generating','reviewMode':'local_without_external_api','validationOwner':'codex_local_review'})
    state=load(reference);assert state['reviewMode']=='local_without_external_api' and state['class']=='kelas'+str(grade)
    frozen=base/'reference_blueprints.json'
    if not frozen.exists():shutil.copyfile(RUN/'pretest_blueprints.json',frozen)
    assert digest(frozen)==plan['referenceHash']
    localplan=base/'generation_plan.json'
    if not localplan.exists():atomic_json(localplan,{**plan,'class':'kelas'+str(grade),'catalog':[r for r in plan['catalog'] if r['class_key']=='kelas'+str(grade)]})
    assert load(localplan)['planHash']==plan['planHash']


def progress(plan):
    classes={};total=images=0
    for grade in range(1,5):
        path=base_for(grade)/'local_generation_checkpoint.json';state=load(path) if path.exists() else {'files':{}}
        count=sum(v['questions'] for v in state['files'].values());visual=sum(v['visual'] for v in state['files'].values());total+=count;images+=visual
        classes['kelas'+str(grade)]={'generated':count,'target':EXPECTED[grade]*30,'visual':visual,'text':count-visual,'published':(base_for(grade)/'hasil_validasi/manifest.json').exists()}
    result={'target':2550,'generated':total,'remaining':2550-total,'percent':round(total/25.5,2),'visual':images,'text':total-images,'apiCalls':0,'classes':classes}
    atomic_json(RUN/'progress.json',result);return result


def check_latex(questions,path):
    expressions=set()
    for q in questions:
        for value in [q['pertanyaan'],q['pembahasan'],q['jawaban_benar'],*[v['teks'] for v in q['distraktor']],*[v['alasan'] for v in q['distraktor']]]:
            assert value.count('$')%2==0 and not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]',value)
            assert not re.search(r'\\(?:'+'|'.join(COMMANDS)+r')\b',MATH.sub('',value)),('Unwrapped LaTeX',q['id'],value)
            expressions.update(math_spans(value))
    atomic_json(path,[{'id':i,'tex':tex,'display':display} for i,(tex,display) in enumerate(sorted(expressions))])
    result=json.loads(subprocess.run(['node',str(ROOT/'scripts/latex_render_check.cjs'),str(path)],capture_output=True,text=True,encoding='utf-8',check=True).stdout)
    assert not result['errors'],result['errors'][:3]
    return result


def verify(bundle):
    bundle=Path(bundle);base=bundle.parent;manifest=load(bundle/'manifest.json')
    if manifest['schemaVersion']=='codex-sd-difficulty-review-v2':
        from scripts.review_sd_difficulty_local import verify
        return verify(bundle)
    assert manifest['schemaVersion']==SCHEMA
    for name,expected in manifest['outputs'].items():assert digest(bundle/name)==expected
    for name,expected in manifest['inputs'].items():assert digest(base/name)==expected
    rows=load(bundle/'validation_results.json');meta=load(bundle/'validation_results_meta.json');source=load(base/'soal_exercise_db.json')['items'];source_meta=load(base/'soal_exercise_meta.json')
    evidence=load(bundle/'bukti_validasi/codex_local_sd_review.json')['items'];by_id={r['questionId']:r for r in evidence}
    assert len(rows)==len(source)==len(by_id)==manifest['questionCount'] and len(meta)==len(rows)
    assert [q['_id'] for q in rows]==[q['_id'] for q in source]
    for row,unlabelled in zip(rows,source):
        qid=row['_id'];record=by_id[qid];assert qid in source_meta and fingerprint(row)==record['publishedHash']
        assert fingerprint(unlabelled)==record['sourceHash']
        assert {k:v for k,v in row.items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}=={k:v for k,v in unlabelled.items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}
        assert row['status']=='active' and row['confidence_score']==0 and row['cognitive_level']==record['assessedLevel']
        assert meta[qid]['validasi']['api_runs']==0 and meta[qid]['validasi']['training_evidence_qualified'] is False
        value=solve(record['certificate']);correct=next(o['text'] for o in row['options'] if o['option_id']==row['jawaban'])
        assert answer_identity(m(value) if not isinstance(value,str) else value)==answer_identity(correct)
        assert len({answer_identity(o['text']) for o in row['options']})==4
        for ref in row['image_url']:safe_asset(base,ref)
    counts=Counter((meta[q['_id']]['bab_id'],meta[q['_id']]['subbab_kode'],q['cognitive_level']) for q in rows)
    visual=Counter((meta[q['_id']]['bab_id'],meta[q['_id']]['subbab_kode'],q['cognitive_level']) for q in rows if q['image_url'])
    expected={(('SD'+manifest['class'][5:]+'-B'+str(job['chapter_no'])),job['code'],level) for job in load(base/'generation_plan.json')['catalog'] for level in LEVELS}
    assert set(counts)==expected and all(n==10 and visual[k]==7 for k,n in counts.items())


def publish(grade,plan):
    base=base_for(grade);final=base/'hasil_validasi'
    if final.exists():
        verify(final)
        state=load(base/'reference_replenishment_state.json');state.update(phase='local_review_complete',publishedQuestions=len(load(final/'validation_results.json')));atomic_json(base/'reference_replenishment_state.json',state)
        return
    checkpoint=load(base/'local_generation_checkpoint.json');jobs=[r for r in plan['catalog'] if r['class_key']=='kelas'+str(grade)]
    assert len(checkpoint['files'])==len(jobs)*3
    rows=[];meta={};raw_questions=[];evidence=[];now=datetime.now(timezone.utc).isoformat();input_files={}
    for job in jobs:
        for level in LEVELS:
            path=base/f"bab{job['chapter_no']:02d}"/f"{job['code']}_{level}.json";assert digest(path)==checkpoint['files'][path.relative_to(base).as_posix()]['sha256']
            raw=load(path);data=ExerciseFile.model_validate(raw);proof_path=resolve(checkpoint['files'][path.relative_to(base).as_posix()]['proof']);proof=load(proof_path)
            assert digest(proof_path)==checkpoint['files'][path.relative_to(base).as_posix()]['proofSha256'] and fingerprint(raw)==proof['rawHash']
            arranged=susun(data);input_files[path.relative_to(base).as_posix()]=digest(path)
            for q,record in zip(raw['soal'],proof['items']):
                assert fingerprint(q)==record['rawHash'];qid=hashlib.md5(q['id'].encode()).hexdigest()[:24];options,key=arranged[q['id']]
                refs=[g.split('/batch01/',1)[1] for g in q.get('gambar',[])]
                row={'_id':qid,'berkas_id':None,'kelas_id':job['class_key'],'subbab_id':job['name'],'soal_text':q['pertanyaan'],'image_url':refs,'soal_type':'Pilihan Ganda','options':options,'matching_pairs':None,'jawaban':key,'cognitive_level':None,'cognitive_score':None,'confidence_score':None,'status':'inactive','created_at':now,'updated_at':now}
                published={**row,'cognitive_level':level,'cognitive_score':SCORES[level],'confidence_score':0,'status':'active'}
                info={'id':q['id'],'batch':1,'bab_id':'SD'+str(grade)+'-B'+str(job['chapter_no']),'subbab_kode':job['code'],'level_target':level,'cognitive_score_target':SCORES[level],
                      'acuan':q['acuan'],'cognitive_c':q['cognitive_c'],'jumlah_langkah':q['jumlah_langkah'],'jenis_soal':q['jenis_soal'],'pembahasan':q['pembahasan'],'alasan_level':q['alasan_level'],
                      'tipe_generate':'variasi','variasi_cara':q['variasi_cara'],'variationAxes':['angka','konteks'],'generator':'codex:sd-local-bank-v1','skill_versi':'v1','bergambar':bool(refs),'gambar':q.get('gambar',[]),'visual_spec':q.get('visual_spec'),'visual_provenance':record['visualProvenance'],'local_math_check':record['certificate'],'sourceAdaptation':{k:record[k] for k in ['sourceClass','sourceChapter','sourceCode','conceptAdaptation']},'validation_status':'codex_local_review_pass'}
                meta[qid]=info;rows.append(row);raw_questions.append(q);evidence.append({**record,'questionId':qid,'sourceHash':fingerprint(row),'publishedHash':fingerprint(published),'publishedQuestion':published})
    rendering=check_latex(raw_questions,RUN/f'latex_{grade}.json');atomic_json(RUN/f'render_{grade}.json',rendering)
    final_meta={}
    for record in evidence:
        qid=record['questionId'];info=deepcopy(meta[qid]);info['local_review']=record
        info['validasi']={'status':'active','cognitive_level':record['assessedLevel'],'cognitive_score':SCORES[record['assessedLevel']],'confidence_score':0,'confidence_available':False,'confidence_status':'not_measured','validation_status':'codex_local_review_pass','validation_method':'codex_local_review','label_provenance':'codex_local_assessment','api_runs':0,'requested_runs':0,'local_review_passes':1,'training_evidence_qualified':False,'full_complete':True,'level_sesuai_target':True}
        final_meta[qid]=info
    master=base/'soal_exercise_db.json';metadata=base/'soal_exercise_meta.json';rollback={p:p.read_bytes() if p.exists() else None for p in (master,metadata)}
    for p in [base/'reference_blueprints.json',base/'generation_plan.json',*sorted((base/'assets').glob('*'))]:input_files[p.relative_to(base).as_posix()]=digest(p)
    # Put the staging folder in batch01 so portable relative inputs resolve identically.
    staging=Path(tempfile.mkdtemp(prefix='.local-publication-',dir=base))
    atomic_json(staging/'validation_results.json',[r['publishedQuestion'] for r in evidence]);atomic_json(staging/'validation_results_meta.json',final_meta)
    atomic_json(staging/'bukti_validasi/codex_local_sd_review.json',{'schemaVersion':SCHEMA,'items':evidence,'apiCalls':0,'rendering':rendering})
    code=staging/'bukti_validasi/reviewed_code';code.mkdir()
    for p in [ROOT/'scripts/generate_sd_bank_local.py',*sorted((ROOT/'app/services/exercise').glob('sd_bank_*.py'))]:shutil.copyfile(p,code/p.name)
    note=f'# Latihan kelas {grade}\n\n{len(rows)} soal, 70% bergambar. Pemeriksaan lokal Codex; confidence 0 berarti belum diukur. Tanpa API, bukan validasi AI independen atau kalibrasi empiris. Tidak disinkronkan ke production.\n'
    for name in ['README.md','RINGKASAN_VALIDASI.md','LAPORAN_VALIDASI.md']:(staging/name).write_text(note,encoding='utf-8')
    manifest={'schemaVersion':SCHEMA,'class':'kelas'+str(grade),'questionCount':len(rows),'visualQuestions':sum(bool(r['image_url']) for r in rows),'apiCalls':0,'inputs':input_files,'outputs':{p.relative_to(staging).as_posix():digest(p) for p in staging.rglob('*') if p.is_file()}}
    journal=RUN/'transactions'/('publish_kelas'+str(grade)+'.json');recovery={}
    for p,data in rollback.items():
        saved=RUN/'backups'/('kelas'+str(grade))/p.name
        if data is not None:
            saved.parent.mkdir(parents=True,exist_ok=True);saved.write_bytes(data);recovery[rel(p)]=rel(saved)
        else:recovery[rel(p)]=None
    atomic_json(journal,{'phase':'prepared','rollback':recovery,'staging':rel(staging)})
    try:
        atomic_json(master,{'book':'kelas'+str(grade),'batch':1,'items':rows});atomic_json(metadata,meta)
        for p in (master,metadata):input_files[p.relative_to(base).as_posix()]=digest(p)
        atomic_json(staging/'manifest.json',manifest)
        verify(staging);staging.rename(final);verify(final)
    except Exception:
        if final.exists():final.rename(RUN/('failed_publication_kelas'+str(grade)))
        for p,data in rollback.items():
            if data is None:p.unlink(missing_ok=True)
            else:p.write_bytes(data)
        raise
    state=load(base/'reference_replenishment_state.json');state.update(phase='local_review_complete',publishedQuestions=len(rows));atomic_json(base/'reference_replenishment_state.json',state)
    atomic_json(journal,{'phase':'committed','questions':len(rows),'manifestSha256':digest(final/'manifest.json')})


def audit(plan):
    # The original target remains a generation baseline; the reviewed export can
    # contain additions and withheld questions after honest difficulty changes.
    manifests=[base_for(g)/'hasil_validasi/manifest.json' for g in range(1,5)]
    if all(p.exists() and load(p)['schemaVersion']=='codex-sd-difficulty-review-v2' for p in manifests):
        from scripts.review_sd_difficulty_local import audit_all
        return audit_all()
    from PIL import Image
    seen=set();visual=0;counts={};representatives={};rendered_total=0
    for grade in range(1,5):
        base=base_for(grade);verify(base/'hasil_validasi');rows=load(base/'hasil_validasi/validation_results.json');meta=load(base/'hasil_validasi/validation_results_meta.json');kind_counts=Counter();identities=set();raw_by={}
        for path in base.glob('bab*/*_*.json'):
            raw=load(path);ExerciseFile.model_validate(raw)
            assert len(raw['soal'])==10 and sum(bool(q.get('gambar')) for q in raw['soal'])==7
            for q in raw['soal']:
                identity=fingerprint({'text':q['pertanyaan'],'scene':(q.get('visual_spec') or {}).get('scene')})
                assert identity not in identities,('Duplicate within class',q['id'])
                identities.add(identity);raw_by[q['id']]=q
        rendered_total+=load(RUN/f'render_{grade}.json')['checked']
        for row in rows:
            assert row['_id'] not in seen;seen.add(row['_id']);kind_counts[meta[row['_id']]['jenis_soal']]+=1
            info=meta[row['_id']];q=raw_by[info['id']];record=info['local_review'];assert fingerprint(q)==record['rawHash'] and q['pertanyaan']==row['soal_text']
            assert answer_identity(q['jawaban_benar'])==answer_identity(next(o['text'] for o in row['options'] if o['option_id']==row['jawaban']))
            assert {answer_identity(v) for v in [q['jawaban_benar'],*[d['teks'] for d in q['distraktor']]]}=={answer_identity(o['text']) for o in row['options']}
            scene=(q.get('visual_spec') or {}).get('scene')
            visual_check({'kind':q['jenis_soal'],'scene':scene,'certificate':record['certificate']})
            if scene:
                provenance=record['visualProvenance'];assert provenance['semanticSpec']==scene
                assert digest(safe_asset(base,row['image_url'][0]))==provenance['pngSha256']
                key=(grade,row['cognitive_level'],scene['kind'])
                representatives.setdefault(key,{'image':str(safe_asset(base,row['image_url'][0])),'question':q['pertanyaan'],'answer':q['jawaban_benar'],'id':q['id']})
            for ref in row['image_url']:
                with Image.open(safe_asset(base,ref)) as im:im.verify()
            visual+=bool(row['image_url'])
        counts[grade]={'questions':len(rows),'images':sum(bool(r['image_url']) for r in rows),'text':sum(not r['image_url'] for r in rows),'families':dict(kind_counts)}
    assert len(seen)==2550 and visual==1785
    original=load(RUN/'protected_inputs.json');assert all(resolve(p).is_file() and digest(resolve(p))==sha for p,sha in original.items()),'Protected pretest/older exercise changed'
    inventory=coverage(load_sources(ROOT/'output'),report_catalog(ROOT/'API_DOCUMENTATION/Pesan_eror.md'));sd=[r for r in inventory['rows'] if r['class_key'] in {'kelas1','kelas2','kelas3','kelas4'}]
    assert len(sd)==85 and all(r['shortfall']==0 for r in sd)
    sheets=contact_sheets(representatives)
    report={'schemaVersion':SCHEMA,'questions':2550,'visual':1785,'text':765,'subchapters':85,'levelSlots':255,'shortfall':0,'apiCalls':0,'confidenceMeasured':False,'classes':counts,'inventory':sd,'protectedFilesUnchanged':len(original),'mathExpressionsRendered':rendered_total,'renderErrors':0,'visualReviewCombinations':len(representatives),'contactSheets':sheets}
    atomic_json(RUN/'final_audit.json',report)
    lines=['# Bank latihan SD kelas 1–4 selesai','', '**2.550/2.550 soal (100%), sisa 0.**','', '| Kelas | Soal | Bergambar | Teks |','|---|---:|---:|---:|']
    for grade,info in counts.items():lines.append(f"| {grade} | {info['questions']} | {info['images']} | {info['text']} |")
    lines+=['','85 subbab, 255 kombinasi subbab-level; setiap level tepat 10 soal (7 gambar, 3 teks). PNG, SVG dan spesifikasi tersedia.',f'{rendered_total} ekspresi KaTeX diperiksa; 0 error. Contoh visual meliputi {len(representatives)} kombinasi kelas–level–jenis diagram.','', 'Confidence 0 berarti belum diukur. Label hasil pemeriksaan lokal Codex, bukan validasi AI independen atau kalibrasi empiris. Tidak ada API atau sinkronisasi production. Pretest dan latihan kelas 5–12 dipertahankan.','']
    (RUN/'REPORT.md').write_text('\n'.join(lines),encoding='utf-8');return report


def contact_sheets(representatives):
    """Review real output images grouped by class, level and scene kind."""
    from PIL import Image,ImageDraw,ImageFont
    from textwrap import wrap
    font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',16) if Path('C:/Windows/Fonts/arial.ttf').exists() else ImageFont.load_default(size=16)
    items=sorted(representatives.items());result=[]
    for start in range(0,len(items),16):
        image=Image.new('RGB',(1600,1320),'#edf0f3');draw=ImageDraw.Draw(image)
        for index,(key,item) in enumerate(items[start:start+16]):
            x=(index%4)*400;y=(index//4)*330
            draw.text((x+8,y+5),str(key),fill='black',font=font)
            with Image.open(item['image']) as source:
                source=source.copy();source.thumbnail((384,210));image.paste(source,(x+(400-source.width)//2,y+30))
            for j,line in enumerate(wrap(item['question'],width=46)[:4]):draw.text((x+7,y+244+j*18),line,fill='#172033',font=font)
        path=RUN/f'contact_sheet_{start//16+1:02d}.png';image.save(path);result.append(rel(path))
    atomic_json(RUN/'visual_review_samples.json',[{'class':k[0],'level':k[1],'sceneKind':k[2],**v} for k,v in items])
    return result


def refresh_owned(grade,plan,files=None):
    """Archive and rebuild only this locally owned SD run after content corrections."""
    base=base_for(grade);state=load(base/'reference_replenishment_state.json')
    manifest=base/'hasil_validasi/manifest.json'
    if manifest.exists() and load(manifest)['schemaVersion']=='codex-sd-difficulty-review-v2':
        raise ValueError('This batch has a newer difficulty review. Use review_sd_difficulty_local.py; rebuilding the initial bank would discard reviewed additions.')
    assert state['schemaVersion']==SCHEMA and state['reviewMode']=='local_without_external_api'
    assert load(base/'generation_plan.json')['planHash']==plan['planHash']
    checkpoint=base/'local_generation_checkpoint.json'
    if not checkpoint.exists():return
    current=load(checkpoint);stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
    archive=RUN/'revisions'/('kelas'+str(grade))/stamp
    assert archive.resolve().is_relative_to(RUN.resolve()) and base.resolve().is_relative_to((ROOT/'output/exercise'/('kelas'+str(grade))).resolve())
    shutil.copytree(base,archive/'batch01',ignore=shutil.ignore_patterns('.workflow.lock','.write-*.tmp'))
    for key,info in current['files'].items():
        path=(base/key).resolve();assert path.is_relative_to(base.resolve()) and re.fullmatch(r'[A-Z]_(easy|medium|hard)\.json',path.name)
        proof=resolve(info['proof']);saved=archive/'checks'/proof.name;saved.parent.mkdir(exist_ok=True);shutil.copyfile(proof,saved)
    atomic_json(archive/'refresh_journal.json',{'phase':'archived','class':grade,'questions':sum(v['questions'] for v in current['files'].values()),'planHash':plan['planHash']})
    # Never recursively delete a computed directory; retain the old publication.
    if (base/'hasil_validasi').exists():(base/'hasil_validasi').rename(archive/'previous_publication')
    selected=set(current['files']) if files is None else set(files)
    assert selected<=set(current['files'])
    for key in selected:
        (base/key).unlink();current['files'].pop(key)
    if current['files']:atomic_json(checkpoint,current)
    else:checkpoint.unlink()
    for path in [base/'soal_exercise_db.json',base/'soal_exercise_meta.json']:path.unlink(missing_ok=True)
    state.update(phase='generating',publishedQuestions=0);atomic_json(base/'reference_replenishment_state.json',state)
    atomic_json(archive/'refresh_journal.json',{'phase':'rebuilding','class':grade,'planHash':plan['planHash']})


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--pilot',action='store_true');parser.add_argument('--audit-only',action='store_true');parser.add_argument('--refresh-owned',action='store_true');parser.add_argument('--classes',nargs='+',type=int,choices=range(1,5),default=[1,2,3,4]);args=parser.parse_args();plan=prepare()
    if args.refresh_owned and (args.pilot or args.audit_only):parser.error('--refresh-owned requires a full generation run')
    if args.audit_only:print(json.dumps(audit(plan),ensure_ascii=False));return
    for grade in args.classes:
        with batch_lock(base_for(grade)):
            initialize(grade,plan)
            if args.refresh_owned:refresh_owned(grade,plan)
            jobs=[r for r in plan['catalog'] if r['class_key']=='kelas'+str(grade)]
            if args.pilot:jobs=jobs[:1]
            for job in jobs:
                for level in LEVELS:generate_file(job,level,plan)
                print(json.dumps({**progress(plan),'lastClass':grade,'lastChapter':job['chapter_no'],'lastSubchapter':job['code']}),flush=True)
            if not args.pilot:publish(grade,plan)
    if not args.pilot and len(args.classes)==4:audit(plan)


if __name__=='__main__':main()
