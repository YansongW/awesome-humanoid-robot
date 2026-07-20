# Bosch Rexroth ctrlX CORE / ctrlX CORE

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [보쉬 렉스로스 / Bosch Rexroth](../companies/company_bosch_rexroth.md) |
| **제품 카테고리** | 산업 자동화 컨트롤러 |
| **출시일** | 2020년 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [보쉬 렉스로스 공식 홈페이지](https://www.boschrexroth.com) |

## 제품 개요

ctrlX CORE는 Bosch Rexroth ctrlX AUTOMATION 플랫폼의 핵심 컨트롤러로, Linux 기반 실시간 운영 체제를 사용하며 PLC, 모션, 로봇 및 IoT 기능을 앱 방식으로 확장할 수 있습니다.

컨트롤러는 다중 프로토콜 통신 기능을 내장하여 엣지 컴퓨팅 노드로 상위 클라우드 플랫폼과 연결할 수 있으며, 높은 유연성과 소프트웨어 정의 자동화가 필요한 시스템에 적합합니다.

## 제품 이미지

> Bosch Rexroth ctrlX CORE: [공식 자료](https://www.boschrexroth.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 산업 자동화 컨트롤러 / IPC | 공식 자료 |
| 운영 체제 | ctrlX OS (Linux 실시간 커널 기반) | 공식 자료 |
| 프로세서 | 미공개 | 미공개 |
| 제어 축 수 | 최대 99축 | 공식 자료 |
| 통신 인터페이스 | EtherCAT, Sercos III, PROFINET, OPC UA, MQTT | 공식 자료 |
| 공급 전압 | 24 VDC | 공식 자료 |
| 작동 온도 | 0 °C ~ 50 °C | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [보쉬 렉스로스 / Bosch Rexroth](../companies/company_bosch_rexroth.md)
- **핵심 부품/기술 출처**: 자체 개발 ctrlX OS 및 제어 소프트웨어; 프로세서, 통신 모듈, 전력 소자, 스토리지는 외부 구매.
- **하위 응용/고객**: 스마트 공작 기계, 포장, 물류, 모바일 기계, 휴머노이드 로봇 제어 플랫폼.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_bosch_rexroth_ctrlx_core`
- 제조사 엔터티: `ent_company_bosch_rexroth`
- 주요 관계:
  - `ent_company_bosch_rexroth` → `manufactures` → `ent_product_bosch_rexroth_ctrlx_core` (관계 파일: `rel_ent_company_bosch_rexroth_manufactures_ent_product_bosch_rexroth_ctrlx_core.md`)

## 응용 시나리오

- **스마트 공작 기계**: 다축 연동 및 공정 최적화.
- **포장 기계**: 플라잉 커팅, 트래킹 커팅 및 전자 캠.
- **이동 로봇**: AGV/AMR 운동 제어 및 스케줄링.
- **휴머노이드 로봇**: 본체 컨트롤러 또는 관절 구동 게이트웨이로 사용.

## 경쟁 비교

| 비교 항목 | Bosch Rexroth ctrlX CORE | Siemens SIMATIC S7-1500 | Beckhoff CX2030 |
|--------|---------------|--------|--------|
| 운영 체제 | Linux RT (ctrlX OS) | 실시간 Windows / Linux | TwinCAT/BSD |
| 소프트웨어 형태 | app 기반 | 전통적인 PLC 프로젝트 | TwinCAT 런타임 |
| 제어 축 수 | 최대 99축 | 모델에 따라 다름 | 모델에 따라 다름 |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배포 권장 사항

소프트웨어 정의 자동화, 타사 알고리즘의 빠른 통합 및 클라우드-엣지 협업이 필요한 프로젝트에 적합합니다. 앱 생태계 성숙도와 실시간 요구 사항을 평가해야 합니다.

## 참고 자료

1. [보쉬 렉스로스 공식 홈페이지](https://www.boschrexroth.com)
2. [Bosch Rexroth ctrlX CORE 제품 페이지](https://www.boschrexroth.com/en/us/products/product-groups/controls/ctrlx-automation/ctrlx-core)
3. Bosch Rexroth ctrlX AUTOMATION 제품 페이지
