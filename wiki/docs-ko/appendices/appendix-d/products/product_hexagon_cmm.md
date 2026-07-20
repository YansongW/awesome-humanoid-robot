# 헥사곤 3차원 측정기

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [헥사곤 / Hexagon](../companies/company_hexagon.md) |
| **제품 카테고리** | 정밀 기하학 측정 장비 |
| **출시 시기** | 지속적 업데이트, GLOBAL 시리즈는 클래식 제품 라인 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | 본문 참고 자료 참조 |

## 제품 개요

헥사곤 3차원 측정기(CMM)는 산업 계측 분야의 핵심 장비로, 접촉식 프로브를 통해 3차원 공간에서 공작물의 기하학적 치수와 형상 공차를 획득합니다. GLOBAL 시리즈는 헥사곤의 클래식 브리지 타입 CMM으로, 높은 정밀도와 안정성, 풍부한 프로브/소프트웨어 생태계를 바탕으로 로봇 관절, 감속기, 커넥팅 로드 등 핵심 부품의 정밀 검사 및 품질 관리에 널리 사용됩니다.

## 제품 이미지

> 헥사곤 3차원 측정기: [공식 자료](https://hexagon.com/products/coordinate-measuring-machines)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 측정 범위 | 500×700×500 mm ~ 2000×4000×1500 mm | Hexagon 제품 매뉴얼 |
| 정밀도 | MPE_E 약 1.5 + L/350 µm (모델에 따라 다름) | Hexagon 제품 매뉴얼 |
| 프로브 시스템 | HP-S-X5 / HH-T / 트리거 프로브 | Hexagon 제품 매뉴얼 |
| 소프트웨어 | PC-DMIS / QUINDOS | Hexagon 공식 사이트 |
| 구조 | 화강암 작업대, 에어 베어링 가이드, 강철 브리지 | Hexagon 제품 매뉴얼 |
| 온도 보상 | 자동 온도 보상 | Hexagon 제품 매뉴얼 |
| 인터페이스 | USB / 이더넷 | Hexagon 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [헥사곤 / Hexagon](../companies/company_hexagon.md)
- **핵심 부품/기술 출처**: 고정밀 리니어 엔코더, 에어 베어링, 화강암, 프로브 센서, 산업용 소프트웨어.
- **하위 응용/고객**: 자동차 부품, 항공우주, 전자, 의료 기기, 로봇 부품 제조사.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_hexagon_cmm`
- 제조사 엔터티: `ent_company_hexagon`
- 주요 관계:
  - `rel_ent_company_hexagon_manufactures_ent_product_hexagon_cmm` (`ent_company_hexagon` → `manufactures` → `ent_product_hexagon_cmm`)
  - `ent_product_hexagon_cmm` -- `uses` --> `ent_component_linear_encoder`
  - `ent_product_hexagon_cmm` -- `measures` --> `ent_component_robot_gearbox`

## 응용 시나리오

- **로봇 관절 검사**: 관절 하우징, 출력 플랜지, 베어링 구멍의 기하학적 정밀도 측정.
- **감속기 검사**: 기어, 사이클로이드 휠, 핀 휠 하우징의 치형 및 위치도 측정.
- **전체 기계 교정**: 측정 암을 결합하여 로봇 링크 매개변수 및 DH 매개변수 교정.

## 경쟁 비교

| 비교 항목 | Hexagon GLOBAL | ZEISS PRISMO | Wenzel LH |
|--------|------|------|------|
| 정밀도 등급 | 마이크로미터급 | 서브 마이크로미터급 | 마이크로미터급 |
| 소프트웨어 | PC-DMIS | CALYPSO | WM | Quartis |
| 장점 | 생태계 및 안정성 | 최고 정밀도 | 가성비 |

## 구매 및 배포 권장 사항

- 컴퓨팅 성능/정밀도/시나리오 요구 사항에 따라 해당 모델을 선택하고, 공식 지원 툴체인 및 생태계 호환성을 우선 고려하세요.
- 배포 전 전원 공급, 방열, 기계 인터페이스 및 통신 프로토콜이 전체 기계 요구 사항을 충족하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 헥사곤 / Hexagon](../companies/company_hexagon.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [헥사곤 / Hexagon 공식 제품/회사 페이지](https://hexagon.com/products/coordinate-measuring-machines)
2. [Hexagon 공식 사이트](https://hexagon.com)
3. Hexagon GLOBAL 시리즈 기술 매뉴얼
