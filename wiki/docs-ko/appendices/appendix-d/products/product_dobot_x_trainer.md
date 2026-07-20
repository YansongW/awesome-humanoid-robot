# Dobot X-Trainer / Dobot X-Trainer

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Yuejiang Technology / Dobot / Yuejiang Technology](../companies/company_dobot.md) |
| **제품 카테고리** | 양팔 원격 조작 AI 훈련 플랫폼 |
| **출시 시간** | 2024년 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [https://www.dobot.cn](https://www.dobot.cn) |

## 제품 개요

구현 지능 데이터 수집, 모방 학습, 연구 교육, AGI 시뮬레이션 및 경진 대회.

Dobot X-Trainer는 Yuejiang Technology의 대표 제품입니다. 산업용 Nova 2 협동 로봇 팔(종속), ±0.05 mm 반복 위치 정밀도, 25 Hz 종단 간 운동 인터페이스, VR/조이스틱 원격 조작, 데이터 수집 SDK. 주요 사양은 다음과 같습니다: 베이스 1400×1000 mm(경량 버전, 손잡이 제외)(크기), 미공개(무게), 주종 6-DOF×2, 종속 Nova 2 협동 로봇 팔×2(자유도).

## 제품 이미지

![Dobot X-Trainer](https://www.dobot-robots.com/media/upload/2024/x-trainer/tab.png)

> 이미지 출처: Dobot 공식 홈페이지 제품 이미지.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 베이스 1400×1000 mm(경량 버전, 손잡이 제외) | Dobot X-Trainer 사용자 매뉴얼 |
| 무게 | 미공개 | - |
| 자유도 | 주종 6-DOF×2, 종속 Nova 2 협동 로봇 팔×2 | 사용자 매뉴얼 |
| 부하/토크 | 단일 팔 2 kg, 양팔 3 kg; 그리퍼 최대 행정 95 mm | 브로셔 |
| 속도/회전 속도 | 말단 최고 속도 1.6 m/s | 브로셔 |
| 배터리 지속 시간 | 상용 전원 공급 | - |
| 인터페이스/통신 | 기가비트 이더넷 포트, USB, WiFi(Nova 2 옵션) | 사용자 매뉴얼 |
| 가격 | 미공개 | 문의 필요 |

## 공급망 위치

- **제조사**: [Yuejiang Technology / Dobot / Yuejiang Technology](../companies/company_dobot.md)
- **핵심 부품/기술 출처**: 자체 개발 협동 로봇 조인트, 모터, 감속기, 컨트롤러; Intel RealSense D405 깊이 카메라; NVIDIA Jetson 컴퓨팅 플랫폼.
- **하위 응용/고객**: 구현 지능 데이터 수집, 모방 학습, 연구 교육, AGI 시뮬레이션 및 경진 대회.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_dobot_x_trainer`
- 제조사 엔터티: `ent_company_dobot`
- 주요 관계:
  - `rel_ent_company_dobot_manufactures_ent_product_dobot_x_trainer` (`ent_company_dobot` → `manufactures` → `ent_product_dobot_x_trainer`)
  - `ent_product_dobot_x_trainer` -- `uses` --> `ent_component_dobot_nova2`

## 응용 시나리오

- **구현 지능 데이터 수집, 모방 학습, 연구 교육, AGI 시뮬레이션 및 경진 대회.**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁 제품 |
|--------|--------|----------|
| 포지셔닝 | 양팔 원격 조작 AI 훈련 플랫폼 | 유사 제품은 특정 시나리오에 따라 다름 |
| 핵심 장점 | 산업용 Nova 2 협동 로봇 팔(종속), ±0.05 mm 반복 위치 정밀도, 25 Hz 종단 간 운동 인터페이스, VR/조이스틱 원격 조작, 데이터 수집 SDK | 미공개 |
| 가격 | 미공개 | 미공개 |

## 구매 및 배포 제안

- 공식 채널을 통해 최신 소프트웨어 버전, SDK 지원 및 사후 교육을 확인하는 것이 좋습니다.
- 연구 및 교육 사용자는 2차 개발 인터페이스, 시뮬레이션 플랫폼 호환성 및 커뮤니티 활동성을 우선 평가해야 합니다.
- 산업 사용자는 특정 공정에 따라 부하, 정밀도, 보호 등급 및 통합 인터페이스를 검증해야 합니다.

## 참고 자료

1. [Dobot X-Trainer 제품 페이지](https://www.dobot-robots.com/products/humanoid-robots/x-trainer.html)
2. [Dobot X-Trainer 브로셔](https://www.roscomponents.com/wp-content/uploads/2026/02/X-Trainer-leaflet-Lightweight-Base_Brochure.pdf)
3. [Yuejiang Technology 공식 홈페이지](https://www.dobot.cn)
