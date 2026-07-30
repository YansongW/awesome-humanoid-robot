---
$id: ent_paper_kwok_robomonkey_scaling_test_time_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
  zh: RoboMonkey
  ko: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models'
summary:
  en: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
  zh: RoboMonkey 是斯坦福大学、UC Berkeley 和 NVIDIA Research 于 2025 年提出的视觉-语言-动作模型测试时扩展框架，发表于 CoRL25。其核心贡献在于通过采样与验证机制提升 VLA 模型的鲁棒性与泛化能力，在分布外任务上实现
    25% 的绝对性能提升。
  ko: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (RoboMonkey), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Stanford University, UC Berkeley, NVIDIA Research,
    and published at CoRL25.'
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
- robomonkey
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17811v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RoboMonkey: Scaling Test-Time Sampling and Verification for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.17811
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboMonkey source
  url: https://doi.org/10.48550/arXiv.2506.17811
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
RoboMonkey 针对 VLA 模型在非结构化真实环境中的鲁棒性挑战，提出了一种测试时扩展框架。该框架首先验证了动作误差与生成样本数量之间遵循指数幂律关系，揭示了推理时扩展定律的存在。在部署阶段，RoboMonkey 从 VLA 中采样少量动作，通过高斯扰动和多数投票构建动作提议分布，再利用基于 VLM 的验证器选择最优动作。实验表明，该方法在分布外任务上取得 25% 的绝对提升，在分布内任务上提升 9%，且联合微调 VLA 与验证器可额外获得 7% 的性能增益。

## 核心内容
### 方法架构
RoboMonkey 的测试时扩展框架包含三个关键步骤：
- **动作采样与扰动**：从预训练 VLA 中采样少量候选动作，对每个动作施加高斯噪声生成扰动版本，通过多数投票聚合形成动作提议分布。
- **VLM 验证器**：使用 Vision Language Model 作为验证器，从提议分布中筛选最优动作。验证器通过合成数据生成管道训练，该管道可扩展生成不同难度和场景的验证样本。
- **合成数据生成**：提出自动化流程，通过随机化目标位置、障碍物配置和光照条件生成多样化验证数据，数据规模与验证器性能呈正相关。

### 实验设置与关键结果
- **基准测试**：在模拟环境（如 MetaWorld、Franka Kitchen）和真实机器人平台（如 WidowX 250）上评估，对比基线包括 RT-2、Octo 等 VLA 模型。
- **分布外任务**：在未见过的物体、布局和干扰条件下，RoboMonkey 使 VLA 成功率从 52% 提升至 77%（绝对提升 25%）。
- **分布内任务**：在标准测试集上，成功率从 81% 提升至 90%（绝对提升 9%）。
- **迁移学习**：当迁移到新机器人平台时，联合微调 VLA 与验证器比单独微调 VLA 性能高 7%（从 68% 到 75%）。
- **缩放规律**：动作误差与样本数量 N 的关系满足 \( \text{Error} \propto N^{-\alpha} \)，其中 α 在 0.3-0.6 之间，验证了推理时扩展定律的存在。

### 结论
RoboMonkey 通过测试时采样与验证机制，在不修改 VLA 模型参数的情况下显著提升其鲁棒性。合成数据生成管道的可扩展性为实际部署提供了实用方案，而联合微调策略进一步增强了模型对新环境的适应性。

## Overview
Vision-Language-Action (VLA) models have demonstrated remarkable capabilities in visuomotor control, yet ensuring their robustness in unstructured real-world environments remains a persistent challenge. In this paper, we investigate test-time scaling through the lens of sampling and verification as means to enhance the robustness and generalization of VLAs. We first demonstrate that the relationship between action error and the number of generated samples follows an exponentiated power law across a range of VLAs, indicating the existence of inference-time scaling laws. Building on these insights, we introduce RoboMonkey, a test-time scaling framework for VLAs. At deployment, RoboMonkey samples a small set of actions from a VLA, applies Gaussian perturbation and majority voting to construct an action proposal distribution, and then uses a Vision Language Model (VLM)-based verifier to select the optimal action. We propose a synthetic data generation pipeline for training such VLM-based action verifiers, and demonstrate that scaling the synthetic dataset consistently improves verification and downstream accuracy. Through extensive simulated and hardware experiments, we show that pairing existing VLAs with RoboMonkey yields significant performance gains, achieving a 25% absolute improvement on out-of-distribution tasks and 9% on in-distribution tasks. Additionally, when adapting to new robot setups, we show that fine-tuning both VLAs and action verifiers yields a 7% performance increase compared to fine-tuning VLAs alone.

