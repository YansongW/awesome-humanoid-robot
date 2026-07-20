# OptiTrack（자연점）

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | OptiTrack（자연점） |
| **영문명** | OptiTrack（NaturalPoint, Inc.） |
| **본사** | 미국 오리건주 코발리스 |
| **설립 시간** | 1996 |
| **공식 사이트** | [https://optitrack.com](https://optitrack.com) |
| **공급망 단계** | 광학 모션 캡처, 추적 카메라, 동작 측정 |
| **기업 속성** | 사기업（NaturalPoint 산하） |
| **모회사/소속 그룹** | NaturalPoint, Inc. |
| **데이터 출처** | OptiTrack 공식 사이트, 제품 페이지, 공개 보도 |

## 회사 소개

OptiTrack은 세계적으로 선도적인 광학 모션 캡처 시스템 공급업체로, 제품은 높은 정밀도, 낮은 지연 시간, 넓은 캡처 범위로 유명하며, 영화 애니메이션, 게임, 생체 역학, 스포츠 과학, 드론/로봇 위치 추적 및 휴머노이드 로봇 동작 검증에 널리 사용됩니다. OptiTrack의 카메라 어레이는 Motive 소프트웨어와 함께 작동하여 서브밀리미터 수준의 6DoF 자세 추적을 구현합니다.

OptiTrack은 PrimeX 시리즈 고해상도 적외선 카메라, Motive 추적 소프트웨어 및 능동/수동 마커 솔루션을 제공하며, 로봇 연구 개발에서 보행 분석, 전신 모션 캡처, 원격 조작 검증 및 알고리즘 보정에 사용되는 일반적인 도구입니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| PrimeX 카메라 시리즈 | 고성능 적외선 모션 캡처 카메라 | [OptiTrack 모션 캡처 시스템](../products/product_optitrack_motive_system.md) | 영화, 스포츠, 로봇 |
| Motive 소프트웨어 | 데이터 수집 및 실시간 해석 | Motive 3 | 모션 캡처, 분석 |
| 추적 액세서리 | 마커, 보정 도구, 동기화 장치 | Active/Passive Marker Sets | 연구 개발, 통합 |

## 대표 제품

### OptiTrack 모션 캡처 시스템

> OptiTrack 모션 캡처 시스템: [공식 자료](https://optitrack.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 시스템 유형 | 광학 적외선 모션 캡처 시스템 | OptiTrack 공식 사이트 |
| 대표 카메라 | PrimeX 13 / PrimeX 41 등 | 제품 페이지 |
| 추적 정밀도 | 서브밀리미터 수준（정확한 값 미공개） | 공개 자료 |
| 지연 시간 | 수 밀리초 수준 | 제품 페이지 |
| 해상도 | 최대 약 2048×2048（PrimeX 41） | 제품 페이지 |
| 프레임 속도 | 최대 240 fps 이상（모델에 따라 다름） | 제품 페이지 |
| 소프트웨어 | Motive 3（실시간 해석, 데이터 내보내기） | 공식 사이트 |
| 동기화 인터페이스 | eSync / Ethernet | 제품 페이지 |
| 가격 | 미공개 | 비즈니스 견적 |

**기술 하이라이트**: 고해상도 적외선 이미징, 서브밀리미터 정밀도, 낮은 지연 시간 실시간 해석, 대규모 다중 카메라 동기화, 풍부한 SDK 및 데이터 인터페이스.

**응용 시나리오**: 휴머노이드 로봇 보행 및 동작 보정, 원격 조작 훈련, 드론/AGV 위치 추적 검증, 영화 애니메이션, 스포츠 생체 역학, 재활 의학.

## 공급망 위치

- **상류 핵심 부품/재료**: 적외선 이미지 센서, 광학 렌즈, FPGA/처리 칩, 적외선 LED, 정밀 구조 부품, 보정 알고리즘, 네트워크 동기화 모듈
- **하류 고객/응용 시나리오**: 영화 제작사, 게임 개발사, 로봇/드론 연구 기관, 대학 연구실, 스포츠/의료 기관
- **주요 경쟁사/대상**: Vicon, Motion Analysis, Qualisys, Noitom（노이톰）, Xsens（관성）

## 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_optitrack`
- 제품 엔티티: `ent_product_optitrack_motive_system`
- 부품 엔티티: `ent_component_optitrack_motive_system_core`
- 주요 관계:
  - `ent_company_optitrack` -- `manufactures` --> `ent_product_optitrack_motive_system`
  - `ent_company_optitrack` -- `manufactures` --> `ent_component_optitrack_motive_system_core`
  - `ent_product_optitrack_motive_system` -- `uses` --> `ent_component_optitrack_motive_system_core`

## 참고 자료

1. [OptiTrack 공식 사이트](https://optitrack.com)
2. [OptiTrack 카메라 제품 페이지](https://optitrack.com/cameras/)
3. [부록 D 기업 디렉토리](../index-companies.md)
