"""Extend canonical exercise stock to three sessions, completely offline."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from app.services.exercise.session_expansion import prepare,generate_class,audit,progress


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sessions',type=int,default=3,choices=[3])
    parser.add_argument('--classes',nargs='+')
    parser.add_argument('--plan-only',action='store_true')
    parser.add_argument('--pilot',action='store_true')
    parser.add_argument('--resume',action='store_true',help='Resume durable checkpoints (also the default).')
    parser.add_argument('--audit-only',action='store_true')
    args=parser.parse_args();plan=prepare(args.sessions)
    names=args.classes or plan['classes']
    if not set(names)<=set(plan['classes']):parser.error('Unknown class; use kelas1 … kelas12, kelas11_tl, kelas12_tl')
    if args.plan_only:
        print(json.dumps({'roundId':plan['roundId'],'targetAdditions':plan['initialShortfall'],'newVisualMinimum':plan['newVisualMinimum'],'jobs':len(plan['jobs']),'apiCalls':0}));return
    if args.audit_only:
        result=audit(plan);print(json.dumps({k:v for k,v in result.items() if k not in ('classes','coverage')}));return
    for name in names:generate_class(name,plan,pilot=args.pilot)
    progress(plan,'pilot_complete' if args.pilot else 'generation_complete')
    if not args.pilot and set(names)==set(plan['classes']):audit(plan)


if __name__=='__main__':main()
