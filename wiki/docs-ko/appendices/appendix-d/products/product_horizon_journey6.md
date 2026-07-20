# Horizon Journey 6

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Horizon Robotics](../companies/company_horizon.md) |
| **제품 카테고리** | 스마트 드라이빙/임베디드 인텔리전스 컴퓨팅 SoC |
| **출시일** | 2024년 출시 |
| **상태** | 양산 도입 중 |
| **공식 사이트/출처** | 본문 참고 자료 참조 |

## 제품 개요

Horizon Journey 6 시리즈는 차세대 고급 스마트 드라이빙 및 임베디드 인텔리전스 시나리오를 위한 고성능 엣지 AI SoC입니다. 자체 개발한 BPU Nash 아키텍처를 채택한 Journey 6는 알고리즘과 칩의 협력 설계를 강조하며, 다중 고해상도 카메라, 라이다 및 밀리미터파 레이더 융합을 지원합니다. 고급 스마트 드라이빙과 휴머노이드 로봇/AMR에 인식 및 의사 결정 컴퓨팅 성능을 제공하는 것이 목표입니다.

## 제품 이미지

> Horizon Journey 6: [공식 자료](https://www.horizon.ai)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 컴퓨팅 성능 | Journey 6E 128 TOPS; Journey 6P 560 TOPS | Horizon 공개 자료 |
| BPU 아키텍처 | BPU Nash | Horizon 공개 자료 |
| CPU | 멀티코어 ARM Cortex-A78AE / 보안 코어 | 공개 보도 |
| ISP | 다중 고해상도 카메라 지원 | Horizon 공개 자료 |
| 기능 안전 | ASIL-D / ASIL-B 지원 | Horizon 공개 자료 |
| 인터페이스 | PCIe, Ethernet, MIPI CSI-2, CAN-FD | 제품 매뉴얼 |
| 전력 소비 | 미공개 | - |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [Horizon Robotics](../companies/company_horizon.md)
- **핵심 부품/기술 출처**: 웨이퍼 파운드리, ARM IP, 메모리, ISP IP, 차량용 인증, 센서 파트너.
- **하위 응용/고객**: 승용차 OEM, Tier 1, 로봇/AMR 솔루션 업체, 자율주행 기업.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_horizon_journey6`
- 제조사 엔터티: `ent_company_horizon`
- 주요 관계:
  - `rel_ent_company_horizon_manufactures_ent_product_horizon_journey6` (`ent_company_horizon` → `manufactures` → `ent_product_horizon_journey6`)
  - `ent_product_horizon_journey6` -- `uses` --> `ent_component_bpu_nash`
  - `ent_product_horizon_journey6` -- `processes` --> `ent_component_camera_sensor`

## 응용 시나리오

- **고급 스마트 드라이빙**: 고속도로 및 도시 NOA, 주행 및 주차 통합 지원.
- **임베디드 인텔리전스 인식**: 로봇에 시각/다중 센서 융합 인식 제공.
- **멀티모달 엣지 AI**: 저지연 시각 언어 이해 및 의사 결정.

## 경쟁 비교

| 비교 항목 | Journey 6 | NVIDIA Orin | Qualcomm Snapdragon Ride |
|--------|------|------|------|
| 컴퓨팅 성능 | 128–560 TOPS | 254 TOPS | 수십에서 수백 TOPS |
| 아키텍처 | BPU Nash | Ampere/Blackwell | Adreno/DSP |
| 장점 | 알고리즘 협력, 비용 최적화 | 생태계 성숙도 | 연결성 및 차량 내 통합 |

## 구매 및 배포 권장 사항

- 컴퓨팅 성능/정확도/시나리오 요구 사항에 따라 해당 모델을 선택하고, 공식 지원 도구 체인 및 생태계 호환성을 우선 고려하세요.
- 배포 전 전원 공급, 방열, 기계 인터페이스 및 통신 프로토콜이 전체 기기 요구 사항을 충족하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: Horizon Robotics](../companies/company_horizon.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Horizon Robotics 공식 제품/회사 페이지](https://www.horizon.ai)
2. [Horizon 공식 사이트](https://www.horizon.ai)
3. Horizon Journey 6 발표회 자료
