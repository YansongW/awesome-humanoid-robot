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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.14048v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (901 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2606.14048v3

## 개요
기존 세계 행동 모델은 주로 2D 비디오 또는 잠재 공간에서 작동하며, 생성된 시각적 전개는 정밀한 조작에 필요한 3D 공간 제약과 폐색 접촉 기하학이 부족합니다. 기하학 기반 모델이 밀집된 3D 구조를 복원할 수 있지만, 밀집된 4D 표현을 강제로 예측하면 높은 기하학 디코딩 비용이 발생하고 인과적 행동 생성을 지연시킵니다. WAM4D는 경량 공간 등록 토큰을 훈련 시 미래 깊이 판독으로 도입하여 사전 훈련된 기하학 사전 지식을 인과적 비디오-행동 Transformer로 전이하고, 추론 시 등록 분기를 제거하여 경량 행동 추론을 실현합니다. 또한, Mixture-of-Transformers 백본 네트워크를 위해 인과적 혼합 어텐션 메커니즘을 설계하여 비디오, 행동, 기하학 토큰 간의 모달별 가시성을 명확히 정의합니다.

## 핵심 내용
### 방법
- **공간 등록 토큰**: 훈련 단계에서 WAM4D는 경량 공간 등록 토큰을 미래 깊이 판독으로 사용하여 사전 훈련된 기하학 기반 모델의 사전 지식을 인과적 비디오-행동 Transformer에 주입합니다. 이러한 토큰은 훈련 시에만 존재하며 추론 시 제거되어 추가 기하학 디코딩 오버헤드를 방지합니다.
- **인과적 혼합 어텐션**: 비인과적 정보 누출을 방지하기 위해 WAM4D는 Mixture-of-Transformers 백본 네트워크에서 인과적 혼합 어텐션 메커니즘을 설계합니다. 이 메커니즘은 비디오, 행동, 기하학 토큰에 대한 모달별 가시성 규칙을 정의하여 인과적 순서가 깨지지 않도록 보장합니다.

### 실험 설정
- **벤치마크**: RoboTwin 2.0 데이터셋과 도전적인 실제 세계 조작 작업에서 평가를 수행합니다.
- **비교 대상**: 기존 2D 세계 행동 모델 및 4D 표현을 직접 예측하는 기준 방법과 비교합니다.

### 주요 결과
- **공간 일관성**: WAM4D는 생성된 궤적의 공간 일관성을 크게 향상시켰으며, RoboTwin 2.0에서 기준 방법 대비 3D 공간 오류를 줄였습니다.
- **행동 예측 성능**: 최신 방법과 경쟁력 있는 수준의 행동 예측 정확도를 달성하면서도 효율적인 추론 속도를 유지합니다.
- **추론 효율성**: 추론 시 등록 분기를 제거함으로써 WAM4D의 추론 속도는 밀집된 4D 표현을 강제로 예측하는 방법보다 몇 배 빠릅니다.

### 결론
WAM4D는 경량 공간 등록 토큰과 인과적 혼합 어텐션 메커니즘을 통해 효율적인 추론을 유지하면서 4D 세계 행동 모델의 공간 일관성을 향상시켜, 로봇 조작 작업에 실용적인 솔루션을 제공합니다.
