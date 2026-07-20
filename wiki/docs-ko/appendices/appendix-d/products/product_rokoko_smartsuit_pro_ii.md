# Rokoko Smartsuit Pro II / Rokoko Smartsuit Pro II

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Rokoko](../companies/company_rokoko.md) |
| **제품 카테고리** | 관성 모션 캡처 슈트 |
| **출시일** | 2021년 10월 출시 |
| **상태** | 상용 |
| **공식 홈페이지/출처** | [Rokoko 공식 홈페이지](https://rokoko.com) |

## 제품 개요

Rokoko Smartsuit Pro II는 Rokoko가 출시한 2세대 전신 관성 모션 캡처 슈트로, 독립 크리에이터, 게임 스튜디오, 영화 제작, 스포츠 과학 및 로봇 연구 분야를 대상으로 합니다. 슈트는 Wi-Fi를 통해 무료 Rokoko Studio 소프트웨어와 연결되어 실시간으로 모션 데이터를 녹화, 정리, 편집하고 Unreal Engine, Unity, Blender, Maya, MotionBuilder 등 주요 3D 도구로 스트리밍할 수 있습니다.

1세대에 비해 Smartsuit Pro II는 드리프트 억제, 고충격 동작 안정성, 다층 추적(계단/사다리/수직 이동) 및 Smartgloves 손 추적과의 통합에서 크게 향상되었습니다. 17–19개의 9-DOF IMU 센서, 200fps 스트리밍 및 약 6시간의 배터리 수명으로 높은 가성비를 자랑하는 전문 모션 캡처 솔루션으로 자리 잡았습니다.

로봇 분야에서 Smartsuit Pro II는 인간의 자연스러운 움직임 데이터를 수집하여 휴머노이드 로봇, 디지털 휴먼 및 임베디드 지능형 모델에 동작 참조 및 훈련 데이터를 제공하는 데 사용됩니다.

## 제품 이미지

> Rokoko Smartsuit Pro II: [공식 자료](https://rokoko.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 센서 개수 | 17× 또는 19× 9-DOF IMU | Rokoko 공식 홈페이지 |
| 3D 방향 정밀도 | ±1° | Rokoko 공개 사양 |
| 샘플링/스트리밍 | 200fps | Rokoko 공개 사양 |
| 가속도계 범위 | 16g | Rokoko 공개 사양 |
| 무선 연결 | Wi-Fi (최대 약 100m) | Rokoko 공개 사양 |
| 배터리 수명 | 약 6시간 | Rokoko 공개 사양 |
| 슈트 사이즈 | S / M / L / XL | Rokoko 공식 홈페이지 |
| 원단 | 세탁 가능한 나일론/신축성 원단 | Rokoko 공개 사양 |
| 가격 | 약 2,745 USD부터 | 공개 견적 |

## 공급망 위치

- **제조사**: [Rokoko](../companies/company_rokoko.md)
- **핵심 부품/기술 출처**: MEMS IMU 센서, Wi-Fi 모듈, 웨어러블 텍스타일, 리튬 배터리, 센서 퓨전 알고리즘 칩, Rokoko Studio 소프트웨어.
- **하위 응용 분야/고객**: 독립 애니메이터, 게임 스튜디오(Ubisoft, EA 등), 영화 VFX, 스포츠 연구 기관, 로봇/휴머노이드 로봇 회사.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_rokoko_smartsuit_pro_ii`
- 제조사 엔터티: `ent_company_rokoko`
- 주요 관계:
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartsuit_pro_ii` (`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartsuit_pro_ii`)

## 응용 시나리오

- **영화 및 게임 애니메이션**: 실시간 캐릭터 구동, 고품질 애니메이션 신속 생성.
- **가상 방송 / VTubing**: 저지연 가상 캐릭터 구동.
- **스포츠 생체역학**: 선수의 동작, 자세 및 힘 전달 패턴 분석.
- **로봇 동작 참조**: 휴머노이드 로봇을 위한 자연스러운 움직임 데이터 수집, 모방 학습 및 동작 계획에 활용.

## 경쟁 비교

| 비교 항목 | Rokoko Smartsuit Pro II | Xsens MVN Link | Noitom Perception Neuron |
|-----------|------------------------|----------------|--------------------------|
| 포지셔닝 | 고성능 가성비 전문 관성 모션 캡처 | 고급 전문 관성 모션 캡처 | 입문형 관성 모션 캡처 |
| 센서 | 17–19× 9-DOF IMU | 17× 유선 IMU | 적은 IMU |
| 업데이트율 | 200fps | 최대 240Hz | 낮음 |
| 가격 | 약 2,745 USD부터 | 기업 문의 | 약 1,500 USD부터 |
| 소프트웨어 생태계 | Rokoko Studio (무료 기본 버전) | MVN Analyze/Animate | 자체 소프트웨어 |

## 구매 및 배포 제안

- 예산은 제한적이지만 전문가 수준의 전신 모션 캡처가 필요한 팀, 특히 독립 크리에이터와 중소 규모 스튜디오에 적합합니다.
- 고충격 동작이나 수직 이동 캡처가 필요한 경우, 다층 추적을 지원하는 최신 펌웨어인지 확인하는 것이 좋습니다.
- 로봇 데이터 수집에 사용할 경우, 추가로 골격 비율을 보정하고 BVH/FBX/CSV 등 범용 형식으로 내보내야 합니다.

## 참고 자료

1. [Rokoko 공식 홈페이지](https://rokoko.com)
2. [CGW – Rokoko Smartsuit Pro II 출시](https://www.cgw.com/Press-Center/News/2021/Rokoko-Launches-the-Next-Gen-Smartsuit-Pro-II.aspx)
3. [Animation Xpress – Rokoko Smartsuit Pro II](https://www.animationxpress.com/latest-news/motion-capture-company-rokoko-launches-smartsuit-pro-ii/)
4. [Rokoko Studio 다운로드 페이지](https://rokoko.com/studio)
