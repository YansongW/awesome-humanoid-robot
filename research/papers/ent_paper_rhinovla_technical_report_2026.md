---
$id: ent_paper_rhinovla_technical_report_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: RhinoVLA Technical Report
  zh: RhinoVLA Technical Report
  ko: RhinoVLA Technical Report
summary:
  en: 'arXiv:2606.07383v2 Announce Type: replace Abstract: Vision-Language-Action (VLA) models have shown strong potential
    for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM
    visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation
    grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose
    RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL
    backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained
    multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines
    View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations
    and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware
    compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream
    performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi
    R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.'
  zh: RhinoVLA 是一个面向边缘部署的视觉-语言-动作模型，由 Huixi AI 与 Huixi R1 边缘 SoC 协同设计。其核心贡献在于通过 token 高效的 Qwen3-VL 骨干网络和连续动作专家模块降低计算负担，并引入统一接口支持跨机器人学习。在
    Huixi R1 上实现了 11.69 Hz 的端到端推理，满足 10 Hz 实时闭环控制需求。
  ko: 'arXiv:2606.07383v2 Announce Type: replace Abstract: Vision-Language-Action (VLA) models have shown strong potential
    for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM
    visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation
    grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose
    RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL
    backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained
    multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines
    View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations
    and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware
    compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream
    performance comparable to {\pi}0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi
    R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- rhinovla_technical_report
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.07383v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: RhinoVLA Technical Report
  url: https://arxiv.org/abs/2606.07383
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
RhinoVLA 针对 VLA 模型在边缘硬件上实时部署的延迟问题，识别出 VLM 视觉和上下文 token 是主要瓶颈。为此，它采用 token 高效的 Qwen3-VL 骨干网络和连续动作专家模块，在保持预训练多模态能力的同时减少 token 和计算量。为支持跨机器人学习，RhinoVLA 设计了统一接口，结合视图注册表、72D 物理状态-动作槽空间和机器人实例 LoRA，使异构机器人观测和动作模式能在共享策略下对齐。部署方面，通过硬件感知编译、混合精度执行和并行视觉编码进行优化。实验表明，RhinoVLA 在相似参数量下达到与 π0.5 相当的下游性能，并在 Huixi R1 上实现 11.69 Hz 的端到端推理。

## 核心内容
### 方法
- **问题识别**：VLM 的视觉和上下文 token 是部署延迟的主要来源。在 GEMM 主导的投影算子中，当模型维度固定时，计算量随输入 token 数量线性增长。
- **模型架构**：采用 token 高效的 Qwen3-VL 骨干网络，结合连续动作专家模块，在保留预训练多模态能力的同时降低 VLM 侧的 token 和计算负担。
- **跨机器人学习**：引入统一接口，包含视图注册表、72D 物理状态-动作槽空间和机器人实例 LoRA，使不同机器人的观测和动作模式能在共享策略下对齐。

### 部署优化
- **硬件感知编译**：针对 Huixi R1 边缘 SoC 进行定制化编译优化。
- **混合精度执行**：结合不同精度计算以平衡性能与效率。
- **并行视觉编码**：通过并行处理加速视觉编码阶段。

### 实验设置与结果
- **性能对比**：在相似参数量下，RhinoVLA 的下游性能与 π0.5 相当。
- **推理速度**：在 Huixi R1 上实现 11.69 Hz 的端到端推理，超过 10 Hz 的实时闭环控制目标。
- **开源计划**：项目代码将在 https://github.com/HuixiAI/RhinoVLA 开源。

