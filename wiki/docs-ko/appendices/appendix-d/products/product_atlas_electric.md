# Boston Dynamics Atlas (전기식)

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Boston Dynamics](../companies/company_boston_dynamics.md) |
| **제품 카테고리** | 산업용 휴머노이드 로봇 |
| **출시 시간** | 2024년 4월 전기식 버전 출시; 2026년 초기 양산 진입 |
| **상태** | 초기 양산/기업 내부 테스트 |
| **공식 사이트/출처** | [Boston Dynamics Atlas](https://bostondynamics.com/products/atlas/) |

## 제품 개요

Boston Dynamics는 2024년 4월 유압 구동 방식의 클래식 Atlas를 퇴역시키고, 완전 전기식 Atlas를 출시했습니다. 새로운 Atlas는 맞춤형 고출력 전기 구동 액추에이터를 채택했으며, 엉덩이 관절, 허리 및 목이 360° 연속 회전을 지원합니다. 전체 기계는 56개의 자유도를 가지며, 적재 용량과 운동 범위 모두 업계 선두 수준입니다.

전기식 Atlas는 중량물 운반, 장비 조작 및 자동차 제조 공정을 포함한 중부하 산업 작업에 특화되어 있습니다. 배터리는 자동 핫 스와핑을 지원하며, Boston Dynamics Orbit 함대 관리 플랫폼과 결합하여 거의 연속적인 작업이 가능합니다. 최초 배치는 현대자동차그룹(Hyundai) 제조 기지와 Google DeepMind 연구 현장에 집중될 것으로 예상됩니다.

## 제품 이미지

> Boston Dynamics Atlas Electric: [공식 자료](https://bostondynamics.com/products/atlas/)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 크기 | 약 190 cm (높이) | 공식 사양 페이지 |
| 무게 | 약 90 kg | 공식 사양 페이지 |
| 자유도 (전체 기계) | 56 DOF | 공식 사양 페이지 |
| 주요 성능 지표 | 순간 부하 50 kg; 지속 부하 30 kg; 최대 팔 길이 2.3 m | 공식 사양 페이지 |
| 보행 속도 | 약 9 km/h | 제3자 평가 |
| 배터리 지속 시간 | 약 4시간 (일반 작업 기준) | 공식 사양 페이지 |
| 보호 등급 | IP67 | 공식 사양 페이지 |
| 작동 온도 | -20°C ~ 40°C | 공식 사양 페이지 |
| 가격 | 미공개 (업계 추정 약 150,000 USD) | 제3자 추정 |

## 공급망 위치

- **제조사**: [Boston Dynamics](../companies/company_boston_dynamics.md)
- **핵심 부품/기술 출처**: 맞춤형 전기 구동 액추에이터, 다중 카메라 360° 비전, 자체 개발 실시간 제어 스택 및 Orbit 소프트웨어 플랫폼; 현대자동차그룹이 제조 및 공급망 지원 제공.
- **하류 응용/고객**: 현대자동차 제조, Google DeepMind 연구, 중부하 산업 현장.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_boston_dynamics_atlas_electric`
- 제조사 엔터티: `ent_company_boston_dynamics`
- 주요 관계:
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_atlas_electric` (`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_atlas_electric`)

## 응용 시나리오

- **자동차 제조**: 현대자동차그룹 공장에서의 중량물 운반, 부품 이동 및 복잡한 조립.
- **중부하 산업**: 30 kg 이상의 반복적인 운반, 장비 유지보수 및 위험 지역 작업을 사람 대신 수행.
- **연구 및 개발**: Google DeepMind 등 기관에서 로봇 학습 및 동적 운동 제어 알고리즘 검증에 사용.

## 경쟁 비교

| 비교 항목 | Boston Dynamics Atlas (전기식) | Tesla Optimus Gen 3 | Agility Digit |
|-----------|--------------------------------|---------------------|---------------|
| 포지셔닝 | 중부하 산업용 휴머노이드 | 범용/산업용 휴머노이드 | 물류 창고 휴머노이드 |
| 전체 기계 DOF | 56 | 28+ 몸통 + 22×2 손 | 16–28 |
| 부하 | 50 kg 순간 / 30 kg 지속 | 약 20 kg | 16 kg |
| 핵심 강점 | 운동 능력, 부하, 360° 관절 | 비용 목표, AI 데이터 폐쇄 루프 | 상업 배포 성숙도 |

## 구매 및 배포 권장 사항

- 현재 Atlas 전기식 버전은 주로 기업 파일럿 및 현대자동차그룹 생태계 고객을 대상으로 하며, Boston Dynamics 영업 채널을 통해 문의하는 것을 권장합니다.
- 배포 전에 현장 하중 용량, 인간-로봇 협업 안전 계획 및 MES/WMS와의 통합 요구 사항을 평가해야 합니다.

## 참고 자료

1. [Boston Dynamics Atlas 공식 제품 페이지](https://bostondynamics.com/products/atlas/)
2. [Boston Dynamics Blog – Electric Atlas Reveal](https://bostondynamics.com/)
3. [Robozaps – Boston Dynamics Atlas Review](https://blog.robozaps.com/b/boston-dynamics-atlas-review)
4. [Humanoid.Guide – Atlas](https://humanoid.guide/product/atlas/)
