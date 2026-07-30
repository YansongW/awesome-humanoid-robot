---
$id: ent_paper_prism_personalized_robotic_dat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis'
  zh: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis'
  ko: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis'
summary:
  en: 'arXiv:2607.04880v1 Announce Type: new Abstract: Recent advances in large-scale pretrained vision-language-action models
    have improved robot policy learning, but directly deploying such policies in user-specific environments remains challenging
    due to limited generalization, which inevitably requires collecting a dataset tailored to the target environment. Teleoperation
    yields well-aligned data but is costly and difficult to scale, whereas simulation scales easily but struggles to resemble
    the target environment and generate task-specific trajectories. To meet both simultaneously, we propose PRISM, an end-to-end
    pipeline that generates personalized robotic datasets from a single image and a natural-language instruction. PRISM constructs
    digital cousin scenes that are semantically and geometrically aligned with the user environment yet diverse at the instance
    level, and synthesizes executable demonstrations without human teleoperation. Extensive experiments show that policies
    trained on PRISM-generated datasets outperform those trained on baseline-generated datasets on LIBERO and LIBERO-Plus,
    achieve up to 100\% success rate on three real-world manipulation tasks, and maintain stronger performance when evaluated
    in environments that differ from those seen during training.'
  zh: PRISM 是一个端到端流水线，能从单张图像和自然语言指令生成个性化机器人数据集。它由研究团队提出，核心贡献在于构建与用户环境语义和几何对齐但实例多样的“数字表亲”场景，并自动合成可执行的演示数据，无需人类遥操作。实验表明，基于 PRISM
    数据训练的策略在 LIBERO 和 LIBERO-Plus 基准上优于基线方法，并在三项真实世界操作任务中达到 100% 的成功率。
  ko: 'arXiv:2607.04880v1 Announce Type: new Abstract: Recent advances in large-scale pretrained vision-language-action models
    have improved robot policy learning, but directly deploying such policies in user-specific environments remains challenging
    due to limited generalization, which inevitably requires collecting a dataset tailored to the target environment. Teleoperation
    yields well-aligned data but is costly and difficult to scale, whereas simulation scales easily but struggles to resemble
    the target environment and generate task-specific trajectories. To meet both simultaneously, we propose PRISM, an end-to-end
    pipeline that generates personalized robotic datasets from a single image and a natural-language instruction. PRISM constructs
    digital cousin scenes that are semantically and geometrically aligned with the user environment yet diverse at the instance
    level, and synthesizes executable demonstrations without human teleoperation. Extensive experiments show that policies
    trained on PRISM-generated datasets outperform those trained on baseline-generated datasets on LIBERO and LIBERO-Plus,
    achieve up to 100\% success rate on three real-world manipulation tasks, and maintain stronger performance when evaluated
    in environments that differ from those seen during training.'
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
- robotics
- prism
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04880v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis (arXiv)'
  url: https://arxiv.org/abs/2607.04880
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
PRISM 解决了机器人策略学习中的个性化数据集生成难题。它通过从单张用户环境图像和自然语言指令出发，自动构建与目标环境语义和几何对齐的“数字表亲”场景，并在这些场景中合成无需人类遥操作的可执行演示。该方法在 LIBERO 和 LIBERO-Plus 基准上显著提升了策略性能，并在三项真实世界操作任务中实现了高达 100% 的成功率，同时在训练时未见过的环境中也保持了更强的泛化能力。

## 核心内容
### 方法概述
PRISM 是一个端到端流水线，其核心在于从单张图像和自然语言指令生成个性化机器人数据集。它通过构建“数字表亲”场景——这些场景在语义和几何上与用户环境对齐，但在实例层面保持多样性——来弥合仿真与真实环境之间的差距。整个流程无需人类遥操作，即可自动合成可执行的演示数据。

### 架构与流程
- **场景构建**：PRISM 首先根据用户提供的单张图像和自然语言指令，生成与目标环境语义和几何对齐的“数字表亲”场景。这些场景在实例层面（如物体外观、布局）具有多样性，以增强数据集的泛化能力。
- **演示合成**：在构建的场景中，PRISM 自动生成可执行的机器人操作演示，无需人类遥操作。这通过结合场景理解与运动规划实现，确保演示在物理上可行且与任务指令一致。

### 实验设置与关键结果
- **基准测试**：在 LIBERO 和 LIBERO-Plus 基准上，基于 PRISM 生成数据集训练的策略，其性能显著优于基于基线方法生成数据训练的策略。
- **真实世界任务**：在三项真实世界操作任务中，PRISM 训练的策略达到了 100% 的成功率，展示了其在个性化环境中的有效性。
- **泛化能力**：当在训练时未见过的环境中进行评估时，PRISM 训练的策略仍能保持更强的性能，表明其生成的场景多样性有助于提升泛化能力。

