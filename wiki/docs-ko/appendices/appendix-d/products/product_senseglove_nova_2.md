# SenseGlove Nova 2 햅틱 힘 피드백 장갑 / SenseGlove Nova 2 Haptic Force-Feedback Glove

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [SenseGlove](../companies/company_senseglove.md) |
| **제품 카테고리** | 무선 힘 피드백/햅틱 피드백 장갑 |
| **출시 시간** | Nova 시리즈 지속 판매 중, Nova 2는 차세대 모델 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [SenseGlove Nova 2 제품 페이지](https://senseglove.com/products/nova-2/) |

## 제품 개요

SenseGlove Nova 2는 가상 현실, 원격 조작 로봇 및 산업 훈련을 위한 무선 힘 피드백 장갑입니다. 손가락 주요 부위에 능동 저항 액추에이터와 진동 촉각 모듈을 구성하여 쥐기, 누르기, 마찰 등의 힘 감각을 시뮬레이션할 수 있으며, 주류 VR 헤드셋 및 트래킹 솔루션과 함께 몰입형 원격 제어 및 훈련 경험을 제공합니다. Nova 2는 휴머노이드 로봇 원격 조작, 수술 로봇 훈련, 항공 정비 시뮬레이션 등 다양한 분야에서 널리 사용됩니다.

## 제품 이미지

> SenseGlove Nova 2: [공식 자료](https://senseglove.com/products/nova-2/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 무선 힘 피드백 장갑 | 공식 홈페이지 |
| 피드백 액추에이터 | 4방향 능동 저항 (엄지, 검지, 중지, 약지) | 제품 페이지 |
| 촉각 피드백 | 진동 촉각 피드백 모듈 | 제품 페이지 |
| 손가락 트래킹 | 5손가락 트래킹 (외부 트래커 의존) | 제품 페이지 |
| 무선 연결 | 블루투스 / 2.4 GHz 전용 프로토콜 | 제품 페이지 |
| 호환 플랫폼 | Meta Quest 2/3/Pro, SteamVR, PC VR | 제품 페이지 |
| 배터리 지속 시간 | 약 2–3시간 | 제품 페이지 |
| 단일 무게 | 약 320 g (정확한 값 미공개) | 공개 자료 |
| 소프트웨어 개발 | Unity, Unreal Engine, C++ SDK | 공식 홈페이지 |
| 가격 | 미공개 | 비즈니스 견적 |

## 공급망 위치

- **제조사**: [SenseGlove](../companies/company_senseglove.md)
- **핵심 부품/기술 출처**: 마이크로 힘 피드백 액추에이터, 유연한 동력 전달, 관성/굽힘 센서, 블루투스 무선 모듈, 배터리, 장갑 직물, 트래커 어댑터
- **하류 응용/고객**: 로봇 원격 조작 개발사, 의료 수술 훈련, VR 훈련 통합업체, 자동차/항공 시뮬레이션, 연구 기관

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_senseglove_nova_2`
- 부품 엔터티: `ent_component_senseglove_nova_2_core`
- 제조사 엔터티: `ent_company_senseglove`
- 주요 관계:
  - `rel_ent_company_senseglove_manufactures_ent_product_senseglove_nova_2` (`ent_company_senseglove` → `manufactures` → `ent_product_senseglove_nova_2`)
  - `rel_ent_company_senseglove_manufactures_ent_component_senseglove_nova_2_core` (`ent_company_senseglove` → `manufactures` → `ent_component_senseglove_nova_2_core`)
  - `rel_ent_product_senseglove_nova_2_uses_ent_component_senseglove_nova_2_core` (`ent_product_senseglove_nova_2` → `uses` → `ent_component_senseglove_nova_2_core`)

## 응용 시나리오

- **휴머노이드 로봇 원격 조작**: 조작자가 장갑을 통해 원격으로 휴머노이드 로봇의 손가락 쥐기 및 조작을 제어합니다.
- **수술 로봇 훈련**: 조직 저항과 기구 촉감을 시뮬레이션하여 훈련의 현실감을 높입니다.
- **VR 산업 정비 훈련**: 가상 환경에서 볼트 조임, 부품 분해/조립 힘을 인지합니다.
- **재활 평가**: 손 움직임과 힘 피드백 데이터를 기록하여 손 기능 재활 훈련에 사용합니다.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 무선 힘 피드백 장갑 | HaptX Gloves G1 | Manus VR Haptic Glove |
| 피드백 | 능동 저항 + 진동 촉각 | 공압 고충실도 힘 피드백 | 진동 촉각 위주 |
| 무선 | 예 | 외부 공기 공급/케이블 필요 | 예 |
| 가격대 | 미공개 | 고급 | 중고급 |

## 구매 및 배포 권장 사항

- 대상 플랫폼 트래킹 솔루션(Quest / SteamVR / 광학 트래킹) 및 SDK 지원 여부를 확인하세요.
- 훈련 시나리오에 따라 단일 또는 한 쌍의 장갑을 선택하고, 힘 보정 및 콘텐츠 적응 시간을 확보하세요.
- 최신 펌웨어와 기술 지원을 받으려면 공식 또는 공인 대리점에서 구매하는 것을 권장합니다.

## 관련 항목

- [제조사: SenseGlove](../companies/company_senseglove.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [SenseGlove 공식 홈페이지](https://senseglove.com)
2. [SenseGlove Nova 2 제품 페이지](https://senseglove.com/products/nova-2/)
3. 공개 제품 리뷰 및 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
