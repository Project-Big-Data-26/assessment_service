"""Verify append-only generation and write per-class previews. No API calls."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.services.exercise.schema import ExerciseFile
from app.services.exercise.workflow import atomic_json,digest,load,validation_allowed

RUN=ROOT/'runs/exercise_replenishment/codex_batch01'


def main():
    progress=load(RUN/'progress.json');jobs={j['job_id']:j for j in load(RUN/'jobs.json')}
    report={'target':progress['target'],'newCandidates':0,'classes':{},'errors':[],
            'validationApiCalls':0,'productionWrites':0,'state':'generation_only'}
    formulas=set();all_added_ids=set()
    def check(condition,message):
        if not condition:report['errors'].append(message)
    for name,entry in progress['classes'].items():
        base=ROOT/'output/exercise'/name/'batch01';backup=RUN/'backups'/name
        master=load(base/'soal_exercise_db.json')['items'];meta=load(base/'soal_exercise_meta.json')
        old=load(backup/'soal_exercise_db.json')['items'];oldmeta=load(backup/'soal_exercise_meta.json')
        check(master[:len(old)]==old,f'{name}: old master prefix changed')
        check(all(meta.get(qid)==value for qid,value in oldmeta.items()),f'{name}: old metadata changed')
        added=master[len(old):];report['newCandidates']+=len(added)
        check(len(added)==entry['target']==entry['added'],f'{name}: class total differs')
        check(len({row['_id'] for row in master})==len(master),f'{name}: duplicate master IDs')
        check(not validation_allowed(base),f'{name}: automatic validation must stay blocked')
        manifest=load(base/'reference_replenishment_manifest.json')
        check(all(digest(base/rel)==value for rel,value in manifest['files'].items()),f'{name}: generation checksum changed')
        check(load(base/'reference_replenishment_state.json')['manifestSha256']==digest(base/'reference_replenishment_manifest.json'),f'{name}: manifest binding differs')
        frozen=load(base/'_replenishment/blueprints.json');frozen_hash=digest(base/'_replenishment/blueprints.json')
        previews=[f'# Kandidat penambalan {name} — batch01','',
                  f'{len(added)} kandidat baru; belum divalidasi Gemini dan belum aktif.',
                  'Soal lama dipertahankan. Acuan di bawah adalah snapshot saat generate.','']
        new_by_id={row['_id']:row for row in added}
        seen={re.sub(r'\s+',' ',row['soal_text'].casefold()).strip() for row in old}
        for row in added:
            qid=row['_id'];info=meta[qid];reference=info['acuan'];original=frozen[reference['id']]
            check(qid not in all_added_ids,f'Duplicate new ID across classes: {qid}');all_added_ids.add(qid)
            check(original['class']==name and original['code']==info['subbab_kode'] and info['bab_id'].endswith('-B'+str(original['bab'])),f'{qid}: reference crosses scope')
            check(original['item']['status']=='active' and original['item']['cognitive_level'] in ('easy','medium','hard'),f'{qid}: reference not validated active')
            original_key=next(o['text'] for o in original['item']['options'] if o['option_id']==original['item']['jawaban'])
            check(reference['teks']==original['item']['soal_text'] and reference['jawaban']==original_key and reference['source_sha256']==frozen_hash,f'{qid}: original reference differs')
            check(row['status']=='inactive' and row['cognitive_level'] is None and row['cognitive_score'] is None,f'{qid}: candidate prematurely published')
            check({o['option_id'] for o in row['options']}==set('ABCD') and len({o['text'] for o in row['options']})==4,f'{qid}: options invalid')
            stem=re.sub(r'\s+',' ',row['soal_text'].casefold()).strip()
            check(stem not in seen,f'{qid}: repeated class stem');seen.add(stem)
            for text in [row['soal_text'],info['pembahasan'],*[o['text'] for o in row['options']]]:
                check(text.count('$')%2==0 and '$$' not in text,f'{qid}: delimiter error')
                parts=re.findall(r'\$([^$]+)\$',text)
                formulas.update(parts)
                plain=re.sub(r'\$[^$]+\$','',text)
                check(not re.search(r'\\[A-Za-z]+',plain),f'{qid}: bare LaTeX command')
            previews += [f'## {info["id"]} — target {info["level_target"]}','',row['soal_text'],'']
            previews += [f'- {o["option_id"]}. {o["text"]}' for o in row['options']]
            previews += ['',f'Kunci usulan: **{row["jawaban"]}**','',info['pembahasan'],'',
                         '### Soal acuan asli','',original['item']['soal_text'],'']
            previews += [f'- {o["option_id"]}. {o["text"]}' for o in original['item']['options']]
            previews += ['',f'Kunci acuan: {original["item"]["jawaban"]}. ID: `{reference["id"]}`.',
                         f'Sumber: `{original["source"]}`. Label acuan: `{original["item"]["cognitive_level"]}`.','', '---','']
        for job_id,status in progress['jobs'].items():
            if jobs[job_id]['class_key']!=name:continue
            job=jobs[job_id];path=ROOT/status['path'];raw=load(path);ExerciseFile.model_validate(raw)
            original_path=backup/path.relative_to(base)
            old_raw=load(original_path) if original_path.exists() else None
            old_questions=old_raw['soal'] if old_raw else []
            check(raw['soal'][:len(old_questions)]==old_questions,f'{job_id}: old raw questions changed')
            new=raw['soal'][len(old_questions):]
            check(len(new)==job['shortfall'] and len(new)+job['active_now']==job['required'],f'{job_id}: target level count differs')
            check([q['id'] for q in new]==status['ids'],f'{job_id}: progress ID list differs')
            for question in new:
                qid=hashlib.md5(question['id'].encode()).hexdigest()[:24]
                check(qid in new_by_id and new_by_id[qid]['soal_text']==question['pertanyaan'],f'{job_id}: raw/master mismatch')
                check(meta[qid]['level_target']==job['level_target'],f'{qid}: target level mismatch')
        preview=base/'_replenishment/PREVIEW.md';preview.write_text('\n'.join(previews)+'\n',encoding='utf-8')
        report['classes'][name]={'old':len(old),'new':len(added),'total':len(master),'preview':str(preview.relative_to(ROOT))}
    check(report['newCandidates']==report['target']==2028,'Overall candidate target not met')
    report['uniqueMathExpressions']=len(formulas)
    atomic_json(RUN/'math_expressions.json',sorted(formulas))
    atomic_json(RUN/'audit.json',report)
    print(json.dumps({k:v for k,v in report.items() if k!='classes'},ensure_ascii=False))
    return 1 if report['errors'] else 0


if __name__=='__main__':raise SystemExit(main())
