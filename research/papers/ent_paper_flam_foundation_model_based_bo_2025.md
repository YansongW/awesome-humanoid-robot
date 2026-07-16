---
$id: ent_paper_flam_foundation_model_based_bo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
  zh: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
  ko: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation'
summary:
  en: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flam
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.22249v1.
sources:
- id: src_001
  type: paper
  title: 'FLAM: Foundation Model-Based Body Stabilization for Humanoid Locomotion and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2503.22249
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## 核心内容
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## 参考
- http://arxiv.org/abs/2503.22249v1

## Overview
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## Content
Humanoid robots have attracted significant attention in recent years. Reinforcement Learning (RL) is one of the main ways to control the whole body of humanoid robots. RL enables agents to complete tasks by learning from environment interactions, guided by task rewards. However, existing RL methods rarely explicitly consider the impact of body stability on humanoid locomotion and manipulation. Achieving high performance in whole-body control remains a challenge for RL methods that rely solely on task rewards. In this paper, we propose a Foundation model-based method for humanoid Locomotion And Manipulation (FLAM for short). FLAM integrates a stabilizing reward function with a basic policy. The stabilizing reward function is designed to encourage the robot to learn stable postures, thereby accelerating the learning process and facilitating task completion. Specifically, the robot pose is first mapped to the 3D virtual human model. Then, the human pose is stabilized and reconstructed through a human motion reconstruction model. Finally, the pose before and after reconstruction is used to compute the stabilizing reward. By combining this stabilizing reward with the task reward, FLAM effectively guides policy learning. Experimental results on a humanoid robot benchmark demonstrate that FLAM outperforms state-of-the-art RL methods, highlighting its effectiveness in improving stability and overall performance.

## 개요
휴머노이드 로봇은 최근 몇 년간 큰 주목을 받아왔습니다. 강화 학습(Reinforcement Learning, RL)은 휴머노이드 로봇의 전신을 제어하는 주요 방법 중 하나입니다. RL은 작업 보상(task reward)에 따라 환경과의 상호작용을 통해 학습함으로써 에이전트가 작업을 완료할 수 있게 합니다. 그러나 기존의 RL 방법은 신체 안정성이 휴머노이드의 보행 및 조작에 미치는 영향을 명시적으로 고려하는 경우가 드뭅니다. 작업 보상에만 의존하는 RL 방법으로는 전신 제어에서 높은 성능을 달성하는 것이 여전히 어려운 과제입니다. 본 논문에서는 휴머노이드 보행 및 조작을 위한 Foundation 모델 기반 방법(FLAM)을 제안합니다. FLAM은 안정화 보상 함수(stabilizing reward function)를 기본 정책(basic policy)과 통합합니다. 안정화 보상 함수는 로봇이 안정적인 자세를 학습하도록 유도하여 학습 과정을 가속화하고 작업 완료를 촉진하도록 설계되었습니다. 구체적으로, 먼저 로봇 자세를 3D 가상 인간 모델에 매핑합니다. 그런 다음, 인간 동작 재구성 모델을 통해 인간 자세를 안정화하고 재구성합니다. 마지막으로, 재구성 전후의 자세를 사용하여 안정화 보상을 계산합니다. 이 안정화 보상을 작업 보상과 결합함으로써 FLAM은 정책 학습을 효과적으로 안내합니다. 휴머노이드 로봇 벤치마크에서의 실험 결과는 FLAM이 최신 RL 방법보다 우수한 성능을 보여주며, 안정성 및 전반적인 성능 향상에 있어 효과적임을 입증합니다.

## 핵심 내용
휴머노이드 로봇은 최근 몇 년간 큰 주목을 받아왔습니다. 강화 학습(RL)은 휴머노이드 로봇의 전신을 제어하는 주요 방법 중 하나입니다. RL은 작업 보상에 따라 환경과의 상호작용을 통해 학습함으로써 에이전트가 작업을 완료할 수 있게 합니다. 그러나 기존의 RL 방법은 신체 안정성이 휴머노이드의 보행 및 조작에 미치는 영향을 명시적으로 고려하는 경우가 드뭅니다. 작업 보상에만 의존하는 RL 방법으로는 전신 제어에서 높은 성능을 달성하는 것이 여전히 어려운 과제입니다. 본 논문에서는 휴머노이드 보행 및 조작을 위한 Foundation 모델 기반 방법(FLAM)을 제안합니다. FLAM은 안정화 보상 함수를 기본 정책과 통합합니다. 안정화 보상 함수는 로봇이 안정적인 자세를 학습하도록 유도하여 학습 과정을 가속화하고 작업 완료를 촉진하도록 설계되었습니다. 구체적으로, 먼저 로봇 자세를 3D 가상 인간 모델에 매핑합니다. 그런 다음, 인간 동작 재구성 모델을 통해 인간 자세를 안정화하고 재구성합니다. 마지막으로, 재구성 전후의 자세를 사용하여 안정화 보상을 계산합니다. 이 안정화 보상을 작업 보상과 결합함으로써 FLAM은 정책 학습을 효과적으로 안내합니다. 휴머노이드 로봇 벤치마크에서의 실험 결과는 FLAM이 최신 RL 방법보다 우수한 성능을 보여주며, 안정성 및 전반적인 성능 향상에 있어 효과적임을 입증합니다.
