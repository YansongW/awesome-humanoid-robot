# 미쓰비시전기 / Mitsubishi Electric Corporation

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 미쓰비시전기 |
| **영문명** | Mitsubishi Electric Corporation |
| **본사** | 일본 도쿄 |
| **설립일** | 1921년 |
| **공식 웹사이트** | [https://www.mitsubishielectric.com](https://www.mitsubishielectric.com) |
| **공급망 단계** | 공장 자동화(FA), PLC, 서보 시스템, CNC, 산업용 로봇 |
| **기업 속성** | 상장 기업(TYO: 6503) |
| **모회사/소속 그룹** | 미쓰비시 그룹(단일 지배 모회사 없음, 독립 상장) |
| **데이터 출처** | 미쓰비시전기 공식 웹사이트, FA 제품 샘플, 공개 재무제표 |

## 회사 소개

미쓰비시전기는 세계적으로 선도적인 공장 자동화(FA) 및 전기 기계 제품 종합 제조업체입니다.

미쓰비시전기의 FA 사업은 MELSEC 프로그래머블 컨트롤러, MELSERVO 서보, CNC 수치 제어 시스템, 산업용 로봇(MELFA) 및 시각화 소프트웨어를 포괄합니다. iQ 플랫폼은 고속, 고신뢰성 및 네트워크 통합으로 유명하며, 자동차, 반도체, 공작 기계, 엘리베이터 등 분야에서 깊은 기반을 가지고 있습니다. 미쓰비시전기의 서보 및 모션 제어 기술은 휴머노이드 로봇의 관절 구동 및 정밀 위치 제어에 핵심 부품을 제공할 수 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|-----------|----------|-----------|-----------|
| PLC / 컨트롤러 | 고속 모듈식 컨트롤러 | MELSEC iQ-R / iQ-F | 자동차, 반도체, 공작 기계 |
| 서보 시스템 | 고정밀 모션 제어 | MELSERVO-J5 / J4 | 전자, 로봇, 포장 |
| 산업용 로봇 | 수직 다관절 / SCARA | MELFA RV / RH / F 시리즈 | 조립, 운반, 용접 |

## 대표 제품

### Mitsubishi Electric MELSEC iQ-R R04CPU

> Mitsubishi Electric MELSEC iQ-R R04CPU: [공식 자료](https://www.mitsubishielectric.com)를 방문하여 확인하십시오.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 제품 유형 | 모듈식 PLC CPU | 공식 자료 |
| 프로그램 용량 | 40 k 스텝 | 공식 자료(R04CPU) |
| 기본 명령 처리 속도 | 0.98 ns | 공식 자료 |
| 최대 I/O 포인트 수 | 4,096 포인트 | 공식 자료 |
| 통신 인터페이스 | CC-Link IE Field, Ethernet, RS-232 | 공식 자료 |
| 프로그래밍 소프트웨어 | GX Works3 | 공식 자료 |
| 공급 전압 | 100–240 VAC / 24 VDC | 공식 자료 |
| 가격 | 미공개 | 미공개 |

**기술적 특징**: 나노초 단위 명령 처리, 내장 CC-Link IE 필드 네트워크, 통합 엔지니어링 소프트웨어 GX Works3, 모듈식 고확장성.

**적용 시나리오**: 자동차 생산 라인 제어, 반도체 장비, CNC 공작 기계, 엘리베이터 제어, 휴머노이드 로봇 조립 및 테스트 장비.

## 휴머노이드 로봇과의 연관성

휴머노이드 로봇 관절 서보는 고속 응답과 정밀 위치 제어에 엄격한 요구 사항을 가지며, 미쓰비시전기의 MELSERVO 및 iQ-R 컨트롤러는 관절 모듈 개발 및 전체 기계 모션 제어를 위한 고신뢰성 플랫폼을 제공할 수 있습니다.

## 공급망 위치

- **상류 핵심 부품/재료**: 반도체, 파워 모듈, 엔코더, 자성 재료, 구조 부품, PCB
- **하류 고객/적용 시나리오**: 자동차 제조, 반도체 장비, 공작 기계, 엘리베이터, 에너지 인프라
- **주요 경쟁사/벤치마크**: Siemens, OMRON, Schneider Electric, Fanuc

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_mitsubishi_electric`
- 제품 엔터티: `ent_product_mitsubishi_iq_r`
- 주요 관계:
  - `ent_company_mitsubishi_electric` -- `manufactures` --> `ent_product_mitsubishi_iq_r`

## 참고 자료

1. [미쓰비시전기 공식 웹사이트](https://www.mitsubishielectric.com)
2. [Mitsubishi Electric MELSEC iQ-R R04CPU 제품 페이지](https://www.mitsubishielectric.com/fa/products/cnt/plc/r/r04cpu.html)
3. Mitsubishi Electric FA Global Website / MELSEC iQ-R Catalog
