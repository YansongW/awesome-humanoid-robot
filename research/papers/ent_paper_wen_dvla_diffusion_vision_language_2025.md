---
$id: ent_paper_wen_dvla_diffusion_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought'
  zh: dVLA
  ko: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought'
summary:
  en: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
  zh: dVLA 是由北京大学和上海交通大学于 2025 年提出的扩散式视觉-语言-动作模型，用于机器人操作。其核心贡献在于利用多模态思维链统一视觉感知、语言推理与机器人控制，并在单一扩散目标下联合优化，在 LIBERO 基准上达到 96.4%
    的平均成功率，同时通过前缀注意力掩码和 KV 缓存实现测试时推理加速。
  ko: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25681v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (910 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (arXiv)'
  url: https://arxiv.org/abs/2509.25681
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: dVLA source
  url: https://doi.org/10.48550/arXiv.2509.25681
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
dVLA 是一种基于扩散的视觉-语言-动作模型，旨在通过多模态思维链将视觉感知、语言推理和机器人控制整合为单一系统。该模型在单一扩散目标下联合优化感知、语言理解和动作生成，从而增强跨模态推理能力，并更好地泛化到新指令和新物体。为应对实际部署中的推理延迟问题，dVLA 引入了前缀注意力掩码和 KV 缓存两种加速策略，在测试时推理中实现了约数倍的速度提升。在 LIBERO 基准上，dVLA 以 96.4% 的平均成功率取得了最先进性能，持续超越离散和连续动作策略；在真实 Franka 机器人上，它成功完成了一系列多样化任务，包括需要多步规划的挑战性抓取任务，展现了稳健的现实世界表现。

## 核心内容
### 方法
- dVLA 采用扩散模型作为核心框架，将视觉感知、语言理解和动作生成统一在单一扩散目标下进行联合优化。
- 通过多模态思维链机制，模型能够依次处理视觉输入、语言指令和动作序列，实现跨模态的推理与决策。

### 架构
- 模型架构基于扩散过程，输入为多模态数据（图像和文本），输出为连续动作序列。
- 为加速推理，引入了两种策略：
  - **前缀注意力掩码**：限制注意力计算范围，减少冗余计算。
  - **KV 缓存**：缓存关键-值对，避免重复计算，提升测试时速度。

### 实验设置
- 在 LIBERO 仿真基准上进行评估，涵盖多种操作任务。
- 在真实世界中使用 Franka 机器人进行测试，任务包括简单操作和复杂多步规划（如 bin-picking）。

### 关键数字
- LIBERO 基准：平均成功率 96.4%，超越所有离散和连续动作策略。
- 推理加速：通过前缀注意力掩码和 KV 缓存，实现约数倍的速度提升（具体倍数未明确给出，但强调“up to around times speedup”）。
- 真实世界表现：在 Franka 机器人上成功完成多样化任务，包括需要多步规划的 bin-picking。

### 结论
- dVLA 证明了统一扩散框架在实用、高性能 VLA 机器人中的潜力，通过联合优化和加速策略，实现了跨模态推理与实时部署的平衡。

## Overview
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## 参考
- http://arxiv.org/abs/2509.25681v1

## 개요
dVLA는 확산 기반의 시각-언어-행동 모델로, 다중 모달 사고 체인을 통해 시각 인식, 언어 추론, 로봇 제어를 단일 시스템으로 통합하는 것을 목표로 합니다. 이 모델은 단일 확산 목표 하에 인식, 언어 이해, 행동 생성을 공동으로 최적화하여 교차 모달 추론 능력을 강화하고 새로운 지시와 새로운 물체에 더 잘 일반화합니다. 실제 배포 시 추론 지연 문제를 해결하기 위해 dVLA는 프리픽스 어텐션 마스크와 KV 캐시라는 두 가지 가속 전략을 도입하여 테스트 시 추론에서 약 수 배의 속도 향상을 달성했습니다. LIBERO 벤치마크에서 dVLA는 96.4%의 평균 성공률로 최첨단 성능을 달성하며 이산 및 연속 행동 정책을 지속적으로 능가했습니다. 실제 Franka 로봇에서는 다단계 계획이 필요한 도전적인 파지 작업을 포함한 다양한 작업을 성공적으로 완료하여 견고한 실제 세계 성능을 입증했습니다.

## 핵심 내용
### 방법
- dVLA는 확산 모델을 핵심 프레임워크로 채택하여 시각 인식, 언어 이해, 행동 생성을 단일 확산 목표 하에 공동 최적화합니다.
- 다중 모달 사고 체인 메커니즘을 통해 모델은 시각 입력, 언어 지시, 행동 시퀀스를 순차적으로 처리하여 교차 모달 추론과 의사 결정을 구현합니다.

### 아키텍처
- 모델 아키텍처는 확산 과정을 기반으로 하며, 입력은 다중 모달 데이터(이미지 및 텍스트)이고 출력은 연속 행동 시퀀스입니다.
- 추론 가속을 위해 두 가지 전략이 도입되었습니다:
  - **프리픽스 어텐션 마스크**: 어텐션 계산 범위를 제한하여 중복 계산을 줄입니다.
  - **KV 캐시**: 키-값 쌍을 캐시하여 반복 계산을 방지하고 테스트 시 속도를 향상시킵니다.

### 실험 설정
- LIBERO 시뮬레이션 벤치마크에서 평가되며 다양한 조작 작업을 포함합니다.
- 실제 세계에서는 Franka 로봇을 사용하여 테스트하며, 작업에는 단순 조작과 복잡한 다단계 계획(예: 빈 피킹)이 포함됩니다.

### 주요 수치
- LIBERO 벤치마크: 평균 성공률 96.4%로 모든 이산 및 연속 행동 정책을 능가합니다.
- 추론 가속: 프리픽스 어텐션 마스크와 KV 캐시를 통해 약 수 배의 속도 향상을 달성합니다(구체적인 배수는 명시되지 않았지만 "up to around times speedup"으로 강조됨).
- 실제 세계 성능: Franka 로봇에서 다단계 계획이 필요한 빈 피킹을 포함한 다양한 작업을 성공적으로 완료합니다.

### 결론
- dVLA는 통합 확산 프레임워크가 실용적이고 고성능의 VLA 로봇에서 잠재력을 입증했으며, 공동 최적화와 가속 전략을 통해 교차 모달 추론과 실시간 배포의 균형을 달성했습니다.
