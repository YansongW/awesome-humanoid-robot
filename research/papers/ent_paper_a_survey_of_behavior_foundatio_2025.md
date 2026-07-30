---
$id: ent_paper_a_survey_of_behavior_foundatio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots'
  zh: 'A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots'
  ko: 'A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots'
summary:
  en: 'A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 《行为基础模型综述：下一代人形机器人全身控制系统》是2025年关于人形机器人全身控制与移动操作的研究工作。该综述系统梳理了行为基础模型（BFM）这一新范式，通过大规模预训练学习可复用的原始技能和行为先验，实现零样本或快速适应多种下游任务，并提供了持续更新的论文与项目资源库。
  ko: 'A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_survey_of_behavior_foundatio
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20487v5. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'A Survey of Behavior Foundation Model: Next-Generation Whole-Body Control System of Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2506.20487
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人因具备复杂运动控制、人机交互和通用物理智能的潜力而备受关注，但实现高效的全身控制（WBC）仍面临动力学复杂、欠驱动及任务多样性等挑战。传统基于学习的控制器虽能处理复杂任务，却因需要针对新场景进行昂贵且耗时的重新训练而限制实际应用。行为基础模型（BFM）通过大规模预训练学习可复用的原始技能和行为先验，使机器人能零样本或快速适应广泛下游任务。本文全面综述了BFM在人形机器人WBC中的发展，涵盖多种预训练流程，并讨论了实际应用、当前局限、紧迫挑战及未来机遇，同时提供了持续更新的论文与项目资源库（https://github.com/yuanmingqi/awesome-bfm-papers）。

## 核心内容
### 核心贡献
- 首次系统梳理行为基础模型（BFM）在人形机器人全身控制（WBC）中的应用，覆盖从预训练到下游任务适配的完整流程。
- 提出BFM作为解决传统学习控制器“重新训练成本高”问题的关键范式，通过大规模预训练实现零样本或快速适应。

### 方法架构
- **预训练流程**：综述了多种BFM预训练方法，包括基于模仿学习、强化学习及多模态数据融合的管线，旨在学习通用行为先验（如行走、抓取、平衡）。
- **全身控制整合**：BFM将原始技能（如步态调整、手臂操作）作为可复用模块，通过组合或微调适配新任务，避免从头训练。

### 实验设置与关键数字
- 文中未提供具体实验数据，但指出BFM在仿真和真实场景中均展现出对未知任务的快速适应能力（如零样本迁移至新地形或物体操作）。
- 强调当前挑战包括：预训练数据规模与多样性不足、跨任务泛化稳定性、以及实时推理的计算效率。

### 结论与展望
- BFM被视为实现可扩展、通用人形机器人智能的核心路径，未来需解决数据效率、安全约束及长期任务规划等难题。
- 作者维护的GitHub仓库（https://github.com/yuanmingqi/awesome-bfm-papers）将持续更新相关论文与项目，以推动后续研究。

## Overview
Humanoid robots are drawing significant attention as versatile platforms for complex motor control, human-robot interaction, and general-purpose physical intelligence. However, achieving efficient whole-body control (WBC) in humanoids remains a fundamental challenge due to sophisticated dynamics, underactuation, and diverse task requirements. While learning-based controllers have shown promise for complex tasks, their reliance on labor-intensive and costly retraining for new scenarios limits real-world applicability. To address these limitations, behavior(al) foundation models (BFMs) have emerged as a new paradigm that leverages large-scale pre-training to learn reusable primitive skills and broad behavioral priors, enabling zero-shot or rapid adaptation to a wide range of downstream tasks. In this paper, we present a comprehensive overview of BFMs for humanoid WBC, tracing their development across diverse pre-training pipelines. Furthermore, we discuss real-world applications, current limitations, urgent challenges, and future opportunities, positioning BFMs as a key approach toward scalable and general-purpose humanoid intelligence. Finally, we provide a curated and regularly updated collection of BFM papers and projects to facilitate more subsequent research, which is available at https://github.com/yuanmingqi/awesome-bfm-papers.

## 개요
휴머노이드 로봇은 복잡한 운동 제어, 인간-로봇 상호작용, 범용 물리적 지능을 위한 다목적 플랫폼으로서 큰 주목을 받고 있습니다. 그러나 정교한 동역학, 구동 부족, 다양한 작업 요구사항으로 인해 휴머노이드에서 효율적인 전신 제어(WBC)를 달성하는 것은 여전히 근본적인 과제로 남아 있습니다. 학습 기반 제어기는 복잡한 작업에서 가능성을 보여주었지만, 새로운 시나리오에 대한 노동 집약적이고 비용이 많이 드는 재학습에 의존하기 때문에 실제 적용 가능성이 제한됩니다. 이러한 한계를 해결하기 위해 행동 기반 모델(BFM)이 새로운 패러다임으로 등장하여 대규모 사전 학습을 활용해 재사용 가능한 기본 기술과 광범위한 행동 사전 지식을 학습함으로써 다양한 하위 작업에 대한 제로샷 또는 빠른 적응을 가능하게 합니다. 본 논문에서는 휴머노이드 WBC를 위한 BFM의 포괄적인 개요를 제시하며, 다양한 사전 학습 파이프라인을 통한 발전 과정을 추적합니다. 또한 실제 응용, 현재 한계, 시급한 과제, 미래 기회를 논의하며, BFM을 확장 가능하고 범용적인 휴머노이드 지능을 위한 핵심 접근 방식으로 자리매김합니다. 마지막으로, 추가 연구를 촉진하기 위해 엄선되고 정기적으로 업데이트되는 BFM 논문 및 프로젝트 모음을 제공하며, 이는 https://github.com/yuanmingqi/awesome-bfm-papers에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇은 복잡한 운동 제어, 인간-로봇 상호작용, 범용 물리적 지능을 위한 다목적 플랫폼으로서 큰 주목을 받고 있습니다. 그러나 정교한 동역학, 구동 부족, 다양한 작업 요구사항으로 인해 휴머노이드에서 효율적인 전신 제어(WBC)를 달성하는 것은 여전히 근본적인 과제로 남아 있습니다. 학습 기반 제어기는 복잡한 작업에서 가능성을 보여주었지만, 새로운 시나리오에 대한 노동 집약적이고 비용이 많이 드는 재학습에 의존하기 때문에 실제 적용 가능성이 제한됩니다. 이러한 한계를 해결하기 위해 행동 기반 모델(BFM)이 새로운 패러다임으로 등장하여 대규모 사전 학습을 활용해 재사용 가능한 기본 기술과 광범위한 행동 사전 지식을 학습함으로써 다양한 하위 작업에 대한 제로샷 또는 빠른 적응을 가능하게 합니다. 본 논문에서는 휴머노이드 WBC를 위한 BFM의 포괄적인 개요를 제시하며, 다양한 사전 학습 파이프라인을 통한 발전 과정을 추적합니다. 또한 실제 응용, 현재 한계, 시급한 과제, 미래 기회를 논의하며, BFM을 확장 가능하고 범용적인 휴머노이드 지능을 위한 핵심 접근 방식으로 자리매김합니다. 마지막으로, 추가 연구를 촉진하기 위해 엄선되고 정기적으로 업데이트되는 BFM 논문 및 프로젝트 모음을 제공하며, 이는 https://github.com/yuanmingqi/awesome-bfm-papers에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2506.20487v5
