# Emerson PACSystems RSTi-EP PLC / RSTi-EP

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [에머슨 일렉트릭 / Emerson Electric](../companies/company_emerson.md) |
| **제품 카테고리** | 프로그래밍 가능 자동화 컨트롤러 (PAC) |
| **출시 시기** | 현역 (RSTi-EP 시리즈 지속 업데이트) |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [에머슨 일렉트릭 공식 사이트](https://www.emerson.com) |

## 제품 개요

PACSystems RSTi-EP는 에머슨이 컴팩트하고 고밀도 애플리케이션을 위해 출시한 PAC 플랫폼으로, 컨트롤러와 확장 가능한 분산 I/O를 통합했습니다.

이 플랫폼은 PROFINET, EtherNet/IP, Modbus/TCP 및 OPC UA를 지원하며, 정보 보안 및 이중화 옵션을 갖추고 있어 높은 유연성과 신뢰성이 요구되는 이산 및 혼합 공정 애플리케이션에 적합합니다.

## 제품 이미지

> Emerson PACSystems RSTi-EP PLC: [공식 자료](https://www.emerson.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 프로그래밍 가능 자동화 컨트롤러 (PAC) | 공식 자료 |
| I/O 용량 | 최대 2,048 포인트 (구성에 따라 다름) | 공식 자료 |
| 스캔 속도 | 1 ms / 1K 부울 명령어 | 공식 자료 |
| 통신 인터페이스 | PROFINET, EtherNet/IP, Modbus/TCP, OPC UA | 공식 자료 |
| 프로그래밍 소프트웨어 | PAC Machine Edition | 공식 자료 |
| 이중화 지원 | 지원 | 공식 자료 |
| 작동 온도 | -20 °C ~ 60 °C | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [에머슨 일렉트릭 / Emerson Electric](../companies/company_emerson.md)
- **핵심 부품/기술 출처**: 자체 개발 PAC 펌웨어 및 Machine Edition 소프트웨어; 프로세서, 통신 모듈, I/O 모듈, 전원 공급 장치는 외부 조달.
- **하위 애플리케이션/고객**: 수처리, 식음료, 생명 과학, 에너지, 로봇 테스트 및 통합 시스템.

## 지식 그래프 노드 및 관계

- 제품 엔티티: `ent_product_emerson_pacsystems_rsti_ep`
- 제조사 엔티티: `ent_company_emerson`
- 주요 관계:
  - `ent_company_emerson` → `manufactures` → `ent_product_emerson_pacsystems_rsti_ep` (관계 파일: `rel_ent_company_emerson_manufactures_ent_product_emerson_pacsystems_rsti_ep.md`)

## 적용 시나리오

- **수처리**: 펌프장, 폭기, 여과 제어.
- **식음료**: 충진, 포장, 컨베이어 라인.
- **생명 과학**: 배치 제어 및 장비 통합.
- **로봇 테스트**: 휴머노이드 로봇 연구소에 고속 I/O 및 모션 조정 제공.

## 경쟁 비교

| 비교 항목 | Emerson PACSystems RSTi-EP PLC | Honeywell ControlEdge | Siemens S7-1500 |
|--------|---------------|--------|--------|
| 제품 형태 | 컴팩트 PAC + 분산 I/O | 모듈형 PLC | 모듈형 PLC |
| 스캔 속도 | 1 ms / 1K 부울 | 미공개 | 미공개 |
| 주요 통신 | PROFINET / EtherNet/IP | EtherNet/IP / Modbus | PROFINET / EtherNet/IP |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배포 권장 사항

I/O 포인트가 분산되어 있고 공간 및 스캔 속도에 대한 요구 사항이 있는 시나리오에서는 RSTi-EP를 우선 고려하십시오. 모델 선정 시 I/O 모듈 유형과 네트워크 보안 기능 라이선스를 확인하십시오.

## 참고 자료

1. [에머슨 일렉트릭 공식 사이트](https://www.emerson.com)
2. [Emerson PACSystems RSTi-EP PLC 제품 페이지](https://www.emerson.com/en-us/catalog/controllers/pacsystems-rsti-ep)
3. Emerson PACSystems RSTi-EP 제품 카탈로그
