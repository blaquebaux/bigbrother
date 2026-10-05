#!/usr/bin/python3
# =============================================================================
# bigbrother_1_gov_dependence.py — is government entanglement a SUPPORT (steady backstop) or a DRAG (inefficiency)?
# Two liquid proxies for "the state is a shareholder/customer": DEFENSE primes + ITA (government-revenue-dependent,
# the steady-backstop case) and CHIPS-Act semis INTC/MU/GFS/TSM (industrial-policy beneficiaries, the subsidy case).
# Test each basket vs SPY — alpha/beta/M² + the tail. Support shows positive risk-adjusted; drag shows negative α.
# =============================================================================
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bigbrother_common import panel, rets, riskadj
import numpy as np

DEF=["LMT","RTX","NOC","GD","ITA"]; CHIPS=["INTC","MU","GFS","TSM"]
P,dates=panel(DEF+CHIPS+["SPY"])
R={s:rets(P[s]) for s in P}; spy=R["SPY"]
def basket(names):
    have=[s for s in names if s in R];
    if not have: return None,have
    n=min(len(R[s]) for s in have); return np.mean(np.vstack([R[s][-n:] for s in have]),axis=0),have
print("="*90); print(f"BIGBROTHER — government backing: support or drag?  ({dates[0]} → {dates[-1]}, {len(dates)} days)"); print("="*90)
print(f"\n  {'':16}{'Sharpe':>8}{'CAGR':>8}{'maxDD':>8}{'β/SPY':>7}{'α/SPY':>9}{'M²exc':>8}")
def line(nm,r):
    if r is None: return None
    m=min(len(r),len(spy)); a=riskadj(r[-m:],spy[-m:])
    print(f"  {nm:16}{a['sh']:>+8.2f}{a['cagr']*100:>+7.0f}%{a['dd']*100:>+7.0f}%{a['beta']:>+7.2f}{a['alpha_ann']*100:>+8.1f}%{a['m2_excess']*100:>+7.1f}%")
    return a
db,dh=basket(DEF); cb,ch=basket(CHIPS)
ad=line("defense (ITA+)",db); ac=line("CHIPS semis",cb)
line("SPY (bench)",spy)
def tag(a):
    if a is None: return "n/a"
    if a["alpha_ann"]>0.01 and a["m2_excess"]>0: return "SUPPORT (positive risk-adjusted — backstop earns its keep)"
    if a["alpha_ann"]<-0.01: return "DRAG (negative alpha — the state entanglement costs the shareholder)"
    return "NEUTRAL (just beta — gov backing neither helps nor hurts risk-adjusted)"
print(f"\n  VERDICT:")
print(f"    defense  → {tag(ad)}")
print(f"    CHIPS    → {tag(ac)}")
print("  (Defense = steady government-revenue backstop; CHIPS = subsidy-cycle beta. 'Government equity stakes'")
print("   proper — direct US ownership (airlines/Intel-style) — isn't a clean ticker set; these are the priceable")
print("   proxies. The honest split: a reliable customer (defense) vs a policy-cycle bet (chips).)")
