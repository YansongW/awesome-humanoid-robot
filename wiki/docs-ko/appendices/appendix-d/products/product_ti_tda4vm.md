# TI TDA4VM Jacinto 프로세서

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [텍사스 인스트루먼트 / Texas Instruments](../companies/company_texas_instruments.md) |
| **제품 카테고리** | ADAS / 산업용 엣지 AI SoC / 기능 안전 프로세서 |
| **출시일** | 2020년 출시, 2021년 양산 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [TI TDA4VM 제품 페이지](https://www.ti.com/product/TDA4VM) |

## 제품 개요

TI TDA4VM은 Jacinto 7 아키텍처 기반의 이기종 SoC로, ADAS 및 산업용 엣지 AI를 대상으로 합니다. 칩은 8 TOPS INT8의 Matrix Multiply Accelerator, C7x 벡터 DSP, 듀얼 코어 Cortex-A72 및 6코어 실시간 Cortex-R5F를 통합하며, ISP, 비전 가속기, 8포트 기가비트 이더넷 스위치 및 PCIe 허브를 갖추고 있습니다. ASIL-D 기능 안전 지원으로 고신뢰 로봇, 자율주행 인식 및 산업용 비전에 이상적인 선택입니다.

## 제품 이미지

> TI TDA4VM Jacinto 프로세서: [공식 자료](https://www.ti.com/product/TDA4VM)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 공정 | 16 nm FinFET (공개 보도) | TI 공개 자료 |
| CPU | 듀얼 코어 64-bit Arm Cortex-A72 @ 최대 2.0 GHz + 6코어 Cortex-R5F @ 1.0 GHz | TI 공개 자료 |
| AI 가속기 | C7x DSP + Matrix Multiply Accelerator (MMA) | TI 공개 자료 |
| AI 연산 성능 | 최대 8 TOPS INT8 (MMA) | TI 공개 자료 |
| DSP | 2× C7x + 2× C66x | TI 공개 자료 |
| GPU | PowerVR Rogue 8XE GE8430 (약 100 GFLOPS) | TI 공개 자료 |
| ISP/비전 | 7세대 ISP, VPAC, DMPAC 통합 | TI 공개 자료 |
| 메모리 | LPDDR4 지원 | TI 공개 자료 |
| 인터페이스 | PCIe 허브, 8포트 GbE 스위치, CSI-2, CAN-FD, USB 3.1, MCASP | TI 공개 자료 |
| 전력 소비 | 일반 약 5–20 W (구성에 따라 다름) | TI 공개 자료 |
| 안전 | ASIL-D / SIL-3 목표 기능 안전 | TI 공개 자료 |
| 가격 | SK-TDA4VM 개발 키트 약 199 USD | TI 공개 자료 |

## 공급망 위치

- **제조사**: [텍사스 인스트루먼트 / Texas Instruments](../companies/company_texas_instruments.md)
- **핵심 부품/기술 출처**: TI 자체 개발 C7x/MMA/ISP, ARM CPU/GPU IP, 16 nm 파운드리, LPDDR4, PMIC, 캐리어 보드
- **하위 응용/고객**: 자동차 Tier1/OEM, 산업용 AMR/AGV 제조사, 머신 비전 통합업체, 로봇 완제품 제조사

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ti_tda4vm`
- 부품 엔터티: `ent_component_ti_tda4vm_soc`
- 제조사 엔터티: `ent_company_texas_instruments`
- 주요 관계:
  - `rel_ent_company_texas_instruments_manufactures_ent_product_ti_tda4vm` (`ent_company_texas_instruments` → `manufactures` --> `ent_product_ti_tda4vm`)
  - `rel_ent_company_texas_instruments_manufactures_ent_component_ti_tda4vm_soc` (`ent_company_texas_instruments` → `manufactures` --> `ent_component_ti_tda4vm_soc`)
  - `ent_product_ti_tda4vm` -- `uses` --> `ent_component_ti_tda4vm_soc`

## 응용 시나리오

- **산업용 AMR/AGV**: 다중 센서 융합, 안전 인증, 실시간 경로 계획 및 장애물 회피
- **머신 비전 검사**: ISP + MMA를 통한 고속 결함 검출 및 객체 인식
- **ADAS 인식 ECU**: 전방/서라운드 뷰, 레이더/라이다 융합, ASIL-D 지원

## 경쟁 비교

| 비교 항목 | TI TDA4VM | NXP S32G / i.MX 8M Plus | NVIDIA Jetson Orin NX |
|---|---|---|---|
| AI 연산 성능 | 8 TOPS | 2.3 TOPS / S32G NPU 없음 | 최대 100 TOPS |
| 기능 안전 | ASIL-D 목표 | ASIL-B/D (버전에 따라 다름) | 산업용 |
| CPU | 듀얼 코어 A72 + 6코어 R5F | 쿼드 코어 A53 + M7 | 8코어 / 12코어 ARM |

## 구매 및 배포 권장 사항

TI Processor SDK (Linux/RTOS)를 사용하여 MMA 및 C7x 성능을 평가하세요. 기능 안전 등급 요구 사항을 확인하세요. 산업용 배포 시 적절한 방열 및 캐리어 보드 설계를 선택하세요.

## 관련 항목

- [제조사: 텍사스 인스트루먼트 / Texas Instruments](../companies/company_texas_instruments.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [TI TDA4VM 제품 페이지](https://www.ti.com/product/TDA4VM)
2. [TI Jacinto 7 페이지](https://www.ti.com/processors/automotive-processors/jacino-7-family.html)
3. [SK-TDA4VM 개발 키트](https://www.ti.com/tool/SK-TDA4VM)
