# Blaque Baux Big Brother — research

When Washington takes a stake, is it a backstop premium or an SOE-style value drag? Direct stakes are rare,
hand-curated events (Intel 2025; 2008–09 TARP; F/F); the ongoing proxy is the industrial-policy basket —
CHIPS recipients + defense primes — vs `SPY`. Read-only Alpaca SIP bars. Verdicts use the family fat-tail
toolkit ([`_bigbrother_common.py`](_bigbrother_common.py): Jarque-Bera + Jensen's alpha + M²).

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
# python research/bigbrother_1_backed_basket.py   # [to build] backed basket vs SPY: beta/JB/Jensen α/M²/DD
# python research/bigbrother_2_stake_event.py      # [to build] abnormal return around stake announcements
```

## Planned scorecard

| # | Question | Metric | Status |
|---|----------|--------|--------|
| 1 | Does the government-backed basket out/under-perform, risk-adjusted? | Jensen's α, M², JB, maxDD vs SPY | ☐ to build |
| 2 | Is there a "stake announced" premium? | small-n event study | ☐ to build |

**Two opposed priors (the data decides):** *backstop = downside protection & outperformance* vs *state
overhang = value drag (the SOE record)*. The tell is the tail — a backstop may shrink drawdown even if it
drags the mean.

## Status
**[Concept] — plan defined, no sketches run.** Boundary set (rare hand-curated stake events; industrial-policy
basket as the ongoing proxy). Next: sketch #1 (basket vs SPY) and #2 (stake event study).
