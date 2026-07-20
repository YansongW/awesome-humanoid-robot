# Bota Systems SensONE 6축 힘/토크 센서 / Bota Systems SensONE 6-Axis Force/Torque Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 날짜: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Bota Systems (보타 시스템) / Bota Systems](../companies/company_bota_systems.md) |
| **제품 카테고리** | 6축 힘/토크 센서 |
| **출시일** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Bota Systems SensONE 6축 힘 센서 제품/자료 페이지](https://www.bota-systems.com/sensone) |

## 제품 개요

SensONE은 Bota Systems가 협동 로봇 및 휴머노이드 로봇을 위해 설계한 주력 6축 힘/토크 센서로, 드래그 티칭, 힘 제어 조립, 연마 및 충돌 감지를 지원합니다. 컴팩트한 원반형 구조로 로봇 엔드 이펙터 플랜지에 직접 장착할 수 있으며, 다양한 측정 범위와 통신 인터페이스 옵션을 제공합니다.

## 제품 이미지

> Bota Systems SensONE 6축 힘 센서: [공식 자료](https://www.bota-systems.com/sensone)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 6축 힘/토크 센서 | 공식 홈페이지 |
| 직경 | 약 80 mm | 공식 홈페이지/데이터시트 |
| 높이 | 약 21 mm | 공식 홈페이지/데이터시트 |
| 무게 | 약 290 g | 공식 홈페이지/데이터시트 |
| 힘 측정 범위 (Fx/Fy) | ±200 N | 공식 홈페이지/데이터시트 |
| 힘 측정 범위 (Fz) | ±500 N | 공식 홈페이지/데이터시트 |
| 토크 측정 범위 (Mx/My/Mz) | ±8 Nm | 공식 홈페이지/데이터시트 |
| 정밀도 | 미공개 | - |
| 과부하 용량 | 약 500% FS | 공식 홈페이지/데이터시트 |
| 샘플링 주파수 | 최대 1000 Hz | 공식 홈페이지/데이터시트 |
| 통신 인터페이스 | EtherCAT / Ethernet / USB / RS485 / CAN | 공식 홈페이지/데이터시트 |
| 보호 등급 | IP67 | 공식 홈페이지/데이터시트 |
| 전원 공급 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [Bota Systems (보타 시스템) / Bota Systems](../companies/company_bota_systems.md)
- **핵심 부품/기술 출처**: 자체 개발 6축 힘 감지 탄성체 및 디커플링 알고리즘, 실리콘 스트레인 게이지, 신호 컨디셔닝 회로, 산업용 하우징 및 커넥터.
- **하위 응용 분야/고객**: 협동 로봇 OEM, 휴머노이드 로봇 완성체 제조사, 의료 재활 장비, 자동화 통합 업체, 연구 기관.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_bota_systems_sensone`
- 부품 엔터티: `ent_component_bota_systems_sensone_sensor`
- 제조사 엔터티: `ent_company_bota_systems`
- 주요 관계:
  - `rel_ent_company_bota_systems_manufactures_ent_product_bota_systems_sensone` (`ent_company_bota_systems` → `manufactures` → `ent_product_bota_systems_sensone`)
  - `rel_ent_company_bota_systems_manufactures_ent_component_bota_systems_sensone_sensor` (`ent_company_bota_systems` → `manufactures` → `ent_component_bota_systems_sensone_sensor`)
  - `rel_ent_product_bota_systems_sensone_uses_ent_component_bota_systems_sensone_sensor` (`ent_product_bota_systems_sensone` → `uses` → `ent_component_bota_systems_sensone_sensor`)

## 응용 분야

- **협동 로봇 힘 제어**: 엔드 이펙터 힘 피드백을 통한 유연한 조립, 연마 및 그라인딩.
- **휴머노이드 로봇 손목**: 6축 힘 감지 제공, 파지, 균형 및 충돌 감지 지원.
- **드래그 티칭**: 힘 피드백 기반 빠른 궤적 티칭 및 프로그래밍.
- **의료 재활 로봇**: 저지연 힘 감지 피드백을 재활 훈련 및 수술 보조에 사용.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 협동 로봇 6축 힘 센서 | ATI Nano 시리즈 | OnRobot HEX-E |
| 측정 범위 | Fx/Fy ±200 N / Fz ±500 N | 다중 모델 | ±100 N / ±10 Nm |
| 통신 | EtherCAT/Ethernet/USB/CAN | 아날로그/DAQ/EtherCAT | TCP/IP/USB/EtherNet/IP |
| 핵심 장점 | 컴팩트, 높은 가성비 | 초소형 크기, 높은 과부하 | 플러그 앤 플레이 생태계 |

## 구매 및 배치 권장 사항

- 대상 응용 분야의 분해능, 측정 범위, 정밀도 또는 연산 요구 사항에 따라 특정 모델을 선택하십시오.
- 배치 전 인터페이스, 전원 공급, 방열, 기계적 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 최신 펌웨어, SDK 및 기술 지원을 위해 공식 채널 또는 공인 대리점을 통해 문의하는 것이 좋습니다.

## 관련 항목

- [제조사: Bota Systems (보타 시스템) / Bota Systems](../companies/company_bota_systems.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Bota Systems 공식 홈페이지](https://www.bota-systems.com)
2. [Bota Systems SensONE 6축 힘 센서 제품/자료 페이지](https://www.bota-systems.com/sensone)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
