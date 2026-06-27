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
  en: This paper proposes a two-stage training framework that learns action priors
    from unconditioned trajectories via flow matching, then transfers them to VLA
    models for faster convergence and higher success rates in cross-embodiment manipulation,
    including humanoid robots.
  zh: 本文提出一个两阶段训练框架，通过流匹配从无条件轨迹中学习动作先验，然后将其迁移到VLA模型，以在跨实体操作（包括人形机器人）中实现更快的收敛和更高的成功率。
  ko: 본 논문은 흐름 매칭을 통해 무조건적 궤적으로부터 행동 사전을 학습한 후, 이를 VLA 모델에 전이하여 교차 구현 조작(인간형 로봇 포함)에서
    더 빠른 수렴과 높은 성공률을 달성하는 2단계 훈련 프레임워크를 제안한다.
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
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
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

## Overview

This paper addresses the lack of explicit motion priors in Vision-Language-Action (VLA) models, which forces the action module to learn physical motion from scratch during cross-modal alignment, leading to unstable optimization and poor cross-embodiment generalization. The authors propose a two-stage training framework: Stage 1 pretrains a flow-matching-based encoder-decoder action module on unconditioned action trajectories to capture temporal motion structure; Stage 2 transfers this prior to VLA training via decoder reuse and early-stage latent distillation, while also using the encoder as a history compressor. The method is evaluated on 13 cross-embodiment tasks in simulation (LIBERO, RoboCasa) and on a real-world Franka robot, demonstrating faster convergence, higher success rates, and improved data efficiency. The approach also scales favorably with more action data in Stage 1.

## Key Contributions

- Identifies absence of action priors as a structural bottleneck in VLA training and proposes a two-stage framework to learn action-centric motion before cross-modal alignment.
- Introduces a flow-matching encoder-decoder action module that learns compact motion-aware embeddings and transfers them as action priors for VLA training.
- Validates the method across 13 cross-embodiment tasks in simulation and real world, showing faster convergence, higher success rates, improved long-tail stability, and favorable scaling with more action data.

## Relevance to Humanoid Robotics

The paper directly addresses cross-embodiment robot manipulation, which is critical for humanoid robots that must operate in diverse environments. The method is evaluated on RoboCasa GR1 humanoid robot tasks, demonstrating its applicability to humanoid platforms. By learning action priors that generalize across embodiments, the approach can reduce the need for embodiment-specific data, accelerating deployment of humanoid robots in industrial and service applications. The two-stage framework also improves data efficiency, which is particularly valuable for humanoid robots where collecting large amounts of real-world data is expensive.
