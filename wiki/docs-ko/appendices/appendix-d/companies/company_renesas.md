# 르네사스 일렉트로닉스 / Renesas Electronics

> 본 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 파라미터는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표기합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 르네사스 일렉트로닉스 |
| **영문명** | Renesas Electronics |
| **본사** | 일본 도쿄 |
| **설립 시기** | 2010년 (NEC 일렉트로닉스와 히타치/미쓰비시 반도체 사업부 합병) |
| **공식 사이트** | [https://www.renesas.com](https://www.renesas.com) |
| **공급망 단계** | MCU/MPU, 엣지 AI, 자동차 전자, 산업 제어, 로봇 비전 |
| **기업 속성** | 상장 기업 (TSE: 6723) |
| **모회사/소속 그룹** | 없음 (Renesas Electronics가 상장 주체) |
| **데이터 출처** | Renesas 공식 사이트, RZ/V 제품 매뉴얼, 공식 보도자료, 산업 보고서 |

## 회사 개요

Renesas Electronics(르네사스 일렉트로닉스)는 세계 최고의 MCU/MPU 및 아날로그 반도체 공급업체로, 제품은 자동차, 산업 및 인프라 분야에 널리 사용됩니다. RZ/V 시리즈 AI MPU는 자체 개발한 DRP-AI 가속기를 통합하여 매우 낮은 전력 소비로 높은 TOPS의 비전 추론을 구현합니다. RA/RX/RL 시리즈 MCU는 센서 노드부터 실시간 제어까지 광범위한 시나리오를 포괄합니다. 르네사스는 또한 로봇, 스마트 카메라 및 산업 비전의 신속한 구축을 지원하는 완벽한 AI 툴체인과 레퍼런스 디자인을 제공합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| RZ/V 시리즈 | 비전 AI MPU / DRP-AI 가속기 | RZ/V2H / RZ/V2N | 로봇, 스마트 카메라, 산업 비전, ADAS |
| RA / RX / RL MCU | 실시간 제어 및 보안 MCU | RA8 / RX700 | 모터 제어, 센서 노드, 기능 안전 |

## 대표 제품

### Renesas RZ/V2H

> Renesas RZ/V2H: [공식 자료](https://www.renesas.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 미공개 | Renesas 공개 자료 |
| CPU | 쿼드 코어 Arm Cortex-A55 @ 1.8 GHz + 듀얼 코어 Cortex-R8 @ 800 MHz + Cortex-M33 @ 200 MHz | Renesas 공개 자료 |
| AI 가속기 | DRP-AI3 (동적 재구성 가능 프로세서 + AI-MAC) | Renesas 공개 자료 |
| AI 연산 성능 | 8 TOPS (고밀도 모델) / 최대 80 TOPS (희소 모델) | Renesas 공개 자료 |
| ISP | 옵션 Arm Mali-C55 ISP | Renesas 공개 자료 |
| GPU | GE3D 3D GPU | Renesas 공개 자료 |
| 메모리 | LPDDR4 / LPDDR4X 인터페이스 | Renesas 공개 자료 |
| 인터페이스 | PCIe Gen3 x4, USB 3.2 Gen2 x2, GbE x2, MIPI CSI-2 x4, CAN-FD x6 | Renesas 공개 자료 |
| 전력 소비 | 미공개 (일반적으로 10 W 미만) | Renesas 공개 자료 |
| 패키지 | BGA 19 mm × 19 mm, 1368 핀 | Renesas 공개 자료 |
| 가격 | 미공개 | Renesas 공개 자료 |

**기술 하이라이트**: DRP-AI3 고연산 저전력, INT8 양자화 및 프루닝 지원, 4채널 MIPI CSI, PCIe/USB 3.2 고속 인터페이스, 팬 없이 고부하 AI 실행 가능.

**응용 시나리오**: **자율 이동 로봇**: 다중 채널 비전 인식, SLAM, 동적 장애물 회피 및 경로 계획; **스마트 산업용 카메라**: 고속 결함 검출, 객체 인식 및 측정, 외부 가속기 불필요; **비전 유도 로봇**: 실시간 자세 추정 및 그리핑 위치 결정, Transformer/CNN 혼합 네트워크 지원

### Renesas RZ/V2N

> Renesas RZ/V2N: [공식 자료](https://www.renesas.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| CPU | 쿼드 코어 Cortex-A55 + Cortex-M33 | Renesas 공개 자료 |
| AI 가속기 | DRP-AI3 | Renesas 공개 자료 |
| AI 연산 성능 | 최대 15 TOPS (희소) | Renesas 공개 자료 |
| 전력 소비 | 저전력 무팬 디자인 | Renesas 공개 자료 |
| 인터페이스 | MIPI CSI, PCIe, USB, GbE, CAN-FD | Renesas 공개 자료 |
| 패키지 | 15 mm × 15 mm | Renesas 공개 자료 |
| 가격 | 미공개 | Renesas 공개 자료 |

**기술 하이라이트**: 더 작은 패키지, 더 낮은 전력 소비, RZ/V2H의 DRP-AI3 아키텍처 계승, 대량 생산 비전 AI 기기에 적합.

**응용 시나리오**: 스마트 보안 카메라, 교통 모니터링, 산업 비전, 서비스 로봇.

## 공급망 위치

- **상류 핵심 부품/소재**: 르네사스 자체 개발 DRP-AI IP, ARM CPU/ISP IP, TSMC 위탁 생산, LPDDR4x, 패키징/테스트, PMIC
- **하류 고객/응용 시나리오**: 자동차 OEM/Tier1, 산업 자동화 업체, 로봇 회사, 스마트 카메라 및 보안 고객
- **주요 경쟁사/대상**: NXP i.MX, Texas Instruments Jacinto, NVIDIA Jetson, Horizon Robotics Journey, Ambarella

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_renesas`
- 제품 엔터티: `ent_product_renesas_rz_v2h`, `ent_product_renesas_rz_v2n`
- 부품 엔터티: `ent_component_renesas_rz_v2h_soc`, `ent_component_renesas_rz_v2n_soc`
- 주요 관계:
  - `ent_company_renesas` -- `manufactures` --> `ent_product_renesas_rz_v2h`
  - `ent_company_renesas` -- `manufactures` --> `ent_product_renesas_rz_v2n`
  - `ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2h_soc`
  - `ent_company_renesas` -- `manufactures` --> `ent_component_renesas_rz_v2n_soc`
  - `ent_product_renesas_rz_v2h` -- `uses` --> `ent_component_renesas_rz_v2h_soc`
  - `ent_product_renesas_rz_v2n` -- `uses` --> `ent_component_renesas_rz_v2n_soc`

## 참고 자료

1. [Renesas 공식 사이트](https://www.renesas.com)
2. [RZ/V2H 제품 페이지](https://www.renesas.com/en/products/rz-v2h)
3. [Renesas RZ/V 시리즈](https://www.renesas.com/en/products/microcontrollers-microprocessors/rz-mpus/rz-v-ai-accelerator)
