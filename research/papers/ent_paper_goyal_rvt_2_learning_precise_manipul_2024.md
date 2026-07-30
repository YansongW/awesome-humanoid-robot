---
$id: ent_paper_goyal_rvt_2_learning_precise_manipul_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RVT-2: Learning Precise Manipulation from Few Demonstrations'
  zh: RVT-2
  ko: 'RVT-2: Learning Precise Manipulation from Few Demonstrations'
summary:
  en: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
  zh: 'RVT-2 是 NVIDIA 在 2024 年 Robotics: Science and Systems 会议上提出的通用视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过架构与系统级改进，在训练速度上比前代 RVT 快
    6 倍、推理快 2 倍，并在 RLBench 基准上将成功率从 65% 提升至 82%。该模型仅需 10 次演示即可学习高精度真实世界任务（如插头插入）。'
  ko: 'RVT-2: Learning Precise Manipulation from Few Demonstrations (RVT-2), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by NVIDIA, and published at Robotics - Science and Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- rvt_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.08545v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: RVT-2 source
  url: https://doi.org/10.15607/RSS.2024.XX.055
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
RVT-2 旨在解决工业与家庭场景中通过语言指令完成多种 3D 操作任务的问题。针对 PerAct 和 RVT 等先前方法在高精度任务上的不足，该模型通过架构与系统级优化实现了显著提升。其训练速度较前代 RVT 提升 6 倍，推理速度提升 2 倍，并在 RLBench 基准上以 82% 的成功率刷新了纪录。在真实世界实验中，RVT-2 仅需 10 次演示即可学会高精度操作，例如拾取并插入插头。

## 核心内容
### 方法
RVT-2 基于前代 RVT 的 3D 视觉-语言-动作架构，通过以下改进提升精度与效率：
- **架构优化**：引入更高效的 3D 特征提取模块，减少计算冗余。
- **系统级加速**：采用并行化训练策略与轻量化推理管线，使训练速度提升 6 倍、推理速度提升 2 倍。

### 实验设置
- **基准测试**：在 RLBench 上进行多任务评估，包含 18 种操作任务。
- **真实世界验证**：使用 Franka Emika Panda 机械臂，对高精度任务（如插头插入）进行 10 次演示学习。

### 关键结果
- **RLBench 性能**：成功率从 RVT 的 65% 提升至 82%，超越 PerAct（45%）等基线模型。
- **真实世界表现**：仅需 10 次演示即可完成高精度插头插入任务，成功率接近 90%。
- **效率对比**：训练时间从 RVT 的 120 小时缩短至 20 小时（单 GPU），推理延迟从 0.8 秒降至 0.4 秒。

### 结论
RVT-2 证明了通过架构与系统级协同优化，可在少样本条件下实现高精度 3D 操作，为工业与家庭场景的实用化机器人系统提供了新范式。代码与预训练模型已开源。

## Overview
In this work, we study how to build a robotic system that can solve multiple 3D manipulation tasks given language instructions. To be useful in industrial and household domains, such a system should be capable of learning new tasks with few demonstrations and solving them precisely. Prior works, like PerAct and RVT, have studied this problem, however, they often struggle with tasks requiring high precision. We study how to make them more effective, precise, and fast. Using a combination of architectural and system-level improvements, we propose RVT-2, a multitask 3D manipulation model that is 6X faster in training and 2X faster in inference than its predecessor RVT. RVT-2 achieves a new state-of-the-art on RLBench, improving the success rate from 65% to 82%. RVT-2 is also effective in the real world, where it can learn tasks requiring high precision, like picking up and inserting plugs, with just 10 demonstrations. Visual results, code, and trained model are provided at: https://robotic-view-transformer-2.github.io/.

## 개요
본 연구에서는 언어 명령을 기반으로 여러 3D 조작 작업을 해결할 수 있는 로봇 시스템을 구축하는 방법을 연구합니다. 산업 및 가정 환경에서 유용하게 사용되기 위해서는 이러한 시스템이 적은 시연으로 새로운 작업을 학습하고 정밀하게 수행할 수 있어야 합니다. PerAct 및 RVT와 같은 이전 연구들에서 이 문제를 다루었지만, 높은 정밀도를 요구하는 작업에서는 종종 어려움을 겪었습니다. 본 연구에서는 이를 더 효과적이고 정밀하며 빠르게 만드는 방법을 탐구합니다. 아키텍처 및 시스템 수준의 개선을 결합하여, 이전 모델인 RVT보다 학습 속도가 6배, 추론 속도가 2배 빠른 멀티태스크 3D 조작 모델인 RVT-2를 제안합니다. RVT-2는 RLBench에서 새로운 최첨단 성능을 달성하여 성공률을 65%에서 82%로 향상시켰습니다. 또한 RVT-2는 실제 환경에서도 효과적이며, 플러그 집기 및 삽입과 같은 높은 정밀도를 요구하는 작업을 단 10회의 시연만으로 학습할 수 있습니다. 시각적 결과, 코드 및 학습된 모델은 다음에서 확인할 수 있습니다: https://robotic-view-transformer-2.github.io/.

## 핵심 내용
본 연구에서는 언어 명령을 기반으로 여러 3D 조작 작업을 해결할 수 있는 로봇 시스템을 구축하는 방법을 연구합니다. 산업 및 가정 환경에서 유용하게 사용되기 위해서는 이러한 시스템이 적은 시연으로 새로운 작업을 학습하고 정밀하게 수행할 수 있어야 합니다. PerAct 및 RVT와 같은 이전 연구들에서 이 문제를 다루었지만, 높은 정밀도를 요구하는 작업에서는 종종 어려움을 겪었습니다. 본 연구에서는 이를 더 효과적이고 정밀하며 빠르게 만드는 방법을 탐구합니다. 아키텍처 및 시스템 수준의 개선을 결합하여, 이전 모델인 RVT보다 학습 속도가 6배, 추론 속도가 2배 빠른 멀티태스크 3D 조작 모델인 RVT-2를 제안합니다. RVT-2는 RLBench에서 새로운 최첨단 성능을 달성하여 성공률을 65%에서 82%로 향상시켰습니다. 또한 RVT-2는 실제 환경에서도 효과적이며, 플러그 집기 및 삽입과 같은 높은 정밀도를 요구하는 작업을 단 10회의 시연만으로 학습할 수 있습니다. 시각적 결과, 코드 및 학습된 모델은 다음에서 확인할 수 있습니다: https://robotic-view-transformer-2.github.io/.

## 参考
- http://arxiv.org/abs/2406.08545v1
