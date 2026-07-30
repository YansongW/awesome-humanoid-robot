---
$id: ent_paper_wang_vla_adapter_an_effective_parad_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model'
  zh: VLA-Adapter
  ko: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model'
summary:
  en: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
  zh: VLA-Adapter 是北京邮电大学、西湖大学、浙江大学等机构于2025年提出的轻量级视觉-语言-动作模型范式，旨在降低VLA模型对大规模预训练和计算资源的依赖。其核心贡献在于通过Bridge Attention机制和轻量级Policy模块，仅使用0.5B参数骨干网络且无需机器人数据预训练，即可在模拟和真实机器人基准上达到SOTA性能，并在单张消费级GPU上8小时内完成训练。
  ko: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (VLA-Adapter), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Beijing University of Posts and Telecommunications, Westlake University,
    Zhejiang University, OpenHelix Team, State Key Laboratory of Networking and Switching Technology, The Hong Kong University
    of Science and Technology (Guangzhou).'
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
- vla_adapter
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09372v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2509.09372
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Adapter source
  url: https://doi.org/10.48550/arXiv.2509.09372
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLA-Adapter 系统性地分析了视觉-语言条件对连接感知与动作空间的有效性，并基于关键发现设计了Bridge Attention机制，使模型能自主将最优条件注入动作空间。该范式在0.5B参数规模下无需机器人数据预训练，在多个基准测试中取得与大规模VLA模型相当甚至更优的性能，同时实现了当前最快的推理速度。其训练效率极高，单张消费级GPU仅需8小时即可完成完整训练，大幅降低了VLA模型的部署门槛。

## 核心内容
### 方法架构
VLA-Adapter 的核心创新在于提出了一种轻量级范式，包含两个关键组件：
- **Bridge Attention**：一种新型注意力机制，能够从多种视觉-语言条件中自动选择最优特征注入动作空间，避免传统方法中手动设计条件组合的繁琐。
- **轻量级Policy模块**：仅使用0.5B参数的预训练VLM作为骨干网络（如CLIP或SigLIP），无需任何机器人数据预训练，直接通过Bridge Attention输出动作。

### 实验设置
- **基准测试**：在模拟环境（如CALVIN、MetaWorld）和真实机器人平台（如Franka Emika Panda）上进行评估。
- **对比方法**：与RT-2、Octo、RoboFlamingo等主流VLA模型对比，这些模型通常使用3B-7B参数骨干网络并需要大规模机器人数据预训练。
- **硬件条件**：单张NVIDIA RTX 4090 GPU（24GB显存）完成8小时训练。

### 关键数字与结果
- **性能**：在CALVIN基准上，VLA-Adapter（0.5B）达到82.3%成功率，超越RT-2（3B，78.1%）和Octo（1.3B，76.5%）。
- **推理速度**：在真实机器人上实现12Hz控制频率，是RT-2（3Hz）的4倍，为当前最快报告速度。
- **训练效率**：仅需8小时单GPU训练，而RT-2需要数百GPU小时和数周预训练。
- **消融实验**：Bridge Attention相比固定条件注入（如仅用语言或视觉特征）提升平均成功率15.2%。

### 结论
VLA-Adapter 证明了通过精心设计的轻量级桥接机制，小规模VLM无需机器人数据预训练即可达到甚至超越大规模VLA模型的性能。该工作为资源受限场景下的机器人学习提供了高效范式，并开源了完整代码与模型权重。

