---
id: ent_company_hcfa
schema_version: 1
type: company
title: HCFA
domain: 02_components
theoretical_depth: system
names:
  zh: 禾川科技
  en: HCFA
status: active
sources:
  - id: src_hcfa_official
    type: website
    title: HCFA 공식 웹사이트
    url: https://www.hcfa.cn
verification:
  reviewed_by: human_and_ai
  reviewed_at: 2026-07-01
---

# 禾川科技 / HCFA

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 '미공개'로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 허촨 테크놀로지 |
| **영문명** | HCFA |
| **본사** | 중국 저장성 룽유 |
| **설립 연도** | 2011 |
| **공식 웹사이트** | [https://www.hcfa.cn](https://www.hcfa.cn) |
| **공급망 단계** | 서보 시스템 / 모터 / 드라이브 / 컨트롤러 |
| **기업 속성** | 국산 브랜드, 상장 기업 (688320.SH) |
| **모회사/소속 그룹** | 없음 (독립 상장) |
| **데이터 출처** | 공식 웹사이트, 제품 매뉴얼, 공개 리서치 보고서, WAIC 2026 보도 |

## 회사 소개

국내 범용 서보 및 로봇 핵심 부품 공급업체로, 서보 모터, 드라이브, PLC 및 일체형 관절 모듈을 제공합니다.

허촨 테크놀로지 X3E/X5E 시리즈 서보 시스템은 100W~7.5kW를 지원하며, EtherCAT, PROFINET, CANopen 등 버스를 지원하고, 엔코더는 최대 20비트입니다. 제품은 로봇, 태양광, 리튬 배터리 및 물류 자동화 분야에 널리 사용됩니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| X3E 서보 시스템 | 경제형 범용 서보 | SV-X3E + X3E 모터 | 로봇, 3C, 태양광 |
| X5E 서보 시스템 | 고성능 버스 서보 | SV-X5E | 리튬 배터리, 반도체, 휴머노이드 로봇 |

## 대표 제품

### X3E 시리즈 서보 모터 / X3E Series Servo Motor

> X3E 시리즈 서보 모터: [공식 자료](https://www.hcfa.cn)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 출력 범위 | 50W – 2kW | HCFA X3E 매뉴얼 |
| 정격 속도 | 3000 rpm | HCFA X3E 매뉴얼 |
| 엔코더 | 17비트 절대값 자기 엔코더 / 증분식 | HCFA X3E 매뉴얼 |
| 보호 등급 | IP65 | HCFA 기업 공고 |
| 정격 토크 | 미공개 | - |
| 과부하 용량 | 미공개 | - |
| 전압 등급 | AC 200–230V | HCFA X3E 매뉴얼 |

**기술적 특징**: 경제형 고신뢰성 서보 모터로, 범용 자동화 및 로봇 관절에 적합합니다.

**적용 분야**: 3C 자동화, 포장 기계, AGV, 협동 로봇.

### SV-X5E 서보 드라이브 / SV-X5E Servo Drive

> SV-X5E 서보 드라이브: [공식 자료](https://www.hcfa.cn)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 출력 범위 | 100W – 7.5kW | HCFA 2024 연례 보고서 |
| 전압 등급 | 220V / 380V | HCFA 2024 연례 보고서 |
| 통신 프로토콜 | EtherCAT / PROFINET / CANopen / Modbus | HCFA 2024 연례 보고서 |
| 제어 방식 | 펄스 / 버스 / 완전 폐루프 | HCFA 2024 연례 보고서 |
| 안전 기능 | STO, 동적 브레이크, 로터 보호 | HCFA 2024 연례 보고서 |
| 보호 | 독립형 에어 덕트, 컨포멀 코팅 | HCFA 2024 연례 보고서 |

**기술적 특징**: 고성능 버스형 서보 드라이브로, 다축 협업 및 로봇 고속 응답을 지원합니다.

**적용 분야**: 산업용 로봇, 휴머노이드 로봇, 리튬 배터리/태양광 생산 라인, 고급 CNC.

## 공급망 위치

- **상류 핵심 부품/재료**: 희토류 자석 재료, IGBT, PCB, 칩, 구조 부품
- **하류 고객/적용 분야**: 산업용 로봇, 휴머노이드 로봇, 태양광, 리튬 배터리, 물류 장비 제조업체
- **주요 경쟁사/벤치마크**: 인보브 테크놀로지, 리드샤인 인텔리전트, 야스카와, 파나소닉

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_hcfa`
- 제품 엔터티: `ent_component_hcfa_x3e_motor`, `ent_component_hcfa_x5e_drive`
- 주요 관계:
  - `ent_company_hcfa` -- `manufactures` --> `ent_component_hcfa_x3e_motor`
  - `ent_company_hcfa` -- `manufactures` --> `ent_component_hcfa_x5e_drive`

## 참고 자료

1. [공식 웹사이트](https://www.hcfa.cn)
2. [WAIC 2026 전시 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 리서치 보고서](https://www.inovance.com) (실제 제품 모델에 따라 확인하세요)
