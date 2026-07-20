# Honeywell ControlEdge PLC / ControlEdge PLC

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 '미공개'로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [허니웰 / Honeywell](../companies/company_honeywell.md) |
| **제품 카테고리** | 프로그래머블 로직 컨트롤러 (PLC) |
| **출시일** | 2016년 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [허니웰 공식 사이트](https://www.honeywell.com) |

## 제품 개요

ControlEdge PLC는 허니웰이 프로세스 및 이산 혼합 애플리케이션을 위해 출시한 차세대 PLC로, IEC 61131-3 프로그래밍과 다양한 산업용 이더넷 프로토콜을 지원합니다.

이 제품은 Experion PKS 분산 제어 시스템에 직접 연결할 수 있으며, OPC UA 및 MQTT를 통해 IIoT 데이터를 클라우드로 전송할 수 있어 높은 신뢰성과 사이버 보안 인증이 필요한 핵심 인프라에 적합합니다.

## 제품 이미지

> Honeywell ControlEdge PLC: [공식 자료](https://www.honeywell.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 프로그래머블 로직 컨트롤러 (PLC) | 공식 자료 |
| 통신 프로토콜 | Modbus/TCP, EtherNet/IP, OPC UA, MQTT | 공식 자료 |
| 이중화 지원 | 지원 (구성에 따라 다름) | 공식 자료 |
| 프로그래밍 표준 | IEC 61131-3 | 공식 자료 |
| 작동 온도 | -20 °C ~ 60 °C | 공식 자료 |
| 안전 인증 | 미공개 | 미공개 |
| 공급 전압 | 24 VDC | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [허니웰 / Honeywell](../companies/company_honeywell.md)
- **핵심 부품/기술 출처**: 자체 개발 제어 펌웨어 및 Experion 통합 소프트웨어; 프로세서, 통신 칩, I/O 모듈, 전원 공급 장치는 외부 조달.
- **하위 애플리케이션/고객**: 프로세스 산업, 전력, 수처리, 제약, 스마트 제조, 로봇 테스트 플랫폼.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_honeywell_control_edge`
- 제조사 엔터티: `ent_company_honeywell`
- 주요 관계:
  - `ent_company_honeywell` → `manufactures` → `ent_product_honeywell_control_edge` (관계 파일: `rel_ent_company_honeywell_manufactures_ent_product_honeywell_control_edge.md`)

## 적용 시나리오

- **석유 가스 화학**: 저장 및 운송, 반응기, 압축기 제어.
- **전력 수처리**: 보조 제어 시스템 및 원격 모니터링.
- **제약 식품**: 배치 제어 및 추적.
- **로봇 테스트**: 휴머노이드 로봇 연구소에 프로세스 모니터링 제공.

## 경쟁 비교

| 비교 항목 | Honeywell ControlEdge PLC | Emerson PACSystems | Siemens S7-1500 |
|--------|---------------|--------|--------|
| 목표 시장 | 프로세스/혼합 산업 | 이산/프로세스 산업 | 이산/범용 |
| DCS 통합 | Experion PKS | DeltaV | SIMATIC PCS 7 |
| IIoT 프로토콜 | OPC UA / MQTT | OPC UA / MQTT | OPC UA / PROFINET |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배포 권장 사항

이미 허니웰 DCS 시스템을 보유한 프로세스 공장에서 이산 제어를 확장하거나, IIoT 연결 및 높은 환경 적응성이 필요한 시나리오에 적합합니다.

## 참고 자료

1. [허니웰 공식 사이트](https://www.honeywell.com)
2. [Honeywell ControlEdge PLC 제품 페이지](https://process.honeywell.com/us/en/products/control-edge-plc)
3. Honeywell Process Solutions ControlEdge PLC 데이터시트
