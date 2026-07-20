# 오필름 3D ToF 깊이 카메라 모듈 / OFILM 3D ToF Depth Camera Module

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [오필름 / OFILM](../companies/company_ofilm.md) |
| **제품 카테고리** | 비행시간 3D 깊이 카메라 모듈 |
| **출시일** | 지속 판매/업데이트 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [오필름 3D ToF 깊이 카메라 모듈 제품/자료 페이지](http://www.ofilm.com/en/products_inner1_39.html) |

## 제품 개요

오필름 3D ToF 깊이 카메라 모듈은 비행시간(Time-of-Flight) 원리를 기반으로, 940 nm VCSEL을 통해 변조된 적외선을 방출하고 반사광을 수신하여 실시간으로 깊이 맵과 포인트 클라우드를 출력합니다. 모듈은 RGB 카메라를 통합하여 RGB-D 정렬을 구현할 수 있으며, 로봇 청소기 장애물 회피, 서비스 로봇 내비게이션, AR/VR 제스처 상호작용 및 얼굴 인식에 널리 사용됩니다.

## 제품 이미지

> 오필름 3D ToF 깊이 카메라 모듈: [공식 자료](http://www.ofilm.com/en/products_inner1_39.html)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 비행시간 3D 깊이 카메라 모듈 | 오필름 공식 홈페이지 |
| 깊이 해상도 | VGA / QVGA (모델에 따라 다름) | 오필름 공식 홈페이지 |
| RGB 해상도 | 2MP / 5MP 선택 가능 | 오필름 공식 홈페이지 |
| 광원 | 940 nm VCSEL | 오필름 공식 홈페이지 |
| 시야각 | 60°×45° / 70°×54° (일반) | 오필름 공식 홈페이지 |
| 측정 범위 | 0.3 – 5 m | 오필름 공식 홈페이지 |
| 정밀도 | 약 1% @ 1 m | 오필름 공식 홈페이지 |
| 프레임 속도 | 최대 30 fps | 오필름 공식 홈페이지 |
| 인터페이스 | MIPI / USB2.0 | 오필름 공식 홈페이지 |
| 전원 공급 | 3.3 V / 5 V DC | 오필름 공식 홈페이지 |
| 작동 온도 | -20℃ – +70℃ | 오필름 공식 홈페이지 |
| 무게 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [오필름 / OFILM](../companies/company_ofilm.md)
- **핵심 부품/기술 출처**: VCSEL, ToF 이미지 센서, DOE/광학 렌즈, ISP, PCB/FPC, 구조 부품
- **하위 응용 분야/고객**: 스마트폰, 스마트 로봇, AR/VR, 스마트 홈, 자동차 전자

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ofilm_tof_3d_module`
- 부품 엔터티: `ent_component_ofilm_tof_module_core`
- 제조사 엔터티: `ent_company_ofilm`
- 주요 관계:
  - `rel_ent_company_ofilm_manufactures_ent_product_ofilm_tof_3d_module` (`ent_company_ofilm` → `manufactures` → `ent_product_ofilm_tof_3d_module`)
  - `rel_ent_company_ofilm_manufactures_ent_component_ofilm_tof_module_core` (`ent_company_ofilm` → `manufactures` → `ent_component_ofilm_tof_module_core`)
  - `ent_product_ofilm_tof_3d_module` -- `uses` --> `ent_component_ofilm_tof_module_core`

## 응용 시나리오

- **로봇 청소기 장애물 회피, 서비스 로봇 내비게이션, AR/VR 제스처, 얼굴/생체 인식, 산업용 3D 검사**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 제안

- 목표 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: 오필름 / OFILM](../companies/company_ofilm.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [오필름 공식 홈페이지](http://www.ofilm.com)
2. [오필름 3D ToF 깊이 카메라 모듈 제품/자료 페이지](http://www.ofilm.com/en/products_inner1_39.html)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
