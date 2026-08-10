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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.17811v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1031 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.17811v2

## 개요
RoboMonkey는 비구조화된 실제 환경에서 VLA 모델의 견고성 문제를 해결하기 위해 테스트 시 확장 프레임워크를 제안합니다. 이 프레임워크는 먼저 동작 오류와 생성 샘플 수 사이에 지수 멱법칙 관계가 성립함을 검증하여 추론 시 확장 법칙의 존재를 밝힙니다. 배포 단계에서 RoboMonkey는 VLA에서 소량의 동작을 샘플링하고, 가우시안 교란과 다수결 투표를 통해 동작 제안 분포를 구성한 후, VLM 기반 검증기를 사용하여 최적의 동작을 선택합니다. 실험 결과, 이 방법은 분포 외 작업에서 25%의 절대적 향상을, 분포 내 작업에서 9%의 향상을 달성했으며, VLA와 검증기를 공동 미세 조정하면 추가로 7%의 성능 향상을 얻을 수 있습니다.

## 핵심 내용
### 방법 아키텍처
RoboMonkey의 테스트 시 확장 프레임워크는 세 가지 핵심 단계로 구성됩니다:
- **동작 샘플링 및 교란**: 사전 훈련된 VLA에서 소량의 후보 동작을 샘플링하고, 각 동작에 가우시안 노이즈를 적용하여 교란 버전을 생성한 후, 다수결 투표를 통해 집계하여 동작 제안 분포를 형성합니다.
- **VLM 검증기**: Vision Language Model을 검증기로 사용하여 제안 분포에서 최적의 동작을 선별합니다. 검증기는 합성 데이터 생성 파이프라인을 통해 훈련되며, 이 파이프라인은 다양한 난이도와 시나리오의 검증 샘플을 확장 생성할 수 있습니다.
- **합성 데이터 생성**: 목표 위치, 장애물 구성, 조명 조건을 무작위화하여 다양한 검증 데이터를 생성하는 자동화된 프로세스를 제안하며, 데이터 규모는 검증기 성능과 양의 상관관계를 가집니다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 시뮬레이션 환경(예: MetaWorld, Franka Kitchen)과 실제 로봇 플랫폼(예: WidowX 250)에서 평가하며, 비교 기준에는 RT-2, Octo 등의 VLA 모델이 포함됩니다.
- **분포 외 작업**: 보지 못한 객체, 레이아웃, 교란 조건에서 RoboMonkey는 VLA 성공률을 52%에서 77%로 향상시킵니다(절대적 향상 25%).
- **분포 내 작업**: 표준 테스트 세트에서 성공률이 81%에서 90%로 향상됩니다(절대적 향상 9%).
- **전이 학습**: 새로운 로봇 플랫폼으로 전이할 때, VLA와 검증기를 공동 미세 조정하면 VLA만 미세 조정하는 것보다 성능이 7% 높습니다(68%에서 75%로).
- **확장 법칙**: 동작 오류와 샘플 수 N의 관계는 \( \text{Error} \propto N^{-\alpha} \)를 만족하며, 여기서 α는 0.3-0.6 사이로, 추론 시 확장 법칙의 존재를 검증합니다.

### 결론
RoboMonkey는 테스트 시 샘플링 및 검증 메커니즘을 통해 VLA 모델 파라미터를 수정하지 않고도 견고성을 크게 향상시킵니다. 합성 데이터 생성 파이프라인의 확장성은 실제 배포에 실용적인 솔루션을 제공하며, 공동 미세 조정 전략은 새로운 환경에 대한 모델의 적응성을 더욱 강화합니다.
