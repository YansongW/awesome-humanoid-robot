---
$id: ent_paper_pan_vision_language_action_model_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
  zh: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
  ko: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
summary:
  en: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
  zh: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
  ko: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand (Vision-Language-Action
    Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Swiss Federal Institute of Technology Lausanne.
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
- robotic_manipulation
- vision_language_action
- vision_language_action_model_a
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14022v2.
sources:
- id: src_001
  type: paper
  title: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
    (arXiv)
  url: https://arxiv.org/abs/2410.14022
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Vision-Language-Action Model and Diffusion Policy Switching Enables Dexterous Control of an Anthropomorphic Hand
    source
  url: https://doi.org/10.48550/arXiv.2410.14022
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## 核心内容
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## 参考
- http://arxiv.org/abs/2410.14022v2

## Overview
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## Content
Human dexterity arises from combining high-level task reasoning with finger-level dexterity control and physical compliance at the muscle and skin layers. In robotics, large Vision-Language-Action (VLA) models demonstrate text-conditioned high-level planning across diverse manipulation tasks, typically using pincher grippers. Smaller imitation-learning policies, conversely, show success in dexterous tasks using higher degree-of-freedom (DoF) grippers, but only for limited-scope tasks. However, few approaches combine high-level reasoning with dexterous, robust low-level control, which requires both intelligent control and compliant robot design. We propose a method inspired by the two-channel hypothesis of human motor control that combines these capabilities using a switching controller integrating high-level VLAs and smaller control models. Coordination between the two channels is managed through an event-driven switching mechanism that monitors subtask progression and completion, requiring minimal demonstration data by fine-tuning the VLA to predict event signals and training lightweight subtask-level dexterous policies. This approach is applied to our custom compliant 13-DoF anthropomorphic robotic hand, where compliance can be modulated to evaluate its impact on dexterity and robustness when combined with an autonomous policy. We show that hardware-level compliance in robotic fingers enables passive adaptation to disturbances and improves contact stability. The methodology is validated across a range of language-conditioned dexterous tasks. To demonstrate modularity, we show that adaptation to additional dexterous skills and different compliant hands can be achieved without retraining the VLA model. This provides an efficient, scalable, cross-embodiment approach to dexterity that leverages compliance while retaining the advantages of large AI models.

## 개요
인간의 손재주는 고수준 작업 추론과 손가락 수준의 손재주 제어, 그리고 근육 및 피부 층에서의 물리적 순응성을 결합하여 발생합니다. 로봇 공학에서 대규모 Vision-Language-Action(VLA) 모델은 일반적으로 핀셔 그리퍼를 사용하여 다양한 조작 작업에서 텍스트 조건부 고수준 계획을 보여줍니다. 반면, 소규모 모방 학습 정책은 더 높은 자유도(DoF) 그리퍼를 사용하여 손재주가 필요한 작업에서 성공을 보여주지만, 제한된 범위의 작업에만 적용됩니다. 그러나 고수준 추론과 손재주 있고 강건한 저수준 제어를 결합하는 접근 방식은 거의 없으며, 이는 지능적인 제어와 순응적인 로봇 설계를 모두 필요로 합니다. 우리는 인간 운동 제어의 이중 채널 가설에서 영감을 받아 고수준 VLA와 소규모 제어 모델을 통합하는 스위칭 컨트롤러를 사용하여 이러한 기능을 결합하는 방법을 제안합니다. 두 채널 간의 조정은 이벤트 기반 스위칭 메커니즘을 통해 관리되며, 이는 하위 작업 진행 및 완료를 모니터링합니다. VLA를 미세 조정하여 이벤트 신호를 예측하고 경량의 하위 작업 수준 손재주 정책을 훈련함으로써 최소한의 시연 데이터만 필요로 합니다. 이 접근 방식은 당사의 맞춤형 순응형 13-DoF 인간형 로봇 손에 적용되며, 순응성을 조절하여 자율 정책과 결합했을 때 손재주와 강건성에 미치는 영향을 평가할 수 있습니다. 우리는 로봇 손가락의 하드웨어 수준 순응성이 교란에 대한 수동적 적응을 가능하게 하고 접촉 안정성을 향상시킨다는 것을 보여줍니다. 이 방법론은 다양한 언어 조건부 손재주 작업에서 검증됩니다. 모듈성을 입증하기 위해 VLA 모델을 재훈련하지 않고도 추가 손재주 기술과 다른 순응형 손에 적응할 수 있음을 보여줍니다. 이는 대규모 AI 모델의 장점을 유지하면서 순응성을 활용하는 효율적이고 확장 가능한 교차 체현 손재주 접근 방식을 제공합니다.

## 핵심 내용
인간의 손재주는 고수준 작업 추론과 손가락 수준의 손재주 제어, 그리고 근육 및 피부 층에서의 물리적 순응성을 결합하여 발생합니다. 로봇 공학에서 대규모 Vision-Language-Action(VLA) 모델은 일반적으로 핀셔 그리퍼를 사용하여 다양한 조작 작업에서 텍스트 조건부 고수준 계획을 보여줍니다. 반면, 소규모 모방 학습 정책은 더 높은 자유도(DoF) 그리퍼를 사용하여 손재주가 필요한 작업에서 성공을 보여주지만, 제한된 범위의 작업에만 적용됩니다. 그러나 고수준 추론과 손재주 있고 강건한 저수준 제어를 결합하는 접근 방식은 거의 없으며, 이는 지능적인 제어와 순응적인 로봇 설계를 모두 필요로 합니다. 우리는 인간 운동 제어의 이중 채널 가설에서 영감을 받아 고수준 VLA와 소규모 제어 모델을 통합하는 스위칭 컨트롤러를 사용하여 이러한 기능을 결합하는 방법을 제안합니다. 두 채널 간의 조정은 이벤트 기반 스위칭 메커니즘을 통해 관리되며, 이는 하위 작업 진행 및 완료를 모니터링합니다. VLA를 미세 조정하여 이벤트 신호를 예측하고 경량의 하위 작업 수준 손재주 정책을 훈련함으로써 최소한의 시연 데이터만 필요로 합니다. 이 접근 방식은 당사의 맞춤형 순응형 13-DoF 인간형 로봇 손에 적용되며, 순응성을 조절하여 자율 정책과 결합했을 때 손재주와 강건성에 미치는 영향을 평가할 수 있습니다. 우리는 로봇 손가락의 하드웨어 수준 순응성이 교란에 대한 수동적 적응을 가능하게 하고 접촉 안정성을 향상시킨다는 것을 보여줍니다. 이 방법론은 다양한 언어 조건부 손재주 작업에서 검증됩니다. 모듈성을 입증하기 위해 VLA 모델을 재훈련하지 않고도 추가 손재주 기술과 다른 순응형 손에 적응할 수 있음을 보여줍니다. 이는 대규모 AI 모델의 장점을 유지하면서 순응성을 활용하는 효율적이고 확장 가능한 교차 체현 손재주 접근 방식을 제공합니다.