## Overview
Vision-Language-Action (VLA) models have shown strong potential for robotic manipulation, but real-time deployment on edge hardware remains challenging. In this work, we identify VLM visual and context tokens as a major source of deployment latency: for GEMM-dominated projection operators, computation grows linearly with the number of input tokens when model dimensions are fixed. Motivated by this observation, we propose RhinoVLA, a deployment-oriented VLA model co-designed with the Huixi R1 edge SoC. RhinoVLA adopts a token-efficient Qwen3-VL backbone and a continuous Action Expert, reducing the VLM-side token and computation burden while preserving pretrained multimodal capability. To support cross-robot learning, RhinoVLA further introduces a unified interface that combines View Registry, 72D physical state-action slot space, and robotinstance LoRA, allowing heterogeneous robot observations and action schemas to be aligned under a shared policy. On the deployment side, RhinoVLA is optimized through hardware-aware compilation, mixed-precision execution, and parallel visual encoding. Experiments show that RhinoVLA achieves downstream performance comparable to π0.5 at a similar parameter scale, while reaching 11.69 Hz end-to-end inference on Huixi R1, meeting the 10 Hz real-time closedloop control target. The project will be open-sourced at https://github.com/HuixiAI/RhinoVLA.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 조작 분야에서 강력한 잠재력을 보여주었지만, 엣지 하드웨어에서의 실시간 배포는 여전히 어려운 과제입니다. 본 연구에서는 VLM 시각 및 컨텍스트 토큰이 배포 지연 시간의 주요 원인임을 확인했습니다. GEMM이 지배적인 투영 연산자의 경우, 모델 차원이 고정되었을 때 계산량이 입력 토큰 수에 따라 선형적으로 증가합니다. 이러한 관찰에 기반하여, 우리는 Huixi R1 엣지 SoC와 공동 설계된 배포 지향 VLA 모델인 RhinoVLA를 제안합니다. RhinoVLA는 토큰 효율적인 Qwen3-VL 백본과 연속적인 Action Expert를 채택하여, 사전 학습된 멀티모달 능력을 유지하면서 VLM 측의 토큰 및 계산 부담을 줄입니다. 교차 로봇 학습을 지원하기 위해 RhinoVLA는 View Registry, 72D 물리적 상태-행동 슬롯 공간, 로봇 인스턴스 LoRA를 결합한 통합 인터페이스를 추가로 도입하여, 이기종 로봇 관측 및 행동 스키마를 공유 정책 하에 정렬할 수 있게 합니다. 배포 측면에서 RhinoVLA는 하드웨어 인식 컴파일, 혼합 정밀도 실행, 병렬 시각 인코딩을 통해 최적화되었습니다. 실험 결과, RhinoVLA는 유사한 파라미터 규모에서 π0.5와 견줄 만한 다운스트림 성능을 달성하면서, Huixi R1에서 11.69Hz의 종단 간 추론 속도를 기록하여 10Hz 실시간 폐루프 제어 목표를 충족합니다. 이 프로젝트는 https://github.com/HuixiAI/RhinoVLA에서 오픈소스로 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 조작 분야에서 강력한 잠재력을 보여주었지만, 엣지 하드웨어에서의 실시간 배포는 여전히 어려운 과제입니다. 본 연구에서는 VLM 시각 및 컨텍스트 토큰이 배포 지연 시간의 주요 원인임을 확인했습니다. GEMM이 지배적인 투영 연산자의 경우, 모델 차원이 고정되었을 때 계산량이 입력 토큰 수에 따라 선형적으로 증가합니다. 이러한 관찰에 기반하여, 우리는 Huixi R1 엣지 SoC와 공동 설계된 배포 지향 VLA 모델인 RhinoVLA를 제안합니다. RhinoVLA는 토큰 효율적인 Qwen3-VL 백본과 연속적인 Action Expert를 채택하여, 사전 학습된 멀티모달 능력을 유지하면서 VLM 측의 토큰 및 계산 부담을 줄입니다. 교차 로봇 학습을 지원하기 위해 RhinoVLA는 View Registry, 72D 물리적 상태-행동 슬롯 공간, 로봇 인스턴스 LoRA를 결합한 통합 인터페이스를 추가로 도입하여, 이기종 로봇 관측 및 행동 스키마를 공유 정책 하에 정렬할 수 있게 합니다. 배포 측면에서 RhinoVLA는 하드웨어 인식 컴파일, 혼합 정밀도 실행, 병렬 시각 인코딩을 통해 최적화되었습니다. 실험 결과, RhinoVLA는 유사한 파라미터 규모에서 π0.5와 견줄 만한 다운스트림 성능을 달성하면서, Huixi R1에서 11.69Hz의 종단 간 추론 속도를 기록하여 10Hz 실시간 폐루프 제어 목표를 충족합니다. 이 프로젝트는 https://github.com/HuixiAI/RhinoVLA에서 오픈소스로 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2606.07383v3
