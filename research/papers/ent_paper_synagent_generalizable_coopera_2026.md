---
$id: ent_paper_synagent_generalizable_coopera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy'
  zh: SynAgent｜通过单独与合作的智能体协同进行可推广的合作人形操作
  ko: 'SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy'
summary:
  en: Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due
    to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this
    paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation
    by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent
    human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving
    retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial
    relationships among humans and objects. Building upon this refined da
  zh: SynAgent 先从相机图像/多视角观测恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、地形/场景表征。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: SynAgent 先从相机图像/多视角观测恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、地形/场景表征。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- scene_understanding
- synagent
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: SynAgent: Generalizable
    Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy.'
sources:
- id: src_001
  type: website
  title: SynAgent project page
  url: https://yw0208.github.io/synagent/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## 核心内容
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## 参考
- Semantic Scholar search: SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy

