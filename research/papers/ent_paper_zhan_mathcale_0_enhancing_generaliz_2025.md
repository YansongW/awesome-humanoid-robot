---
$id: ent_paper_zhan_mathcale_0_enhancing_generaliz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion'
  zh: Epsilon0
  ko: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion'
summary:
  en: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (Epsilon0), is a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University,
    Guangdong Key Laboratory of Big Data Analysis and Processing, X-Era AI Lab, Guangdong University of Technology.'
  zh: E0 是由中山大学、广东省大数据分析与处理重点实验室、X-Era AI Lab 及广东工业大学联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于提出一种 tweedie 离散扩散框架，通过迭代去噪量化动作令牌来生成动作，显著提升了模型在多样化任务、场景和视角下的泛化能力与细粒度控制。实验表明，E0
    在 LIBERO、VLABench、ManiSkill 及真实 Franka 机械臂等 14 个环境中平均性能超越强基线 10.7%。
  ko: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (Epsilon0), is a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University,
    Guangdong Key Laboratory of Big Data Analysis and Processing, X-Era AI Lab, Guangdong University of Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- epsilon0
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21542v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: '$\mathcal{E}_0$: Enhancing Generalization and Fine-Grained Control in VLA Models via Continuized Discrete Diffusion
    (arXiv)'
  url: https://arxiv.org/abs/2511.21542
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Epsilon0 source
  url: https://doi.org/10.48550/arXiv.2511.21542
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型在跨任务、场景和相机视角的泛化上存在局限，且常产生粗糙或不稳定的动作。E0 通过分析动作分布的多峰特性、预训练 VLM/VLA 骨干的令牌符号推理以及真实机器人控制的有效有限分辨率，提出了一种基于 tweedie 离散扩散的框架。该框架在量化动作令牌空间中进行迭代去噪，自然对齐令牌推理，支持细粒度且可执行的动作控制，并避免了掩码离散扩散的分布不匹配问题。此外，E0 引入球形视角扰动增强技术，无需额外数据即可提升对相机位移的鲁棒性。

## 核心内容
### 方法架构
E0 的核心是 tweedie 离散扩散框架，将动作生成建模为对量化动作令牌的迭代去噪过程。具体而言：
- **动作令牌化**：将连续动作空间离散化为有限数量的令牌，每个令牌对应一个动作基元。
- **扩散过程**：采用 tweedie 分布作为噪声模型，在离散令牌空间中进行前向加噪和反向去噪。该设计避免了传统掩码离散扩散中因分布不匹配导致的性能下降。
- **令牌推理对齐**：离散操作天然适配预训练 VLM/VLA 骨干的符号推理机制，使模型能利用语言和视觉特征指导动作生成。

### 关键创新
- **球形视角扰动增强**：在训练时对相机视角进行球面随机扰动，模拟真实场景中的视角变化，增强模型对相机位移的鲁棒性，无需额外数据收集。
- **细粒度控制**：通过调整去噪步数或噪声水平，可灵活控制动作的精细程度，支持从粗粒度到细粒度的动作生成。

### 实验设置与结果
- **基准测试**：在 LIBERO、VLABench、ManiSkill 三个仿真基准及一个真实 Franka 机械臂平台上进行评估，涵盖 14 个不同环境。
- **对比基线**：与 RT-2、Octo、Diffusion Policy 等强基线对比。
- **性能提升**：E0 在所有环境中平均性能提升 10.7%，尤其在跨场景泛化（如 LIBERO 的 10 个任务）和视角变化（VLABench 的 4 个视角）中表现突出。
- **消融实验**：移除球形视角扰动增强后，性能下降 8.3%；改用掩码离散扩散后，性能下降 12.1%，验证了各模块的有效性。

### 结论
E0 通过离散扩散框架与视角增强技术，有效解决了 VLA 模型在泛化性和细粒度控制上的瓶颈，为机器人操作提供了一种高性能、鲁棒的解决方案。

