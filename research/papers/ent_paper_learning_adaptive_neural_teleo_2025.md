---
$id: ent_paper_learning_adaptive_neural_teleo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Adaptive Neural Teleoperation for Humanoid Robots
  zh: Learning Adaptive Neural Teleoperation for Humanoid Robots
  ko: Learning Adaptive Neural Teleoperation for Humanoid Robots
summary:
  en: Learning Adaptive Neural Teleoperation for Humanoid Robots is a 2025 work on teleoperation for humanoid robots.
  zh: Learning Adaptive Neural Teleoperation for Humanoid Robots is a 2025 work on teleoperation for humanoid robots.
  ko: Learning Adaptive Neural Teleoperation for Humanoid Robots is a 2025 work on teleoperation for humanoid robots.
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
- learning_adaptive_neural_teleo
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.12390v1.
sources:
- id: src_001
  type: paper
  title: Learning Adaptive Neural Teleoperation for Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2511.12390
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Virtual reality (VR) teleoperation has emerged as a promising approach for controlling humanoid robots in complex manipulation tasks. However, traditional teleoperation systems rely on inverse kinematics (IK) solvers and hand-tuned PD controllers, which struggle to handle external forces, adapt to different users, and produce natural motions under dynamic conditions. In this work, we propose a learning-based neural teleoperation framework that replaces the conventional IK+PD pipeline with learned policies trained via reinforcement learning. Our approach learns to directly map VR controller inputs to robot joint commands while implicitly handling force disturbances, producing smooth trajectories, and adapting to user preferences. We train our policies in simulation using demonstrations collected from IK-based teleoperation as initialization, then fine-tune them with force randomization and trajectory smoothness rewards. Experiments on the Unitree G1 humanoid robot demonstrate that our learned policies achieve 34% lower tracking error, 45% smoother motions, and superior force adaptation compared to the IK baseline, while maintaining real-time performance (50Hz control frequency). We validate our approach on manipulation tasks including object pick-and-place, door opening, and bimanual coordination. These results suggest that learning-based approaches can significantly improve the naturalness and robustness of humanoid teleoperation systems.

## 核心内容
Virtual reality (VR) teleoperation has emerged as a promising approach for controlling humanoid robots in complex manipulation tasks. However, traditional teleoperation systems rely on inverse kinematics (IK) solvers and hand-tuned PD controllers, which struggle to handle external forces, adapt to different users, and produce natural motions under dynamic conditions. In this work, we propose a learning-based neural teleoperation framework that replaces the conventional IK+PD pipeline with learned policies trained via reinforcement learning. Our approach learns to directly map VR controller inputs to robot joint commands while implicitly handling force disturbances, producing smooth trajectories, and adapting to user preferences. We train our policies in simulation using demonstrations collected from IK-based teleoperation as initialization, then fine-tune them with force randomization and trajectory smoothness rewards. Experiments on the Unitree G1 humanoid robot demonstrate that our learned policies achieve 34% lower tracking error, 45% smoother motions, and superior force adaptation compared to the IK baseline, while maintaining real-time performance (50Hz control frequency). We validate our approach on manipulation tasks including object pick-and-place, door opening, and bimanual coordination. These results suggest that learning-based approaches can significantly improve the naturalness and robustness of humanoid teleoperation systems.

## 参考
- http://arxiv.org/abs/2511.12390v1

## Overview
Virtual reality (VR) teleoperation has emerged as a promising approach for controlling humanoid robots in complex manipulation tasks. However, traditional teleoperation systems rely on inverse kinematics (IK) solvers and hand-tuned PD controllers, which struggle to handle external forces, adapt to different users, and produce natural motions under dynamic conditions. In this work, we propose a learning-based neural teleoperation framework that replaces the conventional IK+PD pipeline with learned policies trained via reinforcement learning. Our approach learns to directly map VR controller inputs to robot joint commands while implicitly handling force disturbances, producing smooth trajectories, and adapting to user preferences. We train our policies in simulation using demonstrations collected from IK-based teleoperation as initialization, then fine-tune them with force randomization and trajectory smoothness rewards. Experiments on the Unitree G1 humanoid robot demonstrate that our learned policies achieve 34% lower tracking error, 45% smoother motions, and superior force adaptation compared to the IK baseline, while maintaining real-time performance (50Hz control frequency). We validate our approach on manipulation tasks including object pick-and-place, door opening, and bimanual coordination. These results suggest that learning-based approaches can significantly improve the naturalness and robustness of humanoid teleoperation systems.

