# ams OSRAM Mira220 근적외선 CMOS 이미지 센서 / ams OSRAM Mira220 NIR CMOS Image Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [ams OSRAM](../companies/company_ams_osram.md) |
| **제품 카테고리** | 근적외선 강화 글로벌 셔터 CMOS 이미지 센서 |
| **출시일** | 2022년부터 상용화 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [ams OSRAM Mira220 근적외선 CMOS 이미지 센서 제품/자료 페이지](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220) |

## 제품 개요

Mira220은 ams OSRAM이 3D 센싱 및 근적외선 이미징을 위해 설계한 2.2 MP 글로벌 셔터 CMOS 이미지 센서입니다. 850 nm 및 940 nm 근적외선 대역에서 높은 광양자 효율을 제공하며, 저전력, 고프레임률 작동을 지원하여 로봇 3D 비전, 구조광/ToF 카메라 및 차량 내 모니터링에 이상적인 감광 소자입니다.

## 제품 이미지

> ams OSRAM Mira220 근적외선 CMOS 이미지 센서: [공식 자료](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 근적외선 강화 글로벌 셔터 CMOS | 공식 홈페이지/datasheet |
| 유효 화소 | 2.2 MP | 공식 홈페이지/datasheet |
| 해상도 | 약 1920 × 1080 | 공식 홈페이지/datasheet |
| 광학 크기 | 1/2.7형 | 공식 홈페이지/datasheet |
| 화소 크기 | 2.79 µm | 공식 홈페이지/datasheet |
| 셔터 | 글로벌 셔터 | 공식 홈페이지/datasheet |
| NIR QE | 850/940 nm 대역 높은 광양자 효율 | 공식 홈페이지/datasheet |
| 최대 프레임률 | 최대 90 fps | 공식 홈페이지/datasheet |
| 인터페이스 | MIPI CSI-2 | 공식 홈페이지/datasheet |
| 소비 전력 | 미공개 | - |
| 전원 공급 | 미공개 | - |
| 작동 온도 | 미공개 | - |
| 패키지 | CSP | 공식 홈페이지/datasheet |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [ams OSRAM](../companies/company_ams_osram.md)
- **핵심 부품/기술 출처**: 자체 개발 NIR 강화 화소, 글로벌 셔터 판독 회로, MIPI 인터페이스, 웨이퍼 레벨 광학(WLO) 적용.
- **하위 응용/고객**: 3D 카메라 모듈 제조사, 로봇 OEM, AR/VR 기기 제조사, 보안 감시, 자동차 Tier 1.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ams_osram_mira220`
- 부품 엔터티: `ent_component_ams_osram_mira220_sensor`
- 제조사 엔터티: `ent_company_ams_osram`
- 주요 관계:
  - `rel_ent_company_ams_osram_manufactures_ent_product_ams_osram_mira220` (`ent_company_ams_osram` → `manufactures` → `ent_product_ams_osram_mira220`)
  - `rel_ent_company_ams_osram_manufactures_ent_component_ams_osram_mira220_sensor` (`ent_company_ams_osram` → `manufactures` → `ent_component_ams_osram_mira220_sensor`)
  - `rel_ent_product_ams_osram_mira220_uses_ent_component_ams_osram_mira220_sensor` (`ent_product_ams_osram_mira220` → `uses` → `ent_component_ams_osram_mira220_sensor`)

## 응용 시나리오

- **로봇 3D 비전**: 구조광/ToF 프로젝터와 함께 고품질 깊이 맵 획득.
- **얼굴 인식 및 제스처**: 높은 NIR QE로 어두운 조명 및 강한 조명에서 인식률 향상.
- **차량 내 모니터링**: 저전력으로 운전자/승객 상태 지속 모니터링.
- **AR/VR 추적**: 고속 글로벌 셔터로 모션 아티팩트 감소.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | NIR 글로벌 셔터 CMOS | Sony IMX426 | Himax 3D 센싱 |
| NIR 최적화 | 850/940 nm 높은 광양자 효율 | 일부 모델 지원 | 모듈 레벨 솔루션 |
| 셔터 | 글로벌 셔터 | 글로벌 셔터 | 구조광/ToF |
| 핵심 장점 | 발광+수광 광학 통합 | 고해상도 | WLO 소형화 |

## 구매 및 배포 권장 사항

- 대상 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: ams OSRAM](../companies/company_ams_osram.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [ams OSRAM 공식 홈페이지](https://ams-osram.com)
2. [ams OSRAM Mira220 근적외선 CMOS 이미지 센서 제품/자료 페이지](https://ams-osram.com/products/sensors/area-imaging-sensors/ams-mira220)
3. 제품 datasheet 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
