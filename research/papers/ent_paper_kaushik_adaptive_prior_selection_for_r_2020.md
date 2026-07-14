---
$id: ent_paper_kaushik_adaptive_prior_selection_for_r_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Prior Selection for Repertoire-based Online Adaptation in Robotics
  zh: 机器人中基于技能库的在线自适应的自适应先验选择
  ko: 로봇 공학에서 레퍼토리 기반 온라인 적응을 위한 적응형 사전 선택
summary:
  en: This paper introduces APROL, an algorithm that maintains multiple MAP-Elites behavioral repertoires as simulation priors
    and selects the most suitable prior online using Gaussian-process transformation models and a MAP/UCB action-selection
    criterion. It enables reset-free adaptation to damage and environmental changes, and is shown to outperform single-prior
    and RTE baselines on simulated object pushing and hexapod locomotion, with validation on a real damaged hexapod.
  zh: 本文提出了APROL算法，该算法维护多个作为仿真先验的MAP-Elites行为技能库，并通过高斯过程变换模型与MAP/UCB动作选择准则在线选择最合适的先验。它实现了无重置的损坏与环境变化适应，在模拟推物与六足运动任务上优于单先验和RTE基线，并在真实损坏六足机器人上进行了验证。
  ko: 본 논문은 여러 MAP-Elites 행동 레퍼토리를 시뮬레이션 사전 정보로 유지하고, 가우시안 프로세스 변환 모델과 MAP/UCB 행동 선택 기준을 통해 온라인으로 가장 적절한 사전 정보를 선택하는 APROL
    알고리즘을 제안한다. 이는 재설정 없는 손상 및 환경 변화 적응을 가능하게 하며, 모의 물체 밀기와 육족 보행 과제에서 단일 사전 정보 및 RTE 기준보다 우수한 성능을 보이고, 실제 손상된 육족 로봇에서 검증되었다.
domains:
- 07_ai_models_algorithms
- 03_manufacturing_processes
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- repertoire_based_learning
- online_adaptation
- map_elites
- gaussian_process
- reset_free_learning
- damage_recovery
- simulation_prior
- behavioral_repertoire
- robot_adaptation
- aprol
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1907.07029v3.
sources:
- id: src_001
  type: paper
  title: Adaptive Prior Selection for Repertoire-based Online Adaptation in Robotics
  url: https://arxiv.org/abs/1907.07029
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Repertoire-based learning is a data-efficient adaptation approach based on a two-step process in which (1) a large and diverse set of policies is learned in simulation, and (2) a planning or learning algorithm chooses the most appropriate policies according to the current situation (e.g., a damaged robot, a new object, etc.). In this paper, we relax the assumption of previous works that a single repertoire is enough for adaptation. Instead, we generate repertoires for many different situations (e.g., with a missing leg, on different floors, etc.) and let our algorithm selects the most useful prior. Our main contribution is an algorithm, APROL (Adaptive Prior selection for Repertoire-based Online Learning) to plan the next action by incorporating these priors when the robot has no information about the current situation. We evaluate APROL on two simulated tasks: (1) pushing unknown objects of various shapes and sizes with a robotic arm and (2) a goal reaching task with a damaged hexapod robot. We compare with "Reset-free Trial and Error" (RTE) and various single repertoire-based baselines. The results show that APROL solves both the tasks in less interaction time than the baselines. Additionally, we demonstrate APROL on a real, damaged hexapod that quickly learns to pick compensatory policies to reach a goal by avoiding obstacles in the path.

## 核心内容
Repertoire-based learning is a data-efficient adaptation approach based on a two-step process in which (1) a large and diverse set of policies is learned in simulation, and (2) a planning or learning algorithm chooses the most appropriate policies according to the current situation (e.g., a damaged robot, a new object, etc.). In this paper, we relax the assumption of previous works that a single repertoire is enough for adaptation. Instead, we generate repertoires for many different situations (e.g., with a missing leg, on different floors, etc.) and let our algorithm selects the most useful prior. Our main contribution is an algorithm, APROL (Adaptive Prior selection for Repertoire-based Online Learning) to plan the next action by incorporating these priors when the robot has no information about the current situation. We evaluate APROL on two simulated tasks: (1) pushing unknown objects of various shapes and sizes with a robotic arm and (2) a goal reaching task with a damaged hexapod robot. We compare with "Reset-free Trial and Error" (RTE) and various single repertoire-based baselines. The results show that APROL solves both the tasks in less interaction time than the baselines. Additionally, we demonstrate APROL on a real, damaged hexapod that quickly learns to pick compensatory policies to reach a goal by avoiding obstacles in the path.

## 参考
- http://arxiv.org/abs/1907.07029v3

