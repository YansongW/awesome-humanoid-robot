# OmniVision OX08D10 자동차/로봇 8MP 이미지 센서 / OmniVision OX08D10 8MP Image Sensor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [옴니비전 테크놀로지(OmniVision) / OmniVision](../companies/company_omnivision.md) |
| **제품 카테고리** | 차량용 8MP CMOS 이미지 센서 |
| **출시일** | 2022년부터 상용화 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [OmniVision OX08D10 자동차/로봇 8MP 이미지 센서 제품/자료 페이지](https://www.ovt.com/products/ox08d10) |

## 제품 개요

OX08D10은 OmniVision이 전방 ADAS 및 고급 로봇 비전을 위해 설계한 8MP 차량용 CMOS 이미지 센서입니다. 1/1.7인치 광학 포맷과 2.1 µm 픽셀을 채택하며, 120 dB HDR, LED 플리커 억제(LFM) 및 ASIL-B 기능 안전을 지원하여 휴머노이드 로봇 헤드 메인 카메라, 무인 차량 및 산업 검사 카메라에 적합합니다.

## 제품 이미지

> OmniVision OX08D10 자동차/로봇 8MP 이미지 센서: [공식 자료](https://www.ovt.com/products/ox08d10)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 유형 | 차량용 8MP CMOS 이미지 센서 | 공식 홈페이지/datasheet |
| 유효 픽셀 | 8 MP | 공식 홈페이지/datasheet |
| 광학 크기 | 1/1.7" | 공식 홈페이지/datasheet |
| 픽셀 크기 | 2.1 µm | 공식 홈페이지/datasheet |
| 셔터 | 롤링 셔터(HDR 포함) | 공식 홈페이지/datasheet |
| 최대 프레임 속도 | 최대 60 fps | 공식 홈페이지/datasheet |
| 동적 범위 | 120 dB HDR | 공식 홈페이지/datasheet |
| LED 플리커 억제 | LFM 지원 | 공식 홈페이지/datasheet |
| 기능 안전 | ASIL-B | 공식 홈페이지/datasheet |
| 인터페이스 | MIPI D-PHY / C-PHY | 공식 홈페이지/datasheet |
| 출력 포맷 | RAW / YUV | 공식 홈페이지/datasheet |
| 작동 온도 | -40℃ – +105℃(차량용) | 공식 홈페이지/datasheet |
| 패키지 | COB / CSP | 공식 홈페이지/datasheet |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [옴니비전 테크놀로지(OmniVision) / OmniVision](../companies/company_omnivision.md)
- **핵심 부품/기술 출처**: 자체 개발 BSI 픽셀, HDR/LFM 판독 회로, ISP 알고리즘, 차량용 패키지 및 테스트.
- **하위 응용/고객**: 자동차 Tier 1, 로봇 OEM, 무인 차량 회사, 산업용 카메라 제조사, 보안 감시 브랜드.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_omnivision_ox08d10`
- 부품 엔터티: `ent_component_omnivision_ox08d10_sensor`
- 제조사 엔터티: `ent_company_omnivision`
- 주요 관계:
  - `rel_ent_company_omnivision_manufactures_ent_product_omnivision_ox08d10`(`ent_company_omnivision` → `manufactures` → `ent_product_omnivision_ox08d10`)
  - `rel_ent_company_omnivision_manufactures_ent_component_omnivision_ox08d10_sensor`(`ent_company_omnivision` → `manufactures` → `ent_component_omnivision_ox08d10_sensor`)
  - `rel_ent_product_omnivision_ox08d10_uses_ent_component_omnivision_ox08d10_sensor`(`ent_product_omnivision_ox08d10` → `uses` → `ent_component_omnivision_ox08d10_sensor`)

## 응용 시나리오

- **휴머노이드 로봇 헤드 메인 카메라**: 8MP 고해상도로 원거리 목표 인식 및 SLAM 지원.
- **무인 차량/AMR 내비게이션**: 복잡한 조명 및 신호등 환경에서 HDR과 LFM으로 안정적인 이미징.
- **ADAS 전방 시야**: 차선 유지, AEB, 교통 표지판 인식.
- **산업 검사**: 높은 동적 범위와 큰 픽셀로 저조도 검사 성능 향상.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|-----------|---------|---------------|---------------|
| 유형 | 차량용 8MP CIS | Sony IMX490 | Samsung ISOCELL 자동차 CIS |
| 해상도 | 8 MP | 5 MP | 모델에 따라 다름 |
| HDR | 120 dB | 130 dB | 모델에 따라 다름 |
| 핵심 장점 | ASIL-B / LFM | 높은 동적 범위 | 삼성 생태계 통합 |

## 구매 및 배치 권장 사항

- 대상 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배치 전 인터페이스, 전원 공급, 방열, 기계 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 옴니비전 테크놀로지(OmniVision) / OmniVision](../companies/company_omnivision.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [OmniVision 공식 홈페이지](https://www.ovt.com)
2. [OmniVision OX08D10 자동차/로봇 8MP 이미지 센서 제품/자료 페이지](https://www.ovt.com/products/ox08d10)
3. 제품 datasheet 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
