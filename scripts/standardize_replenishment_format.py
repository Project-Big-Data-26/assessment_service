"""Standardize generated additions after relocating audits outside output/.

No question or answer is generated here. Original question/evidence rows stay intact.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.services.exercise.schema import ExerciseFile
from app.services.exercise.workflow import atomic_json,batch_lock,digest,load,reference_manifest_intact
from app.services.exercise.replenishment_format import standard_question,distractor_reason

RUN=ROOT/'runs/exercise_replenishment/codex_batch01'


def standardize_class(name,progress):
    base=ROOT/'output/exercise'/name/'batch01';audit_dir=RUN/'audit'/name
    snapshot=audit_dir/'blueprints.json'
    if not snapshot.is_file():raise ValueError(f'{name}: relocate the audit directory before standardization')
    snapshot_hash=digest(snapshot);snapshot_reference=snapshot.relative_to(ROOT).as_posix()
    frozen=load(snapshot)
    jobs=[entry for entry in progress['jobs'].values()
          if entry['path'].replace('\\','/').startswith(f'output/exercise/{name}/')]
    if sum(len(entry['ids']) for entry in jobs)!=progress['classes'][name]['target']:
        raise ValueError('Progress index does not match class target; no data written')
    backup=RUN/'format_backups'/name
    with batch_lock(base):
        state_path=base/'reference_replenishment_state.json';state=load(state_path)
        if state.get('phase')=='validation_authorized':raise ValueError('Do not rewrite an approved batch')
        old_manifest=load(base/'reference_replenishment_manifest.json')
        # Old audit paths have just moved; verify their exact bytes at the new location.
        for relative,checksum in old_manifest.get('files',{}).items():
            source=audit_dir/Path(relative).name if relative.startswith('_replenishment/') else base/relative
            if digest(source)!=checksum:raise ValueError(f'{name}: unexpected change before migration: {relative}')
        if old_manifest.get('auditFiles') and not reference_manifest_intact(base,old_manifest):
            raise ValueError('Audit hash differs before standardization')
        master_path=base/'soal_exercise_db.json';meta_path=base/'soal_exercise_meta.json'
        master=load(master_path);metadata=load(meta_path);rows={q['_id']:q for q in master['items']}
        affected=[master_path,meta_path,state_path,base/'reference_replenishment_manifest.json',
                  *[ROOT/entry['path'] for entry in jobs]]
        for path in affected:
            target=backup/path.relative_to(base)
            if not target.exists():target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(path.read_bytes())
        state.update(phase='formatting',validationStatus='validation_pending');atomic_json(state_path,state)
        count=0
        for entry in jobs:
            path=ROOT/entry['path'];raw=load(path);ids=set(entry['ids']);seen=set()
            for index,question in enumerate(raw['soal']):
                if question['id'] not in ids:continue
                seen.add(question['id']);qid=hashlib.md5(question['id'].encode()).hexdigest()[:24]
                before=deepcopy(question)
                reference=question['acuan'];original=frozen[reference['id']]
                if (reference['teks']!=original['item']['soal_text']
                        or reference['source_sha256']!=snapshot_hash):
                    raise ValueError('Frozen reference differs')
                reference['snapshot']=snapshot_reference
                proof=metadata[qid]['local_math_check']
                for option_index,distractor in enumerate(question['distraktor']):
                    distractor['alasan']=distractor_reason(question,option_index,proof)
                question=standard_question(question);raw['soal'][index]=question
                # Update only the new question's provenance and option explanations.
                metadata[qid]['acuan']=deepcopy(question['acuan'])
                reason_by_text={d['teks']:d['alasan'] for d in question['distraktor']}
                row=rows[qid]
                for option in row['options']:
                    if option['option_id']!=row['jawaban']:
                        option['alasan']='Salah: '+reason_by_text[option['text']]
                assert question['id']==before['id'] and question['pertanyaan']==before['pertanyaan']
                assert question['jawaban_benar']==before['jawaban_benar']
                count+=1
            if seen!=ids:raise ValueError('Progress refers to missing questions')
            ExerciseFile.model_validate(raw);atomic_json(path,raw)
        if count!=progress['classes'][name]['target']:raise ValueError('Class question count changed')
        atomic_json(master_path,master);atomic_json(meta_path,metadata)
        files=[master_path,meta_path,*[ROOT/entry['path'] for entry in jobs]]
        manifest={'class':name,'batch':'batch01','added':count,'generationOnly':True,
                  'files':{p.relative_to(base).as_posix():digest(p) for p in files},
                  'auditFiles':{p.relative_to(ROOT).as_posix():digest(p)
                                for p in [snapshot,*audit_dir.glob('*_checks.json')]}}
        manifest_path=base/'reference_replenishment_manifest.json';atomic_json(manifest_path,manifest)
        state.update(phase='generation_complete',validationStatus='validation_pending',
                     manifestSha256=digest(manifest_path),added=count)
        atomic_json(state_path,state)
        return count


def main():
    progress=load(RUN/'progress.json');results={}
    for name in progress['classes']:
        results[name]=standardize_class(name,progress)
        print(f'{name}: {results[name]} soal lengkap diseragamkan',flush=True)
    atomic_json(RUN/'format_standardization.json',{'classes':results,'questions':sum(results.values()),
                'validationApiCalls':0,'productionWrites':0,'oldQuestionsPreserved':True,
                'dataFolder':'output/exercise/<kelas>/batch01/babNN',
                'generatedOnlyFolder':str((RUN/'generated').relative_to(ROOT)),
                'auditFolder':str((RUN/'audit').relative_to(ROOT))})


if __name__=='__main__':main()
