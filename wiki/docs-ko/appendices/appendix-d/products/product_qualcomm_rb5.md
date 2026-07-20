# 퀄컴 RB5 / 로봇 플랫폼

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목록](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [퀄컴 / Qualcomm](../companies/company_qualcomm.md) |
| **제품 카테고리** | 로봇 엣지 AI 개발 플랫폼 |
| **출시 시간** | 2020년 RB5 출시 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | 본문 참고 자료 참조 |

## 제품 개요

Qualcomm Robotics RB5 플랫폼은 QRB5165 SoC를 기반으로 하며, 5세대 AI 엔진, 7채널 동시 카메라 지원, 5G/Wi-Fi 6 연결 및 풍부한 센서 인터페이스를 통합하여 AMR, 배송 로봇, 드론 및 휴머노이드 로봇 프로토타입 개발에 흔히 사용되는 엣지 컴퓨팅 플랫폼입니다. 퀄컴 로봇 플랫폼은 이기종 컴퓨팅, 연결성 및 개발자 생태계를 강조합니다.

## 제품 이미지

> 퀄컴 RB5 / 로봇 플랫폼: [공식 자료](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| SoC | Qualcomm QRB5165 | 퀄컴 공식 홈페이지 |
| AI 연산 성능 | 5세대 AI 엔진, 15 TOPS | 퀄컴 공개 자료 |
| CPU | Kryo 585 옥타코어 (최대 2.84 GHz) | 퀄컴 공식 홈페이지 |
| GPU | Adreno 650 | 퀄컴 공식 홈페이지 |
| ISP | 7채널 카메라 동시 지원 | 퀄컴 공식 홈페이지 |
| 연결 | 5G, Wi-Fi 6, 블루투스 5.1, GPS | 퀄컴 공식 홈페이지 |
| 인터페이스 | USB 3.1, PCIe, MIPI CSI, GPIO | 개발 키트 자료 |
| 가격 | 개발 키트 약 449 USD (참고 가격) | 퀄컴/대리점 |

## 공급망 위치

- **제조사**: [퀄컴 / Qualcomm](../companies/company_qualcomm.md)
- **핵심 부품/기술 출처**: TSMC 위탁 생산, ARM IP, 메모리, RF 프론트엔드, 베이스밴드, 센서 생태계.
- **하위 응용/고객**: AMR 제조사, 드론 제조사, 서비스 로봇 제조사, 개발자 및 교육 기관.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_qualcomm_rb5`
- 제조사 엔터티: `ent_company_qualcomm`
- 주요 관계:
  - `rel_ent_company_qualcomm_manufactures_ent_product_qualcomm_rb5` (`ent_company_qualcomm` → `manufactures` → `ent_product_qualcomm_rb5`)
  - `ent_product_qualcomm_rb5` -- `uses` --> `ent_component_qrb5165_soc`
  - `ent_product_qualcomm_rb5` -- `supports` --> `ent_component_5g_module`

## 응용 시나리오

- **AMR**: 창고 물류 자율 이동 로봇의 인식 및 내비게이션.
- **배송 로봇**: 실외/실내 배송, 5G 및 AI 비전에 의존.
- **드론**: 항공 촬영, 검사, 물류 드론의 엣지 AI 및 연결.

## 경쟁 비교

| 비교 항목 | RB5 | NVIDIA Jetson AGX Orin | Horizon Robotics Journey 5 |
|--------|------|------|------|
| 연산 성능 | 15 TOPS | 275 TOPS | 128 TOPS |
| 연결 | 통합 5G/Wi-Fi 6 | 외부 모듈 필요 | 외부 모듈 필요 |
| 생태계 | ROS 2 + 모바일 생태계 | CUDA/Isaac 강력 | 자율주행 생태계 |

## 구매 및 배포 권장 사항

- 연산 성능/정밀도/시나리오 요구 사항에 따라 해당 모델을 선택하고, 공식 지원 툴체인 및 생태계 호환성을 우선 고려하십시오.
- 배포 전 전원 공급, 방열, 기계 인터페이스 및 통신 프로토콜이 전체 기기 요구 사항을 충족하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 퀄컴 / Qualcomm](../companies/company_qualcomm.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [퀄컴 / Qualcomm 공식 제품/회사 페이지](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
2. [Qualcomm Robotics RB5 페이지](https://www.qualcomm.com/products/internet-of-things/industrial/robotics/qualcomm-robotics-rb5-platform)
