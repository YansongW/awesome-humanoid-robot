# SRT SFG 유연 그리퍼 / SRT SFG Soft Gripper

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [소프트 로봇 테크놀로지 / SRT](../companies/company_srt.md) |
| **제품 카테고리** | 공압 유연 그리퍼 / 소프트 로봇 엔드 이펙터 |
| **출시 시간** | 2018년부터 지속적 업데이트 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [SRT 공식 홈페이지](https://www.softrobottech.com) |

## 제품 개요

SRT SFG 유연 그리퍼는 소프트 로봇 기술을 기반으로 한 적응형 공압 엔드 이펙터입니다. 기존의 강성 그리퍼와 달리, SFG의 핑거는 식품 등급 실리콘으로 제작되었으며 내부에 생체 모방 에어백 구조가 있습니다: 양압을 가하면 핑거가 구부러지며 대상 물체를 적응적으로 감싸고, 음압을 가하면 핑거가 펴지면서 물체를 놓습니다. 부드럽고 변형 가능한 특성 덕분에 SFG는 동일한 그리퍼 세트로 다양한 크기, 형상, 경도 및 표면 특성을 가진 물체를 파지할 수 있으며, 특히 기존 그리퍼로 처리하기 어려운 유연, 이형 및 파손 위험이 있는 물품에 적합합니다.

SFG 시리즈는 컴팩트형(FTN), 대칭 조절형(FMA), 원주형(FNC) 등 다양한 구조 형태로 발전했으며, 고객 요구에 따라 핑거 모듈과 장착 브래킷을 맞춤 제작할 수 있으며 UR, ABB, 신송 등 주요 로봇과 호환됩니다.

## 제품 이미지

> SRT SFG 그리퍼: [공식 자료](https://www.softrobottech.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 구동 방식 | 공압(양압 파지 / 음압 해제) | 제품 매뉴얼 |
| 핑거 재질 | 식품 등급 실리콘 | 제품 매뉴얼 |
| 핑거 구조 | 생체 모방 에어백/소프트 구조 | 제품 매뉴얼 |
| 작동 온도 | -40 ℃ – 150 ℃ | 제품 매뉴얼 |
| 작동 압력 | -100 – 100 kPa | 제품 매뉴얼 |
| 사용 수명 | >300만 회 사이클 | 제품 매뉴얼 |
| 반복 위치 정밀도 | 0.08 mm | 제품 매뉴얼 |
| 작동 주파수 | ≤110 CPM | 제품 매뉴얼 |
| 부하 범위 | 100 g – 7 kg(모델에 따라 다름) | DirectIndustry |
| 그리퍼 무게 | 38 g – 1090 g(모델에 따라 다름) | DirectIndustry |
| 적용 가능한 공작물 크기 | 모델에 따라 변화, 다양한 SKU 커버 가능 | 제품 매뉴얼 |
| 구동 매체 | 청정 공기 | 제품 매뉴얼 |
| 장착 인터페이스 | ISO 9409-1:2004 / GB/T 14468.1 호환 | 제품 매뉴얼 |
| 전용 컨트롤러 | SCB 시리즈 공압 컨트롤러 | 제품 매뉴얼 |
| 인증 | CE, RoHS, FDA, LFGB, JFSL370 등 | 공식 홈페이지 공개 자료 |
| 통신 인터페이스 | 공압 컨트롤러 + 로봇 I/O | 제품 매뉴얼 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [소프트 로봇 테크놀로지 / SRT](../companies/company_srt.md)
- **핵심 부품/기술 출처**: 자체 개발 실리콘 재료 배합, 소프트 구조 설계 및 성형 공정; 공압 부품, 컨트롤러, 3D 비전 모듈은 외부 구매.
- **하류 응용/고객**: 식품 신선, 3C 전자, 자동차 부품, 의료 일용, 물류 창고, 협동 로봇 통합업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_srt_soft_gripper`
- 제조사 엔터티: `ent_company_srt`
- 부품 엔터티: `ent_component_srt_flexible_finger`
- 주요 관계:
  - `rel_ent_company_srt_manufactures_ent_product_srt_soft_gripper`(`ent_company_srt` → `manufactures` --> `ent_product_srt_soft_gripper`)
  - `rel_ent_company_srt_manufactures_ent_component_srt_flexible_finger`(`ent_company_srt` → `manufactures` --> `ent_component_srt_flexible_finger`)
  - `rel_ent_product_srt_soft_gripper_uses_ent_component_srt_flexible_finger`(`ent_product_srt_soft_gripper` → `uses` --> `ent_component_srt_flexible_finger`)

## 응용 시나리오

- **식품 신선**: 육류, 과일·채소, 베이커리, 해산물, 조리 식품의 선별 및 포장.
- **3C 전자**: 휴대폰 프레임, 회로 기판, 이형 전자 부품의 무손상 상하차.
- **자동차 부품**: 고무 부품, 와이어 하네스, 이형 사출 부품 조립.
- **의료 일용**: 앰플, 주사기, 의료 기기, 화장품 포장.
- **물류 창고**: 이형, 부드럽고, 깨지기 쉬운 물품의 혼합 SKU 선별.

## 경쟁 비교

| 비교 항목 | SRT SFG | OnRobot Soft Gripper | Soft Robotics Inc. mGrip |
|--------|---------|----------------------|--------------------------|
| 구동 방식 | 공압 | 전동/공압 | 공압 |
| 핑거 재질 | 식품 등급 실리콘 | 유연 재료 | 유연 재료 |
| 작동 온도 | -40 ℃ – 150 ℃ | 모델에 따라 다름 | 모델에 따라 다름 |
| 사용 수명 | >300만 회 | 모델에 따라 다름 | 모델에 따라 다름 |
| 핵심 장점 | 식품 등급 인증, 다양한 시리즈, 글로벌 고객 다수 | 플러그 앤 플레이 생태계 | 모듈화, 통합 용이 |

## 구매 및 배치 제안

- 공작물 무게, 크기, 형상에 따라 FTN/FMA/FNC 등 해당 시리즈와 핑거 모듈을 선택하세요.
- 청정 공기 공급원과 SRT 공압 컨트롤러를 함께 사용하여 압력과 택트 타임이 일치하도록 해야 합니다.
- 식품 직접 접촉 시나리오의 경우 SFG-N 식품 등급 인증 모델을 선택하는 것이 좋습니다.

## 참고 자료

1. [SRT 소프트 로봇 공식 홈페이지](https://www.softrobottech.com)
2. [SRT Shopify 국제 사이트](https://softrobotgripper.com)
3. [Asian Robotics Review – SRT 보도](https://asianroboticsreview.com/home620-html)
4. [DirectIndustry – SFG 시리즈 제품 매개변수](https://www.directindustry.com/prod/soft-robot-tech-co-ltd/product-244815-2538729.html)
5. [부록 D 기업 목록](../index-companies.md)
