---
$id: ent_paper_top_time_optimization_policy_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots'
  zh: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots'
  ko: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots'
summary:
  en: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots is a 2025 work on
    manipulation for humanoid robots.'
  zh: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots is a 2025 work on
    manipulation for humanoid robots.'
  ko: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots is a 2025 work on
    manipulation for humanoid robots.'
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
- manipulation
- top
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.00355v1.
sources:
- id: src_001
  type: paper
  title: 'TOP: Time Optimization Policy for Stable and Accurate Standing Manipulation with Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2508.00355
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have the potential capability to perform a diverse range of manipulation tasks, but this is based on a robust and precise standing controller. Existing methods are either ill-suited to precisely control high-dimensional upper-body joints, or difficult to ensure both robustness and accuracy, especially when upper-body motions are fast. This paper proposes a novel time optimization policy (TOP), to train a standing manipulation control model that ensures balance, precision, and time efficiency simultaneously, with the idea of adjusting the time trajectory of upper-body motions but not only strengthening the disturbance resistance of the lower-body. Our approach consists of three parts. Firstly, we utilize motion prior to represent upper-body motions to enhance the coordination ability between the upper and lower-body by training a variational autoencoder (VAE). Then we decouple the whole-body control into an upper-body PD controller for precision and a lower-body RL controller to enhance robust stability. Finally, we train TOP method in conjunction with the decoupled controller and VAE to reduce the balance burden resulting from fast upper-body motions that would destabilize the robot and exceed the capabilities of the lower-body RL policy. The effectiveness of the proposed approach is evaluated via both simulation and real world experiments, which demonstrate the superiority on standing manipulation tasks stably and accurately. The project page can be found at https://anonymous.4open.science/w/top-258F/.

## 核心内容
Humanoid robots have the potential capability to perform a diverse range of manipulation tasks, but this is based on a robust and precise standing controller. Existing methods are either ill-suited to precisely control high-dimensional upper-body joints, or difficult to ensure both robustness and accuracy, especially when upper-body motions are fast. This paper proposes a novel time optimization policy (TOP), to train a standing manipulation control model that ensures balance, precision, and time efficiency simultaneously, with the idea of adjusting the time trajectory of upper-body motions but not only strengthening the disturbance resistance of the lower-body. Our approach consists of three parts. Firstly, we utilize motion prior to represent upper-body motions to enhance the coordination ability between the upper and lower-body by training a variational autoencoder (VAE). Then we decouple the whole-body control into an upper-body PD controller for precision and a lower-body RL controller to enhance robust stability. Finally, we train TOP method in conjunction with the decoupled controller and VAE to reduce the balance burden resulting from fast upper-body motions that would destabilize the robot and exceed the capabilities of the lower-body RL policy. The effectiveness of the proposed approach is evaluated via both simulation and real world experiments, which demonstrate the superiority on standing manipulation tasks stably and accurately. The project page can be found at https://anonymous.4open.science/w/top-258F/.

## 参考
- http://arxiv.org/abs/2508.00355v1

## Overview
Humanoid robots have the potential capability to perform a diverse range of manipulation tasks, but this is based on a robust and precise standing controller. Existing methods are either ill-suited to precisely control high-dimensional upper-body joints, or difficult to ensure both robustness and accuracy, especially when upper-body motions are fast. This paper proposes a novel time optimization policy (TOP), to train a standing manipulation control model that ensures balance, precision, and time efficiency simultaneously, with the idea of adjusting the time trajectory of upper-body motions but not only strengthening the disturbance resistance of the lower-body. Our approach consists of three parts. Firstly, we utilize motion prior to represent upper-body motions to enhance the coordination ability between the upper and lower-body by training a variational autoencoder (VAE). Then we decouple the whole-body control into an upper-body PD controller for precision and a lower-body RL controller to enhance robust stability. Finally, we train TOP method in conjunction with the decoupled controller and VAE to reduce the balance burden resulting from fast upper-body motions that would destabilize the robot and exceed the capabilities of the lower-body RL policy. The effectiveness of the proposed approach is evaluated via both simulation and real world experiments, which demonstrate the superiority on standing manipulation tasks stably and accurately. The project page can be found at https://anonymous.4open.science/w/top-258F/.

