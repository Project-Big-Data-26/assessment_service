"""Generate authored reference variants into batch01, without external APIs."""
from __future__ import annotations
import argparse
from collections import Counter,defaultdict
from datetime import datetime,timezone
from difflib import SequenceMatcher
import hashlib
import json
from pathlib import Path
import random
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.ingestion.question_sync import load_sources
from app.services.exercise.schema import ExerciseFile,Soal
from app.services.exercise.workflow import atomic_json,batch_lock,digest,load

RUN=ROOT/'runs/exercise_replenishment/codex_batch01'
CLASSES=['kelas5','kelas6','kelas7','kelas8','kelas9','kelas10','kelas11','kelas11_tl','kelas12','kelas12_tl']


def normalized(text):
    return re.sub(r'\s+',' ',text.casefold()).strip()


def save_progress(progress):
    atomic_json(RUN/'progress.json',progress)
    count=sum(row['added'] for row in progress['classes'].values())
    lines=['# Progres generate penambalan batch01','',f'Kandidat tersimpan: **{count} / {progress["target"]}**.',
           f'Sisa: **{progress["target"]-count}**. Validasi Gemini belum dijalankan.','',
           '| Kelas | Target kandidat | Tersimpan | Status |','|---|---:|---:|---|']
    for name in CLASSES:
        entry=progress['classes'][name]
        lines.append(f'| {name} | {entry["target"]} | {entry["added"]} | {entry["status"]} |')
    (RUN/'PROGRESS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')


def factory(book,bab,code,level,r):
    grade=int(book.split('_')[0][5:])
    if grade<=6:
        from app.services.exercise.replenishment_sd import generate
    elif grade<=9:
        from app.services.exercise.replenishment_smp import generate
    elif book.endswith('_tl'):
        from app.services.exercise.replenishment_tl import generate
    else:
        from app.services.exercise.replenishment_sma import generate
    return generate(book,bab,code,level,r)


def initialize():
    if (RUN/'progress.json').exists():return load(RUN/'progress.json'),load(RUN/'jobs.json')
    plan=load(ROOT/'runs/exercise_replenishment/plan.json')
    jobs=[j for j in plan['jobs'] if j['class_key'] in CLASSES]
    targets=Counter()
    for job in jobs:targets[job['class_key']]+=job['shortfall']
    if sum(targets.values())!=2028:raise ValueError('Audit scope changed; inspect target before creating a new run')
    progress={'schemaVersion':'codex-reference-replenishment-v1','target':sum(targets.values()),
              'generationOnly':True,'apiCalls':0,'validationStatus':'validation_pending','jobs':{},
              'classes':{name:{'target':targets[name],'added':0,'status':'queued'} for name in CLASSES}}
    atomic_json(RUN/'jobs.json',jobs);save_progress(progress)
    return progress,jobs


