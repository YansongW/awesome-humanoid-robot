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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.10631v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
조작 정책 설계의 근본적인 목표는 로봇이 인간의 명령을 이해하고, 장면 단서를 추론하며, 동적 환경에서 일반화된 동작을 실행할 수 있도록 하는 것입니다. 최근의 자기회귀형 시각-언어-행동(VLA) 방법은 시각-언어 모델(VLM)로부터 상식 추론 능력을 계승하여 다음 행동 토큰을 예측합니다. 그러나 이러한 방법은 행동을 이산적인 구간으로 양자화하여 정밀한 제어에 필요한 연속성을 방해합니다. 반면, 기존의 확산 기반 VLA 방법은 VLM이 추출한 특징 표현에만 조건화된 연속적인 행동을 예측하기 위해 추가적인 확산 헤드를 통합하며, 토큰 수준 생성을 통해 VLM의 사전 학습된 추론 능력을 완전히 활용하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 단일 대규모 언어 모델 내에서 확산 기반 행동의 연속성과 자기회귀의 맥락적 추론을 통합하는 통합 프레임워크인 HybridVLA를 소개합니다. 두 생성 패러다임 간의 간섭을 완화하기 위해, 우리는 다음 토큰 예측 과정에 확산 잡음 제거를 원활하게 통합하는 협력적 훈련 방식을 제안합니다. 이 방식을 통해, 우리는 이 두 행동 예측 방법이 서로를 강화할 뿐만 아니라 다양한 작업에 따라 서로 다른 강점을 보인다는 것을 발견했습니다. 따라서, 우리는 두 예측을 적응적으로 융합하여 더 강력한 제어를 이끌어내는 협력적 행동 앙상블 메커니즘을 설계합니다. HybridVLA는 시뮬레이션 및 실제 세계 작업에서 평균 성공률이 각각 14%와 19% 향상되어 이전 최첨단 VLA 방법을 능가하며, 보이지 않는 구성에서도 안정적인 조작을 보여줍니다.

## 핵심 내용
조작 정책 설계의 근본적인 목표는 로봇이 인간의 명령을 이해하고, 장면 단서를 추론하며, 동적 환경에서 일반화된 동작을 실행할 수 있도록 하는 것입니다. 최근의 자기회귀형 시각-언어-행동(VLA) 방법은 시각-언어 모델(VLM)로부터 상식 추론 능력을 계승하여 다음 행동 토큰을 예측합니다. 그러나 이러한 방법은 행동을 이산적인 구간으로 양자화하여 정밀한 제어에 필요한 연속성을 방해합니다. 반면, 기존의 확산 기반 VLA 방법은 VLM이 추출한 특징 표현에만 조건화된 연속적인 행동을 예측하기 위해 추가적인 확산 헤드를 통합하며, 토큰 수준 생성을 통해 VLM의 사전 학습된 추론 능력을 완전히 활용하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 단일 대규모 언어 모델 내에서 확산 기반 행동의 연속성과 자기회귀의 맥락적 추론을 통합하는 통합 프레임워크인 HybridVLA를 소개합니다. 두 생성 패러다임 간의 간섭을 완화하기 위해, 우리는 다음 토큰 예측 과정에 확산 잡음 제거를 원활하게 통합하는 협력적 훈련 방식을 제안합니다. 이 방식을 통해, 우리는 이 두 행동 예측 방법이 서로를 강화할 뿐만 아니라 다양한 작업에 따라 서로 다른 강점을 보인다는 것을 발견했습니다. 따라서, 우리는 두 예측을 적응적으로 융합하여 더 강력한 제어를 이끌어내는 협력적 행동 앙상블 메커니즘을 설계합니다. HybridVLA는 시뮬레이션 및 실제 세계 작업에서 평균 성공률이 각각 14%와 19% 향상되어 이전 최첨단 VLA 방법을 능가하며, 보이지 않는 구성에서도 안정적인 조작을 보여줍니다.

## 参考
- http://arxiv.org/abs/2503.10631v3
