# 타산 테크놀로지 TS-F+ 다중 모드 촉각 센서 / Tashan TS-F+ Multimodal Tactile Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [타산 테크놀로지 / Tashan Technology](../companies/company_tashan.md) |
| **제품 카테고리** | 다중 모드 촉각 센서 / 전자 피부 |
| **출시 시간** | 2024년 (세계 로봇 대회 최초 공개) |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [타산 테크놀로지 공식 사이트](https://www.iteschina.com) |

## 제품 개요

타산 테크놀로지 TS-F+ 다중 모드 촉각 센서는 휴머노이드 로봇의 정교한 손과 전자 피부를 위한 고집적 정전 용량식 촉각 감지 유닛입니다. 센서에는 타산 테크놀로지가 자체 개발한 디지털-아날로그 혼합 AI 촉각 칩이 탑재되어 있으며, R-SpiNNaker 분산형 뇌 모방 아키텍처와 펄스 신경망(SNN)을 기반으로 혼합 신호에서 7~10차원의 촉각 정보(3차원 힘, 재질 인식, 근접 감지 및 접촉 위치 등)를 추출할 수 있습니다.

TS-F+는 복잡한 환경에서 유연하고 깨지기 쉬우며 이형 물체에 대한 적응형 힘 파지를 지원하며, 펜 쥐기, 물 따르기, 계란 잡기 등의 정밀 작업을 수행할 수 있습니다. 타산 테크놀로지는 또한 MuJoCo 및 NVIDIA Isaac Sim을 기반으로 오픈 소스 촉각 시뮬레이션 모델을 출시하여 개발자가 시뮬레이션 환경에서 저비용으로 촉각 인식 전략을 훈련하고 실제 센서 데이터와 정렬할 수 있도록 했습니다.

## 제품 이미지

> Tashan TS-F+: [공식 자료](https://www.iteschina.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 감지 원리 | 정전 용량식 | 공식 사이트/공개 보도 |
| 인식 차원 | 3차원 힘, 재질, 근접 감지, 접촉 위치 등 7~10차원 | 공개 보도 |
| 핵심 칩 | 자체 개발 디지털-아날로그 혼합 AI 촉각 칩 | 공개 보도 |
| 칩 아키텍처 | R-SpiNNaker 분산형 뇌 모방 아키텍처 | 공개 보도 |
| 알고리즘 모델 | 3차원 공간 정전 용량 단층 촬영 + SNN 펄스 신경망 | 공개 보도 |
| 공간 해상도 | 미공개 | - |
| 감지점 밀도 | 미공개 | - |
| 측정 범위(법선 힘) | 미공개 | - |
| 응답 시간 | 미공개 | - |
| 샘플링 주파수 | 미공개 | - |
| 통신 인터페이스 | 디지털 인터페이스(주류 로봇 버스 호환) | 공식 사이트 공개 자료 |
| 공급 전압 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 보호 등급 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [타산 테크놀로지 / Tashan Technology](../companies/company_tashan.md)
- **핵심 부품/기술 출처**: 자체 개발 디지털-아날로그 혼합 AI 촉각 칩, R-SpiNNaker 뇌 모방 아키텍처, 정전 용량식 감응 재료; 유연 기재 및 패키징 재료는 외부 조달.
- **하류 응용/고객**: 휴머노이드 로봇 정교한 손, 협동 로봇 말단, 전자 피부, 자동차 내장, 가전 터치, 소비자 전자 제품.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_tashan_tactile_skin`
- 제조사 엔터티: `ent_company_tashan`
- 부품 엔터티: `ent_component_tashan_tactile_sensor_chip`
- 주요 관계:
  - `rel_ent_company_tashan_manufactures_ent_product_tashan_tactile_skin` (`ent_company_tashan` → `manufactures` --> `ent_product_tashan_tactile_skin`)
  - `rel_ent_company_tashan_manufactures_ent_component_tashan_tactile_sensor_chip` (`ent_company_tashan` → `manufactures` --> `ent_component_tashan_tactile_sensor_chip`)
  - `rel_ent_product_tashan_tactile_skin_uses_ent_component_tashan_tactile_sensor_chip` (`ent_product_tashan_tactile_skin` → `uses` --> `ent_component_tashan_tactile_sensor_chip`)

## 응용 시나리오

- **휴머노이드 로봇 정교한 손**: 손가락 끝/손가락 배 촉각 인식, 정밀 파지, 미끄러짐 감지 및 재질 인식 구현.
- **전자 피부**: 로봇 팔, 몸통을 덮어 근접 감지 및 접촉 감지 안전 보호 제공.
- **자동차 및 가전**: 스티어링 휠, 시트, 터치 패널의 지능형 힘/재질 인식.
- **구현 지능 훈련**: 시뮬레이션 모델과 결합하여 촉각 전략 훈련 및 sim-to-real 전이 수행.

## 경쟁 비교

| 비교 항목 | 타산 TS-F+ | 파시니 PX-6AX | XELA uSkin |
|--------|------------|---------------|------------|
| 감지 원리 | 정전 용량식 + AI 칩 | 6D 홀 어레이식 | 자기 저항식 3축 |
| 인식 차원 | 7~10차원 | 15가지 촉각 정보 | 3축 힘 |
| 특화 기능 | 재질 인식, 근접 감지, 오픈 소스 시뮬레이션 | 고집적 정교한 손 | 고밀도 3축, 부드럽고 내구성 우수 |
| 핵심 장점 | 뇌 모방 칩 + 시뮬레이션 생태계 | 풀스택 센서-정교한 손-완제품 | 통합 용이, 디지털 출력 |

## 구매 및 배포 권장 사항

- 정교한 손 또는 전자 피부의 곡면 구조에 따라 센서 부착 방안을 맞춤 제작해야 합니다.
- 시뮬레이션 모델은 실제 센서 데이터와 혼합 훈련이 가능하므로, 프로젝트 초기 단계에서 촉각 시뮬레이션을 도입하여 데이터를 축적하는 것이 좋습니다.

## 참고 자료

1. [타산 테크놀로지 공식 사이트](https://www.iteschina.com)
2. [SENSOR CHINA 2025 – 타산 테크놀로지 참가 보도](https://www.sekorm.com/news/584921525.html)
3. [21세기 경제 보도 – 타산 테크놀로지 CEO 인터뷰](http://mp.weixin.qq.com/s?__biz=Mzk4ODE4MjkzNA==&mid=2247484687&idx=1&sn=84fba2c156a5ed6bbac57f2f0dc097e7)
4. [부록 D 기업 목록](../index-companies.md)
