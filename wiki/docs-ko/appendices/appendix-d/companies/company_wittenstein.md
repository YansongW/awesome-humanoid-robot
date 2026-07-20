# WITTENSTEIN alpha / 비텐슈타인

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 비텐슈타인 |
| **영문명** | WITTENSTEIN alpha |
| **본사** | 독일 이거스하임 (Igersheim) |
| **설립 연도** | 1949 |
| **공식 홈페이지** | [https://www.wittenstein.de](https://www.wittenstein.de) |
| **공급망 단계** | 정밀 감속기 / 서보 액추에이터 / 전기 구동 시스템 |
| **기업 속성** | 가족 기업, 국제 브랜드 |
| **모회사/소속 그룹** | WITTENSTEIN SE (독립 가족 기업) |
| **데이터 출처** | 공식 홈페이지, 제품 매뉴얼, WAIC 2026 보도 |

## 회사 소개

WITTENSTEIN alpha는 독일 WITTENSTEIN SE 산하의 정밀 서보 감속기 및 전기 액추에이터 전문 고급 브랜드입니다. 낮은 백래시 유성 감속기, 고강성 베어링 및 모듈식 모터 인터페이스를 통해 alpha 제품은 고동적, 고정밀 모션 제어 분야에 널리 사용됩니다.

회사는 SP+, TP+, XP+, NPL, CPS 등 시리즈 유성 감속기와 Servo Actuator 전기 액추에이터 및 rack/pinion 선형 시스템을 제공합니다. 엔지니어링 도구 cymex®는 구동 시스템 선정 및 수명 계산을 지원합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 유성 감속기 | 낮은 백래시/고강성 | SP+ / TP+ / XP+ | 공작 기계, 로봇 |
| 전기 액추에이터 | 일체형 선형/회전 구동 | Servo Actuator | 의료, 자동화 |
| 선형 전동 시스템 | 랙/피니언/기어박스 | alpha Rack & Pinion | 갠트리, 로봇 |

## 대표 제품

### SP+ 낮은 백래시 유성 감속기

> SP+ 낮은 백래시 유성 감속기: [공식 자료](https://www.wittenstein.de)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 감속비 | 3:1 – 100:1 | 제품 매뉴얼 |
| 프레임/크기 | 7가지 크기 (MF) | 제품 매뉴얼 |
| 최대 출력 토크 | 48 – 5,700 N·m | 제품 매뉴얼 |
| 최대 입력 회전 속도 | 최대 8,500 rpm | 제품 매뉴얼 |
| 백래시 | 표준 ≤3 arcmin / 감소 ≤1 arcmin | 제품 매뉴얼 |
| 비틀림 강성 | 550 N·m/arcmin | 제품 매뉴얼 |
| 최대 전복 모멘트 | 5,000 N·m | 제품 매뉴얼 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 헬리컬 기어, 일정한 낮은 백래시, 높은 토크 밀도, 원뿔 롤러 베어링이 축/반경 방향 하중 지지, 다양한 출력 형태.

**적용 시나리오**: 산업용 로봇 관절, 휴머노이드 로봇 관절, 공작 기계 이송축, 포장 기계, 의료 장비.

### 기타 대표 제품

TP+ HIGH TORQUE 시리즈: 감속비 22–302.5, 최대 토크 315–22,000 N·m, 고강성 포지셔닝에 적합; alpha Servo Actuator 일체형 액추에이터는 선형/회전 운동에 사용.

## 공급망 위치

- **상류 핵심 부품/재료**: 고강도 합금강, 정밀 베어링, 특수 그리스, 모터, 센서
- **하류 고객/적용 시나리오**: 공작 기계 OEM, 산업용 로봇, 휴머노이드 로봇 완성차 제조사, 의료 및 포장 장비 업체
- **주요 경쟁사/벤치마크**: Neugart, STOBER, Apex Dynamics, Harmonic Drive, Nabtesco

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_wittenstein`
- 부품 엔터티: `ent_component_wittenstein_sp_plus`
- 주요 관계:
  - `ent_company_wittenstein` -- `manufactures` --> `ent_component_wittenstein_sp_plus`

## 참고 자료

1. [비텐슈타인 공식 홈페이지](https://www.wittenstein.de)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [WITTENSTEIN alpha SP+ 기술 데이터](https://alpha.wittenstein.de/en-en/products/sp-planetary-gearbox/)
