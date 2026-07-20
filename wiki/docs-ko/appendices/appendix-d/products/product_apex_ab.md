# Apex Dynamics AB 시리즈 고정밀 유성 감속기 / Apex Dynamics AB Series Planetary Gearbox

> 본 항목은 [부록 D 핵심 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 핵심 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [정예기술(Apex Dynamics) / Apex Dynamics](../companies/company_apex_dynamics.md) |
| **제품 카테고리** | 고정밀 유성 감속기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [정예기술(Apex Dynamics) 공식 홈페이지](https://www.apexdynamics.com) |

## 제품 개요

Apex Dynamics AB 시리즈는 100% 최적화된 헬리컬 기어와 크로스 장착형 고정밀 베어링을 채택하여, 1단 3–10 및 2단 12–100의 감속비를 제공합니다. 프레임 사이즈는 AB042부터 AB220까지이며, 정격 출력 토크는 14–2,000 N·m, 백래시는 P0 ≤1 arcmin, P1 ≤3 arcmin, P2 ≤5 arcmin(1단) 중 선택 가능합니다.

AB 시리즈는 방진 등급 IP65, 작동 온도 -10 °C ~ +90 °C를 지원하며, 출력 플랜지는 ISO 9409-1을 준수하여 턴테이블이나 로봇 암 끝단에 직접 장착할 수 있습니다. CNC, 로봇, 반도체 및 의료 분야에서 널리 사용됩니다.

## 제품 이미지

> Apex Dynamics AB 시리즈 고정밀 유성 감속기 / Apex Dynamics AB Series Planetary Gearbox: [공식 자료](https://www.apexdynamics.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 1단 3–10; 2단 12–100 | 제품 매뉴얼 |
| 프레임 사이즈 | AB042 / 060 / 090 / 115 / 142 / 180 / 220 | 제품 매뉴얼 |
| 정격 출력 토크 | 14 – 2,000 N·m | 제품 매뉴얼 |
| 백래시 | P0 ≤1 / P1 ≤3 / P2 ≤5 arcmin(1단) | 제품 매뉴얼 |
| 효율 | 1단 ≥97%; 2단 ≥94% | 제품 매뉴얼 |
| 방진 등급 | IP65 | 제품 매뉴얼 |
| 작동 온도 | -10 °C – +90 °C | 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [정예기술(Apex Dynamics) / Apex Dynamics](../companies/company_apex_dynamics.md)
- **핵심 부품/기술 출처**: 헬리컬 기어, 고정밀 베어링, 실링 부품, 그리스, ISO 9409-1 플랜지, 알루미늄/스테인리스 하우징
- **하위 응용 분야/고객**: CNC 공작 기계, 산업용 로봇, 휴머노이드 로봇, 반도체, 의료 장비

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_apex_ab`
- 제조사 엔터티: `ent_company_apex_dynamics`
- 주요 관계:
  - `rel_ent_company_apex_dynamics_manufactures_ent_component_apex_ab` (`ent_company_apex_dynamics` --> `manufactures` --> `ent_component_apex_ab`)

## 응용 시나리오

- **산업용 로봇**: 로봇 어깨, 손목, 턴테이블
- **휴머노이드 로봇**: 팔, 다리 회전 관절
- **CNC 공작 기계**: CNC 이송 축, 공구 매거진, 제4/5축 턴테이블
- **기타 자동화**: 반도체 이송, 의료 위치 결정, 포장 기계

## 경쟁 비교

| 비교 항목 | AB 시리즈 유성 감속기 | Neugart PLN | Wittenstein SP+ |
|--------|------------------------|---------------|---------------|
| 핵심 장점 | 고가성비 헬리컬, 대만 제조 | 고정밀 직치 | 독일 고급 헬리컬 기어 |
| 백래시/정밀도 | ≤1–5 arcmin | <1–3 arcmin | ≤1–3 arcmin |
| 가격 수준 | 중고급 | 고급 | 고급 |
| 납기 | 비교적 짧음 | 중간 | 중간 |

## 구매 및 배치 권장 사항

정밀도 등급(P0/P1/P2)과 토크에 따라 프레임 사이즈를 선택하십시오. 로봇 관절에는 P1 이상을 권장하며, 전복 모멘트를 검증해야 합니다.

## 참고 자료

1. [정예기술(Apex Dynamics) 공식 홈페이지](https://www.apexdynamics.com)
2. [Apex Dynamics AB Series High Precision Planetary Gearboxes](https://www.apexdynamicsusa.com/ab-series-high-precision-planetary-gearboxes.html)
3. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
