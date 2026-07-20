# SenseGlove（감융기술）

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | SenseGlove（감융기술） |
| **영문명** | SenseGlove B.V. |
| **본사** | 네덜란드 델프트 |
| **설립일** | 2017 |
| **공식 웹사이트** | [https://senseglove.com](https://senseglove.com) |
| **공급망 단계** | 힘 피드백 장갑, 촉각 피드백, 원격 조작 인간-기계 인터페이스 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | SenseGlove 공식 웹사이트, 제품 페이지, 공개 보도 |

## 회사 소개

SenseGlove는 힘 피드백 및 촉각 피드백 장갑에 특화된 네덜란드 스타트업으로, 제품은 주로 가상 현실 훈련, 원격 조작 로봇, 의료 재활 및 엔지니어링 시뮬레이션에 사용됩니다. Nova 시리즈 무선 장갑은 각 손가락에 능동 저항 피드백과 진동 촉각 피드백을 제공하여 사용자가 가상 또는 원격 환경에서 쥐는 힘, 형태 및 질감을 인지할 수 있도록 합니다.

SenseGlove의 힘 피드백 솔루션은 휴머노이드 로봇 원격 조작, 수술 로봇 훈련, 원자력 및 우주 원격 조작 등 다양한 분야에서 널리 사용되며, 훈련 비용을 크게 절감하고 조작 정밀도를 향상시킬 수 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| Nova 시리즈 | 무선 힘 피드백 장갑 | [SenseGlove Nova 2](../products/product_senseglove_nova_2.md) | 원격 조작, VR 훈련, 의료 재활 |
| DK1/Exoskeleton | 초기 외골격형 힘 피드백 장갑 | SenseGlove DK1 | 연구, 시뮬레이션 |
| 소프트웨어 SDK | 손 추적 및 힘 피드백 통합 | SenseGlove Unity/Unreal SDK | 개발자, 시스템 통합업체 |

## 대표 제품

### SenseGlove Nova 2

> SenseGlove Nova 2: [공식 자료](https://senseglove.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 무선 힘 피드백 장갑 | SenseGlove 공식 웹사이트 |
| 피드백 방식 | 4개 능동 저항 액추에이터 + 진동 촉각 피드백 | 제품 페이지 |
| 손가락 적용 범위 | 엄지, 검지, 중지, 약지 | 제품 페이지 |
| 추적 | SteamVR / Quest 트래커 호환 (추가 트래커 필요) | 제품 페이지 |
| 무선 연결 | 블루투스 / 2.4 GHz 전용 프로토콜 | 제품 페이지 |
| 배터리 지속 시간 | 약 2–3시간 | 제품 페이지/정확한 값 미공개 |
| 무게 | 약 320 g (단일, 정확한 값 미공개) | 공개 자료 |
| 소프트웨어 개발 | Unity, Unreal, C++ SDK | 공식 웹사이트 |
| 가격 | 미공개 | 비즈니스 견적 |

**기술적 특징**: 컴팩트한 무선 디자인, 4방향 능동 힘 피드백, 고충실도 진동 촉각, 플러그 앤 플레이 SDK로 휴머노이드 로봇 원격 조작 및 복잡한 훈련에 적합합니다.

**응용 시나리오**: 휴머노이드 로봇 원격 조작, 수술 로봇 훈련, VR 산업 유지보수 훈련, 원자력/우주 원격 조작, 재활 손 기능 평가.

## 공급망 위치

- **상류 핵심 부품/소재**: 마이크로 액추에이터/모터, 유연한 전동 메커니즘, 센서, 배터리, 블루투스 모듈, 장갑 소재, 트래커 호환 솔루션
- **하류 고객/응용 시나리오**: 로봇 원격 조작, 의료 훈련, VR 시뮬레이션, 자동차/항공 유지보수 훈련, 연구 기관
- **주요 경쟁사/대상**: HaptX, Manus VR, Meta Haptic Glove, StretchSense, CyberGlove

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_senseglove`
- 제품 엔터티: `ent_product_senseglove_nova_2`
- 부품 엔터티: `ent_component_senseglove_nova_2_core`
- 주요 관계:
  - `ent_company_senseglove` -- `manufactures` --> `ent_product_senseglove_nova_2`
  - `ent_company_senseglove` -- `manufactures` --> `ent_component_senseglove_nova_2_core`
  - `ent_product_senseglove_nova_2` -- `uses` --> `ent_component_senseglove_nova_2_core`

## 참고 자료

1. [SenseGlove 공식 웹사이트](https://senseglove.com)
2. [SenseGlove Nova 2 제품 페이지](https://senseglove.com/products/nova-2/)
3. [부록 D 기업 디렉토리](../index-companies.md)
