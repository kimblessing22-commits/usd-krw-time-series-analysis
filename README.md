# USD/KRW Time Series Analysis

2024년 1월부터 2026년 9월까지의 원/달러 환율 데이터를 활용한 시계열 분석 프로젝트입니다.

## 프로젝트 링크

- GitHub Repository: https://github.com/kimblessing22-commits/usd-krw-time-series-analysis
- Jupyter Notebook: `analysis.ipynb`
- 실행 가능한 Python Script: `analysis.py`
- 분석 보고서: `REPORT.md`
- 원본 데이터: `data/usd_krw_2024_2026.csv`

## 분석 내용

- 전체 환율 추세 분석
- 30일 이동평균 분석
- 일별 변화율 분석
- 월별 평균 환율 분석
- IQR 기반 이상치 확인
- 시계열 분해를 통한 트렌드·계절성 분석
- 7일·30일·60일 이동평균 비교
- 2025년 별도 기간 분석
- 일별·주별·월별 집계 결과 비교

## 데이터

- 출처: Yahoo Finance
- 티커: KRW=X
- 기간: 2024-01-01 ~ 2026-09-30
- 데이터 수: 713개
- 주요 분석 변수: Close
- 원본 CSV 위치: `data/usd_krw_2024_2026.csv`

## 데이터 수집 방법

Python의 `yfinance` 라이브러리를 사용하여 데이터를 수집했습니다.

```python
df = yf.download(
    "KRW=X",
    start="2024-01-01",
    end="2026-10-01",
    interval="1d"
)
```

## 핵심 분석 코드

- 결측치 확인: `df.isnull().sum()`
- 30일 이동평균: `close.rolling(window=30).mean()`
- 일별 변화율: `close.pct_change() * 100`
- 월별 평균: `close.resample("ME").mean()`
- 주별 평균: `close.resample("W").mean()`
- 시계열 분해: `seasonal_decompose(..., period=12)`

전체 실행 코드는 `analysis.ipynb` 및 `analysis.py`에서 확인할 수 있습니다.

## 권장 시각화 3개

1. 전체 환율 추세 그래프
   - 전체 기간의 상승·하락과 추세 전환을 확인하기 위해 권장

2. 30일 이동평균 그래프
   - 단기 노이즈를 줄이고 중장기 방향을 확인하기 위해 권장

3. 일별 변화율 그래프
   - 급격한 변동 시점과 이상치 후보를 확인하기 위해 권장

## 프로젝트 구조

```text
usd-krw-time-series-analysis/
├── data/
│   └── usd_krw_2024_2026.csv
├── images/
│   ├── 01_exchange_rate_trend.png
│   ├── 02_moving_average.png
│   ├── 03_daily_change.png
│   ├── 04_monthly_average.png
│   ├── 05_seasonal_decomposition.png
│   ├── 06_moving_average_comparison.png
│   └── 07_2025_weekly_monthly_comparison.png
├── analysis.ipynb
├── analysis.py
├── REPORT.md
├── README.md
└── requirements.txt
```

## 실행 방법

Python 3.10 이상의 환경을 사용합니다.

먼저 필요한 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

Python script를 실행하려면:

```bash
python analysis.py
```

또는 `analysis.ipynb`를 Jupyter Notebook이나 Google Colab에서 위에서부터 순서대로 실행합니다.

## 사용 라이브러리

- pandas
- matplotlib
- yfinance
- statsmodels

## 분석 흐름

데이터 수집 → 구조 확인 → 결측치 확인 → 이상치 확인 → 시계열 분석 → 시각화 → 대안 기간/집계 비교 → 인사이트 도출

## 참고

본 프로젝트는 교육 목적의 데이터 분석 프로젝트이며 투자 판단을 목적으로 하지 않습니다.
