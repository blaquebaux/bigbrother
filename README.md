# Blaque Baux Big Brother

**America's new SOEs — when Washington takes a stake, does government backing prop up the stock?**

Big Brother is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Big Brother points that engine at the
companies Washington has bought into, and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/bigbrother.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

The US is taking **direct equity stakes** in strategic companies (the 2025 Intel stake, CHIPS-Act money,
defense procurement) — starting to look like **China's state-owned enterprises (SOEs)**. The intuition:
a government backstop is an implicit put — too-strategic-to-fail — that **props up the stock** and caps
the downside. Big Brother tests whether that backing is worth anything to a shareholder.

**The honest tension worth naming up front:** the China-SOE record cuts the *other* way — state ownership
has historically *destroyed* value (SOEs chronically **under**perform private peers: political mandates,
overstaffing, capital misallocation). So there are two testable, opposed hypotheses — *government backing =
downside protection & outperformance* vs *government backing = a value-destroying overhang* — and the data,
not the narrative, decides. Either way the interesting number is the **tail**: does the backstop cut
drawdown even if it drags the mean?

**Data honesty — the stake set is a small, recent, hand-curated event list.** Direct US equity stakes are
rare events: Intel (2025), the 2008–09 TARP names (Citi/BAC/GM/AIG — the longest history, some pre-SIP),
Fannie/Freddie. The broader ongoing proxy is **industrial-policy beneficiaries** — CHIPS recipients
(`INTC`, `MU`, `GFS`, US-listed `TSM`) and government-revenue-dependent defense primes (`LMT`, `RTX`,
`NOC`, `GD`, ETF `ITA`) — vs `SPY`. The clean "stake announced" event study is small-n and flagged as such.

## Research plan (Path A)

- **The backed basket vs the market.** Industrial-policy/defense beneficiaries vs `SPY`: beta, Jensen's
  alpha, M², and Jarque-Bera — is there risk-adjusted out/under-performance, and are the tails smaller?
- **The stake event study.** Abnormal return around the announcement of a US government equity stake
  (small-n, hand-curated) — does the market price a backstop premium?
- **The SOE mirror.** Compare the US "backed" basket's drawdown profile to the SOE prior (backing cuts
  downside but drags the mean?) — keep whichever null the data gives.

## Status
**[Concept] — scaffolded, not yet built.** Thesis, the opposed hypotheses (backstop premium vs SOE value
drag), and the data-honesty boundary (rare, hand-curated stake events; industrial-policy basket as the
ongoing proxy) are defined. Verdicts will use the fat-tail toolkit (Jarque-Bera + Jensen's alpha + M²). No
research run yet; no live driver.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   _bigbrother_common.py (loaders + JB/Jensen/M² toolkit) + sketches + scorecard  [to build]
live/       governed live drivers (once a sleeve graduates to paper A/B)
```


## Mirage audit (spec sign-stability) — "survives controls" is FRAGILE

Re-estimating the defense alpha across all control subsets ([nullbar/mirage](https://github.com/blaquebaux/nullbar)):
**+14.6%/yr collapses to +2.3%**, significant in **only 3%** of specs; **industrials (XLI) alone adds +18pp R² while
killing the alpha** (corr 0.70), with QUAL/USMV/VLUE close behind. The defense "alpha" is largely **industrials + low-vol
+ value beta**. This reinforces the #2 validation's skeptical lean (fails the Bogle hurdle; alpha concentrated post-2021) —
treat defense exposure as sector/factor beta, not a distinct governed-demand premium.

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
