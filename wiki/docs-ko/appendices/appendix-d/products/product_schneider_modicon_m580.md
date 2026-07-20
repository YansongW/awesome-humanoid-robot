# Schneider Electric Modicon M580 ePAC / Modicon M580

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [슈나이더 일렉트릭 / Schneider Electric](../companies/company_schneider_electric.md) |
| **제품 카테고리** | 프로그래머블 자동화 컨트롤러(ePAC) |
| **출시일** | 2012년(현역 시리즈 지속 업데이트) |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [슈나이더 일렉트릭 공식 사이트](https://www.se.com) |

## 제품 개요

Modicon M580은 슈나이더 일렉트릭이 출시한 네이티브 이더넷 아키텍처 기반의 ePAC으로, PLC의 유연성과 DCS의 프로세스 제어 기능을 결합하며 내장형 네트워크 보안과 개방형 연결을 강조합니다.

이 시리즈는 Modbus TCP, EtherNet/IP 및 OPC UA 등의 프로토콜을 지원하며, 인버터, 서보, HMI 및 상위 MES/SCADA 시스템과 원활하게 통합되어 높은 가용성과 IIoT 연결이 필요한 스마트 제조 시나리오에 적합합니다.

## 제품 이미지

> Schneider Electric Modicon M580 ePAC: [공식 자료](https://www.se.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | ePAC(이더넷 프로그래머블 자동화 컨트롤러) | 공식 자료 |
| 프로그램/데이터 메모리 | 최대 64 MB | 공식 자료(CPU 모델에 따라 다름) |
| 최대 I/O 용량 | 미공개 | 미공개 |
| 통신 인터페이스 | EtherNet/IP, Modbus TCP, OPC UA | 공식 자료 |
| 보안 인증 | Achilles Level 2 | 공식 자료 |
| 공급 전압 | 24 VDC | 공식 자료 |
| 작동 온도 | 0 °C ~ 60 °C | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [슈나이더 일렉트릭 / Schneider Electric](../companies/company_schneider_electric.md)
- **핵심 부품/기술 출처**: 자체 개발 제어 펌웨어 및 소프트웨어; 프로세서, 이더넷 칩, 전력 소자, 저장 칩은 외부 조달.
- **하위 응용/고객**: 프로세스 산업, 에너지 및 수처리, 식음료, 휴머노이드 로봇 생산 라인 제어 중추.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_schneider_modicon_m580`
- 제조사 엔터티: `ent_company_schneider_electric`
- 주요 관계:
  - `ent_company_schneider_electric` → `manufactures` → `ent_product_schneider_modicon_m580`(관계 파일: `rel_ent_company_schneider_electric_manufactures_ent_product_schneider_modicon_m580.md`)

## 응용 시나리오

- **프로세스 제어**: 석유 가스, 화학, 수처리 등 연속 공정.
- **이산 제조**: 자동차, 전자, 식음료 생산 라인.
- **로봇 셀**: 휴머노이드 로봇 조립 및 테스트를 위한 제어 중추 제공.
- **에너지 관리**: 생산 라인 에너지 효율 모니터링 및 최적화.

## 경쟁 비교

| 비교 항목 | Schneider Electric Modicon M580 ePAC | Siemens S7-1500 | Rockwell ControlLogix |
|--------|---------------|--------|--------|
| 제품 유형 | ePAC | PLC | PLC |
| 네이티브 이더넷 | 예 | 예 | 예 |
| 대표 보안 인증 | Achilles Level 2 | 미공개 | 미공개 |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배포 권장 사항

프로세스와 이산 제어의 융합이 필요하고 네트워크 보안에 대한 규정 준수 요구 사항이 있는 시나리오에서는 M580을 우선 고려하십시오. 선정 시 I/O 포인트 수, 통신 프로토콜 및 이중화 요구 사항을 확인해야 합니다.

## 참고 자료

1. [슈나이더 일렉트릭 공식 사이트](https://www.se.com)
2. [Schneider Electric Modicon M580 ePAC 제품 페이지](https://www.se.com/us/en/product-range/1469-modicon-m580/)
3. Schneider Electric Annual Report / EcoStruxure 플랫폼 페이지
