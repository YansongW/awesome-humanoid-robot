# OMRON NJ501 Sysmac 컨트롤러 / NJ501

> 본 항목은 [부록 D 핵심 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 핵심 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [오므론 / OMRON](../companies/company_omron.md) |
| **제품 카테고리** | 머신 자동화 컨트롤러 (MAC) |
| **출시일** | 2011년부터 (현역 주력 모델) |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [오므론 공식 홈페이지](https://www.omron.com) |

## 제품 개요

NJ501 시리즈는 오므론 Sysmac 플랫폼의 머신 자동화 컨트롤러로, 기존 PLC의 로직 제어와 다축 모션 제어를 동일한 하드웨어 및 소프트웨어 환경에 통합합니다.

EtherCAT 버스를 통해 NJ501은 서보, 인버터, I/O 및 비전 장치를 동기화하여 제어할 수 있으며, IEC 61131-3 프로그래밍과 PLCopen 모션 제어 기능 블록을 지원하여 로직+모션 통합이 필요한 고급 장비에 적합합니다.

## 제품 이미지

> OMRON NJ501 Sysmac 컨트롤러: [공식 자료](https://www.omron.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 머신 자동화 컨트롤러 (MAC) | 공식 자료 |
| 최대 제어 축 수 | 64축 (EtherCAT) | 공식 자료 |
| 최대 I/O 포인트 수 | 2,560 포인트 | 공식 자료 (모델에 따라 다름) |
| 프로그램 용량 | 미공개 | 미공개 |
| 통신 인터페이스 | EtherCAT, EtherNet/IP, USB, OPC UA | 공식 자료 |
| 프로그래밍 표준 | IEC 61131-3 / PLCopen 모션 제어 기능 블록 | 공식 자료 |
| 공급 전압 | 24 VDC | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [오므론 / OMRON](../companies/company_omron.md)
- **핵심 부품/기술 출처**: 자체 개발 컨트롤러 하드웨어 및 Sysmac Studio 소프트웨어; 프로세서, 통신 칩, 전력 소자, 스토리지는 외부 조달.
- **하위 응용/고객**: 3C 제조, 자동차 부품, 포장 기계, 로봇 시스템 통합, 휴머노이드 로봇 프로토타입 제어.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_omron_nj501`
- 제조사 엔터티: `ent_company_omron`
- 주요 관계:
  - `ent_company_omron` → `manufactures` → `ent_product_omron_nj501` (관계 파일: `rel_ent_company_omron_manufactures_ent_product_omron_nj501.md`)

## 응용 시나리오

- **3C 전자**: 칩 마운터, 조립, 검사 장비의 모션 제어.
- **포장 기계**: 다축 동기화 및 플라잉 커팅, 추적 커팅 제어.
- **로봇 통합**: 산업용 로봇 및 휴머노이드 로봇 관절 제어.
- **자동차 부품**: 엔진, 변속기 조립 라인.

## 경쟁 비교

| 비교 항목 | OMRON NJ501 Sysmac 컨트롤러 | Mitsubishi iQ-R | Schneider M580 |
|--------|---------------|--------|--------|
| 제어 축 수 | 최대 64축 | 미공개 | 미공개 |
| 프로그래밍 환경 | Sysmac Studio | GX Works3 | EcoStruxure |
| 주요 통신 | EtherCAT / EtherNet/IP | CC-Link IE / Ethernet | 이더넷 / Modbus TCP |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배치 권장 사항

로직과 모션이 깊게 통합되어야 하고 축 수가 수십 축 이내인 장비의 경우 NJ501을 우선 고려할 수 있습니다. 선정 시 I/O 규모와 EtherCAT 슬레이브 호환성을 확인하십시오.

## 참고 자료

1. [오므론 공식 홈페이지](https://www.omron.com)
2. [OMRON NJ501 Sysmac 컨트롤러 제품 페이지](https://www.omron.com.cn/products/family/3194/)
3. OMRON FA 제품 카탈로그 / Sysmac Studio 문서
