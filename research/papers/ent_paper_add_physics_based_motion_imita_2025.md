---
$id: ent_paper_add_physics_based_motion_imita_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
  zh: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
  ko: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
summary:
  en: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: ADD 是 2025 年提出的一种基于物理的角色动画方法，用于人形机器人的运动模仿。其核心贡献在于提出对抗性差分判别器（Adversarial Differential Discriminator），无需手动设计奖励函数即可实现高保真运动跟踪。该方法通过单次正样本引导多目标优化，在多种杂技与敏捷行为上达到与现有技术相当的效果。
  ko: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- add
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.04961v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators (arXiv)'
  url: https://arxiv.org/abs/2505.04961v1
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
传统多目标优化方法依赖手动调整的聚合函数来构建联合优化目标，其性能受限于繁琐的权重选择过程。在基于强化学习的物理模拟角色运动跟踪中，这一局限性尤为突出，因为精心设计的奖励函数通常需要领域专家进行大量手动调参。ADD 提出了一种对抗性多目标优化技术，通过接收单个正样本的对抗性差分判别器，有效引导优化过程。该方法无需手动设计奖励函数，即可使角色紧密复现多种杂技与敏捷行为，其质量与最先进的运动跟踪方法相当。

## 核心内容
### 方法概述
- **问题背景**：多目标优化问题在众多应用中普遍存在，现有方法依赖手动调整的聚合函数，性能受限于权重选择，耗时且费力。在基于强化学习的运动跟踪任务中，手工设计的奖励函数同样存在领域知识依赖和调参困难的问题。
- **核心创新**：提出对抗性差分判别器（ADD），这是一种对抗性多目标优化技术，适用于包括运动跟踪在内的多种多目标强化学习任务。ADD 仅需接收单个正样本，即可有效引导优化过程，无需手动设计奖励函数。

### 实验设置与结果
- **任务场景**：在物理模拟环境中测试角色复现多种杂技与敏捷行为（如跳跃、翻滚等）的能力。
- **性能对比**：与最先进的运动跟踪方法相比，ADD 在复现行为的保真度上达到同等质量，但完全摆脱了对手工奖励函数的依赖。
- **代码与结果**：相关代码和实验结果已开源，访问地址为 https://add-moo.github.io/。

## Overview
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## 개요
다중 목표 최적화 문제는 여러 목표를 동시에 최적화해야 하며, 다양한 응용 분야에서 널리 발생합니다. 기존의 다중 목표 최적화 방법은 종종 수동으로 조정된 집계 함수를 사용하여 공동 최적화 목표를 구성합니다. 이러한 수동 조정 방법의 성능은 시간이 많이 소요되고 노동 집약적인 과정인 신중한 가중치 선택에 크게 의존합니다. 이러한 한계는 물리적으로 시뮬레이션된 캐릭터를 위한 강화 학습 기반 모션 추적 방법에서도 발생하며, 일반적으로 정교하게 설계된 보상 함수를 사용하여 높은 충실도의 결과를 얻습니다. 이러한 솔루션은 도메인 전문 지식과 상당한 수동 조정이 필요할 뿐만 아니라, 결과 보상 함수의 다양한 기술에 대한 적용 가능성을 제한합니다. 이러한 격차를 해소하기 위해, 우리는 모션 추적을 포함한 다양한 다중 목표 강화 학습 작업에 광범위하게 적용 가능한 새로운 적대적 다중 목표 최적화 기술을 제시합니다. 제안된 Adversarial Differential Discriminator (ADD)는 단일 양성 샘플을 받지만, 최적화 과정을 안내하는 데 여전히 효과적입니다. 우리의 기술을 통해 캐릭터가 다양한 곡예 및 민첩한 행동을 밀접하게 재현할 수 있으며, 수동으로 설계된 보상 함수에 의존하지 않고 최첨단 모션 추적 방법과 비교할 수 있는 품질을 달성할 수 있음을 입증합니다. 코드와 결과는 https://add-moo.github.io/에서 확인할 수 있습니다.

## 핵심 내용
다중 목표 최적화 문제는 여러 목표를 동시에 최적화해야 하며, 다양한 응용 분야에서 널리 발생합니다. 기존의 다중 목표 최적화 방법은 종종 수동으로 조정된 집계 함수를 사용하여 공동 최적화 목표를 구성합니다. 이러한 수동 조정 방법의 성능은 시간이 많이 소요되고 노동 집약적인 과정인 신중한 가중치 선택에 크게 의존합니다. 이러한 한계는 물리적으로 시뮬레이션된 캐릭터를 위한 강화 학습 기반 모션 추적 방법에서도 발생하며, 일반적으로 정교하게 설계된 보상 함수를 사용하여 높은 충실도의 결과를 얻습니다. 이러한 솔루션은 도메인 전문 지식과 상당한 수동 조정이 필요할 뿐만 아니라, 결과 보상 함수의 다양한 기술에 대한 적용 가능성을 제한합니다. 이러한 격차를 해소하기 위해, 우리는 모션 추적을 포함한 다양한 다중 목표 강화 학습 작업에 광범위하게 적용 가능한 새로운 적대적 다중 목표 최적화 기술을 제시합니다. 제안된 Adversarial Differential Discriminator (ADD)는 단일 양성 샘플을 받지만, 최적화 과정을 안내하는 데 여전히 효과적입니다. 우리의 기술을 통해 캐릭터가 다양한 곡예 및 민첩한 행동을 밀접하게 재현할 수 있으며, 수동으로 설계된 보상 함수에 의존하지 않고 최첨단 모션 추적 방법과 비교할 수 있는 품질을 달성할 수 있음을 입증합니다. 코드와 결과는 https://add-moo.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2505.04961v2
