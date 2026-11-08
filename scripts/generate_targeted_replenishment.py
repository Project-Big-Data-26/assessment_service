"""Append certified, difficulty-specific questions to existing batch01 files."""
import argparse
from collections import Counter
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.services.exercise.workflow import atomic_json,batch_lock
from app.services.exercise.schema import ExerciseFile,Soal
from app.services.exercise.replenishment_format import standard_question
from app.services.exercise.targeted_math import solve_certificate
from scripts.review_replenishment_local import verify_local_publication

RUN=ROOT/'runs/exercise_replenishment/codex_batch01/local_review'
SCHEMA='codex-targeted-exercise-publication-v2'


def load(path):return json.loads(Path(path).read_text(encoding='utf-8-sig'))
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def h(value):return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False).encode()).hexdigest()


def save_progress(path,name,result,target):
    # Merge under a separate lock: classes can finish concurrently.
    with batch_lock(RUN):
        progress=load(path) if path.exists() else {'target':target,'classes':{},'apiCalls':0}
        progress['classes'][name]=result
        progress['completed']=sum(v['added'] for v in progress['classes'].values() if v['status']=='complete')
        atomic_json(path,progress)
        return progress


def factory(name,bab,code,level,r):
    if name=='kelas12_tl':
        from app.services.exercise.targeted_tl12 import generate
    elif name.endswith('_tl'):
        from app.services.exercise.targeted_tl11 import generate
    elif int(name[5:])>=10:
        from app.services.exercise.targeted_sma import generate
        return generate(int(name[5:]),bab,code,level,r)
    elif int(name[5:])>=7:
        from app.services.exercise.targeted_smp import generate
        return generate(int(name[5:]),bab,code,level,r)
    else:
        from app.services.exercise.targeted_sd import generate
        return generate(int(name[5:]),bab,code,level,r)
    return generate(bab,code,level,r)


def verify(bundle,check_live=True):
    bundle=Path(bundle);manifest=load(bundle/'manifest.json')
    if manifest['schemaVersion']=='codex-exercise-sessions-local-v3':
        from app.services.exercise.session_expansion import verify_publication
        return verify_publication(bundle)
    assert manifest['schemaVersion']==SCHEMA
    for info in manifest['sourceFiles'].values():assert digest(info['path'])==info['sha256']
    for name,info in manifest['outputs'].items():assert digest(bundle/name)==info['sha256']
    if check_live:
        for info in manifest['liveInputs'].values():assert digest(info['path'])==info['sha256']
    source=load(manifest['sourceFiles']['exerciseEnvelope']['path'])['items']
    old=load(manifest['sourceFiles']['previousResults']['path']);old_by={q['_id']:q for q in old};source_by={q['_id']:q for q in source}
    old_meta=load(manifest['sourceFiles']['previousMetadata']['path'])
    rows=load(bundle/'validation_results.json');meta=load(bundle/'validation_results_meta.json')
    audit=load(bundle/'bukti_validasi/codex_targeted_review.json');new={q['questionId']:q for q in audit['items']}
    assert audit['apiCalls']==0 and len(new)==len(audit['items'])
    assert len(rows)==len(source) and [q['_id'] for q in rows]==[q['_id'] for q in source]
    assert set(meta)=={q['_id'] for q in rows}
    for q in rows:
        qid=q['_id']
        if qid in old_by:
            assert q==old_by[qid] and meta[qid]==old_meta[qid], 'Existing published question changed'
        else:
            item=new[qid];assert h(q)==item['publishedHash'] and q==item['publishedQuestion']
            assert h(source_by[qid])==item['sourceHash']
            assert {k:v for k,v in q.items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}=={k:v for k,v in source_by[qid].items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}
            value=solve_certificate(item['certificate'])
            from app.services.exercise.replenishment_format import exact_value
            assert value==exact_value(item['exactValue'])
            from app.services.exercise.replenishment_math import m
            assert next(o['text'] for o in q['options'] if o['option_id']==q['jawaban'])==m(value)
            assert q['confidence_score']==0 and q['status']=='active'
            assert q['cognitive_level']==item['assessedLevel']
            assert meta[qid]['validasi']['label_provenance']=='codex_local_assessment'
    assert set(new)==set(meta)-set(old_meta)


