---
$id: ent_paper_chen_internvla_m1_a_spatially_guide_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy'
  zh: InternVLA-M1
  ko: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy'
summary:
  en: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (InternVLA-M1), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Intern Robotics, Shanghai AI Laboratory.'
  zh: InternVLA-M1 是由上海人工智能实验室 Intern Robotics 团队于 2025 年提出的大型视觉-语言-动作模型，用于机器人操控。其核心贡献在于提出空间引导的视觉-语言-动作训练范式，通过两阶段流程（空间定位预训练与动作后训练）显著提升了指令跟随机器人的泛化能力。在多个基准测试中，该模型相比无空间引导的变体取得了最高
    17% 的性能提升，并在长时程推理场景中超越现有方法超过 10%。
  ko: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (InternVLA-M1), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Intern Robotics, Shanghai AI Laboratory.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- internvla_m1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13778v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'InternVLA-M1: A Spatially Guided Vision-Language-Action Framework for Generalist Robot Policy (arXiv)'
  url: https://arxiv.org/abs/2510.13778
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: InternVLA-M1 source
  url: https://doi.org/10.48550/arXiv.2510.13778
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
InternVLA-M1 是一个统一的机器人操控框架，旨在通过空间引导训练将指令跟随机器人推向可扩展的通用智能。该框架采用两阶段流水线：首先在超过 230 万条空间推理数据上进行预训练，学习将指令与视觉位置对齐以确定“在哪里行动”；随后通过即插即用的空间提示进行动作后训练，生成具身感知的动作以决定“如何行动”。实验表明，这种空间引导训练策略在 SimplerEnv Google Robot、WidowX 和 LIBERO Franka 等基准上分别带来 14.6%、17% 和 4.3% 的稳定提升。此外，团队构建了仿真引擎收集 24.4 万条可泛化的拾放任务数据，在 200 个任务和 3000+ 物体上实现平均 6.2% 的提升，并在真实世界的杂乱拾放任务中提升 7.3%，通过合成协同训练在未见物体和新配置上达到 20.6% 的提升。

## 核心内容
### 方法架构
InternVLA-M1 的核心是**空间引导的视觉-语言-动作训练**，将空间定位作为连接指令与机器人动作的关键桥梁。其两阶段流程包括：
- **空间定位预训练**：在超过 230 万条空间推理数据上训练，学习将指令与视觉、非具身感知的位置对齐，确定“在哪里行动”。该阶段支持框、点和轨迹三种预测形式。
- **空间引导动作后训练**：通过即插即用的空间提示生成具身感知的动作，决定“如何行动”。这种设计使得空间定位能力与动作生成解耦，便于模块化扩展。

### 实验设置与关键结果
- **消融实验**：在 SimplerEnv Google Robot 上，带空间引导的变体比无引导变体提升 14.6%；在 WidowX 上提升 17%；在 LIBERO Franka 上提升 4.3%。
- **空间推理能力**：在框、点和轨迹预测任务中均展现出更强的空间推理能力。
- **仿真数据扩展**：构建仿真引擎收集 24.4 万条可泛化的拾放任务数据，在 200 个任务和 3000+ 物体上实现平均 6.2% 的提升。
- **真实世界实验**：在杂乱拾放任务中提升 7.3%；通过合成协同训练，在未见物体和新配置上达到 20.6% 的提升。
- **长时程推理**：在需要复杂推理的长时间任务中，超越现有方法超过 10%。

### 结论
InternVLA-M1 验证了空间引导训练作为可扩展、鲁棒的通用机器人策略的统一原则。代码和模型已开源在 https://github.com/InternRobotics/InternVLA-M1。

## Overview
We introduce InternVLA-M1, a unified framework for spatial grounding and robot control that advances instruction-following robots toward scalable, general-purpose intelligence. Its core idea is spatially guided vision-language-action training, where spatial grounding serves as the critical link between instructions and robot actions. InternVLA-M1 employs a two-stage pipeline: (i) spatial grounding pre-training on over 2.3M spatial reasoning data to determine ``where to act'' by aligning instructions with visual, embodiment-agnostic positions, and (ii) spatially guided action post-training to decide ``how to act'' by generating embodiment-aware actions through plug-and-play spatial prompting. This spatially guided training recipe yields consistent gains: InternVLA-M1 outperforms its variant without spatial guidance by +14.6% on SimplerEnv Google Robot, +17% on WidowX, and +4.3% on LIBERO Franka, while demonstrating stronger spatial reasoning capability in box, point, and trace prediction. To further scale instruction following, we built a simulation engine to collect 244K generalizable pick-and-place episodes, enabling a 6.2% average improvement across 200 tasks and 3K+ objects. In real-world clustered pick-and-place, InternVLA-M1 improved by 7.3%, and with synthetic co-training, achieved +20.6% on unseen objects and novel configurations. Moreover, in long-horizon reasoning-intensive scenarios, it surpassed existing works by over 10%. These results highlight spatially guided training as a unifying principle for scalable and resilient generalist robots. Code and models are available at https://github.com/InternRobotics/InternVLA-M1.

