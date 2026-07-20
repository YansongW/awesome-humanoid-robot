# XELA Robotics uSkin 고밀도 3축 촉각 센서 / XELA Robotics uSkin High-Density 3-Axis Tactile Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [XELA Robotics](../companies/company_xela.md) |
| **제품 카테고리** | 고밀도 3축 유연 촉각 센서 / 전자 피부 |
| **출시일** | 2018년부터 지속적 업데이트 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [XELA Robotics 공식 홈페이지](https://www.xelarobotics.com) |

## 제품 개요

XELA Robotics uSkin은 로봇 그리퍼와 다관절 손을 위한 고밀도 3축 유연 촉각 센서입니다. uSkin은 자기저항식 감지 원리를 사용하며, 각 감지 유닛(taxel)은 X, Y, Z 3축 힘을 독립적으로 측정할 수 있습니다. 분해능은 0.1 gf, 샘플링 주파수는 500 Hz이며, 디지털 출력 방식을 통해 배선을 최소 4개 선으로 단순화했습니다.

uSkin의 부드러운 탄성체 외피는 복잡한 곡면에 밀착되고 과부하를 완충하며 파지 대상물을 보호할 수 있어, Robotiq, Weiss Robotics, Wonik Robotics, Tesollo DG-5F 등 주요 그리퍼 및 다관절 손에 널리 사용됩니다. 2026년 XELA는 표준 감지점 크기를 4 mm × 4 mm에서 2.5 mm × 2.5 mm로 축소하여 공간 분해능을 더욱 향상시킬 계획입니다.

## 제품 이미지

> XELA uSkin: [공식 자료](https://www.xelarobotics.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 감지 원리 | 자기저항식 3축 힘 감지 | 공식 홈페이지 공개 자료 |
| 감지 차원 | X, Y, Z 3축 힘 | 공식 홈페이지 공개 자료 |
| 표준 감지점 크기 | 4 mm × 4 mm | 공식 홈페이지/공개 보도 |
| 차세대 감지점 크기 | 2.5 mm × 2.5 mm (2026년 Q2) | Engineering.com |
| 단일 taxel 법선 힘 범위 | 최대 1500 gf (약 14.7 N) | XELA Catalog 2025 |
| 분해능 | 0.1 gf (약 1 mN) | 공식 홈페이지 공개 자료 |
| 샘플링 주파수 | 500 Hz | 공식 홈페이지 공개 자료 |
| 출력 방식 | 디지털 출력 | 공식 홈페이지 공개 자료 |
| 배선 요구 사항 | 전체 센서 읽기에 최소 4선 | 제품 매뉴얼 |
| 패키징 재질 | 부드러운 탄성체 | 공식 홈페이지 공개 자료 |
| 표준 모델 | uSPa 11/21/22/44/46, uSCu, uSPr 시리즈 | 공식 홈페이지 공개 자료 |
| 통신 인터페이스 | 디지털 버스 (구체적 프로토콜 미공개) | 제품 매뉴얼 |
| 공급 전압 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 보호 등급 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [XELA Robotics](../companies/company_xela.md)
- **핵심 부품/기술 출처**: 자체 개발 자기저항식 3축 감지 칩, 탄성체 외피 및 uAi 소프트웨어 플랫폼; 마이크로컨트롤러, 유연 기재는 외부 조달.
- **하위 응용/고객**: 휴머노이드 로봇 다관절 손, 산업용 그리퍼, 물류 창고, 농업 수확, 연구 기관, 의료용 의수.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_xela_uskin`
- 제조사 엔터티: `ent_company_xela`
- 부품 엔터티: `ent_component_xela_uskin_module`
- 주요 관계:
  - `rel_ent_company_xela_manufactures_ent_product_xela_uskin` (`ent_company_xela` → `manufactures` --> `ent_product_xela_uskin`)
  - `rel_ent_company_xela_manufactures_ent_component_xela_uskin_module` (`ent_company_xela` → `manufactures` --> `ent_component_xela_uskin_module`)
  - `rel_ent_product_xela_uskin_uses_ent_component_xela_uskin_module` (`ent_product_xela_uskin` → `uses` --> `ent_component_xela_uskin_module`)

## 응용 시나리오

- **휴머노이드 로봇 다관절 손**: 손끝, 손가락 배, 손바닥의 전면 촉각 커버.
- **산업용 그리퍼 힘 제어**: Robotiq, Weiss Robotics 등 그리퍼에 직접 통합하여 힘/미끄러짐 피드백 구현.
- **물류 분류**: 이형, 깨지기 쉬운, 부드러운 물체의 안전한 파지.
- **농업 수확**: 과일, 채소 등 취약 대상의 적응형 수확.
- **의료용 의수**: 의수에 인간 피부에 가까운 힘 감지 제공.

## 경쟁 비교

| 비교 항목 | XELA uSkin | SynTouch BioTac | 파시니 PX-6AX |
|-----------|------------|-----------------|---------------|
| 감지 원리 | 자기저항식 3축 | 유체/전극/열전도 | 6D 홀 어레이 |
| 감지 차원 | 3축 힘 | 힘+진동+온도 | 15가지 촉각 정보 |
| 감지점 밀도 | 4 mm (표준) / 2.5 mm (계획) | 단일점 생체모방 | 어레이식 |
| 핵심 장점 | 부드러움, 쉬운 통합, 디지털 출력 | 생체모방, 견고함 | 고밀도, 다관절 손 풀스택 |

## 구매 및 배치 권장 사항

- 그리퍼 또는 다관절 손의 기하학적 치수에 따라 uSPa(평면), uSCu(곡면) 또는 uSPr(그리퍼 보호) 시리즈를 선택하세요.
- 센서는 자기장에 민감하므로 배치 시 강한 자기장 및 강자성 재료를 피해야 하며, 필요한 경우 기준 센서를 사용하여 보정하세요.
- 디지털 출력은 하드웨어 통합을 단순화하지만, 로봇 컨트롤러 측에 해당 드라이버 또는 SDK를 미리 준비해야 합니다.

## 참고 자료

1. [XELA Robotics 공식 홈페이지](https://www.xelarobotics.com)
2. [XELA Robotics 제품 카탈로그 2025](https://49063741.fs1.hubspotusercontent-na2.net/hubfs/49063741/XELA%20Robotics%20-%20Catalog%202025.pdf)
3. [Engineering.com – uSkin integrated into Tesollo DG-5F](https://www.engineering.com/uskin-tactile-sensors-integrated-into-tesollo-dg-5f-robot-hand/)
4. [XELA Robotics 기술 페이지](https://xelarobotics.com/technology/)
5. [부록 D 기업 목록](../index-companies.md)