def run_class(name,jobs,execute):
    base=ROOT/'output/exercise'/name/'batch01';final=base/'hasil_validasi'
    relevant=[j for j in jobs if j['class_key']==name]
    status_path=RUN/'targeted_generation_progress.json'
    progress=load(status_path) if status_path.exists() else {'target':sum(j['shortfall'] for j in jobs),'classes':{},'apiCalls':0}
    if progress['classes'].get(name,{}).get('status')=='complete':
        verify(final);return progress['classes'][name]
    with batch_lock(base):
        current=load(final/'manifest.json')
        if current.get('schemaVersion')==SCHEMA:
            verify(final)
            assert current['localReview']['jobSetHash']==h(relevant), 'A different authoring round already owns this batch'
            save_progress(status_path,name,current['localReview'],progress['target'])
            return current['localReview']
        verify_local_publication(final)
        master_path=base/'soal_exercise_db.json';meta_path=base/'soal_exercise_meta.json'
        master=load(master_path);meta=load(meta_path)
        old_rows=load(final/'validation_results.json');old_meta=load(final/'validation_results_meta.json')
        old_by={q['_id']:q for q in old_rows}
        stamp=digest(final/'manifest.json')[:16]
        backup=RUN/'backups'/name;assert backup.is_dir()
        def snapshot(path,label):
            target=backup/f'v2_{stamp}_{label}'
            if target.exists():assert target.read_bytes()==path.read_bytes()
            else:shutil.copyfile(path,target)
            return target
        previous_results=snapshot(final/'validation_results.json','previous_results.json')
        previous_meta=snapshot(final/'validation_results_meta.json','previous_meta.json')
        prior_manifest=snapshot(final/'manifest.json','previous_manifest.json')
        old_master=snapshot(master_path,'original_master.json');old_source_meta=snapshot(meta_path,'original_meta.json')
        blueprint_path=RUN/f'targeted_blueprints_{name}.json'
        if not blueprint_path.exists():atomic_json(blueprint_path,{'class':name,'items':old_rows,'metadata':old_meta})
        bp=load(blueprint_path);assert bp['class']==name
        references=bp['items'];reference_meta=bp['metadata']
        stems={q['soal_text'].strip().casefold() for q in master['items']}
        raw_files={};raw_original={};new_rows=[];records=[]
        for job in relevant:
            bab,code,level=job['chapter_no'],job['code'],job['level_target']
            stock=sum(q.get('status')=='active' and q.get('cognitive_level')==level and meta[q['_id']]['bab_id'].endswith('-B'+str(bab)) and meta[q['_id']]['subbab_kode']==code for q in old_rows)
            assert stock==job['active_now'], (name,bab,code,level,'inventory changed')
            path=base/f'bab{bab:02d}'/f'{code}_{level}.json';assert path.parent.is_dir(), 'No new question folder is permitted'
            raw=load(path) if path.exists() else {'book':name,'bab_no':bab,'subbab':code,'level':level,'batch':1,'skill_versi':'v1','soal':[]}
            raw_original[path]=path.read_bytes() if path.exists() else None
            last=max((int(q['id'].rsplit('-',1)[1]) for q in raw['soal']),default=0)
            pool=[q for q in references if q.get('status')=='active' and not q.get('image_url') and reference_meta[q['_id']]['bab_id'].endswith('-B'+str(bab)) and reference_meta[q['_id']]['subbab_kode']==code]
            assert pool, (name,bab,code,'missing blueprint')
            for i in range(job['shortfall']):
                work=f'{name}-b{bab:02d}-{code.lower()}-{level}-bt01-{last+i+1:03d}';qid=hashlib.md5(work.encode()).hexdigest()[:24]
                assert qid not in meta
                r=random.Random(int(hashlib.sha256(work.encode()).hexdigest()[:16],16))
                for trial in range(200):
                    authored=factory(name,bab,code,level,r);d=authored.draft
                    if d.question.strip().casefold() not in stems:break
                else:raise ValueError('Unique, meaningful variation capacity exhausted: '+work)
                assert authored.level==level and len({d.answer,*d.distractors})==4
                stems.add(d.question.strip().casefold())
                reference=r.choice(pool);correct=next(o['text'] for o in reference['options'] if o['option_id']==reference['jawaban'])
                acuan={'sumber':'exercise_validated','id':reference['_id'],'teks':reference['soal_text'],'jawaban':correct,'snapshot':blueprint_path.relative_to(ROOT).as_posix(),'source_sha256':digest(blueprint_path)}
                cognitive={'easy':'C2','medium':'C3','hard':'C4'}[authored.level]
                def reason(value):
                    from app.services.exercise.replenishment_format import exact_value
                    v=exact_value(d.proof['options'][[d.answer,*d.distractors].index(value)])
                    correct_value=exact_value(d.proof['value'])
                    if v==1-correct_value and 0<correct_value<1:return 'Menggunakan peluang komplemen, bukan kejadian yang diminta.'
                    if v==2*correct_value:return 'Mengalikan hasil akhir dengan 2 meskipun kuantitas yang diminta tidak memerlukan faktor tersebut.'
                    if v==correct_value/2:return 'Mengambil separuh hasil yang semestinya, sehingga salah menerapkan faktor atau penggabungan bagian.'
                    if v==-correct_value:return 'Membalik tanda hasil; tidak sesuai dengan arah, selisih, atau kuantitas yang diminta.'
                    return f'Pilihan ini tidak memenuhi seluruh kendala; perhitungan yang memenuhi syarat memberi {d.answer}.'
                q=standard_question({'id':work,'tipe_generate':'variasi','variasi_cara':'konteks','acuan':acuan,'cognitive_c':cognitive,
                   'jumlah_langkah':authored.steps,'jenis_soal':d.kind,'alasan_level':authored.rationale,'stimulus':None,
                   'pertanyaan':d.question,'jawaban_benar':d.answer,'alasan_benar':d.explanation,
                   'distraktor':[{'teks':v,'alasan':reason(v)} for v in d.distractors],
                   'pembahasan':d.explanation,'catatan':'Codex local authoring v2; confidence belum diukur; tanpa API eksternal.'})
                Soal.model_validate(q);raw['soal'].append(q)
                options=[{'text':q['jawaban_benar'],'alasan':'Benar: '+q['alasan_benar']},*[{'text':v['teks'],'alasan':'Salah: '+v['alasan']} for v in q['distraktor']]]
                r.shuffle(options)
                for letter,o in zip('ABCD',options):o['option_id']=letter
                key=next(o['option_id'] for o in options if o['text']==d.answer);now=datetime.now(timezone.utc).isoformat()
                source={'_id':qid,'berkas_id':None,'kelas_id':name,'subbab_id':job['subchapter_name'],'soal_text':d.question,'image_url':[],
                        'soal_type':'Pilihan Ganda','options':options,'matching_pairs':None,'jawaban':key,'cognitive_level':None,
                        'cognitive_score':None,'confidence_score':None,'status':'inactive','created_at':now,'updated_at':now}
                new_rows.append(source);master['items'].append(source)
                info={'id':work,'batch':1,'bab_id':reference_meta[reference['_id']]['bab_id'],'subbab_kode':code,'level_target':level,
                      'cognitive_score_target':{'easy':600,'medium':1000,'hard':1400}[level],'tipe_generate':'variasi','variasi_cara':'konteks',
                      'acuan':acuan,'cognitive_c':cognitive,'jumlah_langkah':authored.steps,'jenis_soal':d.kind,'pembahasan':d.explanation,
                      'catatan':q['catatan'],'dipaksa_kuota':False,'skill_versi':'v1','generator':'codex:targeted-replenishment-v2',
                      'bergambar':False,'gambar':[],'local_math_check':d.proof,'validation_status':'codex_local_review_pass'}
                meta[qid]=info
                published={**source,'status':'active','cognitive_level':authored.level,'cognitive_score':info['cognitive_score_target'],'confidence_score':0}
                records.append({'questionId':qid,'sourceHash':h(source),'publishedHash':h(published),'publishedQuestion':published,
                                'certificate':authored.certificate,'exactValue':d.proof['value'],'assessedLevel':authored.level,
                                'rationale':authored.rationale,'dependentSteps':authored.steps,'solution':d.explanation,'apiCalls':0,'confidenceMeasured':False})
            ExerciseFile.model_validate(raw);raw_files[path]=raw
        from app.presentation.latex import math_spans
        expressions=set()
        for record in records:
            row=record['publishedQuestion']
            for text in [row['soal_text'],record['solution'],*[o['text'] for o in row['options']],*[o['alasan'] for o in row['options']]]:
                assert text.count('$')%2==0, (record['questionId'],text)
                expressions.update(math_spans(text))
        render_input=RUN/f'targeted_math_{name}.json'
        atomic_json(render_input,[{'id':i,'tex':tex,'display':display} for i,(tex,display) in enumerate(sorted(expressions))])
        rendered=json.loads(subprocess.run(['node',str(ROOT/'scripts/latex_render_check.cjs'),str(render_input)],capture_output=True,text=True,encoding='utf-8',check=True).stdout)
        atomic_json(RUN/f'targeted_render_{name}.json',rendered)
        assert not rendered['errors'], ('LaTeX rendering failed',rendered['errors'][:3])
        result={'class':name,'added':len(new_rows),'status':'reviewed' if not execute else 'complete','levels':dict(Counter(x['assessedLevel'] for x in records)),'apiCalls':0,'jobSetHash':h(relevant)}
        atomic_json(RUN/f'targeted_plan_{name}.json',{'summary':result,'items':records})
        if not execute:print(json.dumps(result),flush=True);return result
        old_meta_final=deepcopy(old_meta);row_map={r['questionId']:r for r in records}
        rows=old_rows+[r['publishedQuestion'] for r in records]
        assert [q['_id'] for q in rows]==[q['_id'] for q in master['items']]
        for rec in records:
            qid=rec['questionId'];info=deepcopy(meta[qid]);info['local_review']=rec
            info['validasi']={'cognitive_level':rec['assessedLevel'],'cognitive_score':rec['publishedQuestion']['cognitive_score'],'confidence_score':0,
                'status':'active','validation_status':'codex_local_review_pass','validation_method':'codex_local_review','label_provenance':'codex_local_assessment',
                'api_runs':0,'requested_runs':0,'local_review_passes':1,'confidence_available':False,'confidence_status':'not_measured',
                'training_evidence_qualified':False,'full_complete':True,'level_sesuai_target':True}
            old_meta_final[qid]=info
        new_master=backup/f'v2_{stamp}_expanded_master.json';new_meta=backup/f'v2_{stamp}_expanded_meta.json'
        atomic_json(new_master,master);atomic_json(new_meta,meta)
        staging=Path(tempfile.mkdtemp(prefix='targeted_',dir=RUN))
        # Retain the prior local review evidence in the canonical publication.
        if (final/'bukti_validasi').is_dir():shutil.copytree(final/'bukti_validasi',staging/'bukti_validasi')
        atomic_json(staging/'validation_results.json',rows);atomic_json(staging/'validation_results_meta.json',old_meta_final)
        atomic_json(staging/'bukti_validasi/codex_targeted_review.json',{'schemaVersion':SCHEMA,'apiCalls':0,'items':records})
        note=f'# Tambahan sesuai kekurangan — {name}\n\n{len(records)} soal baru, confidence 0, pemeriksaan lokal Codex tanpa API.\n\nSoal lama dipertahankan persis. Label adalah intended difficulty berdasarkan isi dan profil penyelesaian, bukan kalibrasi empiris atau hasil blind Gemini. Sertifikat matematika dapat dihitung ulang.\n'
        for file in ['README.md','RINGKASAN_VALIDASI.md','LAPORAN_VALIDASI.md']:(staging/file).write_text(note,encoding='utf-8')
        files={'exerciseEnvelope':new_master,'exerciseMetadata':new_meta,'previousResults':previous_results,'previousMetadata':previous_meta,'previousManifest':prior_manifest,'originalMaster':old_master,'originalSourceMetadata':old_source_meta,'blueprint':blueprint_path}
        live={str(master_path):new_master,str(meta_path):new_meta}
        manifest={'schemaVersion':SCHEMA,'class':name,'sourceFiles':{k:{'path':str(p),'sha256':digest(p)} for k,p in files.items()},
                  'liveInputs':{k:{'path':k,'sha256':digest(p)} for k,p in live.items()},
                  'outputs':{p.relative_to(staging).as_posix():{'sha256':digest(p),'bytes':p.stat().st_size} for p in staging.rglob('*') if p.is_file()},'localReview':result}
        atomic_json(staging/'manifest.json',manifest);verify(staging,False)
        state_path=base/'reference_replenishment_state.json';reference_path=base/'reference_replenishment_manifest.json'
        rollback={p:p.read_bytes() for p in [master_path,meta_path,state_path,reference_path]}
        rollback.update(raw_original)
        recovery={}
        for p,data in rollback.items():
            if data is None:recovery[str(p)]=None
            else:recovery[str(p)]=str(snapshot(p,'rollback_'+p.relative_to(base).as_posix().replace('/','__')))
        journal=RUN/f'targeted_transaction_{name}.json'
        atomic_json(journal,{'phase':'prepared','rollbackFiles':recovery,'staging':str(staging),'retired':str(backup/f'v2_{stamp}_previous_publication')})
        retired=backup/f'v2_{stamp}_previous_publication'
        assert not retired.exists()
        for path in [retired,staging,final]:assert path.resolve().is_relative_to(ROOT.resolve())
        moved=False
        try:
            for path,data in raw_files.items():atomic_json(path,data)
            atomic_json(master_path,master);atomic_json(meta_path,meta)
            reference=load(reference_path)
            for p in [master_path,meta_path,*raw_files]:reference['files'][p.relative_to(base).as_posix()]=digest(p)
            reference['added']+=len(records);atomic_json(reference_path,reference)
            state=load(state_path);state.update(phase='local_review_complete',reviewMode='local_without_external_api',validationOwner='codex_local_review',manifestSha256=digest(reference_path))
            atomic_json(state_path,state)
            final.rename(retired);moved=True;staging.rename(final);verify(final)
        except Exception:
            if moved:
                if final.exists():final.rename(backup/f'v2_{stamp}_failed_publication')
                retired.rename(final)
            for p,data in rollback.items():
                if data is None:p.unlink(missing_ok=True)
                else:p.write_bytes(data)
            raise
        progress=save_progress(status_path,name,result,progress['target'])
        atomic_json(journal,{'phase':'committed','completed':len(records),'manifestSha256':digest(final/'manifest.json')})
        print(json.dumps({**result,'completedOverall':progress['completed'],'target':progress['target']}),flush=True)
        return result