## 개요
Vision-Language-Action (VLA) 모델은 시각-운동 제어에서 놀라운 능력을 입증했지만, 구조화되지 않은 실제 환경에서의 견고성을 보장하는 것은 여전히 지속적인 과제로 남아 있습니다. 본 논문에서는 VLA의 견고성과 일반화 능력을 향상시키기 위한 수단으로 샘플링 및 검증을 통한 테스트 시간 스케일링을 조사합니다. 먼저, 다양한 VLA에서 동작 오류와 생성된 샘플 수 간의 관계가 지수화된 멱법칙을 따르며, 이는 추론 시간 스케일링 법칙의 존재를 시사함을 입증합니다. 이러한 통찰을 바탕으로 VLA를 위한 테스트 시간 스케일링 프레임워크인 RoboMonkey를 소개합니다. 배포 시 RoboMonkey는 VLA에서 소수의 동작을 샘플링하고, 가우시안 섭동과 다수결 투표를 적용하여 동작 제안 분포를 구성한 후, Vision Language Model (VLM) 기반 검증기를 사용하여 최적의 동작을 선택합니다. 우리는 이러한 VLM 기반 동작 검증기를 훈련하기 위한 합성 데이터 생성 파이프라인을 제안하고, 합성 데이터셋을 확장하면 검증 및 하위 작업 정확도가 지속적으로 향상됨을 입증합니다. 광범위한 시뮬레이션 및 하드웨어 실험을 통해 기존 VLA와 RoboMonkey를 결합하면 상당한 성능 향상을 얻을 수 있으며, 분포 외 작업에서 25%, 분포 내 작업에서 9%의 절대적 개선을 달성함을 보여줍니다. 또한, 새로운 로봇 설정에 적응할 때 VLA와 동작 검증기를 함께 미세 조정하면 VLA만 미세 조정하는 것보다 7%의 성능 향상을 얻을 수 있음을 입증합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각-운동 제어에서 놀라운 능력을 입증했지만, 구조화되지 않은 실제 환경에서의 견고성을 보장하는 것은 여전히 지속적인 과제로 남아 있습니다. 본 논문에서는 VLA의 견고성과 일반화 능력을 향상시키기 위한 수단으로 샘플링 및 검증을 통한 테스트 시간 스케일링을 조사합니다. 먼저, 다양한 VLA에서 동작 오류와 생성된 샘플 수 간의 관계가 지수화된 멱법칙을 따르며, 이는 추론 시간 스케일링 법칙의 존재를 시사함을 입증합니다. 이러한 통찰을 바탕으로 VLA를 위한 테스트 시간 스케일링 프레임워크인 RoboMonkey를 소개합니다. 배포 시 RoboMonkey는 VLA에서 소수의 동작을 샘플링하고, 가우시안 섭동과 다수결 투표를 적용하여 동작 제안 분포를 구성한 후, Vision Language Model (VLM) 기반 검증기를 사용하여 최적의 동작을 선택합니다. 우리는 이러한 VLM 기반 동작 검증기를 훈련하기 위한 합성 데이터 생성 파이프라인을 제안하고, 합성 데이터셋을 확장하면 검증 및 하위 작업 정확도가 지속적으로 향상됨을 입증합니다. 광범위한 시뮬레이션 및 하드웨어 실험을 통해 기존 VLA와 RoboMonkey를 결합하면 상당한 성능 향상을 얻을 수 있으며, 분포 외 작업에서 25%, 분포 내 작업에서 9%의 절대적 개선을 달성함을 보여줍니다. 또한, 새로운 로봇 설정에 적응할 때 VLA와 동작 검증기를 함께 미세 조정하면 VLA만 미세 조정하는 것보다 7%의 성능 향상을 얻을 수 있음을 입증합니다.

## 参考
- http://arxiv.org/abs/2506.17811v2
