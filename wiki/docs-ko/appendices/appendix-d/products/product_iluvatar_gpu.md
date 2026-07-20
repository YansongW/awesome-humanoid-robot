# 天数智芯天垓 200 / Iluvatar BI-V200

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 '미공개'로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [天数智芯 / Iluvatar CoreX](../companies/company_iluvatar.md) |
| **제품 카테고리** | 범용 GPU / AI 학습 추론 가속 카드 |
| **출시일** | 天垓 100 이후 天垓 200으로 업데이트 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | 天数智芯 공식 사이트, 제품 매뉴얼 |

## 제품 개요

天数智芯 天垓 200（BI-V200）은 天数智芯이 출시한 차세대 범용 GPU 가속 카드로, 자체 개발 범용 GPU 아키텍처를 기반으로 AI 학습, 추론 및 고성능 컴퓨팅에 국산 연산력을 제공합니다.

天垓 200은 FP32/FP16/BF16/INT8 등 다중 정밀도 연산을 지원하며, HBM2e 고대역폭 메모리와 PCIe Gen4 인터페이스를 탑재하고 주요 CUDA 애플리케이션 생태계와 호환됩니다. 범용 GPU 아키텍처는 딥러닝뿐만 아니라 과학 컴퓨팅, 그래픽 렌더링 및 로봇 시뮬레이션 학습 등의 작업도 지원합니다.

## 제품 이미지

> 天数智芯 天垓 200: [공식 자료](https://www.iluvatar.com.cn)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| GPU | 天垓 200（BI-V200） | 天数智芯 공식 사이트 |
| 아키텍처 | 자체 개발 범용 GPU 아키텍처 | 天数智芯 공개 자료 |
| 공정 | 7 nm | 공개 보도 |
| AI 연산력 | FP16 / BF16 / FP32 수백 TFLOPS급 | 天数智芯 공개 자료 |
| 메모리 | 32 GB HBM2e（일부 모델） | 공개 보도 |
| 메모리 대역폭 | 미공개 | - |
| 상호 연결 | 다중 카드 상호 연결 지원 | 天数智芯 공개 자료 |
| 인터페이스 | PCIe Gen4 / OAM | 공개 보도 |
| 전력 소비 | 약 300–350 W | 공개 보도 |
| 소프트웨어 스택 | CUDA 호환 런타임, 天数智芯 SDK | 天数智芯 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [天数智芯 / Iluvatar CoreX](../companies/company_iluvatar.md)
- **핵심 부품/기술 출처**: 자체 개발 범용 GPU 아키텍처, 웨이퍼 파운드리, HBM2e 메모리, 패키징 및 테스트, PCB, 방열.
- **하류 응용/고객**: 인터넷 기업, 클라우드 컴퓨팅 업체, 지능형 컴퓨팅 센터, AI 기업, 연구 기관, 로봇 기업.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_iluvatar_biv200`
- 부품 엔터티: `ent_component_iluvatar_biv200_gpu`
- 제조사 엔터티: `ent_company_iluvatar`
- 주요 관계:
  - `rel_ent_company_iluvatar_manufactures_ent_product_iluvatar_biv200`（`ent_company_iluvatar` → `manufactures` --> `ent_product_iluvatar_biv200`）
  - `rel_ent_company_iluvatar_manufactures_ent_component_iluvatar_biv200_gpu`（`ent_company_iluvatar` → `manufactures` --> `ent_component_iluvatar_biv200_gpu`）
  - `ent_product_iluvatar_biv200` -- `uses` --> `ent_component_iluvatar_biv200_gpu`

## 응용 시나리오

- **대규모 모델 학습 및 미세 조정**: 수백억에서 수천억 매개변수 모델의 분산 학습 지원.
- **AIGC 및 과학 컴퓨팅**: 생성형 AI, 분자 시뮬레이션, CFD 등 고성능 컴퓨팅 작업에 사용.
- **로봇 시뮬레이션 및 학습**: Isaac Sim/Gazebo 등 시뮬레이션 플랫폼과 결합하여 정책 학습 및 Sim2Real 가속.

## 경쟁 비교

| 비교 항목 | 天垓 200 | NVIDIA A100 | 华为昇腾 910B |
|--------|------|------|------|
| 아키텍처 | 범용 GPU | NVIDIA Ampere | 다빈치 |
| 생태계 | CUDA 호환 | CUDA | CANN + MindSpore |
| 메모리 | 32 GB HBM2e | 40/80 GB HBM | HBM2e |
| 국산화 | 자체 제어 가능 | 수출 통제 영향 | 자체 제어 가능 |

## 구매 및 배포 권장 사항

- CUDA 애플리케이션 마이그레이션 전에 天数智芯 호환 레이어의 완전성과 성능을 검증해야 합니다.
- 다중 카드 학습 시나리오에서는 상호 연결 대역폭, NCCL 호환성 및 클러스터 토폴로지를 확인해야 합니다.
- 天数智芯 공식 채널을 통해 최신 드라이버, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 天数智芯 / Iluvatar CoreX](../companies/company_iluvatar.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [天数智芯 공식 사이트](https://www.iluvatar.com.cn)
2. [天数智芯 제품 페이지](https://www.iluvatar.com.cn/product/)
3. 天数智芯 제품 발표회 자료
