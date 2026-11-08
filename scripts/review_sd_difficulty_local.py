"""Review actual SD difficulty, retain decisions, and replenish real shortages."""
from __future__ import annotations
from collections import Counter
from copy import deepcopy
from datetime import datetime,timezone
import argparse
import hashlib
import json
import math
from pathlib import Path
import random
import shutil
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT))
from scripts import generate_sd_bank_local as bank
from app.services.exercise.sd_difficulty_review import assess,POLICY
from app.services.exercise.sd_review_additions import generate
from app.services.exercise.schema import ExerciseFile
from app.services.exercise.workflow import atomic_json,batch_lock,digest,safe_asset
from app.services.exercise.sd_bank_visuals import render_scene
from app.services.exercise.options import susun

SCHEMA='codex-sd-difficulty-review-v2';RUN=ROOT/'runs/sd_difficulty_review_v2'
LEVELS=bank.LEVELS;load=bank.load;h=bank.fingerprint


def evaluate(raw,grade,certificate):
    value=bank.solve(certificate)
    assert bank.answer_identity(bank.m(value))==bank.answer_identity(raw['jawaban_benar'])
    assert len({bank.answer_identity(x) for x in [raw['jawaban_benar'],*[d['teks'] for d in raw['distraktor']]]})==4
    scene=(raw.get('visual_spec') or {}).get('scene')
    image_check=bank.visual_check({'scene':scene,'certificate':certificate,'kind':raw['jenis_soal']})
    decision=assess(raw['pertanyaan'],certificate,raw['jenis_soal'],grade,scene)
    return {**decision,'workingId':raw['id'],'certificate':certificate,'exactValue':str(value),'rawHash':h(raw),'visualCheck':image_check,
            'checks':['answer_recomputed','four_inequivalent_options','content_family_reviewed','numerical_shortcuts_checked','visual_data_binding_checked']}


