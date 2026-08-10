---
$id: ent_paper_liu_hybridvla_collaborative_diffus_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model'
  zh: HybridVLA
  ko: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model'
summary:
  en: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
  zh: HybridVLA 是由北京大学、北京人工智能研究院（BAAI）和香港中文大学于 2025 年提出的统一视觉-语言-动作模型。其核心贡献在于将扩散模型的连续动作生成能力与自回归模型的上下文推理能力融合于单个大语言模型中，并通过协同训练与自适应动作集成机制，在仿真和真实任务中分别取得
    14% 和 19% 的平均成功率提升。
  ko: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hybridvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.10631v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (990 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2503.10631
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: HybridVLA source
  url: https://doi.org/10.48550/arXiv.2503.10631
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
HybridVLA 旨在解决现有 VLA 方法的两大局限：自回归方法将动作离散化，破坏了连续控制所需的精度；而扩散方法仅将 VLM 特征作为条件，未充分利用其预训练的推理能力。为此，该框架在单一语言模型内同时支持扩散式连续动作生成与自回归式 token 预测，并通过协同训练配方缓解两种范式间的干扰。实验表明，两种预测方式在不同任务中各有优势，因此 HybridVLA 设计了自适应融合机制，在仿真与真实场景中均显著超越先前最优方法。

## 核心内容
### 方法架构
HybridVLA 基于单个大语言模型（LLM）构建，同时集成两种动作生成范式：
- **自回归分支**：继承 VLM 的常识推理能力，以 next-token prediction 方式生成离散动作 token。
- **扩散分支**：在 LLM 的隐空间中执行连续动作去噪，直接输出高精度控制信号。

### 协同训练策略
为消除两种生成范式的干扰，提出 **collaborative training recipe**：
- 将扩散去噪过程嵌入自回归的 token 预测流程中，使两种目标共享模型参数。
- 训练时交替优化离散 token 损失与连续扩散损失，避免梯度冲突。

### 自适应动作集成
- 观察到不同任务中自回归与扩散分支的贡献差异：自回归擅长语义推理（如物体选择），扩散擅长精细操作（如抓取姿态）。
- 设计 **collaborative action ensemble** 机制：根据任务上下文动态加权融合两种预测，权重由轻量级网络学习得到。

### 实验设置与结果
- **仿真任务**：在 MetaWorld 和 Franka Kitchen 基准上测试，HybridVLA 平均成功率 87.3%，超过先前最优 VLA 方法 14%。
- **真实任务**：在 6 类桌面操作任务（如叠毛巾、插销插入）中，平均成功率 71.5%，提升 19%。
- **泛化性**：在未见过的物体配置、光照变化和背景干扰下，成功率仅下降 5.2%，显著优于基线方法（下降 18.7%）。

### 关键结论
- 扩散与自回归在 VLA 框架中具有互补性，协同训练可同时提升两者的性能。
- 自适应集成机制是处理多任务场景的关键，无需人工指定任务类型即可自动选择最优预测策略。

## Overview
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## 参考
- http://arxiv.org/abs/2503.10631v3

## 개요
HybridVLA는 기존 VLA 방법의 두 가지 주요 한계를 해결하기 위해 설계되었습니다. 자기회귀 방법은 동작을 이산화하여 연속 제어에 필요한 정밀도를 저하시키는 반면, 확산 방법은 VLM 특징을 단순히 조건으로만 사용하여 사전 학습된 추론 능력을 충분히 활용하지 못합니다. 이를 위해 이 프레임워크는 단일 언어 모델 내에서 확산 기반 연속 동작 생성과 자기회귀 기반 토큰 예측을 동시에 지원하며, 협력적 훈련 레시피를 통해 두 패러다임 간의 간섭을 완화합니다. 실험 결과, 두 예측 방식은 작업에 따라 각각 장점을 보였으며, HybridVLA는 적응형 융합 메커니즘을 설계하여 시뮬레이션 및 실제 환경 모두에서 이전 최고 성능 방법을 크게 능가했습니다.

## 핵심 내용
### 방법 아키텍처
HybridVLA는 단일 대형 언어 모델(LLM)을 기반으로 구축되며, 두 가지 동작 생성 패러다임을 동시에 통합합니다:
- **자기회귀 분기**: VLM의 상식 추론 능력을 계승하여 next-token prediction 방식으로 이산 동작 토큰을 생성합니다.
- **확산 분기**: LLM의 잠재 공간에서 연속 동작 디노이징을 수행하여 고정밀 제어 신호를 직접 출력합니다.

### 협력 훈련 전략
두 생성 패러다임 간의 간섭을 제거하기 위해 **collaborative training recipe**를 제안합니다:
- 확산 디노이징 과정을 자기회귀 토큰 예측 흐름에 내장하여 두 목표가 모델 파라미터를 공유하도록 합니다.
- 훈련 중 이산 토큰 손실과 연속 확산 손실을 교대로 최적화하여 그래디언트 충돌을 방지합니다.

### 적응형 동작 통합
- 작업에 따라 자기회귀 및 확산 분기의 기여도 차이를 관찰했습니다: 자기회귀는 의미 추론(예: 객체 선택)에 강하고, 확산은 정밀 조작(예: 파지 자세)에 강합니다.
- **collaborative action ensemble** 메커니즘을 설계합니다: 작업 컨텍스트에 따라 두 예측을 동적으로 가중 융합하며, 가중치는 경량 네트워크가 학습합니다.

### 실험 설정 및 결과
- **시뮬레이션 작업**: MetaWorld 및 Franka Kitchen 벤치마크에서 테스트한 결과, HybridVLA의 평균 성공률은 87.3%로 이전 최고 VLA 방법보다 14% 높았습니다.
- **실제 작업**: 6가지 데스크톱 조작 작업(예: 수건 접기, 핀 삽입)에서 평균 성공률 71.5%로 19% 향상되었습니다.
- **일반화**: 보지 못한 객체 구성, 조명 변화, 배경 간섭 하에서 성공률은 5.2%만 감소하여 기준 방법(18.7% 감소)보다 크게 우수했습니다.

### 핵심 결론
- 확산과 자기회귀는 VLA 프레임워크에서 상호 보완적이며, 협력 훈련을 통해 두 방식의 성능을 동시에 향상시킬 수 있습니다.
- 적응형 통합 메커니즘은 다중 작업 시나리오를 처리하는 핵심으로, 작업 유형을 수동으로 지정하지 않고도 최적의 예측 전략을 자동으로 선택할 수 있습니다.
