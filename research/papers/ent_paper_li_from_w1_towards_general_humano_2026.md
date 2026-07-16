---
$id: ent_paper_li_from_w1_towards_general_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
  zh: FRoM-W1：面向自然语言指令的通用人形机器人全身控制
  ko: 'FRoM-W1: 자연어 명령을 통한 범용 휴머노이드 전신 제어를 향하여'
summary:
  en: FRoM-W1 is an open-source two-stage framework that generates whole-body human motions from natural-language instructions
    using a 9B LLaMA-based model (H-GPT) and then retargets and executes them on real humanoid robots (Unitree H1 and G1)
    via a reinforcement-learning motion controller (H-ACT) with a modular sim2real deployment module (RoboJudo).
  zh: FRoM-W1 是一个开源两阶段框架，首先利用基于 9B LLaMA 的 H-GPT 模型从自然语言指令生成全身人体动作，然后通过强化学习运动控制器 H-ACT 将动作重定向并在宇树 H1 与 G1 等人形机器人上执行，并借助模块化
    sim2real 部署模块 RoboJudo 迁移到真实机器人。
  ko: FRoM-W1은 9B LLaMA 기반 H-GPT 모델로 자연어 명령에서 전신 인체 동작을 생성하고, 강화학습 기반 동작 컨트롤러 H-ACT를 통해 이를 Unitree H1 및 G1 등의 실제 휴머노이드 로봇으로
    리타기팅 및 실행하며, 모듈형 sim2real 배포 모듈인 RoboJudo로 실제 로봇에 적용하는 오픈소스 2단계 프레임워크이다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- natural_language_control
- whole_body_control
- humanoid_robot
- motion_generation
- sim2real
- reinforcement_learning
- human_to_humanoid_retargeting
- llama
- chain_of_thought
- unitree_h1
- unitree_g1
- open_source
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.12799v1.
sources:
- id: src_001
  type: paper
  title: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
  url: https://arxiv.org/abs/2601.12799
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Humanoid robots are capable of performing various actions such as greeting, dancing and even backflipping. However, these motions are often hard-coded or specifically trained, which limits their versatility. In this work, we present FRoM-W1, an open-source framework designed to achieve general humanoid whole-body motion control using natural language. To universally understand natural language and generate corresponding motions, as well as enable various humanoid robots to stably execute these motions in the physical world under gravity, FRoM-W1 operates in two stages: (a) H-GPT: utilizing massive human data, a large-scale language-driven human whole-body motion generation model is trained to generate diverse natural behaviors. We further leverage the Chain-of-Thought technique to improve the model's generalization in instruction understanding. (b) H-ACT: After retargeting generated human whole-body motions into robot-specific actions, a motion controller that is pretrained and further fine-tuned through reinforcement learning in physical simulation enables humanoid robots to accurately and stably perform corresponding actions. It is then deployed on real robots via a modular simulation-to-reality module. We extensively evaluate FRoM-W1 on Unitree H1 and G1 robots. Results demonstrate superior performance on the HumanML3D-X benchmark for human whole-body motion generation, and our introduced reinforcement learning fine-tuning consistently improves both motion tracking accuracy and task success rates of these humanoid robots. We open-source the entire FRoM-W1 framework and hope it will advance the development of humanoid intelligence.

