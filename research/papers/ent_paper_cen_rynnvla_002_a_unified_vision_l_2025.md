---
$id: ent_paper_cen_rynnvla_002_a_unified_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RynnVLA-002: A Unified Vision-Language-Action and World Model'
  zh: RynnVLA-002
  ko: 'RynnVLA-002: A Unified Vision-Language-Action and World Model'
summary:
  en: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
  zh: RynnVLA-002 是由阿里巴巴达摩院、湖畔实验室和浙江大学于 2025 年联合提出的大型视觉-语言-动作与统一世界模型，专为机器人操作任务设计。其核心贡献在于将 VLA 模型与世界模型融合，通过联合学习环境动力学与动作规划实现双向增强。实验表明，该模型在
    LIBERO 仿真基准上达到 97.4% 的成功率，并在真实 LeRobot 任务中将成功率提升 50%。
  ko: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- rynnvla_002
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.17502v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (arXiv)'
  url: https://arxiv.org/abs/2511.17502
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RynnVLA-002 source
  url: https://doi.org/10.48550/arXiv.2511.17502
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
RynnVLA-002 创新性地统一了视觉-语言-动作模型与世界模型，形成双向增强的闭环架构。世界模型利用动作与视觉输入预测未来图像状态，学习环境物理规律以优化动作生成；而 VLA 模型则从图像观测中产生后续动作，增强视觉理解并辅助世界模型的图像生成。这种联合框架使模型能同时掌握环境动态与动作规划，在仿真与真实机器人任务中均展现出显著优势。

## 核心内容
### 方法架构
RynnVLA-002 的核心是统一框架，包含两个相互增强的模块：
- **世界模型**：接收动作与视觉输入，预测未来图像状态，通过学习环境底层物理规律来优化动作生成。
- **VLA 模型**：从图像观测中生成后续动作，增强视觉理解能力，同时为世界模型的图像生成提供支持。

### 实验设置
- **仿真环境**：在 LIBERO 基准上进行评估，无需预训练。
- **真实环境**：在 LeRobot 平台上开展真实机器人操作实验。

### 关键结果
- **LIBERO 仿真基准**：RynnVLA-002 达到 97.4% 的成功率，超越单独的 VLA 模型与世界模型。
- **LeRobot 真实实验**：集成世界模型后，整体成功率提升 50%，验证了双向增强机制的有效性。

### 结论
RynnVLA-002 证明了 VLA 模型与世界模型的联合学习能显著提升机器人操作性能，为未来机器人智能系统提供了统一框架的新范式。

## Overview
We introduce RynnVLA-002, a unified Vision-Language-Action (VLA) and world model. The world model leverages action and visual inputs to predict future image states, learning the underlying physics of the environment to refine action generation. Conversely, the VLA model produces subsequent actions from image observations, enhancing visual understanding and supporting the world model's image generation. The unified framework of RynnVLA-002 enables joint learning of environmental dynamics and action planning. Our experiments show that RynnVLA-002 surpasses individual VLA and world models, demonstrating their mutual enhancement. We evaluate RynnVLA-002 in both simulation and real-world robot tasks. RynnVLA-002 achieves 97.4% success rate on the LIBERO simulation benchmark without pretraining, while in real-world LeRobot experiments, its integrated world model boosts the overall success rate by 50%.

## 개요
우리는 통합된 Vision-Language-Action(VLA) 및 세계 모델인 RynnVLA-002를 소개합니다. 세계 모델은 행동과 시각적 입력을 활용하여 미래 이미지 상태를 예측하고, 환경의 물리적 원리를 학습하여 행동 생성을 개선합니다. 반대로, VLA 모델은 이미지 관찰로부터 후속 행동을 생성하여 시각적 이해를 향상시키고 세계 모델의 이미지 생성을 지원합니다. RynnVLA-002의 통합 프레임워크는 환경 역학과 행동 계획의 공동 학습을 가능하게 합니다. 우리의 실험은 RynnVLA-002가 개별 VLA 및 세계 모델을 능가하며, 이들이 상호 보완적으로 향상됨을 보여줍니다. 우리는 시뮬레이션 및 실제 로봇 작업 모두에서 RynnVLA-002를 평가합니다. RynnVLA-002는 사전 학습 없이 LIBERO 시뮬레이션 벤치마크에서 97.4%의 성공률을 달성했으며, 실제 LeRobot 실험에서는 통합된 세계 모델이 전체 성공률을 50% 향상시켰습니다.

## 핵심 내용
우리는 통합된 Vision-Language-Action(VLA) 및 세계 모델인 RynnVLA-002를 소개합니다. 세계 모델은 행동과 시각적 입력을 활용하여 미래 이미지 상태를 예측하고, 환경의 물리적 원리를 학습하여 행동 생성을 개선합니다. 반대로, VLA 모델은 이미지 관찰로부터 후속 행동을 생성하여 시각적 이해를 향상시키고 세계 모델의 이미지 생성을 지원합니다. RynnVLA-002의 통합 프레임워크는 환경 역학과 행동 계획의 공동 학습을 가능하게 합니다. 우리의 실험은 RynnVLA-002가 개별 VLA 및 세계 모델을 능가하며, 이들이 상호 보완적으로 향상됨을 보여줍니다. 우리는 시뮬레이션 및 실제 로봇 작업 모두에서 RynnVLA-002를 평가합니다. RynnVLA-002는 사전 학습 없이 LIBERO 시뮬레이션 벤치마크에서 97.4%의 성공률을 달성했으며, 실제 LeRobot 실험에서는 통합된 세계 모델이 전체 성공률을 50% 향상시켰습니다.

## 参考
- http://arxiv.org/abs/2511.17502v3
