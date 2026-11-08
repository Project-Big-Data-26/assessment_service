"""Retain arithmetic recipes from the already authored curriculum templates.

Clones are isolated from the production modules. Random draws are inputs;
derived assignments retain their expression instead of becoming answer constants.
"""
from __future__ import annotations
import ast
from copy import deepcopy
import importlib
import inspect
import math
from pathlib import Path
import types
import sympy as s

MODULES=('replenishment_math','replenishment_sd','replenishment_smp','replenishment_sma','replenishment_tl')


def encode(value):
    if value is None or isinstance(value,(str,bool,int,float)):return value
    if isinstance(value,(list,tuple)):return [encode(v) for v in value]
    if isinstance(value,dict):return {'__dict__':[[encode(k),encode(v)] for k,v in value.items()]}
    if isinstance(value,s.MatrixBase):return {'__matrix__':[[encode(v) for v in row] for row in value.tolist()]}
    if isinstance(value,s.Basic):return {'__sympy__':s.srepr(value)}
    raise ValueError('Unsupported retained input: '+type(value).__name__)


def decode(value):
    if isinstance(value,list):return [decode(v) for v in value]
    if isinstance(value,dict):
        if '__sympy__' in value:return s.sympify(value['__sympy__'])
        if '__matrix__' in value:return s.Matrix([[decode(v) for v in row] for row in value['__matrix__']])
        if '__dict__' in value:return {decode(k):decode(v) for k,v in value['__dict__']}
    return value


class Expand(ast.NodeTransformer):
    def __init__(self,env,local):self.env=env;self.local=local;self.bound=set()
    def visit_Name(self,node):
        if not isinstance(node.ctx,ast.Load) or node.id in self.bound:return node
        if node.id in self.env['names']:return deepcopy(self.env['names'][node.id])
        if node.id in self.local and not callable(self.local[node.id]):
            try:
                value=encode(self.local[node.id]);key='data_'+str(self.env['serial']);self.env['serial']+=1
                self.env['inputs'][key]=value;return ast.Name(id=key,ctx=ast.Load())
            except ValueError:pass
        return node
    def visit_Lambda(self,node):
        old=self.bound.copy();self.bound.update(a.arg for a in node.args.args)
        node.body=self.visit(node.body);self.bound=old;return node
    def _comp(self,node):
        old=self.bound.copy()
        for gen in node.generators:
            gen.iter=self.visit(gen.iter);self.bound.update(n.id for n in ast.walk(gen.target) if isinstance(n,ast.Name))
            gen.ifs=[self.visit(n) for n in gen.ifs]
        if hasattr(node,'elt'):node.elt=self.visit(node.elt)
        else:node.key=self.visit(node.key);node.value=self.visit(node.value)
        self.bound=old;return node
    visit_ListComp=_comp
    visit_SetComp=_comp
    visit_GeneratorExp=_comp
    visit_DictComp=_comp


def record(env,targets,recipe,local):
    expression=ast.parse(recipe,mode='eval').body
    stochastic=any(isinstance(n,ast.Name) and n.id=='r' for n in ast.walk(expression))
    try:
        if stochastic:
            for name in targets:
                key='input_'+name+'_'+str(env['serial']);env['serial']+=1
                env['inputs'][key]=encode(local[name]);env['names'][name]=ast.Name(id=key,ctx=ast.Load())
        elif len(targets)==1:
            env['names'][targets[0]]=Expand(env,local).visit(expression)
        else:
            expanded=Expand(env,local).visit(expression)
            for i,name in enumerate(targets):env['names'][name]=ast.Subscript(value=deepcopy(expanded),slice=ast.Constant(i),ctx=ast.Load())
    except (ValueError,KeyError):
        for name in targets:env['names'].pop(name,None)


def target_names(node):
    if isinstance(node,ast.Name):return [node.id]
    if isinstance(node,(ast.Tuple,ast.List)):return [v for n in node.elts for v in target_names(n)]
    return []


