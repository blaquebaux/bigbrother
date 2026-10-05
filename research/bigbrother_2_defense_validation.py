#!/usr/bin/python3
# =============================================================================
# bigbrother_2_defense_validation.py — graduate the ONE positive finding: defense as a "reliable-customer" keeper.
# #1 showed defense (ITA + primes) beats SPY risk-adjusted at low beta. Validation asks the keeper questions:
#   1) KEEPER STATS vs SPY + the Bogle hurdle (Sharpe/α/M²/maxDD/crisis-day).
#   2) ALPHA SURVIVAL — is it distinct "government-revenue" alpha, or just Industrials (XLI) / Quality (QUAL) /
#      Low-vol (USMV) factor beta? Jensen alpha vs each control. Survives all ⇒ distinct edge.
#   3) STABILITY — split the sample in half; alpha in each. One-period artifact or persistent?
#   4) CRISIS — on SPY's worst-5% days, does defense hold up? (the "backstop" claim, made testable)
#   5) BREADTH — ITA vs the 4-name prime basket vs each name (broad edge or a single-name fluke)
# Defense names run back to 2016 (CHIPS dropped on purpose → long sample). Alpaca SIP daily, causal, gross.
# =============================================================================
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bigbrother_common import panel, rets, riskadj, jensens_alpha, stats
import numpy as np

PRIMES=["LMT","RTX","NOC","GD"]; CTRL=["SPY","XLI","QUAL","USMV"]
P,dates=panel(["ITA"]+PRIMES+CTRL)
R={s:rets(P[s]) for s in P}; spy=R["SPY"]
n=min(len(R[s]) for s in R);
def al(x): return x[-n:]
# keeper = ITA + 4 primes, equal weight (the diversified "defense/government-customer" book)
dnames=[s for s in ["ITA"]+PRIMES if s in R]
DEF=np.mean(np.vstack([al(R[s]) for s in dnames]),axis=0)
SPY=al(spy)
print("="*92); print(f"BIGBROTHER — defense keeper validation  ({dates[-n]} → {dates[-1]}, {n} days, {n/252:.1f}y)"); print("="*92)

# 1) keeper stats + Bogle hurdle
a=riskadj(DEF,SPY); b=riskadj(SPY,SPY)
print(f"\n(1) KEEPER STATS         Sharpe   CAGR   maxDD   skew   β/SPY   α/SPY   M²exc")
print(f"    defense (ITA+primes) {a['sh']:>+7.2f}{a['cagr']*100:>+6.0f}%{a['dd']*100:>+6.0f}%{a['skew']:>+7.2f}{a['beta']:>+7.2f}{a['alpha_ann']*100:>+7.1f}%{a['m2_excess']*100:>+7.1f}%")
print(f"    SPY (Bogle hurdle)   {b['sh']:>+7.2f}{b['cagr']*100:>+6.0f}%{b['dd']*100:>+6.0f}%{b['skew']:>+7.2f}{1.0:>+7.2f}{0.0:>+7.1f}%{0.0:>+7.1f}%")
clears_hurdle = a['sh']>b['sh'] and a['alpha_ann']>0 and a['m2_excess']>0

# 2) alpha survival vs factor controls
print(f"\n(2) ALPHA SURVIVAL (Jensen α, annualized):")
surv={}
for c in CTRL:
    if c not in R: continue
    ja=jensens_alpha(DEF, al(R[c])); surv[c]=ja['alpha_ann']
    print(f"    vs {c:5}  α {ja['alpha_ann']*100:>+6.1f}%   β {ja['beta']:>+5.2f}")
survives = all(v>0.01 for v in surv.values())

# 3) sub-period stability
h=n//2
print(f"\n(3) STABILITY (Jensen α vs SPY by half):")
a1=jensens_alpha(DEF[:h],SPY[:h])['alpha_ann']; a2=jensens_alpha(DEF[h:],SPY[h:])['alpha_ann']
print(f"    first half {a1*100:+.1f}%   second half {a2*100:+.1f}%")
stable = a1>0 and a2>0

# 4) crisis behavior
crash=SPY<=np.percentile(SPY,5)
dc=DEF[crash].mean(); sc=SPY[crash].mean()
print(f"\n(4) CRISIS (SPY worst-5% days):  defense {dc*100:+.2f}%/day   vs SPY {sc*100:+.2f}%/day   (cushion {(dc-sc)*100:+.2f}pp)")
defensive = dc > sc

# 5) breadth
print(f"\n(5) BREADTH (α vs SPY per name):")
for s in dnames:
    ra=riskadj(al(R[s]),SPY); print(f"    {s:5}  α {ra['alpha_ann']*100:>+6.1f}%   β {ra['beta']:>+5.2f}   Sharpe {ra['sh']:+.2f}")
pos=sum(1 for s in dnames if jensens_alpha(al(R[s]),SPY)['alpha_ann']>0.01)
broad = pos >= max(3, len(dnames)-1)

print("\n"+"="*92)
checks=[("clears Bogle hurdle",clears_hurdle),("alpha survives factor controls",survives),
        ("stable across both halves",stable),("defensive in crisis",defensive),("broad (not one name)",broad)]
for lbl,ok in checks: print(f"  [{'PASS' if ok else 'FAIL'}] {lbl}")
npass=sum(ok for _,ok in checks)
if npass>=5:   v="VALIDATED KEEPER — defense is a distinct, stable, crisis-resilient edge. Graduate to a governed sleeve."
elif npass>=3: v=f"CONDITIONAL KEEPER ({npass}/5) — real but not clean on every axis; ships as a tilt, not a core keeper."
else:          v=f"NOT VALIDATED ({npass}/5) — the edge is mostly factor beta; keep as research, not a keeper."
print(f"\n  VERDICT: {v}")
print("  (If the α dies vs QUAL/USMV, 'government as a reliable customer' is really just the quality/low-vol factor")
print("   wearing a flag; if it survives AND cushions crises, it's the genuine backstop the thesis claims.)")
