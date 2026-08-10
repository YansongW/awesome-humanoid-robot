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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.20487v5. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (865 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.20487v5

## 개요
휴머노이드 로봇은 복잡한 운동 제어, 인간-로봇 상호작용 및 범용 물리 지능의 잠재력으로 주목받고 있지만, 효율적인 전신 제어(WBC)를 구현하는 것은 여전히 동역학적 복잡성, 부족 구동 및 작업 다양성 등의 도전 과제에 직면해 있습니다. 전통적인 학습 기반 제어기는 복잡한 작업을 처리할 수 있지만, 새로운 시나리오에 대해 비용이 많이 들고 시간이 오래 걸리는 재학습이 필요하여 실제 적용이 제한됩니다. 행동 기반 모델(BFM)은 대규모 사전 학습을 통해 재사용 가능한 원시 기술과 행동 사전 지식을 학습하여 로봇이 광범위한 하위 작업에 제로샷 또는 빠르게 적응할 수 있게 합니다. 본 논문은 휴머노이드 로봇 WBC에서 BFM의 발전을 포괄적으로 검토하며, 다양한 사전 학습 프로세스를 다루고 실제 적용, 현재 한계, 시급한 도전 과제 및 미래 기회를 논의하며, 지속적으로 업데이트되는 논문 및 프로젝트 리소스 저장소(https://github.com/yuanmingqi/awesome-bfm-papers)도 제공합니다.

## 핵심 내용
### 핵심 기여
- 휴머노이드 로봇 전신 제어(WBC)에서 행동 기반 모델(BFM)의 적용을 최초로 체계적으로 정리하여, 사전 학습부터 하위 작업 적응까지의 전체 프로세스를 다룹니다.
- BFM을 전통적인 학습 제어기의 "재학습 비용이 높은" 문제를 해결하는 핵심 패러다임으로 제안하며, 대규모 사전 학습을 통해 제로샷 또는 빠른 적응을 구현합니다.

### 방법 아키텍처
- **사전 학습 프로세스**: 모방 학습, 강화 학습 및 다중 모달 데이터 융합 기반 파이프라인을 포함한 다양한 BFM 사전 학습 방법을 검토하여, 일반적인 행동 사전 지식(예: 보행, 파지, 균형)을 학습하는 것을 목표로 합니다.
- **전신 제어 통합**: BFM은 원시 기술(예: 보행 조정, 팔 조작)을 재사용 가능한 모듈로 활용하여, 조합 또는 미세 조정을 통해 새로운 작업에 적응하며 처음부터 학습하는 것을 피합니다.

### 실험 설정 및 핵심 수치
- 본문에는 구체적인 실험 데이터가 제공되지 않지만, BFM이 시뮬레이션 및 실제 환경 모두에서 알려지지 않은 작업에 대한 빠른 적응 능력(예: 새로운 지형 또는 물체 조작으로의 제로샷 전이)을 보여준다고 지적합니다.
- 현재 도전 과제로는 사전 학습 데이터의 규모와 다양성 부족, 교차 작업 일반화 안정성, 실시간 추론의 계산 효율성 등이 강조됩니다.

### 결론 및 전망
- BFM은 확장 가능하고 범용적인 휴머노이드 로봇 지능을 구현하는 핵심 경로로 간주되며, 향후 데이터 효율성, 안전 제약 및 장기 작업 계획 등의 문제를 해결해야 합니다.
- 저자가 유지 관리하는 GitHub 저장소(https://github.com/yuanmingqi/awesome-bfm-papers)는 관련 논문과 프로젝트를 지속적으로 업데이트하여 후속 연구를 촉진할 것입니다.
