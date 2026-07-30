---
$id: ent_paper_physdiff_physics_guided_human_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
  zh: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
  ko: 'PhysDiff: Physics-Guided Human Motion Diffusion Model'
summary:
  en: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
  zh: PhysDiff 是一个由研究者提出的物理引导人体运动扩散模型，旨在解决现有运动扩散模型生成的运动存在物理不真实性问题（如漂浮、脚滑、地面穿透）。其核心贡献是通过物理模拟器中的运动模仿模块，在扩散过程中迭代地将去噪运动投影到物理合理空间，从而显著提升运动质量与物理合理性。
  ko: 'PhysDiff: Physics-Guided Human Motion Diffusion Model is a 2022 work on human motion analysis and synthesis for humanoid
    robots.'
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
- physdiff
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2212.02500v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PhysDiff: Physics-Guided Human Motion Diffusion Model (arXiv)'
  url: https://arxiv.org/abs/2212.02500
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'PhysDiff: Physics-Guided Human Motion Diffusion Model project page'
  url: https://nvlabs.github.io/PhysDiff/
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
现有运动扩散模型在生成多样化、真实人体运动方面潜力巨大，但常忽略物理规律，导致生成的运动出现漂浮、脚滑、地面穿透等明显伪影，严重影响质量并限制实际应用。PhysDiff 创新性地在扩散过程中引入物理约束，通过一个基于物理的运动投影模块，利用物理模拟器中的运动模仿技术，将每一步去噪后的运动投影为物理合理运动，并用于引导后续扩散步骤。这种迭代式物理约束方法能持续将运动拉向物理合理空间，效果远超简单的后处理。在大型人体运动数据集上的实验表明，PhysDiff 在运动质量上达到最优，并将所有数据集的物理合理性提升超过 78%。

## 核心内容
### 方法
- **核心问题**：现有运动扩散模型在生成过程中忽视物理定律，导致输出运动存在漂浮、脚滑、地面穿透等伪影，影响真实感与应用。
- **PhysDiff 架构**：提出物理引导运动扩散模型，在标准扩散过程中嵌入物理约束。
- **物理投影模块**：关键创新是使用物理模拟器中的运动模仿技术，将扩散步骤的去噪运动投影为物理合理运动。该投影运动被用于下一步扩散，引导去噪过程。
- **迭代优化**：通过迭代使用物理约束，模型持续将运动拉向物理合理空间，而非仅靠后处理修正。

### 实验设置
- **数据集**：在大型人体运动数据集上进行评估，涵盖多种运动类型。
- **评估指标**：关注运动质量与物理合理性，物理合理性通过特定指标量化（如漂浮、脚滑、地面穿透的减少程度）。

### 关键结果
- **物理合理性提升**：在所有数据集上，物理合理性提升超过 78%，显著减少伪影。
- **运动质量**：达到 state-of-the-art 水平，生成的运动在多样性与真实感上均优于现有方法。

### 结论
PhysDiff 通过将物理约束融入扩散过程，有效解决了运动生成中的物理不真实性问题，为人体运动分析与合成提供了更可靠、更实用的解决方案。

## Overview
Denoising diffusion models hold great promise for generating diverse and realistic human motions. However, existing motion diffusion models largely disregard the laws of physics in the diffusion process and often generate physically-implausible motions with pronounced artifacts such as floating, foot sliding, and ground penetration. This seriously impacts the quality of generated motions and limits their real-world application. To address this issue, we present a novel physics-guided motion diffusion model (PhysDiff), which incorporates physical constraints into the diffusion process. Specifically, we propose a physics-based motion projection module that uses motion imitation in a physics simulator to project the denoised motion of a diffusion step to a physically-plausible motion. The projected motion is further used in the next diffusion step to guide the denoising diffusion process. Intuitively, the use of physics in our model iteratively pulls the motion toward a physically-plausible space, which cannot be achieved by simple post-processing. Experiments on large-scale human motion datasets show that our approach achieves state-of-the-art motion quality and improves physical plausibility drastically (>78% for all datasets).

## 개요
Denoising diffusion 모델은 다양하고 사실적인 인간 동작을 생성하는 데 큰 잠재력을 가지고 있습니다. 그러나 기존의 동작 diffusion 모델은 확산 과정에서 물리 법칙을 대부분 무시하며, 종종 떠다니기, 발 미끄러짐, 지면 관통과 같은 두드러진 인공물이 있는 물리적으로 타당하지 않은 동작을 생성합니다. 이는 생성된 동작의 품질에 심각한 영향을 미치고 실제 응용을 제한합니다. 이 문제를 해결하기 위해, 우리는 확산 과정에 물리적 제약을 통합한 새로운 물리 유도 동작 diffusion 모델(PhysDiff)을 제시합니다. 구체적으로, 우리는 물리 시뮬레이터에서 동작 모방을 사용하여 확산 단계의 잡음 제거된 동작을 물리적으로 타당한 동작으로 투영하는 물리 기반 동작 투영 모듈을 제안합니다. 투영된 동작은 다음 확산 단계에서 잡음 제거 확산 과정을 안내하는 데 추가로 사용됩니다. 직관적으로, 우리 모델에서 물리 사용은 동작을 반복적으로 물리적으로 타당한 공간으로 끌어당기며, 이는 단순한 후처리로는 달성할 수 없습니다. 대규모 인간 동작 데이터셋에 대한 실험은 우리의 접근 방식이 최첨단 동작 품질을 달성하고 물리적 타당성을 크게 향상시킴을 보여줍니다(모든 데이터셋에서 >78%).

## 핵심 내용
Denoising diffusion 모델은 다양하고 사실적인 인간 동작을 생성하는 데 큰 잠재력을 가지고 있습니다. 그러나 기존의 동작 diffusion 모델은 확산 과정에서 물리 법칙을 대부분 무시하며, 종종 떠다니기, 발 미끄러짐, 지면 관통과 같은 두드러진 인공물이 있는 물리적으로 타당하지 않은 동작을 생성합니다. 이는 생성된 동작의 품질에 심각한 영향을 미치고 실제 응용을 제한합니다. 이 문제를 해결하기 위해, 우리는 확산 과정에 물리적 제약을 통합한 새로운 물리 유도 동작 diffusion 모델(PhysDiff)을 제시합니다. 구체적으로, 우리는 물리 시뮬레이터에서 동작 모방을 사용하여 확산 단계의 잡음 제거된 동작을 물리적으로 타당한 동작으로 투영하는 물리 기반 동작 투영 모듈을 제안합니다. 투영된 동작은 다음 확산 단계에서 잡음 제거 확산 과정을 안내하는 데 추가로 사용됩니다. 직관적으로, 우리 모델에서 물리 사용은 동작을 반복적으로 물리적으로 타당한 공간으로 끌어당기며, 이는 단순한 후처리로는 달성할 수 없습니다. 대규모 인간 동작 데이터셋에 대한 실험은 우리의 접근 방식이 최첨단 동작 품질을 달성하고 물리적 타당성을 크게 향상시킴을 보여줍니다(모든 데이터셋에서 >78%).

## 参考
- http://arxiv.org/abs/2212.02500v3
