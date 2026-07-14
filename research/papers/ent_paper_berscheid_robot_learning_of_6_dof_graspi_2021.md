---
$id: ent_paper_berscheid_robot_learning_of_6_dof_graspi_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Learning of 6 DoF Grasping using Model-based Adaptive Primitives
  zh: 基于模型自适应原语的机器人六自由度抓取学习
  ko: 모델 기반 적응형 프리미티브를 이용한 6자유도 그래스핑 로봇 학습
summary:
  en: This paper presents a hybrid 6-DoF bin-picking approach that combines a fully-convolutional neural network for planar
    grasp-reward estimation with a model-based controller for lateral orientation adaptation, achieving over 92% real-world
    grasp success in dense clutter after 27,000 self-supervised grasp attempts with inference under 50 ms.
  zh: 本文提出了一种混合六自由度料箱拣选方法，将用于平面抓取奖励估计的全卷积神经网络与用于侧向朝向自适应的基于模型控制器相结合，在 27,000 次自监督真实世界抓取尝试后，于密集 clutter 中实现了超过 92% 的抓取成功率，推理时间低于
    50 毫秒。
  ko: 본 논문은 평면 그래스프 보상 추정을 위한 완전 컨볼루션 신경망과 측면 방향 적응을 위한 모델 기반 컨트롤러를 결합한 하이브리드 6자유도 빈 피킹 접근법을 제안하며, 27,000회의 자기 감독 실제 그래스프
    시도 후 밀집된 clutter에서 92% 이상의 그래스프 성공률과 50ms 미만의 추론 시간을 달성하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- 6dof_grasping
- bin_picking
- model_based_control
- deep_learning
- fcnn
- self_supervised_learning
- collision_avoidance
- grasp_primitives
- robot_learning
- end_effector
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2103.12810v1.
sources:
- id: src_001
  type: paper
  title: Robot Learning of 6 DoF Grasping using Model-based Adaptive Primitives
  url: https://arxiv.org/abs/2103.12810
  date: '2021'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Robot learning is often simplified to planar manipulation due to its data consumption. Then, a common approach is to use a fully-convolutional neural network to estimate the reward of grasp primitives. In this work, we extend this approach by parametrizing the two remaining, lateral Degrees of Freedom (DoFs) of the primitives. We apply this principle to the task of 6 DoF bin picking: We introduce a model-based controller to calculate angles that avoid collisions, maximize the grasp quality while keeping the uncertainty small. As the controller is integrated into the training, our hybrid approach is able to learn about and exploit the model-based controller. After real-world training of 27000 grasp attempts, the robot is able to grasp known objects with a success rate of over 92% in dense clutter. Grasp inference takes less than 50ms. In further real-world experiments, we evaluate grasp rates in a range of scenarios including its ability to generalize to unknown objects. We show that the system is able to avoid collisions, enabling grasps that would not be possible without primitive adaption.

## 核心内容
Robot learning is often simplified to planar manipulation due to its data consumption. Then, a common approach is to use a fully-convolutional neural network to estimate the reward of grasp primitives. In this work, we extend this approach by parametrizing the two remaining, lateral Degrees of Freedom (DoFs) of the primitives. We apply this principle to the task of 6 DoF bin picking: We introduce a model-based controller to calculate angles that avoid collisions, maximize the grasp quality while keeping the uncertainty small. As the controller is integrated into the training, our hybrid approach is able to learn about and exploit the model-based controller. After real-world training of 27000 grasp attempts, the robot is able to grasp known objects with a success rate of over 92% in dense clutter. Grasp inference takes less than 50ms. In further real-world experiments, we evaluate grasp rates in a range of scenarios including its ability to generalize to unknown objects. We show that the system is able to avoid collisions, enabling grasps that would not be possible without primitive adaption.

## 参考
- http://arxiv.org/abs/2103.12810v1

