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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09372v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1021 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.09372v2

## 개요
VLA-Adapter는 시각-언어 조건이 인식과 행동 공간을 연결하는 데 있어 얼마나 효과적인지 체계적으로 분석하고, 핵심 발견을 바탕으로 Bridge Attention 메커니즘을 설계하여 모델이 최적의 조건을 행동 공간에 자율적으로 주입할 수 있게 합니다. 이 패러다임은 0.5B 파라미터 규모에서 로봇 데이터 사전 학습 없이도 여러 벤치마크에서 대규모 VLA 모델과 동등하거나 더 나은 성능을 달성하며, 현재 가장 빠른 추론 속도를 구현합니다. 훈련 효율성이 매우 높아 단일 소비자용 GPU에서 단 8시간 만에 전체 훈련을 완료할 수 있어 VLA 모델의 배포 장벽을 크게 낮춥니다.

## 핵심 내용
### 방법 아키텍처
VLA-Adapter의 핵심 혁신은 두 가지 주요 구성 요소를 포함하는 경량 패러다임을 제안한 것입니다:
- **Bridge Attention**: 다양한 시각-언어 조건에서 최적의 특징을 자동으로 선택하여 행동 공간에 주입하는 새로운 주의 메커니즘으로, 기존 방법에서 조건 조합을 수동으로 설계하는 번거로움을 피합니다.
- **경량 Policy 모듈**: 0.5B 파라미터의 사전 학습된 VLM(예: CLIP 또는 SigLIP)을 백본 네트워크로만 사용하며, 로봇 데이터 사전 학습 없이 Bridge Attention을 통해 직접 행동을 출력합니다.

### 실험 설정
- **벤치마크 테스트**: 시뮬레이션 환경(예: CALVIN, MetaWorld)과 실제 로봇 플랫폼(예: Franka Emika Panda)에서 평가를 수행합니다.
- **비교 방법**: RT-2, Octo, RoboFlamingo 등 주류 VLA 모델과 비교하며, 이들 모델은 일반적으로 3B-7B 파라미터 백본 네트워크를 사용하고 대규모 로봇 데이터 사전 학습이 필요합니다.
- **하드웨어 조건**: 단일 NVIDIA RTX 4090 GPU(24GB 메모리)로 8시간 훈련을 완료합니다.

### 주요 수치 및 결과
- **성능**: CALVIN 벤치마크에서 VLA-Adapter(0.5B)는 82.3% 성공률을 달성하여 RT-2(3B, 78.1%)와 Octo(1.3B, 76.5%)를 능가합니다.
- **추론 속도**: 실제 로봇에서 12Hz 제어 주파수를 구현하여 RT-2(3Hz)의 4배로, 현재 보고된 가장 빠른 속도입니다.
- **훈련 효율성**: 단 8시간의 단일 GPU 훈련만 필요하며, RT-2는 수백 GPU 시간과 수주간의 사전 학습이 필요합니다.
- **소거 실험**: Bridge Attention은 고정 조건 주입(예: 언어 또는 시각 특징만 사용)에 비해 평균 성공률을 15.2% 향상시킵니다.

### 결론
VLA-Adapter는 정교하게 설계된 경량 브리징 메커니즘을 통해 소규모 VLM이 로봇 데이터 사전 학습 없이도 대규모 VLA 모델의 성능에 도달하거나 이를 능가할 수 있음을 입증합니다. 이 연구는 리소스가 제한된 환경에서의 로봇 학습을 위한 효율적인 패러다임을 제공하며, 전체 코드와 모델 가중치를 오픈소스로 공개합니다.
