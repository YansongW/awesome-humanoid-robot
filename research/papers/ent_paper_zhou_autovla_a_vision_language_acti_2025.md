---
$id: ent_paper_zhou_autovla_a_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning'
  zh: AutoVLA
  ko: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning'
summary:
  en: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (AutoVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by University
    of California, Los Angeles, and published at NIPS25.'
  zh: AutoVLA 是加州大学洛杉矶分校在 NIPS25 提出的端到端自动驾驶视觉-语言-动作模型。其核心贡献在于将连续轨迹离散化为可行动作，并引入双思维模式（快速/慢速推理）与基于 GRPO 的强化微调方法，在 nuPlan、nuScenes、Waymo
    和 CARLA 等基准上取得竞争性表现。
  ko: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (AutoVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by University
    of California, Los Angeles, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autovla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.13757v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (700 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement
    Fine-Tuning (arXiv)'
  url: https://arxiv.org/abs/2506.13757
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AutoVLA source
  url: https://doi.org/10.48550/arXiv.2506.13757
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
AutoVLA 通过单一自回归生成模型统一了语义推理与动作生成，直接从原始视觉输入和语言指令进行轨迹规划。该模型将连续轨迹离散化为离散动作，使其能无缝集成到语言模型中。训练阶段采用监督微调赋予模型双思维模式：仅输出轨迹的快速推理，以及结合思维链的慢速推理。为提升规划效率，AutoVLA 引入基于 Group Relative Policy Optimization (GRPO) 的强化微调方法，在简单场景中减少不必要的推理步骤。

## 核心内容
### 方法架构
- **统一生成框架**：AutoVLA 将推理与动作生成整合为单一自回归模型，输入为原始视觉数据与语言指令，直接输出语义推理结果与轨迹规划。
- **动作离散化**：将连续轨迹通过 tokenization 转化为离散可行动作，使动作序列可直接嵌入语言模型输出空间。

### 训练策略
- **双思维模式**：通过监督微调实现两种推理模式：
  - **快速推理**：仅输出轨迹 token，适用于简单场景。
  - **慢速推理**：结合思维链 (Chain-of-Thought) 进行逐步推理，适用于复杂场景。
- **强化微调**：基于 GRPO 的强化学习方法，在简单场景中抑制不必要的长推理，提升规划效率与性能。

### 实验设置与结果
- **数据集与基准**：在 nuPlan、nuScenes、Waymo 和 CARLA 上评估，涵盖开环与闭环设置。
- **关键表现**：在开环与闭环场景中均展现竞争性性能，定性结果验证了自适应推理能力（如根据场景复杂度动态切换推理模式）与精确轨迹规划能力。

## Overview
Recent advancements in Vision-Language-Action (VLA) models have shown promise for end-to-end autonomous driving by leveraging world knowledge and reasoning capabilities. However, current VLA models often struggle with physically infeasible action outputs, complex model structures, or unnecessarily long reasoning. In this paper, we propose AutoVLA, a novel VLA model that unifies reasoning and action generation within a single autoregressive generation model for end-to-end autonomous driving. AutoVLA performs semantic reasoning and trajectory planning directly from raw visual inputs and language instructions. We tokenize continuous trajectories into discrete, feasible actions, enabling direct integration into the language model. For training, we employ supervised fine-tuning to equip the model with dual thinking modes: fast thinking (trajectory-only) and slow thinking (enhanced with chain-of-thought reasoning). To further enhance planning performance and efficiency, we introduce a reinforcement fine-tuning method based on Group Relative Policy Optimization (GRPO), reducing unnecessary reasoning in straightforward scenarios. Extensive experiments across real-world and simulated datasets and benchmarks, including nuPlan, nuScenes, Waymo, and CARLA, demonstrate the competitive performance of AutoVLA in both open-loop and closed-loop settings. Qualitative results showcase the adaptive reasoning and accurate planning capabilities of AutoVLA in diverse scenarios.

## 参考
- http://arxiv.org/abs/2506.13757v3

## 개요
AutoVLA는 단일 자기회귀 생성 모델을 통해 의미 추론과 행동 생성을 통합하며, 원시 시각 입력과 언어 명령으로부터 직접 궤적 계획을 수행합니다. 이 모델은 연속 궤적을 이산 행동으로 이산화하여 언어 모델에 원활하게 통합할 수 있게 합니다. 훈련 단계에서는 지도 미세 조정을 통해 모델에 이중 사고 모드를 부여합니다: 궤적만 출력하는 빠른 추론과 사고 사슬을 결합한 느린 추론입니다. 계획 효율성을 높이기 위해 AutoVLA는 Group Relative Policy Optimization (GRPO) 기반의 강화 미세 조정 방법을 도입하여 단순한 시나리오에서 불필요한 추론 단계를 줄입니다.

## 핵심 내용
### 방법 아키텍처
- **통합 생성 프레임워크**: AutoVLA는 추론과 행동 생성을 단일 자기회귀 모델로 통합하며, 입력은 원시 시각 데이터와 언어 명령이고, 출력은 직접 의미 추론 결과와 궤적 계획입니다.
- **행동 이산화**: 연속 궤적을 토큰화를 통해 이산 실행 가능한 행동으로 변환하여, 행동 시퀀스를 언어 모델 출력 공간에 직접 삽입할 수 있게 합니다.

### 훈련 전략
- **이중 사고 모드**: 지도 미세 조정을 통해 두 가지 추론 모드를 구현합니다:
  - **빠른 추론**: 궤적 토큰만 출력하며, 단순한 시나리오에 적합합니다.
  - **느린 추론**: 사고 사슬(Chain-of-Thought)을 결합하여 단계적으로 추론하며, 복잡한 시나리오에 적합합니다.
- **강화 미세 조정**: GRPO 기반의 강화 학습 방법으로, 단순한 시나리오에서 불필요한 긴 추론을 억제하여 계획 효율성과 성능을 향상시킵니다.

### 실험 설정 및 결과
- **데이터셋 및 벤치마크**: nuPlan, nuScenes, Waymo 및 CARLA에서 평가하며, 개루프 및 폐루프 설정을 모두 포함합니다.
- **주요 성과**: 개루프 및 폐루프 시나리오 모두에서 경쟁력 있는 성능을 보였으며, 정성적 결과는 적응형 추론 능력(예: 시나리오 복잡도에 따라 추론 모드를 동적으로 전환)과 정밀한 궤적 계획 능력을 검증합니다.
