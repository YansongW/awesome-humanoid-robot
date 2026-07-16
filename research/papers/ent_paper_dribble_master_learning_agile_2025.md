---
$id: ent_paper_dribble_master_learning_agile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
  zh: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
  ko: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
summary:
  en: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dribble_master
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12679v3.
sources:
- id: src_001
  type: paper
  title: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.12679
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## 核心内容
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## 参考
- http://arxiv.org/abs/2505.12679v3

## Overview
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## Content
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## 개요
휴머노이드 축구 드리블은 동적 균형을 유지하면서 정교한 공 조작을 요구하는 매우 도전적인 과제입니다. 기존의 규칙 기반 방법은 고정된 보행 패턴에 의존하고 실시간 공 역학에 대한 적응성이 제한적이어서 정확한 공 제어를 달성하는 데 어려움을 겪는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 명시적인 동역학이나 사전 정의된 궤적 없이 휴머노이드 로봇이 드리블 기술을 습득할 수 있도록 하는 2단계 커리큘럼 학습 프레임워크를 제안합니다. 첫 번째 단계에서 로봇은 기본적인 보행 기술을 학습하고, 두 번째 단계에서는 민첩한 드리블 동작을 위해 정책을 미세 조정합니다. 또한, 실제 로봇의 시야와 인식 제약 조건을 시뮬레이션하는 가상 카메라 모델을 시뮬레이션에 도입하여 훈련 중 현실적인 공 인식을 가능하게 합니다. 또한, 능동적 감지를 장려하는 휴리스틱 보상을 설계하여 지속적인 공 인식을 위한 더 넓은 시각적 범위를 촉진합니다. 정책은 시뮬레이션에서 훈련되고 실제 휴머노이드 로봇으로 성공적으로 전이됩니다. 실험 결과는 우리의 방법이 여러 환경에서 유연하고 시각적으로 매력적인 드리블 동작을 달성하여 효과적인 공 조작을 가능하게 함을 보여줍니다. 이 연구는 민첩한 휴머노이드 축구 로봇 개발에 있어 강화 학습의 잠재력을 강조합니다. 추가 세부 사항과 비디오는 https://zhuoheng0910.github.io/dribble-master/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 축구 드리블은 동적 균형을 유지하면서 정교한 공 조작을 요구하는 매우 도전적인 과제입니다. 기존의 규칙 기반 방법은 고정된 보행 패턴에 의존하고 실시간 공 역학에 대한 적응성이 제한적이어서 정확한 공 제어를 달성하는 데 어려움을 겪는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 명시적인 동역학이나 사전 정의된 궤적 없이 휴머노이드 로봇이 드리블 기술을 습득할 수 있도록 하는 2단계 커리큘럼 학습 프레임워크를 제안합니다. 첫 번째 단계에서 로봇은 기본적인 보행 기술을 학습하고, 두 번째 단계에서는 민첩한 드리블 동작을 위해 정책을 미세 조정합니다. 또한, 실제 로봇의 시야와 인식 제약 조건을 시뮬레이션하는 가상 카메라 모델을 시뮬레이션에 도입하여 훈련 중 현실적인 공 인식을 가능하게 합니다. 또한, 능동적 감지를 장려하는 휴리스틱 보상을 설계하여 지속적인 공 인식을 위한 더 넓은 시각적 범위를 촉진합니다. 정책은 시뮬레이션에서 훈련되고 실제 휴머노이드 로봇으로 성공적으로 전이됩니다. 실험 결과는 우리의 방법이 여러 환경에서 유연하고 시각적으로 매력적인 드리블 동작을 달성하여 효과적인 공 조작을 가능하게 함을 보여줍니다. 이 연구는 민첩한 휴머노이드 축구 로봇 개발에 있어 강화 학습의 잠재력을 강조합니다. 추가 세부 사항과 비디오는 https://zhuoheng0910.github.io/dribble-master/에서 확인할 수 있습니다.
