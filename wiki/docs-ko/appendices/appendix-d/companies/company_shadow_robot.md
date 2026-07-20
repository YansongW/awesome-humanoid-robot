# Shadow Robot Company / Shadow Robot Company

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 '미공개'로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Shadow Robot Company |
| **영문명** | Shadow Robot Company |
| **본사** | 영국 런던 |
| **설립 연도** | 1987 |
| **공식 웹사이트** | [https://www.shadowrobot.com](https://www.shadowrobot.com) |
| **공급망 단계** | 인간형 로봇 손 / 로봇 말단 장치 / 연구 플랫폼 |
| **기업 속성** | 글로벌 선도 인간형 로봇 손 기업, 연구용 제품 |
| **모회사/소속 그룹** | Shadow Robot Company Ltd. |
| **데이터 출처** | 공식 웹사이트, 제품 매뉴얼, 공개 보도, WAIC 2026 보도 |

## 회사 소개

세계에서 가장 진보된 인간형 로봇 손 개발사 중 하나로, 연구 및 고급 응용 분야에 특화되어 있습니다.

Shadow Robot Company는 1987년에 설립되었으며, 본사는 영국 런던에 있습니다. 오랫동안 고도로 인간을 닮은 로봇 손 개발에 집중해 왔습니다. Shadow Dexterous Hand는 인간 손과 유사한 크기와 운동학을 가지고 있으며, 로봇 파지 연구, 원격 조작, 의료 수술, 원자력 산업 및 인간형 로봇 분야에서 널리 사용됩니다. ROS/EtherCAT 생태계에서 가장 대표적인 연구용 로봇 손 중 하나입니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| Shadow Dexterous Hand | 고자유도 연구용 | 다섯 손가락 로봇 손 | 연구, 의료 |
| Shadow Hand Lite | 경량화 저비용 | 네 손가락 로봇 손 | 교육, 상업 |
| Teleoperation Systems | 원격 조작 | Shadow Glove | 원격 제어, 원자력 산업 |

## 대표 제품

### Shadow Dexterous Hand / Shadow Dexterous Hand

> Shadow Dexterous Hand: [공식 자료](https://www.shadowrobot.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 크기 | 성인 남성 손 크기와 유사 | 공식 사양서 |
| 무게 | 4.3 kg (전완 포함) | 공식 사양서 |
| 자유도 | 20 능동 + 4 수동 / 24 관절 | 공식 사양서 |
| 하중 | 강력 파지 4–5 kg | 공식 사양서 / 공개 보도 |
| 운동 속도 | 일반 관절 1.0 Hz | 공식 사양서 |
| 통신 인터페이스 | EtherCAT | 공식 사양서 |
| 제어 주파수 | 위치 루프 1 kHz / 토크 루프 5 kHz | 공식 사양서 |
| 공급 전압 | 미공개 | - |
| 가격 | 미공개 | - |

**기술적 특징**: 고도로 생체 모방된 운동학, 손끝/손바닥 촉각 센서, ROS 완전 통합, 위치/힘/토크 다중 모드 제어로 바늘 꿰기, 집기 등 정밀 동작 수행 가능.

**응용 시나리오**: 대학 및 연구 기관의 파지 연구, 의료 수술 훈련, 원자력 산업 원격 조작, 인간형 로봇 고급 검증.

### Shadow Hand Lite / Shadow Hand Lite

> Shadow Hand Lite: [공식 자료](https://www.shadowrobot.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 크기 | 미공개 | - |
| 무게 | 미공개 | - |
| 자유도 | 미공개 | - |
| 하중 | 미공개 | - |
| 손끝 힘 | 미공개 | - |
| 통신 인터페이스 | EtherCAT | 제품 매뉴얼 |
| 공급 전압 | 미공개 | - |
| 가격 | 미공개 | - |

**기술적 특징**: Shadow Hand의 정밀 조작 능력을 유지하면서 구조를 간소화하여 더 넓은 교육 및 상업 응용 분야를 대상으로 함.

**응용 시나리오**: 교육 시연, 상업 전시, 경량 연구, 서비스 로봇.

## 공급망 위치

- **상류 핵심 부품/재료**: 마이크로 모터, 텐던, 힘/촉각 센서, 알루미늄 합금/엔지니어링 플라스틱, EtherCAT 제어 보드
- **하류 고객/응용 시나리오**: 대학 및 연구 기관, 의료 수술, 원자력 산업, 원격 조작, 인간형 로봇
- **주요 경쟁사/대상**: SCHUNK, qb Soft Robotics, Agile Robots, 인시 로봇

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_shadow_robot`
- 제품/부품 엔터티: `ent_product_shadow_dexterous_hand`
- 주요 관계:
  - `ent_company_shadow_robot` -- `manufactures` --> `ent_product_shadow_dexterous_hand`

## 참고 자료

1. [공식 웹사이트](https://www.shadowrobot.com)
2. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
3. [공개 제품 매뉴얼 및 연구 보고서](https://www.shadowrobot.com) (실제 제품 모델에 따라 확인 필요)