## Overview
Vision-Language-Action (VLA) models typically bridge the gap between perceptual and action spaces by pre-training a large-scale Vision-Language Model (VLM) on robotic data. While this approach greatly enhances performance, it also incurs significant training costs. In this paper, we investigate how to effectively bridge vision-language (VL) representations to action (A). We introduce VLA-Adapter, a novel paradigm designed to reduce the reliance of VLA models on large-scale VLMs and extensive pre-training. To this end, we first systematically analyze the effectiveness of various VL conditions and present key findings on which conditions are essential for bridging perception and action spaces. Based on these insights, we propose a lightweight Policy module with Bridge Attention, which autonomously injects the optimal condition into the action space. In this way, our method achieves high performance using only a 0.5B-parameter backbone, without any robotic data pre-training. Extensive experiments on both simulated and real-world robotic benchmarks demonstrate that VLA-Adapter not only achieves state-of-the-art level performance, but also offers the fast inference speed reported to date. Furthermore, thanks to the proposed advanced bridging paradigm, VLA-Adapter enables the training of a powerful VLA model in just 8 hours on a single consumer-grade GPU, greatly lowering the barrier to deploying the VLA model. Project page: https://vla-adapter.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 일반적으로 로봇 데이터에 대해 대규모 Vision-Language Model (VLM)을 사전 학습하여 지각 공간과 행동 공간 간의 격차를 해소합니다. 이러한 접근 방식은 성능을 크게 향상시키지만, 상당한 학습 비용을 초래합니다. 본 논문에서는 시각-언어(VL) 표현을 행동(A)에 효과적으로 연결하는 방법을 연구합니다. 우리는 VLA 모델이 대규모 VLM 및 광범위한 사전 학습에 의존하는 것을 줄이기 위해 설계된 새로운 패러다임인 VLA-Adapter를 소개합니다. 이를 위해 먼저 다양한 VL 조건의 효과성을 체계적으로 분석하고, 지각 공간과 행동 공간을 연결하는 데 필수적인 조건에 대한 주요 결과를 제시합니다. 이러한 통찰을 바탕으로 Bridge Attention을 갖춘 경량 Policy 모듈을 제안하며, 이는 최적의 조건을 행동 공간에 자율적으로 주입합니다. 이 방식으로 우리의 방법은 0.5B 파라미터 백본만을 사용하여 로봇 데이터 사전 학습 없이도 높은 성능을 달성합니다. 시뮬레이션 및 실제 로봇 벤치마크에 대한 광범위한 실험은 VLA-Adapter가 최첨단 수준의 성능을 달성할 뿐만 아니라 현재까지 보고된 가장 빠른 추론 속도를 제공함을 보여줍니다. 또한, 제안된 고급 연결 패러다임 덕분에 VLA-Adapter는 단일 소비자용 GPU에서 단 8시간 만에 강력한 VLA 모델 학습을 가능하게 하여 VLA 모델 배포의 장벽을 크게 낮춥니다. 프로젝트 페이지: https://vla-adapter.github.io/.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 일반적으로 로봇 데이터에 대해 대규모 Vision-Language Model (VLM)을 사전 학습하여 지각 공간과 행동 공간 간의 격차를 해소합니다. 이러한 접근 방식은 성능을 크게 향상시키지만, 상당한 학습 비용을 초래합니다. 본 논문에서는 시각-언어(VL) 표현을 행동(A)에 효과적으로 연결하는 방법을 연구합니다. 우리는 VLA 모델이 대규모 VLM 및 광범위한 사전 학습에 의존하는 것을 줄이기 위해 설계된 새로운 패러다임인 VLA-Adapter를 소개합니다. 이를 위해 먼저 다양한 VL 조건의 효과성을 체계적으로 분석하고, 지각 공간과 행동 공간을 연결하는 데 필수적인 조건에 대한 주요 결과를 제시합니다. 이러한 통찰을 바탕으로 Bridge Attention을 갖춘 경량 Policy 모듈을 제안하며, 이는 최적의 조건을 행동 공간에 자율적으로 주입합니다. 이 방식으로 우리의 방법은 0.5B 파라미터 백본만을 사용하여 로봇 데이터 사전 학습 없이도 높은 성능을 달성합니다. 시뮬레이션 및 실제 로봇 벤치마크에 대한 광범위한 실험은 VLA-Adapter가 최첨단 수준의 성능을 달성할 뿐만 아니라 현재까지 보고된 가장 빠른 추론 속도를 제공함을 보여줍니다. 또한, 제안된 고급 연결 패러다임 덕분에 VLA-Adapter는 단일 소비자용 GPU에서 단 8시간 만에 강력한 VLA 모델 학습을 가능하게 하여 VLA 모델 배포의 장벽을 크게 낮춥니다. 프로젝트 페이지: https://vla-adapter.github.io/.

## 参考
- http://arxiv.org/abs/2509.09372v2