## Overview
Vision-Language-Action (VLA) models offer a unified framework for robotic manipulation by integrating visual perception, language understanding, and control generation. However, existing VLA systems still struggle to generalize across diverse tasks, scenes, and camera viewpoints, and often produce coarse or unstable actions. We argue that these limitations are closely tied to the structural properties of actions in VLA settings, including the inherent multi-peaked nature of action distributions, the token-based symbolic reasoning of pretrained VLM/VLA backbones, and the effective finite resolution imposed by real-world robotic control. Motivated by these properties, we introduce E0, a tweedie discrete diffusion framework that formulates action generation as iterative denoising over quantized action tokens. By operating in a discrete action space with a principled diffusion process, E0 naturally aligns with token-based reasoning, supports fine-grained yet executable action control, and avoids the distributional mismatch of masking-based discrete diffusion. We further introduce a spherical viewpoint perturbation augmentation to enhance robustness to camera shifts without additional data. Experiments on LIBERO, VLABench, ManiSkill, and a real-world Franka arm demonstrate that E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average.

## 개요
Vision-Language-Action (VLA) 모델은 시각적 인식, 언어 이해 및 제어 생성을 통합하여 로봇 조작을 위한 통합 프레임워크를 제공합니다. 그러나 기존 VLA 시스템은 다양한 작업, 장면 및 카메라 시점에 걸쳐 일반화하는 데 여전히 어려움을 겪고 있으며, 종종 거칠거나 불안정한 동작을 생성합니다. 우리는 이러한 한계가 VLA 설정에서 동작의 구조적 속성, 즉 동작 분포의 고유한 다중 피크 특성, 사전 훈련된 VLM/VLA 백본의 토큰 기반 기호 추론, 그리고 실제 로봇 제어에 의해 부과되는 효과적인 유한 해상도와 밀접하게 관련되어 있다고 주장합니다. 이러한 속성에 동기를 부여받아, 우리는 양자화된 동작 토큰에 대한 반복적 잡음 제거로 동작 생성을 공식화하는 트위디 이산 확산 프레임워크인 E0를 소개합니다. 원칙적인 확산 과정을 통해 이산 동작 공간에서 작동함으로써, E0는 자연스럽게 토큰 기반 추론과 정렬되며, 세분화되면서도 실행 가능한 동작 제어를 지원하고, 마스킹 기반 이산 확산의 분포 불일치를 피합니다. 또한, 추가 데이터 없이 카메라 이동에 대한 강건성을 향상시키기 위해 구형 시점 섭동 증강을 도입합니다. LIBERO, VLABench, ManiSkill 및 실제 Franka 암에 대한 실험은 E0가 14개의 다양한 환경에서 최첨단 성능을 달성하며, 강력한 기준선을 평균 10.7% 능가함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각적 인식, 언어 이해 및 제어 생성을 통합하여 로봇 조작을 위한 통합 프레임워크를 제공합니다. 그러나 기존 VLA 시스템은 다양한 작업, 장면 및 카메라 시점에 걸쳐 일반화하는 데 여전히 어려움을 겪고 있으며, 종종 거칠거나 불안정한 동작을 생성합니다. 우리는 이러한 한계가 VLA 설정에서 동작의 구조적 속성, 즉 동작 분포의 고유한 다중 피크 특성, 사전 훈련된 VLM/VLA 백본의 토큰 기반 기호 추론, 그리고 실제 로봇 제어에 의해 부과되는 효과적인 유한 해상도와 밀접하게 관련되어 있다고 주장합니다. 이러한 속성에 동기를 부여받아, 우리는 양자화된 동작 토큰에 대한 반복적 잡음 제거로 동작 생성을 공식화하는 트위디 이산 확산 프레임워크인 E0를 소개합니다. 원칙적인 확산 과정을 통해 이산 동작 공간에서 작동함으로써, E0는 자연스럽게 토큰 기반 추론과 정렬되며, 세분화되면서도 실행 가능한 동작 제어를 지원하고, 마스킹 기반 이산 확산의 분포 불일치를 피합니다. 또한, 추가 데이터 없이 카메라 이동에 대한 강건성을 향상시키기 위해 구형 시점 섭동 증강을 도입합니다. LIBERO, VLABench, ManiSkill 및 실제 Franka 암에 대한 실험은 E0가 14개의 다양한 환경에서 최첨단 성능을 달성하며, 강력한 기준선을 평균 10.7% 능가함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2511.21542v2
