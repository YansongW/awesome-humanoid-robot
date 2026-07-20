# 엔씨프 / NXP Semiconductors

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 엔씨프 |
| **영문명** | NXP Semiconductors |
| **본사** | 네덜란드 에인트호번 |
| **설립 시기** | 2006년 (Philips 반도체 부문 분사) |
| **공식 웹사이트** | [https://www.nxp.com](https://www.nxp.com) |
| **공급망 단계** | MCU/MPU, 엣지 AI, 산업 제어, 자동차 전자, 로봇 메인 컨트롤러 |
| **기업 속성** | 상장사 (NASDAQ: NXPI) |
| **모회사/소속 그룹** | 없음 (NXP Semiconductors는 상장 주체) |
| **데이터 출처** | NXP 공식 웹사이트, i.MX 제품 매뉴얼, 공개 보도자료, 업계 보고서 |

## 회사 소개

NXP Semiconductors(엔씨프)는 세계적인 임베디드 반도체 공급업체로, MCU, MPU, 보안 식별, 자동차 전자 및 아날로그 소자를 포괄합니다. i.MX 시리즈 애플리케이션 프로세서는 산업, 자동차 및 IoT 엣지 컴퓨팅을 대상으로 하며, i.MX 8M Plus 등의 모델은 NPU를 통합하여 로봇, 산업용 비전 및 AIoT에 로컬 AI 추론 기능을 제공하면서 높은 신뢰성과 긴 공급 주기를 갖추고 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| i.MX 8 시리즈 | 고성능 멀티미디어 및 AI 애플리케이션 프로세서 | i.MX 8M Plus | 산업용 HMI, 로봇 메인 컨트롤러, 엣지 AI, 스마트 게이트웨이 |
| i.MX 9 / i.MX 93 시리즈 | NPU 통합 차세대 엣지 AI 프로세서 | i.MX 93 | AIoT, 산업 자동화, 스마트 홈, 로봇 |

## 대표 제품

### NXP i.MX 8M Plus

> NXP i.MX 8M Plus: [공식 자료](https://www.nxp.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 14 nm FinFET | NXP 공개 자료 |
| CPU | 쿼드 코어 Arm Cortex-A53 @ 최대 1.8 GHz + Cortex-M7 @ 800 MHz | NXP 공개 자료 |
| NPU | 통합 Neural Processing Unit | NXP 공개 자료 |
| AI 연산 성능 | 최대 2.3 TOPS INT8 | NXP 공개 자료 |
| ISP | 듀얼 ISP, 12MP, HDR, 어안 보정 지원 | NXP 공개 자료 |
| GPU | Vivante GC7000UL 3D GPU + GC520L 2D GPU | NXP 공개 자료 |
| 메모리 | LPDDR4/DDR4 지원, 최대 6 GB (모듈 일반 2–4 GB) | NXP 공개 자료 |
| 인터페이스 | USB 3.0, PCIe 3.0, 2× GbE (TSN 포함), 2× CAN-FD, MIPI CSI/DSI, HDMI, LVDS | NXP 공개 자료 |
| 전력 소비 | 미공개 (일반 전체 보드 2–5 W) | NXP 공개 자료 |
| 패키지 | FCBGA 15 mm × 15 mm | NXP 공개 자료 |
| 가격 | 미공개 | NXP 공개 자료 |

**기술 하이라이트**: NPU 통합 산업용 이기종 SoC, 듀얼 ISP, TSN 이더넷, CAN-FD, ECC 메모리, 15년 공급 주기로 기능 안전 및 실시간 제어 시나리오에 적합합니다.

**적용 시나리오**: **산업용 비전 검사**: NPU가 결함 분류와 OCR을 가속화하고, 듀얼 ISP가 HDR 및 고역동 시나리오를 지원합니다. **AGV/AMR 메인 컨트롤러**: TSN/CAN-FD가 실시간 통신을 지원하고, 저전력으로 SLAM 및 내비게이션을 실행합니다. **스마트 게이트웨이 및 HMI**: 다중 화면 이기종 디스플레이, 풍부한 인터페이스 및 산업용 신뢰성

### NXP i.MX 93

> NXP i.MX 93: [공식 자료](https://www.nxp.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| CPU | 듀얼 코어 Cortex-A55 + Cortex-M33 | NXP 공개 자료 |
| NPU | 통합 Arm Ethos U65 | NXP 공개 자료 |
| AI 연산 성능 | 약 0.5 TOPS | NXP 공개 자료 |
| 공정 | 미공개 | NXP 공개 자료 |
| 인터페이스 | GbE, CAN-FD, USB, MIPI CSI/DSI | NXP 공개 자료 |
| 전력 소비 | 초저전력 설계 | NXP 공개 자료 |
| 가격 | 미공개 | NXP 공개 자료 |

**기술 하이라이트**: 저전력, 저비용, Arm Ethos U65 NPU 통합으로 경량 AIoT 및 음성/비전 웨이크업에 적합합니다.

**적용 시나리오**: 스마트 홈, 산업용 센서, 음성 어시스턴트, 경량 로봇 제어.

## 공급망 위치

- **상류 핵심 부품/소재**: TSMC/GlobalFoundries 위탁 생산, ARM IP, 자체 NPU, LPDDR4/DDR4, eMMC, 패키징/테스트, PMIC
- **하류 고객/적용 시나리오**: 산업 자동화 업체, 자동차 OEM/Tier1, 로봇 완제품 제조사, AIoT 장비 업체, 게이트웨이 업체
- **주요 경쟁사/대상**: Texas Instruments Jacinto, Renesas RZ/V, NVIDIA Jetson, Qualcomm QCS, Rockchip RK3588

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_nxp`
- 제품 엔터티: `ent_product_nxp_imx8m_plus`, `ent_product_nxp_imx93`
- 부품 엔터티: `ent_component_nxp_imx8m_plus_soc`, `ent_component_nxp_imx93_soc`
- 주요 관계:
  - `ent_company_nxp` -- `manufactures` --> `ent_product_nxp_imx8m_plus`
  - `ent_company_nxp` -- `manufactures` --> `ent_product_nxp_imx93`
  - `ent_company_nxp` -- `manufactures` --> `ent_component_nxp_imx8m_plus_soc`
  - `ent_company_nxp` -- `manufactures` --> `ent_component_nxp_imx93_soc`
  - `ent_product_nxp_imx8m_plus` -- `uses` --> `ent_component_nxp_imx8m_plus_soc`
  - `ent_product_nxp_imx93` -- `uses` --> `ent_component_nxp_imx93_soc`

## 참고 자료

1. [NXP 공식 웹사이트](https://www.nxp.com)
2. [i.MX 8M Plus 제품 페이지](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
3. [NXP i.MX 생태계](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors:IMX_HOME)
