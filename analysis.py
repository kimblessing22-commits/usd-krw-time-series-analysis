import os
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

os.makedirs("data", exist_ok=True)
os.makedirs("images", exist_ok=True)

# 1. 데이터 수집
df = yf.download(
    "KRW=X",
    start="2024-01-01",
    end="2026-10-01",
    interval="1d"
)

df.to_csv("data/usd_krw_2024_2026.csv")

# Close 데이터 추출
close_data = df["Close"]

if isinstance(close_data, pd.DataFrame):
    close = close_data.iloc[:, 0]
else:
    close = close_data

# 2. 기본 데이터 확인
print("데이터 개수:", len(df))
print("시작 날짜:", df.index.min())
print("마지막 날짜:", df.index.max())

print("\n결측치")
print(df.isnull().sum())

print("\n기본 통계")
print(close.describe())

# 3. 시계열 분석
moving_avg_7 = close.rolling(window=7).mean()
moving_avg_30 = close.rolling(window=30).mean()
moving_avg_60 = close.rolling(window=60).mean()

daily_change = close.pct_change() * 100
monthly_avg = close.resample("ME").mean()

# 4. IQR 이상치
Q1 = daily_change.quantile(0.25)
Q3 = daily_change.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = daily_change[
    (daily_change < lower_bound) |
    (daily_change > upper_bound)
]

print("\nIQR 이상치")
print("하한:", lower_bound)
print("상한:", upper_bound)
print("이상치 후보 개수:", len(outliers))

# 5. 그래프 01
plt.figure(figsize=(12, 6))
plt.plot(close)
plt.title("USD/KRW Exchange Rate (2024-2026)")
plt.xlabel("Date")
plt.ylabel("KRW per USD")
plt.grid(True)
plt.savefig("images/01_exchange_rate_trend.png", dpi=300, bbox_inches="tight")
plt.close()

# 6. 그래프 02
plt.figure(figsize=(12, 6))
plt.plot(close, label="Daily Exchange Rate")
plt.plot(moving_avg_30, label="30-Day Moving Average")
plt.title("USD/KRW Exchange Rate with 30-Day Moving Average")
plt.xlabel("Date")
plt.ylabel("KRW per USD")
plt.legend()
plt.grid(True)
plt.savefig("images/02_moving_average.png", dpi=300, bbox_inches="tight")
plt.close()

# 7. 그래프 03
plt.figure(figsize=(12, 6))
plt.plot(daily_change)
plt.axhline(0)
plt.title("Daily Percentage Change in USD/KRW Exchange Rate")
plt.xlabel("Date")
plt.ylabel("Daily Change (%)")
plt.grid(True)
plt.savefig("images/03_daily_change.png", dpi=300, bbox_inches="tight")
plt.close()

# 8. 그래프 04
plt.figure(figsize=(12, 6))
plt.plot(monthly_avg, marker="o")
plt.title("Monthly Average USD/KRW Exchange Rate")
plt.xlabel("Date")
plt.ylabel("Average KRW per USD")
plt.grid(True)
plt.savefig("images/04_monthly_average.png", dpi=300, bbox_inches="tight")
plt.close()

# 9. 그래프 05 - 시계열 분해
decomposition = seasonal_decompose(
    monthly_avg,
    model="additive",
    period=12,
    extrapolate_trend="freq"
)

fig = decomposition.plot()
fig.set_size_inches(12, 9)
fig.savefig(
    "images/05_seasonal_decomposition.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close(fig)

# 10. 그래프 06 - 이동평균 비교
plt.figure(figsize=(12, 6))
plt.plot(close, label="Daily Exchange Rate", alpha=0.4)
plt.plot(moving_avg_7, label="7-Day Moving Average")
plt.plot(moving_avg_30, label="30-Day Moving Average")
plt.plot(moving_avg_60, label="60-Day Moving Average")
plt.title("Comparison of Moving Average Windows")
plt.xlabel("Date")
plt.ylabel("KRW per USD")
plt.legend()
plt.grid(True)
plt.savefig(
    "images/06_moving_average_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# 11. 2025년 별도 기간 및 집계 비교
close_2025 = close.loc["2025-01-01":"2025-12-31"]
weekly_avg_2025 = close_2025.resample("W").mean()
monthly_avg_2025 = close_2025.resample("ME").mean()

plt.figure(figsize=(12, 6))
plt.plot(close_2025, label="Daily Exchange Rate", alpha=0.3)
plt.plot(weekly_avg_2025, label="Weekly Average")
plt.plot(monthly_avg_2025, label="Monthly Average", marker="o")
plt.title("2025 USD/KRW: Daily vs Weekly vs Monthly Average")
plt.xlabel("Date")
plt.ylabel("KRW per USD")
plt.legend()
plt.grid(True)
plt.savefig(
    "images/07_2025_weekly_monthly_comparison.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\n분석 완료")
print("결과는 data/ 및 images/ 폴더에 저장되었습니다.")
