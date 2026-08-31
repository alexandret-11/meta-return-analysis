# Single-Stock Return Analysis — Meta Platforms (2012–2026)

What do the return, volatility, and drawdown characteristics of a single
mega-cap equity look like — and how far do they depart from the normal
distribution assumed by introductory models?

**Project 1 of a 7-project quantitative research portfolio.**

## Data

Yahoo Finance daily prices via `yfinance` (`auto_adjust=True`, so splits and
dividends are folded in and daily percent change approximates a total return).
2012-05-18 (IPO) to present, 3,585 trading days. Downloaded once, cached to
`data/`, read from disk thereafter. Data layer is isolated in a single cell
for a planned swap to CRSP via WRDS.

## Method

Simple and log returns; four moments and Jarque-Bera; annualised volatility
(sd × √252) and rolling 30-day volatility; maximum drawdown, duration, and
recovery computed on the total return index. Benchmark volatility computed on
SPY over the identical window and method.

## Results

- **Distribution:** strongly leptokurtic — excess kurtosis 19.3; 23 days
  beyond ±4σ vs 0.23 predicted under normality (100×). Skew +0.41, against
  the typical negative skew of equities.
- **Volatility:** 39.9% annualised (2.4× SPY's 16.7%), but ranging 7%–97%
  across 30-day windows — persistent regimes, not a constant.
- **Drawdown:** −76.74% (Sep 2021 → Nov 2022, 422 days), recovered after a
  further 442 days; 2.4 years underwater; +330% gain required to break even.

## Limitations

Single security, single sample period; no out-of-sample test; volatility
estimated unconditionally despite visible clustering; unofficial data source
(Yahoo) with undocumented adjustment methodology. The coincidence of
volatility regimes and the major drawdown is observed, not formally linked.

## Repo structure

    notebooks/01_meta_return_analysis.ipynb   — full analysis, narrative, figures
    data/                                     — cached prices (gitignored; re-downloadable)
    src/                                      — reusable functions (grows with later projects)
    requirements.txt                          — pinned environment