class Instrument(ast.NodeTransformer):
    def __init__(self):self.depth=0
    def visit_FunctionDef(self,node):
        self.depth+=1;node=self.generic_visit(node);self.depth-=1
        if node.name.startswith('__'):return node
        node.body.insert(0,ast.parse("_recipe={'names':{},'inputs':{},'serial':0}").body[0]);return node
    def visit_Assign(self,node):
        node=self.generic_visit(node)
        if not self.depth:return node
        names=[v for target in node.targets for v in target_names(target)]
        if not names or any(name.startswith('_recipe') for name in names):return node
        call=ast.Expr(value=ast.Call(func=ast.Name(id='_retain',ctx=ast.Load()),args=[ast.Name(id='_recipe',ctx=ast.Load()),ast.List(elts=[ast.Constant(v) for v in names],ctx=ast.Load()),ast.Constant(ast.unparse(node.value)),ast.Call(func=ast.Name(id='locals',ctx=ast.Load()),args=[],keywords=[])],keywords=[]))
        return [node,call]
    def visit_Call(self,node):
        node=self.generic_visit(node)
        if isinstance(node.func,ast.Name) and node.func.id=='numeric' and len(node.args)>1:
            node.func.id='_capture_numeric';node.keywords.extend([ast.keyword(arg='_recipe',value=ast.Name(id='_recipe',ctx=ast.Load())),ast.keyword(arg='_expression',value=ast.Constant(ast.unparse(node.args[1]))),ast.keyword(arg='_local',value=ast.Call(func=ast.Name(id='locals',ctx=ast.Load()),args=[],keywords=[]))])
        return node


def globals_for_eval():
    from . import replenishment_math as rm
    namespace={'__builtins__':{},'s':s,'math':math,'min':min,'max':max,'sum':sum,'len':len,'range':range,'abs':abs,'sorted':sorted,'int':int,'float':float,'tuple':tuple,'list':list,'enumerate':enumerate,'zip':zip,'set':set,'all':all,'any':any,'x':rm.x}
    namespace.update({k:v for k,v in vars(rm).items() if callable(v) and not k.startswith('_')})
    return namespace


def solve(cert):
    assert cert['type']=='session_expression'
    recipe=cert['expression'];assert len(recipe)<150000
    tree=ast.parse(recipe,mode='eval')
    for n in ast.walk(tree):
        if isinstance(n,ast.Attribute):assert not n.attr.startswith('_')
        if isinstance(n,ast.Name):assert not n.id.startswith('_')
    namespace=globals_for_eval();namespace.update({k:decode(v) for k,v in cert['inputs'].items()})
    value=eval(compile(tree,'retained-arithmetic','eval'),namespace,namespace)
    value=s.simplify(value);assert value.is_finite is True and not value.free_symbols
    return value


def capture_numeric(question,value,explanation,kind,*args,_recipe,_expression,_local,**kwargs):
    from .replenishment_math import numeric
    expr=Expand(_recipe,_local).visit(ast.parse(_expression,mode='eval').body);expr=ast.fix_missing_locations(expr)
    used={n.id for n in ast.walk(expr) if isinstance(n,ast.Name)}
    cert={'type':'session_expression','expression':ast.unparse(expr),'inputs':{k:v for k,v in _recipe['inputs'].items() if k in used}}
    assert cert['inputs'],'A constant answer is not a retained arithmetic recipe'
    assert s.simplify(solve(cert)-s.sympify(value))==0
    draft=numeric(question,value,explanation,kind,*args,**kwargs);draft.proof['session_certificate']=cert
    return draft


_CLONES=None
def clones():
    global _CLONES
    if _CLONES is not None:return _CLONES
    result={}
    for name in MODULES:
        original=importlib.import_module('.'+name,__package__);source=Path(original.__file__).read_text(encoding='utf-8-sig');tree=Instrument().visit(ast.parse(source));ast.fix_missing_locations(tree)
        ns={'__name__':__package__+'._session_'+name,'__package__':__package__,'_retain':record,'_capture_numeric':capture_numeric}
        # Imports/dataclass type resolution require a real, isolated module.
        import sys
        module=types.ModuleType(ns['__name__']);module.__dict__.update(ns);sys.modules[module.__name__]=module
        exec(compile(tree,original.__file__,'exec'),module.__dict__)
        result[name]=module
    helpers=result['replenishment_math']
    for module in result.values():
        for key,value in list(vars(module).items()):
            if callable(value) and getattr(value,'__module__','')==__package__+'.replenishment_math' and hasattr(helpers,key):setattr(module,key,getattr(helpers,key))
    _CLONES=result;return result


def capture(name,bab,code,level,r):
    grade=int(name.split('_')[0][5:]);key='replenishment_tl' if name.endswith('_tl') else 'replenishment_sma' if grade>=10 else 'replenishment_smp' if grade>=7 else 'replenishment_sd'
    return clones()[key].generate(name,bab,code,level,r)
