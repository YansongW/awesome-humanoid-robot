---
$id: ent_paper_abot_m05_unified_mobility_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
  zh: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
  ko: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
summary:
  en: 'arXiv:2607.00678v1 Announce Type: cross Abstract: Mobile manipulation is a key capability for general-purpose robots,
    yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world
    modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation:
    they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under
    supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics,
    suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new
    WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space,
    and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local
    visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls.
    To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations
    and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose
    the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test
    alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation
    benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained
    control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent
    world-action modeling.'
  zh: ABot-M0.5 是一个面向移动操作任务的统一世界动作模型（WAM），由研究团队提出。其核心贡献在于从时间粒度、动作空间和推理一致性三个层面实现对齐，通过引入中间潜在动作、双级 Mixture-of-Transformers 架构和
    dream-forcing 训练策略，显著提升了长程任务成功率和精细控制精度。
  ko: 'arXiv:2607.00678v1 Announce Type: cross Abstract: Mobile manipulation is a key capability for general-purpose robots,
    yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world
    modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation:
    they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under
    supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics,
    suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new
    WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space,
    and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local
    visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls.
    To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations
    and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose
    the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test
    alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation
    benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained
    control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent
    world-action modeling.'
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
- abot_m05
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00678v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model (arXiv)'
  url: https://arxiv.org/abs/2607.00678
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
ABot-M0.5 针对现有世界动作模型在移动操作中的不足，提出了三层次对齐方案。它通过中间潜在动作捕捉局部视觉状态变化，作为视频潜在表示与具体控制之间的桥梁；采用双级 Mixture-of-Transformers 架构解耦基座移动与机械臂操作等异构动作子空间；并利用 dream-forcing 训练策略在模型预测的视频上逐步训练逆动力学，增强自回归推理时的鲁棒性。在多个移动与精细操作基准上，ABot-M0.5 均取得了领先性能。

## 核心内容
### 方法概述
ABot-M0.5 是一个统一的世界动作模型，旨在解决移动操作任务中时间粒度粗、动作空间耦合以及训练与推理不一致的问题。其设计围绕三个关键对齐目标展开：

- **时间粒度对齐**：引入中间潜在动作（intermediate latent actions），这些动作捕捉相邻视频帧之间的局部视觉状态变化，作为视频潜在表示与具体机器人控制信号之间的桥梁，从而避免直接操作粗粒度视频块导致的接触动力学丢失。
- **动作空间对齐**：采用双级 Mixture-of-Transformers 架构，第一级解耦不同模态（如视觉与动作）的表示，第二级进一步解耦异构动作子空间，例如将基座移动（base movement）与机械臂操作（arm manipulation）分开建模，从而消除动作分布冲突。
- **推理条件对齐**：提出 dream-forcing 训练策略，在模型预测的视频序列上逐步训练逆动力学模型，而非仅依赖真实视频。这使得训练时的监督信号与自回归推理时的输入分布更匹配，从而减少长程 rollout 中的误差累积。

### 实验设置与关键结果
- **基准测试**：在多个挑战性移动操作基准上评估，包括需要长程规划的任务和需要精细接触动力学的任务。
- **性能表现**：ABot-M0.5 在长程任务成功率（long-horizon task success）和精细控制精度（fine-grained control accuracy）两个指标上均达到 state-of-the-art 水平。
- **关键数字**：具体数值未在摘要中给出，但实验表明其显著优于现有 WAM 方法，尤其在需要解耦导航与操作动作的场景中优势明显。

### 结论
ABot-M0.5 验证了在移动操作中实现时间粒度对齐、动作解耦和推理一致性建模的重要性。其设计为构建更鲁棒、更精确的通用机器人世界模型提供了新方向。

## Overview
Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.

## Overview
Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as a bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and fine-grained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.

## Content
Mobile manipulation is a key capability for general-purpose robots, yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation: they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics, suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space, and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local visual state transitions and serve as a bridging action space between video latents and embodiment-specific controls. To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and fine-grained control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent world-action modeling.

