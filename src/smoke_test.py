"""Verify the environment : data download, pandas, stats, plotting."""

import matplotlib

matplotlib.use("Agg")  # write plots to file rather than opening a window

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf

TICKER = "META"

# 1. Download Data
df = yf.download(TICKER, start="2020-01-01", auto_adjust=True, progress=False)
if df.empty:
    raise SystemExit(
        "Download returned nothing — check your internet or see the yfinance note."
    )

# yfinance returns multi-level columns for some calls; flatten if needed
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

print(f"Rows: {len(df)}   Range: {df.index.min().date()} to {df.index.max().date()}")

# 2. Compute returns
df["ret"] = df["Close"].pct_change()
df["logret"] = np.log(df["Close"]).diff()
df = df.dropna()

# 3. Summary stats
ann_vol = df["logret"].std() * np.sqrt(252)
ann_ret = df["logret"].mean() * 252
print(f"Annualized return (log):  {ann_ret:>7.2%}")
print(f"Annualized volatility:    {ann_vol:>7.2%}")
print(f"Skew:                     {df['ret'].skew():>7.2f}")
print(f"Excess kurtosis:          {df['ret'].kurtosis():>7.2f}")
print(
    f"Worst day:                {df['ret'].min():>7.2%}  on {df['ret'].idxmin().date()}"
)

# 4. Save the data and a chart
df.to_csv("data/meta_prices.csv")

fig, ax = plt.subplots(figsize=(10, 4))
ax.hist(df["ret"], bins=100, color="steelblue", edgecolor="none")
ax.set_title(f"{TICKER} daily returns")
ax.set_xlabel("Daily return")
fig.tight_layout()
fig.savefig("output/returns_hist.png", dpi=150)

print("\nAll good. Wrote data/meta_prices.csv and output/returns_hist.png")
