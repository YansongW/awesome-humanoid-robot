# 삼성전기 200MP ISOCELL 카메라 모듈 / Samsung Electro-Mechanics 200MP ISOCELL Camera Module

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [삼성전기 (Samsung Electro-Mechanics) / Samsung Electro-Mechanics](../companies/company_samsung_electro_mechanics.md) |
| **제품 카테고리** | 고화소 카메라 모듈 |
| **출시 시기** | 플래그십 모델 업데이트에 따라 출시 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [삼성전기 200MP ISOCELL 카메라 모듈 제품/자료 페이지](https://www.samsungsem.com/product/camera-module) |

## 제품 개요

해당 모듈은 삼성전기가 삼성 ISOCELL 200MP 이미지 센서를 기반으로 개발한 고화소 카메라 모듈로, 고정밀 광학 렌즈, VCM 자동 초점 및 OIS 광학 손떨림 보정 기구를 통합했습니다. 스마트폰 메인 카메라 외에도 높은 해상력과 소형화 설계로 로봇 비전, 드론 항공 촬영 및 차량용 서라운드 뷰 등 시나리오에 적합합니다.

## 제품 이미지

> 삼성전기 200MP ISOCELL 카메라 모듈: [공식 자료](https://www.samsungsem.com/product/camera-module)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 고화소 카메라 모듈 | 공식 홈페이지/보도자료 |
| 유효 화소 | 200 MP | 공식 홈페이지/보도자료 |
| 광학 크기 | 약 1/1.3"–1/1.4" | 공식 홈페이지/보도자료 |
| 픽셀 크기 | 약 0.56 µm | 공식 홈페이지/보도자료 |
| 렌즈 | 다매체 플라스틱/유리 하이브리드 렌즈 | 공식 홈페이지/보도자료 |
| 초점 | VCM 자동 초점 | 공식 홈페이지/보도자료 |
| 손떨림 보정 | 선택형 OIS | 공식 홈페이지/보도자료 |
| 화각 | 미공개 | - |
| 인터페이스 | MIPI D-PHY / C-PHY | 공식 홈페이지/보도자료 |
| 모듈 크기 | 미공개 | - |
| 소비 전력 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [삼성전기 (Samsung Electro-Mechanics) / Samsung Electro-Mechanics](../companies/company_samsung_electro_mechanics.md)
- **핵심 부품/기술 출처**: ISOCELL 200MP CMOS 이미지 센서, 하이브리드 광학 렌즈, VCM 모터, OIS 기구, FPC/커넥터, 패키징 구조 부품.
- **하위 응용/고객**: 스마트폰 OEM, 로봇 완제품 제조사, 드론 제조사, 자동차 Tier 1, 모듈 통합 업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_samsung_electro_mechanics_200mp_camera_module`
- 부품 엔터티: `ent_component_samsung_electro_mechanics_200mp_camera_module`
- 제조사 엔터티: `ent_company_samsung_electro_mechanics`
- 주요 관계:
  - `rel_ent_company_samsung_electro_mechanics_manufactures_ent_product_samsung_electro_mechanics_200mp_camera_module` (`ent_company_samsung_electro_mechanics` → `manufactures` → `ent_product_samsung_electro_mechanics_200mp_camera_module`)
  - `rel_ent_company_samsung_electro_mechanics_manufactures_ent_component_samsung_electro_mechanics_200mp_camera_module` (`ent_company_samsung_electro_mechanics` → `manufactures` → `ent_component_samsung_electro_mechanics_200mp_camera_module`)
  - `rel_ent_product_samsung_electro_mechanics_200mp_camera_module_uses_ent_component_samsung_electro_mechanics_200mp_camera_module` (`ent_product_samsung_electro_mechanics_200mp_camera_module` → `uses` → `ent_component_samsung_electro_mechanics_200mp_camera_module`)

## 응용 시나리오

- **스마트폰 메인 카메라**: 초고해상력 촬영 및 다배율 무손실 줌.
- **로봇 비전**: 이동 로봇/휴머노이드 로봇에 고해상도 시각 입력 제공.
- **차량용 서라운드 뷰**: 고화소 서라운드 뷰 및 블랙박스.
- **산업 검사**: 고정밀 표면 결함 검사 및 치수 측정.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 200MP 카메라 모듈 | 순우광학 차량용 모듈 | 추타이테크 머신 비전 모듈 |
| 센서 | Samsung ISOCELL 200MP | 다종 CIS | 다종 CIS |
| 픽셀 크기 | 약 0.56 µm | 모델에 따라 다름 | 모델에 따라 다름 |
| 핵심 장점 | 삼성 자체 센서+모듈 수직 통합 | 차량용 신뢰성 | 비용 및 신속 납기 |

## 구매 및 배치 권장 사항

- 대상 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배치 전 인터페이스, 전원 공급, 방열, 기계 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 삼성전기 (Samsung Electro-Mechanics) / Samsung Electro-Mechanics](../companies/company_samsung_electro_mechanics.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Samsung Electro-Mechanics 공식 홈페이지](https://www.samsungsem.com)
2. [삼성전기 200MP ISOCELL 카메라 모듈 제품/자료 페이지](https://www.samsungsem.com/product/camera-module)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