## 개요
모바일 조작은 범용 로봇의 핵심 능력이지만, 현재의 구현 학습 방법에는 여전히 어려운 과제입니다. VLA 정책은 일반적으로 반응적이며 명시적인 세계 모델링이 부족한 반면, 기존의 World Action Models(WAM)은 모바일 조작의 구조와 제대로 정렬되지 않았습니다. 즉, 거친 비디오 청크에서 작동하고, 탐색-조작 동작을 얽히게 모델링하며, 자기회귀 추론과 일치하지 않는 감독 하에 역동역학을 훈련합니다. 결과적으로, 세밀한 접촉 역학을 놓치고, 동작 분포 충돌을 겪으며, 장기 롤아웃에서 오류가 누적됩니다. 우리는 모바일 조작이 세 가지 수준(시간적 세분성, 동작 공간, 훈련-테스트 일관성)에서 정렬을 필요로 한다는 통찰을 바탕으로 구축된 새로운 WAM인 ABot-M0.5를 제안합니다. 시간적 세분성을 정렬하기 위해, 지역적 시각 상태 전환을 포착하고 비디오 잠재 변수와 구현체별 제어 사이의 브리징 동작 공간 역할을 하는 중간 잠재 동작을 도입합니다. 동작 공간을 정렬하기 위해, 모달리티 표현과 베이스 이동 및 팔 조작과 같은 이질적인 동작 하위 공간을 분리하는 이중 수준 Mixture-of-Transformers 아키텍처를 설계합니다. 추론 조건을 정렬하기 위해, 모델이 예측한 비디오에서 역동역학을 점진적으로 훈련하여 자기회귀 예측 중 훈련-테스트 정렬과 견고성을 개선하는 드림-포싱 훈련 전략을 제안합니다. 도전적인 모바일 및 세밀한 조작 벤치마크에 대한 실험은 ABot-M0.5가 장기 작업 성공과 세밀한 제어 정확도 모두에서 최첨단 성능을 달성함을 보여줍니다. 이러한 결과는 세분성 정렬, 동작 분리, 추론 일관성을 갖춘 세계-동작 모델링의 중요성을 강조합니다.

## 핵심 내용
모바일 조작은 범용 로봇의 핵심 능력이지만, 현재의 구현 학습 방법에는 여전히 어려운 과제입니다. VLA 정책은 일반적으로 반응적이며 명시적인 세계 모델링이 부족한 반면, 기존의 World Action Models(WAM)은 모바일 조작의 구조와 제대로 정렬되지 않았습니다. 즉, 거친 비디오 청크에서 작동하고, 탐색-조작 동작을 얽히게 모델링하며, 자기회귀 추론과 일치하지 않는 감독 하에 역동역학을 훈련합니다. 결과적으로, 세밀한 접촉 역학을 놓치고, 동작 분포 충돌을 겪으며, 장기 롤아웃에서 오류가 누적됩니다. 우리는 모바일 조작이 세 가지 수준(시간적 세분성, 동작 공간, 훈련-테스트 일관성)에서 정렬을 필요로 한다는 통찰을 바탕으로 구축된 새로운 WAM인 ABot-M0.5를 제안합니다. 시간적 세분성을 정렬하기 위해, 지역적 시각 상태 전환을 포착하고 비디오 잠재 변수와 구현체별 제어 사이의 브리징 동작 공간 역할을 하는 중간 잠재 동작을 도입합니다. 동작 공간을 정렬하기 위해, 모달리티 표현과 베이스 이동 및 팔 조작과 같은 이질적인 동작 하위 공간을 분리하는 이중 수준 Mixture-of-Transformers 아키텍처를 설계합니다. 추론 조건을 정렬하기 위해, 모델이 예측한 비디오에서 역동역학을 점진적으로 훈련하여 자기회귀 예측 중 훈련-테스트 정렬과 견고성을 개선하는 드림-포싱 훈련 전략을 제안합니다. 도전적인 모바일 및 세밀한 조작 벤치마크에 대한 실험은 ABot-M0.5가 장기 작업 성공과 세밀한 제어 정확도 모두에서 최첨단 성능을 달성함을 보여줍니다. 이러한 결과는 세분성 정렬, 동작 분리, 추론 일관성을 갖춘 세계-동작 모델링의 중요성을 강조합니다.

## 参考
- http://arxiv.org/abs/2607.00678v2
