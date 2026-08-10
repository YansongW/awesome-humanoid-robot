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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.15270v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1014 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2408.15270v2

## 개요
전통적인 강화학습 방법은 인간-물체 상호작용 작업에서 수작업으로 설계된 기술 보상에 의존하여 다양한 상호작용 시나리오로 일반화하기 어렵습니다. SkillMimic은 통합된 HOI 모방 보상을 도입하여 상호작용 데이터셋에서 직접 상호작용 패턴의 본질적 특징을 추출함으로써 단일 정책이 여러 기술을 동시에 습득하도록 훈련합니다. 이 방법은 약 35분의 다양한 농구 기술을 포함하는 두 데이터셋에서 평가되었으며, 실험을 통해 드리블, 레이업, 슛 등의 기술 스타일 변형을 성공적으로 학습할 수 있음을 보여주었습니다. 이러한 기술은 상위 수준 컨트롤러를 통해 결합되어 연속 득점과 같은 복잡한 장기 작업을 완료할 수 있으며, 확장 가능하고 일반화 가능한 상호작용 기술 학습의 새로운 경로를 개척합니다.

## 핵심 내용
### 방법 핵심
- **통합 보상 함수**: 드리블, 슛 등 각 기술에 대해 개별적으로 보상을 설계하는 전통적 방법을 배제하고, 상호작용 데이터에서 인간과 물체의 상대 운동 패턴(예: 손과 공의 위치, 속도, 접촉 타이밍)을 자동으로 포착하는 일반적인 HOI 모방 보상을 제안합니다.
- **단일 정책 학습**: 이 통합 보상을 통해 SkillMimic은 여러 상호작용 기술을 동시에 처리하는 정책 네트워크를 훈련하며, 기술별로 네트워크나 보상 함수를 전환할 필요가 없습니다. HOI 데이터셋 규모가 증가함에 따라 기술의 다양성과 일반화 능력도 함께 향상됩니다.
- **기술 조합 메커니즘**: 상위 수준 컨트롤러는 하위 수준에서 학습된 기술을 호출하여 장기 작업(예: 연속 득점)을 구현할 수 있으며, 이는 기술 간의 부드러운 전환 능력(예: 드리블에서 레이업으로의 연결)에 의존합니다.

### 실험 설정
- **데이터셋**: 두 개의 농구 상호작용 데이터셋을 수집했으며, 총 약 35분으로 드리블(다양한 리듬과 방향 변화 포함), 레이업(좌우 손 방향 전환 포함), 슛(다양한 거리와 각도 포함) 등의 기술을 포함합니다.
- **기준선 비교**: 수작업 보상 기반 강화학습 방법(예: 특정 기술을 위해 설계된 보상 함수)과 비교하여, SkillMimic은 기술 다양성(예: 드리블 스타일 수)과 일반화성(예: 새로운 초기 상태에 대한 적응)에서 모두显著히 향상되었습니다.

### 핵심 결과
- **기술 습득**: 드리블, 레이업, 슛의 다양한 스타일 변형을 성공적으로 학습했습니다. 예를 들어 드리블 작업에서 정책은 시연의 낮은 드리블, 높은 드리블, 크로스오버 드리블 등의 패턴을 모방할 수 있습니다.
- **조합 작업**: 상위 수준 컨트롤러를 통해 SkillMimic은 연속 득점 작업(예: 후방에서 드리블 전진 → 레이업 → 리바운드 → 재슛)을 완료할 수 있으며, 성공률이 기준선 방법보다 높습니다.
- **일반화 능력**: 보지 못한 초기 위치나 물체 상태(예: 공이 다른 높이에 있을 때)에서도 기술 실행이 안정적으로 유지되어, 통합 보상이 우수한 일반화성을 가짐을 보여줍니다.

### 결론
SkillMimic은 통합 HOI 모방 보상이 수작업 설계 없이도 여러 상호작용 기술을 효과적으로 학습하고 조합할 수 있음을 입증했으며, 물리 시뮬레이션 캐릭터 애니메이션과 로봇 상호작용 기술 학습에 확장 가능한 패러다임을 제공합니다. 프로젝트 페이지에서 비디오 데모와 코드를 제공합니다.
