# 루링크 3D 인터랙티브 근전도 밴드 / Rulink 3D Interactive EMG Wristband

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [루링크 / Rulink](../companies/company_rulink.md) |
| **제품 카테고리** | 플렉서블 근전도/촉각 센서 밴드 |
| **출시 시간** | 2022년부터 지속적 업데이트 |
| **상태** | 상용 |
| **공식 홈페이지/출처** | [루링크 36Kr 프로젝트 페이지](https://pitchhub.36kr.com/project/1678511003644934) |

## 제품 개요

루링크 3D 인터랙티브 근전도 밴드는 플렉서블 전자 피부 기반의 표면 근전도(sEMG) 센서 장치입니다. 이 밴드는 나노 금속 입자 플렉서블 전극과 경량 설계를 채택하여 인체 팔뚝 피부에 밀착되며, 전완부 근전도 신호를 수집하고 AI 알고리즘을 통해 제스처와 운동 의도를 디코딩하여 가상 객체와의 컨트롤러 없는 상호작용을 실현합니다.

이 제품은 AR 안경과 함께 사용할 수 있어 사용자가 제스처를 통해 가상 객체를 잡기, 회전, 이동 또는 메뉴 선택 등의 작업을 수행할 수 있습니다. 플렉서블 센서 기술은 로봇 원격 조작 및 휴머노이드 로봇의 말단 힘/의도 인식에도 적용 가능하며, 전자 피부 및 신경 상호작용 분야의 대표적인 제품입니다.

## 제품 이미지

> Rulink EMG Wristband: [공식 자료](https://pitchhub.36kr.com/project/1678511003644934)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 센싱 유형 | 플렉서블 표면 근전도(sEMG) | 공개 보도 |
| 전극 재질 | 신형 나노 금속 입자 플렉서블 전극 | 공개 보도 |
| 인식 차원 | 근전도 신호, 제스처 운동 의도 | 공개 보도 |
| 채널 수 | 미공개 | - |
| 샘플링 속도 | 미공개 | - |
| 측정 범위 | 미공개 | - |
| 응답 시간 | 미공개 | - |
| 통신 인터페이스 | 미공개 | - |
| 전원 공급 방식 | 미공개 | - |
| 무게 | 미공개 | - |
| 배터리 지속 시간 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [루링크 / Rulink](../companies/company_rulink.md)
- **핵심 부품/기술 출처**: 자체 개발 나노 금속 입자 플렉서블 전극, AI 신호 분리 및 디코딩 알고리즘; 플렉서블 기재, 생체 전기 프론트엔드 칩 외부 구매.
- **하위 응용/고객**: AR/VR 기기, 로봇 원격 조작, 의수 제어, 스마트 웨어러블, 의료 재활.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_rulink_tactile_sensor`
- 제조사 엔터티: `ent_company_rulink`
- 부품 엔터티: `ent_component_rulink_flexible_electrode`
- 주요 관계:
  - `rel_ent_company_rulink_manufactures_ent_product_rulink_tactile_sensor` (`ent_company_rulink` → `manufactures` --> `ent_product_rulink_tactile_sensor`)
  - `rel_ent_company_rulink_manufactures_ent_component_rulink_flexible_electrode` (`ent_company_rulink` → `manufactures` --> `ent_component_rulink_flexible_electrode`)
  - `rel_ent_product_rulink_tactile_sensor_uses_ent_component_rulink_flexible_electrode` (`ent_product_rulink_tactile_sensor` → `uses` --> `ent_component_rulink_flexible_electrode`)

## 응용 시나리오

- **AR/VR 상호작용**: 컨트롤러 없는 제스처 인식 및 가상 객체 조작.
- **로봇 원격 조작**: 근전도 신호를 통해 로봇 팔 또는 정교한 손을 구동하여 모방 동작 수행.
- **의수 제어**: 절단 환자에게 자연스러운 제스처 의도 인식 제공.
- **휴머노이드 로봇 전자 피부**: 플렉서블 촉각/의도 인식 모듈로 로봇 사지에 통합.

## 경쟁 비교

| 비교 항목 | 루링크 근전도 밴드 | Meta 신경 밴드 | 나노스타 플렉서블 센서 |
|-----------|-------------------|----------------|------------------------|
| 센싱 원리 | 플렉서블 sEMG 전극 | 근전도 + 신경 신호 | 플렉서블 압저항/압전 |
| 형태 | 밴드/스트랩 | 밴드/시계 | 필름/패치 |
| 상호작용 능력 | 제스처 + 3D 가상 상호작용 | 제스처/입력 | 압력/변형 인식 |
| 핵심 장점 | 나노 플렉서블 전극, 경량 | 생태계 통합 | 다양한 플렉서블 센싱 |

## 구매 및 배치 제안

- 배치 전 전극과 피부의 밀착 안정성을 확인해야 하며, 고정 밴드 또는 탄성 직물을 함께 사용하는 것을 권장합니다.
- 근전도 신호는 개인 차이의 영향을 크게 받으므로 사용자별 소량의 캘리브레이션 또는 전이 학습이 필요합니다.

## 참고 자료

1. [36Kr PitchHub – 루링크 프로젝트 정보](https://pitchhub.36kr.com/project/1678511003644934)
2. [DH Capital – 루링크 인터뷰](https://www.dh-capital.cn/blog/7f0a7eeafb4)
3. [KEE Sleep – 루링크 창립자 인터뷰](https://www.keesleep.com/news/info/3305.html)
4. [부록 D 기업 목록](../index-companies.md)
