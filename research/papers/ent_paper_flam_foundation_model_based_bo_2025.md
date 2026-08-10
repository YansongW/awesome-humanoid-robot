---
$id: ent_paper_flam_foundation_model_based_bo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
  zh: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
  ko: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
summary:
  en: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: FLAM 是 2025 年提出的一种基于基础模型的人形机器人全身控制方法，由研究团队开发。其核心贡献在于将稳定性奖励函数与基础策略结合，通过人体运动重建模型计算姿态稳定性，显著提升了人形机器人在 locomotion 和 manipulation
    任务中的学习效率与性能。
  ko: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flam
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22249v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (767 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2503.22249
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有强化学习方法在控制人形机器人全身时，往往忽视身体稳定性对 locomotion 和 manipulation 的影响，导致任务奖励驱动的策略难以达到高性能。FLAM 通过引入一个稳定性奖励函数，将机器人姿态映射到 3D 虚拟人体模型，再利用人体运动重建模型进行稳定化与重构，最终基于重构前后的姿态差异计算奖励。该奖励与任务奖励共同指导策略学习，在 benchmark 测试中，FLAM 超越了当前最先进的强化学习方法，验证了其在提升稳定性和整体性能方面的有效性。

## 核心内容
### 方法概述
FLAM 的核心框架包含两个关键组件：
- **稳定性奖励函数**：设计用于鼓励机器人学习稳定姿态，加速学习过程并促进任务完成。
- **基础策略**：与稳定性奖励结合，共同优化策略学习。

### 具体实现流程
1. **姿态映射**：将机器人当前姿态映射到 3D 虚拟人体模型。
2. **姿态稳定与重构**：通过人体运动重建模型对映射后的人体姿态进行稳定化处理，生成重构后的姿态。
3. **奖励计算**：基于重构前后的姿态差异计算稳定性奖励，并与任务奖励结合形成最终奖励信号。

### 实验设置与结果
- **基准测试**：在标准人形机器人 benchmark 上进行评估。
- **对比方法**：与当前最先进的强化学习方法（state-of-the-art RL methods）进行对比。
- **关键结果**：FLAM 在稳定性和整体性能上均优于对比方法，具体表现为任务完成率提升和姿态控制更平稳。

### 结论
FLAM 通过显式引入稳定性奖励，有效解决了 RL 方法在全身控制中忽视身体稳定性的问题，为人形机器人的 locomotion 和 manipulation 任务提供了更高效的解决方案。

## Overview
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## 参考
- http://arxiv.org/abs/2503.22249v1

## 개요
기존 강화학습 방법은 휴머노이드 로봇의 전신 제어 시 신체 안정성이 locomotion 및 manipulation에 미치는 영향을 간과하는 경우가 많아, 작업 보상 기반 정책이 높은 성능을 달성하기 어렵습니다. FLAM은 안정성 보상 함수를 도입하여 로봇 자세를 3D 가상 인체 모델에 매핑하고, 인체 동작 재구성 모델을 활용해 안정화 및 재구성을 수행한 뒤, 재구성 전후의 자세 차이를 기반으로 보상을 계산합니다. 이 보상은 작업 보상과 함께 정책 학습을 안내하며, 벤치마크 테스트에서 FLAM은 현재 최첨단 강화학습 방법을 능가하여 안정성 및 전반적 성능 향상에 효과적임을 입증했습니다.

## 핵심 내용
### 방법 개요
FLAM의 핵심 프레임워크는 두 가지 주요 구성 요소를 포함합니다:
- **안정성 보상 함수**: 로봇이 안정적인 자세를 학습하도록 장려하여 학습 과정을 가속화하고 작업 완료를 촉진하도록 설계되었습니다.
- **기본 정책**: 안정성 보상과 결합하여 정책 학습을 공동으로 최적화합니다.

### 구체적 구현 절차
1. **자세 매핑**: 로봇의 현재 자세를 3D 가상 인체 모델에 매핑합니다.
2. **자세 안정화 및 재구성**: 인체 동작 재구성 모델을 통해 매핑된 인체 자세를 안정화 처리하고, 재구성된 자세를 생성합니다.
3. **보상 계산**: 재구성 전후의 자세 차이를 기반으로 안정성 보상을 계산하고, 작업 보상과 결합하여 최종 보상 신호를 형성합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: 표준 휴머노이드 로봇 벤치마크에서 평가를 수행합니다.
- **비교 방법**: 현재 최첨단 강화학습 방법(state-of-the-art RL methods)과 비교합니다.
- **주요 결과**: FLAM은 안정성 및 전반적 성능에서 비교 방법보다 우수하며, 구체적으로 작업 완료율 향상과 자세 제어의 안정성 증가로 나타납니다.

### 결론
FLAM은 안정성 보상을 명시적으로 도입하여 RL 방법이 전신 제어에서 신체 안정성을 간과하는 문제를 효과적으로 해결하며, 휴머노이드 로봇의 locomotion 및 manipulation 작업에 더 효율적인 솔루션을 제공합니다.
