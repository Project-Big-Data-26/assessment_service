"""Offline, resumable authoring rounds that preserve prior exercise publications."""
from __future__ import annotations

from collections import Counter, defaultdict
from copy import deepcopy
from datetime import datetime, timezone
from functools import lru_cache
import hashlib
import importlib
import json
import math
from pathlib import Path
import random
import re
import shutil
import tempfile
import time

from app.ingestion.question_sync import coverage, load_sources, report_catalog, threshold
from app.presentation.latex import normalize_document
from .schema import ExerciseFile, Soal
from .workflow import atomic_json, batch_lock, digest, safe_asset

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / 'runs/exercise_sessions_3'
SCHEMA = 'codex-exercise-sessions-local-v3'
POLICY = 'codex-content-session-review-v3'
LEVELS = ('easy', 'medium', 'hard')
SCORES = dict(easy=600, medium=1000, hard=1400)


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))


def h(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def base_for(name):
    return ROOT / 'output/exercise' / name / 'batch01'


def grade(name):
    return int(name.split('_')[0][5:])


def provider(name):
    return importlib.import_module('app.services.exercise.session_sd' if grade(name) <= 4 else 'app.services.exercise.session_high')


def identity(question, scene):
    # A second model-based identity below rejects cosmetic wording variations.
    text = re.sub(r'\s+', ' ', question).strip().casefold()
    return h({'question': text, 'scene': scene})


def semantic_identity(model,scope=None):
    def clean(value):
        if isinstance(value,dict):
            return {k:clean(v) for k,v in value.items() if k not in {'visual_bindings','description','title','label','labels','headers','policyVersion','reviewedTask','assessment_rationale','dependent_steps','assessed_level','independent_ai_validation'}}
        if isinstance(value,list):return [clean(v) for v in value]
        return value
    return h({'location':scope,'family':model['kind'],'certificate':clean(model['certificate']),'scene':clean(model.get('scene'))})


def copy_asset(source,destination):
    """Git may convert SVG/JSON line endings; retain existing immutable bytes."""
    if not destination.exists():
        destination.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,destination);return
    if source.suffix=='.json':assert load(source)==load(destination),'Different immutable asset metadata'
    elif source.suffix=='.svg':assert source.read_text(encoding='utf-8')==destination.read_text(encoding='utf-8'),'Different immutable SVG geometry'
    else:assert source.read_bytes()==destination.read_bytes(),'Different immutable PNG pixels'


def _copy_baseline(base, destination):
    def ignore(directory, names):
        return [n for n in names if n in ('assets', '.workflow.lock') or n.startswith('.write-')]
    destination.parent.mkdir(parents=True,exist_ok=True)
    temporary=Path(tempfile.mkdtemp(prefix='.baseline-copy-',dir=destination.parent))
    shutil.copytree(base, temporary, ignore=ignore,dirs_exist_ok=True)
    atomic_json(temporary/'snapshot_complete.json',{'files':{p.relative_to(temporary).as_posix():digest(p) for p in temporary.rglob('*') if p.is_file()}})
    temporary.rename(destination)


