"""Finish local publications, retain evidence, and audit actual exercise availability."""
from collections import Counter
from copy import deepcopy
from pathlib import Path
import sys
import json
import shutil
import subprocess
import tempfile
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from scripts.generate_targeted_replenishment import ROOT,RUN,load,digest,h,verify,SCHEMA
from app.services.exercise.workflow import atomic_json,batch_lock
from app.services.exercise.replenishment_math import m
from app.services.exercise.replenishment_format import exact_value
from app.services.exercise.schema import ExerciseFile
from app.presentation.latex import math_spans,normalize_text,MATH,COMMANDS
from app.ingestion.question_sync import load_sources,report_catalog,coverage
import re


def finalize(name,force=False):
    base=ROOT/'output/exercise'/name/'batch01';final=base/'hasil_validasi'
    with batch_lock(base):
        verify(final);manifest=load(final/'manifest.json')
        if manifest.get('finalization') and not force:return manifest['finalization']
        master=load(base/'soal_exercise_db.json');source_meta=load(base/'soal_exercise_meta.json')
        rows=load(final/'validation_results.json');meta=load(final/'validation_results_meta.json');audit=load(final/'bukti_validasi/codex_targeted_review.json')
        masters={q['_id']:q for q in master['items']};published={q['_id']:q for q in rows};raw_files={};repairs=[];math_repairs=[]
        for rec in audit['items']:
            qid=rec['questionId'];row=published[qid];info=source_meta[qid];proof=info['local_math_check'];value=exact_value(proof['value'])
            if info['jenis_soal']=='v2_turunan_hasil_kali_balik' and 'memberi f′=' in rec['solution']:
                solution=re.sub(r'memberi f′=(.+?)\. Kedua',lambda match:'memberi $f^\\prime(x)='+match[1]+'$. Kedua',rec['solution'])
                assert solution!=rec['solution']
                raw_path=base/f"bab{int(info['bab_id'].split('-B')[1]):02d}"/f"{info['subbab_kode']}_{info['level_target']}.json"
                raw=raw_files.setdefault(raw_path,load(raw_path));q=next(q for q in raw['soal'] if q['id']==info['id'])
                q.update(pembahasan=solution,alasan_benar=solution);info['pembahasan']=solution;meta[qid]['pembahasan']=solution
                next(o for o in row['options'] if o['option_id']==row['jawaban'])['alasan']='Benar: '+solution
                masters[qid]['options']=deepcopy(row['options'])
                rec.update(solution=solution,sourceHash=h(masters[qid]),publishedHash=h(row),publishedQuestion=deepcopy(row))
                meta[qid]['local_review']=deepcopy(rec);math_repairs.append(qid)
            if not ('peluang' in row['soal_text'].lower() or 'proporsi' in row['soal_text'].lower()) or not 0<=value<=1:continue
            if all(0<=exact_value(v)<=1 for v in proof['options']):continue
            wrong=[]
            for v in [1-value,value**2,value/2,(1+value)/2,exact_value('1/3'),exact_value('2/3'),0,1]:
                if 0<=v<=1 and v!=value and v not in wrong:wrong.append(v)
                if len(wrong)==3:break
            assert len(wrong)==3
            raw_path=base/f"bab{int(info['bab_id'].split('-B')[1]):02d}"/f"{info['subbab_kode']}_{info['level_target']}.json"
            raw=raw_files.setdefault(raw_path,load(raw_path));q=next(q for q in raw['soal'] if q['id']==info['id'])
            replacements=[]
            for v in wrong:
                reason=('Menggunakan peluang komplemen, sedangkan yang diminta adalah kejadian semula.' if v==1-value else 'Menggunakan perbandingan yang tidak memenuhi seluruh syarat kejadian; perhitungan yang sesuai memberi '+m(value)+'.')
                replacements.append({'teks':m(v),'alasan':reason})
            q['distraktor']=replacements
            for option,replacement in zip([o for o in row['options'] if o['option_id']!=row['jawaban']],replacements):
                option.update(text=replacement['teks'],alasan='Salah: '+replacement['alasan'])
            masters[qid]['options']=deepcopy(row['options']);proof['options']=[str(value),*[str(v) for v in wrong]]
            rec.update(sourceHash=h(masters[qid]),publishedHash=h(row),publishedQuestion=deepcopy(row))
            meta[qid]['local_math_check']=deepcopy(proof);meta[qid]['local_review']=deepcopy(rec)
            repairs.append(qid)
        backup=RUN/'backups'/name;stamp=digest(final/'manifest.json')[:16]
        frozen_master=backup/f'final_{stamp}_master.json';frozen_meta=backup/f'final_{stamp}_meta.json'
        atomic_json(frozen_master,master);atomic_json(frozen_meta,source_meta)
        staging=Path(tempfile.mkdtemp(prefix='final_review_',dir=RUN));shutil.copytree(final,staging,dirs_exist_ok=True)
        # Evidence from the first local review remains available in the same folder.
        prior=Path(manifest['sourceFiles']['previousManifest']['path']);old=prior.parent/f'v2_{digest(prior)[:16]}_previous_publication'/'bukti_validasi'
        if old.is_dir():
            for src in old.rglob('*'):
                if src.is_file():
                    dest=staging/'bukti_validasi'/src.relative_to(old);dest.parent.mkdir(parents=True,exist_ok=True)
                    if dest.exists():assert dest.read_bytes()==src.read_bytes()
                    else:shutil.copyfile(src,dest)
        code_dir=staging/'bukti_validasi/reviewed_code';code_dir.mkdir(exist_ok=True)
        code=[*sorted((ROOT/'app/services/exercise').glob('targeted_*.py')),ROOT/'scripts/generate_targeted_replenishment.py',Path(__file__)]
        for src in code:shutil.copyfile(src,code_dir/src.name)
        atomic_json(staging/'validation_results.json',rows);atomic_json(staging/'validation_results_meta.json',meta);atomic_json(staging/'bukti_validasi/codex_targeted_review.json',audit)
        details={'class':name,'questions':len(audit['items']),'probabilityOptionRepairs':len(repairs),'mathDelimiterRepairs':len(math_repairs),'apiCalls':0,'confidenceMeasured':False}
        atomic_json(staging/'bukti_validasi/quality_finalization.json',{**details,'repairedQuestionIds':repairs,'mathDelimiterQuestionIds':math_repairs})
        manifest['sourceFiles']['exerciseEnvelope']={'path':str(frozen_master),'sha256':digest(frozen_master)}
        manifest['sourceFiles']['exerciseMetadata']={'path':str(frozen_meta),'sha256':digest(frozen_meta)}
        manifest['liveInputs']={str(base/'soal_exercise_db.json'):{'path':str(base/'soal_exercise_db.json'),'sha256':digest(frozen_master)},str(base/'soal_exercise_meta.json'):{'path':str(base/'soal_exercise_meta.json'),'sha256':digest(frozen_meta)}}
        manifest['finalization']=details
        manifest['outputs']={p.relative_to(staging).as_posix():{'sha256':digest(p),'bytes':p.stat().st_size} for p in staging.rglob('*') if p.is_file() and p!=staging/'manifest.json'}
        atomic_json(staging/'manifest.json',manifest);verify(staging,False)
        mutable=[base/'soal_exercise_db.json',base/'soal_exercise_meta.json',base/'reference_replenishment_state.json',base/'reference_replenishment_manifest.json',*raw_files]
        rollback={p:p.read_bytes() for p in mutable};retired=backup/f'final_{stamp}_previous_publication';assert not retired.exists()
        for p in [final,staging,retired,*mutable]:assert p.resolve().is_relative_to(ROOT.resolve())
        journal=RUN/f'finalization_{name}.json';recovery={}
        for p in mutable:
            target=backup/f"final_{stamp}_rollback_{p.relative_to(base).as_posix().replace('/','__')}";shutil.copyfile(p,target);recovery[str(p)]=str(target)
        atomic_json(journal,{'phase':'prepared','rollback':recovery,'staging':str(staging),'retired':str(retired)})
        moved=False
        try:
            for p,raw in raw_files.items():ExerciseFile.model_validate(raw);atomic_json(p,raw)
            atomic_json(base/'soal_exercise_db.json',master);atomic_json(base/'soal_exercise_meta.json',source_meta)
            reference=load(base/'reference_replenishment_manifest.json')
            for p in [base/'soal_exercise_db.json',base/'soal_exercise_meta.json',*raw_files]:reference['files'][p.relative_to(base).as_posix()]=digest(p)
            atomic_json(base/'reference_replenishment_manifest.json',reference)
            state=load(base/'reference_replenishment_state.json');state['manifestSha256']=digest(base/'reference_replenishment_manifest.json');atomic_json(base/'reference_replenishment_state.json',state)
            final.rename(retired);moved=True;staging.rename(final);verify(final)
        except Exception:
            if moved:
                if final.exists():final.rename(backup/f'final_{stamp}_failed_publication')
                retired.rename(final)
            for p,data in rollback.items():p.write_bytes(data)
            raise
        atomic_json(journal,{'phase':'committed',**details})
        return details


