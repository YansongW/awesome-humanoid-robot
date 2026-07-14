---
$id: ent_paper_johns_coarse_to_fine_imitation_learn_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration'
  zh: 从粗到精的模仿学习：单演示下的机器人操作
  ko: 'Coarse-to-Fine 모방 학습: 단일 시연으로부터의 로봇 조작'
summary:
  en: Johns (2021) proposes a visual imitation-learning method that learns a novel manipulation task from a single human demonstration
    by estimating the end-effector's bottleneck pose and replaying the demonstration's end-effector velocities from that pose.
  zh: Johns（2021）提出了一种视觉模仿学习方法，通过估计末端执行器的瓶颈位姿并从此位姿开始回放演示的末端执行器速度，从单条人类演示中学习新的操作任务。
  ko: Johns(2021)은 엔드이펙터의 병목 자세를 추정하고 해당 자세부터 시연의 엔드이펙터 속도를 재생함으로써 단일 인간 시연으로부터 새로운 조작 작업을 학습하는 시각적 모방 학습 방법을 제안한다.
domains:
- 07_ai_models_algorithms
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- imitation_learning
- single_demonstration_learning
- visual_imitation
- bottleneck_pose_estimation
- end_effector_velocity_replay
- self_supervised_learning
- manipulation
- sawyer_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2105.06411v2.
sources:
- id: src_001
  type: paper
  title: 'Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration'
  url: https://arxiv.org/abs/2105.06411
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the point where object interaction begins, as observed from the demonstration. By then modelling a manipulation task as a coarse, approach trajectory followed by a fine, interaction trajectory, this state estimator can be trained in a self-supervised manner, by automatically moving the end-effector's camera around the object. At test time, the end-effector moves to the estimated state through a linear path, at which point the original demonstration's end-effector velocities are simply replayed. This enables convenient acquisition of a complex interaction trajectory, without actually needing to explicitly learn a policy. Real-world experiments on 8 everyday tasks show that our method can learn a diverse range of skills from a single human demonstration, whilst also yielding a stable and interpretable controller.

## 核心内容
We introduce a simple new method for visual imitation learning, which allows a novel robot manipulation task to be learned from a single human demonstration, without requiring any prior knowledge of the object being interacted with. Our method models imitation learning as a state estimation problem, with the state defined as the end-effector's pose at the point where object interaction begins, as observed from the demonstration. By then modelling a manipulation task as a coarse, approach trajectory followed by a fine, interaction trajectory, this state estimator can be trained in a self-supervised manner, by automatically moving the end-effector's camera around the object. At test time, the end-effector moves to the estimated state through a linear path, at which point the original demonstration's end-effector velocities are simply replayed. This enables convenient acquisition of a complex interaction trajectory, without actually needing to explicitly learn a policy. Real-world experiments on 8 everyday tasks show that our method can learn a diverse range of skills from a single human demonstration, whilst also yielding a stable and interpretable controller.

## 参考
- http://arxiv.org/abs/2105.06411v2

