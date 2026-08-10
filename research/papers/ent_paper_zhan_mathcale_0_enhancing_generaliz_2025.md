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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21542v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1008 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.21542v2

## 개요
기존 비전-언어-행동 모델은 과제, 장면, 카메라 시점 간 일반화에 한계가 있으며, 종종 거칠거나 불안정한 행동을 생성한다. E0는 행동 분포의 다중 모드 특성, 사전 훈련된 VLM/VLA 백본의 토큰 기호 추론, 그리고 실제 로봇 제어에 효과적인 유한 해상도를 분석하여 tweedie 이산 확산 기반 프레임워크를 제안한다. 이 프레임워크는 양자화된 행동 토큰 공간에서 반복적 잡음 제거를 수행하며, 토큰 추론과 자연스럽게 정렬되어 세밀하고 실행 가능한 행동 제어를 지원하고, 마스크 이산 확산의 분포 불일치 문제를 피한다. 또한, E0는 구형 시점 섭동 증강 기법을 도입하여 추가 데이터 없이 카메라 변위에 대한 강건성을 향상시킨다.

## 핵심 내용
### 방법 아키텍처
E0의 핵심은 tweedie 이산 확산 프레임워크로, 행동 생성을 양자화된 행동 토큰에 대한 반복적 잡음 제거 과정으로 모델링한다. 구체적으로:
- **행동 토큰화**: 연속 행동 공간을 유한한 수의 토큰으로 이산화하며, 각 토큰은 행동 원시 요소에 해당한다.
- **확산 과정**: tweedie 분포를 잡음 모델로 사용하여 이산 토큰 공간에서 전방 잡음 추가 및 역방향 잡음 제거를 수행한다. 이 설계는 전통적인 마스크 이산 확산에서 분포 불일치로 인한 성능 저하를 피한다.
- **토큰 추론 정렬**: 이산 연산은 사전 훈련된 VLM/VLA 백본의 기호 추론 메커니즘에 자연스럽게 적합하여, 모델이 언어 및 시각 특징을 활용해 행동 생성을 안내할 수 있게 한다.

### 핵심 혁신
- **구형 시점 섭동 증강**: 훈련 중 카메라 시점에 구면 무작위 섭동을 적용하여 실제 장면의 시점 변화를 모의하고, 추가 데이터 수집 없이 카메라 변위에 대한 모델 강건성을 향상시킨다.
- **세밀한 제어**: 잡음 제거 단계 수 또는 잡음 수준을 조정하여 행동의 정밀도를 유연하게 제어할 수 있으며, 거친 수준에서 세밀한 수준까지의 행동 생성을 지원한다.

### 실험 설정 및 결과
- **벤치마크**: LIBERO, VLABench, ManiSkill 세 가지 시뮬레이션 벤치마크와 실제 Franka 로봇 팔 플랫폼에서 평가하며, 14개의 서로 다른 환경을 포함한다.
- **비교 기준선**: RT-2, Octo, Diffusion Policy 등 강력한 기준선과 비교한다.
- **성능 향상**: E0는 모든 환경에서 평균 성능이 10.7% 향상되었으며, 특히 교차 장면 일반화(예: LIBERO의 10개 과제) 및 시점 변화(VLABench의 4개 시점)에서 두드러진 성과를 보인다.
- **절제 실험**: 구형 시점 섭동 증강을 제거하면 성능이 8.3% 하락하고, 마스크 이산 확산으로 대체하면 성능이 12.1% 하락하여 각 모듈의 유효성을 검증한다.

### 결론
E0는 이산 확산 프레임워크와 시점 증강 기술을 통해 VLA 모델의 일반화 및 세밀한 제어의 병목을 효과적으로 해결하며, 로봇 조작을 위한 고성능의 강건한 솔루션을 제공한다.
