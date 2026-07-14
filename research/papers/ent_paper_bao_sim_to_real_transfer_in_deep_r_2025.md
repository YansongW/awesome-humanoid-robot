---
$id: ent_paper_bao_sim_to_real_transfer_in_deep_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion
  zh: 双足运动深度强化学习中的仿真到现实迁移
  ko: 이족 보행 심층 강화학습의 시뮬레이션-현실 전이
summary:
  en: This survey chapter examines how deep reinforcement learning policies for bipedal locomotion can be transferred from
    simulation to real robots. It maps the sources of the sim-to-real gap and organizes mitigation strategies around model-centric
    fidelity improvements and policy hardening through robustness training and online adaptation.
  zh: 本综述章节研究如何将双足运动的深度强化学习策略从仿真迁移到真实机器人。它梳理了仿真-现实差距的来源，并从模型中心的保真度提升以及通过鲁棒性训练和在线自适应强化策略两个角度组织缓解方法。
  ko: 본 서베이 장에서는 이족 보행을 위한 심층 강화학습 정책을 시뮬레이션에서 실제 로봇으로 전이하는 방법을 다룬다. 시뮬-리얼 간극의 원인을 정리하고, 모델 중심의 충실도 향상과 강건성 훈련 및 온라인 적응을 통한
    정책 강화라는 두 축으로 해결책을 조직한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- deep_reinforcement_learning
- bipedal_locomotion
- domain_randomization
- system_identification
- residual_dynamics_learning
- teacher_student_learning
- online_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06465v1.
sources:
- id: src_001
  type: paper
  title: Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion
  url: https://arxiv.org/abs/2511.06465
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
This chapter addresses the critical challenge of simulation-to-reality (sim-to-real) transfer for deep reinforcement learning (DRL) in bipedal locomotion. After contextualizing the problem within various control architectures, we dissect the ``curse of simulation'' by analyzing the primary sources of sim-to-real gap: robot dynamics, contact modeling, state estimation, and numerical solvers. Building on this diagnosis, we structure the solutions around two complementary philosophies. The first is to shrink the gap through model-centric strategies that systematically improve the simulator's physical fidelity. The second is to harden the policy, a complementary approach that uses in-simulation robustness training and post-deployment adaptation to make the policy inherently resilient to model inaccuracies. The chapter concludes by synthesizing these philosophies into a strategic framework, providing a clear roadmap for developing and evaluating robust sim-to-real solutions.

## 核心内容
This chapter addresses the critical challenge of simulation-to-reality (sim-to-real) transfer for deep reinforcement learning (DRL) in bipedal locomotion. After contextualizing the problem within various control architectures, we dissect the ``curse of simulation'' by analyzing the primary sources of sim-to-real gap: robot dynamics, contact modeling, state estimation, and numerical solvers. Building on this diagnosis, we structure the solutions around two complementary philosophies. The first is to shrink the gap through model-centric strategies that systematically improve the simulator's physical fidelity. The second is to harden the policy, a complementary approach that uses in-simulation robustness training and post-deployment adaptation to make the policy inherently resilient to model inaccuracies. The chapter concludes by synthesizing these philosophies into a strategic framework, providing a clear roadmap for developing and evaluating robust sim-to-real solutions.

## 参考
- http://arxiv.org/abs/2511.06465v1

