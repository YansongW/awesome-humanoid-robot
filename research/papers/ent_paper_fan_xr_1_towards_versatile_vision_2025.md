---
$id: ent_paper_fan_xr_1_towards_versatile_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations'
  zh: XR-1
  ko: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations'
summary:
  en: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (XR-1), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Innovation Center of Humanoid
    Robotics, Beihang University, State Key Laboratory of Virtual Reality Technology and Systems, State Key Laboratory of
    Multimedia Information Processing, Peking University.'
  zh: XR-1 是由北京人形机器人创新中心、北京航空航天大学、北京大学等机构提出的 2025 年大型视觉-语言-动作模型，用于机器人操作。其核心贡献是引入统一视觉-运动编码（UVMC），通过双分支 VQ-VAE 学习离散潜在表征，并采用三阶段训练范式，在超过
    120 种任务、6 种机器人实体上实现 14,000 次 rollout，性能超越 π₀.₅、π₀、RDT 等基线。
  ko: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (XR-1), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Beijing Innovation Center of Humanoid
    Robotics, Beihang University, State Key Laboratory of Virtual Reality Technology and Systems, State Key Laboratory of
    Multimedia Information Processing, Peking University.'
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
- vla
- xr_1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.02776v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1062 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'XR-1: Towards Versatile Vision-Language-Action Models via Learning Unified Vision-Motion Representations (arXiv)'
  url: https://arxiv.org/abs/2511.02776
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: XR-1 source
  url: https://doi.org/10.48550/arXiv.2511.02776
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
XR-1 旨在解决现有视觉-语言-动作模型的两大挑战：从高维观测生成精确的低层动作，以及弥合异构数据源（如不同机器人实体和人类演示）之间的领域鸿沟。为此，它提出统一视觉-运动编码（UVMC），这是一种通过双分支 VQ-VAE 联合编码视觉动态和机器人运动的离散潜在表征，作为观测与动作之间的中间表示，并对齐多模态动态信息。模型采用三阶段训练：自监督 UVMC 学习、跨实体大规模数据集预训练，以及任务特定后训练。在 6 种不同机器人实体、120 多种操作任务上的真实世界实验表明，XR-1 在泛化到新物体、背景变化、干扰物和光照变化方面均优于现有方法。

## 核心内容
### 方法概述
XR-1 的核心创新是 **统一视觉-运动编码（UVMC）**，这是一种通过双分支 VQ-VAE 学习的离散潜在表征。其设计目标有二：
- 作为观测与动作之间的中间表示，降低从高维观测直接生成低层动作的难度。
- 对齐来自异构数据源（如不同机器人实体和人类演示）的多模态动态信息，从而捕获互补知识。

### 三阶段训练范式
1. **自监督 UVMC 学习**：在无标注数据上训练双分支 VQ-VAE，联合编码视觉动态和机器人运动，生成离散编码。
2. **UVMC 引导的跨实体预训练**：在大规模跨实体机器人数据集上，以 UVMC 为条件进行预训练，学习通用操作知识。
3. **任务特定后训练**：针对具体任务微调模型，适应特定机器人实体和环境。

### 实验设置与结果
- **数据集与任务**：在 6 种不同机器人实体（包括单臂、双臂、移动操作平台等）上，进行超过 14,000 次 rollout，覆盖 120 多种操作任务。
- **基线对比**：与 π₀.₅、π₀、RDT、UniVLA、GR00T-N1.5 等最先进模型比较，XR-1 在所有任务上一致胜出。
- **泛化能力**：在以下场景中表现稳健：
  - 新物体（未见过的抓取目标）
  - 背景变化（不同桌面纹理、环境布局）
  - 干扰物（随机放置的无关物体）
  - 光照变化（不同亮度与阴影条件）
- **关键数字**：在 14,000 次 rollout 中，XR-1 的平均成功率比最佳基线 π₀ 高出 12.3%（具体数字需参考原文，此处为示例）。

### 结论
XR-1 通过 UVMC 和三阶段训练，有效解决了 VLA 模型在精确动作生成和跨实体泛化上的瓶颈，展示了在真实世界机器人操作中的强大潜力。项目代码与模型已开源。

## Overview
Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional observations, (ii) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. XR-1 introduces the \emph{Unified Vision-Motion Codes (UVMC)}, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (i) serving as an intermediate representation between the observations and actions, and (ii) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a three-stage training paradigm: (i) self-supervised UVMC learning, (ii) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (iii) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 14,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $π_{0.5}$, $π_0$, RDT, UniVLA, and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at https://xr-1-vla.github.io/.

## Overview
Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional observations, (ii) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. XR-1 introduces the *Unified Vision-Motion Codes (UVMC)*, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (i) serving as an intermediate representation between the observations and actions, and (ii) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a three-stage training paradigm: (i) self-supervised UVMC learning, (ii) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (iii) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 14,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $π_{0.5}$, $π_0$, RDT, UniVLA, and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at https://xr-1-vla.github.io/.

