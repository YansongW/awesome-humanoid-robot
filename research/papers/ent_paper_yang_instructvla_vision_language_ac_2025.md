---
$id: ent_paper_yang_instructvla_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation'
  zh: InstructVLA
  ko: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation'
summary:
  en: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
  zh: InstructVLA 是由中国科学技术大学、浙江大学和上海人工智能实验室于 2025 年提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于提出 Vision-Language-Action Instruction
    Tuning (VLA-IT) 训练范式，通过混合专家适配在保留大视觉语言模型灵活推理能力的同时，显著提升操作性能。在 SimplerEnv 任务上，InstructVLA 相比 SpatialVLA 提升 33%，并在新基准 SimplerEnv-Instruct
    上超越 GPT-4o 辅助的动作专家 29%。
  ko: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (InstructVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by University of Science and Technology of China,
    Zhejiang University, Shanghai Artificial Intelligence Laboratory.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- instructvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.17520v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'InstructVLA: Vision-Language-Action Instruction Tuning from Understanding to Manipulation (arXiv)'
  url: https://arxiv.org/abs/2507.17520
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InstructVLA source
  url: https://doi.org/10.48550/arXiv.2507.17520
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
InstructVLA 旨在解决现有视觉-语言-动作模型在融合多模态推理与精确动作生成时的权衡问题，避免因过度聚焦任务特定操作数据而导致的预训练能力灾难性遗忘。该模型采用端到端架构，通过 VLA-IT 训练范式在标准 VLM 语料库和精心构建的 65 万样本 VLA-IT 数据集上联合优化具身推理与动作生成。实验表明，InstructVLA 在 SimplerEnv 域内任务中表现优异，并在包含 80 个任务的 SimplerEnv-Instruct 基准上验证了其泛化能力，同时展现出推理时扩展特性，即通过文本推理提升模拟与真实场景的操作性能。

## 核心内容
### 方法
- **VLA-IT 训练范式**：采用混合专家适配（Mixture-of-Experts Adaptation）进行多模态训练，在标准 VLM 语料库与 65 万样本的 VLA-IT 数据集上联合优化具身推理与动作生成。
- **架构设计**：端到端模型，保留大视觉语言模型（VLM）的灵活推理能力，同时通过具身推理增强操作性能。

### 实验设置
- **域内任务**：在 SimplerEnv 基准上评估，InstructVLA 相比 SpatialVLA 实现 33% 的性能提升。
- **泛化评估**：引入新基准 SimplerEnv-Instruct，包含 80 个任务，要求闭环控制与高级指令理解。InstructVLA 在此基准上超越微调后的 OpenVLA 96%，并超过由 GPT-4o 辅助的动作专家 29%。

### 关键结果
- **多模态任务**：InstructVLA 在标准多模态任务上超越基线 VLM 模型。
- **推理时扩展**：通过利用文本推理，InstructVLA 在模拟与真实场景中均能提升操作性能，展现出推理时扩展特性。

### 结论
InstructVLA 成功弥合了直观可操控的人机交互与高效策略学习之间的鸿沟，证明了其在机器人操作领域融合推理与动作生成的潜力。

## Overview
To operate effectively in the real world, robots should integrate multimodal reasoning with precise action generation. However, existing vision-language-action (VLA) models often sacrifice one for the other, narrow their abilities to task-specific manipulation data, and suffer catastrophic forgetting of pre-trained vision-language capabilities. To bridge this gap, we introduce InstructVLA, an end-to-end VLA model that preserves the flexible reasoning of large vision-language models (VLMs) while delivering leading manipulation performance with the help of embodied reasoning. InstructVLA introduces a novel training paradigm, Vision-Language-Action Instruction Tuning (VLA-IT), which employs multimodal training with mixture-of-experts adaptation to jointly optimize embodied reasoning and action generation on both standard VLM corpora and a curated 650K-sample VLA-IT dataset. On in-domain SimplerEnv tasks, InstructVLA achieves 33% improvement over SpatialVLA. To evaluate generalization, we introduce SimplerEnv-Instruct, an 80-task benchmark requiring closed-loop control and high-level instruction understanding, where it outperforms a fine-tuned OpenVLA by 96% and an action expert aided by GPT-4o by 29%. Additionally, InstructVLA surpasses baseline VLMs on multimodal tasks and exhibits inference-time scaling by leveraging textual reasoning to boost manipulation performance in both simulated and real-world settings. These results demonstrate InstructVLA's potential for bridging intuitive and steerable human-robot interaction with efficient policy learning.

## 개요
실제 세계에서 효과적으로 작동하기 위해 로봇은 다중 모드 추론과 정밀한 동작 생성을 통합해야 합니다. 그러나 기존의 시각-언어-동작(VLA) 모델은 종종 한쪽을 희생하고, 작업별 조작 데이터에 능력을 제한하며, 사전 훈련된 시각-언어 능력의 치명적 망각을 겪습니다. 이러한 격차를 해소하기 위해 우리는 InstructVLA를 소개합니다. 이는 대규모 시각-언어 모델(VLM)의 유연한 추론을 유지하면서도 체화된 추론의 도움으로 최고 수준의 조작 성능을 제공하는 종단간 VLA 모델입니다. InstructVLA는 새로운 훈련 패러다임인 시각-언어-동작 명령 튜닝(VLA-IT)을 도입하며, 이는 혼합 전문가 적응을 통한 다중 모드 훈련을 활용하여 표준 VLM 코퍼스와 선별된 65만 샘플 VLA-IT 데이터셋에서 체화된 추론과 동작 생성을 공동으로 최적화합니다. 도메인 내 SimplerEnv 작업에서 InstructVLA는 SpatialVLA 대비 33% 향상된 성능을 달성합니다. 일반화를 평가하기 위해 폐루프 제어와 고수준 명령 이해가 필요한 80개 작업 벤치마크인 SimplerEnv-Instruct를 도입했으며, 여기서 미세 조정된 OpenVLA보다 96%, GPT-4o의 지원을 받는 동작 전문가보다 29% 더 우수한 성능을 보입니다. 또한 InstructVLA는 다중 모드 작업에서 기준 VLM을 능가하며, 텍스트 추론을 활용하여 시뮬레이션 및 실제 환경 모두에서 조작 성능을 향상시키는 추론 시간 스케일링을 보여줍니다. 이러한 결과는 InstructVLA가 직관적이고 제어 가능한 인간-로봇 상호작용과 효율적인 정책 학습을 연결할 잠재력을 입증합니다.

## 핵심 내용
실제 세계에서 효과적으로 작동하기 위해 로봇은 다중 모드 추론과 정밀한 동작 생성을 통합해야 합니다. 그러나 기존의 시각-언어-동작(VLA) 모델은 종종 한쪽을 희생하고, 작업별 조작 데이터에 능력을 제한하며, 사전 훈련된 시각-언어 능력의 치명적 망각을 겪습니다. 이러한 격차를 해소하기 위해 우리는 InstructVLA를 소개합니다. 이는 대규모 시각-언어 모델(VLM)의 유연한 추론을 유지하면서도 체화된 추론의 도움으로 최고 수준의 조작 성능을 제공하는 종단간 VLA 모델입니다. InstructVLA는 새로운 훈련 패러다임인 시각-언어-동작 명령 튜닝(VLA-IT)을 도입하며, 이는 혼합 전문가 적응을 통한 다중 모드 훈련을 활용하여 표준 VLM 코퍼스와 선별된 65만 샘플 VLA-IT 데이터셋에서 체화된 추론과 동작 생성을 공동으로 최적화합니다. 도메인 내 SimplerEnv 작업에서 InstructVLA는 SpatialVLA 대비 33% 향상된 성능을 달성합니다. 일반화를 평가하기 위해 폐루프 제어와 고수준 명령 이해가 필요한 80개 작업 벤치마크인 SimplerEnv-Instruct를 도입했으며, 여기서 미세 조정된 OpenVLA보다 96%, GPT-4o의 지원을 받는 동작 전문가보다 29% 더 우수한 성능을 보입니다. 또한 InstructVLA는 다중 모드 작업에서 기준 VLM을 능가하며, 텍스트 추론을 활용하여 시뮬레이션 및 실제 환경 모두에서 조작 성능을 향상시키는 추론 시간 스케일링을 보여줍니다. 이러한 결과는 InstructVLA가 직관적이고 제어 가능한 인간-로봇 상호작용과 효율적인 정책 학습을 연결할 잠재력을 입증합니다.

## 参考
- http://arxiv.org/abs/2507.17520v2