## 核心内容
Humanoid robots are capable of performing various actions such as greeting, dancing and even backflipping. However, these motions are often hard-coded or specifically trained, which limits their versatility. In this work, we present FRoM-W1, an open-source framework designed to achieve general humanoid whole-body motion control using natural language. To universally understand natural language and generate corresponding motions, as well as enable various humanoid robots to stably execute these motions in the physical world under gravity, FRoM-W1 operates in two stages: (a) H-GPT: utilizing massive human data, a large-scale language-driven human whole-body motion generation model is trained to generate diverse natural behaviors. We further leverage the Chain-of-Thought technique to improve the model's generalization in instruction understanding. (b) H-ACT: After retargeting generated human whole-body motions into robot-specific actions, a motion controller that is pretrained and further fine-tuned through reinforcement learning in physical simulation enables humanoid robots to accurately and stably perform corresponding actions. It is then deployed on real robots via a modular simulation-to-reality module. We extensively evaluate FRoM-W1 on Unitree H1 and G1 robots. Results demonstrate superior performance on the HumanML3D-X benchmark for human whole-body motion generation, and our introduced reinforcement learning fine-tuning consistently improves both motion tracking accuracy and task success rates of these humanoid robots. We open-source the entire FRoM-W1 framework and hope it will advance the development of humanoid intelligence.

## 参考
- http://arxiv.org/abs/2601.12799v1

## Overview
Humanoid robots are capable of performing various actions such as greeting, dancing and even backflipping. However, these motions are often hard-coded or specifically trained, which limits their versatility. In this work, we present FRoM-W1, an open-source framework designed to achieve general humanoid whole-body motion control using natural language. To universally understand natural language and generate corresponding motions, as well as enable various humanoid robots to stably execute these motions in the physical world under gravity, FRoM-W1 operates in two stages: (a) H-GPT: utilizing massive human data, a large-scale language-driven human whole-body motion generation model is trained to generate diverse natural behaviors. We further leverage the Chain-of-Thought technique to improve the model's generalization in instruction understanding. (b) H-ACT: After retargeting generated human whole-body motions into robot-specific actions, a motion controller that is pretrained and further fine-tuned through reinforcement learning in physical simulation enables humanoid robots to accurately and stably perform corresponding actions. It is then deployed on real robots via a modular simulation-to-reality module. We extensively evaluate FRoM-W1 on Unitree H1 and G1 robots. Results demonstrate superior performance on the HumanML3D-X benchmark for human whole-body motion generation, and our introduced reinforcement learning fine-tuning consistently improves both motion tracking accuracy and task success rates of these humanoid robots. We open-source the entire FRoM-W1 framework and hope it will advance the development of humanoid intelligence.

## Content
Humanoid robots are capable of performing various actions such as greeting, dancing and even backflipping. However, these motions are often hard-coded or specifically trained, which limits their versatility. In this work, we present FRoM-W1, an open-source framework designed to achieve general humanoid whole-body motion control using natural language. To universally understand natural language and generate corresponding motions, as well as enable various humanoid robots to stably execute these motions in the physical world under gravity, FRoM-W1 operates in two stages: (a) H-GPT: utilizing massive human data, a large-scale language-driven human whole-body motion generation model is trained to generate diverse natural behaviors. We further leverage the Chain-of-Thought technique to improve the model's generalization in instruction understanding. (b) H-ACT: After retargeting generated human whole-body motions into robot-specific actions, a motion controller that is pretrained and further fine-tuned through reinforcement learning in physical simulation enables humanoid robots to accurately and stably perform corresponding actions. It is then deployed on real robots via a modular simulation-to-reality module. We extensively evaluate FRoM-W1 on Unitree H1 and G1 robots. Results demonstrate superior performance on the HumanML3D-X benchmark for human whole-body motion generation, and our introduced reinforcement learning fine-tuning consistently improves both motion tracking accuracy and task success rates of these humanoid robots. We open-source the entire FRoM-W1 framework and hope it will advance the development of humanoid intelligence.

