---
$id: ent_paper_wen_diffusion_vla_scaling_robot_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression'
  zh: Diffusion-VLA
  ko: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression'
summary:
  en: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
  zh: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
  ko: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (Diffusion-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea Group,
    Shanghai University, and published at ICML25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_vla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.03293v3.
sources:
- id: src_001
  type: paper
  title: 'Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression (arXiv)'
  url: https://arxiv.org/abs/2412.03293
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Diffusion-VLA source
  url: https://doi.org/10.48550/arXiv.2412.03293
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## 核心内容
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## 参考
- http://arxiv.org/abs/2412.03293v3

## Overview
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## Content
In this paper, we present DiffusionVLA, a novel framework that seamlessly combines the autoregression model with the diffusion model for learning visuomotor policy. Central to our approach is a next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations. Subsequently, a diffusion model is attached to generate robust action outputs. To enhance policy learning through self-reasoning, we introduce a novel reasoning injection module that integrates reasoning phrases directly into the policy learning process. The whole framework is simple and flexible, making it easy to deploy and upgrade. We conduct extensive experiments using multiple real robots to validate the effectiveness of DiffusionVLA. Our tests include a challenging factory sorting task, where DiffusionVLA successfully categorizes objects, including those not seen during training. We observe that the reasoning module makes the model interpretable. It allows observers to understand the model thought process and identify potential causes of policy failures. Additionally, we test DiffusionVLA on a zero-shot bin-picking task, achieving 63.7\% accuracy on 102 previously unseen objects. Our method demonstrates robustness to visual changes, such as distractors and new backgrounds, and easily adapts to new embodiments. Furthermore, DiffusionVLA can follow novel instructions and retain conversational ability. Notably, DiffusionVLA is data-efficient and fast at inference; our smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task. Finally, we scale the model from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size.

## 개요
본 논문에서는 시각-운동 정책 학습을 위해 자기회귀 모델과 확산 모델을 원활하게 결합한 새로운 프레임워크인 DiffusionVLA를 제시합니다. 우리 접근법의 핵심은 다음 토큰 예측 목표로, 모델이 현재 관찰 맥락에서 사용자 질의에 대해 효과적으로 추론할 수 있게 합니다. 이후 확산 모델을 연결하여 강건한 행동 출력을 생성합니다. 자기 추론을 통한 정책 학습을 강화하기 위해, 추론 구문을 정책 학습 과정에 직접 통합하는 새로운 추론 주입 모듈을 도입합니다. 전체 프레임워크는 간단하고 유연하여 배포 및 업그레이드가 용이합니다. 우리는 여러 실제 로봇을 사용한 광범위한 실험을 통해 DiffusionVLA의 효과성을 검증합니다. 테스트에는 훈련 중 보지 못한 객체를 포함한 물체를 성공적으로 분류하는 까다로운 공장 분류 작업이 포함됩니다. 추론 모듈이 모델을 해석 가능하게 만드는 것을 관찰했습니다. 이를 통해 관찰자는 모델의 사고 과정을 이해하고 정책 실패의 잠재적 원인을 식별할 수 있습니다. 또한, 제로샷 빈 피킹 작업에서 DiffusionVLA를 테스트하여 이전에 본 적 없는 102개 객체에 대해 63.7%의 정확도를 달성했습니다. 우리 방법은 방해 요소 및 새로운 배경과 같은 시각적 변화에 강건함을 보여주며, 새로운 구현체에 쉽게 적응합니다. 더 나아가, DiffusionVLA는 새로운 지시를 따르고 대화 능력을 유지할 수 있습니다. 특히, DiffusionVLA는 데이터 효율적이고 추론 속도가 빠릅니다. 가장 작은 DiffusionVLA-2B는 단일 A6000 GPU에서 82Hz로 작동하며, 복잡한 작업에 대해 50개 미만의 시연으로 처음부터 훈련할 수 있습니다. 마지막으로, 모델을 2B에서 72B 파라미터로 확장하여 모델 크기 증가에 따른 일반화 능력 향상을 입증합니다.

## 핵심 내용
본 논문에서는 시각-운동 정책 학습을 위해 자기회귀 모델과 확산 모델을 원활하게 결합한 새로운 프레임워크인 DiffusionVLA를 제시합니다. 우리 접근법의 핵심은 다음 토큰 예측 목표로, 모델이 현재 관찰 맥락에서 사용자 질의에 대해 효과적으로 추론할 수 있게 합니다. 이후 확산 모델을 연결하여 강건한 행동 출력을 생성합니다. 자기 추론을 통한 정책 학습을 강화하기 위해, 추론 구문을 정책 학습 과정에 직접 통합하는 새로운 추론 주입 모듈을 도입합니다. 전체 프레임워크는 간단하고 유연하여 배포 및 업그레이드가 용이합니다. 우리는 여러 실제 로봇을 사용한 광범위한 실험을 통해 DiffusionVLA의 효과성을 검증합니다. 테스트에는 훈련 중 보지 못한 객체를 포함한 물체를 성공적으로 분류하는 까다로운 공장 분류 작업이 포함됩니다. 추론 모듈이 모델을 해석 가능하게 만드는 것을 관찰했습니다. 이를 통해 관찰자는 모델의 사고 과정을 이해하고 정책 실패의 잠재적 원인을 식별할 수 있습니다. 또한, 제로샷 빈 피킹 작업에서 DiffusionVLA를 테스트하여 이전에 본 적 없는 102개 객체에 대해 63.7%의 정확도를 달성했습니다. 우리 방법은 방해 요소 및 새로운 배경과 같은 시각적 변화에 강건함을 보여주며, 새로운 구현체에 쉽게 적응합니다. 더 나아가, DiffusionVLA는 새로운 지시를 따르고 대화 능력을 유지할 수 있습니다. 특히, DiffusionVLA는 데이터 효율적이고 추론 속도가 빠릅니다. 가장 작은 DiffusionVLA-2B는 단일 A6000 GPU에서 82Hz로 작동하며, 복잡한 작업에 대해 50개 미만의 시연으로 처음부터 훈련할 수 있습니다. 마지막으로, 모델을 2B에서 72B 파라미터로 확장하여 모델 크기 증가에 따른 일반화 능력 향상을 입증합니다.
