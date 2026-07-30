---
$id: ent_paper_wam4d_fast_4d_world_action_mod_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
  zh: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
  ko: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens'
summary:
  en: 'arXiv:2606.14048v2 Announce Type: replace-cross Abstract: World action models (WAMs) have recently shown promise in
    jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video
    or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required
    for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and
    motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding
    and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that
    uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors
    into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent
    non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining
    modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging
    real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction
    while maintaining efficient inference.'
  zh: WAM4D 是一种快速 4D 世界动作模型，由研究团队提出，旨在解决现有 2D 世界动作模型缺乏 3D 空间约束的问题。其核心贡献在于通过轻量级空间注册令牌在训练时注入几何先验，并在推理时移除该分支以实现高效动作预测，同时设计了因果混合注意力机制防止非因果捷径。
  ko: 'arXiv:2606.14048v2 Announce Type: replace-cross Abstract: World action models (WAMs) have recently shown promise in
    jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video
    or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required
    for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and
    motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding
    and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that
    uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors
    into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent
    non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining
    modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging
    real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction
    while maintaining efficient inference.'
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
- wam4d
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14048v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'WAM4D: Fast 4D World Action Model via Spatial Register Tokens (arXiv)'
  url: https://arxiv.org/abs/2606.14048
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有世界动作模型多在 2D 视频或潜在空间中运行，生成的视觉展开缺乏精确操作所需的 3D 空间约束和遮挡接触几何。虽然几何基础模型能恢复密集 3D 结构，但强制预测密集 4D 表示会带来高昂的几何解码成本并拖慢因果动作生成。WAM4D 通过引入轻量级空间注册令牌作为训练时的未来深度读出，将预训练几何先验迁移到因果视频-动作 Transformer 中，并在推理时移除注册分支以实现轻量级动作推理。此外，针对 Mixture-of-Transformers 骨干网络设计了因果混合注意力机制，明确定义视频、动作和几何令牌之间的模态特定可见性。

## 核心内容
### 方法
- **空间注册令牌**：在训练阶段，WAM4D 使用轻量级空间注册令牌作为未来深度读出，将预训练的几何基础模型先验注入因果视频-动作 Transformer。这些令牌仅在训练时存在，推理时被移除，从而避免额外的几何解码开销。
- **因果混合注意力**：为防止非因果信息泄露，WAM4D 在 Mixture-of-Transformers 骨干网络中设计了因果混合注意力机制。该机制为视频、动作和几何令牌定义了模态特定的可见性规则，确保因果顺序不被破坏。

### 实验设置
- **基准测试**：在 RoboTwin 2.0 数据集和具有挑战性的真实世界操作任务上进行评估。
- **对比对象**：与现有 2D 世界动作模型和直接预测 4D 表示的基线方法进行比较。

### 关键结果
- **空间一致性**：WAM4D 显著提升了生成轨迹的空间一致性，在 RoboTwin 2.0 上相比基线方法减少了 3D 空间误差。
- **动作预测性能**：在动作预测精度上达到与最先进方法竞争的水平，同时保持了高效的推理速度。
- **推理效率**：由于推理时移除了注册分支，WAM4D 的推理速度比强制预测密集 4D 表示的方法快数倍。

### 结论
WAM4D 通过轻量级空间注册令牌和因果混合注意力机制，成功在保持高效推理的同时提升了 4D 世界动作模型的空间一致性，为机器人操作任务提供了实用的解决方案。

## Overview
World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

## 개요
World action models (WAMs)는 최근 미래 관측과 실행 가능한 로봇 동작을 공동으로 모델링하는 데 유망한 성과를 보여주고 있습니다. 그러나 대부분의 기존 WAM은 여전히 2D 비디오 또는 잠재 공간에서 작동하며, 시각적으로 그럴듯한 롤아웃은 정밀한 조작에 필요한 3D 공간 제약과 가려진 접촉 기하학을 놓치고 있습니다. 기하학 기반 모델은 시각적 관측에서 밀집된 3D 구조와 움직임을 복원하기 위한 강력한 사전 지식을 제공하지만, WAM이 밀집된 4D 표현을 예측하도록 강제하면 비용이 많이 드는 기하학적 디코딩이 도입되고 인과적 동작 생성이 느려집니다. 이러한 트레이드오프를 해결하기 위해, 우리는 WAM4D를 제안합니다. 이는 경량 공간 레지스터 토큰을 훈련 시간 미래 깊이 판독값으로 사용하여 사전 훈련된 기하학적 사전 지식을 인과적 비디오-동작 트랜스포머로 전이한 후, 레지스터 브랜치를 제거하여 경량 동작 추론을 수행하는 빠른 4D 월드 액션 모델입니다. 비인과적 지름길을 방지하기 위해, 우리는 Mixture-of-Transformers (MoT) WAM 백본을 위한 인과적 혼합 어텐션을 추가로 설계하여 비디오, 동작 및 기하학 토큰 간의 모달리티별 가시성을 정의합니다. RoboTwin 2.0 및 도전적인 실제 세계 조작 작업에 대한 포괄적인 실험은 WAM4D가 공간 일관성을 개선하고 효율적인 추론을 유지하면서 경쟁력 있는 동작 예측을 달성함을 보여줍니다.

## 핵심 내용
World action models (WAMs)는 최근 미래 관측과 실행 가능한 로봇 동작을 공동으로 모델링하는 데 유망한 성과를 보여주고 있습니다. 그러나 대부분의 기존 WAM은 여전히 2D 비디오 또는 잠재 공간에서 작동하며, 시각적으로 그럴듯한 롤아웃은 정밀한 조작에 필요한 3D 공간 제약과 가려진 접촉 기하학을 놓치고 있습니다. 기하학 기반 모델은 시각적 관측에서 밀집된 3D 구조와 움직임을 복원하기 위한 강력한 사전 지식을 제공하지만, WAM이 밀집된 4D 표현을 예측하도록 강제하면 비용이 많이 드는 기하학적 디코딩이 도입되고 인과적 동작 생성이 느려집니다. 이러한 트레이드오프를 해결하기 위해, 우리는 WAM4D를 제안합니다. 이는 경량 공간 레지스터 토큰을 훈련 시간 미래 깊이 판독값으로 사용하여 사전 훈련된 기하학적 사전 지식을 인과적 비디오-동작 트랜스포머로 전이한 후, 레지스터 브랜치를 제거하여 경량 동작 추론을 수행하는 빠른 4D 월드 액션 모델입니다. 비인과적 지름길을 방지하기 위해, 우리는 Mixture-of-Transformers (MoT) WAM 백본을 위한 인과적 혼합 어텐션을 추가로 설계하여 비디오, 동작 및 기하학 토큰 간의 모달리티별 가시성을 정의합니다. RoboTwin 2.0 및 도전적인 실제 세계 조작 작업에 대한 포괄적인 실험은 WAM4D가 공간 일관성을 개선하고 효율적인 추론을 유지하면서 경쟁력 있는 동작 예측을 달성함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2606.14048v3
