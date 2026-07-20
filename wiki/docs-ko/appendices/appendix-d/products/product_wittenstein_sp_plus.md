# WITTENSTEIN alpha SP+ 유성 감속기 / WITTENSTEIN alpha SP+ Planetary Gearbox

> 본 항목은 [부록 D 핵심 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 핵심 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [비텐슈타인 / WITTENSTEIN alpha](../companies/company_wittenstein.md) |
| **제품 카테고리** | 유성 감속기 / 서보 감속기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [비텐슈타인 공식 사이트](https://www.wittenstein.de) |

## 제품 개요

SP+는 WITTENSTEIN alpha의 고전적인 저백래시 유성 감속기 시리즈로, 높은 위치 정밀도와 사이클 다이내믹 애플리케이션을 위해 설계되었습니다. 헬리컬 유성 기어, 프리로드 테이퍼 롤러 베어링 및 모듈식 모터 인터페이스를 채택하여 48 N·m에서 5,700 N·m까지의 가속 토크 범위를 제공합니다.

이 시리즈는 표준(MF) 버전, 감속비 3–100, 7가지 사이즈를 제공하며, 백래시 감소 버전을 선택할 수 있습니다. SP+ HIGH SPEED 및 MC-L 저마찰 버전은 연속 운전 및 고속 시나리오를 추가로 커버하며, 공작 기계, 로봇 및 자동화 생산 라인의 핵심 동력 전달 부품입니다.

## 제품 이미지

> WITTENSTEIN alpha SP+ 유성 감속기 / WITTENSTEIN alpha SP+ Planetary Gearbox: [공식 자료](https://www.wittenstein.de)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3:1 – 100:1 | 제품 매뉴얼 |
| 프레임/사이즈 | 7가지 사이즈 (MF) | 제품 매뉴얼 |
| 최대 출력 토크 | 48 – 5,700 N·m | 제품 매뉴얼 |
| 최대 입력 회전 속도 | 최대 8,500 rpm | 제품 매뉴얼 |
| 백래시 | 표준 ≤3 arcmin / 감소 ≤1 arcmin | 제품 매뉴얼 |
| 비틀림 강성 | 550 N·m/arcmin | 제품 매뉴얼 |
| 최대 전복 모멘트 | 5,000 N·m | 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [비텐슈타인 / WITTENSTEIN alpha](../companies/company_wittenstein.md)
- **핵심 부품/기술 출처**: 고강도 합금강 기어, 정밀 베어링, 실링, 그리스, 모터 어댑터 플랜지
- **하위 애플리케이션/고객**: 산업용 로봇, 휴머노이드 로봇 관절, CNC 공작 기계, 포장 및 의료 장비 제조사

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_wittenstein_sp_plus`
- 제조사 엔터티: `ent_company_wittenstein`
- 주요 관계:
  - `rel_ent_company_wittenstein_manufactures_ent_component_wittenstein_sp_plus` (`ent_company_wittenstein` --> `manufactures` --> `ent_component_wittenstein_sp_plus`)

## 애플리케이션 시나리오

- **산업용 로봇**: 6축 로봇 손목, 어깨 관절의 고정밀 감속
- **휴머노이드 로봇**: 팔, 다리 회전 관절 동력 전달
- **CNC 공작 기계**: 공작 기계 이송축, 공구 매거진, 턴테이블 위치 결정
- **기타 자동화**: 포장 기계, 인쇄 장비, 의료 위치 결정 플랫폼

## 경쟁 비교

| 비교 항목 | SP+ 유성 감속기 | Neugart PLN | STOBER P |
|--------|------------------------|---------------|---------------|
| 핵심 장점 | 독일 고급 헬리컬 기어, 일정한 저백래시 | 고정밀 직선 기어, PLN 표준 | 모듈식 helical 유성 |
| 백래시/정밀도 | ≤1–3 arcmin | ≤1–3 arcmin | 1–4 arcmin |
| 가격 수준 | 고급 | 고급 | 중고급 |
| 납기 | 중간 | 중간 | 중간 |

## 구매 및 배치 권장 사항

사이클 횟수, 피크 토크 및 설치 공간에 따라 사이즈를 선택하십시오. 고다이내믹 로봇 관절에는 백래시 감소 버전을 선택하고, alpha 선정 소프트웨어 cymex®를 통해 수명을 검증하는 것이 좋습니다.

## 참고 자료

1. [비텐슈타인 공식 사이트](https://www.wittenstein.de)
2. [WITTENSTEIN alpha SP+ Planetary Gearbox](https://www.wittenstein.de/en-en/products/servo-gearboxes/low-backlash-planetary-gearboxes/sp-planetary-gearbox/)
3. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
