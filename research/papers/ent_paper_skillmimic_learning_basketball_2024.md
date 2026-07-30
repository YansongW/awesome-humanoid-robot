---
$id: ent_paper_skillmimic_learning_basketball_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
  zh: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
  ko: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
summary:
  en: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
  zh: SkillMimic 是 2024 年提出的一种基于数据驱动的物理仿真角色动画框架，用于人形机器人学习人-物交互技能。其核心贡献在于提出统一的 HOI 模仿奖励函数，无需为每种技能手动设计奖励，即可从演示数据中学习多种篮球交互技能（如运球、上篮、投篮），并支持技能间的平滑切换与组合。
  ko: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- skillmimic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.15270v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2408.15270
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
传统强化学习方法在人-物交互任务中依赖人工设计的技能奖励，难以泛化到不同交互场景。SkillMimic 通过引入统一的 HOI 模仿奖励，直接从交互数据集中提取交互模式的本质特征，从而训练单一策略同时掌握多种技能。该方法在包含约 35 分钟多样化篮球技能的两个数据集上进行了评估，实验表明其能成功学习运球、上篮、投篮等技能的风格变体，且这些技能可通过高层控制器组合完成连续得分等复杂长时任务，为可扩展、可泛化的交互技能学习开辟了新路径。

## 核心内容
### 方法核心
- **统一奖励函数**：摒弃传统方法中为每种技能（如运球、投篮）单独设计奖励的做法，提出一个通用的 HOI 模仿奖励，该奖励从交互数据中自动捕捉人与物体的相对运动模式（如手与球的位置、速度、接触时序）。
- **单策略学习**：通过该统一奖励，SkillMimic 训练一个策略网络同时处理多种交互技能，无需为不同技能切换网络或奖励函数。随着 HOI 数据集规模增大，技能的多样性和泛化能力同步提升。
- **技能组合机制**：高层控制器可调用底层学到的技能，实现长时任务（如连续得分），这依赖于技能间的平滑过渡能力（例如从运球到上篮的衔接）。

### 实验设置
- **数据集**：收集了两个篮球交互数据集，总计约 35 分钟，涵盖运球（含不同节奏与方向变化）、上篮（含左右手变向）、投篮（含不同距离与角度）等技能。
- **基线对比**：与基于手工奖励的强化学习方法（如针对特定技能设计的奖励函数）对比，SkillMimic 在技能多样性（如运球风格数量）和泛化性（如对新初始状态的适应）上均显著提升。

### 关键结果
- **技能掌握**：成功学习运球、上篮、投篮的多种风格变体，例如在运球任务中，策略能模仿演示中的低运球、高运球、交叉运球等模式。
- **组合任务**：通过高层控制器，SkillMimic 可完成连续得分任务（如从后场运球推进→上篮→抢篮板→再次投篮），成功率高于基线方法。
- **泛化能力**：在未见过的初始位置或物体状态（如球在不同高度）下，技能执行仍保持稳定，表明统一奖励具有较好的泛化性。

### 结论
SkillMimic 证明了统一 HOI 模仿奖励在无需手工设计的前提下，能够有效学习并组合多种交互技能，为物理仿真角色动画和机器人交互技能学习提供了可扩展的范式。项目页面提供视频演示与代码。

## Overview
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## 개요
인간-객체 상호작용(HOI)을 위한 전통적인 강화 학습 방법은 노동 집약적이고 수동으로 설계된 기술 보상에 의존하며, 이는 다양한 상호작용 간에 잘 일반화되지 않습니다. 우리는 SkillMimic을 소개합니다. 이는 기술별 보상의 필요성을 제거하여 에이전트가 상호작용 기술을 학습하는 방식을 근본적으로 변화시키는 통합 데이터 기반 프레임워크입니다. 우리의 핵심 통찰은 통합된 HOI 모방 보상이 HOI 데이터셋의 다양한 상호작용 패턴의 본질을 효과적으로 포착할 수 있다는 것입니다. 이를 통해 SkillMimic은 단일 정책을 학습하여 여러 상호작용 기술을 숙달할 뿐만 아니라 기술 전환을 용이하게 하며, HOI 데이터셋이 성장함에 따라 다양성과 일반화가 모두 향상됩니다. 평가를 위해 약 35분 분량의 다양한 농구 기술을 포함하는 두 개의 농구 데이터셋을 수집하고 소개합니다. 광범위한 실험 결과, SkillMimic은 드리블, 레이업, 슛의 스타일 변형을 포함한 다양한 농구 기술을 성공적으로 숙달함을 보여줍니다. 더욱이, 이러한 학습된 기술은 고수준 컨트롤러에 의해 효과적으로 구성되어 연속 득점과 같은 복잡하고 장기적인 작업을 수행할 수 있으며, 확장 가능하고 일반화 가능한 상호작용 기술 학습의 새로운 가능성을 열어줍니다. 프로젝트 페이지: https://ingrid789.github.io/SkillMimic/

## 핵심 내용
인간-객체 상호작용(HOI)을 위한 전통적인 강화 학습 방법은 노동 집약적이고 수동으로 설계된 기술 보상에 의존하며, 이는 다양한 상호작용 간에 잘 일반화되지 않습니다. 우리는 SkillMimic을 소개합니다. 이는 기술별 보상의 필요성을 제거하여 에이전트가 상호작용 기술을 학습하는 방식을 근본적으로 변화시키는 통합 데이터 기반 프레임워크입니다. 우리의 핵심 통찰은 통합된 HOI 모방 보상이 HOI 데이터셋의 다양한 상호작용 패턴의 본질을 효과적으로 포착할 수 있다는 것입니다. 이를 통해 SkillMimic은 단일 정책을 학습하여 여러 상호작용 기술을 숙달할 뿐만 아니라 기술 전환을 용이하게 하며, HOI 데이터셋이 성장함에 따라 다양성과 일반화가 모두 향상됩니다. 평가를 위해 약 35분 분량의 다양한 농구 기술을 포함하는 두 개의 농구 데이터셋을 수집하고 소개합니다. 광범위한 실험 결과, SkillMimic은 드리블, 레이업, 슛의 스타일 변형을 포함한 다양한 농구 기술을 성공적으로 숙달함을 보여줍니다. 더욱이, 이러한 학습된 기술은 고수준 컨트롤러에 의해 효과적으로 구성되어 연속 득점과 같은 복잡하고 장기적인 작업을 수행할 수 있으며, 확장 가능하고 일반화 가능한 상호작용 기술 학습의 새로운 가능성을 열어줍니다. 프로젝트 페이지: https://ingrid789.github.io/SkillMimic/

## 参考
- http://arxiv.org/abs/2408.15270v2
