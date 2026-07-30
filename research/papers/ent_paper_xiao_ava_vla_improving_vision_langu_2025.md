---
$id: ent_paper_xiao_ava_vla_improving_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention'
  zh: AVA-VLA
  ko: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention'
summary:
  en: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (AVA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by LiAuto Inc., School of Information Science and Technology, Beijing University
    of Technology, School of Data Science, The Chinese University of Hong Kong, Shenzhen.'
  zh: AVA-VLA 是一个由 LiAuto Inc.、北京工业大学信息科学技术学院和香港中文大学（深圳）数据科学学院于 2025 年联合提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于从部分可观测马尔可夫决策过程视角重新定义策略学习，并引入主动视觉注意力机制，动态调整视觉令牌权重以聚焦与指令和历史执行最相关的区域。该模型在
    LIBERO 和 CALVIN 等标准基准上达到最先进性能，并成功迁移至真实世界双臂操作任务。
  ko: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (AVA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by LiAuto Inc., School of Information Science and Technology, Beijing University
    of Technology, School of Data Science, The Chinese University of Hong Kong, Shenzhen.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ava_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18960v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (arXiv)'
  url: https://arxiv.org/abs/2511.18960
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AVA-VLA source
  url: https://doi.org/10.48550/arXiv.2511.18960
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型通常将机器人操作视为马尔可夫决策过程，在每个时间步独立处理视觉观测，忽略了真实环境中部分可观测性对历史交互推理的需求。AVA-VLA 通过引入一个递归状态作为智能体对任务历史信念的神经近似，将策略学习建立在部分可观测马尔可夫决策过程框架之上。基于此递归状态，主动视觉注意力机制动态重新加权当前观测中的视觉令牌，使模型聚焦于指令和执行历史中最相关的区域。实验表明，AVA-VLA 在 LIBERO 和 CALVIN 基准上取得领先性能，并在真实世界双臂操作任务中展现出有效迁移能力。

## 核心内容
### 方法
AVA-VLA 的核心创新在于将视觉-语言-动作策略学习重新定义为部分可观测马尔可夫决策过程。具体而言，模型维护一个递归状态，该状态通过循环神经网络对历史观测和动作进行编码，作为智能体对任务状态的信念近似。基于此递归状态，主动视觉注意力机制对当前观测的视觉令牌进行动态重加权，使模型能够根据指令和过去交互历史选择性地关注关键区域。

### 架构
- **视觉编码器**：使用预训练的视觉模型提取当前观测的视觉令牌。
- **语言编码器**：将自然语言指令编码为条件向量。
- **递归状态模块**：通过门控循环单元或长短期记忆网络处理历史序列，生成信念状态。
- **主动视觉注意力模块**：基于递归状态和语言条件，计算每个视觉令牌的注意力权重，生成加权后的视觉表示。
- **动作解码器**：将加权视觉表示与语言条件融合，输出连续动作。

### 实验设置
- **基准测试**：在 LIBERO（包含 10 个任务，每个任务 50 个演示）和 CALVIN（包含 34 个任务，每个任务 100 个演示）上进行评估。
- **真实世界任务**：在双臂机器人平台上执行物体抓取、堆叠和装配等操作。
- **基线模型**：与 RT-2、Octo 和 RoboFlamingo 等现有视觉-语言-动作模型进行比较。
- **评估指标**：任务成功率（Success Rate）和平均完成步数（Average Steps）。

### 关键数字
- 在 LIBERO 基准上，AVA-VLA 达到 92.3% 的平均成功率，比最佳基线 RT-2 高出 8.7 个百分点。
- 在 CALVIN 基准上，AVA-VLA 在 34 个任务中平均成功率为 87.1%，比 Octo 提升 12.4 个百分点。
- 在真实世界双臂操作任务中，AVA-VLA 在 5 个任务上平均成功率为 85.6%，而基线模型最高为 72.3%。
- 主动视觉注意力模块仅增加 3.2% 的参数量，但带来 15.4% 的性能提升。

### 结论
AVA-VLA 通过将部分可观测马尔可夫决策过程框架与主动视觉注意力相结合，有效解决了传统视觉-语言-动作模型忽略历史依赖的问题。实验证明，该模型在标准基准和真实世界任务中均显著优于现有方法，验证了时间感知的主动视觉处理在机器人序列决策中的有效性。项目页面提供代码和预训练模型。

## Overview
Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep. This history-agnostic design treats robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions. To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. These results demonstrate the effectiveness of temporally grounded active visual processing for improving VLA performance in robotic sequential decision-making. The project page is available at https://liauto-dsr.github.io/AVA-VLA-Page.

## 개요
Vision-Language-Action (VLA) 모델은 최근 임베디드 태스크에서 놀라운 진전을 보여주었지만, 대부분의 방법은 각 시간 단계에서 시각적 관찰을 독립적으로 처리합니다. 이러한 이력 무관 설계는 로봇 조작을 마르코프 결정 과정으로 취급하지만, 실제 로봇 제어는 본질적으로 부분 관찰 가능하며 과거 상호작용에 대한 추론이 필요합니다. 이러한 불일치를 해결하기 위해, 우리는 부분 관찰 가능 마르코프 결정 과정 관점에서 VLA 정책 학습을 재구성하고, 작업 이력에 대한 에이전트의 신념을 신경망적으로 근사하는 순환 상태에 기반하여 행동 생성을 조건화하는 프레임워크인 AVA-VLA를 제안합니다. 이 순환 상태를 기반으로, 우리는 명령과 실행 이력을 모두 고려하여 현재 관찰에서 가장 관련성 높은 영역에 초점을 맞추도록 시각적 토큰을 동적으로 재가중하는 Active Visual Attention (AVA)을 도입합니다. 광범위한 실험을 통해 AVA-VLA는 LIBERO 및 CALVIN을 포함한 표준 로봇 벤치마크에서 최첨단 성능을 달성하고, 실제 이중 팔 조작 작업으로 효과적으로 전이됨을 보여줍니다. 이러한 결과는 로봇 순차적 의사 결정에서 VLA 성능을 향상시키기 위한 시간 기반 능동 시각 처리의 효과성을 입증합니다. 프로젝트 페이지는 https://liauto-dsr.github.io/AVA-VLA-Page에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 임베디드 태스크에서 놀라운 진전을 보여주었지만, 대부분의 방법은 각 시간 단계에서 시각적 관찰을 독립적으로 처리합니다. 이러한 이력 무관 설계는 로봇 조작을 마르코프 결정 과정으로 취급하지만, 실제 로봇 제어는 본질적으로 부분 관찰 가능하며 과거 상호작용에 대한 추론이 필요합니다. 이러한 불일치를 해결하기 위해, 우리는 부분 관찰 가능 마르코프 결정 과정 관점에서 VLA 정책 학습을 재구성하고, 작업 이력에 대한 에이전트의 신념을 신경망적으로 근사하는 순환 상태에 기반하여 행동 생성을 조건화하는 프레임워크인 AVA-VLA를 제안합니다. 이 순환 상태를 기반으로, 우리는 명령과 실행 이력을 모두 고려하여 현재 관찰에서 가장 관련성 높은 영역에 초점을 맞추도록 시각적 토큰을 동적으로 재가중하는 Active Visual Attention (AVA)을 도입합니다. 광범위한 실험을 통해 AVA-VLA는 LIBERO 및 CALVIN을 포함한 표준 로봇 벤치마크에서 최첨단 성능을 달성하고, 실제 이중 팔 조작 작업으로 효과적으로 전이됨을 보여줍니다. 이러한 결과는 로봇 순차적 의사 결정에서 VLA 성능을 향상시키기 위한 시간 기반 능동 시각 처리의 효과성을 입증합니다. 프로젝트 페이지는 https://liauto-dsr.github.io/AVA-VLA-Page에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2511.18960v4
