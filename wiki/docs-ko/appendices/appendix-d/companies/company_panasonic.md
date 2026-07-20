# 파나소닉 홀딩스 / 파나소닉 인더스트리 / Panasonic Holdings Corporation / Panasonic Industry Co., Ltd.

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 파나소닉 홀딩스 / 파나소닉 인더스트리 |
| **영문명** | Panasonic Holdings Corporation / Panasonic Industry Co., Ltd. |
| **본사** | 일본 오사카 |
| **설립 연도** | 1918년 |
| **공식 사이트** | [https://www.panasonic.com](https://www.panasonic.com) |
| **공급망 단계** | 산업 자동화, 서보 모터, PLC, 센서, 전자 부품 |
| **기업 속성** | 상장 기업 (TYO: 6752, 지주 회사); 산업 자동화 사업은 Panasonic Industry가 운영 |
| **모회사/소속 그룹** | Panasonic Holdings Corporation |
| **데이터 출처** | Panasonic 공식 사이트, Panasonic Industry 제품 샘플, 공개 재무 보고서 |

## 회사 소개

파나소닉은 세계적으로 유명한 전자 및 산업 자동화 제품 제조업체이며, 산업 자동화 사업은 Panasonic Industry가 운영합니다.

Panasonic Industry는 MINAS 시리즈 서보 시스템, FP 시리즈 PLC, 센서, 커넥터, 배터리, 모터 등 산업 자동화 핵심 부품을 제공합니다. MINAS A6 시리즈는 2.0 kHz 속도 응답, 23비트 절대값 엔코더 및 컴팩트한 설계로 유명하며, 전자 제조, 반도체, 로봇 및 정밀 플랫폼에 널리 사용됩니다. 파나소닉은 또한 로봇용 원통형 배터리와 브러시리스 모터 등 핵심 부품을 제공합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|-----------|----------|-----------|-----------|
| 서보 시스템 | 고속 응답 서보 모터/드라이브 | MINAS A6 시리즈 | 전자, 반도체, 로봇 |
| PLC / 컨트롤러 | 컴팩트형 프로그래머블 컨트롤러 | FP-XH / FP0H / FP7 | 3C, 포장, 장비 |
| 부품 및 배터리 | 센서, 커넥터, 배터리 | PM 릴레이 / 18650 원통형 배터리 | 자동차, 로봇, 에너지 |

## 대표 제품

### Panasonic MINAS A6 서보 시스템

> Panasonic MINAS A6 서보 시스템: [공식 자료](https://www.panasonic.com)를 방문하여 확인하십시오.

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 제품 유형 | AC 서보 모터 + 드라이브 | 공식 자료 |
| 출력 범위 | 50 W ~ 5 kW | 공식 자료 (모델에 따름) |
| 속도 응답 | 2.0 kHz | 공식 자료 |
| 엔코더 | 23비트 절대값 엔코더 | 공식 자료 |
| 통신 인터페이스 | EtherCAT / RTEX / Modbus (모델에 따름) | 공식 자료 |
| 제어 모드 | 위치 / 속도 / 토크 / 완전 폐루프 | 공식 자료 |
| 보호 등급 | IP67 (모터, 모델에 따름) / IP20 (드라이브) | 공식 자료 |
| 가격 | 미공개 | 미공개 |

**기술적 특징**: 2.0 kHz 고속 응답, 23비트 고정밀 절대값 엔코더, 컴팩트 경량 설계, 풍부한 버스 옵션.

**적용 시나리오**: 3C 전자 실장, 반도체 장비, CNC 공작 기계, 산업용 로봇 암, 휴머노이드 로봇 팔 및 손가락 관절.

## 휴머노이드 로봇과의 연관성

휴머노이드 로봇의 손가락, 손목 등 소형 공간 관절에는 소형 고속 응답 서보가 필요하며, MINAS A6의 컴팩트 모터와 고정밀 엔코더는 휴머노이드 로봇 말단 관절에 정밀한 힘 제어 기반을 제공할 수 있습니다.

## 공급망 위치

- **상류 핵심 부품/재료**: 희토류 자석 재료, 규소 강판, 엔코더 칩, 전력 반도체, PCB, 하우징
- **하류 고객/적용 시나리오**: 3C 전자, 반도체, 자동차, 로봇, 의료 장비
- **주요 경쟁사/대상**: Yaskawa, Mitsubishi Electric, Inovance, Kollmorgen

## 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_panasonic`
- 제품 엔티티: `ent_product_panasonic_minas_a6`
- 주요 관계:
  - `ent_company_panasonic` -- `manufactures` --> `ent_product_panasonic_minas_a6`

## 참고 자료

1. [파나소닉 홀딩스 / 파나소닉 인더스트리 공식 사이트](https://www.panasonic.com)
2. [Panasonic MINAS A6 서보 시스템 제품 페이지](https://industry.panasonic.com/global/en/motor/servo_motor/a6)
3. Panasonic Industry MINAS A6 서보 카탈로그