## Content
Virtual reality (VR) teleoperation has emerged as a promising approach for controlling humanoid robots in complex manipulation tasks. However, traditional teleoperation systems rely on inverse kinematics (IK) solvers and hand-tuned PD controllers, which struggle to handle external forces, adapt to different users, and produce natural motions under dynamic conditions. In this work, we propose a learning-based neural teleoperation framework that replaces the conventional IK+PD pipeline with learned policies trained via reinforcement learning. Our approach learns to directly map VR controller inputs to robot joint commands while implicitly handling force disturbances, producing smooth trajectories, and adapting to user preferences. We train our policies in simulation using demonstrations collected from IK-based teleoperation as initialization, then fine-tune them with force randomization and trajectory smoothness rewards. Experiments on the Unitree G1 humanoid robot demonstrate that our learned policies achieve 34% lower tracking error, 45% smoother motions, and superior force adaptation compared to the IK baseline, while maintaining real-time performance (50Hz control frequency). We validate our approach on manipulation tasks including object pick-and-place, door opening, and bimanual coordination. These results suggest that learning-based approaches can significantly improve the naturalness and robustness of humanoid teleoperation systems.

## 개요
가상 현실(VR) 원격 조작은 복잡한 조작 작업에서 휴머노이드 로봇을 제어하기 위한 유망한 접근 방식으로 부상했습니다. 그러나 기존의 원격 조작 시스템은 역기구학(IK) 솔버와 수동 조정 PD 제어기에 의존하여 외부 힘을 처리하고, 다양한 사용자에 적응하며, 동적 조건에서 자연스러운 동작을 생성하는 데 어려움을 겪습니다. 본 연구에서는 강화 학습을 통해 훈련된 학습 기반 정책으로 기존의 IK+PD 파이프라인을 대체하는 학습 기반 신경 원격 조작 프레임워크를 제안합니다. 우리의 접근 방식은 VR 컨트롤러 입력을 로봇 관절 명령에 직접 매핑하면서, 힘 교란을 암시적으로 처리하고, 부드러운 궤적을 생성하며, 사용자 선호도에 적응하는 방법을 학습합니다. 우리는 IK 기반 원격 조작에서 수집한 시연을 초기화로 사용하여 시뮬레이션에서 정책을 훈련한 후, 힘 무작위화와 궤적 부드러움 보상으로 미세 조정합니다. Unitree G1 휴머노이드 로봇 실험에서 학습된 정책이 IK 기준선 대비 추적 오차 34% 감소, 동작 부드러움 45% 향상, 우수한 힘 적응을 달성하면서 실시간 성능(50Hz 제어 주파수)을 유지함을 입증했습니다. 우리는 물체 집기 및 놓기, 문 열기, 양손 협업을 포함한 조작 작업에서 접근 방식을 검증했습니다. 이러한 결과는 학습 기반 접근 방식이 휴머노이드 원격 조작 시스템의 자연스러움과 견고성을 크게 향상시킬 수 있음을 시사합니다.

## 핵심 내용
가상 현실(VR) 원격 조작은 복잡한 조작 작업에서 휴머노이드 로봇을 제어하기 위한 유망한 접근 방식으로 부상했습니다. 그러나 기존의 원격 조작 시스템은 역기구학(IK) 솔버와 수동 조정 PD 제어기에 의존하여 외부 힘을 처리하고, 다양한 사용자에 적응하며, 동적 조건에서 자연스러운 동작을 생성하는 데 어려움을 겪습니다. 본 연구에서는 강화 학습을 통해 훈련된 학습 기반 정책으로 기존의 IK+PD 파이프라인을 대체하는 학습 기반 신경 원격 조작 프레임워크를 제안합니다. 우리의 접근 방식은 VR 컨트롤러 입력을 로봇 관절 명령에 직접 매핑하면서, 힘 교란을 암시적으로 처리하고, 부드러운 궤적을 생성하며, 사용자 선호도에 적응하는 방법을 학습합니다. 우리는 IK 기반 원격 조작에서 수집한 시연을 초기화로 사용하여 시뮬레이션에서 정책을 훈련한 후, 힘 무작위화와 궤적 부드러움 보상으로 미세 조정합니다. Unitree G1 휴머노이드 로봇 실험에서 학습된 정책이 IK 기준선 대비 추적 오차 34% 감소, 동작 부드러움 45% 향상, 우수한 힘 적응을 달성하면서 실시간 성능(50Hz 제어 주파수)을 유지함을 입증했습니다. 우리는 물체 집기 및 놓기, 문 열기, 양손 협업을 포함한 조작 작업에서 접근 방식을 검증했습니다. 이러한 결과는 학습 기반 접근 방식이 휴머노이드 원격 조작 시스템의 자연스러움과 견고성을 크게 향상시킬 수 있음을 시사합니다.
