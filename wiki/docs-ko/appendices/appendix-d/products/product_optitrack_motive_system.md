# OptiTrack 모션 캡처 시스템 / OptiTrack Motion Capture System

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [OptiTrack](../companies/company_optitrack.md) |
| **제품 카테고리** | 광학 모션 캡처 시스템 |
| **출시 시간** | PrimeX 시리즈 지속 판매 중; Motive 3 현행 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [OptiTrack 카메라 제품 페이지](https://optitrack.com/cameras/) |

## 제품 개요

OptiTrack 모션 캡처 시스템은 PrimeX 시리즈 적외선 카메라, Motive 추적 소프트웨어 및 능동/수동 마커로 구성되어 실내 환경에서 서브밀리미터급, 저지연 6DoF 자세 추적을 구현합니다. 이 시스템은 휴머노이드 로봇 모션 검증, 원격 조작 훈련, 보행 분석, 드론/AGV 위치 측정 및 교정, 영화 및 애니메이션 제작에 널리 사용됩니다.

## 제품 이미지

> OptiTrack 모션 캡처 시스템: [공식 자료](https://optitrack.com/cameras/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 시스템 구성 | PrimeX 카메라 + Motive 소프트웨어 + 마커 | 공식 홈페이지 |
| 대표 카메라 | PrimeX 13 (1.3 MP), PrimeX 41 (2048×2048) | 제품 페이지 |
| 추적 정밀도 | 서브밀리미터급 (정확한 값 미공개) | 공개 자료 |
| 지연 시간 | 수 밀리초 수준 | 제품 페이지 |
| 최대 프레임 속도 | PrimeX 13: 240 fps; PrimeX 41: 180 fps | 제품 페이지 |
| 시야각 | 미공개 | 제품 페이지 |
| 동기화 방식 | eSync / 이더넷 | 제품 페이지 |
| 소프트웨어 인터페이스 | Motive 3, C/C++ SDK, Python, ROS, VRPN | 공식 홈페이지 |
| 작업 거리 | 미공개 | 제품 페이지 |
| 가격 | 미공개 | 비즈니스 견적 |

## 공급망 위치

- **제조사**: [OptiTrack](../companies/company_optitrack.md)
- **핵심 부품/기술 출처**: 적외선 이미지 센서, 광학 렌즈, FPGA/처리 칩, 적외선 조명, 캘리브레이션 알고리즘, 네트워크 동기화 및 3D 해석 소프트웨어
- **하위 응용/고객**: 영화 및 애니메이션 회사, 로봇/드론 연구 개발 팀, 대학 및 연구 기관, 스포츠/재활 기관

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_optitrack_motive_system`
- 부품 엔터티: `ent_component_optitrack_motive_system_core`
- 제조사 엔터티: `ent_company_optitrack`
- 주요 관계:
  - `rel_ent_company_optitrack_manufactures_ent_product_optitrack_motive_system` (`ent_company_optitrack` → `manufactures` → `ent_product_optitrack_motive_system`)
  - `rel_ent_company_optitrack_manufactures_ent_component_optitrack_motive_system_core` (`ent_company_optitrack` → `manufactures` → `ent_component_optitrack_motive_system_core`)
  - `rel_ent_product_optitrack_motive_system_uses_ent_component_optitrack_motive_system_core` (`ent_product_optitrack_motive_system` → `uses` → `ent_component_optitrack_motive_system_core`)

## 응용 시나리오

- **휴머노이드 로봇 모션 교정**: 전신 관절 궤적을 포착하여 모션 계획 및 제어 알고리즘을 검증합니다.
- **원격 조작 훈련**: 작업자의 손/신체 동작을 기록하여 원격 조작 전략 훈련에 사용합니다.
- **드론/AGV 위치 측정 검증**: 고정밀 ground truth를 제공하여 SLAM 및 위치 측정 알고리즘을 평가합니다.
- **영화 애니메이션 및 게임**: 캐릭터 동작 캡처 및 실시간 가상 제작.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 광학 적외선 모션 캡처 | Vicon Vero/Vantage | Qualisys Miqus/Arqus |
| 정밀도 | 서브밀리미터급 | 서브밀리미터급 | 서브밀리미터급 |
| 지연 시간 | 저지연 | 저지연 | 저지연 |
| 가격 | 미공개 | 고가 | 고가 |

## 구매 및 배포 권장 사항

- 캡처 공간 크기 및 정밀도 요구 사항에 따라 카메라 수와 모델을 선택하십시오.
- 통제된 적외선 반사 조건을 갖춘 장소를 확보하여 햇빛과 강한 적외선 간섭을 피하십시오.
- 배포 전 시스템 캘리브레이션을 수행하고 SDK와 대상 소프트웨어 스택의 인터페이스 호환성을 확인하십시오.

## 관련 항목

- [제조사: OptiTrack](../companies/company_optitrack.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [OptiTrack 공식 홈페이지](https://optitrack.com)
2. [OptiTrack 카메라 제품 페이지](https://optitrack.com/cameras/)
3. Motive 소프트웨어 문서 및 공개 기술 자료
4. [부록 D 기업 목록](../index-companies.md)
