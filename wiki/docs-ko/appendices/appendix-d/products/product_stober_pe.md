# STOBER PE 시리즈 경제형 유성 감속기 / STOBER PE Series Planetary Gearbox

> 본 항목은 [부록 D 핵심 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 핵심 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [STOBER (슈토버) / STOBER](../companies/company_stober.md) |
| **제품 카테고리** | 경제형 유성 감속기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [STOBER (슈토버) 공식 홈페이지](https://www.stober.com) |

## 제품 개요

STOBER PE 시리즈는 비용에 민감한 서보 애플리케이션을 위한 경제형 유성 감속기로, 헬리컬 유성 기어와 통합 모터 어댑터(MAI)를 채택하여 3:1–100:1 감속비와 최대 160 N·m 정격 토크를 제공합니다. 이 시리즈는 PE21, PE31, PE41, PE51의 네 가지 크기로 제공되며, 백래시 <8 arcmin, 효율은 단단 97%, 이단 95%입니다.

PE 시리즈는 보호 등급 IP64, 평생 윤활 방식을 채택하며, 최대 입력 회전수 8,000 rpm으로 중소형 로봇 관절, 자동화 장치, 포장 및 의료 장비에 적합합니다.

## 제품 이미지

> STOBER PE 시리즈 경제형 유성 감속기 / STOBER PE Series Planetary Gearbox: [공식 자료](https://www.stober.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3:1 – 100:1 | 제품 매뉴얼 |
| 프레임 크기 | PE21 / PE31 / PE41 / PE51 | 제품 매뉴얼 |
| 정격 출력 토크 | 최대 160 N·m | 제품 매뉴얼 |
| 가속 토크 | 최대 310 N·m | 제품 매뉴얼 |
| 백래시 | <8 arcmin | 제품 매뉴얼 |
| 효율 | 1단 97% / 2단 95% | 제품 매뉴얼 |
| 최대 입력 회전수 | 최대 8,000 rpm | 제품 매뉴얼 |
| 보호 등급 | IP64 | - |

## 공급망 위치

- **제조사**: [STOBER (슈토버) / STOBER](../companies/company_stober.md)
- **핵심 부품/기술 출처**: 헬리컬 유성 기어, 베어링, 실, 그리스, 모터 어댑터 플랜지, 알루미늄 하우징
- **하위 애플리케이션/고객**: 중소형 로봇, 자동화 장비, 포장, 의료, 반도체

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_stober_pe`
- 제조사 엔터티: `ent_company_stober`
- 주요 관계:
  - `rel_ent_company_stober_manufactures_ent_component_stober_pe` (`ent_company_stober` --> `manufactures` --> `ent_component_stober_pe`)

## 적용 시나리오

- **산업용 로봇**: 소형 산업용 로봇 관절, 턴테이블
- **휴머노이드 로봇**: 손가락/손목 등 소형 토크 관절 또는 액추에이터
- **CNC 공작 기계**: 소형 CNC, 검사 플랫폼
- **기타 자동화**: 포장, 의료, 반도체 이송

## 경쟁 비교

| 비교 항목 | PE 시리즈 유성 감속기 | Neugart PLE | Apex Dynamics PA II |
|--------|------------------------|---------------|---------------|
| 핵심 장점 | 경제형 헬리컬, 빠른 납기 | 경제형 직치, 브랜드 평판 | 경제형 헬리컬, 가성비 |
| 백래시/정밀도 | <8 arcmin | 경제형 <8 arcmin | 6–12 arcmin |
| 가격 수준 | 중급 | 중급 | 중급 |
| 납기 | 비교적 짧음 | 보통 | 비교적 짧음 |

## 구매 및 배치 권장 사항

백래시 요구 사항이 높지 않은 중저토크 서보 축에 적합합니다. 고속 애플리케이션의 경우 임계 회전수와 베어링 수명을 검증해야 합니다.

## 참고 자료

1. [STOBER (슈토버) 공식 홈페이지](https://www.stober.com)
2. [STOBER PE Series Inline Planetary Gearbox](https://www.stober.com)
3. [WAIC 2026 전시 보도](https://www.worldrobotconference.com)
