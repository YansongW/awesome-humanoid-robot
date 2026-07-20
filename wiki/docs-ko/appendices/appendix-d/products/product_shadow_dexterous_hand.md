# Shadow Dexterous Hand / Shadow Dexterous Hand

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Shadow Robot Company / Shadow Robot Company](../companies/company_shadow_robot.md) |
| **제품 카테고리** | 정교한 손 / 말단 실행기 |
| **출시 시기** | 현역 주력 모델 |
| **상태** | 상업용/연구용 |
| **공식 홈페이지/출처** | [Shadow Robot Company 공식 홈페이지](https://www.shadowrobot.com) |

## 제품 개요

Shadow Dexterous Hand는 Shadow Robot Company가 출시한 고도로 인간을 닮은 다섯 손가락 정교한 손으로, 인간 손과 유사한 운동학 및 크기를 가지며 위치, 힘, 토크 다중 모드 제어를 지원합니다. 전 세계 연구 및 고급 원격 조작 분야에서 가장 영향력 있는 정교한 손 플랫폼 중 하나입니다.

## 제품 이미지

> Shadow Dexterous Hand: [공식 자료](https://www.shadowrobot.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 인간 성인 남성 손 크기 | 공식 사양서 |
| 무게 | 4.3 kg (전완 포함) | 공식 사양서 |
| 자유도 | 20 능동 + 4 수동 / 24 관절 | 공식 사양서 |
| 하중 | 강력 파지 4–5 kg | 공식 사양서 / 공개 보도 |
| 운동 속도 | 일반 관절 1.0 Hz | 공식 사양서 |
| 통신 인터페이스 | EtherCAT | 공식 사양서 |
| 제어 주파수 | 위치 루프 1 kHz / 토크 루프 5 kHz | 공식 사양서 |
| 공급 전압 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [Shadow Robot Company / Shadow Robot Company](../companies/company_shadow_robot.md)
- **핵심 부품/기술 출처**: 초소형 모터, 텐던, 힘/촉각 센서, 알루미늄 합금/엔지니어링 플라스틱, EtherCAT 제어 보드.
- **하위 응용/고객**: 대학 및 연구 기관, 의료 수술, 원자력 산업, 원격 조작, 휴머노이드 로봇.

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_product_shadow_dexterous_hand`
- 제조사 엔터티: `ent_company_shadow_robot`
- 주요 관계:
  - `rel_ent_company_shadow_robot_manufactures_ent_product_shadow_dexterous_hand` (`ent_company_shadow_robot` --> `manufactures` --> `ent_product_shadow_dexterous_hand`)

## 응용 시나리오

- **연구**: 파지 전략, 정교한 조작, AI 알고리즘 검증
- **의료**: 수술 훈련, 재활 로봇, 원격 수술
- **원자력 산업**: 위험 환경 원격 조작 및 유지보수
- **휴머노이드 로봇**: 고급 휴머노이드 플랫폼 말단 실행기

## 경쟁 비교

| 비교 항목 | 본 제품 | 국제 브랜드 | 국내 대응 제품 |
|--------|--------|----------|----------|
| 핵심 장점 | 매우 높은 자유도, 성숙한 ROS/EtherCAT 생태계, 연구 벤치마크 | 고급 정밀도 및 신뢰성 | 동일 구간 성능 경쟁 |
| 납기 | 비교적 짧음/구성에 따라 다름 | 비교적 김 | 비교적 짧음 |
| 서비스 대응 | 신속 | 보통 | 신속 |
| 가격 수준 | 매우 높음 | 고급 | 중저가 |

## 선택 및 배치 권장 사항

- 선정 시 하중, 이동 거리, 속도 및 정밀도 요구 사항에 따라 적합한 모델을 매칭해야 하며, 필요 시 제조사에 문의하여 맞춤형 솔루션을 받으십시오.
- 배치 전 하중 관성 식별, 강성 매칭 및 진동 억제 튜닝을 수행하여 전체 시스템과의 호환성을 보장하는 것이 좋습니다.

## 참고 자료

1. [Shadow Robot Company 공식 홈페이지](https://www.shadowrobot.com)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 연구 보고서](https://www.shadowrobot.com) (실제 제품 모델에 따라 확인하세요)
