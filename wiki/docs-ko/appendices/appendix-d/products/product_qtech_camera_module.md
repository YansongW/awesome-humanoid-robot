# 丘钛科技 머신비전/차량용 카메라 모듈 / Q-Tech Machine Vision / Automotive Camera Module

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [丘钛科技 / Q-Tech](../companies/company_qtech.md) |
| **제품 카테고리** | 머신비전/차량용 카메라 모듈 |
| **출시일** | 지속 판매/반복 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [丘钛科技 머신비전/차량용 카메라 모듈 제품/자료 페이지](https://www.qtechsmartvision.com/) |

## 제품 개요

丘钛科技 머신비전/차량용 카메라 모듈은 스마트 자동차 ADAS, 드론 항공 촬영, 서비스 로봇 내비게이션 및 산업 검사 등 시나리오를 대상으로 하며, COB/COF 고신뢰성 패키징을 채택하고, 글로벌 셔터 또는 롤링 셔터 CMOS를 선택할 수 있으며, MIPI 또는 GMSL2 고속 인터페이스를 지원하고, 넓은 온도 범위와 IP67 방호 성능을 갖추고 있습니다.

## 제품 이미지

> 丘钛科技 머신비전/차량용 카메라 모듈: [공식 자료](https://www.qtechsmartvision.com/)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 유형 | 머신비전/차량용 카메라 모듈 | 丘钛科技 공식 홈페이지 |
| 해상도 | 2MP / 5MP / 8MP 다중 모델 | 丘钛科技 공식 홈페이지 |
| 센서 | 1/2.8" – 1/2.3" CMOS | 丘钛科技 공식 홈페이지 |
| 셔터 | 글로벌 셔터 / 롤링 셔터 (선택 가능) | 丘钛科技 공식 홈페이지 |
| 화각 | 120° / 140° / 맞춤형 | 丘钛科技 공식 홈페이지 |
| 인터페이스 | MIPI / GMSL2 | 丘钛科技 공식 홈페이지 |
| 방호 등급 | IP67 (차량용 모델) | 丘钛科技 공식 홈페이지 |
| 작동 온도 | -40℃ – +85℃ | 丘钛科技 공식 홈페이지 |
| 전원 공급 | 12 V DC (일반) | 丘钛科技 공식 홈페이지 |
| 무게 | 약 30 – 80 g | 丘钛科技 공식 홈페이지 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [丘钛科技 / Q-Tech](../companies/company_qtech.md)
- **핵심 부품/기술 출처**: CMOS 이미지 센서, 렌즈, VCM, FPC, 구동 IC, 구조 부품
- **하류 응용/고객**: 스마트폰 OEM, 자동차 OEM/Tier1, 드론, 로봇, IoT 업체

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_qtech_machine_vision_camera_module`
- 부품 엔터티: `ent_component_qtech_camera_module_core`
- 제조사 엔터티: `ent_company_qtech`
- 주요 관계:
  - `rel_ent_company_qtech_manufactures_ent_product_qtech_machine_vision_camera_module` (`ent_company_qtech` → `manufactures` → `ent_product_qtech_machine_vision_camera_module`)
  - `rel_ent_company_qtech_manufactures_ent_component_qtech_camera_module_core` (`ent_company_qtech` → `manufactures` → `ent_component_qtech_camera_module_core`)
  - `ent_product_qtech_machine_vision_camera_module` -- `uses` --> `ent_component_qtech_camera_module_core`

## 응용 시나리오

- **산업용 로봇 비전 검사, 드론 항공 촬영, 스마트 자동차 서라운드/전방 시야, 서비스 로봇 SLAM**

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

- [제조사: 丘钛科技 / Q-Tech](../companies/company_qtech.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [丘钛科技 공식 홈페이지](https://www.qtechsmartvision.com)
2. [丘钛科技 머신비전/차량용 카메라 모듈 제품/자료 페이지](https://www.qtechsmartvision.com/)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