def audit_all():
    progress=load(RUN/'targeted_generation_progress.json');assert progress['completed']==progress['target']==1751
    counts={};expressions=set();seen=set();old_count=0;new_count=0;raw_questions=0
    for name in sorted(progress['classes']):
        base=ROOT/'output/exercise'/name/'batch01';final=base/'hasil_validasi';verify(final);manifest=load(final/'manifest.json')
        rows=load(final/'validation_results.json');meta=load(final/'validation_results_meta.json');items=load(final/'bukti_validasi/codex_targeted_review.json')['items'];source_meta=load(base/'soal_exercise_meta.json');newids={q['questionId'] for q in items}
        original_master=load(manifest['sourceFiles']['originalMaster']['path']);live_master=load(base/'soal_exercise_db.json')
        assert live_master['items'][:len(original_master['items'])]==original_master['items']
        original_meta=load(manifest['sourceFiles']['originalSourceMetadata']['path'])
        assert all(source_meta[k]==v for k,v in original_meta.items())
        reference=load(base/'reference_replenishment_manifest.json')
        assert all(digest(base/p)==sha for p,sha in reference['files'].items())
        state=load(base/'reference_replenishment_state.json');assert state['reviewMode']=='local_without_external_api' and state['validationOwner']=='codex_local_review'
        old_count+=len(rows)-len(newids);new_count+=len(newids);counts[name]={'added':len(newids),'levels':dict(Counter(i['assessedLevel'] for i in items))}
        raw_by={}
        for path in sorted(base.glob('bab*/*_*.json')):
            if not re.fullmatch(r'[A-Z]_(easy|medium|hard)\.json',path.name):continue
            raw=load(path);ExerciseFile.model_validate(raw)
            for q in raw['soal']:
                assert q['id'] not in raw_by;raw_by[q['id']]=q
            # Compare retained items with the frozen file before this round.
            prefix=Path(manifest['sourceFiles']['previousManifest']['path']);backup=prefix.parent;stamp=digest(prefix)[:16]
            original=backup/f"v2_{stamp}_rollback_{path.relative_to(base).as_posix().replace('/','__')}"
            if original.exists():
                old=load(original)['soal'];assert raw['soal'][:len(old)]==old,'An existing raw question changed'
        for item in items:
            qid=item['questionId'];assert qid not in seen;seen.add(qid);info=meta[qid];row=next(q for q in rows if q['_id']==qid);q=raw_by[info['id']];raw_questions+=1
            assert q['pertanyaan']==row['soal_text'] and info['level_target']==row['cognitive_level']
            assert row['options'][next(i for i,o in enumerate(row['options']) if o['option_id']==row['jawaban'])]['text']==q['jawaban_benar']
            assert {o['text'] for o in row['options']}=={q['jawaban_benar'],*[d['teks'] for d in q['distraktor']]}
            assert len(row['options'])==4 and len({o['text'] for o in row['options']})==4
            assert row['status']=='active' and row['confidence_score']==0 and info['validasi']['api_runs']==0
            assert info['validasi']['training_evidence_qualified'] is False
            for text in [q['pertanyaan'],q['pembahasan'],q['jawaban_benar'],*[v['teks'] for v in q['distraktor']],*[v['alasan'] for v in q['distraktor']]]:
                assert text.count('$')%2==0
                assert not re.search(r'[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]',text)
                expressions.update(math_spans(text))
                outside=MATH.sub('',text)
                assert not re.search(r'\\(?:'+ '|'.join(COMMANDS)+r')\b',outside),('Undelimited math',qid,outside)
        print(json.dumps({'class':name,'verifiedNew':len(newids),'preservedOld':len(rows)-len(newids)}),flush=True)
    request=RUN/'final_math_expressions.json';atomic_json(request,[{'id':i,'tex':tex,'display':display} for i,(tex,display) in enumerate(sorted(expressions))])
    rendered=json.loads(subprocess.run(['node',str(ROOT/'scripts/latex_render_check.cjs'),str(request)],capture_output=True,text=True,encoding='utf-8',check=True).stdout);atomic_json(RUN/'final_render_audit.json',rendered);assert not rendered['errors']
    questions=load_sources(ROOT/'output');inventory=coverage(questions,report_catalog(ROOT/'API_DOCUMENTATION/Pesan_eror.md'))
    scope=set(counts);scope_rows=[row for row in inventory['rows'] if row['class_key'] in scope];remaining=[row for row in scope_rows if row['shortfall']];assert not remaining
    assert old_count==10360 and new_count==raw_questions==1751
    result={'scope':'kelas5_to_kelas12_including_tl','generated':new_count,'preservedExistingExercise':old_count,'apiCalls':0,'confidenceScore':0,'remainingQuestions':0,'remainingLevelSlots':0,'auditedSubchapters':len(scope_rows),'auditedLevelSlots':3*len(scope_rows),'classes':counts,'mathRendering':rendered,'inventory':scope_rows,'outsideScope':{'shortfall':sum(r['shortfall'] for r in inventory['rows'] if r['class_key'] not in scope),'note':'Kelas 1–4 di luar target pengisian 1.751 soal ini.'}}
    atomic_json(RUN/'final_targeted_audit.json',result);atomic_json(RUN/'remaining_after_targeted.json',{'scope':result['scope'],'questionsNeeded':0,'jobs':[],'apiCalls':0})
    lines=['# Pengisian kekurangan soal selesai','',f'**1.751/1.751 soal (100%). Sisa kekurangan dalam cakupan: 0.**','',f'Pemeriksaan lokal meliputi {len(scope_rows)} subbab dan {3*len(scope_rows)} kombinasi subbab-level. Minimum tiap level: SD 10, SMP 15, SMA 20.','', '| Kelas | Tambahan easy | Medium | Hard | Total |','|---|---:|---:|---:|---:|']
    for name,info in counts.items():lines.append(f"| {name} | {info['levels'].get('easy',0)} | {info['levels'].get('medium',0)} | {info['levels'].get('hard',0)} | {info['added']} |")
    lines+=['',f"Seluruh {old_count:,} soal latihan yang sudah ada dipertahankan. Soal baru tetap berada di batch01/bab masing-masing, dengan format JSON standar dan canonical hasil_validasi diperbarui.",'',f"Render KaTeX: {rendered['checked']} ekspresi unik, {len(rendered['errors'])} error. Sertifikat hitung, konsistensi pilihan, ID, metadata, serta urutan soal lama diperiksa ulang.",'','Tidak ada pemanggilan API. Label adalah penilaian kesulitan lokal Codex berdasarkan isi, belum kalibrasi empiris. Confidence 0 berarti belum diukur; hasil lokal tidak dipakai sebagai bukti pelatihan berlabel AI independen.','', 'Audit ini terhadap berkas lokal, belum menyinkronkan database production. Kelas 1–4 bukan cakupan pengisian ini; audit katalog masih mencatat kekurangan 2.550 soal untuk kelas tersebut.','']
    (RUN/'TARGETED_PROGRESS.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['inventory','classes','mathRendering']}),flush=True)
    return result


if __name__=='__main__':
    import sys
    for name in sorted(load(RUN/'targeted_generation_progress.json')['classes']):print(json.dumps(finalize(name)),flush=True)
    audit_all()
