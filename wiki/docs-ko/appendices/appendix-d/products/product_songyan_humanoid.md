# 송연동력 N2 / Songyan N2

> 본 항목은 [부록 D 중점 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 중점 제품 Wiki 목록](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [송연동력 / Songyan Dynamics / Noetix Robotics](../companies/company_songyan_dynamics.md) |
| **제품 카테고리** | 범용 휴머노이드 로봇 |
| **출시일** | 2025년 3월 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [https://noetixrobotics.com](https://noetixrobotics.com) |

## 제품 개요

고등교육 연구, 유아 동반, 엔터테인먼트 공연, 상업 전시, 로봇 경진대회.

송연동력 N2는 송연동력의 대표 제품입니다. 세계 최초 다중 장면 연속 공중제비, MPC+강화학습 운동 제어, 경량 알루미늄 합금 구조, 이중 엔코더 관절, 선택 가능 NVIDIA Jetson Orin Nano Super. 주요 사양: 1180×470×290 mm (서 있을 때) (크기), 약 30 kg (무게), 18 DOF (다리당 5 DOF×2, 팔당 4 DOF×2) (자유도).

## 제품 이미지

![송연동력 N2](https://www.noetixrobotics.com/mtsc/uploads/Ckeditor/Images/2025-12-25/N2.webp)

> 이미지 출처: 송연동력 공식 홈페이지 제품 이미지.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | 1180×470×290 mm (서 있을 때) | 송연 공식 홈페이지 / 바이두 백과 |
| 무게 | 약 30 kg | 송연 공식 홈페이지 |
| 자유도 | 18 DOF (다리당 5 DOF×2, 팔당 4 DOF×2) | 송연 공식 홈페이지 |
| 부하/토크 | 무릎 관절 최대 토크 150 N·m; 지속 보행 부하 약 5 kg | 송연 공식 홈페이지 |
| 속도/회전수 | 달리기 속도 최대 3.5 m/s | 송연 공식 홈페이지 / 바이두 백과 |
| 배터리 지속 시간 | 약 1–2 시간 (48 V / 7 Ah) | 송연 공식 홈페이지 |
| 인터페이스/통신 | Wi-Fi 6, 블루투스 5.2, OTA, 2차 개발 인터페이스 (EDU 버전) | 송연 공식 홈페이지 |
| 가격 | 3.99만 위안부터 | 공개 보도 |

## 공급망 위치

- **제조사**: [송연동력 / Songyan Dynamics / Noetix Robotics](../companies/company_songyan_dynamics.md)
- **핵심 부품/기술 출처**: 자체 개발 고성능 관절 모터 및 드라이버, 알루미늄 합금 구조물, 깊이 카메라, IMU, 리튬 배터리; 핵심 부품 국산화율 거의 100%.
- **하류 응용/고객**: 고등교육 연구, 유아 동반, 엔터테인먼트 공연, 상업 전시, 로봇 경진대회.

## 지식 그래프 노드와 관계

- 제품 엔터티: `ent_product_songyan_dynamics_n2`
- 제조사 엔터티: `ent_company_songyan_dynamics`
- 주요 관계:
  - `rel_ent_company_songyan_dynamics_manufactures_ent_product_songyan_dynamics_n2` (`ent_company_songyan_dynamics` → `manufactures` → `ent_product_songyan_dynamics_n2`)
  - `ent_product_songyan_dynamics_n2` -- `uses` --> `ent_component_songyan_joint_motor`

## 응용 시나리오

- **고등교육 연구, 유아 동반, 엔터테인먼트 공연, 상업 전시, 로봇 경진대회.**
- **상업 서비스**: 안내, 접객, 전시 및 브랜드 인터랙션에 사용.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁 제품 |
|-----------|---------|----------------|
| 포지셔닝 | 범용 휴머노이드 로봇 | 유사 제품은 특정 시나리오에 따라 다름 |
| 핵심 강점 | 세계 최초 다중 장면 연속 공중제비, MPC+강화학습 운동 제어, 경량 알루미늄 합금 구조, 이중 엔코더 관절, 선택 가능 NVIDIA Jetson Orin Nano Super | 미공개 |
| 가격 | 3.99만 위안부터 | 미공개 |

## 구매 및 배치 권장 사항

- 공식 채널을 통해 최신 소프트웨어 버전, SDK 지원 및 사후 교육을 확인하는 것을 권장합니다.
- 연구 및 교육 사용자는 2차 개발 인터페이스, 시뮬레이션 플랫폼 호환성 및 커뮤니티 활동성을 우선 평가해야 합니다.
- 산업 사용자는 특정 공정에 따라 부하, 정밀도, 보호 등급 및 통합 인터페이스를 검증해야 합니다.

## 참고 자료

1. [송연동력 N2 제품 페이지](https://noetixrobotics.com/n2)
2. [송연동력 공식 홈페이지](https://noetixrobotics.com/)
3. [바이두 백과 – 송연동력 N2](https://baike.baidu.com/item/%E6%9D%BE%E5%BB%B6%E5%8A%A8%E5%8A%9BN2/67393633)
