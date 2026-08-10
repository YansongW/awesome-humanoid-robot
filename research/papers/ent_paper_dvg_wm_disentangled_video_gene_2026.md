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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.32028v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (691 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.32028v2

## 개요
기존의 비디오 기반 구현형 세계 모델은 근본적인 얽힘 문제를 겪고 있습니다. 역학을 정밀하게 모델링하려면 저수준 시계열 추론이 필요한 반면, 고해상도 프레임을 생성하려면 고수준 의미론적 시각 합성이 필요합니다. 이러한 얽힘은 반복 계획 속도를 느리게 하거나 예측이 너무 거칠어 접촉이 풍부한 세부 정보를 보존하지 못하게 합니다. DVG-WM은 분리 설계를 통해 이 문제를 해결하며, 초기 관측과 언어 지시를 기반으로 중간 시각 상태 시퀀스를 먼저 생성하여 물리적 상호작용을 미리 보여준 후, 정제 과정을 거쳐 고충실도 비디오를 얻습니다. 또한, 모델은 flow matching을 사용하여 역학을 비디오 잠재 공간에 직접 매핑하는 캐스케이드 메커니즘을 도입하고, 잠재 퇴화 메커니즘을 통해 접촉 세부 정보를 재생성합니다.

## 핵심 내용
### 방법 아키텍처
DVG-WM은 세계 모델을 두 개의 모듈로 분해합니다:
- **역학 학습 모듈**: 저수준 시계열 추론에 집중하여 물리적 상호작용의 중간 상태 시퀀스를 예측합니다.
- **시각 합성 모듈**: 고수준 의미론 기반의 시각 생성을 담당하며, 역학을 고해상도 비디오 프레임으로 매핑합니다.

### 캐스케이드 메커니즘
- **Flow Matching 매핑**: 역학 예측을 비디오 잠재 변수로 직접 변환하여 프레임별 생성으로 인한 계산 오버헤드를 피합니다.
- **잠재 퇴화 메커니즘**: 접촉이 풍부한 영역에서 잠재 변수를 능동적으로 퇴화시킨 후, 생성 모델을 통해 세부 정보를 재합성하여 충실도를 향상시킵니다.

### 실험 설정
- **벤치마크**: LIBERO 시뮬레이션 환경과 실제 로봇 플랫폼에서 평가를 수행합니다.
- **비교 방법**: 분리되지 않은 비디오 세계 모델과 비교하여 비디오 품질과 추론 속도를 측정합니다.

### 주요 결과
- **비디오 품질**: DVG-WM이 생성한 비디오는 충실도와 세부 정보 보존에서 기준 방법보다 크게 우수합니다.
- **추론 속도**: 기존 방법 대비 최대 3.97배 가속을 달성하여 분리 설계의 효율성을 검증합니다.
- **결론**: 분리된 비디오 생성은 로봇 조작을 위한 효율적인 구현형 세계 모델로 작동할 수 있으며, 역학 정밀도와 시각 품질을 모두 충족합니다.
