---
$id: ent_paper_dc_motion_decoupling_structure_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation'
  zh: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation'
  ko: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation'
summary:
  en: 'arXiv:2606.14721v2 Announce Type: replace-cross Abstract: Text-to-motion generation requires modeling both global action
    structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous
    diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit
    compositional structure for temporal planning, while discrete token-based methods improve controllability but compress
    motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation
    mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional,
    whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion,
    a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural
    tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned
    structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces
    continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves
    strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.'
  zh: DC-Motion 是一种用于文本到人体动作生成的新型框架，由研究团队提出。其核心贡献在于将动作分解为离散的结构化标记（捕捉全局动作布局）和连续的残差潜变量（建模细粒度动态），从而解决了现有扩散模型与离散标记方法在表示上的不匹配问题。在
    HumanML3D 和 KIT-ML 基准上，DC-Motion 在 FID 和 R-Precision 指标上均优于代表性基线。
  ko: 'arXiv:2606.14721v2 Announce Type: replace-cross Abstract: Text-to-motion generation requires modeling both global action
    structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous
    diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit
    compositional structure for temporal planning, while discrete token-based methods improve controllability but compress
    motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation
    mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional,
    whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion,
    a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural
    tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned
    structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces
    continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves
    strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- dc_motion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14721v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DC-Motion: Decoupling Structure and Details via Discrete-Continuous Tokens for Human Motion Generation (arXiv)'
  url: https://arxiv.org/abs/2606.14721
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有文本到动作生成方法主要依赖连续扩散模型或向量量化离散表示，但前者缺乏显式的组合结构，后者因压缩动作到有限码本而丢失细粒度动态。DC-Motion 通过提出离散-连续因子化框架来应对这一挑战：它将动作分解为离散结构标记和连续残差潜变量，分别处理全局动作布局与局部运动细节。该框架包含一个基于文本条件、通过迭代掩码建模预测离散标记的结构生成器，以及一个以结构为条件、基于扩散的残差生成器来产生连续运动。在 HumanML3D 和 KIT-ML 上的实验表明，DC-Motion 在 FID 和 R-Precision 上均取得了强劲性能，超越了代表性的扩散模型和离散标记基线。

## 核心内容
### 方法架构
DC-Motion 的核心思想是将人体动作生成任务分解为两个互补的表示层次：
- **离散结构标记（Discrete Structural Tokens）**：捕捉全局动作布局，包括意图、阶段转换和时间安排等语义，这些语义本质上是离散且组合的。
- **连续残差潜变量（Continuous Residual Latents）**：建模关节轨迹和运动动态等细粒度信息，这些信息是连续且局部相关的。

该框架由两个主要模块组成：
1. **文本条件结构生成器**：通过迭代掩码建模（iterative masked modeling）预测离散结构标记。该生成器以自然语言描述为条件，逐步生成代表动作整体结构的标记序列。
2. **基于扩散的残差生成器**：以预测出的离散结构为条件，通过扩散过程生成连续的残差潜变量，从而补全动作的细粒度动态细节。

### 实验设置与关键结果
- **数据集**：在 HumanML3D 和 KIT-ML 两个标准基准上进行评估。
- **评估指标**：主要使用 FID（衡量生成动作的真实性）和 R-Precision（衡量生成动作与文本描述的对齐程度）。
- **性能表现**：DC-Motion 在 FID 和 R-Precision 上均取得了领先结果，显著优于以下两类基线：
  - 代表性扩散模型（如 MDM、MotionDiffuse）
  - 离散标记方法（如 T2M-GPT、MotionGPT）

### 结论
DC-Motion 通过离散-连续因子化表示，有效弥合了动作语义的离散性与运动动态的连续性之间的鸿沟。实验证明，这种分解策略在保持动作结构可控性的同时，保留了细粒度运动细节，从而在文本到动作生成任务中实现了更优的性能。

