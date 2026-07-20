# Agility Robotics Digit

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Agility Robotics](../companies/company_agility_robotics.md) |
| **제품 카테고리** | 물류/창고 휴머노이드 로봇 |
| **출시일** | 2019년 최초 출시; 현재 양산형 개량 버전 |
| **상태** | 양산/상업 배치 |
| **공식 사이트/출처** | [Agility Robotics 공식 사이트](https://agilityrobotics.com/) |

## 제품 개요

Agility Robotics Digit은 현재 창고 물류 분야에서 가장 널리 배치된 휴머노이드 로봇 중 하나입니다. 머리와 몸통이 일체화된 디자인과 역방향 무릎 관절을 채택하여, 좁은 통로, 계단, 경사로 등 인간 건축 환경에서 운반 상자(tote)를 옮기는 데 최적화되었습니다. Digit의 인식 시스템은 4개의 Intel RealSense 깊이 카메라, LiDAR, IMU 및 힘 센서로 구성되어, 외부 인프라 없이 자율 주행이 가능합니다.

Agility는 미국 오리건주 Salem에 RoboFab 휴머노이드 로봇 공장을 보유하고 있으며, 설계 연간 생산 능력은 10,000대입니다. Digit은 Amazon, GXO, Spanx 등 고객의 창고에서 분류 및 운반 작업을 수행하며, Robot-as-a-Service(RaaS) 모델을 통해 기업 고객에게 서비스를 제공하여 초기 구매 장벽을 낮췄습니다.

## 제품 이미지

> Agility Robotics Digit: [공식 자료](https://agilityrobotics.com/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 175 cm(높이) | 공개 사양 |
| 무게 | 약 63.5–65 kg | 공개 사양 |
| 자유도(전체) | 16–28 DOF(출처에 따라 다름) | 공개 사양 |
| 주요 성능 지표 | 적재 16 kg; 지속 운반 35 lb | 공식 사양 |
| 보행 속도 | 약 5.4 km/h | 공개 사양 |
| 배터리 지속 시간 | 약 4시간(일반 작업 기준) | 공식 사양 |
| 충전 | 자율 도킹 충전 | Agility Robotics |
| 가격 | 미공개(업계 추정 약 250,000 USD 또는 RaaS) | 제3자 추정 |

## 공급망 위치

- **제조사**: [Agility Robotics](../companies/company_agility_robotics.md)
- **핵심 부품/기술 출처**: Intel RealSense 깊이 카메라, LiDAR, 맞춤형 전기 구동 액추에이터, Agility Arc 클라우드 fleet 관리 플랫폼.
- **하위 응용/고객**: Amazon, GXO, Spanx, Toyota Canada 등 창고 및 제조 고객.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_agility_robotics_digit`
- 제조사 엔터티: `ent_company_agility_robotics`
- 주요 관계:
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit`(`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit`)

## 응용 시나리오

- **전자상거래 창고**: Amazon, GXO 등 창고에서 운반 상자(tote) 운반 및 분류 작업 수행.
- **소매 유통**: 선반에서 컨베이어 벨트로의 보충, 반품 정리 및 재고 이동.
- **제조 물류**: 자동차 및 소비재 공장 내 부품 배송 및 라인 사이드 보충.

## 경쟁 비교

| 비교 항목 | Agility Digit | Tesla Optimus Gen 3 | Figure 02 |
|--------|---------------|---------------------|-----------|
| 포지셔닝 | 물류 창고 휴머노이드 | 범용/산업 휴머노이드 | 산업 제조 휴머노이드 |
| 손 | 맞춤형 엔드 이펙터 | 22×2 정교한 손 | 16 DOF 정교한 손 |
| 비즈니스 모델 | RaaS / 기업 배치 | 목표 소매 | 기업 파일럿 |
| 핵심 강점 | 배치 규모, 배터리 지속 시간, RoboFab 생산 능력 | 비용 및 제조 규모 목표 | AI 모델 및 정교한 조작 |

## 구매 및 배치 권장 사항

- 기업 고객은 Agility Robotics 비즈니스 팀을 통해 RaaS 또는 구매 방안을 평가할 수 있으며, 일반적으로 창고 현장 조사가 필요합니다.
- 배치 전에 운반 상자 사양, 바닥 조건, Wi-Fi 커버리지 및 WMS와의 데이터 인터페이스를 확인해야 합니다.

## 참고 자료

1. [Agility Robotics 공식 사이트](https://agilityrobotics.com/)
2. [Robozaps – Agility Robotics Digit Review](https://blog.robozaps.com/b/agility-robotics-digit-review)
3. [Humanoid.Guide – Digit](https://humanoid.guide/product/digit/)
4. [The Robot Report – Agility Digit Deployments](https://www.therobotreport.com)
