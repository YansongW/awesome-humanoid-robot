# 보쉬 렉스로스 / Bosch Rexroth AG

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 보쉬 렉스로스 |
| **영문명** | Bosch Rexroth AG |
| **본사** | 독일 로어 (Lohr am Main) |
| **설립일** | 2001년 (Rexroth 기원은 1795년까지 거슬러 올라감) |
| **공식 웹사이트** | [https://www.boschrexroth.com](https://www.boschrexroth.com) |
| **공급망 단계** | 구동 및 제어 기술, 유압, 선형 구동, 서보 시스템, 산업 자동화 플랫폼 |
| **기업 속성** | 비상장 (Robert Bosch GmbH 전액 출자 자회사) |
| **모회사/소속 그룹** | Robert Bosch GmbH |
| **데이터 출처** | Bosch Rexroth 공식 웹사이트, 제품 페이지, 보쉬 그룹 연례 보고서 |

## 회사 소개

보쉬 렉스로스는 글로벌 구동 및 제어 기술 분야의 시스템 공급업체입니다.

보쉬 렉스로스는 유압, 전기 구동 및 제어, 선형 구동 및 조립 기술, IoT 및 자동화 플랫폼 등의 제품을 제공하며, 공장 자동화, 이동 기계 및 산업 4.0에 서비스를 제공합니다. ctrlX AUTOMATION 플랫폼은 "스마트폰 방식"의 앱 생태계와 개방형 Linux 실시간 시스템을 특징으로 하며, PLC, 모션, 로봇, IoT 및 머신 비전 애플리케이션을 지원합니다. 서보 및 선형 구동 제품은 휴머노이드 로봇의 관절 및 구동 기구에도 적합합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 자동화 플랫폼 | 개방형, 앱 기반 제어 | ctrlX CORE / ctrlX OS | 공작 기계, 포장, 이동 기계 |
| 전기 구동 | 서보 구동 및 모터 | IndraDrive / MS2N | 로봇, 공작 기계, 물류 |
| 선형 구동 | 가이드 레일, 볼스크류, 전기 실린더 | 볼 가이드 레일 / 행성 롤러 스크류 | 조립, 반도체, 의료 |

## 대표 제품

### Bosch Rexroth ctrlX CORE

> Bosch Rexroth ctrlX CORE: [공식 자료](https://www.boschrexroth.com)를 방문하여 확인하십시오.

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

**기술적 특징**: 앱 기반 아키텍처, 개방형 Linux 실시간 시스템, 통합 PLC/모션/IoT/로봇 기능, 다중 프로토콜 통신.

**적용 시나리오**: 스마트 공작 기계, 포장 기계, 이동 로봇, 창고 물류, 휴머노이드 로봇 제어 시스템 및 엣지 컴퓨팅.

## 휴머노이드 로봇과의 연관성

휴머노이드 로봇 개발에는 유연한 소프트웨어 아키텍처와 다축 실시간 제어가 필요하며, ctrlX CORE의 앱 생태계와 개방형 인터페이스는 로봇 본체 컨트롤러 또는 관절 구동 게이트웨이로 사용될 수 있습니다.

## 공급망 위치

- **상류 핵심 부품/재료**: 프로세서, 전력 반도체, 유압 부품, 베어링, 알루미늄, PCB
- **하류 고객/적용 시나리오**: 공작 기계, 포장, 이동 기계, 자동차, 물류 자동화
- **주요 경쟁사/대응 기업**: Siemens, Beckhoff, B&R, Schneider Electric

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_bosch_rexroth`
- 제품 엔터티: `ent_product_bosch_rexroth_ctrlx_core`
- 주요 관계:
  - `ent_company_bosch_rexroth` -- `manufactures` --> `ent_product_bosch_rexroth_ctrlx_core`

## 참고 자료

1. [보쉬 렉스로스 공식 웹사이트](https://www.boschrexroth.com)
2. [Bosch Rexroth ctrlX CORE 제품 페이지](https://www.boschrexroth.com/en/us/products/product-groups/controls/ctrlx-automation/ctrlx-core)
3. Bosch Rexroth ctrlX AUTOMATION 제품 페이지
