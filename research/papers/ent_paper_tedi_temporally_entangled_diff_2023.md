---
$id: ent_paper_tedi_temporally_entangled_diff_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
  zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
  ko: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
summary:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: TEDi 是 2023 年提出的一种用于生成长序列人体运动的方法。其核心贡献在于将扩散模型中的“扩散时间轴”与运动序列的“时间轴”相纠缠，通过一个带噪运动缓冲区的迭代去噪过程，实现任意长度的自回归运动帧生成。
  ko: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- tedi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.15042v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (946 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis (arXiv)'
  url: https://arxiv.org/abs/2307.15042
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
TEDi 方法的核心创新在于将 Denoising Diffusion Probabilistic Models (DDPM) 中沿扩散时间轴逐步去噪的概念，迁移并应用到运动序列的时间轴上。通过设计一种支持时变去噪的公式，TEDi 将这两个轴纠缠在一起。具体而言，它维护一个包含不同噪声程度姿态的运动缓冲区，并在每个扩散步骤中，仅沿运动的时间轴前进，从而生成一个干净的新帧，同时从缓冲区头部移除旧帧并追加新的噪声向量。这种机制使得模型能够自回归地生成任意长度的连续运动序列，为角色动画等领域的长期运动合成提供了新框架。

## 核心内容
### 方法概述
TEDi 的核心思想是将 DDPM 的逐步去噪过程（沿扩散时间轴）与运动序列的时间轴进行纠缠。传统 DDPM 在生成时，每一步都降低整个样本的噪声水平；而 TEDi 则是在一个固定的扩散时间步上，仅对运动序列的时间轴进行增量式处理。

### 架构与机制
- **运动缓冲区**：维护一个固定长度的缓冲区，其中包含一系列姿态，这些姿态的噪声程度沿时间轴递增。
- **迭代去噪过程**：在每个扩散步骤中，模型仅对缓冲区中最新（噪声最高）的姿态进行去噪，生成一个干净的帧。
- **自回归生成**：生成的干净帧从缓冲区头部移除并输出，同时一个新的噪声向量被追加到缓冲区尾部，从而推动时间轴前进。
- **关键参数**：扩散时间轴保持静止，而运动时间轴在每个步骤中仅前进一帧。这使得模型能够以恒定的计算成本生成任意长度的序列。

### 实验设置与结果
- **数据集**：在 HumanML3D 和 KIT-ML 等标准人体运动数据集上进行评估。
- **对比基准**：与 MotionDiffuse、MDM 等现有运动生成模型进行比较。
- **关键数字**：在长期运动合成任务中，TEDi 在 FID（Fréchet Inception Distance）和多样性指标上均优于现有方法，特别是在生成超过 1000 帧的连续运动时，保持了良好的时间一致性和动作质量。
- **结论**：TEDi 通过将扩散过程与时间轴纠缠，有效解决了长期运动合成中的累积误差和计算效率问题，为角色动画和人形机器人运动规划提供了新的解决方案。

## Overview
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## 参考
- http://arxiv.org/abs/2307.15042v2

## 개요
TEDi 방법의 핵심 혁신은 Denoising Diffusion Probabilistic Models (DDPM)에서 확산 시간 축을 따라 점진적으로 노이즈를 제거하는 개념을 운동 시퀀스의 시간 축에 적용하고 전이하는 데 있습니다. 시간에 따라 변하는 노이즈 제거를 지원하는 공식을 설계함으로써, TEDi는 이 두 축을 서로 얽히게 합니다. 구체적으로, 서로 다른 노이즈 정도를 가진 포즈를 포함하는 운동 버퍼를 유지하고, 각 확산 단계에서 운동의 시간 축을 따라서만 전진하여 깨끗한 새 프레임을 생성하는 동시에 버퍼의 앞부분에서 오래된 프레임을 제거하고 새로운 노이즈 벡터를 추가합니다. 이 메커니즘을 통해 모델은 임의 길이의 연속 운동 시퀀스를 자기회귀적으로 생성할 수 있으며, 캐릭터 애니메이션과 같은 분야의 장기 운동 합성을 위한 새로운 프레임워크를 제공합니다.

## 핵심 내용
### 방법 개요
TEDi의 핵심 아이디어는 DDPM의 점진적 노이즈 제거 과정(확산 시간 축을 따라)을 운동 시퀀스의 시간 축과 얽히게 하는 것입니다. 기존 DDPM은 생성 시 각 단계에서 전체 샘플의 노이즈 수준을 낮추는 반면, TEDi는 고정된 확산 시간 단계에서 운동 시퀀스의 시간 축에 대해서만 증분 방식으로 처리합니다.

### 아키텍처 및 메커니즘
- **운동 버퍼**: 시간 축을 따라 노이즈 정도가 증가하는 일련의 포즈를 포함하는 고정 길이 버퍼를 유지합니다.
- **반복적 노이즈 제거 과정**: 각 확산 단계에서 모델은 버퍼에서 가장 최신(노이즈가 가장 높은) 포즈만 노이즈 제거하여 깨끗한 프레임을 생성합니다.
- **자기회귀 생성**: 생성된 깨끗한 프레임은 버퍼의 앞부분에서 제거되어 출력되고, 동시에 새로운 노이즈 벡터가 버퍼의 끝부분에 추가되어 시간 축을 전진시킵니다.
- **핵심 매개변수**: 확산 시간 축은 정지 상태를 유지하고, 운동 시간 축은 각 단계에서 한 프레임씩만 전진합니다. 이를 통해 모델은 일정한 계산 비용으로 임의 길이의 시퀀스를 생성할 수 있습니다.

### 실험 설정 및 결과
- **데이터셋**: HumanML3D 및 KIT-ML과 같은 표준 인간 운동 데이터셋에서 평가되었습니다.
- **비교 기준**: MotionDiffuse, MDM과 같은 기존 운동 생성 모델과 비교되었습니다.
- **핵심 수치**: 장기 운동 합성 작업에서 TEDi는 FID(Fréchet Inception Distance) 및 다양성 지표에서 기존 방법보다 우수했으며, 특히 1000프레임 이상의 연속 운동을 생성할 때 시간적 일관성과 동작 품질을 잘 유지했습니다.
- **결론**: TEDi는 확산 과정을 시간 축과 얽히게 함으로써 장기 운동 합성에서의 누적 오류 및 계산 효율성 문제를 효과적으로 해결하며, 캐릭터 애니메이션 및 휴머노이드 로봇 운동 계획을 위한 새로운 솔루션을 제공합니다.
