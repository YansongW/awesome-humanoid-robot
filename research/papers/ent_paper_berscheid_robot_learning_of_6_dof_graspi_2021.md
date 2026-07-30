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
  zh: 本文提出一种混合6自由度（6-DoF）抓取方法，结合全卷积神经网络进行平面抓取奖励估计，并引入基于模型的控制器实现侧向姿态自适应调整。经过27,000次自监督抓取尝试后，该方法在密集杂乱场景中实现了超过92%的真实世界抓取成功率，推理时间低于50毫秒。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2103.12810v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
机器人学习常因数据消耗问题被简化为平面操作，常见方案是使用全卷积神经网络估计抓取基元的奖励。本文通过参数化基元中剩余的两个侧向自由度（DoFs），将这一方法扩展到6自由度抓取任务。核心创新在于引入基于模型的控制器，用于计算避免碰撞、最大化抓取质量并保持不确定性的角度。该控制器被集成到训练过程中，使混合系统能够学习并利用基于模型的控制器。经过27,000次真实世界训练尝试后，机器人对已知物体在密集杂乱场景中的抓取成功率超过92%，推理时间低于50毫秒。进一步实验评估了系统在多种场景下的抓取率，包括对未知物体的泛化能力，并证明系统能够避免碰撞，实现无基元自适应时无法完成的抓取。

## 核心内容
### 方法概述
- 本文提出一种混合6自由度抓取方法，结合全卷积神经网络（fully-convolutional neural network）与基于模型的控制器（model-based controller）。
- 全卷积神经网络用于估计平面抓取基元的奖励，而控制器则参数化剩余的两个侧向自由度（lateral Degrees of Freedom, DoFs），实现姿态自适应调整。

### 架构与训练
- 控制器计算角度时，同时考虑三个目标：避免碰撞（collision avoidance）、最大化抓取质量（maximize grasp quality）以及保持不确定性最小化（keep uncertainty small）。
- 控制器被集成到训练流程中，使混合系统能够通过自监督学习（self-supervised learning）逐步学习并利用控制器的输出。
- 真实世界训练共进行27,000次抓取尝试（grasp attempts），每次推理时间低于50毫秒。

### 实验设置与结果
- 在密集杂乱场景（dense clutter）中，机器人对已知物体的抓取成功率超过92%。
- 进一步实验评估了系统在多种场景下的抓取率，包括对未知物体（unknown objects）的泛化能力。
- 实验证明，系统能够有效避免碰撞，实现无基元自适应（primitive adaptation）时无法完成的抓取动作。

### 结论
- 本文方法通过混合架构，在保持低推理延迟的同时，显著提升了6自由度抓取在杂乱环境中的成功率与鲁棒性。

## Overview
Robot learning is often simplified to planar manipulation due to its data consumption. Then, a common approach is to use a fully-convolutional neural network to estimate the reward of grasp primitives. In this work, we extend this approach by parametrizing the two remaining, lateral Degrees of Freedom (DoFs) of the primitives. We apply this principle to the task of 6 DoF bin picking: We introduce a model-based controller to calculate angles that avoid collisions, maximize the grasp quality while keeping the uncertainty small. As the controller is integrated into the training, our hybrid approach is able to learn about and exploit the model-based controller. After real-world training of 27000 grasp attempts, the robot is able to grasp known objects with a success rate of over 92% in dense clutter. Grasp inference takes less than 50ms. In further real-world experiments, we evaluate grasp rates in a range of scenarios including its ability to generalize to unknown objects. We show that the system is able to avoid collisions, enabling grasps that would not be possible without primitive adaption.

## 개요
로봇 학습은 데이터 소비 문제로 인해 종종 평면 조작으로 단순화됩니다. 이후 일반적인 접근 방식은 완전 컨볼루션 신경망을 사용하여 그립 프리미티브의 보상을 추정하는 것입니다. 본 연구에서는 프리미티브의 나머지 두 개의 측면 자유도를 매개변수화하여 이 접근 방식을 확장합니다. 이 원리를 6자유도 빈 피킹 작업에 적용합니다: 충돌을 피하고, 그립 품질을 최대화하며 불확실성을 최소화하는 각도를 계산하는 모델 기반 제어기를 도입합니다. 제어기가 훈련에 통합됨에 따라, 우리의 하이브리드 접근 방식은 모델 기반 제어기에 대해 학습하고 이를 활용할 수 있습니다. 27,000회의 실제 그립 시도 훈련 후, 로봇은 밀집된 혼잡 환경에서 알려진 물체를 92% 이상의 성공률로 잡을 수 있습니다. 그립 추론은 50ms 미만이 소요됩니다. 추가 실제 실험에서는 알려지지 않은 물체에 대한 일반화 능력을 포함한 다양한 시나리오에서 그립 성공률을 평가합니다. 우리는 시스템이 충돌을 피할 수 있어 프리미티브 적응 없이는 불가능했던 그립을 가능하게 함을 보여줍니다.

## 핵심 내용
로봇 학습은 데이터 소비 문제로 인해 종종 평면 조작으로 단순화됩니다. 이후 일반적인 접근 방식은 완전 컨볼루션 신경망을 사용하여 그립 프리미티브의 보상을 추정하는 것입니다. 본 연구에서는 프리미티브의 나머지 두 개의 측면 자유도를 매개변수화하여 이 접근 방식을 확장합니다. 이 원리를 6자유도 빈 피킹 작업에 적용합니다: 충돌을 피하고, 그립 품질을 최대화하며 불확실성을 최소화하는 각도를 계산하는 모델 기반 제어기를 도입합니다. 제어기가 훈련에 통합됨에 따라, 우리의 하이브리드 접근 방식은 모델 기반 제어기에 대해 학습하고 이를 활용할 수 있습니다. 27,000회의 실제 그립 시도 훈련 후, 로봇은 밀집된 혼잡 환경에서 알려진 물체를 92% 이상의 성공률로 잡을 수 있습니다. 그립 추론은 50ms 미만이 소요됩니다. 추가 실제 실험에서는 알려지지 않은 물체에 대한 일반화 능력을 포함한 다양한 시나리오에서 그립 성공률을 평가합니다. 우리는 시스템이 충돌을 피할 수 있어 프리미티브 적응 없이는 불가능했던 그립을 가능하게 함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2103.12810v1
