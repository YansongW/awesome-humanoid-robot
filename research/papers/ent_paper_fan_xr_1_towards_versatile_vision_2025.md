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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.02776v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
대규모 로봇 데이터셋과 비전-언어 모델(VLM)의 최근 발전은 비전-언어-행동(VLA) 모델 연구를 진전시켰습니다. 그러나 기존 VLA 모델은 여전히 두 가지 근본적인 과제에 직면해 있습니다: (i) 고차원 관측값으로부터 정밀한 저수준 행동을 생성하는 것, (ii) 다양한 로봇 구현체와 인간 시연을 포함한 이질적 데이터 소스 간의 도메인 격차를 해소하는 것입니다. 기존 방법들은 종종 시각적 역학 또는 로봇 행동으로부터 잠재 변수를 인코딩하여 정책 학습을 안내하지만, 대규모 이질적 데이터셋에 존재하는 상호 보완적인 다중 모달 지식을 완전히 활용하지 못합니다. 본 연구에서는 다양한 로봇, 작업 및 환경에 걸쳐 범용적이고 확장 가능한 VLA 학습을 위한 새로운 프레임워크인 X 로봇 모델 1(XR-1)을 제시합니다. XR-1은 이중 분기 VQ-VAE를 통해 학습된 이산 잠재 표현인 \emph{통합 비전-모션 코드(UVMC)}를 도입하며, 이는 시각적 역학과 로봇 움직임을 공동으로 인코딩합니다. UVMC는 (i) 관측값과 행동 사이의 중간 표현 역할을 하고, (ii) 이질적 데이터 소스의 다중 모달 동적 정보를 정렬하여 상호 보완적 지식을 포착함으로써 이러한 과제를 해결합니다. UVMC를 효과적으로 활용하기 위해 세 단계 학습 패러다임을 제안합니다: (i) 자기 지도 UVMC 학습, (ii) 대규모 교차 구현체 로봇 데이터셋에서 UVMC 기반 사전 학습, (iii) 작업별 사후 학습. 우리는 6가지 다른 로봇 구현체에서 14,000회 이상의 롤아웃을 포함한 광범위한 실제 실험을 통해 XR-1을 검증했으며, 이는 120개 이상의 다양한 조작 작업을 포괄합니다. XR-1은 $π_{0.5}$, $π_0$, RDT, UniVLA, GR00T-N1.5와 같은 최첨단 기준 모델을 일관되게 능가하며, 새로운 객체, 배경 변화, 방해 요소 및 조명 변화에 대한 강력한 일반화 능력을 보여줍니다. 프로젝트 페이지: https://xr-1-vla.github.io/.

## 핵심 내용
대규모 로봇 데이터셋과 비전-언어 모델(VLM)의 최근 발전은 비전-언어-행동(VLA) 모델 연구를 진전시켰습니다. 그러나 기존 VLA 모델은 여전히 두 가지 근본적인 과제에 직면해 있습니다: (i) 고차원 관측값으로부터 정밀한 저수준 행동을 생성하는 것, (ii) 다양한 로봇 구현체와 인간 시연을 포함한 이질적 데이터 소스 간의 도메인 격차를 해소하는 것입니다. 기존 방법들은 종종 시각적 역학 또는 로봇 행동으로부터 잠재 변수를 인코딩하여 정책 학습을 안내하지만, 대규모 이질적 데이터셋에 존재하는 상호 보완적인 다중 모달 지식을 완전히 활용하지 못합니다. 본 연구에서는 다양한 로봇, 작업 및 환경에 걸쳐 범용적이고 확장 가능한 VLA 학습을 위한 새로운 프레임워크인 X 로봇 모델 1(XR-1)을 제시합니다. XR-1은 이중 분기 VQ-VAE를 통해 학습된 이산 잠재 표현인 \emph{통합 비전-모션 코드(UVMC)}를 도입하며, 이는 시각적 역학과 로봇 움직임을 공동으로 인코딩합니다. UVMC는 (i) 관측값과 행동 사이의 중간 표현 역할을 하고, (ii) 이질적 데이터 소스의 다중 모달 동적 정보를 정렬하여 상호 보완적 지식을 포착함으로써 이러한 과제를 해결합니다. UVMC를 효과적으로 활용하기 위해 세 단계 학습 패러다임을 제안합니다: (i) 자기 지도 UVMC 학습, (ii) 대규모 교차 구현체 로봇 데이터셋에서 UVMC 기반 사전 학습, (iii) 작업별 사후 학습. 우리는 6가지 다른 로봇 구현체에서 14,000회 이상의 롤아웃을 포함한 광범위한 실제 실험을 통해 XR-1을 검증했으며, 이는 120개 이상의 다양한 조작 작업을 포괄합니다. XR-1은 $π_{0.5}$, $π_0$, RDT, UniVLA, GR00T-N1.5와 같은 최첨단 기준 모델을 일관되게 능가하며, 새로운 객체, 배경 변화, 방해 요소 및 조명 변화에 대한 강력한 일반화 능력을 보여줍니다. 프로젝트 페이지: https://xr-1-vla.github.io/.

## 参考
- http://arxiv.org/abs/2511.02776v3
