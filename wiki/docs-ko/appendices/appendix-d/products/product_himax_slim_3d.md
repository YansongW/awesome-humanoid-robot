# Himax SLiM 3D 센싱 모듈 / Himax SLiM 3D Sensing Module

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [기경전기(Himax Technologies) / Himax Technologies](../companies/company_himax.md) |
| **제품 카테고리** | 구조광 3D 센싱 모듈 |
| **출시일** | 2018년부터 상용화 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Himax SLiM 3D 센싱 모듈 제품/자료 페이지](https://www.himax.com.tw/products/structured-light-sensing/) |

## 제품 개요

SLiM(Structured Light Module)은 기경전기가 출시한 구조광 3D 센싱 종합 솔루션으로, 적외선 프로젝터, WLO 광학 부품 및 수신 센서를 통합하여 고정밀, 저전력의 3D 깊이 인식을 구현합니다. 소형화 설계 덕분에 스마트폰 얼굴 잠금 해제뿐만 아니라 로봇의 근거리 장애물 회피, 제스처 인식 및 물체 파지 유도에도 적합합니다.

## 제품 이미지

> Himax SLiM 3D 센싱 모듈: [공식 자료](https://www.himax.com.tw/products/structured-light-sensing/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 유형 | 구조광 3D 센싱 모듈 | 공식 사이트/보도자료 |
| 깊이 기술 | 구조광 / 능동 적외선 투사 | 공식 사이트/보도자료 |
| 깊이 해상도 | VGA급 (640 × 480) @ 30 fps | 공식 사이트/보도자료 |
| 시야각 | 수평 약 67° (일반) | 공식 사이트/보도자료 |
| 작동 거리 | 약 0.3 m – 1.0 m | 공식 사이트/보도자료 |
| 깊이 정밀도 | 미공개 | - |
| 크기 | 소형화 모듈 (구체적 미공개) | 공식 사이트/보도자료 |
| 전력 소비 | 미공개 | - |
| 인터페이스 | MIPI / USB2.0 (솔루션에 따라 다름) | 공식 사이트/보도자료 |
| 방출기 | VCSEL / EEL + WLO DOE | 공식 사이트/보도자료 |
| 수신기 | NIR 강화 CMOS / ToF | 공식 사이트/보도자료 |
| 작동 온도 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [기경전기(Himax Technologies) / Himax Technologies](../companies/company_himax.md)
- **핵심 부품/기술 출처**: 자체 개발 WLO 회절 광학 소자, 적외선 프로젝터, NIR CMOS 수신기, 깊이 알고리즘 ASIC, 모듈 패키징.
- **하위 응용/고객**: 스마트폰 OEM, 로봇 완제품 제조사, AR/VR 기기 업체, 스마트 도어락/출입 통제 업체, 결제 단말기 업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_himax_slim_3d`
- 부품 엔터티: `ent_component_himax_slim_3d_module`
- 제조사 엔터티: `ent_company_himax`
- 주요 관계:
  - `rel_ent_company_himax_manufactures_ent_product_himax_slim_3d` (`ent_company_himax` → `manufactures` → `ent_product_himax_slim_3d`)
  - `rel_ent_company_himax_manufactures_ent_component_himax_slim_3d_module` (`ent_company_himax` → `manufactures` → `ent_component_himax_slim_3d_module`)
  - `rel_ent_product_himax_slim_3d_uses_ent_component_himax_slim_3d_module` (`ent_product_himax_slim_3d` → `uses` → `ent_component_himax_slim_3d_module`)

## 응용 시나리오

- **로봇 장애물 회피 및 파지**: 근거리 고정밀 깊이 맵이 로봇 팔 경로 계획을 지원합니다.
- **얼굴 인식 및 결제**: 구조광 생체 감지로 보안 수준을 향상시킵니다.
- **AR/VR 제스처**: 저지연 손 추적 및 상호 작용.
- **3D 스캐닝**: 소형화 모듈을 휴대용 또는 고정식 3차원 재구성에 사용합니다.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|-----------|---------|---------------|---------------|
| 유형 | 구조광 3D 모듈 | 오비중광 Gemini 335 | Intel RealSense D435i |
| 깊이 기술 | 구조광 | 능동+수동 양안 | 능동 적외선 스테레오 |
| 최적 거리 | 0.3–1.0 m | 0.1–20 m+ | 0.3–10 m |
| 핵심 장점 | WLO 소형화, 결제급 보안 | 옥외 강광, MX6800 ASIC | 생태계 성숙, ROS 지원 |

## 구매 및 배포 권장 사항

- 대상 응용 프로그램의 해상도, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전에 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: 기경전기(Himax Technologies) / Himax Technologies](../companies/company_himax.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Himax Technologies 공식 사이트](https://www.himax.com.tw)
2. [Himax SLiM 3D 센싱 모듈 제품/자료 페이지](https://www.himax.com.tw/products/structured-light-sensing/)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
