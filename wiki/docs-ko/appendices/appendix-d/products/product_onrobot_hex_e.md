# OnRobot HEX-E QC 6축 힘/토크 센서 / OnRobot HEX-E QC 6-Axis Force/Torque Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [OnRobot(온로봇) / OnRobot](../companies/company_onrobot.md) |
| **제품 카테고리** | 협동로봇 6축 힘/토크 센서 |
| **출시 시간** | 지속 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [OnRobot HEX-E QC 6축 힘/토크 센서 제품/자료 페이지](https://www.onrobot.com/en/products/he-x) |

## 제품 개요

HEX-E QC는 OnRobot이 협동로봇 말단을 위해 설계한 6축 힘/토크 센서로, Quick Changer 퀵 체인지 인터페이스가 통합되어 플러그 앤 플레이 설치를 지원합니다. 실시간으로 6축 힘/토크 데이터를 측정하여 로봇이 정밀 조립, 일정 힘 연마, 표면 처리 및 충돌 감지를 수행할 수 있도록 돕습니다.

## 제품 이미지

> OnRobot HEX-E QC 6축 힘/토크 센서: [공식 자료](https://www.onrobot.com/en/products/he-x)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 6축 힘/토크 센서 | 공식 홈페이지 |
| 힘 측정 범위 (Fx/Fy/Fz) | ±100 N / ±100 N / ±200 N | 공식 홈페이지/데이터시트 |
| 토크 측정 범위 (Mx/My/Mz) | ±10 Nm / ±10 Nm / ±10 Nm | 공식 홈페이지/데이터시트 |
| 정밀도 | 미공개 | - |
| 분해능 | 미공개 | - |
| 샘플링 주파수 | 미공개 | - |
| 과부하 용량 | 약 500% FS | 공식 홈페이지/데이터시트 |
| 보호 등급 | IP67 | 공식 홈페이지/데이터시트 |
| 통신 인터페이스 | TCP/IP, USB, EtherNet/IP, PROFINET | 공식 홈페이지/데이터시트 |
| 통합 인터페이스 | Quick Changer / 로봇 플랜지 | 공식 홈페이지/데이터시트 |
| 전원 공급 | 24 V DC | 공식 홈페이지/데이터시트 |
| 무게 | 약 350 g | 공식 홈페이지/데이터시트 |
| 작동 온도 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [OnRobot(온로봇) / OnRobot](../companies/company_onrobot.md)
- **핵심 부품/기술 출처**: 자체 개발 힘 감지 유닛, 신호 처리 및 통신 회로, Quick Changer 기계식 인터페이스, 산업용 밀봉 케이스.
- **하위 응용/고객**: 협동로봇 OEM, 자동차 및 전자 제조사, 휴머노이드 로봇 완성체 제조사, 자동화 시스템 통합 업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_onrobot_hex_e`
- 부품 엔터티: `ent_component_onrobot_hex_e_sensor`
- 제조사 엔터티: `ent_company_onrobot`
- 주요 관계:
  - `rel_ent_company_onrobot_manufactures_ent_product_onrobot_hex_e` (`ent_company_onrobot` → `manufactures` → `ent_product_onrobot_hex_e`)
  - `rel_ent_company_onrobot_manufactures_ent_component_onrobot_hex_e_sensor` (`ent_company_onrobot` → `manufactures` → `ent_component_onrobot_hex_e_sensor`)
  - `rel_ent_product_onrobot_hex_e_uses_ent_component_onrobot_hex_e_sensor` (`ent_product_onrobot_hex_e` → `uses` → `ent_component_onrobot_hex_e_sensor`)

## 응용 시나리오

- **힘 제어 조립**: 정밀 삽입, 기어 조립 시의 유연한 삽입 및 위치 결정.
- **일정 힘 연마/광택**: 일정한 접촉력을 유지하여 표면 품질 일관성 향상.
- **삽입 및 테스트**: 커넥터, 스위치 등 부품의 힘-변위 테스트.
- **휴머노이드 로봇 팔**: 말단 6축 힘 감지를 통한 파지 및 상호 작용.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 협동로봇 6축 힘 센서 | ATI Nano25 | Bota Systems SensONE |
| 힘 범위 | ±100 N / ±200 N | ±250 N / ±1000 N | ±200 N / ±500 N |
| 통신 | TCP/IP/USB/EtherNet/IP | 아날로그/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |
| 핵심 장점 | 퀵 체인지 통합, 생태계 성숙 | 초소형 크기, 높은 과부하 | 소형 고가성비 |

## 구매 및 배포 권장 사항

- 목표 응용 분야의 분해능, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: OnRobot(온로봇) / OnRobot](../companies/company_onrobot.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [OnRobot 공식 홈페이지](https://www.onrobot.com)
2. [OnRobot HEX-E QC 6축 힘/토크 센서 제품/자료 페이지](https://www.onrobot.com/en/products/he-x)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
