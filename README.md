# USD/KRW Time Series Analysis

2024년 1월부터 2026년 9월까지의 원/달러 환율 데이터를 활용한 시계열 분석 프로젝트입니다.

## 분석 내용

- 전체 환율 추세 분석
- 30일 이동평균 분석
- 일별 변화율 분석
- 월별 평균 환율 분석
- IQR 기반 이상치 확인

## 데이터

- 출처: Yahoo Finance
- 티커: KRW=X
- 기간: 2024-01-01 ~ 2026-09-30
- 데이터 수: 713개

## 프로젝트 구조

usd-krw-analysis/
- data/
  - usd_krw_2024_2026.csv
- images/
  - 01_exchange_rate_trend.png
  - 02_moving_average.png
  - 03_daily_change.png
  - 04_monthly_average.png
- analysis.ipynb
- REPORT.md
- README.md
- requirements.txt

## 실행 방법

1. Python 3.10 이상의 환경을 준비합니다.
2. 필요한 라이브러리를 설치합니다.

pip install -r requirements.txt

3. analysis.ipynb 파일을 Jupyter Notebook 또는 Google Colab에서 실행합니다.

## 사용 라이브러리

- pandas
- matplotlib
- yfinance

## 참고

본 프로젝트는 교육 목적의 데이터 분석 프로젝트이며,
환율 데이터를 이용한 투자 판단을 목적으로 하지 않습니다.
