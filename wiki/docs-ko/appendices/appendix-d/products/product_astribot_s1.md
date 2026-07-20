# Astribot S1 / Astribot S1

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [성진지능 / Astribot](../companies/company_astribot.md) |
| **제품 카테고리** | 범용 휴머노이드 로봇 |
| **출시일** | 2024년 8월 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [https://www.astribot.com](https://www.astribot.com) |

## 제품 개요

옷 개기, 요리, 청소, 서예, 다도, 연구 실험, 노인 돌봄, 신소매 전시.

Astribot S1은 성진지능의 대표 제품입니다. 케이블 구동 방식, ±0.1 mm 반복 위치 정밀도, 100 m/s² 말단 가속도, 힘 제어 안전, VR 원격 조작 및 코드 없는 시각화 인터페이스를 갖추고 있습니다. 주요 사양: 170 cm(높이)(크기), 80 kg(무게), 전신 23 DOF(단일 팔 7 DOF×2, 몸통 4 DOF, 머리 2 DOF, 전방향 바퀴형 섀시 3 DOF)(자유도).

## 제품 이미지

![Astribot S1](https://cdn.shopify.com/s/files/1/0659/1437/2184/files/Astribot_image_1_resized.png?v=1768350773&width=800)

> 이미지 출처: Astribot 제품 자료 이미지(제3자 대리점).

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | 170 cm(높이) | Astribot 공식 홈페이지 |
| 무게 | 80 kg | Astribot 공식 홈페이지 |
| 자유도 | 전신 23 DOF(단일 팔 7 DOF×2, 몸통 4 DOF, 머리 2 DOF, 전방향 바퀴형 섀시 3 DOF) | Astribot 공식 홈페이지 / 기술 문서 |
| 부하/토크 | 단일 팔 수평 신장 정격 부하 5 kg, 최대 10 kg | Astribot 공식 홈페이지 |
| 속도/회전 속도 | 말단 최고 속도 ≥10 m/s | Astribot 공식 홈페이지 |
| 배터리 지속 시간 | 4–6시간(전원 연결 지원) | Astribot 공식 홈페이지 |
| 인터페이스/통신 | ROS 2 / Python SDK, Gigabit Ethernet, Wi-Fi | 기술 문서 |
| 가격 | 연구용 약 ¥50만; 기업/연구용 약 $96,000–$150,000 | 공개 보도 |

## 공급망 위치

- **제조사**: [성진지능 / Astribot](../companies/company_astribot.md)
- **핵심 부품/기술 출처**: 자체 개발 케이블 구동 액추에이터, 고성능 모터, 힘/토크 센서, 컴퓨팅 플랫폼; 외부 구매 카메라, 라이다, 배터리.
- **하류 응용/고객**: 옷 개기, 요리, 청소, 서예, 다도, 연구 실험, 노인 돌봄, 신소매 전시.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_astribot_s1`
- 제조사 엔터티: `ent_company_astribot`
- 주요 관계:
  - `rel_ent_company_astribot_manufactures_ent_product_astribot_s1`(`ent_company_astribot` → `manufactures` → `ent_product_astribot_s1`)
  - `ent_product_astribot_s1` -- `uses` --> `ent_component_astribot_cable_actuator`

## 응용 시나리오

- **옷 개기, 요리, 청소, 서예, 다도, 연구 실험, 노인 돌봄, 신소매 전시.**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁 제품 |
|-----------|---------|----------------|
| 포지셔닝 | 범용 휴머노이드 로봇 | 유사 제품은 구체적인 시나리오에 따라 다름 |
| 핵심 장점 | 케이블 구동 방식, ±0.1 mm 반복 위치 정밀도, 100 m/s² 말단 가속도, 힘 제어 안전, VR 원격 조작 및 코드 없는 시각화 인터페이스 | 미공개 |
| 가격 | 연구용 약 ¥50만; 기업/연구용 약 $96,000–$150,000 | 미공개 |

## 구매 및 배치 권장 사항

- 공식 채널을 통해 최신 소프트웨어 버전, SDK 지원 및 사후 교육을 확인하는 것이 좋습니다.
- 연구 및 교육 사용자는 2차 개발 인터페이스, 시뮬레이션 플랫폼 호환성 및 커뮤니티 활동성을 우선 평가해야 합니다.
- 산업 사용자는 구체적인 공정에 따라 부하, 정밀도, 보호 등급 및 통합 인터페이스를 검증해야 합니다.

## 참고 자료

1. [Astribot 공식 홈페이지 제품 페이지](https://www.astribot.com/en/product)
2. [RobotScope – Astribot 회사 자료](https://robotscope.net/companies/astribot/)
3. [바이두 백과 – Astribot S1](https://baike.baidu.com/item/Astribot%20S1/64813493)
