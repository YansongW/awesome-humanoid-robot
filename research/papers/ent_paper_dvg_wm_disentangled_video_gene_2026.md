---
$id: ent_paper_dvg_wm_disentangled_video_gene_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
  zh: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
  ko: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
summary:
  en: 'arXiv:2606.32028v1 Announce Type: new Abstract: Video-based embodied world models provide an appealing substrate for
    robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement:
    accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands
    expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative
    planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video
    Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning
    and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible
    sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos.
    Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics
    to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO
    and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled
    video generation can be an efficient embodied world model for robotic manipulation.'
  zh: DVG-WM 是一种面向机器人操作的高效具身世界模型，由研究团队提出。其核心贡献在于将世界建模显式解耦为动力学学习与视觉合成两个独立过程，从而在提升视频预测质量的同时实现高达 3.97 倍的推理加速。
  ko: 'arXiv:2606.32028v1 Announce Type: new Abstract: Video-based embodied world models provide an appealing substrate for
    robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement:
    accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands
    expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative
    planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video
    Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning
    and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible
    sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos.
    Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics
    to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO
    and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled
    video generation can be an efficient embodied world model for robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dvg_wm
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.32028v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
  url: https://arxiv.org/abs/2606.32028
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有基于视频的具身世界模型面临根本性纠缠：精确建模动力学需要低层时序推理，而生成高分辨率帧又依赖高层语义的视觉合成。这种纠缠导致迭代规划速度慢或预测过于粗糙，无法保留接触丰富的细节。DVG-WM 通过解耦设计解决了这一困境，它先基于初始观测和语言指令生成中间视觉状态序列以预览物理交互，再通过精炼获得高保真视频。此外，模型引入级联机制，利用 flow matching 将动力学直接映射到视频潜空间，并采用潜退化机制再生接触细节。

## 核心内容
### 方法架构
DVG-WM 将世界模型分解为两个模块：
- **动力学学习模块**：专注于低层时序推理，预测物理交互的中间状态序列。
- **视觉合成模块**：负责高层语义驱动的视觉生成，将动力学映射为高分辨率视频帧。

### 级联机制
- **Flow Matching 映射**：将动力学预测直接转换为视频潜变量，避免逐帧生成带来的计算开销。
- **潜退化机制**：在接触丰富的区域主动退化潜变量，再通过生成模型重新合成细节，提升保真度。

### 实验设置
- **基准测试**：在 LIBERO 模拟环境和真实机器人平台上进行评估。
- **对比方法**：与未解耦的视频世界模型进行对比，衡量视频质量和推理速度。

### 关键结果
- **视频质量**：DVG-WM 生成的视频在保真度和细节保留上显著优于基线方法。
- **推理速度**：相比传统方法，实现最高 3.97 倍的加速，验证了解耦设计的高效性。
- **结论**：解耦视频生成可作为机器人操作的高效具身世界模型，兼顾动力学精度与视觉质量。

## Overview
Video-based embodied world models provide an appealing substrate for robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement: accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos. Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled video generation can be an efficient embodied world model for robotic manipulation.

## 개요
비디오 기반 체화된 세계 모델은 미래 상태를 예측하여 로봇 조작을 위한 매력적인 기반을 제공하지만, 현재 접근 방식은 근본적인 얽힘 문제로 인해 제한을 받습니다. 즉, 역학을 정확하게 모델링하려면 일반적으로 저수준 시간적 추론이 필요한 반면, 고해상도 프레임을 생성하려면 고수준 의미론에 따른 광범위한 시각적 합성이 필요합니다. 이러한 얽힘은 반복 계획의 추론 속도를 느리게 하거나 접촉이 많은 세부 정보를 유지하기에는 너무 거친 예측을 초래합니다. 이 딜레마를 해결하기 위해, 우리는 세계 모델링을 역학 학습과 시각적 합성으로 명시적으로 분해하는 효율적인 프레임워크인 Disentangled Video Generation World Model (DVG-WM)을 제시합니다. 초기 관찰과 언어 명령을 조건으로, 우리의 모델은 먼저 물리적 상호 작용을 미리 보기 위한 중간 시각적 상태의 그럴듯한 시퀀스를 생성하고 이를 정제하여 고충실도 비디오를 얻습니다. 또한, 효율적인 캐스케이딩 메커니즘이 제안되며, 여기서 DVG-WM은 흐름 매칭을 사용하여 역학을 비디오 잠재 변수에 직접 매핑하고, 잠재 변수 저하 메커니즘을 도입하여 접촉이 많은 세부 정보를 재생성합니다. LIBERO 및 실제 플랫폼에서의 실험은 최대 3.97배의 가속화와 함께 향상된 비디오 품질을 입증하며, 분리된 비디오 생성이 로봇 조작을 위한 효율적인 체화된 세계 모델이 될 수 있음을 검증합니다.

## 핵심 내용
비디오 기반 체화된 세계 모델은 미래 상태를 예측하여 로봇 조작을 위한 매력적인 기반을 제공하지만, 현재 접근 방식은 근본적인 얽힘 문제로 인해 제한을 받습니다. 즉, 역학을 정확하게 모델링하려면 일반적으로 저수준 시간적 추론이 필요한 반면, 고해상도 프레임을 생성하려면 고수준 의미론에 따른 광범위한 시각적 합성이 필요합니다. 이러한 얽힘은 반복 계획의 추론 속도를 느리게 하거나 접촉이 많은 세부 정보를 유지하기에는 너무 거친 예측을 초래합니다. 이 딜레마를 해결하기 위해, 우리는 세계 모델링을 역학 학습과 시각적 합성으로 명시적으로 분해하는 효율적인 프레임워크인 Disentangled Video Generation World Model (DVG-WM)을 제시합니다. 초기 관찰과 언어 명령을 조건으로, 우리의 모델은 먼저 물리적 상호 작용을 미리 보기 위한 중간 시각적 상태의 그럴듯한 시퀀스를 생성하고 이를 정제하여 고충실도 비디오를 얻습니다. 또한, 효율적인 캐스케이딩 메커니즘이 제안되며, 여기서 DVG-WM은 흐름 매칭을 사용하여 역학을 비디오 잠재 변수에 직접 매핑하고, 잠재 변수 저하 메커니즘을 도입하여 접촉이 많은 세부 정보를 재생성합니다. LIBERO 및 실제 플랫폼에서의 실험은 최대 3.97배의 가속화와 함께 향상된 비디오 품질을 입증하며, 분리된 비디오 생성이 로봇 조작을 위한 효율적인 체화된 세계 모델이 될 수 있음을 검증합니다.

## 参考
- http://arxiv.org/abs/2606.32028v2
