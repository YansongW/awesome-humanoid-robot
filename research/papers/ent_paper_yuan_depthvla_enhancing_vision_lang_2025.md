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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13375v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (967 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2510.13375v1

## 개요
기존의 비전-언어-행동 모델은 정밀한 공간 추론이 필요한 작업에서 성능이 저조한데, 이는 기본 비전 언어 모델에 내재된 공간 이해의 한계에서 비롯됩니다. 전통적인 방법은 대규모 행동 데이터 사전 훈련을 통해 이러한 결함을 보완하려 하지만, 효율성이 낮고 효과도 제한적입니다. DepthVLA는 간결하면서도 효과적인 해결책을 제시합니다: 사전 훈련된 깊이 예측 모듈을 모델에 통합하고, 혼합 Transformer 설계를 통해 비전 언어 모델, 깊이 Transformer, 행동 전문가 모듈을 완전히 공유된 어텐션 방식으로 종단 간 융합합니다. 실험 결과, 이 방법은 실제 세계 작업에서 78.5%의 성공률(기준선 65.0% 대비)을 달성했으며, LIBERO 및 Simpler 시뮬레이터에서도 각각 94.9%와 74.8%의 우수한 성능을 기록했습니다.

## 핵심 내용
### 방법 아키텍처
DepthVLA의 핵심은 세 가지 주요 구성 요소를 통합하는 혼합 Transformer 아키텍처입니다:
- **비전 언어 모델**: RGB 이미지와 언어 명령을 처리하여 기본적인 의미 이해를 제공합니다.
- **깊이 Transformer**: 사전 훈련된 깊이 예측 모듈을 통해 RGB 이미지에서 깊이 정보를 추출하고, 3차원 공간 구조를 명시적으로 인코딩합니다.
- **행동 전문가 모듈**: 융합된 비전, 언어, 깊이 특징을 기반으로 로봇 행동 명령을 직접 출력합니다.

이 세 모듈은 **완전히 공유된 어텐션 메커니즘**을 통해 종단 간 훈련되며, 깊이 정보가 추가적인 행동 데이터 사전 훈련 단계 없이도 행동 결정 과정에 원활하게 통합됩니다.

### 실험 설정 및 결과
DepthVLA는 실제 세계와 여러 시뮬레이션 환경에서 포괄적으로 평가되었습니다:
- **실제 세계 작업**: 다양한 로봇 조작 시나리오에서 DepthVLA는 **78.5%**의 작업 성공률을 달성하여 기준선 방법의 **65.0%**보다 크게 우수했습니다.
- **LIBERO 시뮬레이터**: LIBERO 벤치마크에서 DepthVLA는 **94.9%**의 성공률을 기록했으며, 기준선 방법의 **93.6%**와 비교됩니다.
- **Simpler 시뮬레이터**: 더 도전적인 Simpler 환경에서 DepthVLA는 **74.8%**의 성적으로 기준선 방법의 **58.8%**를 크게 앞질렀습니다.

### 결론
DepthVLA는 깊이를 명시적으로 도입한 공간 추론을 통해 기존 VLA 모델의 공간 이해 병목 현상을 효과적으로 해결합니다. 혼합 Transformer 설계는 훈련 효율성을 향상시킬 뿐만 아니라 다양한 작업에서 성능 돌파구를 달성했습니다. 코드는 추가 연구를 위해 오픈소스로 공개될 예정입니다.
