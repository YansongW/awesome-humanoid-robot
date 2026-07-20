# Bonfiglioli 300M 시리즈 유성 감속기 / Bonfiglioli 300M Series Planetary Gearbox

> 본 항목은 [부록 D 핵심 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 핵심 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Bonfiglioli / Bonfiglioli](../companies/company_bonfiglioli.md) |
| **제품 카테고리** | 유성 감속기 / 중부하 감속기 |
| **출시 시간** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Bonfiglioli 공식 홈페이지](https://www.bonfiglioli.com) |

## 제품 개요

300M 시리즈는 Bonfiglioli의 플래그십 산업용 유성 감속기로, 동축 및 직각 두 가지 레이아웃을 제공하며 토크 범위는 1,000 ~ 450,000 N·m, 감속비는 최대 5,000:1입니다. 제품은 구상흑연주철 하우징, 경화된 태양 기어/유성 기어 및 모듈식 입력 인터페이스를 채택하여 IEC/NEMA 모터 또는 유압 모터에 적용할 수 있습니다.

이 시리즈는 20가지 크기, 다양한 출력 샤프트(실제 키 샤프트, 스플라인, 중공 샤프트 팽창 슬리브) 및 IP65/ATEX/냉각 옵션을 제공하며, 풍력 발전, 광산, 건설 기계 및 휴머노이드 로봇의 중부하 관절에 널리 사용됩니다.

## 제품 이미지

> Bonfiglioli 300M 시리즈 유성 감속기 / Bonfiglioli 300M Series Planetary Gearbox: [공식 자료](https://www.bonfiglioli.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3.4:1 – 5,000:1 | 제품 매뉴얼 |
| 출력 토크 | 1,000 – 450,000 N·m (시리즈 범위) | 제품 매뉴얼 |
| 프레임 크기 | 20가지 세밀하게 구분된 크기 | 제품 매뉴얼 |
| 설치 방식 | 풋 / 플랜지 / 중공 샤프트 / 실제 키 샤프트 | 제품 매뉴얼 |
| 입력 방식 | IEC/NEMA 모터 어댑터, 유압 모터, 실제 샤프트 | 제품 매뉴얼 |
| 보호/옵션 | IP65, ATEX, 독립 냉각, Taconite 씰 | 제품 매뉴얼 |
| 전동 단수 | 1–4단 (직각/조합 포함) | 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [Bonfiglioli / Bonfiglioli](../companies/company_bonfiglioli.md)
- **핵심 부품/기술 출처**: 구상흑연주철 하우징, 합금강 기어, 베어링, 씰, 모터 어댑터 플랜지, 냉각 장치
- **하위 응용 분야/고객**: 풍력 발전기, 건설 기계, 산업용 로봇, 휴머노이드 로봇 중부하 관절, 자재 운반

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_bonfiglioli_300m`
- 제조사 엔터티: `ent_company_bonfiglioli`
- 주요 관계:
  - `rel_ent_company_bonfiglioli_manufactures_ent_component_bonfiglioli_300m` (`ent_company_bonfiglioli` --> `manufactures` --> `ent_component_bonfiglioli_300m`)

## 응용 시나리오

- **산업용 로봇**: 산업용 로봇 베이스, 턴테이블, 중부하 관절
- **휴머노이드 로봇**: 몸통, 엉덩이 등 대토크 관절
- **CNC 공작 기계**: 건설 기계 선회, 권양, 컨베이어 구동
- **기타 자동화**: 풍력 피치, 광산 파쇄기, 항만 크레인

## 경쟁 비교

| 비교 항목 | 300M 유성 감속기 | SEW-Eurodrive R 시리즈 | Lenze G500-S |
|--------|------------------------|---------------|---------------|
| 핵심 장점 | 중부하 유성, 풍력 검증, 모듈화 | 글로벌 서비스 네트워크, 헬리컬 기어 솔루션 | 모션 제어 협업 |
| 백래시/정밀도 | 산업용 백래시 | 산업용 백래시 | 낮은 백래시 옵션 가능 |
| 가격 수준 | 중고급 | 중고급 | 중고급 |
| 납기 | 중간 | 중간 | 중간 |

## 구매 및 배치 권장 사항

중부하 관절 선정 시 피크 토크, 충격 하중 및 연속 열 출력을 제약 조건으로 해야 합니다. 직각 버전은 축 방향 공간을 절약할 수 있지만 반경/축 방향 하중을 검토해야 합니다.

## 참고 자료

1. [Bonfiglioli 공식 홈페이지](https://www.bonfiglioli.com)
2. [Bonfiglioli 300M Series Planetary Gearmotors](https://www.bonfiglioli.com)
3. [WAIC 2026 전시 보도](https://www.worldrobotconference.com)
