---
$id: ent_paper_li_cogact_a_foundational_vision_l_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation'
  zh: CogACT
  ko: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation'
summary:
  en: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation (CogACT),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Microsoft Research
    Asia, USTC, Institute of Microelectronics, CAS.'
  zh: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation (CogACT),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Microsoft Research
    Asia, USTC, Institute of Microelectronics, CAS.'
  ko: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation (CogACT),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Microsoft Research
    Asia, USTC, Institute of Microelectronics, CAS.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cogact
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.19650v1.
sources:
- id: src_001
  type: paper
  title: 'CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation
    (arXiv)'
  url: https://arxiv.org/abs/2411.19650
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CogACT source
  url: https://doi.org/10.48550/arXiv.2411.19650
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low tasks success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a omponentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrates the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real work shows that our model not only significantly surpasses existing VLAs in task performance and but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA which has similar model size (7B) with ours by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## 核心内容
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low tasks success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a omponentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrates the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real work shows that our model not only significantly surpasses existing VLAs in task performance and but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA which has similar model size (7B) with ours by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## 参考
- http://arxiv.org/abs/2411.19650v1

## Overview
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low task success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a componentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrate the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real-world settings shows that our model not only significantly surpasses existing VLAs in task performance but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA, which has a similar model size (7B) to ours, by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## Content
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of language-guided task execution and generalization to unseen scenarios. While existing VLAs adapted from pretrained large Vision-Language-Models (VLM) have demonstrated promising generalizability, their task performance is still unsatisfactory as indicated by the low task success rates in different environments. In this paper, we present a new advanced VLA architecture derived from VLM. Unlike previous works that directly repurpose VLM for action prediction by simple action quantization, we propose a componentized VLA architecture that has a specialized action module conditioned on VLM output. We systematically study the design of the action module and demonstrate the strong performance enhancement with diffusion action transformers for action sequence modeling, as well as their favorable scaling behaviors. We also conduct comprehensive experiments and ablation studies to evaluate the efficacy of our models with varied designs. The evaluation on 5 robot embodiments in simulation and real-world settings shows that our model not only significantly surpasses existing VLAs in task performance but also exhibits remarkable adaptation to new robots and generalization to unseen objects and backgrounds. It exceeds the average success rates of OpenVLA, which has a similar model size (7B) to ours, by over 35% in simulated evaluation and 55% in real robot experiments. It also outperforms the large RT-2-X model (55B) by 18% absolute success rates in simulation. Code and models can be found on our project page (https://cogact.github.io/).

## 개요
대규모 Vision-Language-Action(VLA) 모델의 발전은 언어 기반 작업 실행 및 보지 못한 시나리오에 대한 일반화 측면에서 로봇 조작 성능을 크게 향상시켰습니다. 사전 훈련된 대규모 Vision-Language-Model(VLM)에서 파생된 기존 VLA 모델들은 유망한 일반화 능력을 보여주었지만, 다양한 환경에서 낮은 작업 성공률로 나타나듯이 작업 성능은 여전히 만족스럽지 않습니다. 본 논문에서는 VLM에서 파생된 새로운 고급 VLA 아키텍처를 제시합니다. 단순한 행동 양자화를 통해 VLM을 행동 예측에 직접 재사용한 이전 연구들과 달리, 우리는 VLM 출력에 조건화된 특화된 행동 모듈을 갖춘 구성 요소화된 VLA 아키텍처를 제안합니다. 우리는 행동 모듈의 설계를 체계적으로 연구하고, 확산 행동 트랜스포머를 통한 행동 시퀀스 모델링의 강력한 성능 향상과 유리한 스케일링 특성을 입증합니다. 또한 다양한 설계를 가진 모델의 효능을 평가하기 위해 포괄적인 실험 및 절제 연구를 수행합니다. 시뮬레이션 및 실제 작업에서 5가지 로봇 구현체에 대한 평가는 우리 모델이 기존 VLA 모델의 작업 성능을 크게 능가할 뿐만 아니라 새로운 로봇에 대한 놀라운 적응력과 보지 못한 객체 및 배경에 대한 일반화 능력을 보여줍니다. 우리 모델은 유사한 모델 크기(7B)를 가진 OpenVLA의 평균 성공률을 시뮬레이션 평가에서 35% 이상, 실제 로봇 실험에서 55% 이상 초과합니다. 또한 대형 RT-2-X 모델(55B)을 시뮬레이션에서 절대 성공률 18%로 능가합니다. 코드와 모델은 프로젝트 페이지(https://cogact.github.io/)에서 확인할 수 있습니다.

## 핵심 내용
대규모 Vision-Language-Action(VLA) 모델의 발전은 언어 기반 작업 실행 및 보지 못한 시나리오에 대한 일반화 측면에서 로봇 조작 성능을 크게 향상시켰습니다. 사전 훈련된 대규모 Vision-Language-Model(VLM)에서 파생된 기존 VLA 모델들은 유망한 일반화 능력을 보여주었지만, 다양한 환경에서 낮은 작업 성공률로 나타나듯이 작업 성능은 여전히 만족스럽지 않습니다. 본 논문에서는 VLM에서 파생된 새로운 고급 VLA 아키텍처를 제시합니다. 단순한 행동 양자화를 통해 VLM을 행동 예측에 직접 재사용한 이전 연구들과 달리, 우리는 VLM 출력에 조건화된 특화된 행동 모듈을 갖춘 구성 요소화된 VLA 아키텍처를 제안합니다. 우리는 행동 모듈의 설계를 체계적으로 연구하고, 확산 행동 트랜스포머를 통한 행동 시퀀스 모델링의 강력한 성능 향상과 유리한 스케일링 특성을 입증합니다. 또한 다양한 설계를 가진 모델의 효능을 평가하기 위해 포괄적인 실험 및 절제 연구를 수행합니다. 시뮬레이션 및 실제 작업에서 5가지 로봇 구현체에 대한 평가는 우리 모델이 기존 VLA 모델의 작업 성능을 크게 능가할 뿐만 아니라 새로운 로봇에 대한 놀라운 적응력과 보지 못한 객체 및 배경에 대한 일반화 능력을 보여줍니다. 우리 모델은 유사한 모델 크기(7B)를 가진 OpenVLA의 평균 성공률을 시뮬레이션 평가에서 35% 이상, 실제 로봇 실험에서 55% 이상 초과합니다. 또한 대형 RT-2-X 모델(55B)을 시뮬레이션에서 절대 성공률 18%로 능가합니다. 코드와 모델은 프로젝트 페이지(https://cogact.github.io/)에서 확인할 수 있습니다.