## 개요
우리는 InternVLA-M1을 소개합니다. 이는 공간적 근거(grounding)와 로봇 제어를 위한 통합 프레임워크로, 명령 수행 로봇을 확장 가능한 범용 지능으로 발전시킵니다. 핵심 아이디어는 공간적으로 유도된 시각-언어-행동 훈련으로, 공간적 근거가 명령과 로봇 행동 사이의 중요한 연결고리 역할을 합니다. InternVLA-M1은 두 단계 파이프라인을 사용합니다: (i) 230만 개 이상의 공간 추론 데이터에 대한 공간적 근거 사전 훈련을 통해 명령을 시각적, 구현체에 구애받지 않는 위치와 정렬하여 "어디에서 행동할지" 결정하고, (ii) 플러그 앤 플레이 공간 프롬프팅을 통해 구현체 인식 행동을 생성하여 "어떻게 행동할지" 결정하는 공간적으로 유도된 행동 후속 훈련입니다. 이 공간적으로 유도된 훈련 방식은 일관된 성능 향상을 가져옵니다: InternVLA-M1은 공간적 유도가 없는 변형 모델보다 SimplerEnv Google Robot에서 +14.6%, WidowX에서 +17%, LIBERO Franka에서 +4.3% 더 뛰어난 성능을 보이며, 상자, 점, 궤적 예측에서 더 강력한 공간 추론 능력을 입증합니다. 명령 수행을 더욱 확장하기 위해, 우리는 244K개의 일반화 가능한 집어 옮기기(pick-and-place) 에피소드를 수집하는 시뮬레이션 엔진을 구축하여 200개 작업과 3000개 이상의 객체에서 평균 6.2%의 개선을 가능하게 했습니다. 실제 환경의 군집 집어 옮기기에서 InternVLA-M1은 7.3% 향상되었으며, 합성 공동 훈련을 통해 보지 못한 객체와 새로운 구성에서 +20.6%를 달성했습니다. 또한, 장기적이고 추론 집약적인 시나리오에서는 기존 연구보다 10% 이상 뛰어난 성능을 보였습니다. 이러한 결과는 공간적으로 유도된 훈련이 확장 가능하고 탄력적인 범용 로봇을 위한 통합 원리임을 강조합니다. 코드와 모델은 https://github.com/InternRobotics/InternVLA-M1에서 확인할 수 있습니다.

## 핵심 내용
우리는 InternVLA-M1을 소개합니다. 이는 공간적 근거(grounding)와 로봇 제어를 위한 통합 프레임워크로, 명령 수행 로봇을 확장 가능한 범용 지능으로 발전시킵니다. 핵심 아이디어는 공간적으로 유도된 시각-언어-행동 훈련으로, 공간적 근거가 명령과 로봇 행동 사이의 중요한 연결고리 역할을 합니다. InternVLA-M1은 두 단계 파이프라인을 사용합니다: (i) 230만 개 이상의 공간 추론 데이터에 대한 공간적 근거 사전 훈련을 통해 명령을 시각적, 구현체에 구애받지 않는 위치와 정렬하여 "어디에서 행동할지" 결정하고, (ii) 플러그 앤 플레이 공간 프롬프팅을 통해 구현체 인식 행동을 생성하여 "어떻게 행동할지" 결정하는 공간적으로 유도된 행동 후속 훈련입니다. 이 공간적으로 유도된 훈련 방식은 일관된 성능 향상을 가져옵니다: InternVLA-M1은 공간적 유도가 없는 변형 모델보다 SimplerEnv Google Robot에서 +14.6%, WidowX에서 +17%, LIBERO Franka에서 +4.3% 더 뛰어난 성능을 보이며, 상자, 점, 궤적 예측에서 더 강력한 공간 추론 능력을 입증합니다. 명령 수행을 더욱 확장하기 위해, 우리는 244K개의 일반화 가능한 집어 옮기기(pick-and-place) 에피소드를 수집하는 시뮬레이션 엔진을 구축하여 200개 작업과 3000개 이상의 객체에서 평균 6.2%의 개선을 가능하게 했습니다. 실제 환경의 군집 집어 옮기기에서 InternVLA-M1은 7.3% 향상되었으며, 합성 공동 훈련을 통해 보지 못한 객체와 새로운 구성에서 +20.6%를 달성했습니다. 또한, 장기적이고 추론 집약적인 시나리오에서는 기존 연구보다 10% 이상 뛰어난 성능을 보였습니다. 이러한 결과는 공간적으로 유도된 훈련이 확장 가능하고 탄력적인 범용 로봇을 위한 통합 원리임을 강조합니다. 코드와 모델은 https://github.com/InternRobotics/InternVLA-M1에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.13778v1