def reauthor_class(name,jobs):
    """Replace only this round's additions; all pre-existing questions stay frozen."""
    base=ROOT/'output/exercise'/name/'batch01';final=base/'hasil_validasi';verify(final)
    manifest=load(final/'manifest.json');backup=RUN/'backups'/name
    previous=Path(manifest['sourceFiles']['previousManifest']['path']);stamp=digest(previous)[:16]
    retired=backup/f'v2_{stamp}_previous_publication';archive=backup/f'v2_{stamp}_superseded_targeted_publication'
    assert retired.is_dir() and not archive.exists()
    paths=[base/n for n in ['soal_exercise_db.json','soal_exercise_meta.json','reference_replenishment_state.json','reference_replenishment_manifest.json']]
    paths += [base/f"bab{j['chapter_no']:02d}"/f"{j['code']}_{j['level_target']}.json" for j in jobs if j['class_key']==name]
    before={p:p.read_bytes() if p.exists() else None for p in paths}
    for p in [final,retired,archive,*paths]:assert p.resolve().is_relative_to(ROOT.resolve())
    old_progress=load(RUN/'targeted_generation_progress.json')
    # Freeze the superseded round's source snapshots before the same job is rebuilt.
    for key in ['exerciseEnvelope','exerciseMetadata']:
        dest=backup/f'v2_{stamp}_superseded_{key}.json';shutil.copyfile(manifest['sourceFiles'][key]['path'],dest)
        manifest['sourceFiles'][key]={'path':str(dest),'sha256':digest(dest)}
    try:
        final.rename(archive);atomic_json(archive/'manifest.json',manifest);retired.rename(final)
        for p in paths:
            retained=backup/f"v2_{stamp}_rollback_{p.relative_to(base).as_posix().replace('/','__')}"
            if retained.exists():shutil.copyfile(retained,p)
            else:
                assert p.parent.name.startswith('bab')
                p.unlink(missing_ok=True)
        verify_local_publication(final)
        progress=load(RUN/'targeted_generation_progress.json');progress['classes'].pop(name,None)
        progress['completed']=sum(v['added'] for v in progress['classes'].values());atomic_json(RUN/'targeted_generation_progress.json',progress)
        return run_class(name,jobs,True)
    except Exception:
        if final.exists():
            if not retired.exists():final.rename(retired)
            else:final.rename(backup/f'v2_{stamp}_failed_reauthoring')
        if archive.exists():archive.rename(final)
        for p,data in before.items():
            if data is None:p.unlink(missing_ok=True)
            else:p.write_bytes(data)
        atomic_json(RUN/'targeted_generation_progress.json',old_progress)
        raise


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--classes',nargs='+',required=True);p.add_argument('--execute',action='store_true');p.add_argument('--reauthor',action='store_true');args=p.parse_args()
    jobs=load(RUN/'remaining_level_needs.json')['jobs']
    if args.reauthor:assert args.execute
    for name in args.classes:
        if args.reauthor:reauthor_class(name,jobs)
        else:run_class(name,jobs,args.execute)


if __name__=='__main__':main()
