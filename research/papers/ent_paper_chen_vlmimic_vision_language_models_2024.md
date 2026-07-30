---
$id: ent_paper_chen_vlmimic_vision_language_models_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions'
  zh: VLMimic
  ko: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions'
summary:
  en: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (VLMimic), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Beijing Institute of Technology, The University of Hong Kong, Peking University,
    and published at NIPS24.'
  zh: VLMimic 是 2024 年由北京理工大学、香港大学和北京大学联合提出的视觉-语言-动作大模型，发表于 NIPS24。其核心贡献在于利用视觉语言模型直接从少量人类视频中学习细粒度动作级技能，无需预定义运动基元，在 RLBench
    和真实操作任务中分别提升超过 27% 和 21%。
  ko: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (VLMimic), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Beijing Institute of Technology, The University of Hong Kong, Peking University,
    and published at NIPS24.'
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
- vision_language_action
- vla
- vlmimic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.20927v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: VLMimic source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/8e6f3d53b2bef98fce17e699557f5f11-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
VLMimic 针对当前视觉模仿学习方法依赖预定义运动基元执行物理交互的瓶颈，提出了一种新范式。该方法首先从人类视频中提取以物体为中心的运动信息，然后通过层级约束表示学习技能，从而在仅有少量人类视频的情况下推导出细粒度动作级技能。这些技能通过迭代比较策略进行精炼和更新，能够高效适应未见过的环境。实验表明，仅使用 5 段人类视频，VLMimic 在 RLBench 和真实世界操作任务中分别取得了超过 27% 和 21% 的显著提升，在长时域任务中超越基线方法超过 37%。

## 核心内容
### 方法架构
VLMimic 的核心框架包含两个关键阶段：
- **以物体为中心的运动提取**：首先从人类视频中解析出与物体交互相关的运动轨迹，将视觉信息转化为可学习的运动表征。
- **层级约束表示学习**：通过构建层级约束（如物体空间关系、运动时序约束），从有限的人类演示中推导出细粒度动作级技能，避免了对大量数据或预定义运动基元的依赖。

### 技能精炼与适应
- **迭代比较策略**：通过对比不同技能版本在模拟或真实环境中的执行效果，自动筛选并更新最优技能表征，使模型能高效适应新环境中的物体位置、形状或光照变化。

### 实验设置与关键结果
- **数据集与基准**：在 RLBench 模拟基准和真实世界操作任务上进行评估，使用仅 5 段人类视频作为训练数据。
- **性能提升**：
  - 在 RLBench 任务中，VLMimic 相比基线方法（如使用预定义运动基元的 VIL 方法）平均提升超过 27%。
  - 在真实世界操作任务中，平均提升超过 21%。
  - 在长时域任务（如多步骤物体组装）中，成功率超越基线方法超过 37%。
- **消融实验**：验证了层级约束表示和迭代比较策略的贡献，移除任一模块均导致性能显著下降。

## Overview
Visual imitation learning (VIL) provides an efficient and intuitive strategy for robotic systems to acquire novel skills. Recent advancements in Vision Language Models (VLMs) have demonstrated remarkable performance in vision and language reasoning capabilities for VIL tasks. Despite the progress, current VIL methods naively employ VLMs to learn high-level plans from human videos, relying on pre-defined motion primitives for executing physical interactions, which remains a major bottleneck. In this work, we present VLMimic, a novel paradigm that harnesses VLMs to directly learn even fine-grained action levels, only given a limited number of human videos. Specifically, VLMimic first grounds object-centric movements from human videos, and learns skills using hierarchical constraint representations, facilitating the derivation of skills with fine-grained action levels from limited human videos. These skills are refined and updated through an iterative comparison strategy, enabling efficient adaptation to unseen environments. Our extensive experiments exhibit that our VLMimic, using only 5 human videos, yields significant improvements of over 27% and 21% in RLBench and real-world manipulation tasks, and surpasses baselines by over 37% in long-horizon tasks.

## 개요
시각적 모방 학습(VIL)은 로봇 시스템이 새로운 기술을 습득하기 위한 효율적이고 직관적인 전략을 제공합니다. 최근 비전 언어 모델(VLM)의 발전은 VIL 작업에서 뛰어난 시각 및 언어 추론 능력을 입증했습니다. 이러한 진전에도 불구하고, 현재의 VIL 방법은 인간 비디오에서 고수준 계획을 학습하기 위해 VLM을 단순히 사용하며, 물리적 상호작용 실행을 위해 미리 정의된 동작 프리미티브에 의존하는데, 이는 여전히 주요 병목 현상으로 남아 있습니다. 본 연구에서는 제한된 수의 인간 비디오만 주어졌을 때, VLM을 활용하여 세분화된 행동 수준까지 직접 학습하는 새로운 패러다임인 VLMimic을 제시합니다. 구체적으로, VLMimic은 먼저 인간 비디오에서 객체 중심 움직임을 파악하고, 계층적 제약 표현을 사용하여 기술을 학습함으로써, 제한된 인간 비디오에서 세분화된 행동 수준의 기술을 도출할 수 있게 합니다. 이러한 기술은 반복적 비교 전략을 통해 정제 및 업데이트되어, 보지 못한 환경에 효율적으로 적응할 수 있습니다. 광범위한 실험을 통해, 단 5개의 인간 비디오만 사용한 VLMimic이 RLBench 및 실제 조작 작업에서 27% 이상 및 21% 이상의 유의미한 성능 향상을 보였으며, 장기 작업에서는 기준선을 37% 이상 능가함을 입증했습니다.

## 핵심 내용
시각적 모방 학습(VIL)은 로봇 시스템이 새로운 기술을 습득하기 위한 효율적이고 직관적인 전략을 제공합니다. 최근 비전 언어 모델(VLM)의 발전은 VIL 작업에서 뛰어난 시각 및 언어 추론 능력을 입증했습니다. 이러한 진전에도 불구하고, 현재의 VIL 방법은 인간 비디오에서 고수준 계획을 학습하기 위해 VLM을 단순히 사용하며, 물리적 상호작용 실행을 위해 미리 정의된 동작 프리미티브에 의존하는데, 이는 여전히 주요 병목 현상으로 남아 있습니다. 본 연구에서는 제한된 수의 인간 비디오만 주어졌을 때, VLM을 활용하여 세분화된 행동 수준까지 직접 학습하는 새로운 패러다임인 VLMimic을 제시합니다. 구체적으로, VLMimic은 먼저 인간 비디오에서 객체 중심 움직임을 파악하고, 계층적 제약 표현을 사용하여 기술을 학습함으로써, 제한된 인간 비디오에서 세분화된 행동 수준의 기술을 도출할 수 있게 합니다. 이러한 기술은 반복적 비교 전략을 통해 정제 및 업데이트되어, 보지 못한 환경에 효율적으로 적응할 수 있습니다. 광범위한 실험을 통해, 단 5개의 인간 비디오만 사용한 VLMimic이 RLBench 및 실제 조작 작업에서 27% 이상 및 21% 이상의 유의미한 성능 향상을 보였으며, 장기 작업에서는 기준선을 37% 이상 능가함을 입증했습니다.

## 参考
- http://arxiv.org/abs/2410.20927v3
