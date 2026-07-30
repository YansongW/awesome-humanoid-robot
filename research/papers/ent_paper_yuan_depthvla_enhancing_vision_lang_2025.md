---
$id: ent_paper_yuan_depthvla_enhancing_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning'
  zh: DepthVLA
  ko: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning'
summary:
  en: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
  zh: DepthVLA 是清华大学与 Galaxea AI 于 2025 年联合提出的大型视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于通过一个预训练的深度预测模块显式引入空间感知能力，并采用混合 Transformer 架构统一视觉语言模型、深度
    Transformer 与动作专家模块，显著提升了空间推理精度。在真实与仿真环境中，DepthVLA 均超越了现有最先进方法。
  ko: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- depthvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13375v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (arXiv)'
  url: https://arxiv.org/abs/2510.13375
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DepthVLA source
  url: https://doi.org/10.48550/arXiv.2510.13375
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的视觉-语言-动作模型在需要精确空间推理的任务中表现不佳，这主要源于其基础视觉语言模型固有的空间理解局限。传统方法依赖大量动作数据预训练来弥补这一缺陷，但效率低下且效果有限。DepthVLA 提出了一种简洁而有效的解决方案：在模型中集成一个预训练的深度预测模块，并通过混合 Transformer 设计将视觉语言模型、深度 Transformer 和动作专家模块以完全共享注意力的方式端到端融合。实验表明，该方法在真实世界任务中取得了 78.5% 的成功率（对比基线 65.0%），在 LIBERO 和 Simpler 仿真器中也分别达到了 94.9% 和 74.8% 的优异表现。

## 核心内容
### 方法架构
DepthVLA 的核心是一个混合 Transformer 架构，它统一了三个关键组件：
- **视觉语言模型**：负责处理 RGB 图像与语言指令，提供基础的语义理解。
- **深度 Transformer**：通过预训练的深度预测模块，从 RGB 图像中提取深度信息，显式编码三维空间结构。
- **动作专家模块**：基于融合后的视觉、语言与深度特征，直接输出机器人动作指令。

这三个模块通过**完全共享的注意力机制**进行端到端训练，使得深度信息能够无缝融入动作决策过程，无需额外的动作数据预训练阶段。

### 实验设置与结果
DepthVLA 在真实世界与多个仿真环境中进行了全面评估：
- **真实世界任务**：在多种机器人操作场景中，DepthVLA 取得了 **78.5%** 的任务成功率，显著优于基线方法的 **65.0%**。
- **LIBERO 仿真器**：在 LIBERO 基准测试中，DepthVLA 达到 **94.9%** 的成功率，对比基线方法的 **93.6%**。
- **Simpler 仿真器**：在更具挑战性的 Simpler 环境中，DepthVLA 以 **74.8%** 的成绩大幅领先基线方法的 **58.8%**。

### 结论
DepthVLA 通过显式引入深度感知空间推理，有效解决了现有 VLA 模型在空间理解上的瓶颈。其混合 Transformer 设计不仅提升了训练效率，还在多种任务中实现了性能突破。代码将开源以供进一步研究。

## Overview
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## 개요
Vision-Language-Action (VLA) 모델은 최근 인상적인 일반화 능력과 언어 기반 조작 능력을 보여주고 있습니다. 그러나 Vision-Language Models (VLM)로부터 물려받은 제한된 공간 추론 능력으로 인해 정밀한 공간 추론이 필요한 작업에서는 성능이 저하됩니다. 기존 VLA는 VLM을 3D 공간에 정착시키기 위해 방대한 행동 데이터 사전 학습에 의존하는데, 이는 훈련 효율성을 떨어뜨릴 뿐만 아니라 정확한 공간 이해에도 여전히 부족합니다. 본 연구에서는 사전 학습된 깊이 예측 모듈을 통해 공간 인식을 명시적으로 통합하는 간단하면서도 효과적인 VLA 아키텍처인 DepthVLA를 제시합니다. DepthVLA는 VLM, 깊이 트랜스포머, 행동 전문가를 완전히 공유된 어텐션으로 통합하는 mixture-of-transformers 설계를 채택하여 향상된 공간 추론 능력을 갖춘 종단간 모델을 형성합니다. 실제 환경과 시뮬레이션 환경 모두에서의 광범위한 평가 결과, DepthVLA는 최첨단 접근법을 능가하여 실제 작업에서 78.5% 대 65.0%, LIBERO 시뮬레이터에서 94.9% 대 93.6%, Simpler 시뮬레이터에서 74.8% 대 58.8%의 진전을 달성했습니다. 본 코드는 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 인상적인 일반화 능력과 언어 기반 조작 능력을 보여주고 있습니다. 그러나 Vision-Language Models (VLM)로부터 물려받은 제한된 공간 추론 능력으로 인해 정밀한 공간 추론이 필요한 작업에서는 성능이 저하됩니다. 기존 VLA는 VLM을 3D 공간에 정착시키기 위해 방대한 행동 데이터 사전 학습에 의존하는데, 이는 훈련 효율성을 떨어뜨릴 뿐만 아니라 정확한 공간 이해에도 여전히 부족합니다. 본 연구에서는 사전 학습된 깊이 예측 모듈을 통해 공간 인식을 명시적으로 통합하는 간단하면서도 효과적인 VLA 아키텍처인 DepthVLA를 제시합니다. DepthVLA는 VLM, 깊이 트랜스포머, 행동 전문가를 완전히 공유된 어텐션으로 통합하는 mixture-of-transformers 설계를 채택하여 향상된 공간 추론 능력을 갖춘 종단간 모델을 형성합니다. 실제 환경과 시뮬레이션 환경 모두에서의 광범위한 평가 결과, DepthVLA는 최첨단 접근법을 능가하여 실제 작업에서 78.5% 대 65.0%, LIBERO 시뮬레이터에서 94.9% 대 93.6%, Simpler 시뮬레이터에서 74.8% 대 58.8%의 진전을 달성했습니다. 본 코드는 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2510.13375v1