def prepare(sessions=3):
    """Freeze one run identity; resuming never rebases against its own additions."""
    RUN.mkdir(parents=True, exist_ok=True)
    plan_path = RUN / 'plan.json'
    if plan_path.exists():
        plan = load(plan_path)
        assert plan['sessions'] == sessions, 'This round has a different session target'
        assert h({k:v for k,v in plan.items() if k != 'roundId'}) == plan['roundId']
        return plan
    catalog = report_catalog(ROOT / 'API_DOCUMENTATION/Pesan_eror.md')
    inventory = coverage(load_sources(ROOT / 'output'), catalog, sessions=sessions)
    names = sorted({r['class_key'] for r in catalog}, key=lambda n:(grade(n), '_tl' in n))
    baselines = {}
    jobs = []
    for name in names:
        base = base_for(name)
        destination = RUN / 'baseline' / name / 'batch01'
        if destination.exists():
            marker=destination/'snapshot_complete.json'
            if not marker.exists():
                retired=destination.parent/('incomplete_'+datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f'))
                assert retired.resolve().is_relative_to(RUN.resolve())
                destination.rename(retired);_copy_baseline(base,destination)
            else:
                assert all(digest(destination/p)==sha for p,sha in load(marker)['files'].items()),'Incomplete baseline snapshot'
            assert not (base/'hasil_validasi/manifest.json').exists() or digest(destination/'hasil_validasi/manifest.json') == digest(base/'hasil_validasi/manifest.json')
        else:
            _copy_baseline(base, destination)
        rows = load(destination/'hasil_validasi/validation_results.json')
        meta = load(destination/'soal_exercise_meta.json')
        active = [r for r in rows if r['status']=='active']
        counts = Counter((meta[r['_id']]['bab_id'], meta[r['_id']]['subbab_kode'], r['cognitive_level']) for r in active)
        images = Counter((meta[r['_id']]['bab_id'], meta[r['_id']]['subbab_kode'], r['cognitive_level']) for r in active if r['image_url'])
        local = []
        for row in inventory['rows']:
            if row['class_key'] != name:
                continue
            for level in LEVELS:
                matching = [k for k in counts if k[0].endswith('-B'+str(row['chapter_no'])) and k[1:]==(row['code'],level)]
                current = sum(counts[k] for k in matching)
                visual_now = sum(images[k] for k in matching)
                need = max(0, row['required']-current)
                visual = max(0, 7*sessions-visual_now) if grade(name)<=4 else 0
                text = max(0, 3*sessions-(current-visual_now)) if grade(name)<=4 else need
                local.append({**row, 'level':level, 'activeBefore':current, 'visualBefore':visual_now,
                              'needVisual':visual, 'needText':text, 'required':row['required']})
        final_count = len(active)+sum(j['needVisual']+j['needText'] for j in local)
        if grade(name)>4:
            needed_images = max(0, (3*final_count+9)//10-sum(bool(r['image_url']) for r in active))
            available = sum(j['needText'] for j in local)
            assert needed_images <= available
            exact = [needed_images*j['needText']/available if available else 0 for j in local]
            allocation = [int(v) for v in exact]
            for i in sorted(range(len(local)), key=lambda i:(-(exact[i]-allocation[i]),i))[:needed_images-sum(allocation)]:
                allocation[i] += 1
            for j,n in zip(local,allocation):
                j['needVisual']=n; j['needText']-=n
        old_assets = {p.relative_to(base).as_posix():digest(p) for p in (base/'assets').glob('*') if p.is_file()}
        baselines[name] = {'manifestHash':digest(destination/'hasil_validasi/manifest.json'), 'oldAssets':old_assets,
                           'active':len(active), 'questions':len(rows)}
        jobs.extend(local)
    protected = {p.relative_to(ROOT).as_posix():digest(p) for p in (ROOT/'output/pretest').rglob('*') if p.is_file() and p.name!='.workflow.lock' and not p.name.endswith('.tmp')}
    atomic_json(RUN/'protected_pretest.json',protected)
    plan = {'schemaVersion':SCHEMA, 'policyVersion':POLICY, 'sessions':sessions, 'catalog':catalog,
            'classes':names, 'baselines':baselines, 'jobs':jobs, 'apiCalls':0,
            'initialShortfall':sum(j['needVisual']+j['needText'] for j in jobs),
            'newVisualMinimum':sum(j['needVisual'] for j in jobs)}
    plan['roundId']=h(plan); atomic_json(plan_path,plan)
    return plan


def references(name, plan):
    path = RUN / 'references' / (name+'.json')
    if path.exists():
        return load(path), path
    base = RUN / 'baseline' / name / 'batch01'
    rows = load(base/'hasil_validasi/validation_results.json'); meta=load(base/'soal_exercise_meta.json')
    result = defaultdict(list)
    if grade(name)<=4:
        from scripts.generate_sd_bank_local import reference_pool
        refs=load(base/'reference_blueprints.json')['references']
        for job in plan['catalog']:
            if job['class_key']!=name:continue
            pool,adapted=reference_pool(job,refs)
            result[f"{job['chapter_no']}_{job['code']}"]=[{**r,'sourceKind':'pretest_validated','conceptAdaptation':adapted} for r in pool]
    else:
        for row in rows:
            if row['status']!='active':continue
            m=meta[row['_id']];bab=int(m['bab_id'].split('-B')[1]);correct=next(o['text'] for o in row['options'] if o['option_id']==row['jawaban'])
            result[f"{bab}_{m['subbab_kode']}"] .append({'id':row['_id'],'class':name,'chapter':bab,'code':m['subbab_kode'],
                'text':row['soal_text'],'answer':correct,'sourceKind':'exercise_validated','conceptAdaptation':False})
    assert all(result[f"{j['chapter_no']}_{j['code']}"] for j in plan['jobs'] if j['class_key']==name)
    atomic_json(path,dict(result));return dict(result),path


def _decision(module,model,g):
    result=module.assess(model,g)
    if isinstance(result,str):result={'assessedLevel':result}
    if 'assessedLevel' not in result and 'level' in result:result['assessedLevel']=result['level']
    result.setdefault('reason',model.get('rationale','Penilaian isi dan solusi minimum.'))
    result.setdefault('steps',model.get('steps',1));result.setdefault('apiCalls',0)
    assert result['apiCalls']==0
    return result


@lru_cache(maxsize=40000)
def _review_cached(name,encoded):
    from scripts.generate_sd_bank_local import answer_identity
    from .replenishment_math import m
    module=provider(name);model=json.loads(encoded)
    value=module.solve(model['certificate'])
    answer=m(value) if not isinstance(value,str) else value
    assert answer_identity(answer)==answer_identity(model['answer']), ('Answer disagreement',model['kind'],answer,model['answer'])
    assert len(model['wrong'])==3 and len({answer_identity(v) for v in [model['answer'],*model['wrong']]})==4
    decision=_decision(module,model,grade(name))
    assert decision['assessedLevel'] in LEVELS
    visual=module.check_visual(model) if model.get('scene') else {'status':'text_question'}
    assert visual is not False
    return {'assessment':decision,'exactValue':str(value),'visualCheck':visual or {'status':'local_semantic_counterfactual_pass'},'apiCalls':0}


def review_model(name,model):
    return deepcopy(_review_cached(name,json.dumps(model,sort_keys=True,ensure_ascii=False)))


def _reason(wrong,answer):
    from scripts.generate_sd_bank_local import answer_identity
    a=answer_identity(answer);w=answer_identity(wrong)
    if a.startswith('number:') and w.startswith('number:'):
        import sympy as s
        x=s.sympify(a[7:]);y=s.sympify(w[7:])
        if y==-x:return 'Tanda hasil dibalik, sehingga tidak sesuai arah atau operasi yang diminta.'
        if x!=0 and y==2*x:return 'Hasil dihitung dua kali, padahal bagian tersebut hanya digunakan sekali.'
        if x!=0 and y==x/2:return 'Mengambil setengah hasil, padahal soal meminta seluruh kuantitas.'
        if 0<x<1 and y==1-x:return 'Menggunakan bagian komplemen, bukan bagian yang ditanyakan.'
        return f'Perhitungan pada pilihan ini berselisih {abs(y-x)} dari hasil yang memenuhi data. Gunakan seluruh syarat pada pembahasan.'
    return 'Pilihan ini tidak memenuhi hubungan dan syarat yang ditanyakan; periksa langkah pada pembahasan.'


def make_candidate(name,job,model,review,serial,r,reference,reference_path,stage):
    from .visual_assets import render
    level=review['assessment']['assessedLevel'];work=f"{name}-b{job['chapter_no']:02d}-{job['code'].lower()}-{job['level']}-bt01-{serial:03d}"
    q={'tipe_generate':'variasi','variasi_cara':'angka' if serial%2 else 'konteks',
       'acuan':{'sumber':reference['sourceKind'],'id':reference['id'],'teks':reference['text'],'jawaban':reference['answer'],
                'snapshot':reference_path.relative_to(ROOT).as_posix(),'source_sha256':digest(reference_path)},
       'cognitive_c':{'easy':'C2','medium':'C3','hard':'C4'}[level],'jumlah_langkah':min(8,max(1,review['assessment']['steps'])),
       'jenis_soal':model['kind'][:60],'alasan_level':review['assessment']['reason'],'stimulus':None,
       'pertanyaan':model['question'],'jawaban_benar':model['answer'],'alasan_benar':model['explanation'],
       'distraktor':[{'teks':w,'alasan':(model.get('wrong_reasons') or [_reason(v,model['answer']) for v in model['wrong']])[i]} for i,w in enumerate(model['wrong'])],
       'pembahasan':model['explanation'],'catatan':'Variasi putaran tiga sesi; penilaian lokal Codex tanpa API; confidence belum diukur.','id':work}
    asset=None;provenance={}
    if model.get('scene'):
        spec={'kind':model.get('visual_kind','sd_scene'),'scene':model['scene']}
        asset,provenance=render(spec,stage)
        q.update(gambar=['exercise_assets/'+name+'/batch01/'+asset],visual_spec=spec,
                 deskripsi_gambar='Fakta pada gambar: '+json.dumps(model['scene'],ensure_ascii=False))
    Soal.model_validate(q)
    options=[{'text':q['jawaban_benar'],'alasan':'Benar: '+q['alasan_benar']},*[{'text':v['teks'],'alasan':'Salah: '+v['alasan']} for v in q['distraktor']]]
    r.shuffle(options)
    for option,letter in zip(options,'ABCD'):option['option_id']=letter
    now=datetime.now(timezone.utc).isoformat();qid=hashlib.md5(work.encode()).hexdigest()[:24]
    row={'_id':qid,'berkas_id':None,'kelas_id':name,'subbab_id':job['name'],'soal_text':q['pertanyaan'],
         'image_url':[asset] if asset else [],'soal_type':'Pilihan Ganda','options':options,'jawaban':next(v['option_id'] for v in options if v['text']==q['jawaban_benar']),
         'matching_pairs':None,'cognitive_level':None,'cognitive_score':None,'confidence_score':None,'status':'inactive','created_at':now,'updated_at':now}
    return {'question':q,'source':row,'model':model,'review':review,'visualProvenance':provenance,
            'referenceOrigin':{k:reference[k] for k in ('class','chapter','code','conceptAdaptation')},'job':job}


def progress(plan,phase=None,last=None):
    counts={};complete=0;candidate=0;images=0
    for name in plan['classes']:
        ck=RUN/'staging'/name/'checkpoint.json';state=load(ck) if ck.exists() else {'jobs':{}}
        n=sum(v['count'] for v in state['jobs'].values());v=sum(v['visual'] for v in state['jobs'].values())
        pub=base_for(name)/'hasil_validasi/manifest.json';published=pub.exists() and load(pub).get('roundId')==plan['roundId']
        counts[name]={'candidates':n,'images':v,'published':published};candidate+=n;images+=v;complete+=n if published else 0
    result={'roundId':plan['roundId'],'phase':phase,'last':last,'candidateQuestions':candidate,'publishedAdditions':complete,
            'targetAdditions':plan['initialShortfall'],'percent':round(min(100,100*candidate/max(1,plan['initialShortfall'])),2),
            'remaining':max(0,plan['initialShortfall']-candidate),'visual':images,'text':candidate-images,'classes':counts,'apiCalls':0}
    atomic_json(RUN/'progress.json',result);print(json.dumps(result,ensure_ascii=False),flush=True)
    return result


def generate_class(name,plan,pilot=False):
    base=base_for(name);stage=RUN/'staging'/name;stage.mkdir(parents=True,exist_ok=True)
    state_path=stage/'checkpoint.json'
    with batch_lock(base):
        recover(name)
        final=base/'hasil_validasi'
        if load(final/'manifest.json').get('roundId')==plan['roundId']:
            verify_publication(final);return {'alreadyPublished':True}
        assert digest(final/'manifest.json')==plan['baselines'][name]['manifestHash'],'Live baseline changed before publication'
        state=load(state_path) if state_path.exists() else {'roundId':plan['roundId'],'jobs':{}}
        assert state['roundId']==plan['roundId']
        jobs=[j for j in plan['jobs'] if j['class_key']==name]
        if pilot:jobs=[j for j in jobs if (j['chapter_no'],j['code'])==(jobs[0]['chapter_no'],jobs[0]['code'])]
        refs,refpath=references(name,plan)
        identities=set();semantics=set();old_raw={}
        for path in base.glob('bab*/*_*.json'):
            if not re.fullmatch(r'[A-Z]_(easy|medium|hard)\.json',path.name):continue
            raw=load(path);old_raw[path.relative_to(base).as_posix()]=raw
            identities.update(identity(q['pertanyaan'],(q.get('visual_spec') or {}).get('scene')) for q in raw['soal'])
        old_meta=load(base/'soal_exercise_meta.json')
        for info in old_meta.values():
            cert=info.get('local_math_check',{})
            if isinstance(cert,dict) and cert.get('type'):
                semantics.add(semantic_identity({'kind':info['jenis_soal'],'certificate':cert,'scene':(info.get('visual_spec') or {}).get('scene')},
                    (int(info['bab_id'].split('-B')[1]),info['subbab_kode'])))
        invalidated=[]
        _review_cached.cache_clear()
        for key,info in list(state['jobs'].items()):
            path=stage/info['file'];assert digest(path)==info['sha256']
            saved=load(path)['items'];seen=set();valid=True
            for c in saved:
                try:
                    fresh=review_model(name,c['model']);semantic=semantic_identity(c['model'],(c['job']['chapter_no'],c['job']['code']))
                    if fresh['assessment']['assessedLevel']!=c['job']['level'] or semantic in semantics or semantic in seen:
                        valid=False;break
                    seen.add(semantic)
                except (AssertionError,ValueError,KeyError,TypeError,ZeroDivisionError):valid=False;break
            if not valid:
                archive=RUN/'revisions'/name/(key+'_'+info['sha256'][:16]+'.json');archive.parent.mkdir(parents=True,exist_ok=True)
                if not archive.exists():shutil.copyfile(path,archive)
                invalidated.append(key);state['jobs'].pop(key)
                continue
            identities.update(identity(c['model']['question'],c['model'].get('scene')) for c in saved)
            semantics.update(seen)
        if invalidated:
            atomic_json(state_path,state);atomic_json(stage/'invalidated_jobs.json',{'jobs':invalidated,'reason':'Reassessment or substantive-duplicate check changed; regenerated in this round only.'})
        last_report=time.monotonic();module=provider(name)
        for job in jobs:
            key=f"{job['chapter_no']:02d}_{job['code']}_{job['level']}"
            if key in state['jobs']:continue
            filename=f"bab{job['chapter_no']:02d}/{job['code']}_{job['level']}.json"
            raw=old_raw.get(filename,{'soal':[]});last=max((int(q['id'].rsplit('-',1)[1].lstrip('g')) for q in raw['soal']),default=0)
            accepted=[];rejected=Counter();pool=refs[f"{job['chapter_no']}_{job['code']}"]
            for ordinal,visual in enumerate([True]*job['needVisual']+[False]*job['needText'],1):
                seed=plan['roundId']+name+key+str(ordinal)
                rng=random.Random(int(hashlib.sha256(seed.encode()).hexdigest()[:16],16))
                for trial in range(3000):
                    if time.monotonic()-last_report>=30:
                        progress(plan,'generating',{'class':name,'job':key,'acceptedInJob':len(accepted),'remainingInJob':job['needVisual']+job['needText']-len(accepted)})
                        last_report=time.monotonic()
                    try:
                        model=module.generate(name,job['chapter_no'],job['code'],job['level'],rng,visual,last+ordinal)
                        if model is None:rejected['unsupported_instance']+=1;continue
                        model=deepcopy(model)
                        for field in ('question','answer','wrong','explanation','rationale','wrong_reasons'):
                            if field in model:model[field]=normalize_document(model[field])
                        if bool(model.get('scene'))!=visual:rejected['wrong_modality']+=1;continue
                        ident=identity(model['question'],model.get('scene'))
                        semantic=semantic_identity(model,(job['chapter_no'],job['code']))
                        if ident in identities or semantic in semantics:rejected['duplicate']+=1;continue
                        review=review_model(name,model)
                        if review['assessment']['assessedLevel']!=job['level']:rejected['different_actual_level']+=1;continue
                        candidate=make_candidate(name,job,model,review,last+ordinal,rng,pool[(ordinal-1)%len(pool)],refpath,stage)
                        break
                    except (AssertionError,ValueError,ZeroDivisionError,KeyError,TypeError) as exc:
                        rejected[type(exc).__name__+':'+str(exc)[:180]]+=1
                else:
                    atomic_json(stage/'capacity_failure.json',{'job':job,'ordinal':ordinal,'visual':visual,'rejected':dict(rejected)})
                    raise ValueError('Meaningful variation capacity exhausted: '+name+' '+key+' '+str(visual)+' '+str(dict(rejected)))
                accepted.append(candidate);identities.add(ident);semantics.add(semantic)
            out=stage/'jobs'/(key+'.json');atomic_json(out,{'items':accepted,'job':job,'roundId':plan['roundId'],'rejected':dict(rejected)})
            state['jobs'][key]={'file':out.relative_to(stage).as_posix(),'sha256':digest(out),'count':len(accepted),'visual':sum(bool(c['model'].get('scene')) for c in accepted),
                               'providerCodeHash':digest(Path(module.__file__)) if getattr(module,'__file__',None) else None}
            atomic_json(state_path,state)
            progress(plan,'generating',{'class':name,'chapter':job['chapter_no'],'subchapter':job['code'],'level':job['level']})
            last_report=time.monotonic()
    if not pilot:return publish_class(name,plan)
    return {'pilot':True,'class':name,'candidateQuestions':sum(v['count'] for v in state['jobs'].values())}


def _bab_id(name,bab):
    g=grade(name);prefix='SD' if g<=6 else 'SMP' if g<=9 else 'SMA'
    track=('L' if name.endswith('_tl') else 'U') if g>=11 else ''
    return f'{prefix}{g}{track}-B{bab}'


def recover(name):
    """Recover a process interrupted between raw writes and canonical rename."""
    stage=RUN/'staging'/name;journal=stage/'publication_journal.json'
    if not journal.exists() or load(journal)['phase']!='prepared':return
    info=load(journal);base=base_for(name);baseline=RUN/'baseline'/name/'batch01'
    old=RUN/'publication_backups'/name;final=base/'hasil_validasi'
    if old.exists():
        if final.exists():
            failed=stage/('interrupted_publication_'+datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S%f'))
            final.rename(failed)
        old.rename(final)
    for relative in info['mutated']:
        dest=(base/relative).resolve();assert dest.is_relative_to(base.resolve())
        saved=baseline/relative
        if saved.exists():dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(saved,dest)
        else:dest.unlink(missing_ok=True)
    atomic_json(journal,{**info,'phase':'rolled_back'})


def publish_class(name,plan):
    from scripts.generate_sd_bank_local import check_latex
    base=base_for(name);stage=RUN/'staging'/name;baseline=RUN/'baseline'/name/'batch01';final=base/'hasil_validasi'
    with batch_lock(base):
        recover(name)
        if load(final/'manifest.json').get('roundId')==plan['roundId']:
            verify_publication(final);return load(final/'manifest.json')['summary']
        assert digest(final/'manifest.json')==plan['baselines'][name]['manifestHash']
        state=load(stage/'checkpoint.json');jobs=[j for j in plan['jobs'] if j['class_key']==name]
        assert len(state['jobs'])==len(jobs),'The full class must be generated before publication'
        candidates=[]
        for key,info in state['jobs'].items():
            assert digest(stage/info['file'])==info['sha256'];candidates.extend(load(stage/info['file'])['items'])
        # Recompute, rather than reuse generation's cached content decisions.
        _review_cached.cache_clear()
        for c in candidates:
            fresh=review_model(name,c['model']);assert fresh['assessment']['assessedLevel']==c['review']['assessment']['assessedLevel']
            if c['source']['image_url']:
                asset=base/c['source']['image_url'][0]
                if asset.exists():
                    c['visualProvenance']={**c['visualProvenance'],'svgSha256':digest(asset.with_suffix('.svg')),
                        'retainedAssetMetadataSha256':digest(asset.with_suffix('.json')),'retainedExistingAsset':True}
        raw_files={p.relative_to(baseline).as_posix():load(p) for p in baseline.glob('bab*/*_*.json') if re.fullmatch(r'[A-Z]_(easy|medium|hard)\.json',p.name)}
        previous_raw=deepcopy(raw_files)
        master=load(baseline/'soal_exercise_db.json');source_meta=load(baseline/'soal_exercise_meta.json')
        old_rows=load(baseline/'hasil_validasi/validation_results.json');old_meta=load(baseline/'hasil_validasi/validation_results_meta.json')
        rows=deepcopy(old_rows);meta=deepcopy(old_meta);proofs=[]
        for c in candidates:
            job=c['job'];q=c['question'];source=c['source'];qid=source['_id'];review=c['review'];level=review['assessment']['assessedLevel']
            assert qid not in source_meta
            filename=f"bab{job['chapter_no']:02d}/{job['code']}_{job['level']}.json"
            raw=raw_files.setdefault(filename,{'book':name,'bab_no':job['chapter_no'],'subbab':job['code'],'level':job['level'],'batch':1,'skill_versi':'v1','soal':[]})
            raw['soal'].append(q);master['items'].append(source)
            info={'id':q['id'],'batch':1,'bab_id':_bab_id(name,job['chapter_no']),'subbab_kode':job['code'],'level_target':job['level'],
                  'cognitive_score_target':SCORES[job['level']],'tipe_generate':q['tipe_generate'],'variasi_cara':q['variasi_cara'],
                  'acuan':q['acuan'],'cognitive_c':q['cognitive_c'],'jumlah_langkah':q['jumlah_langkah'],'jenis_soal':q['jenis_soal'],
                  'pembahasan':q['pembahasan'],'alasan_level':q['alasan_level'],'generator':'codex:session-expansion-v3','skill_versi':'v1',
                  'bergambar':bool(q.get('gambar')),'gambar':q.get('gambar',[]),'visual_spec':q.get('visual_spec'),
                  'visual_provenance':c['visualProvenance'],'local_math_check':c['model']['certificate'],
                  'sourceAdaptation':c['referenceOrigin'],'roundId':plan['roundId'],'dipaksa_kuota':False}
            source_meta[qid]=info
            published={**source,'cognitive_level':level,'cognitive_score':SCORES[level],'confidence_score':0,'status':'active'}
            record={'questionId':qid,'workingId':q['id'],'model':c['model'],'review':review,'rawHash':h(q),'sourceHash':h(source),'publishedHash':h(published),
                    'visualProvenance':c['visualProvenance'],'apiCalls':0}
            meta[qid]={**deepcopy(info),'local_review':record,'validasi':{'cognitive_level':level,'cognitive_score':SCORES[level],'confidence_score':0,
                'status':'active','validation_status':'codex_local_review_pass','validation_provider':'codex_direct_review','validation_model':None,
                'api_runs':0,'requested_runs':0,'local_review_passes':1,'confidence_status':'not_measured','confidence_available':False,
                'consistency_measured':False,'training_evidence_qualified':False,'full_complete':True,'validation_method':'codex_local_review',
                'label_provenance':'codex_local_assessment','level_sesuai_target':level==job['level'],'review_policy':POLICY,
                'answer_key_status':'verified_locally','source_hash':h(source),'assessment_reason':review['assessment']['reason']}}
            rows.append(published);proofs.append(record)
        for raw in raw_files.values():ExerciseFile.model_validate(raw)
        rendered=check_latex([c['question'] for c in candidates],RUN/('latex_'+name+'.json'))
        atomic_json(RUN/('render_'+name+'.json'),rendered)
        publication=Path(tempfile.mkdtemp(prefix='.session-publication-',dir=base));shutil.copytree(final,publication,dirs_exist_ok=True)
        prior=publication/'bukti_validasi/previous_session_round'
        atomic_json(prior/'validation_results.json',old_rows);atomic_json(prior/'validation_results_meta.json',old_meta)
        atomic_json(prior/'source.json',load(baseline/'soal_exercise_db.json'));atomic_json(prior/'source_meta.json',load(baseline/'soal_exercise_meta.json'))
        atomic_json(prior/'raw.json',previous_raw);shutil.copyfile(baseline/'hasil_validasi/manifest.json',prior/'manifest.json')
        atomic_json(publication/'validation_results.json',rows);atomic_json(publication/'validation_results_meta.json',meta)
        atomic_json(publication/'bukti_validasi/codex_session_review.json',{'policyVersion':POLICY,'roundId':plan['roundId'],'apiCalls':0,'items':proofs})
        assets={}
        for row in rows:
            if row['status']!='active':continue
            for asset in row['image_url']:
                rec=assets.setdefault(asset,{'asset':asset,'questionIds':[],'status':'verified_locally','independentVisionValidation':False})
                rec['questionIds'].append(row['_id'])
        atomic_json(publication/'bukti_validasi/session_assets_validation.json',{'apiCalls':0,'items':assets})
        levels=dict(Counter(r['cognitive_level'] for r in rows if r['status']=='active'))
        summary={'class':name,'added':len(candidates),'active':sum(r['status']=='active' for r in rows),'inactive':sum(r['status']!='active' for r in rows),
                 'levels':levels,'activeVisual':sum(r['status']=='active' and bool(r['image_url']) for r in rows),'sessions':plan['sessions'],'apiCalls':0,'rendering':rendered}
        text=f'# Latihan {name}: tiga sesi\n\nTambahan {len(candidates)} soal; aktif {summary["active"]}. Target setiap subbab-level: {threshold(name)*plan["sessions"]} soal aktif.\n\nConfidence 0: belum diukur. Label penilaian lokal Codex, bukan validasi AI independen atau kalibrasi empiris. Tanpa API dan tanpa sinkronisasi production. Soal, label lama dan pretest dipertahankan.\n'
        for filename in ('README.md','RINGKASAN_VALIDASI.md','LAPORAN_VALIDASI.md'):(publication/filename).write_text(text,encoding='utf-8')
        code=publication/'bukti_validasi/reviewed_session_code'
        files=[Path(__file__),ROOT/'scripts/extend_exercise_sessions_local.py',*sorted((ROOT/'app/services/exercise').glob('session_*.py')),ROOT/'app/services/exercise/math_scene_visuals.py']
        for p in set(files):
            if p.exists() and p.is_relative_to(ROOT):
                dest=code/p.relative_to(ROOT);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
        # Assets are immutable: publishing new addresses cannot invalidate old ones.
        for src in (stage/'assets').glob('*'):
            copy_asset(src,base/'assets'/src.name)
        mutated=[*raw_files,'soal_exercise_db.json','soal_exercise_meta.json','reference_replenishment_state.json']
        journal=stage/'publication_journal.json';atomic_json(journal,{'phase':'prepared','mutated':mutated,'roundId':plan['roundId']})
        old=RUN/'publication_backups'/name;old.parent.mkdir(parents=True,exist_ok=True);assert not old.exists()
        try:
            for relative,raw in raw_files.items():atomic_json(base/relative,raw)
            atomic_json(base/'soal_exercise_db.json',master);atomic_json(base/'soal_exercise_meta.json',source_meta)
            state=load(baseline/'reference_replenishment_state.json');state.update(reviewMode='local_without_external_api',validationOwner='codex_local_review',phase='local_review_complete',publishedQuestions=len(rows),sessionRound=plan['roundId'],targetSessions=plan['sessions'])
            atomic_json(base/'reference_replenishment_state.json',state)
            inputs={p.relative_to(base).as_posix():digest(p) for p in [base/'soal_exercise_db.json',base/'soal_exercise_meta.json',*[base/p for p in raw_files],*sorted((base/'assets').glob('*'))] if p.is_file()}
            manifest={'schemaVersion':SCHEMA,'policyVersion':POLICY,'roundId':plan['roundId'],'class':name,'sessions':plan['sessions'],
                      'catalog':[r for r in plan['catalog'] if r['class_key']==name],
                      'summary':summary,'inputs':inputs,'oldAssets':plan['baselines'][name]['oldAssets'],
                      'outputs':{p.relative_to(publication).as_posix():digest(p) for p in publication.rglob('*') if p.is_file() and p!=publication/'manifest.json'}}
            atomic_json(publication/'manifest.json',manifest);verify_publication(publication)
            final.rename(old);publication.rename(final);verify_publication(final)
            atomic_json(journal,{'phase':'committed','roundId':plan['roundId'],'summary':summary})
        except BaseException:
            recover(name);raise
        progress(plan,'published',summary)
        return summary


def verify_publication(bundle):
    bundle=Path(bundle);base=bundle.parent;manifest=load(bundle/'manifest.json');assert manifest['schemaVersion']==SCHEMA
    for relative,sha in manifest['outputs'].items():assert digest(bundle/relative)==sha,('Output hash',relative)
    for relative,sha in manifest['inputs'].items():assert digest(base/relative)==sha,('Input hash',relative)
    for relative,sha in manifest['oldAssets'].items():assert digest(base/relative)==sha,('Old asset changed',relative)
    prior=bundle/'bukti_validasi/previous_session_round'
    old=load(prior/'validation_results.json');old_meta=load(prior/'validation_results_meta.json')
    old_source=load(prior/'source.json')['items'];old_source_meta=load(prior/'source_meta.json')
    rows=load(bundle/'validation_results.json');meta=load(bundle/'validation_results_meta.json')
    source=load(base/'soal_exercise_db.json')['items'];source_meta=load(base/'soal_exercise_meta.json')
    assert len(rows)==len(source) and len({r['_id'] for r in rows})==len(rows)
    assert [r['_id'] for r in rows]==[r['_id'] for r in source] and set(meta)==set(source_meta)=={r['_id'] for r in rows}
    by={r['_id']:r for r in rows};sources={r['_id']:r for r in source}
    for row in old:assert by[row['_id']]==row and meta[row['_id']]==old_meta[row['_id']],'Existing publication changed'
    for row in old_source:assert sources[row['_id']]==row and source_meta[row['_id']]==old_source_meta[row['_id']],'Existing source changed'
    raw_by={}
    for path in base.glob('bab*/*_*.json'):
        if not re.fullmatch(r'[A-Z]_(easy|medium|hard)\.json',path.name):continue
        raw=load(path);ExerciseFile.model_validate(raw)
        for q in raw['soal']:assert q['id'] not in raw_by;raw_by[q['id']]=q
    for relative,original in load(prior/'raw.json').items():
        current=load(base/relative)
        assert {k:v for k,v in current.items() if k!='soal'}=={k:v for k,v in original.items() if k!='soal'}
        assert current['soal'][:len(original['soal'])]==original['soal'],'Original raw question changed'
    proof=load(bundle/'bukti_validasi/codex_session_review.json');new={r['questionId']:r for r in proof['items']}
    assert len(new)==len(proof['items']) and set(new)==set(by)-{r['_id'] for r in old}
    assert proof['apiCalls']==0 and proof['policyVersion']==POLICY
    for qid,item in new.items():
        row=by[qid];info=meta[qid];q=raw_by[item['workingId']]
        assert h(q)==item['rawHash'] and h(row)==item['publishedHash'] and h(sources[qid])==item['sourceHash']
        checked=review_model(manifest['class'],item['model']);level=checked['assessment']['assessedLevel']
        assert row['cognitive_level']==level and row['cognitive_score']==SCORES[level] and row['status']=='active' and row['confidence_score']==0
        assert q['pertanyaan']==row['soal_text']==item['model']['question']
        from scripts.generate_sd_bank_local import answer_identity
        assert answer_identity(q['jawaban_benar'])==answer_identity(item['model']['answer'])
        expected_options={answer_identity(v) for v in [q['jawaban_benar'],*[d['teks'] for d in q['distraktor']]]}
        assert expected_options=={answer_identity(v) for v in [item['model']['answer'],*item['model']['wrong']]}
        assert expected_options=={answer_identity(o['text']) for o in row['options']}
        assert len(expected_options)==4 and answer_identity(next(o['text'] for o in row['options'] if o['option_id']==row['jawaban']))==answer_identity(q['jawaban_benar'])
        assert q['pembahasan']==q['alasan_benar']==item['model']['explanation']
        assert info['validasi']['api_runs']==0 and info['validasi']['training_evidence_qualified'] is False
        assert sources[qid]['status']=='inactive' and sources[qid]['cognitive_level'] is None
        for asset in row['image_url']:
            assert digest(safe_asset(base,asset))==item['visualProvenance']['pngSha256']
    sessions=manifest['sessions'];name=manifest['class'];counts=Counter();visual=Counter()
    for row in rows:
        if row['status']=='active':
            key=(source_meta[row['_id']]['bab_id'],source_meta[row['_id']]['subbab_kode'],row['cognitive_level'])
            counts[key]+=1;visual[key]+=bool(row['image_url'])
    expected={(_bab_id(name,j['chapter_no']),j['code'],level) for j in manifest['catalog'] for level in LEVELS}
    assert set(counts)==expected and all(n>=threshold(name)*sessions for n in counts.values())
    if grade(name)<=4:assert all(visual[k]>=7*sessions and counts[k]-visual[k]>=3*sessions for k in counts)
    else:assert sum(visual.values())*10>=sum(counts.values())*3
    assert load(base/'reference_replenishment_state.json')['reviewMode']=='local_without_external_api'
    return manifest['summary']


def audit(plan):
    from PIL import Image
    from app.ingestion.question_sync import class_from_chapter
    summaries=[];assignments={};all_ids=set();new_pictures=0
    for name in plan['classes']:
        base=base_for(name);final=base/'hasil_validasi'
        summary=verify_publication(final);summaries.append(summary)
        rows=load(final/'validation_results.json');meta=load(base/'soal_exercise_meta.json')
        grouped=defaultdict(list)
        for row in rows:
            assert row['_id'] not in all_ids;all_ids.add(row['_id'])
            if row['status']!='active':continue
            info=meta[row['_id']];owner,bab=class_from_chapter(info['bab_id']);assert owner==name
            grouped[(bab,info['subbab_kode'],row['cognitive_level'])].append(row)
            for ref in row['image_url']:
                with Image.open(safe_asset(base,ref)) as image:image.verify()
        known={(r['chapter_no'],r['code'],level) for r in plan['catalog'] if r['class_key']==name for level in LEVELS}
        assert set(grouped)==known
        for (bab,code,level),items in grouped.items():
            pics=sorted((r['_id'] for r in items if r['image_url']));text=sorted(r['_id'] for r in items if not r['image_url'])
            n=threshold(name)
            if grade(name)<=4:
                sessions=[pics[i*7:(i+1)*7]+text[i*3:(i+1)*3] for i in range(plan['sessions'])]
            else:
                order=[]
                # Evenly distribute visuals without changing the final class quota.
                while pics or text:
                    if pics:order.append(pics.pop(0))
                    if text:order.append(text.pop(0))
                    if text:order.append(text.pop(0))
                sessions=[order[i*n:(i+1)*n] for i in range(plan['sessions'])]
            assert all(len(s)==n for s in sessions) and len(set(q for s in sessions for q in s))==n*plan['sessions']
            assignments[f'{name}/{bab:02d}/{code}/{level}']=sessions
        new_pictures+=sum(bool(item['model'].get('scene')) for item in load(final/'bukti_validasi/codex_session_review.json')['items'])
        print(json.dumps({'phase':'audit','class':name,**summary}),flush=True)
    inventory=coverage(load_sources(ROOT/'output'),plan['catalog'],sessions=plan['sessions'])
    assert inventory['under_threshold_levels']==0 and inventory['under_threshold']==0
    frozen=load(RUN/'protected_pretest.json');assert all(digest(ROOT/path)==sha for path,sha in frozen.items()),'Pretest changed'
    result={'schemaVersion':SCHEMA,'roundId':plan['roundId'],'sessions':plan['sessions'],'apiCalls':0,
            'added':sum(c['added'] for c in summaries),'active':sum(c['active'] for c in summaries),'inactive':sum(c['inactive'] for c in summaries),
            'activeVisual':sum(c['activeVisual'] for c in summaries),'newVisual':new_pictures,'shortfall':inventory['shortfall_questions'],
            'subchapters':len(plan['catalog']),'levelSlots':len(assignments),'classes':summaries,'coverage':inventory,
            'mathExpressionsRendered':sum(c['rendering']['checked'] for c in summaries),'renderErrors':0,'pretestFilesUnchanged':len(frozen)}
    atomic_json(RUN/'session_assignments.json',assignments);atomic_json(RUN/'final_audit.json',result)
    lines=['# Tiga sesi latihan seluruh kelas','',f'**{result["active"]:,} soal aktif; tambahan {result["added"]:,}; kekurangan {result["shortfall"]}.**','',
           '| Kelas | Easy | Medium | Hard | Aktif | Bergambar | Tambahan |','|---|---:|---:|---:|---:|---:|---:|']
    for c in summaries:lines.append(f'| {c["class"]} | {c["levels"].get("easy",0)} | {c["levels"].get("medium",0)} | {c["levels"].get("hard",0)} | {c["active"]} | {c["activeVisual"]} | {c["added"]} |')
    lines+=['',f'{len(assignments)} kombinasi subbab-level memenuhi tiga sesi tanpa ID berulang; SD 10, SMP 15, SMA/TL 20 soal per sesi.',
            'Kelas 1–4 memiliki minimal 21 gambar dan 9 teks pada setiap subbab-level. Kelas 5–12/TL minimal 30% gambar pada stok aktif tiap kelas.',
            f'KaTeX: {result["mathExpressionsRendered"]} ekspresi, 0 error. PNG dapat dibuka. Soal lama, penilaiannya, dan pretest dipertahankan.',
            'Confidence 0 berarti belum diukur; label hasil penilaian lokal Codex, bukan validasi AI independen atau kalibrasi empiris. API calls 0; production tidak disinkronkan.','']
    (RUN/'REPORT.md').write_text('\n'.join(lines),encoding='utf-8')
    return result