## Content
Humanoid robots have the potential capability to perform a diverse range of manipulation tasks, but this is based on a robust and precise standing controller. Existing methods are either ill-suited to precisely control high-dimensional upper-body joints, or difficult to ensure both robustness and accuracy, especially when upper-body motions are fast. This paper proposes a novel time optimization policy (TOP), to train a standing manipulation control model that ensures balance, precision, and time efficiency simultaneously, with the idea of adjusting the time trajectory of upper-body motions but not only strengthening the disturbance resistance of the lower-body. Our approach consists of three parts. Firstly, we utilize motion prior to represent upper-body motions to enhance the coordination ability between the upper and lower-body by training a variational autoencoder (VAE). Then we decouple the whole-body control into an upper-body PD controller for precision and a lower-body RL controller to enhance robust stability. Finally, we train TOP method in conjunction with the decoupled controller and VAE to reduce the balance burden resulting from fast upper-body motions that would destabilize the robot and exceed the capabilities of the lower-body RL policy. The effectiveness of the proposed approach is evaluated via both simulation and real world experiments, which demonstrate the superiority on standing manipulation tasks stably and accurately. The project page can be found at https://anonymous.4open.science/w/top-258F/.

## 개요
휴머노이드 로봇은 다양한 조작 작업을 수행할 수 있는 잠재적 능력을 가지고 있지만, 이는 강건하고 정밀한 서 있는 자세 제어기를 기반으로 합니다. 기존 방법들은 고차원 상체 관절을 정밀하게 제어하기에 부적합하거나, 특히 상체 움직임이 빠를 때 강건성과 정밀성을 동시에 보장하기 어렵습니다. 본 논문은 하체의 외란 저항성 강화뿐만 아니라 상체 움직임의 시간 궤적을 조정하는 아이디어를 통해 균형, 정밀성, 시간 효율성을 동시에 보장하는 서 있는 자세 조작 제어 모델을 훈련하기 위한 새로운 시간 최적화 정책(TOP)을 제안합니다. 우리의 접근 방식은 세 부분으로 구성됩니다. 첫째, 변분 오토인코더(VAE)를 훈련하여 상체 움직임을 표현하는 동작 사전을 활용함으로써 상체와 하체 간의 협응 능력을 향상시킵니다. 그런 다음 전신 제어를 정밀성을 위한 상체 PD 제어기와 강건한 안정성 향상을 위한 하체 RL 제어기로 분리합니다. 마지막으로, 분리된 제어기 및 VAE와 함께 TOP 방법을 훈련하여 로봇을 불안정하게 만들고 하체 RL 정책의 능력을 초과하는 빠른 상체 움직임으로 인한 균형 부담을 줄입니다. 제안된 접근 방식의 효과는 시뮬레이션 및 실제 실험을 통해 평가되었으며, 서 있는 자세 조작 작업을 안정적이고 정확하게 수행하는 데 있어 우수성을 입증했습니다. 프로젝트 페이지는 https://anonymous.4open.science/w/top-258F/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇은 다양한 조작 작업을 수행할 수 있는 잠재적 능력을 가지고 있지만, 이는 강건하고 정밀한 서 있는 자세 제어기를 기반으로 합니다. 기존 방법들은 고차원 상체 관절을 정밀하게 제어하기에 부적합하거나, 특히 상체 움직임이 빠를 때 강건성과 정밀성을 동시에 보장하기 어렵습니다. 본 논문은 하체의 외란 저항성 강화뿐만 아니라 상체 움직임의 시간 궤적을 조정하는 아이디어를 통해 균형, 정밀성, 시간 효율성을 동시에 보장하는 서 있는 자세 조작 제어 모델을 훈련하기 위한 새로운 시간 최적화 정책(TOP)을 제안합니다. 우리의 접근 방식은 세 부분으로 구성됩니다. 첫째, 변분 오토인코더(VAE)를 훈련하여 상체 움직임을 표현하는 동작 사전을 활용함으로써 상체와 하체 간의 협응 능력을 향상시킵니다. 그런 다음 전신 제어를 정밀성을 위한 상체 PD 제어기와 강건한 안정성 향상을 위한 하체 RL 제어기로 분리합니다. 마지막으로, 분리된 제어기 및 VAE와 함께 TOP 방법을 훈련하여 로봇을 불안정하게 만들고 하체 RL 정책의 능력을 초과하는 빠른 상체 움직임으로 인한 균형 부담을 줄입니다. 제안된 접근 방식의 효과는 시뮬레이션 및 실제 실험을 통해 평가되었으며, 서 있는 자세 조작 작업을 안정적이고 정확하게 수행하는 데 있어 우수성을 입증했습니다. 프로젝트 페이지는 https://anonymous.4open.science/w/top-258F/에서 확인할 수 있습니다.