## 개요
휴머노이드 로봇은 인사, 춤, 심지어 백플립과 같은 다양한 동작을 수행할 수 있습니다. 그러나 이러한 동작은 종종 하드코딩되거나 특별히 훈련되어 있어 다용도성이 제한됩니다. 본 연구에서는 자연어를 사용하여 일반적인 휴머노이드 전신 동작 제어를 달성하도록 설계된 오픈소스 프레임워크인 FRoM-W1을 제시합니다. 자연어를 보편적으로 이해하고 이에 상응하는 동작을 생성하며, 다양한 휴머노이드 로봇이 중력 하의 물리적 세계에서 이러한 동작을 안정적으로 실행할 수 있도록 하기 위해 FRoM-W1은 두 단계로 작동합니다: (a) H-GPT: 방대한 인간 데이터를 활용하여 대규모 언어 기반 인간 전신 동작 생성 모델을 훈련시켜 다양한 자연스러운 행동을 생성합니다. 또한 Chain-of-Thought 기법을 활용하여 명령 이해에서 모델의 일반화 능력을 향상시킵니다. (b) H-ACT: 생성된 인간 전신 동작을 로봇 특화 동작으로 리타겟팅한 후, 물리적 시뮬레이션에서 강화 학습을 통해 사전 훈련되고 추가 미세 조정된 동작 컨트롤러가 휴머노이드 로봇이 해당 동작을 정확하고 안정적으로 수행할 수 있도록 합니다. 그런 다음 모듈식 시뮬레이션-현실 모듈을 통해 실제 로봇에 배포됩니다. 우리는 Unitree H1 및 G1 로봇에서 FRoM-W1을 광범위하게 평가했습니다. 결과는 인간 전신 동작 생성을 위한 HumanML3D-X 벤치마크에서 우수한 성능을 보여주었으며, 도입된 강화 학습 미세 조정은 이러한 휴머노이드 로봇의 동작 추적 정확도와 작업 성공률을 일관되게 향상시킵니다. 우리는 FRoM-W1 프레임워크 전체를 오픈소스로 공개하며, 이것이 휴머노이드 지능 개발을 발전시키는 데 기여하기를 바랍니다.

## 핵심 내용
휴머노이드 로봇은 인사, 춤, 심지어 백플립과 같은 다양한 동작을 수행할 수 있습니다. 그러나 이러한 동작은 종종 하드코딩되거나 특별히 훈련되어 있어 다용도성이 제한됩니다. 본 연구에서는 자연어를 사용하여 일반적인 휴머노이드 전신 동작 제어를 달성하도록 설계된 오픈소스 프레임워크인 FRoM-W1을 제시합니다. 자연어를 보편적으로 이해하고 이에 상응하는 동작을 생성하며, 다양한 휴머노이드 로봇이 중력 하의 물리적 세계에서 이러한 동작을 안정적으로 실행할 수 있도록 하기 위해 FRoM-W1은 두 단계로 작동합니다: (a) H-GPT: 방대한 인간 데이터를 활용하여 대규모 언어 기반 인간 전신 동작 생성 모델을 훈련시켜 다양한 자연스러운 행동을 생성합니다. 또한 Chain-of-Thought 기법을 활용하여 명령 이해에서 모델의 일반화 능력을 향상시킵니다. (b) H-ACT: 생성된 인간 전신 동작을 로봇 특화 동작으로 리타겟팅한 후, 물리적 시뮬레이션에서 강화 학습을 통해 사전 훈련되고 추가 미세 조정된 동작 컨트롤러가 휴머노이드 로봇이 해당 동작을 정확하고 안정적으로 수행할 수 있도록 합니다. 그런 다음 모듈식 시뮬레이션-현실 모듈을 통해 실제 로봇에 배포됩니다. 우리는 Unitree H1 및 G1 로봇에서 FRoM-W1을 광범위하게 평가했습니다. 결과는 인간 전신 동작 생성을 위한 HumanML3D-X 벤치마크에서 우수한 성능을 보여주었으며, 도입된 강화 학습 미세 조정은 이러한 휴머노이드 로봇의 동작 추적 정확도와 작업 성공률을 일관되게 향상시킵니다. 우리는 FRoM-W1 프레임워크 전체를 오픈소스로 공개하며, 이것이 휴머노이드 지능 개발을 발전시키는 데 기여하기를 바랍니다.
