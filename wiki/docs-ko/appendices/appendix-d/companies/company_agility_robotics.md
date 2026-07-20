# Agility Robotics / Agility Robotics

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Agility Robotics |
| **영문명** | Agility Robotics |
| **본사** | 미국 오리건주 세일럼 (RoboFab 소재지) |
| **설립일** | 2015 |
| **공식 사이트** | [https://agilityrobotics.com](https://agilityrobotics.com) |
| **공급망 단계** | 물류 휴머노이드 로봇 완제품 제조사, RaaS |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Agility Robotics 공식 사이트, Digit 제품 페이지, 공개 배치 관련 보도 |

## 회사 소개

Agility Robotics는 휴머노이드 로봇의 상업적 배치를 선도하는 기업으로, Digit은 Amazon, GXO 등의 창고에서 실제 물품 운반 작업을 수행하고 있습니다.

Digit은 물류 환경에 특화되어 설계되었으며, 역방향 무릎 관절을 채택하여 보행 및 운반 효율성을 최적화했습니다. Agility Arc 클라우드 플랫폼을 통해 원격 모니터링 및 차량 관리를 지원합니다. 회사는 세일럼에 RoboFab 휴머노이드 로봇 제조 공장을 보유하고 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Digit 휴머노이드 로봇 | 물류 창고 휴머노이드 | Digit 현재 세대 / 차세대 | 창고 분류, 운반, 트럭 적재/하역 |
| Agility Arc | 클라우드 로봇 관리 플랫폼 | Agility Arc | 차량 모니터링, 작업 스케줄링, 데이터 분석 |

## 대표 제품

### Agility Robotics Digit (현재 세대)

> Agility Robotics Digit (현재 세대): [공식 자료](https://agilityrobotics.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 175 cm (높이) | 공개 자료 |
| 무게 | 약 63–65 kg | 공개 자료 |
| 자유도 | 전신 28; 팔/손은 물류 맞춤형 그리퍼 | 공개 자료 |
| 적재/토크 | 약 16 kg | 공개 자료 |
| 속도/회전수 | 약 5.4 km/h | 공개 자료 |
| 배터리 지속 시간 | 약 4시간 (작업 관련) | 공개 자료 |
| 인터페이스/통신 | LiDAR, Intel RealSense 깊이 카메라, IMU, Agility Arc | 공식 공개 |
| 가격 | RaaS 임대 / 약 250,000 USD부터 | 타사 견적 |

**기술적 특징**: 역방향 무릎 관절로 보행 최적화, tote/상자 운반에 특화 설계, LiDAR + 깊이 카메라 360° 인식, Amazon/GXO 창고에 배치 완료.

**적용 시나리오**: 창고 물품 운반, 트럭 적재/하역, 반복적인 물류 작업.


### Agility Robotics Digit (차세대)

> Agility Robotics Digit (차세대): [공식 자료](https://agilityrobotics.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 크기 | 약 175 cm (높이) | 공개 보도 |
| 무게 | 약 63.5 kg | 공개 보도 |
| 자유도 | 30+ | 공개 보도 |
| 적재/토크 | 약 22.6 kg (50 lbs) | 공개 보도 |
| 속도/회전수 | 미공개 | - |
| 배터리 지속 시간 | 개선 중 (구체적 수치 미공개) | - |
| 인터페이스/통신 | Agility Arc | - |
| 가격 | 미공개 | - |

**기술적 특징**: 기존 Digit 기반으로 적재 용량과 상체 유연성을 향상, 물류 대규모 배치 지속 목표.

**적용 시나리오**: 고하중 창고 운반, 더 복잡한 물류 작업.


## 공급망 위치

- **상류 핵심 부품/소재**: Intel RealSense 깊이 카메라, 모터/구동계, 구조 부품, 배터리 및 컴퓨팅 모듈.
- **하류 고객/적용 시나리오**: Amazon, GXO Logistics, Mercado Libre 등 물류 및 소매 기업.
- **주요 경쟁사/대상**: Tesla Optimus, Apptronik Apollo, Boston Dynamics Stretch.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_agility_robotics`
- 제품/플랫폼 엔터티: `ent_product_agility_robotics_digit`, `ent_product_agility_robotics_digit_next_gen`
- 주요 관계:
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit` (`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit`)
  - `rel_ent_company_agility_robotics_manufactures_ent_product_agility_robotics_digit_next_gen` (`ent_company_agility_robotics` → `manufactures` → `ent_product_agility_robotics_digit_next_gen`)

## 참고 자료

1. [Agility Robotics 공식 사이트](https://agilityrobotics.com)
2. [RoboZaps Agility Digit 리뷰](https://blog.robozaps.com/b/agility-robotics-digit-review)
3. [Humanoid.guide Digit 사양](https://humanoid.guide/product/digit/)
