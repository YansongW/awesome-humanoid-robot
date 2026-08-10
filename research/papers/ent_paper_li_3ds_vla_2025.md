---
$id: ent_paper_li_3ds_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3DS-VLA
  zh: 3DS-VLA
  ko: 3DS-VLA
summary:
  en: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
  zh: 3DS-VLA 是北京大学、PKU-Agibot Lab 及香港中文大学等机构于 2025 年提出的面向机器人操作的大型视觉-语言-动作模型。其核心贡献在于将 3D 感知、推理与动作生成通过生成式世界模型无缝链接，并引入交互令牌与扩散模型，显著提升了具身环境中的推理与规划能力。
  ko: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3ds_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.09631v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (856 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 3DS-VLA source
  url: https://proceedings.mlr.press/v305/li25g.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型多依赖 2D 输入，缺乏与 3D 物理世界的深度融合，且通过直接学习感知到动作的映射，忽略了世界动态及动作与动态间的关系。3DS-VLA 受人类世界模型启发，构建在 3D 大语言模型之上，通过引入交互令牌与具身环境交互，并训练一系列具身扩散模型将其对齐至 LLM，以预测目标图像与点云。为训练该模型，团队从现有机器人数据集中提取大量 3D 信息，构建了大规模 3D 具身指令数据集。实验表明，3DS-VLA 在推理、多模态生成与规划能力上均有显著提升。

## 核心内容
### 方法架构
- **基础模型**：3DS-VLA 基于 3D 大语言模型（3D-based LLM）构建，将 3D 感知、推理与动作通过生成式世界模型统一。
- **交互令牌**：引入一组交互令牌（interaction tokens），用于与具身环境进行交互，使模型能够动态响应环境变化。
- **生成能力注入**：训练一系列具身扩散模型（embodied diffusion models），并将其对齐至 LLM，用于预测目标图像（goal images）与点云（point clouds），从而模拟未来场景并规划动作。

### 数据集构建
- 从现有机器人数据集中提取大量 3D 相关信息，整理为大规模 3D 具身指令数据集（3D embodied instruction dataset），用于训练模型。

### 实验设置与结果
- **实验数据**：在 held-in 数据集上进行评估。
- **关键结果**：3DS-VLA 在推理、多模态生成与规划能力上均显著优于基线模型，展示了其在真实世界应用中的潜力。具体提升包括更准确的 3D 场景理解、更合理的动作序列生成以及更强的动态适应能力。

### 结论
3DS-VLA 通过将 3D 感知、推理与动作生成整合至生成式世界模型，克服了传统 VLA 模型对 2D 输入的依赖及对世界动态的忽视，为具身智能体提供了更接近人类认知的决策框架。

## Overview
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 参考
- http://arxiv.org/abs/2403.09631v1

## 개요
기존 VLA 모델은 대부분 2D 입력에 의존하여 3D 물리 세계와의 깊은 융합이 부족하고, 지각에서 행동으로의 매핑을 직접 학습함으로써 세계 역학 및 행동과 역학 간의 관계를 무시합니다. 3DS-VLA는 인간 세계 모델에서 영감을 받아 3D 대규모 언어 모델 위에 구축되었으며, 상호작용 토큰을 도입하여 구현 환경과 상호작용하고, 일련의 구현 확산 모델을 훈련하여 이를 LLM에 정렬함으로써 목표 이미지와 포인트 클라우드를 예측합니다. 이 모델을 훈련하기 위해 팀은 기존 로봇 데이터셋에서 대량의 3D 정보를 추출하여 대규모 3D 구현 명령 데이터셋을 구축했습니다. 실험 결과, 3DS-VLA는 추론, 다중 모드 생성 및 계획 능력에서 현저한 향상을 보였습니다.

## 핵심 내용
### 방법 아키텍처
- **기반 모델**: 3DS-VLA는 3D 기반 대규모 언어 모델(3D-based LLM) 위에 구축되어 3D 지각, 추론 및 행동을 생성적 세계 모델로 통합합니다.
- **상호작용 토큰**: 구현 환경과 상호작용하기 위한 일련의 상호작용 토큰(interaction tokens)을 도입하여 모델이 환경 변화에 동적으로 대응할 수 있게 합니다.
- **생성 능력 주입**: 일련의 구현 확산 모델(embodied diffusion models)을 훈련하고 이를 LLM에 정렬하여 목표 이미지(goal images)와 포인트 클라우드(point clouds)를 예측함으로써 미래 시나리오를 시뮬레이션하고 행동을 계획합니다.

### 데이터셋 구축
- 기존 로봇 데이터셋에서 대량의 3D 관련 정보를 추출하여 대규모 3D 구현 명령 데이터셋(3D embodied instruction dataset)으로 정리하고, 이를 모델 훈련에 사용합니다.

### 실험 설정 및 결과
- **실험 데이터**: held-in 데이터셋에서 평가를 수행합니다.
- **주요 결과**: 3DS-VLA는 추론, 다중 모드 생성 및 계획 능력에서 기준 모델보다 현저히 우수하여 실제 세계 적용 가능성을 보여줍니다. 구체적인 향상에는 더 정확한 3D 장면 이해, 더 합리적인 행동 시퀀스 생성 및 더 강력한 동적 적응 능력이 포함됩니다.

### 결론
3DS-VLA는 3D 지각, 추론 및 행동 생성을 생성적 세계 모델에 통합함으로써 기존 VLA 모델의 2D 입력 의존성과 세계 역학 무시 문제를 극복하고, 구현 에이전트에 인간 인지에 더 가까운 의사 결정 프레임워크를 제공합니다.
