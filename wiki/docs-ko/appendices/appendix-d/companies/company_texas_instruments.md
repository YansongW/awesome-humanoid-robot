# 텍사스 인스트루먼트 / Texas Instruments

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 텍사스 인스트루먼트 |
| **영문명** | Texas Instruments |
| **본사** | 미국 텍사스주 댈러스 |
| **설립 연도** | 1930년 |
| **공식 사이트** | [https://www.ti.com](https://www.ti.com) |
| **공급망 단계** | 산업용 MCU, Jacinto ADAS/엣지 AI, 아날로그 및 전원 관리 |
| **기업 속성** | 상장 기업 (NASDAQ: TXN) |
| **모회사/소속 그룹** | 없음 (Texas Instruments가 상장 주체) |
| **데이터 출처** | TI 공식 사이트, Jacinto 제품 매뉴얼, 공개 보도자료, 업계 보고서 |

## 회사 개요

Texas Instruments(텍사스 인스트루먼트)는 세계 최대의 아날로그 및 임베디드 반도체 기업 중 하나로, 프로세서, MCU, 센서, 전원 관리 및 아날로그 소자를 포괄합니다. Jacinto 7 시리즈 SoC(예: TDA4VM)는 ADAS 및 엣지 AI 전용으로 설계되었으며, 딥러닝 가속기(MMA), DSP, ISP, 기능 안전 하드웨어 및 다양한 산업용 인터페이스를 통합하여 자동차, 산업용 로봇 및 머신 비전에 널리 사용됩니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| Jacinto 7 / TDA4x | ADAS 및 엣지 AI 프로세서 | TDA4VM | 자율주행 인지, 산업용 AMR, 머신 비전, 엣지 AI Box |
| Sitara / AM6x | 산업용 Arm 프로세서 | AM68A / AM69A | 산업용 게이트웨이, 로봇 제어, HMI, 실시간 통신 |

## 대표 제품

### TI TDA4VM

> TI TDA4VM: [공식 자료](https://www.ti.com)를 방문하여 확인하세요.

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
| 인터페이스 | PCIe hub, 8-port GbE 스위치, CSI-2, CAN-FD, USB 3.1, MCASP | TI 공개 자료 |
| 전력 소비 | 일반 약 5–20 W (구성에 따라 다름) | TI 공개 자료 |
| 안전 | ASIL-D / SIL-3 목표 기능 안전 | TI 공개 자료 |
| 가격 | SK-TDA4VM 개발 키트 약 199 USD | TI 공개 자료 |

**기술적 특징**: Jacinto 7 이기종 아키텍처, 8 TOPS MMA, C7x 벡터 DSP, 통합 ISP 및 VPAC/DMPAC, ASIL-D 기능 안전, 풍부한 차량용/산업용 인터페이스.

**응용 시나리오**: **산업용 AMR/AGV**: 다중 센서 융합, 안전 인증, 실시간 경로 계획 및 장애물 회피; **머신 비전 검사**: ISP + MMA를 통한 고속 결함 검출 및 객체 인식; **ADAS 인지 ECU**: 전방/서라운드 뷰, 레이더/라이다 융합, ASIL-D 지원

### TI AM68A

> TI AM68A: [공식 자료](https://www.ti.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| CPU | 듀얼 코어 Cortex-A72 + 6코어 Cortex-R5F | TI 공개 자료 |
| AI 가속기 | MMA + C7x DSP | TI 공개 자료 |
| AI 연산 성능 | 최대 8 TOPS | TI 공개 자료 |
| 인터페이스 | PCIe, GbE, USB, CSI-2, CAN-FD | TI 공개 자료 |
| 전력 소비 | 약 5–15 W | TI 공개 자료 |
| 안전 | 산업용 안전 기능 | TI 공개 자료 |
| 가격 | 미공개 | TI 공개 자료 |

**기술적 특징**: 산업 및 엣지 AI를 위한 Jacinto 7 파생 플랫폼으로, 연산 성능, 전력 소비 및 산업용 인터페이스의 균형을 유지합니다.

**응용 시나리오**: 산업용 게이트웨이, 엣지 AI Box, 로봇 메인 컨트롤러, 스마트 리테일.

## 공급망 위치

- **상류 핵심 부품/소재**: TSMC/자체 웨이퍼 팹, ARM IP, 자체 개발 C7x DSP/MMA, 메모리, PMIC, 패키징/테스트, PCB
- **하류 고객/응용 시나리오**: 자동차 Tier1/OEM, 산업 자동화 업체, 로봇 기업, 머신 비전 통합업체, 에너지 및 인프라
- **주요 경쟁사/대상**: NXP i.MX / S32, NVIDIA Jetson, Renesas RZ/V, Qualcomm Ride, Horizon Robotics Journey

## 지식 그래프 노드 및 관계

- 기업 엔터티: `ent_company_texas_instruments`
- 제품 엔터티: `ent_product_ti_tda4vm`, `ent_product_ti_am68a`
- 부품 엔터티: `ent_component_ti_tda4vm_soc`, `ent_component_ti_am68a_soc`
- 주요 관계:
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_product_ti_tda4vm`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_product_ti_am68a`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_component_ti_tda4vm_soc`
  - `ent_company_texas_instruments` -- `manufactures` --> `ent_component_ti_am68a_soc`
  - `ent_product_ti_tda4vm` -- `uses` --> `ent_component_ti_tda4vm_soc`
  - `ent_product_ti_am68a` -- `uses` --> `ent_component_ti_am68a_soc`

## 참고 자료

1. [TI 공식 사이트](https://www.ti.com)
2. [TDA4VM 제품 페이지](https://www.ti.com/product/TDA4VM)
3. [Jacinto 7 프로세서](https://www.ti.com/processors/automotive-processors/jacino-7-family.html)
