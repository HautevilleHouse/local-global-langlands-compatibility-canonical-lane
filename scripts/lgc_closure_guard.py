#!/usr/bin/env python3
"""Canonical-lane closure guard for the global langlands reciprocity super-repo."""

from __future__ import annotations

import argparse, datetime as dt, json, math
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
PRIMARY_KEYS = ('kappa_compatibility', 'sigma_localglobal', 'kappa_compact', 'rho_rigidity', 'reciprocity_transfer')
COHERENCE_KEY = 'eps_coh'
DEFAULT_REGISTRY='artifacts/constants_registry.json'
DEFAULT_STITCH='artifacts/stitch_constants.json'
DEFAULT_OUT='repro/certificate_runtime.json'
DEFAULT_HISTORY='repro/drift_guard_runs.jsonl'


def _finite(v: Any) -> bool:
    return isinstance(v,(int,float)) and math.isfinite(float(v))


def _resolve(p: str) -> Path:
    q = Path(p).expanduser()
    return q if q.is_absolute() else PROJECT_ROOT / q


def _bootstrap(path: Path) -> None:
    payload={'constants':{k:{'value':None,'theorem_level':False,'source':'','notes':'pending theorem extraction'} for k in (*PRIMARY_KEYS, COHERENCE_KEY)}}
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True)+'\n')


def _load_registry(path: Path):
    if not path.exists():
        _bootstrap(path)
    data=json.loads(path.read_text())
    if not isinstance(data,dict) or not isinstance(data.get('constants'),dict):
        raise ValueError('bad registry')
    return data


def _load_sigma(path: Path):
    if not path.exists():
        return None
    try:
        data=json.loads(path.read_text())
    except Exception:
        return None
    consts=data.get('constants')
    if not isinstance(consts,dict):
        return None
    obj=consts.get('sigma_star_can')
    if isinstance(obj,dict):
        v=obj.get('value')
        return float(v) if _finite(v) else None
    return float(obj) if _finite(obj) else None


def _entry(constants,key):
    obj=constants.get(key)
    if isinstance(obj,dict):
        v=obj.get('value')
        return (float(v) if _finite(v) else None, bool(obj.get('theorem_level',False)))
    if _finite(obj):
        return float(obj), False
    return None, False


def compute_report(data,sigma_star,strict):
    consts=data['constants']
    vals={}
    th={}
    for key in PRIMARY_KEYS:
        vals[key], th[key]=_entry(consts,key)
    eps_coh, th_coh = _entry(consts, COHERENCE_KEY)
    gate_pass=[th[k] and _finite(vals[k]) and float(vals[k])>0.0 for k in PRIMARY_KEYS]
    coh_base=th_coh and _finite(eps_coh) and float(eps_coh)>=0.0
    coh_pass=coh_base and ((abs(float(eps_coh))<1e-15) if strict else True)
    margin=min(float(vals[k]) for k in PRIMARY_KEYS)-float(eps_coh) if all(_finite(vals[k]) for k in PRIMARY_KEYS) and _finite(eps_coh) else None
    gm_pass=all(gate_pass) and coh_pass and _finite(margin) and float(margin)>0.0
    gates={f'LGC_G{i}':('PASS' if p else 'FAIL') for i,p in enumerate(gate_pass, start=1)}
    gates['LGC_G6']='PASS' if coh_pass else 'FAIL'
    gates['LGC_GM']='PASS' if gm_pass else 'FAIL'
    blockers={name:([] if status=='PASS' else ['missing/nonpositive or not theorem-level']) for name,status in gates.items() if name not in ('LGC_G6','LGC_GM')}
    blockers['LGC_G6']=[] if coh_pass else ['eps_coh missing/invalid or strict-zero target failed']
    blockers['LGC_GM']=[] if gm_pass else ['strict margin <= 0 or upstream gates failed']
    normalized_gates={'G1':gates['LGC_G1'],'G2':gates['LGC_G2'],'G3':gates['LGC_G3'],'G4':gates['LGC_G4'],'G5':gates['LGC_G5'],'G6':'NA','GCoh':gates['LGC_G6'],'GM':gates['LGC_GM']}
    normalized_blockers={'G1':blockers['LGC_G1'],'G2':blockers['LGC_G2'],'G3':blockers['LGC_G3'],'G4':blockers['LGC_G4'],'G5':blockers['LGC_G5'],'G6':[],'GCoh':blockers['LGC_G6'],'GM':blockers['LGC_GM']}
    report={'meta':{'computed_at_utc':dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),'framework':'local_global_langlands_compatibility' },'schema':{'normalized_gate_keys':['G1','G2','G3','G4','G5','G6','GCoh','GM'],'g6_policy':'NA means this framework has no standalone pre-coherence G6 gate'},'lane':{'canonical_theorem_lane':'manifold_constrained','active_lane':'manifold_constrained'},'inputs':{**vals,'eps_coh':eps_coh,'sigma_star_can':sigma_star},'derived':{'strict_margin':margin,'strict_coh_zero':bool(strict)},'gates':gates,'blockers':blockers,'normalized':{'gates':normalized_gates,'blockers':normalized_blockers}}
    report['all_pass']=all(v=='PASS' for v in gates.values())
    report['all_pass_normalized']=all(v in {'PASS','NA'} for v in normalized_gates.values()) and all(v=='PASS' for v in normalized_gates.values() if v!='NA')
    return report


def append_history(path,report):
    path.parent.mkdir(parents=True, exist_ok=True)
    row={'timestamp_utc':report['meta']['computed_at_utc'],'all_pass':report['all_pass'],'gates':report['gates'],'strict_margin':report['derived']['strict_margin']}
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(row, sort_keys=True)+'\n')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--registry', default=DEFAULT_REGISTRY)
    ap.add_argument('--stitch', default=DEFAULT_STITCH)
    ap.add_argument('--out', default=DEFAULT_OUT)
    ap.add_argument('--history', default=DEFAULT_HISTORY)
    ap.add_argument('--strict-coh-zero', action='store_true')
    ap.add_argument('--pretty', action='store_true')
    ns=ap.parse_args()
    report=compute_report(_load_registry(_resolve(ns.registry)), _load_sigma(_resolve(ns.stitch)), bool(ns.strict_coh_zero))
    out=_resolve(ns.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2 if ns.pretty else None, sort_keys=True)+'\n')
    append_history(_resolve(ns.history), report)
    print(json.dumps(report, indent=2 if ns.pretty else None, sort_keys=True))


if __name__=='__main__':
    main()
