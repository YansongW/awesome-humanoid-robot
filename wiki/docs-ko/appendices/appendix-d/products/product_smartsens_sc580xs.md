# 스마트센스 SC580XS CMOS 이미지 센서 / SmartSens SC580XS CMOS Image Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [스마트센스 / SmartSens](../companies/company_smartsens.md) |
| **제품 카테고리** | 50MP 플래그십 스마트폰/머신 비전 CMOS 이미지 센서 |
| **출시일** | 2024년 출시/양산 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [스마트센스 SC580XS CMOS 이미지 센서 제품/자료 페이지](https://www.smartsenstech.com/en/m) |

## 제품 개요

스마트센스 SC580XS는 플래그십 스마트폰 메인 카메라를 위한 5000만 화소 1/1.28인치 CMOS 이미지 센서로, 22nm HKMG Stack 공정과 SFCPixel®-2 기술을 채택했으며, PixGain HDR®, AllPix ADAF® 및 Sparse PDAF를 통합하여 높은 동적 범위, 저잡음 및 전 픽셀 초점 기능을 겸비했습니다.

## 제품 이미지

> 스마트센스 SC580XS CMOS 이미지 센서: [공식 자료](https://www.smartsenstech.com/en/m)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 유형 | 50MP CMOS 이미지 센서 | 스마트센스 공식 사이트 |
| 유효 화소 | 50 MP | 스마트센스 공식 사이트 |
| 픽셀 크기 | 1.22 µm | 스마트센스 공식 사이트 |
| 광학 크기 | 1/1.28" | 스마트센스 공식 사이트 |
| 공정 | 22 nm HKMG Stack | 스마트센스 공식 사이트 |
| HDR | PixGain HDR® / 삼중 노출 HDR | 스마트센스 공식 사이트 |
| 동적 범위 | 최대 120 dB | 스마트센스 공식 사이트 |
| 읽기 노이즈 | 최저 0.7 e⁻ | 스마트센스 공식 사이트 |
| 초점 | AllPix ADAF® / Sparse PDAF | 스마트센스 공식 사이트 |
| 비디오 | 4K 120fps (4-in-1 모드) | 스마트센스 공식 사이트 |
| 인터페이스 | MIPI C-PHY / D-PHY | 스마트센스 공식 사이트 |
| 전력 소비 | 50MP@25fps 약 500 mW | 스마트센스 공식 사이트 |
| 작동 온도 | -20℃ – +70℃ | 스마트센스 공식 사이트 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [스마트센스 / SmartSens](../companies/company_smartsens.md)
- **핵심 부품/기술 출처**: 웨이퍼 파운드리, 패키징 및 테스트, 광학 렌즈, 필터, ISP 알고리즘
- **하위 응용/고객**: 스마트폰 OEM, 보안 업체, 차량용 Tier1, 로봇, 산업용 카메라

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_smartsens_sc580xs`
- 부품 엔터티: `ent_component_smartsens_sc580xs_sensor`
- 제조사 엔터티: `ent_company_smartsens`
- 주요 관계:
  - `rel_ent_company_smartsens_manufactures_ent_product_smartsens_sc580xs` (`ent_company_smartsens` → `manufactures` → `ent_product_smartsens_sc580xs`)
  - `rel_ent_company_smartsens_manufactures_ent_component_smartsens_sc580xs_sensor` (`ent_company_smartsens` → `manufactures` → `ent_component_smartsens_sc580xs_sensor`)
  - `ent_product_smartsens_sc580xs` -- `uses` --> `ent_component_smartsens_sc580xs_sensor`

## 응용 시나리오

- **플래그십 스마트폰 메인 카메라, 초광각, 로봇 비전, 산업 검사, 드론 항공 촬영**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|-----------|---------|---------------|---------------|
| 유형 | 사양 매개변수 표 참조 | 동급 제품 | 동급 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 권장 사항

- 대상 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 성능 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: 스마트센스 / SmartSens](../companies/company_smartsens.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [스마트센스 공식 사이트](https://www.smartsenstech.com)
2. [스마트센스 SC580XS CMOS 이미지 센서 제품/자료 페이지](https://www.smartsenstech.com/en/m)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 디렉토리](../index-companies.md)
