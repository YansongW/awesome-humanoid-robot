# AMD / Advanced Micro Devices

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | AMD(에이엠디) |
| **영문명** | Advanced Micro Devices |
| **본사** | 미국 캘리포니아주 산타클라라 |
| **설립 시간** | 1969년 |
| **공식 웹사이트** | [https://www.amd.com](https://www.amd.com) |
| **공급망 단계** | CPU/GPU/FPGA/AI 가속, 데이터센터, 엣지 AI 컴퓨팅 |
| **기업 속성** | 상장 기업 (NASDAQ: AMD) |
| **모회사/소속 그룹** | 없음 (AMD는 상장 주체) |
| **데이터 출처** | AMD 공식 웹사이트, Xilinx 공식 웹사이트, 제품 매뉴얼, 공개 보도자료 |

## 회사 소개

AMD는 세계적인 반도체 설계 및 컴퓨팅 플랫폼 기업으로, 제품은 CPU, GPU, FPGA 및 적응형 컴퓨팅을 포괄하며, Xilinx 인수를 통해 AI 가속 및 엣지 컴퓨팅 시장에 진출했습니다.

AMD는 로봇 및 임베디드 지능을 위한 다양한 컴퓨팅 성능을 제공합니다: EPYC 서버 CPU는 훈련 및 시뮬레이션용, Instinct GPU는 대규모 모델 훈련/추론용, Ryzen AI 프로세서는 NPU를 통합하여 엣지 AI용, Xilinx Kria 및 Versal 적응형 컴퓨팅 플랫폼은 저지연, 프로그래밍 가능한 AI 추론 및 센서 융합 기능을 제공합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| EPYC | 데이터센터 서버 CPU | EPYC 9004 / 9005 시리즈 | 클라우드 컴퓨팅, 훈련/추론 서버 |
| Instinct | 데이터센터 AI GPU | MI300X / MI325X | 대규모 모델 훈련/추론, HPC |
| Ryzen AI | 엣지 AI PC/임베디드 프로세서 | Ryzen AI 300 시리즈 | 엣지 AI, 로봇 메인 컨트롤러 |
| Xilinx Kria | 적응형 엣지 AI 플랫폼 | Kria K26 / KR260 | 로봇 비전, 산업 제어 |
| Xilinx Versal | 적응형 컴퓨팅 가속 플랫폼 | Versal AI Edge 시리즈 | 자율 주행, 로봇 인식 |

## 대표 제품

### AMD Ryzen AI (NPU 통합 프로세서)

> AMD Ryzen AI: [공식 자료](https://www.amd.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 아키텍처 | Zen CPU + RDNA GPU + XDNA NPU | AMD 공개 자료 |
| NPU 연산 성능 | 최대 약 55 TOPS INT8 (Ryzen AI 300 시리즈) | AMD 공개 자료 |
| CPU 코어 | 최대 12코어 Zen 5 | AMD 공개 자료 |
| 공정 | 4 nm (공개 보도) | 공개 보도 |
| 메모리 | LPDDR5X / DDR5 지원 | AMD 공개 자료 |
| 인터페이스 | USB4, PCIe, 디스플레이 출력 등 | AMD 공개 자료 |
| 전력 소비 | 약 15–54 W | 공개 보도 |
| 가격 | OEM 완제품에 따라 다름 | - |

**기술 하이라이트**: CPU+GPU+NPU 3-in-1, XDNA 아키텍처 NPU 고효율, Windows AI 및 ONNX Runtime 지원.

**적용 시나리오**: AI PC, 엣지 AI 박스, 로봇 엣지 인식 및 의사 결정, 산업용 HMI.

### AMD Xilinx Kria K26

> AMD Xilinx Kria K26: [공식 자료](https://www.amd.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 아키텍처 | Zynq UltraScale+ MPSoC | AMD/Xilinx 공개 자료 |
| AI 연산 성능 | 약 1.4 TOPS INT8 | AMD/Xilinx 공개 자료 |
| CPU | 쿼드 코어 ARM Cortex-A53 + 듀얼 코어 Cortex-R5 | AMD/Xilinx 공개 자료 |
| 인터페이스 | 다중 MIPI, USB, 기가비트 이더넷, GPIO | AMD/Xilinx 공개 자료 |
| 전력 소비 | 약 5–15 W | 공개 보도 |
| 폼 팩터 | SOM 모듈 + 캐리어 보드 | AMD/Xilinx 공개 자료 |
| 가격 | 약 199 USD부터 (1k) | AMD 공개 가격 |

**기술 하이라이트**: FPGA+ARM 이기종, 프로그래밍 가능 로직, 저지연 센서 인터페이스, 산업용 신뢰성.

**적용 시나리오**: 로봇 비전, 산업 검사, 의료 영상, 스마트 리테일, 엣지 AI.

## 공급망 위치

- **상류 핵심 부품/소재**: TSMC 위탁 생산, 메모리 파트너, 패키징/테스트, EDA/IP, PCB/수동 부품.
- **하류 고객/적용 시나리오**: 데이터센터, 클라우드 컴퓨팅 업체, OEM/ODM, 산업 자동화, 자동차 전자, 로봇 완제품 제조사, 연구 기관.
- **주요 경쟁사/대응**: NVIDIA GPU/플랫폼, Intel Xeon/AI PC, Qualcomm 엣지 AI, Huawei Ascend, Horizon Robotics.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_amd`
- 제품 엔터티: `ent_product_amd_ryzen_ai`
- 부품 엔터티: `ent_component_amd_ryzen_ai_npu`
- 주요 관계:
  - `ent_company_amd` -- `manufactures` --> `ent_product_amd_ryzen_ai`
  - `ent_company_amd` -- `manufactures` --> `ent_component_amd_ryzen_ai_npu`
  - `ent_product_amd_ryzen_ai` -- `uses` --> `ent_component_amd_ryzen_ai_npu`

## 참고 자료

1. [AMD 공식 웹사이트](https://www.amd.com)
2. [AMD Ryzen AI 제품 페이지](https://www.amd.com/en/processors/ryzen-ai)
3. [AMD Xilinx Kria 제품 페이지](https://www.amd.com/en/products/system-on-modules/kria.html)
