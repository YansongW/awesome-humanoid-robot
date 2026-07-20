# 에머슨 일렉트릭 / Emerson Electric Co.

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 에머슨 일렉트릭 |
| **영문명** | Emerson Electric Co. |
| **본사** | 미국 미주리주 세인트루이스 |
| **설립 시간** | 1890년 |
| **공식 사이트** | [https://www.emerson.com](https://www.emerson.com) |
| **공급망 단계** | 프로세스 제어, 산업 자동화, 유체 제어, 전기 장비, 산업 소프트웨어 |
| **기업 속성** | 상장 기업 (NYSE: EMR) |
| **모회사/소속 그룹** | 없음 (독립 상장) |
| **데이터 출처** | Emerson 공식 사이트, 제품 카탈로그, 연례 보고서 |

## 회사 소개

에머슨 일렉트릭은 글로벌 프로세스 산업 자동화 및 유체 제어 기술의 선도 기업입니다.

에머슨은 DeltaV DCS, PACSystems PLC, Ovation 제어 시스템, ASCO 유체 제어, Rosemount 계측기 및 AspenTech 산업 소프트웨어를 통해 에너지, 화학, 전력, 생명 과학 등 산업에 자동화 솔루션을 제공합니다. PACSystems RSTi-EP 시리즈는 컴팩트 컨트롤러와 분산 I/O를 결합하여 모듈성, 확장성 및 정보 보안을 강조합니다. 센서, 밸브 및 모션 제어 제품은 로봇 및 스마트 장비에도 활용될 수 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|----------|----------|----------|----------|
| 프로세스 제어 / DCS | 연속 프로세스 자동화 | DeltaV / Ovation | 석유 가스, 화학, 전력 |
| PLC / PAC | 이산 및 혼합 제어 | PACSystems RX3i / RSTi-EP | 제조, 수처리, 에너지 |
| 유체 제어 및 계측기 | 밸브, 액추에이터, 센서 | ASCO / Rosemount / AVENTICS | 프로세스 공장, 로봇 공압 |

## 대표 제품

### Emerson PACSystems RSTi-EP PLC

> Emerson PACSystems RSTi-EP PLC: [공식 자료](https://www.emerson.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|----------|------|-----------|
| 제품 유형 | 프로그래밍 가능 자동화 컨트롤러 (PAC) | 공식 자료 |
| I/O 용량 | 최대 2,048 포인트 (구성에 따라 다름) | 공식 자료 |
| 스캔 속도 | 1 ms / 1K 부울 명령어 | 공식 자료 |
| 통신 인터페이스 | PROFINET, EtherNet/IP, Modbus/TCP, OPC UA | 공식 자료 |
| 프로그래밍 소프트웨어 | PAC Machine Edition | 공식 자료 |
| 이중화 지원 | 지원 | 공식 자료 |
| 작동 온도 | -20 °C ~ 60 °C | 공식 자료 |
| 가격 | 미공개 | 미공개 |

**기술 하이라이트**: 컴팩트 모듈형 PAC, 분산 I/O 확장, 내장 정보 보안 기능, 다중 프로토콜 통신 및 이중화 기능.

**적용 시나리오**: 수처리, 식음료, 이산 제조, 에너지, 생명 과학, 로봇 셀 제어 및 테스트 시스템.

## 휴머노이드 로봇과의 연관성

휴머노이드 로봇 프로토타입 개발 및 테스트는 많은 센서 데이터 수집과 주변 장치 제어가 필요하며, PACSystems의 모듈형 I/O와 빠른 스캔 성능은 실험실 테스트 벤치 및 생산 라인 제어 노드에 적합합니다.

## 공급망 위치

- **상류 핵심 부품/재료**: 프로세서, 전력 모듈, I/O 모듈, 센서, 공압 부품, PCB
- **하류 고객/적용 시나리오**: 석유 천연가스, 화학, 전력, 수처리, 이산 제조, 로봇 통합
- **주요 경쟁사/대상**: Honeywell, Siemens, Schneider Electric, Rockwell Automation

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_emerson`
- 제품 엔터티: `ent_product_emerson_pacsystems_rsti_ep`
- 주요 관계:
  - `ent_company_emerson` -- `manufactures` --> `ent_product_emerson_pacsystems_rsti_ep`

## 참고 자료

1. [에머슨 일렉트릭 공식 사이트](https://www.emerson.com)
2. [Emerson PACSystems RSTi-EP PLC 제품 페이지](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep)
3. Emerson PACSystems RSTi-EP 제품 카탈로그
