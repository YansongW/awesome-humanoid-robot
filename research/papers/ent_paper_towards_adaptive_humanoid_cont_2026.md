---
$id: ent_paper_towards_adaptive_humanoid_cont_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning
  zh: 多行为蒸馏不是简单拼策略
  ko: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning
summary:
  en: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning is a knowledge node related
    to paper in the humanoid robot value chain.
  zh: Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking,
    running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding
    behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains
    and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage
    framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first
    train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior
    controller, facilitating adaptive behavior switching based
  ko: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning is a knowledge node related
    to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06371v3.
sources:
- id: src_001
  type: paper
  title: Towards Adaptive Humanoid Control via Multi-Behavior Distillation and Reinforced Fine-Tuning (arXiv)
  url: https://arxiv.org/abs/2511.06371
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 多行为蒸馏不是简单拼策略 project page
  url: https://ahc-humanoid.github.io
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## 核心内容
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## 参考
- http://arxiv.org/abs/2511.06371v3

## Overview
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## Content
Humanoid robots are promising to learn a diverse set of human-like locomotion behaviors, including standing up, walking, running, and jumping. However, existing methods predominantly require training independent policies for each skill, yielding behavior-specific controllers that exhibit limited generalization and brittle performance when deployed on irregular terrains and in diverse situations. To address this challenge, we propose Adaptive Humanoid Control (AHC) that adopts a two-stage framework to learn an adaptive humanoid locomotion controller across different skills and terrains. Specifically, we first train several primary locomotion policies and perform a multi-behavior distillation process to obtain a basic multi-behavior controller, facilitating adaptive behavior switching based on the environment. Then, we perform reinforced fine-tuning by collecting online feedback in performing adaptive behaviors on more diverse terrains, enhancing terrain adaptability for the controller. We conduct experiments in both simulation and real-world experiments in Unitree G1 robots. The results show that our method exhibits strong adaptability across various situations and terrains. Project website: https://ahc-humanoid.github.io.

## 개요
휴머노이드 로봇은 일어서기, 걷기, 달리기, 점프 등 다양한 인간형 보행 행동을 학습할 수 있는 가능성을 보여주고 있습니다. 그러나 기존 방법들은 주로 각 기술에 대해 독립적인 정책을 학습해야 하므로, 불규칙한 지형과 다양한 상황에서 배치될 때 일반화 능력이 제한적이고 성능이 취약한 행동별 제어기를 생성합니다. 이러한 문제를 해결하기 위해, 우리는 적응형 휴머노이드 제어(AHC)를 제안합니다. 이는 두 단계 프레임워크를 채택하여 다양한 기술과 지형에 걸쳐 적응형 휴머노이드 보행 제어기를 학습합니다. 구체적으로, 먼저 여러 기본 보행 정책을 학습하고 다중 행동 증류 과정을 수행하여 기본 다중 행동 제어기를 얻음으로써 환경에 기반한 적응형 행동 전환을 용이하게 합니다. 그런 다음, 더 다양한 지형에서 적응형 행동을 수행하는 과정에서 온라인 피드백을 수집하여 강화 미세 조정을 수행함으로써 제어기의 지형 적응성을 향상시킵니다. 우리는 Unitree G1 로봇을 사용하여 시뮬레이션과 실제 실험을 모두 수행했습니다. 결과는 우리의 방법이 다양한 상황과 지형에서 강력한 적응성을 보여줌을 입증합니다. 프로젝트 웹사이트: https://ahc-humanoid.github.io.

## 핵심 내용
휴머노이드 로봇은 일어서기, 걷기, 달리기, 점프 등 다양한 인간형 보행 행동을 학습할 수 있는 가능성을 보여주고 있습니다. 그러나 기존 방법들은 주로 각 기술에 대해 독립적인 정책을 학습해야 하므로, 불규칙한 지형과 다양한 상황에서 배치될 때 일반화 능력이 제한적이고 성능이 취약한 행동별 제어기를 생성합니다. 이러한 문제를 해결하기 위해, 우리는 적응형 휴머노이드 제어(AHC)를 제안합니다. 이는 두 단계 프레임워크를 채택하여 다양한 기술과 지형에 걸쳐 적응형 휴머노이드 보행 제어기를 학습합니다. 구체적으로, 먼저 여러 기본 보행 정책을 학습하고 다중 행동 증류 과정을 수행하여 기본 다중 행동 제어기를 얻음으로써 환경에 기반한 적응형 행동 전환을 용이하게 합니다. 그런 다음, 더 다양한 지형에서 적응형 행동을 수행하는 과정에서 온라인 피드백을 수집하여 강화 미세 조정을 수행함으로써 제어기의 지형 적응성을 향상시킵니다. 우리는 Unitree G1 로봇을 사용하여 시뮬레이션과 실제 실험을 모두 수행했습니다. 결과는 우리의 방법이 다양한 상황과 지형에서 강력한 적응성을 보여줌을 입증합니다. 프로젝트 웹사이트: https://ahc-humanoid.github.io.
