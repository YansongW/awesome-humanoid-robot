---
$id: ent_paper_kaidanov_the_role_of_domain_randomizati_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: The Role of Domain Randomization in Training Diffusion Policies for Whole-Body
    Humanoid Control
  zh: 领域随机化在训练全身人形机器人控制扩散策略中的作用
  ko: 전신 휴머노이드 제어를 위한 확산 정책 학습에서 도메인 랜덤화의 역할
summary:
  en: This paper studies how dataset diversity and size affect Diffusion Policies
    for whole-body humanoid locomotion by generating synthetic demonstrations with
    AMP RL agents under various Domain Randomization conditions in IsaacGym. It finds
    that Diffusion Policies require substantially larger and more diverse datasets
    than manipulation tasks to achieve robust walking, with perturbation and terrain
    randomization being especially important.
  zh: 本文通过在 IsaacGym 中使用 AMP 强化学习智能体在不同域随机化条件下生成合成演示，研究数据集多样性和规模如何影响全身人形机器人运动的扩散策略。研究发现，与操作任务相比，扩散策略需要更大、更多样化的数据集才能实现稳健的行走，其中扰动和地形随机化尤为重要。
  ko: 이 논문은 IsaacGym에서 AMP 강화학습 에이전트를 다양한 도메인 랜덤화 조건 하에서 합성 데모를 생성하여 전신 휴머노이드 보행에
    대한 확산 정책에 미치는 데이터셋 다양성과 크기의 영향을 연구한다. 연구 결과, 조작 작업에 비해 확산 정책이 안정적인 보행을 위해 훨씬 더
    크고 다양한 데이터셋이 필요하며, 특히 외란 및 지형 랜덤화가 중요함을 발견했다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_policy
- domain_randomization
- whole_body_control
- humanoid_locomotion
- adversarial_motion_prior
- imitation_learning
- isaacgym
- synthetic_demonstrations
- unitree_h1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: The Role of Domain Randomization in Training Diffusion Policies for Whole-Body
    Humanoid Control
  url: https://arxiv.org/abs/2411.01349
  date: '2024'
  accessed_at: '2026-06-26'
---


## Overview

The paper investigates how dataset diversity and size affect the performance of Diffusion Policies (DPs) for whole-body humanoid control. It focuses on locomotion rather than manipulation, using a simulated Unitree H1 humanoid in IsaacGym. The authors first train robust Adversarial Motion Prior (AMP) reinforcement-learning policies under extensive Domain Randomization (DR), then use these policies to collect synthetic observation-action datasets under different randomization conditions and at different sizes. Diffusion Policies are fitted to each dataset and evaluated on both non-randomized flat terrain and randomized uneven terrain.

## Key Contributions

- First ablation study on the impact of Domain Randomization in dataset generation for training Diffusion Policies on humanoid whole-body control.
- Introduction and comparison of multiple DR strategies, including dynamics, perturbation, terrain, initial-state, and humanoid-scale randomization.
- Systematic analysis of how dataset size interacts with different randomization techniques.
- Finding that whole-body humanoid control requires substantially larger and more diverse datasets than manipulation tasks for Diffusion Policies.

## Relevance to Humanoid Robotics

The work is directly relevant to scalable data generation and robust policy learning for humanoid robots. It shows that high-quality synthetic demonstrations combined with careful DR can enable Diffusion Policies to match the performance of the source RL policy on velocity-tracking locomotion. This supports broader efforts to reduce reliance on scarce real-world humanoid demonstrations and to develop generalizable whole-body controllers for human-centered environments.