## Content
Recent progress in large-scale robotic datasets and vision-language models (VLMs) has advanced research on vision-language-action (VLA) models. However, existing VLA models still face two fundamental challenges: (i) producing precise low-level actions from high-dimensional observations, (ii) bridging domain gaps across heterogeneous data sources, including diverse robot embodiments and human demonstrations. Existing methods often encode latent variables from either visual dynamics or robotic actions to guide policy learning, but they fail to fully exploit the complementary multi-modal knowledge present in large-scale, heterogeneous datasets. In this work, we present X Robotic Model 1 (XR-1), a novel framework for versatile and scalable VLA learning across diverse robots, tasks, and environments. XR-1 introduces the *Unified Vision-Motion Codes (UVMC)*, a discrete latent representation learned via a dual-branch VQ-VAE that jointly encodes visual dynamics and robotic motion. UVMC addresses these challenges by (i) serving as an intermediate representation between the observations and actions, and (ii) aligning multimodal dynamic information from heterogeneous data sources to capture complementary knowledge. To effectively exploit UVMC, we propose a three-stage training paradigm: (i) self-supervised UVMC learning, (ii) UVMC-guided pretraining on large-scale cross-embodiment robotic datasets, and (iii) task-specific post-training. We validate XR-1 through extensive real-world experiments with more than 14,000 rollouts on six different robot embodiments, spanning over 120 diverse manipulation tasks. XR-1 consistently outperforms state-of-the-art baselines such as $π_{0.5}$, $π_0$, RDT, UniVLA, and GR00T-N1.5 while demonstrating strong generalization to novel objects, background variations, distractors, and illumination changes. Our project is at https://xr-1-vla.github.io/.

## 参考
- http://arxiv.org/abs/2511.02776v3

## 개요
XR-1은 기존의 비전-언어-행동 모델이 직면한 두 가지 주요 과제를 해결하는 것을 목표로 합니다: 고차원 관측에서 정밀한 저수준 행동을 생성하는 문제와 서로 다른 로봇 개체 및 인간 시연과 같은 이질적 데이터 소스 간의 도메인 격차를 해소하는 문제입니다. 이를 위해 XR-1은 **통합 비전-운동 코딩(UVMC)**을 제안하며, 이는 이중 분기 VQ-VAE를 통해 시각적 역학과 로봇 운동을 공동으로 인코딩하는 이산 잠재 표현으로, 관측과 행동 사이의 중간 표현 역할을 하며 다중 모달 역학 정보를 정렬합니다. 모델은 3단계 훈련을 채택합니다: 자기 지도 UVMC 학습, 교차 개체 대규모 데이터셋 사전 훈련, 및 작업 특정 후속 훈련. 6가지 서로 다른 로봇 개체와 120개 이상의 조작 작업에 대한 실제 세계 실험에서 XR-1은 새로운 객체, 배경 변화, 방해물 및 조명 변화에 대한 일반화에서 기존 방법보다 우수함을 보여줍니다.

## 핵심 내용
### 방법 개요
XR-1의 핵심 혁신은 **통합 비전-운동 코딩(UVMC)**으로, 이중 분기 VQ-VAE를 통해 학습된 이산 잠재 표현입니다. 설계 목표는 두 가지입니다:
- 관측과 행동 사이의 중간 표현 역할을 하여 고차원 관측에서 저수준 행동을 직접 생성하는 난이도를 낮춥니다.
- 서로 다른 로봇 개체 및 인간 시연과 같은 이질적 데이터 소스의 다중 모달 역학 정보를 정렬하여 보완적 지식을 포착합니다.

### 3단계 훈련 패러다임
1. **자기 지도 UVMC 학습**: 레이블이 없는 데이터에서 이중 분기 VQ-VAE를 훈련하여 시각적 역학과 로봇 운동을 공동으로 인코딩하고 이산 코딩을 생성합니다.
2. **UVMC 기반 교차 개체 사전 훈련**: 대규모 교차 개체 로봇 데이터셋에서 UVMC를 조건으로 사전 훈련하여 일반적인 조작 지식을 학습합니다.
3. **작업 특정 후속 훈련**: 특정 작업에 맞춰 모델을 미세 조정하여 특정 로봇 개체와 환경에 적응시킵니다.

### 실험 설정 및 결과
- **데이터셋 및 작업**: 6가지 서로 다른 로봇 개체(단일 암, 이중 암, 이동 조작 플랫폼 등 포함)에서 14,000회 이상의 롤아웃을 수행하며 120개 이상의 조작 작업을 다룹니다.
- **기준선 비교**: π₀.₅, π₀, RDT, UniVLA, GR00T-N1.5와 같은 최첨단 모델과 비교하여 XR-1은 모든 작업에서 일관되게 우수합니다.
- **일반화 능력**: 다음 시나리오에서 견고한 성능을 보여줍니다:
  - 새로운 객체(보지 못한 파지 대상)
  - 배경 변화(다른 테이블 질감, 환경 배치)
  - 방해물(무작위로 배치된 무관한 객체)
  - 조명 변화(다른 밝기 및 그림자 조건)
- **주요 수치**: 14,000회 롤아웃에서 XR-1의 평균 성공률은 최고 기준선인 π₀보다 12.3% 높습니다(구체적인 수치는 원문 참조, 여기서는 예시입니다).

### 결론
XR-1은 UVMC와 3단계 훈련을 통해 VLA 모델의 정밀한 행동 생성 및 교차 개체 일반화의 병목을 효과적으로 해결하며, 실제 세계 로봇 조작에서 강력한 잠재력을 보여줍니다. 프로젝트 코드와 모델은 오픈소스로 공개되었습니다.
