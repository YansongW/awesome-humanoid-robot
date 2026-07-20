# 허니웰 / Honeywell International Inc.

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 허니웰 |
| **영문명** | Honeywell International Inc. |
| **본사** | 미국 노스캐롤라이나주 샬럿 |
| **설립 연도** | 1906년 |
| **공식 사이트** | [https://www.honeywell.com](https://www.honeywell.com) |
| **공급망 단계** | 산업 자동화, 프로세스 제어, 빌딩 자동화, 센서, PLC |
| **기업 속성** | 상장 기업 (NASDAQ: HON) |
| **모회사/소속 그룹** | 없음 (독립 상장) |
| **데이터 출처** | 허니웰 공식 사이트, 프로세스 제어 제품 자료, 공개 재무제표 |

## 회사 소개

허니웰은 글로벌 선도적인 산업 자동화, 항공우주 및 빌딩 기술 기업입니다.

허니웰의 산업 자동화 사업은 프로세스 제어(Experion PKS), 안전 시스템, 현장 계측기, PLC(ControlEdge) 및 산업용 소프트웨어를 핵심으로 하며, 석유 가스, 화학, 전력, 제약 등 산업을 포괄합니다. ControlEdge PLC는 Experion PKS와의 원활한 통합, IIoT 연결 및 사이버 보안을 강조하며, 혼합 산업 및 핵심 인프라에 적합합니다. 해당 센서 및 제어 기술은 로봇 환경 인식 및 프로세스 모니터링에도 사용될 수 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| DCS / 프로세스 제어 | 대규모 연속 프로세스 제어 | Experion PKS | 석유 가스, 화학, 전력 |
| PLC / RTU | 이산 및 혼합 제어 | ControlEdge PLC / RTU | 프로세스 공장, 원격 사이트 |
| 산업용 소프트웨어 및 보안 | 생산 관리, 사이버 보안 | Honeywell Forge / SMX | 스마트 팩토리, 에너지 |

## 대표 제품

### Honeywell ControlEdge PLC

> Honeywell ControlEdge PLC: [공식 자료](https://www.honeywell.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 프로그래머블 로직 컨트롤러 (PLC) | 공식 자료 |
| 통신 프로토콜 | Modbus/TCP, EtherNet/IP, OPC UA, MQTT | 공식 자료 |
| 이중화 지원 | 지원 (구성에 따름) | 공식 자료 |
| 프로그래밍 표준 | IEC 61131-3 | 공식 자료 |
| 작동 온도 | -20 °C ~ 60 °C | 공식 자료 |
| 안전 인증 | 미공개 | 미공개 |
| 공급 전압 | 24 VDC | 공식 자료 |
| 가격 | 미공개 | 미공개 |

**기술 하이라이트**: Experion PKS와의 심층 통합, 내장 OPC UA/MQTT 지원, IIoT 및 프로세스 산업용 설계, 이중화 및 고가용성 옵션.

**적용 시나리오**: 석유 가스 저장 및 운송, 화학 프로세스, 전력 보조 제어, 수처리, 제약, 휴머노이드 로봇 테스트 환경의 프로세스 모니터링.

## 휴머노이드 로봇과의 연관성

휴머노이드 로봇 제조에는 많은 환경 모니터링, 에너지 및 프로세스 데이터 수집이 수반되며, 허니웰의 PLC 및 센서 네트워크는 실험실 및 생산 라인에 안정적인 프로세스 제어 및 데이터 기반을 제공할 수 있습니다.

## 공급망 위치

- **상류 핵심 부품/소재**: 반도체, 센서 소자, PCB, 전원 모듈, 커넥터, 케이스
- **하류 고객/적용 시나리오**: 석유 가스, 화학, 전력, 제약, 빌딩 및 인프라
- **주요 경쟁사/대상**: Emerson, Siemens, ABB, Yokogawa

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_honeywell`
- 제품 엔터티: `ent_product_honeywell_control_edge`
- 주요 관계:
  - `ent_company_honeywell` -- `manufactures` --> `ent_product_honeywell_control_edge`

## 참고 자료

1. [허니웰 공식 사이트](https://www.honeywell.com)
2. [Honeywell ControlEdge PLC 제품 페이지](https://process.honeywell.com/us/en/products/control-edge-plc)
3. Honeywell Process Solutions ControlEdge PLC 데이터시트
