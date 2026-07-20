# 가속 진화 / Booster Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중국어명** | 가속 진화 |
| **영문명** | Booster Robotics |
| **본사** | 중국 베이징 |
| **설립 시간** | 2023년 |
| **공식 사이트** | [https://www.booster.tech](https://www.booster.tech) |
| **공급망 단계** | 완제품 OEM / 휴머노이드 로봇 개발 플랫폼 |
| **기업 속성** | 칭화대 배경, 개발자/경진대회 플랫폼, RoboCup 챔피언 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Booster 공식 사이트, Bipedal 문서, 과학창업판 일보/36氪 |

## 회사 소개

가속 진화는 개발자, 대학 및 로봇 경진대회를 대상으로 가볍고 유연하며 내구성이 뛰어난 휴머노이드 로봇 플랫폼을 제공하며, 2025 RoboCup AdultSize 챔피언을 차지했습니다.

Booster T1은 키 약 1.2m, 무게 30kg, 전신 23 DOF, Intel i7 1370p와 NVIDIA Jetson AGX Orin(200 TOPS)을 탑재하고 ROS2, 시뮬레이션 플랫폼 및 모바일 App 제어를 지원합니다. T1은 걷기, 축구, 팔굽혀펴기, 무술 등 동적 동작을 수행할 수 있으며, 연구 및 경진대회 분야에서 널리 사용되는 플랫폼입니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| 개발자 휴머노이드 로봇 | 연구, 경진대회, 교육 | Booster T1 | 대학, RoboCup, 개발자 |
| 입문 플랫폼 | 저비용 교육 | Booster K1 | 교육, 초보자 |

## 대표 제품

### Booster T1

![Booster T1](https://www.althumans.com/media/catalog/product/cache/7e65f7ea2c9ff177580b02a356862407/a/h/ah-booster-t1-01.jpg)

> 이미지 출처: AltHumans 제품 이미지(Booster T1 딜러).

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 118 cm(높이) | Booster 공식 사이트 / Bipedal 문서 |
| 무게 | 30 kg | Booster 공식 사이트 / Bipedal 문서 |
| 자유도 | 23 DOF(선택 구성 최대 41 DOF) | Bipedal 문서 / 공개 보도 |
| 부하/토크 | 무릎 관절 최대 토크 130 N·m; 중공축 관절 모터 | Bipedal 문서 |
| 속도/회전수 | 전방향 보행, 구체적인 속도 미공개 | Bipedal 문서 |
| 배터리 지속 시간 | 10.5 Ah 배터리; 보행 약 2시간, 서 있기 약 4시간 | Booster 공식 사이트 |
| 인터페이스/통신 | ROS 2, USB, Ethernet, Wi-Fi 6, 블루투스 5.2, 모바일 App | Booster 공식 사이트 |
| 가격 | 약 19.9만 위안부터(공개 보도) | 36氪 / 공개 보도 |

**기술 하이라이트**: Intel i7 1370p + NVIDIA Jetson AGX Orin 200 TOPS, 전방향 보행, 간섭 저항, 시뮬레이션 플랫폼 지원(Isaac Sim/Mujoco), RoboCup 2025 챔피언 버전

**응용 시나리오**: 대학 연구, RoboCup 경진대회, 운동 제어 알고리즘 검증, AI 훈련, 산업 자동화 프로토타입.

### Booster K1

> Booster K1: [공식 자료](https://www.booster.tech)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 미공개 | - |
| 무게 | 미공개 | - |
| 자유도 | 미공개 | - |
| 부하/토크 | 미공개 | - |
| 속도/회전수 | 미공개 | - |
| 배터리 지속 시간 | 미공개 | - |
| 인터페이스/통신 | 미공개 | - |
| 가격 | 5999달러부터 | Booster 공식 사이트 |

**기술 하이라이트**: 입문형 지능형 개발 플랫폼, 휴머노이드 로봇 학습 및 개발 진입 장벽 완화

**응용 시나리오**: 교육, 입문 개발, 경량 연구.

## 공급망 위치

- **상류 핵심 부품/소재**: 자체 개발 중공축 관절 모터, NVIDIA Jetson AGX Orin, Intel i7 컴퓨팅 플랫폼, 깊이 카메라, 9축 IMU, 배터리.
- **하류 고객/응용 시나리오**: 대학 연구팀, RoboCup 참가팀, 개발자, 산업 프로토타입 고객.
- **주요 경쟁사/대상**: Yushu G1, Songyan N2, Robotis OP3

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_booster_robotics`
- 제품 엔터티: `ent_product_booster_t1`
- 주요 관계:
  - `ent_company_booster_robotics` -- `manufactures` --> `ent_product_booster_t1`
  - `ent_product_booster_t1` -- `uses` --> `ent_component_nvidia_jetson_agx_orin`

## 참고 자료

1. [Booster T1 공식 사이트](https://www.booster.tech/booster-t1/)
2. [Bipedal – Booster T1 문서](http://www.docs.bipedal.de/projects/t1/html/overview.html)
3. [과학창업판 일보 – CES 보도](https://www.cls.cn/detail/1912332)