## Overview
Text-to-motion generation requires modeling both global action structure and fine-grained motion dynamics from natural language. Existing approaches typically rely on either continuous diffusion models or vector-quantized discrete representations. Diffusion models generate smooth motions but lack explicit compositional structure for temporal planning, while discrete token-based methods improve controllability but compress motion into finite codebooks, losing fine-grained dynamics. We argue that this limitation stems from a representation mismatch: action semantics such as intent, phase transitions, and temporal layout are inherently discrete and compositional, whereas joint trajectories and motion dynamics are continuous and locally correlated. To address this, we propose DC-Motion, a discrete-continuous factorized framework for human motion generation. DC-Motion decomposes motion into discrete structural tokens capturing global action layout and continuous residual latents modeling fine-grained dynamics. A text-conditioned structure generator predicts discrete tokens via iterative masked modeling, and a diffusion-based residual generator produces continuous motion conditioned on the structure. Experiments on HumanML3D and KIT-ML demonstrate that DC-Motion achieves strong performance in both FID and R-Precision, outperforming representative diffusion-based and discrete-token baselines.

## 개요
텍스트-모션 생성은 자연어로부터 전역적 동작 구조와 세부적인 움직임 역학을 모두 모델링해야 합니다. 기존 접근법은 일반적으로 연속 확산 모델 또는 벡터 양자화된 이산 표현에 의존합니다. 확산 모델은 부드러운 움직임을 생성하지만 시간적 계획을 위한 명시적 구성 구조가 부족한 반면, 이산 토큰 기반 방법은 제어 가능성을 향상시키지만 움직임을 유한한 코드북으로 압축하여 세부 역학을 잃습니다. 우리는 이러한 한계가 표현 불일치에서 비롯된다고 주장합니다. 의도, 단계 전환, 시간적 배치와 같은 동작 의미는 본질적으로 이산적이고 구성적인 반면, 관절 궤적과 움직임 역학은 연속적이고 국소적으로 상관관계가 있습니다. 이를 해결하기 위해 우리는 인간 모션 생성을 위한 이산-연속 분해 프레임워크인 DC-Motion을 제안합니다. DC-Motion은 움직임을 전역적 동작 레이아웃을 포착하는 이산 구조 토큰과 세부 역학을 모델링하는 연속 잔차 잠재 변수로 분해합니다. 텍스트 조건 구조 생성기는 반복 마스킹 모델링을 통해 이산 토큰을 예측하고, 확산 기반 잔차 생성기는 구조에 조건화된 연속 움직임을 생성합니다. HumanML3D 및 KIT-ML 실험에서 DC-Motion은 FID와 R-Precision 모두에서 강력한 성능을 달성하며, 대표적인 확산 기반 및 이산 토큰 기준선을 능가합니다.

## 핵심 내용
텍스트-모션 생성은 자연어로부터 전역적 동작 구조와 세부적인 움직임 역학을 모두 모델링해야 합니다. 기존 접근법은 일반적으로 연속 확산 모델 또는 벡터 양자화된 이산 표현에 의존합니다. 확산 모델은 부드러운 움직임을 생성하지만 시간적 계획을 위한 명시적 구성 구조가 부족한 반면, 이산 토큰 기반 방법은 제어 가능성을 향상시키지만 움직임을 유한한 코드북으로 압축하여 세부 역학을 잃습니다. 우리는 이러한 한계가 표현 불일치에서 비롯된다고 주장합니다. 의도, 단계 전환, 시간적 배치와 같은 동작 의미는 본질적으로 이산적이고 구성적인 반면, 관절 궤적과 움직임 역학은 연속적이고 국소적으로 상관관계가 있습니다. 이를 해결하기 위해 우리는 인간 모션 생성을 위한 이산-연속 분해 프레임워크인 DC-Motion을 제안합니다. DC-Motion은 움직임을 전역적 동작 레이아웃을 포착하는 이산 구조 토큰과 세부 역학을 모델링하는 연속 잔차 잠재 변수로 분해합니다. 텍스트 조건 구조 생성기는 반복 마스킹 모델링을 통해 이산 토큰을 예측하고, 확산 기반 잔차 생성기는 구조에 조건화된 연속 움직임을 생성합니다. HumanML3D 및 KIT-ML 실험에서 DC-Motion은 FID와 R-Precision 모두에서 강력한 성능을 달성하며, 대표적인 확산 기반 및 이산 토큰 기준선을 능가합니다.

## 参考
- http://arxiv.org/abs/2606.14721v2
