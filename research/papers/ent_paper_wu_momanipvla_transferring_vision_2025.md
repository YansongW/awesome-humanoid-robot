---
$id: ent_paper_wu_momanipvla_transferring_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation'
  zh: MoManipVLA
  ko: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation'
summary:
  en: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation (MoManipVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications,
    Nanyang Technological University, Tsinghua University, and published at CVPR25.'
  zh: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation (MoManipVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications,
    Nanyang Technological University, Tsinghua University, and published at CVPR25.'
  ko: 'MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation (MoManipVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications,
    Nanyang Technological University, Tsinghua University, and published at CVPR25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- momanipvla
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.13446v1.
sources:
- id: src_001
  type: website
  title: MoManipVLA source
  url: https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Mobile manipulation is the fundamental challenge for robotics to assist humans with diverse tasks and environments in everyday life. However, conventional mobile manipulation approaches often struggle to generalize across different tasks and environments because of the lack of large-scale training. In contrast, recent advances in vision-language-action (VLA) models have shown impressive generalization capabilities, but these foundation models are developed for fixed-base manipulation tasks. Therefore, we propose an efficient policy adaptation framework named MoManipVLA to transfer pre-trained VLA models of fix-base manipulation to mobile manipulation, so that high generalization ability across tasks and environments can be achieved in mobile manipulation policy. Specifically, we utilize pre-trained VLA models to generate waypoints of the end-effector with high generalization ability. We design motion planning objectives for the mobile base and the robot arm, which aim at maximizing the physical feasibility of the trajectory. Finally, we present an efficient bi-level objective optimization framework for trajectory generation, where the upper-level optimization predicts waypoints for base movement to enhance the manipulator policy space, and the lower-level optimization selects the optimal end-effector trajectory to complete the manipulation task. In this way, MoManipVLA can adjust the position of the robot base in a zero-shot manner, thus making the waypoints predicted from the fixed-base VLA models feasible. Extensive experimental results on OVMM and the real world demonstrate that MoManipVLA achieves a 4.2% higher success rate than the state-of-the-art mobile manipulation, and only requires 50 training cost for real world deployment due to the strong generalization ability in the pre-trained VLA models.

## 核心内容
Mobile manipulation is the fundamental challenge for robotics to assist humans with diverse tasks and environments in everyday life. However, conventional mobile manipulation approaches often struggle to generalize across different tasks and environments because of the lack of large-scale training. In contrast, recent advances in vision-language-action (VLA) models have shown impressive generalization capabilities, but these foundation models are developed for fixed-base manipulation tasks. Therefore, we propose an efficient policy adaptation framework named MoManipVLA to transfer pre-trained VLA models of fix-base manipulation to mobile manipulation, so that high generalization ability across tasks and environments can be achieved in mobile manipulation policy. Specifically, we utilize pre-trained VLA models to generate waypoints of the end-effector with high generalization ability. We design motion planning objectives for the mobile base and the robot arm, which aim at maximizing the physical feasibility of the trajectory. Finally, we present an efficient bi-level objective optimization framework for trajectory generation, where the upper-level optimization predicts waypoints for base movement to enhance the manipulator policy space, and the lower-level optimization selects the optimal end-effector trajectory to complete the manipulation task. In this way, MoManipVLA can adjust the position of the robot base in a zero-shot manner, thus making the waypoints predicted from the fixed-base VLA models feasible. Extensive experimental results on OVMM and the real world demonstrate that MoManipVLA achieves a 4.2% higher success rate than the state-of-the-art mobile manipulation, and only requires 50 training cost for real world deployment due to the strong generalization ability in the pre-trained VLA models.

## 参考
- http://arxiv.org/abs/2503.13446v1

## Overview
Mobile manipulation is the fundamental challenge for robotics to assist humans with diverse tasks and environments in everyday life. However, conventional mobile manipulation approaches often struggle to generalize across different tasks and environments because of the lack of large-scale training. In contrast, recent advances in vision-language-action (VLA) models have shown impressive generalization capabilities, but these foundation models are developed for fixed-base manipulation tasks. Therefore, we propose an efficient policy adaptation framework named MoManipVLA to transfer pre-trained VLA models of fix-base manipulation to mobile manipulation, so that high generalization ability across tasks and environments can be achieved in mobile manipulation policy. Specifically, we utilize pre-trained VLA models to generate waypoints of the end-effector with high generalization ability. We design motion planning objectives for the mobile base and the robot arm, which aim at maximizing the physical feasibility of the trajectory. Finally, we present an efficient bi-level objective optimization framework for trajectory generation, where the upper-level optimization predicts waypoints for base movement to enhance the manipulator policy space, and the lower-level optimization selects the optimal end-effector trajectory to complete the manipulation task. In this way, MoManipVLA can adjust the position of the robot base in a zero-shot manner, thus making the waypoints predicted from the fixed-base VLA models feasible. Extensive experimental results on OVMM and the real world demonstrate that MoManipVLA achieves a 4.2% higher success rate than the state-of-the-art mobile manipulation, and only requires 50 training cost for real world deployment due to the strong generalization ability in the pre-trained VLA models.

## Content
Mobile manipulation is the fundamental challenge for robotics to assist humans with diverse tasks and environments in everyday life. However, conventional mobile manipulation approaches often struggle to generalize across different tasks and environments because of the lack of large-scale training. In contrast, recent advances in vision-language-action (VLA) models have shown impressive generalization capabilities, but these foundation models are developed for fixed-base manipulation tasks. Therefore, we propose an efficient policy adaptation framework named MoManipVLA to transfer pre-trained VLA models of fix-base manipulation to mobile manipulation, so that high generalization ability across tasks and environments can be achieved in mobile manipulation policy. Specifically, we utilize pre-trained VLA models to generate waypoints of the end-effector with high generalization ability. We design motion planning objectives for the mobile base and the robot arm, which aim at maximizing the physical feasibility of the trajectory. Finally, we present an efficient bi-level objective optimization framework for trajectory generation, where the upper-level optimization predicts waypoints for base movement to enhance the manipulator policy space, and the lower-level optimization selects the optimal end-effector trajectory to complete the manipulation task. In this way, MoManipVLA can adjust the position of the robot base in a zero-shot manner, thus making the waypoints predicted from the fixed-base VLA models feasible. Extensive experimental results on OVMM and the real world demonstrate that MoManipVLA achieves a 4.2% higher success rate than the state-of-the-art mobile manipulation, and only requires 50 training cost for real world deployment due to the strong generalization ability in the pre-trained VLA models.

## 개요
모바일 조작은 로봇이 일상생활에서 인간을 도와 다양한 작업과 환경을 수행하는 데 있어 근본적인 도전 과제입니다. 그러나 기존의 모바일 조작 접근 방식은 대규모 훈련 부족으로 인해 다양한 작업과 환경에 일반화하는 데 어려움을 겪는 경우가 많습니다. 반면, 최근 시각-언어-행동(VLA) 모델의 발전은 뛰어난 일반화 능력을 보여주었지만, 이러한 기초 모델은 고정 베이스 조작 작업을 위해 개발되었습니다. 따라서 우리는 MoManipVLA라는 효율적인 정책 적응 프레임워크를 제안하여 고정 베이스 조작을 위한 사전 훈련된 VLA 모델을 모바일 조작으로 전이함으로써, 작업과 환경 전반에 걸쳐 높은 일반화 능력을 모바일 조작 정책에서 달성할 수 있도록 합니다. 구체적으로, 우리는 사전 훈련된 VLA 모델을 활용하여 높은 일반화 능력을 가진 엔드 이펙터의 웨이포인트를 생성합니다. 모바일 베이스와 로봇 팔을 위한 모션 계획 목표를 설계하여 궤적의 물리적 실현 가능성을 최대화합니다. 마지막으로, 궤적 생성을 위한 효율적인 이중 수준 목표 최적화 프레임워크를 제시합니다. 여기서 상위 수준 최적화는 베이스 이동을 위한 웨이포인트를 예측하여 조작기 정책 공간을 확장하고, 하위 수준 최적화는 최적의 엔드 이펙터 궤적을 선택하여 조작 작업을 완료합니다. 이렇게 하여 MoManipVLA는 제로샷 방식으로 로봇 베이스의 위치를 조정할 수 있어, 고정 베이스 VLA 모델에서 예측된 웨이포인트를 실현 가능하게 만듭니다. OVMM 및 실제 환경에서의 광범위한 실험 결과, MoManipVLA는 최첨단 모바일 조작보다 4.2% 높은 성공률을 달성하며, 사전 훈련된 VLA 모델의 강력한 일반화 능력 덕분에 실제 환경 배포에 50의 훈련 비용만 필요함을 보여줍니다.

## 핵심 내용
모바일 조작은 로봇이 일상생활에서 인간을 도와 다양한 작업과 환경을 수행하는 데 있어 근본적인 도전 과제입니다. 그러나 기존의 모바일 조작 접근 방식은 대규모 훈련 부족으로 인해 다양한 작업과 환경에 일반화하는 데 어려움을 겪는 경우가 많습니다. 반면, 최근 시각-언어-행동(VLA) 모델의 발전은 뛰어난 일반화 능력을 보여주었지만, 이러한 기초 모델은 고정 베이스 조작 작업을 위해 개발되었습니다. 따라서 우리는 MoManipVLA라는 효율적인 정책 적응 프레임워크를 제안하여 고정 베이스 조작을 위한 사전 훈련된 VLA 모델을 모바일 조작으로 전이함으로써, 작업과 환경 전반에 걸쳐 높은 일반화 능력을 모바일 조작 정책에서 달성할 수 있도록 합니다. 구체적으로, 우리는 사전 훈련된 VLA 모델을 활용하여 높은 일반화 능력을 가진 엔드 이펙터의 웨이포인트를 생성합니다. 모바일 베이스와 로봇 팔을 위한 모션 계획 목표를 설계하여 궤적의 물리적 실현 가능성을 최대화합니다. 마지막으로, 궤적 생성을 위한 효율적인 이중 수준 목표 최적화 프레임워크를 제시합니다. 여기서 상위 수준 최적화는 베이스 이동을 위한 웨이포인트를 예측하여 조작기 정책 공간을 확장하고, 하위 수준 최적화는 최적의 엔드 이펙터 궤적을 선택하여 조작 작업을 완료합니다. 이렇게 하여 MoManipVLA는 제로샷 방식으로 로봇 베이스의 위치를 조정할 수 있어, 고정 베이스 VLA 모델에서 예측된 웨이포인트를 실현 가능하게 만듭니다. OVMM 및 실제 환경에서의 광범위한 실험 결과, MoManipVLA는 최첨단 모바일 조작보다 4.2% 높은 성공률을 달성하며, 사전 훈련된 VLA 모델의 강력한 일반화 능력 덕분에 실제 환경 배포에 50의 훈련 비용만 필요함을 보여줍니다.
