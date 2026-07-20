# AMD Ryzen AI (통합 XDNA NPU)

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [AMD / Advanced Micro Devices](../companies/company_amd.md) |
| **제품 카테고리** | 엣지 AI PC / 임베디드 AI 프로세서 |
| **출시 시간** | Ryzen AI 시리즈는 라이젠 프로세서와 함께 반복 출시 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | AMD 공식 사이트, Ryzen AI 제품 페이지 |

## 제품 개요

AMD Ryzen AI는 AMD가 라이젠 프로세서에 통합한 전용 AI 연산 엔진으로, XDNA 아키텍처 NPU를 기반으로 AI PC, 엣지 디바이스 및 로봇 엣지에 고효율 AI 추론 능력을 제공합니다.

Ryzen AI는 Zen CPU, RDNA GPU 및 XDNA NPU를 단일 SoC에 통합하여 Windows AI, ONNX Runtime 및 다양한 엣지 AI 프레임워크를 지원합니다. 15–54 W 전력 구간은 노트북, 미니 PC, 엣지 박스 및 로봇 컨트롤러를 포괄하며, VLM, 음성 인식, 실시간 비전 등 엣지 AI 작업에 적합합니다.

## 제품 이미지

> AMD Ryzen AI: [공식 자료](https://www.amd.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 프로세서 | AMD Ryzen AI 300 시리즈 | AMD 공식 사이트 |
| 아키텍처 | Zen 5 CPU + RDNA GPU + XDNA NPU | AMD 공개 자료 |
| 공정 | 4 nm | 공개 보도 |
| NPU 연산 성능 | 최대 약 55 TOPS INT8 | AMD 공개 자료 |
| CPU 코어 | 최대 12코어 Zen 5 | AMD 공개 자료 |
| GPU | RDNA 3.5 통합 그래픽 | AMD 공개 자료 |
| 메모리 | LPDDR5X / DDR5 지원 | AMD 공개 자료 |
| 인터페이스 | USB4, PCIe, DP/HDMI 등 | AMD 공개 자료 |
| 전력 소비 | 약 15–54 W | 공개 보도 |
| 가격 | OEM 완제품에 따라 다름 | - |

## 공급망 위치

- **제조사**: [AMD / Advanced Micro Devices](../companies/company_amd.md)
- **핵심 부품/기술 출처**: TSMC 위탁 생산, 자체 개발 XDNA NPU, LPDDR5X/DDR5 메모리, 메인보드/PCB, 방열.
- **하위 응용/고객**: OEM PC 제조사, 엣지 디바이스 업체, 산업 자동화, 로봇 완제품 제조사, 개발자.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_amd_ryzen_ai`
- 부품 엔터티: `ent_component_amd_ryzen_ai_npu`
- 제조사 엔터티: `ent_company_amd`
- 주요 관계:
  - `rel_ent_company_amd_manufactures_ent_product_amd_ryzen_ai` (`ent_company_amd` → `manufactures` --> `ent_product_amd_ryzen_ai`)
  - `rel_ent_company_amd_manufactures_ent_component_amd_ryzen_ai_npu` (`ent_company_amd` → `manufactures` --> `ent_component_amd_ryzen_ai_npu`)
  - `ent_product_amd_ryzen_ai` -- `uses` --> `ent_component_amd_ryzen_ai_npu`

## 응용 시나리오

- **AI PC 및 엣지 박스**: 로컬 대규모 언어 모델 실행, 음성 인식, 실시간 번역 및 비전 응용.
- **로봇 엣지 메인 컨트롤러**: 로봇 소뇌/엣지 두뇌 역할, 인식, 내비게이션 및 인간-로봇 상호 작용 처리.
- **산업 HMI 및 엣지 게이트웨이**: 그래픽 렌더링, AI 추론 및 다중 디바이스 연결 기능 제공.

## 경쟁 비교

| 비교 항목 | AMD Ryzen AI | Intel Core Ultra | Qualcomm Snapdragon X |
|--------|------|------|------|
| NPU 아키텍처 | XDNA | NPU (Meteor/Lunar Lake) | Hexagon NPU |
| 연산 성능 | 최대 55 TOPS | 최대 약 48 TOPS | 최대 약 45 TOPS |
| 생태계 | Windows AI / ONNX | Windows AI / ONNX | Windows on ARM |
| 통합도 | CPU+GPU+NPU | CPU+GPU+NPU | CPU+GPU+NPU |

## 구매 및 배포 권장 사항

- 전력 소비 및 폼 팩터에 따라 H/HS/U 시리즈 모델을 선택하고, 대상 프레임워크의 XDNA NPU 드라이버 지원을 확인하세요.
- 로봇 솔루션 배포 시 I/O 인터페이스, 실시간성 및 방열 설계를 평가하세요.
- AMD 공식 채널 또는 OEM을 통해 최신 드라이버, Ryzen AI SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: AMD / Advanced Micro Devices](../companies/company_amd.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [AMD 공식 사이트](https://www.amd.com)
2. [AMD Ryzen AI 제품 페이지](https://www.amd.com/en/processors/ryzen-ai)
3. AMD Ryzen AI 개발자 가이드
