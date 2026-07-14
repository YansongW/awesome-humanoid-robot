---
$id: ent_paper_chen_a_backbone_for_long_horizon_ro_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Backbone for Long-Horizon Robot Task Understanding
  zh: 面向长程机器人任务理解的骨干框架
  ko: 장기적 로봇 작업 이해를 위한 백본
summary:
  en: This paper proposes the Therblig-Based Backbone Framework (TBBF), which decomposes long-horizon robot manipulation tasks
    into elemental therblig units offline and transfers trajectories to novel scenes online via Action Registration and LLM-guided
    visual correction.
  zh: 本文提出基于动素（Therblig）的骨干框架TBBF，将长程机器人操作任务离线分解为基本动素单元，并通过动作注册与大语言模型引导的视觉校正在线将轨迹迁移到新场景。
  ko: 본 논문은 장기 로봇 조작 작업을 기본 동작 단위(therblig)로 오프라인 분해하고, 액션 등록 및 LLM 기반 시각 교정을 통해 온라인으로 새로운 장면에 궤적을 전이하는 TBBF를 제안한다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- long_horizon_manipulation
- therblig_decomposition
- one_shot_learning
- task_understanding
- action_object_mapping
- imitation_learning
- robot_learning
- sam
- llm_alignment
- trajectory_transfer
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.01334v3.
sources:
- id: src_001
  type: paper
  title: A Backbone for Long-Horizon Robot Task Understanding
  url: https://arxiv.org/abs/2408.01334
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
End-to-end robot learning, particularly for long-horizon tasks, often results in unpredictable outcomes and poor generalization. To address these challenges, we propose a novel Therblig-Based Backbone Framework (TBBF) as a fundamental structure to enhance interpretability, data efficiency, and generalization in robotic systems. TBBF utilizes expert demonstrations to enable therblig-level task decomposition, facilitate efficient action-object mapping, and generate adaptive trajectories for new scenarios. The approach consists of two stages: offline training and online testing. During the offline training stage, we developed the Meta-RGate SynerFusion (MGSF) network for accurate therblig segmentation across various tasks. In the online testing stage, after a one-shot demonstration of a new task is collected, our MGSF network extracts high-level knowledge, which is then encoded into the image using Action Registration (ActionREG). Additionally, Large Language Model (LLM)-Alignment Policy for Visual Correction (LAP-VC) is employed to ensure precise action registration, facilitating trajectory transfer in novel robot scenarios. Experimental results validate these methods, achieving 94.37% recall in therblig segmentation and success rates of 94.4% and 80% in real-world online robot testing for simple and complex scenarios, respectively. Supplementary material is available at: https://sites.google.com/view/therbligsbasedbackbone/home

## 核心内容
End-to-end robot learning, particularly for long-horizon tasks, often results in unpredictable outcomes and poor generalization. To address these challenges, we propose a novel Therblig-Based Backbone Framework (TBBF) as a fundamental structure to enhance interpretability, data efficiency, and generalization in robotic systems. TBBF utilizes expert demonstrations to enable therblig-level task decomposition, facilitate efficient action-object mapping, and generate adaptive trajectories for new scenarios. The approach consists of two stages: offline training and online testing. During the offline training stage, we developed the Meta-RGate SynerFusion (MGSF) network for accurate therblig segmentation across various tasks. In the online testing stage, after a one-shot demonstration of a new task is collected, our MGSF network extracts high-level knowledge, which is then encoded into the image using Action Registration (ActionREG). Additionally, Large Language Model (LLM)-Alignment Policy for Visual Correction (LAP-VC) is employed to ensure precise action registration, facilitating trajectory transfer in novel robot scenarios. Experimental results validate these methods, achieving 94.37% recall in therblig segmentation and success rates of 94.4% and 80% in real-world online robot testing for simple and complex scenarios, respectively. Supplementary material is available at: https://sites.google.com/view/therbligsbasedbackbone/home

## 参考
- http://arxiv.org/abs/2408.01334v3

