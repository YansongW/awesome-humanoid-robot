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
  en: This paper presents a hybrid 6-DoF bin-picking approach that combines a fully-convolutional
    neural network for planar grasp-reward estimation with a model-based controller
    for lateral orientation adaptation, achieving over 92% real-world grasp success
    in dense clutter after 27,000 self-supervised grasp attempts with inference under
    50 ms.
  zh: 本文提出了一种混合六自由度料箱拣选方法，将用于平面抓取奖励估计的全卷积神经网络与用于侧向朝向自适应的基于模型控制器相结合，在 27,000 次自监督真实世界抓取尝试后，于密集
    clutter 中实现了超过 92% 的抓取成功率，推理时间低于 50 毫秒。
  ko: 본 논문은 평면 그래스프 보상 추정을 위한 완전 컨볼루션 신경망과 측면 방향 적응을 위한 모델 기반 컨트롤러를 결합한 하이브리드 6자유도
    빈 피킹 접근법을 제안하며, 27,000회의 자기 감독 실제 그래스프 시도 후 밀집된 clutter에서 92% 이상의 그래스프 성공률과 50ms
    미만의 추론 시간을 달성하였다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review is required
    to confirm section-level citations and exact quantitative claims.
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

## Overview

The paper addresses the limitation that robot learning for grasping is often reduced to planar 4-DoF manipulation to limit data consumption. It proposes a hybrid method for 6-DoF bin picking in which a fully-convolutional neural network (FCNN) estimates planar grasp rewards, while a fixed model-based controller calculates the two remaining lateral orientation degrees of freedom (angles b and c). The controller is designed to avoid collisions with the bin or other objects, maximize antipodal grasp quality, and keep orientation uncertainty small.

The model-based controller is integrated into the real-world self-supervised training loop, allowing the FCNN to learn about and exploit the controller rather than treating it as a post-processing step. After approximately 27,000 real-world grasp attempts over about 120 hours, the system grasps known objects with over 92% success in dense clutter, with inference taking less than 50 ms. Additional experiments evaluate generalization to unknown objects, performance with short gripper fingers, and the importance of integrating the controller during training.

## Key Contributions

- Hybrid 6-DoF grasping that combines learned planar grasp evaluation with model-based lateral angle adaptation.
- Model-based controller that calculates lateral angles for collision avoidance, antipodal grasp quality maximization, and uncertainty minimization.
- Integration of the model-based controller into the real-world self-supervised training loop so the FCNN learns to exploit it.
- Real-world evaluation showing over 92% grasp success in dense clutter and inference under 50 ms.
- Demonstration of generalization to unknown objects and robust performance with short gripper fingers.

## Relevance to Humanoid Robotics

Although the experiments use an industrial Franka Panda arm rather than a full humanoid, the core contribution—fast, collision-aware 6-DoF grasp primitive adaptation—is directly transferable to end-effector manipulation modules in humanoid robots. The sub-50 ms inference time and the use of low-cost RGB-D sensing align with the real-time, unstructured-environment requirements typical of warehouse, manufacturing, and service deployments for humanoids. The hybrid learning-plus-model-based-control architecture also offers a practical path to data-efficient manipulation skill acquisition on humanoid platforms.