### 结论
PRISM 通过端到端流水线，从单张图像和自然语言指令生成个性化机器人数据集，有效解决了遥操作成本高和仿真场景不匹配的问题。实验证明，该方法在多个基准和真实任务中均取得了领先性能，并展现出良好的泛化能力。

## Overview
Recent advances in large-scale pretrained vision-language-action models have improved robot policy learning, but directly deploying such policies in user-specific environments remains challenging due to limited generalization, which inevitably requires collecting a dataset tailored to the target environment. Teleoperation yields well-aligned data but is costly and difficult to scale, whereas simulation scales easily but struggles to resemble the target environment and generate task-specific trajectories. To meet both simultaneously, we propose PRISM, an end-to-end pipeline that generates personalized robotic datasets from a single image and a natural-language instruction. PRISM constructs digital cousin scenes that are semantically and geometrically aligned with the user environment yet diverse at the instance level, and synthesizes executable demonstrations without human teleoperation. Extensive experiments show that policies trained on PRISM-generated datasets outperform those trained on baseline-generated datasets on LIBERO and LIBERO-Plus, achieve up to 100\% success rate on three real-world manipulation tasks, and maintain stronger performance when evaluated in environments that differ from those seen during training.

## 개요
최근 대규모 사전 훈련된 시각-언어-행동 모델의 발전은 로봇 정책 학습을 개선했지만, 이러한 정책을 사용자별 환경에 직접 배포하는 것은 일반화의 한계로 인해 여전히 어려움이 있으며, 이는 필연적으로 대상 환경에 맞춤화된 데이터셋 수집을 필요로 합니다. 원격 조작은 정렬이 잘 된 데이터를 제공하지만 비용이 많이 들고 확장이 어려운 반면, 시뮬레이션은 확장이 용이하지만 대상 환경을 모사하고 작업별 궤적을 생성하는 데 어려움을 겪습니다. 이 두 가지를 동시에 충족하기 위해, 우리는 단일 이미지와 자연어 명령으로부터 개인화된 로봇 데이터셋을 생성하는 종단간 파이프라인인 PRISM을 제안합니다. PRISM은 사용자 환경과 의미론적 및 기하학적으로 정렬되면서도 인스턴스 수준에서 다양한 디지털 사촌 장면을 구성하고, 인간의 원격 조작 없이 실행 가능한 시연을 합성합니다. 광범위한 실험 결과, PRISM으로 생성된 데이터셋으로 훈련된 정책이 LIBERO 및 LIBERO-Plus에서 기준선 생성 데이터셋으로 훈련된 정책보다 우수한 성능을 보였으며, 세 가지 실제 조작 작업에서 최대 100% 성공률을 달성하고, 훈련 중에 보지 못한 환경에서 평가했을 때도 더 강력한 성능을 유지했습니다.

## 핵심 내용
최근 대규모 사전 훈련된 시각-언어-행동 모델의 발전은 로봇 정책 학습을 개선했지만, 이러한 정책을 사용자별 환경에 직접 배포하는 것은 일반화의 한계로 인해 여전히 어려움이 있으며, 이는 필연적으로 대상 환경에 맞춤화된 데이터셋 수집을 필요로 합니다. 원격 조작은 정렬이 잘 된 데이터를 제공하지만 비용이 많이 들고 확장이 어려운 반면, 시뮬레이션은 확장이 용이하지만 대상 환경을 모사하고 작업별 궤적을 생성하는 데 어려움을 겪습니다. 이 두 가지를 동시에 충족하기 위해, 우리는 단일 이미지와 자연어 명령으로부터 개인화된 로봇 데이터셋을 생성하는 종단간 파이프라인인 PRISM을 제안합니다. PRISM은 사용자 환경과 의미론적 및 기하학적으로 정렬되면서도 인스턴스 수준에서 다양한 디지털 사촌 장면을 구성하고, 인간의 원격 조작 없이 실행 가능한 시연을 합성합니다. 광범위한 실험 결과, PRISM으로 생성된 데이터셋으로 훈련된 정책이 LIBERO 및 LIBERO-Plus에서 기준선 생성 데이터셋으로 훈련된 정책보다 우수한 성능을 보였으며, 세 가지 실제 조작 작업에서 최대 100% 성공률을 달성하고, 훈련 중에 보지 못한 환경에서 평가했을 때도 더 강력한 성능을 유지했습니다.

## 参考
- http://arxiv.org/abs/2607.04880v1
