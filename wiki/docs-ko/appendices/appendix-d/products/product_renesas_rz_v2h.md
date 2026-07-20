# Renesas RZ/V2H 비전 AI MPU

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [르네사스 일렉트로닉스 / Renesas Electronics](../companies/company_renesas.md) |
| **제품 카테고리** | DRP-AI3 통합 비전 AI MPU / 로봇 엣지 컴퓨팅 플랫폼 |
| **출시일** | 2024년 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Renesas RZ/V2H Product Page](https://www.renesas.com/en/products/rz-v2h) |

## 제품 개요

Renesas RZ/V2H는 고성능 비전 AI를 위한 MPU로, 르네사스 3세대 DRP-AI3 가속기를 통합하여 8 TOPS의 고밀도 연산 성능과 최대 80 TOPS의 희소 연산 성능을 제공합니다. 칩은 쿼드 코어 Cortex-A55, 듀얼 코어 실시간 Cortex-R8 및 Cortex-M33의 이기종 조합을 채택하며, 4채널 MIPI CSI, PCIe Gen3, USB 3.2 및 다중 CAN-FD를 지원하여 저전력, 고연산 성능이 필요한 자율 로봇, 산업용 비전 및 스마트 카메라 애플리케이션에 적합합니다.

## 제품 이미지

> Renesas RZ/V2H 비전 AI MPU: [공식 자료](https://www.renesas.com/en/products/rz-v2h)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 미공개 | Renesas 공개 자료 |
| CPU | 쿼드 코어 Arm Cortex-A55 @ 1.8 GHz + 듀얼 코어 Cortex-R8 @ 800 MHz + Cortex-M33 @ 200 MHz | Renesas 공개 자료 |
| AI 가속기 | DRP-AI3 (동적 재구성 프로세서 + AI-MAC) | Renesas 공개 자료 |
| AI 연산 성능 | 8 TOPS (고밀도 모델) / 최대 80 TOPS (희소 모델) | Renesas 공개 자료 |
| ISP | 옵션 Arm Mali-C55 ISP | Renesas 공개 자료 |
| GPU | GE3D 3D GPU | Renesas 공개 자료 |
| 메모리 | LPDDR4 / LPDDR4X 인터페이스 | Renesas 공개 자료 |
| 인터페이스 | PCIe Gen3 x4, USB 3.2 Gen2 x2, GbE x2, MIPI CSI-2 x4, CAN-FD x6 | Renesas 공개 자료 |
| 전력 소비 | 미공개 (일반적으로 10W 미만) | Renesas 공개 자료 |
| 패키지 | BGA 19 mm × 19 mm, 1368 핀 | Renesas 공개 자료 |
| 가격 | 미공개 | Renesas 공개 자료 |

## 공급망 위치

- **제조사**: [르네사스 일렉트로닉스 / Renesas Electronics](../companies/company_renesas.md)
- **핵심 부품/기술 출처**: 르네사스 자체 개발 DRP-AI3 IP, ARM CPU/ISP/GPU IP, LPDDR4x, 패키징 및 테스트, PMIC, 캐리어 보드
- **하위 응용/고객**: 로봇 완성체 제조사, 산업용 카메라 및 비전 솔루션 업체, AGV/AMR 제조사, 드론 제조사

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_renesas_rz_v2h`
- 부품 엔터티: `ent_component_renesas_rz_v2h_soc`
- 제조사 엔터티: `ent_company_renesas`
- 주요 관계:
  - `rel_ent_company_renesas_manufactures_ent_product_renesas_rz_v2h` (`ent_company_renesas` → `manufactures` --> `ent_product_renesas_rz_v2h`)
  - `rel_ent_company_renesas_manufactures_ent_component_renesas_rz_v2h_soc` (`ent_company_renesas` → `manufactures` --> `ent_component_renesas_rz_v2h_soc`)
  - `ent_product_renesas_rz_v2h` -- `uses` --> `ent_component_renesas_rz_v2h_soc`

## 응용 시나리오

- **자율 이동 로봇**: 다중 채널 시각 인식, SLAM, 동적 장애물 회피 및 경로 계획
- **스마트 산업용 카메라**: 고속 결함 검출, 객체 인식 및 측정, 외부 가속기 불필요
- **비전 유도 로봇**: 실시간 자세 추정 및 그리핑 위치 결정, Transformer/CNN 혼합 네트워크 지원

## 경쟁 비교

| 비교 항목 | RZ/V2H | NXP i.MX 8M Plus | TI TDA4VM |
|---|---|---|---|
| AI 연산 성능 (고밀도) | 8 TOPS | 2.3 TOPS | 8 TOPS |
| 희소 연산 성능 | 최대 80 TOPS | 미공개 | 미공개 |
| CPU | 쿼드 코어 A55 + 듀얼 코어 R8 | 쿼드 코어 A53 + M7 | 듀얼 코어 A72 + 6코어 R5F |

## 구매 및 배포 권장 사항

DRP-AI TVM / RUHMI 툴체인을 사용하여 양자화 모델 컴파일; DRP-AI가 대상 연산자를 지원하는지 확인; 카메라 수와 대역폭에 따라 RZ/V2H EVK 또는 맞춤형 캐리어 보드 선택.

## 관련 항목

- [제조사: 르네사스 일렉트로닉스 / Renesas Electronics](../companies/company_renesas.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Renesas RZ/V2H 제품 페이지](https://www.renesas.com/en/products/rz-v2h)
2. [Renesas RZ/V 시리즈](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rz-v-ai-accelerator)
3. [DRP-AI TVM GitHub](https://renesas-rz.github.io/rzv_drp-ai_tvm/)
