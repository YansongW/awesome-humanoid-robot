---
$id: ent_paper_jing_learning_action_priors_for_cro_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Action Priors for Cross-embodiment Robot Manipulation
  zh: 跨实体机器人操作的动作先验学习
  ko: 교차 구현 로봇 조작을 위한 행동 사전 학습
summary:
  en: This paper proposes a two-stage training framework that learns action priors from unconditioned trajectories via flow
    matching, then transfers them to VLA models for faster convergence and higher success rates in cross-embodiment manipulation,
    including humanoid robots.
  zh: 本文提出一个两阶段训练框架，通过流匹配从无条件轨迹中学习动作先验，然后将其迁移到VLA模型，以在跨实体操作（包括人形机器人）中实现更快的收敛和更高的成功率。
  ko: 본 논문은 흐름 매칭을 통해 무조건적 궤적으로부터 행동 사전을 학습한 후, 이를 VLA 모델에 전이하여 교차 구현 조작(인간형 로봇 포함)에서 더 빠른 수렴과 높은 성공률을 달성하는 2단계 훈련 프레임워크를
    제안한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- action_prior
- flow_matching
- cross_embodiment
- humanoid_manipulation
- transfer_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.26095v1.
sources:
- id: src_001
  type: paper
  title: Learning Action Priors for Cross-embodiment Robot Manipulation
  url: https://arxiv.org/abs/2606.26095
  date: '2026'
  accessed_at: '2026-06-25'
related_entities: []
theoretical_depth:
- system
---
## 概述
Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.

## 核心内容
Most Vision-Language-Action (VLA) models build on a Vision-Language Model (VLM) backbone by attaching an action module and optimizing the full policy jointly. This design inherits strong visual and linguistic priors from the VLM, but leaves the action module to learn physical motion almost from scratch. As a result, the policy lacks an explicit motion prior, forcing early optimization to simultaneously discover temporal action dynamics and cross-modal alignment, a challenge further amplified in cross-embodiment settings. In this work, we propose to pretrain the action module with motion priors before cross-modal VLA alignment. Specifically, we introduce a two-stage training framework that equips the action module with cross-embodiment temporal motion structure before VLA training begins. In Stage~1, a lightweight flow-matching-based encoder-decoder action module efficiently learns temporal motion structure solely from unconditioned action trajectories, without processing visual or language tokens. In Stage~2, this learned prior is transferred to VLA training through decoder reuse and early-stage latent distillation, aligning visual-language features with the action embedding space while still allowing end-to-end policy refinement. In addition, the trained encoder serves as a compact history compressor, summarizing state-action histories into a single temporal context token for history-aware modeling at negligible cost. Extensive experiments across 13 diverse cross-embodiment tasks on both simulated and real-world platforms validate the effectiveness of our approach. Compared with VLA training without action priors, our model achieves faster convergence, higher success rates, and substantially stronger performance on data-scarce real-world tasks. Moreover, scaling up the action data in Stage~1 yields a more generalizable action prior that directly improves downstream VLA performance.

## 参考
- http://arxiv.org/abs/2606.26095v1