def run_class(name,progress,jobs):
    source_questions=load_sources(ROOT/'output')
    refs=defaultdict(list)
    for source in source_questions:
        item=source.item
        if source.class_key==name and item.get('status')=='active' and item.get('cognitive_level') in ('easy','medium','hard') and not item.get('image_url'):
            refs[(source.chapter_no,source.code)].append(source)
    base=ROOT/'output/exercise'/name/'batch01'
    relevant=[j for j in jobs if j['class_key']==name]
    with batch_lock(base):
        state_file=base/'reference_replenishment_state.json'
        if state_file.exists() and load(state_file).get('phase')=='validation_authorized':
            raise ValueError('Generation frozen after validation authorization')
        backup=RUN/'backups'/name;backup.mkdir(parents=True,exist_ok=True)
        def back_up(path):
            if path.exists():
                target=backup/path.relative_to(base)
                if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(path.read_bytes())
        master_file=base/'soal_exercise_db.json';meta_file=base/'soal_exercise_meta.json'
        for path in [master_file,meta_file,base/'extraction_ready.json']:back_up(path)
        atomic_json(state_file,{'class':name,'batch':'batch01','phase':'generating','validationStatus':'validation_pending'})
        (base/'extraction_ready.json').unlink(missing_ok=True)
        envelope=load(master_file);metadata=load(meta_file)
        # Freeze source payloads before touching any source metadata.
        frozen_file=base/'_replenishment/blueprints.json'
        if frozen_file.exists():frozen=load(frozen_file)
        else:
            frozen={q.qid:{'source':q.source,'kind':q.kind,'class':q.class_key,'bab':q.chapter_no,
                           'code':q.code,'item':q.item} for pool in refs.values() for q in pool}
            atomic_json(frozen_file,frozen)
        frozen_hash=digest(frozen_file)
        stems=set()
        for path in (ROOT/'output/exercise'/name).glob('batch*/soal_exercise_db.json'):
            stems.update(normalized(item['soal_text']) for item in load(path).get('items',[]))
        progress['classes'][name]['status']='generating';save_progress(progress)
        for job in relevant:
            key=job['job_id']
            if progress['jobs'].get(key,{}).get('status')=='complete':continue
            chapter=job['chapter_no'];code=job['code'];level=job['level_target'];wanted=job['shortfall']
            pool=refs[chapter,code]
            exercise=[q for q in pool if q.kind=='exercise'];pool=exercise or pool
            if not pool:raise ValueError(f'No validated text blueprint for {key}')
            matching=[q for q in pool if q.item['cognitive_level']==level];pool=matching or pool
            path=base/f'bab{chapter:02d}'/f'{code}_{level}.json';back_up(path)
            raw=load(path) if path.exists() else {'book':name,'bab_no':chapter,'subbab':code,'level':level,'batch':1,'skill_versi':'v1','soal':[]}
            last=max((int(q['id'].rsplit('-',1)[1]) for q in raw['soal']),default=0)
            existing_additions=[q for q in raw['soal'] if (q.get('catatan') or '').startswith('codex-replenishment:')]
            if existing_additions:raise ValueError(f'Uncommitted additions exist for {key}; inspect recovery before rerunning')
            seed=int(hashlib.sha256(key.encode()).hexdigest()[:16],16)
            r=random.Random(seed);new=[];newrows=[];newmeta={};proofs=[]
            for index in range(wanted):
                for trial in range(300):
                    draft=factory(name,chapter,code,level,r)
                    if normalized(draft.question) not in stems:break
                else:raise ValueError(f'Unique generation capacity exhausted for {key}')
                stems.add(normalized(draft.question));reference=r.choice(pool)
                original=reference.item;correct=next(o['text'] for o in original['options'] if o['option_id']==original['jawaban'])
                working=f'{name}-b{chapter:02d}-{code.lower()}-{level}-bt01-{last+index+1:03d}'
                qid=hashlib.md5(working.encode()).hexdigest()[:24]
                if qid in metadata:raise ValueError('Generated ID collision')
                cognitive={'easy':'C2','medium':'C4','hard':'C5'}[level]
                question={'id':working,'tipe_generate':'variasi','variasi_cara':'konteks',
                          'acuan':{'sumber':reference.kind+'_validated','id':reference.qid,
                                   'teks':original['soal_text'],'jawaban':correct,
                                   'snapshot':'_replenishment/blueprints.json','source_sha256':frozen_hash},
                          'cognitive_c':cognitive,'jumlah_langkah':{'easy':2,'medium':3,'hard':4}[level],
                          'jenis_soal':draft.kind[:60],
                          'alasan_level':f'Target {level}; variasi konsep {draft.kind.replace("_"," ")}. Kesulitan final menunggu validasi Gemini.',
                          'stimulus':None,'gambar':[],'pertanyaan':draft.question,'jawaban_benar':draft.answer,
                          'alasan_benar':draft.explanation,
                          'distraktor':[{'teks':d,'alasan':'Hasil ini muncul dari kekeliruan memilih operasi, substitusi, atau langkah hitung; tidak memenuhi perhitungan pada pembahasan.'} for d in draft.distractors],
                          'pembahasan':draft.explanation,
                          'catatan':f'codex-replenishment:{key}; generation_only; level target bukan label tervalidasi.',
                          'dipaksa_kuota':False}
                Soal.model_validate(question)
                new.append(question)
                options=[{'text':d['teks'],'alasan':'Salah: '+d['alasan']} for d in question['distraktor']]
                r.shuffle(options);position=r.randrange(4)
                options.insert(position,{'text':draft.answer,'alasan':'Benar: '+draft.explanation})
                for letter,option in zip('ABCD',options):option['option_id']=letter
                now=datetime.now(timezone.utc).isoformat()
                newrows.append({'_id':qid,'berkas_id':None,'kelas_id':name,'subbab_id':job['subchapter_name'],
                                'soal_text':draft.question,'image_url':[],'soal_type':'Pilihan Ganda',
                                'options':options,'matching_pairs':None,'jawaban':'ABCD'[position],
                                'cognitive_level':None,'cognitive_score':None,'confidence_score':None,'status':'inactive',
                                'created_at':now,'updated_at':now})
                newmeta[qid]={'id':working,'batch':1,'bab_id':next((info['bab_id'] for info in metadata.values()
                                                              if info['bab_id'].endswith('-B'+str(chapter))),
                                                              ('SMA11L-B'+str(chapter) if name=='kelas11_tl' else 'SMP7-B'+str(chapter))),
                              'subbab_kode':code,'level_target':level,'cognitive_score_target':{'easy':600,'medium':1000,'hard':1400}[level],
                              'tipe_generate':'variasi','variasi_cara':'konteks','acuan':question['acuan'],
                              'cognitive_c':cognitive,'jumlah_langkah':question['jumlah_langkah'],'jenis_soal':draft.kind,
                              'pembahasan':draft.explanation,'catatan':question['catatan'],'dipaksa_kuota':False,
                              'kapasitas_kurang':None,'skill_versi':'v1','generator':'codex:reference-parameterized-v1',
                              'bergambar':False,'gambar':[],'deskripsi_gambar':None,'warning':[],
                              'validation_status':'validation_pending','local_math_check':draft.proof}
                proofs.append({'id':working,**draft.proof})
            raw['soal'].extend(new);ExerciseFile.model_validate(raw)
            envelope['items'].extend(newrows);metadata.update(newmeta)
            atomic_json(path,raw);atomic_json(master_file,envelope);atomic_json(meta_file,metadata)
            proof_path=base/'_replenishment'/f'{chapter:02d}_{code}_{level}_checks.json';atomic_json(proof_path,proofs)
            progress['jobs'][key]={'status':'complete','added':wanted,'path':str(path.relative_to(ROOT)),
                                   'ids':[q['id'] for q in new]}
            progress['classes'][name]['added']+=wanted;save_progress(progress)
            print(f'{name} {chapter}/{code}/{level}: +{wanted}; class {progress["classes"][name]["added"]}/{progress["classes"][name]["target"]}',flush=True)
        changed=[master_file,meta_file,frozen_file]
        changed+=list((base/'_replenishment').glob('*_checks.json'))
        changed+=[base/f'bab{j["chapter_no"]:02d}'/f'{j["code"]}_{j["level_target"]}.json' for j in relevant]
        manifest={'class':name,'batch':'batch01','added':progress['classes'][name]['added'],
                  'generationOnly':True,'files':{p.relative_to(base).as_posix():digest(p) for p in changed}}
        manifest_file=base/'reference_replenishment_manifest.json';atomic_json(manifest_file,manifest)
        atomic_json(state_file,{'class':name,'batch':'batch01','phase':'generation_complete','validationStatus':'validation_pending',
                                'manifestSha256':digest(manifest_file),'added':manifest['added']})
        progress['classes'][name]['status']='generation_complete';save_progress(progress)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--classes',nargs='+',choices=CLASSES,required=True)
    args=p.parse_args();progress,jobs=initialize()
    # Hold only the classes in this replenishment scope; no API/training is started.
    for name in CLASSES:
        base=ROOT/'output/exercise'/name/'batch01'
        with batch_lock(base):
            state=base/'reference_replenishment_state.json'
            if not state.exists():
                marker=base/'extraction_ready.json'
                if marker.exists():
                    backup=RUN/'backups'/name/'extraction_ready.json';backup.parent.mkdir(parents=True,exist_ok=True)
                    if not backup.exists():backup.write_bytes(marker.read_bytes())
                    marker.unlink()
                atomic_json(state,{'class':name,'batch':'batch01','phase':'queued_generation',
                                   'validationStatus':'validation_pending'})
    for name in args.classes:run_class(name,progress,jobs)
    print('Progress:',RUN/'PROGRESS.md')


if __name__=='__main__':main()