def verify(bundle):
    if load(Path(bundle)/'manifest.json').get('schemaVersion')=='codex-exercise-sessions-local-v3':
        from app.services.exercise.session_expansion import verify_publication
        return verify_publication(bundle)
    bundle=Path(bundle);base=bundle.parent;manifest=load(bundle/'manifest.json');assert manifest['schemaVersion']==SCHEMA
    for name,sha in manifest['inputs'].items():assert digest(base/name)==sha
    for name,sha in manifest['outputs'].items():assert digest(bundle/name)==sha
    rows=load(bundle/'validation_results.json');meta=load(bundle/'validation_results_meta.json');source=load(base/'soal_exercise_db.json')['items']
    audit=load(bundle/'bukti_validasi/codex_local_review.json');by={i['questionId']:i for i in audit['items']}
    assert len(by)==len(rows)==len(source) and set(meta)==set(by)
    original=load(bundle/'bukti_validasi/previous_validation_results.json');old={q['_id']:q for q in original}
    raw_by={}
    for path in base.glob('bab*/*_*.json'):
        raw=load(path);ExerciseFile.model_validate(raw)
        for q in raw['soal']:assert q['id'] not in raw_by;raw_by[q['id']]=q
    counts=Counter();pictures=Counter();grade=int(manifest['class'][5:])
    for row,unlabelled in zip(rows,source):
        qid=row['_id'];item=by[qid];info=meta[qid];raw=raw_by[info['id']]
        assert qid==unlabelled['_id'] and h(row)==item['publishedHash'] and h(unlabelled)==item['sourceHash']
        assert h(raw)==item['rawHash']
        if qid in old:assert {k:v for k,v in row.items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')}=={k:v for k,v in old[qid].items() if k not in ('status','cognitive_level','cognitive_score','confidence_score')},'Existing question content changed'
        current=evaluate(raw,grade,item['certificate']);assert current['assessedLevel']==item['assessedLevel']
        assert row['cognitive_level']==item['assessedLevel'] and row['confidence_score']==0
        assert row['status']==('active' if item['assessedLevel'] else 'inactive')
        assert info['validasi']['api_runs']==0 and not info['validasi']['training_evidence_qualified']
        assert info['validasi']['review_policy']==POLICY
        if row['status']=='active':
            key=(info['bab_id'],info['subbab_kode'],row['cognitive_level']);counts[key]+=1;pictures[key]+=bool(row['image_url'])
        for ref in row['image_url']:safe_asset(base,ref)
    expected={(f'SD{grade}-B{j["chapter_no"]}',j['code'],level) for j in load(base/'generation_plan.json')['catalog'] for level in LEVELS}
    assert set(counts)==expected
    assert all(counts[k]>=10 and pictures[k]>=7 and counts[k]-pictures[k]>=3 for k in expected)
    assert sum(pictures.values())*10>=sum(counts.values())*7
    assert audit['apiCalls']==0 and audit['policyVersion']==POLICY


def run_class(grade):
    base=bank.base_for(grade);final=base/'hasil_validasi';name='kelas'+str(grade)
    with batch_lock(base):
        if load(final/'manifest.json')['schemaVersion']=='codex-exercise-sessions-local-v3':
            from app.services.exercise.session_expansion import verify_publication
            return verify_publication(final)
        if load(final/'manifest.json')['schemaVersion']==SCHEMA:
            verify(final);return load(final/'bukti_validasi/codex_local_review.json')['summary']
        bank.verify(final)
        original=load(final/'validation_results.json');old_meta=load(final/'validation_results_meta.json');master=load(base/'soal_exercise_db.json');source_meta=load(base/'soal_exercise_meta.json')
        refs=load(base/'reference_blueprints.json')['references'];jobs=load(base/'generation_plan.json')['catalog']
        stamp=digest(final/'manifest.json')[:16];archive=RUN/'backups'/name/stamp
        if not (archive/'snapshot_complete.json').exists():
            shutil.copytree(base,archive/'batch01',ignore=shutil.ignore_patterns('.workflow.lock'),dirs_exist_ok=True)
            atomic_json(archive/'snapshot_complete.json',{'originalManifestHash':digest(final/'manifest.json')})
        raw_files={p:load(p) for p in sorted(base.glob('bab*/*_*.json'))};raw_by={q['id']:q for f in raw_files.values() for q in f['soal']}
        previous_evidence=load(final/'bukti_validasi/codex_local_sd_review.json')['items'];proofs={i['questionId']:i for i in previous_evidence}
        decisions={};counts=Counter();changes=Counter();old_by={r['_id']:r for r in original};new_source=[];identities={h({'text':q['pertanyaan'],'scene':(q.get('visual_spec') or {}).get('scene')}) for q in raw_by.values()}
        for row in original:
            info=old_meta[row['_id']];d=evaluate(raw_by[info['id']],grade,proofs[row['_id']]['certificate']);d.update(questionId=row['_id'],previousLevel=row['cognitive_level'],previousStatus=row['status'],originalTarget=source_meta[row['_id']]['level_target'],addedInReview=False)
            decisions[row['_id']]=d;changes[row['cognitive_level']+'->'+str(d['assessedLevel'])]+=1
            if d['assessedLevel']:counts[(info['bab_id'],info['subbab_kode'],d['assessedLevel'],bool(row['image_url']))]+=1
        additions=[]
        for job in jobs:
            for level in LEVELS:
                for visual,quota in [(True,7),(False,3)]:
                    key=(f'SD{grade}-B{job["chapter_no"]}',job['code'],level,visual)
                    additions.extend((job,level,visual) for _ in range(max(0,quota-counts[key])))
        active=sum(counts.values());visual_now=sum(n for k,n in counts.items() if k[-1]);planned_visual=sum(v for _,_,v in additions);active+=len(additions);visual_now+=planned_visual
        extra_visual=max(0,math.ceil((7*active-10*visual_now)/3))
        # Retain at least 70% essential visuals per class, without forcing labels.
        for i in range(extra_visual):additions.append((jobs[i%len(jobs)],'easy',True))
        for index,(job,level,visual) in enumerate(additions):
            path=base/f"bab{job['chapter_no']:02d}"/f"{job['code']}_{level}.json";raw=raw_files[path]
            serial=max(int(q['id'].rsplit('-',1)[1]) for q in raw['soal'])+1;work=f"{name}-b{job['chapter_no']:02d}-{job['code'].lower()}-{level}-bt01-{serial:03d}"
            rng=random.Random(int(hashlib.sha256((POLICY+work).encode()).hexdigest()[:16],16))
            for trial in range(500):
                model=generate(grade,job['chapter_no'],job['code'],level,rng,visual,serial)
                if model is None:continue
                identity=h({'text':model['question'],'scene':model['scene']})
                if identity in identities:continue
                try:
                    assessed=assess(model['question'],model['certificate'],model['kind'],grade,model['scene'])
                    if assessed['assessedLevel']!=level:continue
                    bank.visual_check(model)
                except (AssertionError,ValueError,ZeroDivisionError):continue
                break
            else:raise ValueError('Suitable variation capacity exhausted: '+work)
            identities.add(identity);model=bank.normalize_document(model);pool,adapted=bank.reference_pool(job,refs);ref=rng.choice(pool)
            q={'id':work,'tipe_generate':'variasi','variasi_cara':'konteks' if index%2 else 'angka','acuan':{'sumber':'pretest_validated','id':ref['id'],'teks':ref['text'],'jawaban':ref['answer'],'snapshot':bank.rel(base/'reference_blueprints.json'),'source_sha256':digest(base/'reference_blueprints.json')},
               'cognitive_c':{'easy':'C2','medium':'C3','hard':'C4'}[level],'jumlah_langkah':assessed['steps'],'jenis_soal':model['kind'],'alasan_level':assessed['reason'],'stimulus':None,'pertanyaan':model['question'],'jawaban_benar':model['answer'],'alasan_benar':model['explanation'],
               'distraktor':[{'teks':w,'alasan':f'Pilihan ini tidak memenuhi seluruh informasi dan syarat pada soal; hasil yang sesuai adalah {model["answer"]}.'} for w in model['wrong']],
               'pembahasan':model['explanation'],'catatan':'Tambahan setelah penilaian ulang kesulitan lokal; tanpa API; confidence belum diukur.'}
            asset_proof={}
            if visual:
                asset,asset_proof=render_scene(model['scene'],base);q.update(gambar=['exercise_assets/'+name+'/batch01/'+asset],visual_spec={'kind':'sd_scene','scene':model['scene']},deskripsi_gambar=asset_proof['description'])
            bank.Soal.model_validate(q);d=evaluate(q,grade,model['certificate']);qid=hashlib.md5(work.encode()).hexdigest()[:24];assert qid not in source_meta
            d.update(questionId=qid,previousLevel=None,previousStatus=None,originalTarget=level,addedInReview=True,visualProvenance=asset_proof,sourceAdaptation={'sourceClass':ref['class'],'sourceChapter':ref['chapter'],'sourceCode':ref['code'],'conceptAdaptation':adapted})
            raw['soal'].append(q);raw_by[work]=q;options,key=susun(ExerciseFile.model_validate({**raw,'soal':[q]}))[work];now=datetime.now(timezone.utc).isoformat()
            row={'_id':qid,'berkas_id':None,'kelas_id':name,'subbab_id':job['name'],'soal_text':q['pertanyaan'],'image_url':([asset] if visual else []),'soal_type':'Pilihan Ganda','options':options,'jawaban':key,'matching_pairs':None,'cognitive_level':None,'cognitive_score':None,'confidence_score':None,'status':'inactive','created_at':now,'updated_at':now}
            master['items'].append(row);new_source.append(row);decisions[qid]=d
            source_meta[qid]={'id':work,'batch':1,'bab_id':f'SD{grade}-B{job["chapter_no"]}','subbab_kode':job['code'],'level_target':level,'cognitive_score_target':bank.SCORES[level],'tipe_generate':'variasi','variasi_cara':q['variasi_cara'],'acuan':q['acuan'],'cognitive_c':q['cognitive_c'],'jumlah_langkah':q['jumlah_langkah'],'jenis_soal':q['jenis_soal'],'pembahasan':q['pembahasan'],'alasan_level':q['alasan_level'],'generator':'codex:sd-difficulty-review-v2','skill_versi':'v1','bergambar':visual,'gambar':q.get('gambar',[]),'visual_spec':q.get('visual_spec'),'visual_provenance':asset_proof,'local_math_check':model['certificate'],'sourceAdaptation':d['sourceAdaptation'],'validation_status':'codex_local_review_pass'}
            counts[(source_meta[qid]['bab_id'],job['code'],level,visual)]+=1
            if (index+1)%25==0:print(json.dumps({'class':name,'reviewedOriginal':len(original),'added':index+1,'addTarget':len(additions)}),flush=True)
        rows=[];meta={}
        for unlabelled in master['items']:
            qid=unlabelled['_id'];d=decisions[qid];level=d['assessedLevel'];published=deepcopy(old_by.get(qid,unlabelled));published.update(cognitive_level=level,cognitive_score=bank.SCORES[level] if level else None,confidence_score=0,status='active' if level else 'inactive')
            d.update(sourceHash=h(unlabelled),publishedHash=h(published));info=deepcopy(old_meta.get(qid,source_meta[qid]))
            if qid in old_meta:info['previous_local_assessment']={'validasi':old_meta[qid]['validasi'],'local_review':old_meta[qid]['local_review']}
            info['local_review']=d;info['difficulty_review']=d;info['validasi']={'cognitive_level':level,'cognitive_score':published['cognitive_score'],'confidence_score':0,'status':published['status'],'validation_status':'codex_local_review_pass' if level else 'local_revision_required','validation_provider':'codex_direct_review','validation_model':None,'api_runs':0,'requested_runs':0,'local_review_passes':2,'confidence_available':False,'confidence_status':'not_measured','consistency_measured':False,'training_evidence_qualified':False,'full_complete':True,'validation_method':'codex_local_review','label_provenance':'codex_local_assessment','level_sesuai_target':level==d['originalTarget'],'review_policy':POLICY,'answer_key_status':'verified_locally','source_hash':d['sourceHash'],'assessment_reason':d['reason']}
            meta[qid]=info;rows.append(published)
        all_raw=[q for f in raw_files.values() for q in f['soal']];rendering=bank.check_latex(all_raw,RUN/f'latex_{grade}.json')
        summary={'class':name,'reviewedOriginal':len(original),'added':len(additions),'total':len(rows),'active':sum(q['status']=='active' for q in rows),'inactive':sum(q['status']!='active' for q in rows),'transitions':dict(changes),'levels':dict(Counter(q['cognitive_level'] for q in rows if q['status']=='active')),'activeVisual':sum(q['status']=='active' and bool(q['image_url']) for q in rows),'apiCalls':0,'policyVersion':POLICY,'rendering':rendering}
        staging=Path(tempfile.mkdtemp(prefix='.difficulty-review-',dir=base));shutil.copytree(final,staging,dirs_exist_ok=True)
        atomic_json(staging/'validation_results.json',rows);atomic_json(staging/'validation_results_meta.json',meta)
        atomic_json(staging/'bukti_validasi/previous_validation_results.json',original);atomic_json(staging/'bukti_validasi/previous_validation_metadata.json',old_meta)
        atomic_json(staging/'bukti_validasi/codex_local_review.json',{'schemaVersion':SCHEMA,'policyVersion':POLICY,'apiCalls':0,'items':list(decisions.values()),'summary':summary})
        asset_reviews={}
        for row in rows:
            for asset in row['image_url']:
                record=asset_reviews.setdefault(asset,{'asset':asset,'pngSha256':digest(safe_asset(base,asset)),'activeQuestionIds':[],'inactiveQuestionIds':[],'reviewPolicy':POLICY,'apiCalls':0,'independentVisionValidation':False})
                record['activeQuestionIds' if row['status']=='active' else 'inactiveQuestionIds'].append(row['_id'])
        for item in asset_reviews.values():item['status']='verified_locally' if item['activeQuestionIds'] else 'inactive_questions_only'
        atomic_json(staging/'bukti_validasi/assets_validation_results.json',{'schemaVersion':SCHEMA,'items':asset_reviews,'apiCalls':0})
        code=staging/'bukti_validasi/reviewed_code'
        for p in [Path(__file__),ROOT/'app/services/exercise/sd_difficulty_review.py',ROOT/'app/services/exercise/sd_review_additions.py']:shutil.copyfile(p,code/p.name)
        note=f'# Penilaian ulang kesulitan — {name}\n\n{len(original)} soal lama dinilai dari isi dan solusi minimum; ditambahkan {len(additions)} soal yang sesuai untuk menutup kekurangan.\n\nSemua subbab memiliki setidaknya 10 easy, 10 medium, dan 10 hard; setiap level minimal 7 soal bergambar dan 3 teks. Label tidak dipaksa mengikuti kuota.\n\nConfidence 0: belum diukur. Tanpa API. Pemeriksaan lokal bukan validasi AI independen atau kalibrasi empiris. Soal lama dan penilaiannya sebelumnya disimpan sebagai riwayat.\n\nHasil per soal: `bukti_validasi/codex_local_review.json`. Hasil gambar: `bukti_validasi/assets_validation_results.json`. Status pending pada JSON di folder assets adalah catatan awal renderer yang dipertahankan; lihat hasil pemeriksaan terkini tersebut.\n'
        for file in ['README.md','RINGKASAN_VALIDASI.md','LAPORAN_VALIDASI.md']:(staging/file).write_text(note,encoding='utf-8')
        transitions=['# Perubahan level dan kapasitas','', '| Level lama → level baru | Jumlah |','|---|---:|']
        transitions += [f'| {key} | {n} |' for key,n in sorted(changes.items())]
        transitions += ['',f'Tambahan soal yang dinilai sesuai: {len(additions)}.',f'Soal aktif: {summary["active"]}; inactive: {summary["inactive"]}.','', 'Alasan tiap keputusan, label awal, model hitung, dan penilaian sebelumnya tersedia pada metadata. Tidak ada confidence atau validasi API yang dibuat-buat.','']
        (staging/'LAPORAN_PERUBAHAN_LEVEL.md').write_text('\n'.join(transitions),encoding='utf-8')
        (staging/'bukti_validasi/ASSET_REVIEW.md').write_text('Status pada JSON aset adalah status saat render, yang tidak diubah agar hash aset tetap stabil. Hasil pemeriksaan lokal terkini per soal, termasuk visualCheck, ada pada codex_local_review.json. Tidak ada klaim validasi gambar AI independen.\n',encoding='utf-8')
        mutable=[base/'soal_exercise_db.json',base/'soal_exercise_meta.json',base/'local_generation_checkpoint.json',base/'reference_replenishment_state.json',*raw_files]
        rollback={p:p.read_bytes() for p in mutable};journal=RUN/f'transaction_{name}.json';retired=archive/'previous_publication'
        if retired.exists():retired=archive/('previous_publication_'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
        for p in [base,staging,retired,*mutable]:assert p.resolve().is_relative_to(ROOT.resolve())
        assert not retired.exists();atomic_json(journal,{'phase':'prepared','class':name,'archive':str(archive),'staging':str(staging)})
        moved=False
        try:
            for p,raw in raw_files.items():ExerciseFile.model_validate(raw);atomic_json(p,raw)
            atomic_json(base/'soal_exercise_db.json',master);atomic_json(base/'soal_exercise_meta.json',source_meta)
            state=load(base/'local_generation_checkpoint.json')
            for p in raw_files:state['files'][p.relative_to(base).as_posix()]['sha256']=digest(p)
            state['postGenerationReview']=POLICY;atomic_json(base/'local_generation_checkpoint.json',state)
            inputs={p.relative_to(base).as_posix():digest(p) for p in [base/'soal_exercise_db.json',base/'soal_exercise_meta.json',base/'generation_plan.json',base/'reference_blueprints.json',*raw_files,*sorted((base/'assets').glob('*'))] if p.is_file()}
            manifest={'schemaVersion':SCHEMA,'class':name,'inputs':inputs,'outputs':{p.relative_to(staging).as_posix():digest(p) for p in staging.rglob('*') if p.is_file() and p.name!='manifest.json'},'questionCount':len(rows),'localReview':summary}
            atomic_json(staging/'manifest.json',manifest);verify(staging)
            final.rename(retired);moved=True;staging.rename(final);verify(final)
            workflow=load(base/'reference_replenishment_state.json');workflow.update(phase='local_review_complete',reviewMode='local_without_external_api',validationOwner='codex_local_review',publishedQuestions=len(rows),latestReviewPolicy=POLICY);atomic_json(base/'reference_replenishment_state.json',workflow)
        except Exception:
            if moved:
                if final.exists():final.rename(archive/'failed_publication')
                retired.rename(final)
            for p,data in rollback.items():p.write_bytes(data)
            raise
        atomic_json(journal,{'phase':'committed',**summary});print(json.dumps(summary),flush=True);return summary


def finalize_reports(grade):
    """Retain renderer facts while publishing a separate authoritative asset review."""
    base=bank.base_for(grade);final=base/'hasil_validasi'
    with batch_lock(base):
        verify(final)
        if (final/'bukti_validasi/assets_validation_results.json').exists():return
        rows=load(final/'validation_results.json');summary=load(final/'bukti_validasi/codex_local_review.json')['summary'];assets={}
        for row in rows:
            for asset in row['image_url']:
                item=assets.setdefault(asset,{'asset':asset,'pngSha256':digest(safe_asset(base,asset)),'activeQuestionIds':[],'inactiveQuestionIds':[],'reviewPolicy':POLICY,'apiCalls':0,'independentVisionValidation':False})
                item['activeQuestionIds' if row['status']=='active' else 'inactiveQuestionIds'].append(row['_id'])
        for item in assets.values():item['status']='verified_locally' if item['activeQuestionIds'] else 'inactive_questions_only'
        staging=Path(tempfile.mkdtemp(prefix='.review-reports-',dir=base));shutil.copytree(final,staging,dirs_exist_ok=True)
        atomic_json(staging/'bukti_validasi/assets_validation_results.json',{'schemaVersion':SCHEMA,'items':assets,'apiCalls':0})
        (staging/'bukti_validasi/ASSET_REVIEW.md').write_text('Catatan pending pada JSON aset dipertahankan sebagai status awal renderer. Hasil pemeriksaan lokal terkini ada pada assets_validation_results.json dan codex_local_review.json. Tidak ada klaim validasi gambar AI independen.\n',encoding='utf-8')
        text=f'# Penilaian ulang kesulitan — kelas{grade}\n\n{summary["reviewedOriginal"]} soal awal dinilai dari isi dan solusi minimum. Ditambahkan {summary["added"]} soal untuk memenuhi level tanpa memaksa label.\n\nAktif {summary["active"]}, inactive {summary["inactive"]}. Setiap subbab mempunyai minimal 10 easy, 10 medium, dan 10 hard; setiap level minimal 7 bergambar dan 3 teks.\n\nConfidence 0: belum diukur; tanpa API. Label merupakan penilaian lokal, bukan validasi AI independen atau kalibrasi empiris.\n\nBukti per soal: `bukti_validasi/codex_local_review.json`. Status gambar terkini: `bukti_validasi/assets_validation_results.json`. JSON pada folder assets mencatat tahap render awal, bukan hasil pemeriksaan akhir.\n'
        for name in ['README.md','RINGKASAN_VALIDASI.md','LAPORAN_VALIDASI.md']:(staging/name).write_text(text,encoding='utf-8')
        table=['# Perubahan level','', '| Level lama → baru | Jumlah |','|---|---:|']+[f'| {key} | {n} |' for key,n in sorted(summary['transitions'].items())]
        table+=['',f'Tambahan {summary["added"]} soal; confidence 0 berarti belum diukur. Riwayat label dan alasan per soal terdapat pada metadata.','']
        (staging/'LAPORAN_PERUBAHAN_LEVEL.md').write_text('\n'.join(table),encoding='utf-8')
        manifest=load(staging/'manifest.json');manifest['outputs']={p.relative_to(staging).as_posix():digest(p) for p in staging.rglob('*') if p.is_file() and p!=staging/'manifest.json'}
        atomic_json(staging/'manifest.json',manifest);verify(staging)
        retired=RUN/'report_backups'/('kelas'+str(grade))/digest(final/'manifest.json')[:16];retired.parent.mkdir(parents=True,exist_ok=True)
        assert not retired.exists() and retired.resolve().is_relative_to(RUN.resolve())
        final.rename(retired)
        try:staging.rename(final);verify(final)
        except Exception:
            if final.exists():final.rename(retired.parent/'failed_reports')
            retired.rename(final);raise


def audit_all():
    if all(load(bank.base_for(g)/'hasil_validasi/manifest.json').get('schemaVersion')=='codex-exercise-sessions-local-v3' for g in range(1,5)):
        from app.services.exercise.session_expansion import audit,prepare
        return audit(prepare())
    from PIL import Image
    summaries=[];ids=set();pictures=0;raw_count=0
    for grade in range(1,5):
        finalize_reports(grade)
        base=bank.base_for(grade);final=base/'hasil_validasi';verify(final)
        summary=load(final/'bukti_validasi/codex_local_review.json')['summary'];summaries.append(summary)
        for row in load(final/'validation_results.json'):
            assert row['_id'] not in ids;ids.add(row['_id'])
            for ref in row['image_url']:
                with Image.open(safe_asset(base,ref)) as image:image.verify()
            pictures+=bool(row['image_url'])
        raw_count+=sum(len(load(p)['soal']) for p in base.glob('bab*/*_*.json'))
    from app.ingestion.question_sync import load_sources,report_catalog,coverage
    inventory=coverage(load_sources(ROOT/'output'),report_catalog(ROOT/'API_DOCUMENTATION/Pesan_eror.md'))
    scope=[r for r in inventory['rows'] if r['class_key'] in {'kelas1','kelas2','kelas3','kelas4'}]
    assert len(scope)==85 and all(r['shortfall']==0 for r in scope) and raw_count==len(ids)
    frozen=load(bank.RUN/'protected_inputs.json')
    assert all(digest(ROOT/path)==sha for path,sha in frozen.items()),'Pretest or classes 5–12 changed'
    result={'policyVersion':POLICY,'apiCalls':0,'reviewedOriginal':sum(q['reviewedOriginal'] for q in summaries),'totalAdded':sum(q['added'] for q in summaries),'totalQuestions':len(ids),'active':sum(q['active'] for q in summaries),'inactive':sum(q['inactive'] for q in summaries),'questionsWithImages':pictures,'activeWithImages':sum(q['activeVisual'] for q in summaries),'shortfall':0,'subchapters':85,'levelSlots':255,'mathExpressionsRendered':sum(q['rendering']['checked'] for q in summaries),'renderErrors':0,'classes':summaries,'inventory':scope,'protectedFilesUnchanged':len(frozen)}
    atomic_json(RUN/'final_audit.json',result)
    lines=['# Penilaian ulang SD kelas 1–4 selesai','',f'{result["reviewedOriginal"]} soal awal diperiksa; {result["totalAdded"]} soal tambahan dibuat setelah perubahan level.',f'**{result["active"]} soal aktif, {result["inactive"]} inactive. Kekurangan satu sesi per subbab-level: 0.**','', '| Kelas | Easy aktif | Medium aktif | Hard aktif | Aktif | Tambahan |','|---|---:|---:|---:|---:|---:|']
    for row in summaries:lines.append(f'| {row["class"]} | {row["levels"].get("easy",0)} | {row["levels"].get("medium",0)} | {row["levels"].get("hard",0)} | {row["active"]} | {row["added"]} |')
    lines += ['', 'Minimum tiap subbab dan level: 10 soal aktif, terdiri dari setidaknya 7 bergambar dan 3 teks. Proporsi gambar aktif tiap kelas paling sedikit 70%.',f'KaTeX: {result["mathExpressionsRendered"]} ekspresi, 0 error. Pretest dan latihan kelas 5–12 tidak berubah.', '', 'Confidence 0 berarti belum diukur. Label merupakan penilaian kesulitan lokal Codex, bukan validasi AI independen atau kalibrasi IRT empiris. Tanpa pemanggilan API dan tanpa sinkronisasi database production.', '', 'Hasil per soal, riwayat label, dan status gambar terkini ada pada hasil_validasi tiap kelas. Berkas JSON aset mempertahankan catatan awal renderer; hasil pemeriksaannya dicatat terpisah.','']
    (RUN/'REPORT.md').write_text('\n'.join(lines),encoding='utf-8');return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--classes',nargs='+',type=int,choices=range(1,5),default=[1,2,3,4]);p.add_argument('--audit-only',action='store_true');args=p.parse_args();RUN.mkdir(parents=True,exist_ok=True)
    if args.audit_only:
        result=audit_all();print(json.dumps({k:v for k,v in result.items() if k not in ('classes','inventory','coverage')}),flush=True);return
    for grade in args.classes:run_class(grade)
    summaries=[]
    for grade in range(1,5):
        final=bank.base_for(grade)/'hasil_validasi'
        if load(final/'manifest.json')['schemaVersion']!=SCHEMA:continue
        verify(final);summaries.append(load(final/'bukti_validasi/codex_local_review.json')['summary'])
    atomic_json(RUN/'summary.json',{'classes':summaries,'apiCalls':0,'totalAdded':sum(s['added'] for s in summaries),'totalActive':sum(s['active'] for s in summaries)})


if __name__=='__main__':main()
