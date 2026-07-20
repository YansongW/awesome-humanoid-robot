# NXP i.MX 8M Plus 애플리케이션 프로세서

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [NXP Semiconductors](../companies/company_nxp.md) |
| **제품 카테고리** | NPU 통합 산업용 애플리케이션 프로세서 / 엣지 AI SoC |
| **출시일** | 2020년 출시, 2021년 양산 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [NXP i.MX 8M Plus 제품 페이지](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS) |

## 제품 개요

NXP i.MX 8M Plus는 산업 및 AIoT를 위한 14nm 이기종 애플리케이션 프로세서로, 2.3 TOPS NPU, 듀얼 ISP, 쿼드 코어 Cortex-A53 및 실시간 Cortex-M7을 통합합니다. 이 칩은 TSN 기가비트 이더넷, CAN-FD, PCIe 3.0 및 다중 디스플레이 출력을 지원하며, 로컬에서 결함 감지, 객체 인식 등의 비전 AI 작업을 수행할 수 있습니다. 또한 산업용 온도 범위와 긴 공급 주기를 갖추고 있어 로봇, AGV 및 산업용 게이트웨이에 널리 사용됩니다.

## 제품 이미지

> NXP i.MX 8M Plus 애플리케이션 프로세서: [공식 자료](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
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

## 공급망 위치

- **제조사**: [NXP Semiconductors](../companies/company_nxp.md)
- **핵심 부품/기술 출처**: NXP 자체 개발 NPU 및 시스템 IP, ARM CPU/GPU IP, TSMC/GlobalFoundries 14nm 파운드리, LPDDR4/DDR4, PMIC, 패키징 및 테스트
- **하위 응용/고객**: 산업 자동화 장비 업체, AGV/AMR 제조사, 로봇 완제품 업체, 의료 및 스마트 게이트웨이 고객

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_nxp_imx8m_plus`
- 부품 엔터티: `ent_component_nxp_imx8m_plus_soc`
- 제조사 엔터티: `ent_company_nxp`
- 주요 관계:
  - `rel_ent_company_nxp_manufactures_ent_product_nxp_imx8m_plus` (`ent_company_nxp` → `manufactures` --> `ent_product_nxp_imx8m_plus`)
  - `rel_ent_company_nxp_manufactures_ent_component_nxp_imx8m_plus_soc` (`ent_company_nxp` → `manufactures` --> `ent_component_nxp_imx8m_plus_soc`)
  - `ent_product_nxp_imx8m_plus` -- `uses` --> `ent_component_nxp_imx8m_plus_soc`

## 응용 시나리오

- **산업용 비전 검사**: NPU 가속 결함 분류 및 OCR, 듀얼 ISP가 HDR 및 고다이내믹 시나리오 지원
- **AGV/AMR 메인 컨트롤러**: TSN/CAN-FD가 실시간 통신 지원, 저전력 SLAM 및 내비게이션 실행
- **스마트 게이트웨이 및 HMI**: 다중 화면 이종 출력, 풍부한 인터페이스 및 산업용 신뢰성

## 경쟁 비교

| 비교 항목 | i.MX 8M Plus | TI TDA4VM | Renesas RZ/V2H |
|---|---|---|---|
| AI 연산 성능 | 2.3 TOPS | 8 TOPS | 8 TOPS (고밀도) |
| CPU | 쿼드 코어 A53 + M7 | 듀얼 코어 A72 + 6코어 R5F | 쿼드 코어 A55 + 듀얼 코어 R8 |
| 산업용 인터페이스 | TSN, CAN-FD, PCIe 3.0 | TSN, CAN-FD, PCIe | CAN-FD, PCIe, USB 3.2 |

## 구매 및 배포 권장 사항

NXP eIQ 툴체인을 사용하여 NPU에서 모델 성능을 평가합니다. 다른 버전(Quad/Lite)이 NPU를 통합했는지 확인합니다. 산업용 시나리오에서는 온도 등급과 ECC 메모리 구성을 확인합니다.

## 관련 항목

- [제조사: NXP Semiconductors](../companies/company_nxp.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [NXP i.MX 8M Plus 제품 페이지](https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-8-applications-processors/i-mx-8m-plus-arm-cortex-a53-machine-learning-vision-multimedia-and-industrial-iot:IMX8MPLUS)
2. [NXP i.MX 8M Plus 데이터 시트](https://www.nxp.com/docs/en/data-sheet/IMX8MPLUSIEC.pdf)
3. [NXP eIQ 머신러닝 소프트웨어](https://www.nxp.com/design/software/development-software/eiq-ml-software-development-environment:EIQ)
