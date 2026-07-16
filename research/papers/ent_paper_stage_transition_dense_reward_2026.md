---
$id: ent_paper_stage_transition_dense_reward_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stage-Transition Dense Reward Modeling for Reinforcement Learning
  zh: Stage-Transition Dense Reward Modeling for Reinforcement Learning
  ko: Stage-Transition Dense Reward Modeling for Reinforcement Learning
summary:
  en: 'arXiv:2606.31377v1 Announce Type: new Abstract: Reinforcement learning for long-horizon robotic manipulation is often
    limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes
    in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning
    framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch.
    STDR leverages semantic understanding to infer a task''s stage structure from demonstrations, and delivers two complementary
    learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage
    progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution
    (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking.
    Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves
    sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several
    challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful
    executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated
    reward assignment across settings.'
  zh: 'arXiv:2606.31377v1 Announce Type: new Abstract: Reinforcement learning for long-horizon robotic manipulation is often
    limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes
    in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning
    framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch.
    STDR leverages semantic understanding to infer a task''s stage structure from demonstrations, and delivers two complementary
    learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage
    progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution
    (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking.
    Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves
    sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several
    challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful
    executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated
    reward assignment across settings.'
  ko: 'arXiv:2606.31377v1 Announce Type: new Abstract: Reinforcement learning for long-horizon robotic manipulation is often
    limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes
    in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning
    framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch.
    STDR leverages semantic understanding to infer a task''s stage structure from demonstrations, and delivers two complementary
    learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage
    progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution
    (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking.
    Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves
    sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several
    challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful
    executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated
    reward assignment across settings.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- stage_transition_dense_reward
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31377v1.
sources:
- id: src_001
  type: paper
  title: Stage-Transition Dense Reward Modeling for Reinforcement Learning
  url: https://arxiv.org/abs/2606.31377
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.

## 核心内容
Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.

## 参考
- http://arxiv.org/abs/2606.31377v1

## Overview
Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.

## Content
Reinforcement learning for long-horizon robotic manipulation is often limited by sparse and delayed rewards, while manually designing dense shaping signals is costly and brittle to changes in environments and object configurations. This work proposes Stage-Transition Dense Reward (STDR), a visual reward-learning framework that converts unstructured expert videos into logically grounded dense rewards for training RL agents from scratch. STDR leverages semantic understanding to infer a task's stage structure from demonstrations, and delivers two complementary learning signals during online training: (i) stage-transition feedback that provides goal-directed reward, and (ii) within-stage progress feedback that supplies fine-grained guidance toward completing each stage. Furthermore, an out-of-distribution (OOD) detection mechanism and a grasping regulation module are integrated to enhance robustness and prevent reward hacking. Experiments on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several challenging tasks. Real-robot evaluations further indicate that STDR assigns stable, progress-aligned rewards on successful executions while producing appropriately low rewards for failures, suggesting robustness to visual noise and better-calibrated reward assignment across settings.

## 개요
장기간 로봇 조작을 위한 강화 학습은 종종 희소하고 지연된 보상에 의해 제한되는 반면, 수동으로 조밀한 형성 신호를 설계하는 것은 비용이 많이 들고 환경 및 객체 구성의 변화에 취약합니다. 본 연구는 Stage-Transition Dense Reward (STDR)를 제안합니다. 이는 구조화되지 않은 전문가 비디오를 논리적으로 근거 있는 조밀한 보상으로 변환하여 처음부터 RL 에이전트를 훈련시키는 시각적 보상 학습 프레임워크입니다. STDR은 의미적 이해를 활용하여 데모에서 작업의 단계 구조를 추론하고, 온라인 훈련 중 두 가지 상호 보완적인 학습 신호를 제공합니다: (i) 목표 지향 보상을 제공하는 단계 전환 피드백, (ii) 각 단계 완료를 위한 세밀한 지침을 제공하는 단계 내 진행 피드백. 또한, 분포 외(OOD) 탐지 메커니즘과 파지 조절 모듈이 통합되어 견고성을 향상시키고 보상 해킹을 방지합니다. MetaWorld, ManiSkill 및 Franka Kitchen 전반에 걸친 14가지 조작 작업에 대한 실험은 STDR이 여러 기준선에 비해 샘플 효율성과 성공률을 일관되게 개선하며, 여러 도전적인 작업에서 수작업으로 만든 조밀한 보상과 일치하거나 능가함을 보여줍니다. 실제 로봇 평가는 STDR이 성공적인 실행에 대해 안정적이고 진행에 맞춰진 보상을 할당하는 반면, 실패에 대해서는 적절히 낮은 보상을 생성하여 시각적 노이즈에 대한 견고성과 설정 전반에 걸쳐 더 잘 보정된 보상 할당을 시사합니다.

## 핵심 내용
장기간 로봇 조작을 위한 강화 학습은 종종 희소하고 지연된 보상에 의해 제한되는 반면, 수동으로 조밀한 형성 신호를 설계하는 것은 비용이 많이 들고 환경 및 객체 구성의 변화에 취약합니다. 본 연구는 Stage-Transition Dense Reward (STDR)를 제안합니다. 이는 구조화되지 않은 전문가 비디오를 논리적으로 근거 있는 조밀한 보상으로 변환하여 처음부터 RL 에이전트를 훈련시키는 시각적 보상 학습 프레임워크입니다. STDR은 의미적 이해를 활용하여 데모에서 작업의 단계 구조를 추론하고, 온라인 훈련 중 두 가지 상호 보완적인 학습 신호를 제공합니다: (i) 목표 지향 보상을 제공하는 단계 전환 피드백, (ii) 각 단계 완료를 위한 세밀한 지침을 제공하는 단계 내 진행 피드백. 또한, 분포 외(OOD) 탐지 메커니즘과 파지 조절 모듈이 통합되어 견고성을 향상시키고 보상 해킹을 방지합니다. MetaWorld, ManiSkill 및 Franka Kitchen 전반에 걸친 14가지 조작 작업에 대한 실험은 STDR이 여러 기준선에 비해 샘플 효율성과 성공률을 일관되게 개선하며, 여러 도전적인 작업에서 수작업으로 만든 조밀한 보상과 일치하거나 능가함을 보여줍니다. 실제 로봇 평가는 STDR이 성공적인 실행에 대해 안정적이고 진행에 맞춰진 보상을 할당하는 반면, 실패에 대해서는 적절히 낮은 보상을 생성하여 시각적 노이즈에 대한 견고성과 설정 전반에 걸쳐 더 잘 보정된 보상 할당을 시사합니다.
