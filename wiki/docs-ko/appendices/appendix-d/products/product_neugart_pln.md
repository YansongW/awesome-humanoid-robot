# Neugart PLN 고정밀 유성 감속기 / Neugart PLN Precision Planetary Gearbox

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [뉴카트 / Neugart](../companies/company_neugart.md) |
| **제품 카테고리** | 고정밀 유성 감속기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [뉴카트 공식 사이트](https://www.neugart.com) |

## 제품 개요

PLN은 Neugart 표준 고정밀 유성 감속기로, 직치 고강성 설계와 프리로드 테이퍼 롤러 베어링을 채택하여 1단 및 2단 전동을 제공합니다. 시리즈 크기는 PLN 070부터 PLN 190까지이며, 감속비는 3–100, 1단 정격 토크는 14–800 N·m, 2단은 최대 43–2,880 N·m입니다.

PLN은 IP65 보호, 평생 윤활, PCS-2 고속 모터 어댑터 및 긴 센터링 칼라를 갖추고 있으며, 위치 정밀도는 <1 arcmin(옵션)까지 가능하여 공작 기계, 로봇 및 반도체 장비에 적합한 고성능 정밀 전동 솔루션입니다.

## 제품 이미지

> Neugart PLN 고정밀 유성 감속기 / Neugart PLN Precision Planetary Gearbox: [공식 자료](https://www.neugart.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 감속비 | 3:1 – 100:1 | 제품 매뉴얼 |
| 프레임 크기 | PLN 070 / 090 / 115 / 142 / 190 | 제품 매뉴얼 |
| 정격 출력 토크 | 14 – 800 N·m (1단); 43 – 2,880 N·m (2단) | 제품 매뉴얼 |
| 백래시 | 표준 <3 arcmin; 옵션 <1 arcmin | 제품 매뉴얼 |
| 효율 | 최대 약 98% | 제품 매뉴얼 |
| 보호 등급 | IP65 | 제품 매뉴얼 |
| 최대 입력 회전 속도 | 최대 8,000 rpm (크기에 따라 다름) | 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [뉴카트 / Neugart](../companies/company_neugart.md)
- **핵심 부품/기술 출처**: 직치 유성 기어, 프리로드 베어링, 씰, 그리스, 모터 어댑터 플랜지
- **하위 응용/고객**: CNC 공작 기계, 산업용 로봇, 휴머노이드 로봇, 반도체 및 의료 장비

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_neugart_pln`
- 제조사 엔터티: `ent_company_neugart`
- 주요 관계:
  - `rel_ent_company_neugart_manufactures_ent_component_neugart_pln` (`ent_company_neugart` --> `manufactures` --> `ent_component_neugart_pln`)

## 응용 시나리오

- **산업용 로봇**: 로봇 손목, 어깨, 턴테이블
- **휴머노이드 로봇**: 팔, 다리 관절 정밀 감속
- **CNC 공작 기계**: 공작 기계 이송, 공구 매거진, 제4/5축 턴테이블
- **기타 자동화**: 포장, 인쇄, 의료 위치 결정 플랫폼

## 경쟁 비교

| 비교 항목 | PLN 유성 감속기 | Wittenstein SP+ | Apex Dynamics AB |
|-----------|-----------------|-----------------|------------------|
| 핵심 장점 | 고정밀, 평생 윤활, PCS-2 | 헬리컬 기어, 일정 백래시 | 대만 고성능, 헬리컬 |
| 백래시/정밀도 | <1–3 arcmin | ≤1–3 arcmin | ≤1–5 arcmin |
| 가격 수준 | 고급 | 고급 | 중고급 |
| 납기 | 중간 | 중간 | 짧음 |

## 구매 및 배포 권장 사항

고정밀 위치 결정 시나리오에서는 백래시 감소 옵션을 우선 선택하세요. PLN은 직치이므로 소음에 민감한 경우 PLE 또는 헬리컬 경쟁 제품을 고려할 수 있습니다.

## 참고 자료

1. [뉴카트 공식 사이트](https://www.neugart.com)
2. [Neugart PLN Precision Planetary Gearbox](https://www.neugart.com/en/gearboxes/precision-gearboxes/pln)
3. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
