# 보스턴 다이내믹스 / Boston Dynamics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 보스턴 다이내믹스 |
| **영문명** | Boston Dynamics |
| **본사** | 미국 매사추세츠주 월섬 |
| **설립일** | 1992 |
| **공식 사이트** | [https://bostondynamics.com](https://bostondynamics.com) |
| **공급망 단계** | 휴머노이드/족형 로봇 완성체 제조사, 산업 자동화 |
| **기업 속성** | 현대자동차그룹 자회사 |
| **모회사/소속 그룹** | Hyundai Motor Group (현대자동차그룹) |
| **데이터 출처** | Boston Dynamics 공식 사이트, 제품 사양 페이지, 공개 보도 |

## 회사 개요

보스턴 다이내믹스는 MIT 출신의 로봇 회사로, Atlas, Spot 등의 족형 로봇으로 유명하며, 2024년 전기식 Atlas를 출시하여 기업용 산업 휴머노이드 로봇으로 포지셔닝했습니다.

보스턴 다이내믹스는 오랫동안 족형 로봇 운동 제어 연구를 선도해 왔습니다. 신형 전기식 Atlas는 중량물 산업 운반 및 자동차 조립 현장을 대상으로 하며, 360° 인식, IP67 보호 등급 및 자동 배터리 교체를 강조합니다. Spot 사족 로봇은 이미 대규모 상업 배치를 실현했습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Atlas 휴머노이드 로봇 | 기업용 산업 휴머노이드 | Atlas (전기식) | 자동차 제조, 중량물 운반 |
| Spot 사족 로봇 | 이동형 순찰 플랫폼 | Spot | 산업 순찰, 측량, 보안 |
| Stretch 물류 로봇 | 창고 하역 | Stretch | 트럭/컨테이너 하역 |

## 대표 제품

### Boston Dynamics Atlas (전기식)

> Boston Dynamics Atlas (전기식): [공식 자료](https://bostondynamics.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 190 cm (높이) | Boston Dynamics 제품 페이지 |
| 무게 | 약 90 kg | Boston Dynamics 제품 페이지 |
| 자유도 | 56 | Boston Dynamics 제품 페이지 |
| 적재/토크 | 순간 50 kg / 지속 30 kg | Boston Dynamics 제품 페이지 |
| 속도/회전 속도 | 미공개 | - |
| 배터리 지속 시간 | 약 4시간; 자동 배터리 교체 지원 | Boston Dynamics 제품 페이지 |
| 인터페이스/통신 | Orbit 플랫폼, Wi-Fi, 기업 시스템 통합 | 공식 공개 |
| 가격 | 미공개 (기업 문의) | - |

**기술적 특징**: 전기식 액추에이터, 360° 시각 및 촉각 인식, 연속 관절 운동, IP67 보호 등급, 자동 배터리 교체 및 Orbit 차량 관리.

**적용 시나리오**: 현대자동차 등 제조 기업의 부품 분류, 중량물 운반, 옥외 및 열악 환경 작업.


### Boston Dynamics Spot

> Boston Dynamics Spot: [공식 자료](https://bostondynamics.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 83 cm (높이, 서 있을 때) | Boston Dynamics 제품 페이지 |
| 무게 | 약 32 kg | 공개 자료 |
| 자유도 | 미공개 | - |
| 적재/토크 | 약 14 kg | 공개 자료 |
| 속도/회전 속도 | 약 1.6 m/s | 공개 자료 |
| 배터리 지속 시간 | 약 90분 | 공개 자료 |
| 인터페이스/통신 | Spot SDK, Ethernet, Wi-Fi | 공식 공개 |
| 가격 | 약 74,500 USD부터 | 공개 견적 |

**기술적 특징**: 사족 기동성, 다중 센서 탑재, 자율 주행, 성숙한 상업 배치 및 개발자 생태계.

**적용 시나리오**: 산업 시설 순찰, 건축 측량, 공공 안전, 연구 및 교육.


## 공급망 위치

- **상류 핵심 부품/소재**: 현대 모비스 공급망, 모터/액추에이터, 고성능 센서, NVIDIA Jetson 등 컴퓨팅 모듈.
- **하류 고객/적용 시나리오**: 현대자동차그룹, 산업 기업, 에너지/건설 고객, 연구 기관.
- **주요 경쟁사/대상**: Tesla Optimus, Figure AI, Apptronik Apollo, Agility Robotics Digit.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_boston_dynamics`
- 제품/플랫폼 엔터티: `ent_product_boston_dynamics_atlas_electric`, `ent_product_boston_dynamics_spot`
- 주요 관계:
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_atlas_electric` (`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_atlas_electric`)
  - `rel_ent_company_boston_dynamics_manufactures_ent_product_boston_dynamics_spot` (`ent_company_boston_dynamics` → `manufactures` → `ent_product_boston_dynamics_spot`)

## 참고 자료

1. [Boston Dynamics 공식 사이트](https://bostondynamics.com)
2. [Boston Dynamics Atlas 제품 페이지](https://bostondynamics.com/products/atlas/)
3. [Boston Dynamics Spot 제품 페이지](https://bostondynamics.com/products/spot/)
