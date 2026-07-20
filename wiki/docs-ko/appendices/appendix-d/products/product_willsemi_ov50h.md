# 윌 세미컨덕터 OmniVision OV50H 이미지 센서 / Will Semiconductor OmniVision OV50H Image Sensor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [윌 세미컨덕터 / Will Semiconductor](../companies/company_willsemi.md) |
| **제품 카테고리** | 50MP 고급 모바일 기기 CMOS 이미지 센서 |
| **출시일** | 2023년 출시/양산 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [윌 세미컨덕터 OmniVision OV50H 이미지 센서 제품/자료 페이지](https://www.ovt.com/products/ov50h/) |

## 제품 개요

OmniVision OV50H는 고급 스마트폰 후면 메인 카메라를 위한 5000만 화소 이미지 센서로, PureCel®Plus-S 스택 기술과 1.2 µm 픽셀을 채택했습니다. 이중 변환 이득(DCG™) HDR, 수평/수직 사방 위상 검출(H/V QPD) 자동 초점을 지원하며, 플래그십 수준의 저조도 및 초점 성능을 갖추고 있습니다.

## 제품 이미지

> 윌 세미컨덕터 OmniVision OV50H 이미지 센서: [공식 자료](https://www.ovt.com/products/ov50h/)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 유형 | 50MP CMOS 이미지 센서 | OmniVision 공식 홈페이지 |
| 유효 화소 | 50 MP (8192 × 6144) | OmniVision 공식 홈페이지 |
| 픽셀 크기 | 1.197 µm | OmniVision 공식 홈페이지 |
| 광학 크기 | 1/1.3" | OmniVision 공식 홈페이지 |
| 기술 | PureCel®Plus-S, DCG™ HDR, H/V QPD | OmniVision 공식 홈페이지 |
| 프레임 속도 | 50MP@30fps / 12.5MP@120fps | OmniVision 공식 홈페이지 |
| HDR | DCG / Staggered HDR | OmniVision 공식 홈페이지 |
| 초점 | H/V QPD PDAF, 100% 커버리지 | OmniVision 공식 홈페이지 |
| 출력 형식 | 10/12/14-bit RGB RAW | OmniVision 공식 홈페이지 |
| 인터페이스 | 4-lane MIPI / C-PHY | OmniVision 공식 홈페이지 |
| 전력 소비 | 활성 모드 약 1395 mW (50MP@30fps) | OmniVision 공식 홈페이지 |
| 작동 온도 | -30℃ – +85℃ | OmniVision 공식 홈페이지 |
| 패키징 | COB / RW | OmniVision 공식 홈페이지 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [윌 세미컨덕터 / Will Semiconductor](../companies/company_willsemi.md)
- **핵심 부품/기술 출처**: 웨이퍼 파운드리, 패키징 테스트, 광학 렌즈, 광학 필터, ISP 알고리즘
- **하위 응용/고객**: 스마트폰 OEM, 노트북 제조사, 차량용 Tier1, 로봇, 의료 기기

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_willsemi_ov50h`
- 부품 엔터티: `ent_component_willsemi_ov50h_sensor`
- 제조사 엔터티: `ent_company_willsemi`
- 주요 관계:
  - `rel_ent_company_willsemi_manufactures_ent_product_willsemi_ov50h` (`ent_company_willsemi` → `manufactures` → `ent_product_willsemi_ov50h`)
  - `rel_ent_company_willsemi_manufactures_ent_component_willsemi_ov50h_sensor` (`ent_company_willsemi` → `manufactures` → `ent_component_willsemi_ov50h_sensor`)
  - `ent_product_willsemi_ov50h` -- `uses` --> `ent_component_willsemi_ov50h_sensor`

## 응용 시나리오

- **고급 스마트폰 메인 카메라/광각, 노트북 카메라, 화상 회의, 로봇 비전, 차량용 인식**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|-----------|---------|---------------|---------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 권장 사항

- 대상 응용 분야의 해상도, 측정 범위, 정밀도 또는 연산 성능 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 장착 및 환경 온도 범위가 일치하는지 확인하십시오.
- 최신 펌웨어, SDK 및 기술 지원을 위해 공식 채널 또는 공인 대리점을 통해 문의하는 것을 권장합니다.

## 관련 항목

- [제조사: 윌 세미컨덕터 / Will Semiconductor](../companies/company_willsemi.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [윌 세미컨덕터 공식 홈페이지](https://www.willsemi.com)
2. [윌 세미컨덕터 OmniVision OV50H 이미지 센서 제품/자료 페이지](https://www.ovt.com/products/ov50h/)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
