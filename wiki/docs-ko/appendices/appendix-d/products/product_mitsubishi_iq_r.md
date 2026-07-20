# Mitsubishi Electric MELSEC iQ-R R04CPU / MELSEC iQ-R

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [미쓰비시 전기 / Mitsubishi Electric](../companies/company_mitsubishi_electric.md) |
| **제품 카테고리** | 프로그래머블 로직 컨트롤러 (PLC) |
| **출시 시기** | 2014년 (현역 시리즈 지속 업데이트) |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [미쓰비시 전기 공식 사이트](https://www.mitsubishielectric.com) |

## 제품 개요

MELSEC iQ-R 시리즈는 미쓰비시 전기가 출시한 차세대 모듈형 PLC로, 고속 연산, 대용량 프로그램 메모리 및 내장 고속 네트워크를 특징으로 합니다.

R04CPU는 iQ-R 시리즈의 대표적인 CPU 모듈로, 나노초 단위 논리 연산, CC-Link IE 현장 네트워크 및 GX Works3 통합 프로그래밍 환경을 지원하며, 대규모 고속 생산 라인 제어에 적합합니다.

## 제품 이미지

> Mitsubishi Electric MELSEC iQ-R R04CPU: [공식 자료](https://www.mitsubishielectric.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 모듈형 PLC CPU | 공식 자료 |
| 프로그램 용량 | 40 k 스텝 | 공식 자료 (R04CPU) |
| 기본 명령어 처리 속도 | 0.98 ns | 공식 자료 |
| 최대 I/O 포인트 수 | 4,096 포인트 | 공식 자료 |
| 통신 인터페이스 | CC-Link IE Field, Ethernet, RS-232 | 공식 자료 |
| 프로그래밍 소프트웨어 | GX Works3 | 공식 자료 |
| 공급 전압 | 100–240 VAC / 24 VDC | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [미쓰비시 전기 / Mitsubishi Electric](../companies/company_mitsubishi_electric.md)
- **핵심 부품/기술 출처**: 자체 개발 CPU 및 FA 네트워크 칩; 전력 소자, 메모리, 커넥터 및 구조 부품은 외부 구매.
- **하위 응용/고객**: 자동차, 반도체 장비, 공작 기계, 로봇 통합, 휴머노이드 로봇 모션 제어 플랫폼.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_mitsubishi_iq_r`
- 제조사 엔터티: `ent_company_mitsubishi_electric`
- 주요 관계:
  - `ent_company_mitsubishi_electric` → `manufactures` → `ent_product_mitsubishi_iq_r` (관계 파일: `rel_ent_company_mitsubishi_electric_manufactures_ent_product_mitsubishi_iq_r.md`)

## 응용 시나리오

- **자동차 생산 라인**: 차체, 파워트레인 조립 제어.
- **반도체 장비**: 웨이퍼 이송, 노광기 제어.
- **CNC 공작 기계**: 고정밀 보간 및 축 제어.
- **로봇 시스템**: 휴머노이드 로봇 조립 및 테스트를 위한 고속 제어 제공.

## 경쟁 비교

| 비교 항목 | Mitsubishi Electric MELSEC iQ-R R04CPU | Siemens S7-1500 | OMRON NJ501 |
|--------|---------------|--------|--------|
| 프로그램 용량 | 40 k 스텝 (R04CPU) | 미공개 | 미공개 |
| 기본 명령어 속도 | 0.98 ns | 미공개 | 미공개 |
| 주요 현장 네트워크 | CC-Link IE | PROFINET | EtherCAT |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배포 권장 사항

일본계 장비 생태계 또는 이미 CC-Link IE 네트워크를 사용 중인 생산 라인에서 iQ-R 시리즈는 원활한 업그레이드를 제공할 수 있습니다. 선정 시 I/O 모듈 및 네트워크 토폴로지와의 일치 여부를 확인해야 합니다.

## 참고 자료

1. [미쓰비시 전기 공식 사이트](https://www.mitsubishielectric.com)
2. [Mitsubishi Electric MELSEC iQ-R R04CPU 제품 페이지](https://www.mitsubishielectric.com/fa/products/cnt/plc/r/r04cpu.html)
3. Mitsubishi Electric FA Global Website / MELSEC iQ-R Catalog
