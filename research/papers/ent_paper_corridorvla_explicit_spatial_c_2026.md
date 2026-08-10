---
$id: ent_paper_corridorvla_explicit_spatial_c_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors'
  zh: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors'
  ko: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors'
summary:
  en: 'arXiv:2604.21241v2 Announce Type: replace Abstract: Vision--Language--Action (VLA) models often use intermediate representations
    to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent
    features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector
    $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation.
    The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution
    falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency
    objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and
    7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy
    4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21%
    success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints
    for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model
    checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.'
  zh: CorridorVLA 是一种通过预测稀疏空间锚点（如末端执行器的 Δ-位置）来为动作生成施加显式容差约束的 VLA 模型。该方法在训练目标中定义了一个“容差走廊”，引导流匹配动作头：偏离走廊的轨迹收到修正梯度，而走廊内的轨迹则通过一致性目标进行细化。在
    LIBERO 和 LIBERO-Plus 基准上，CorridorVLA 分别将 SmolVLA 提升了 4.45 和 12.37 个百分点，并将 GR00T 提升了 7.98 个百分点，在单策略 4-in-1 设置下 GR00T-Corr
    达到 83.21% 的成功率。
  ko: 'arXiv:2604.21241v2 Announce Type: replace Abstract: Vision--Language--Action (VLA) models often use intermediate representations
    to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent
    features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector
    $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation.
    The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution
    falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency
    objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and
    7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy
    4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21%
    success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints
    for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model
    checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.'
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
- corridorvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21241v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (896 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors (arXiv)'
  url: https://arxiv.org/abs/2604.21241
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
CorridorVLA 的核心创新在于将空间引导从隐式潜在特征中显式化，通过预测稀疏空间锚点来定义物理变化的容差走廊。这些锚点作为增量物理变化（如末端执行器的 Δ-位置），在训练目标中施加显式约束：对于流匹配动作头生成的轨迹，若其空间演化超出走廊则施加修正梯度，若在走廊内则通过一致性目标进行细化。实验表明，该方法在 LIBERO 基准上提升 SmolVLA 4.45 个百分点，在更具挑战性的 LIBERO-Plus 基准上分别提升 SmolVLA 和 GR00T 12.37 和 7.98 个百分点。在单策略 4-in-1 联合训练与评估设置下，GR00T-Corr 达到 83.21% 的成功率，验证了动作对齐的物理线索能为生成式动作策略提供直接且可解释的约束。

## 核心内容
### 方法概述
CorridorVLA 通过预测稀疏空间锚点来显式定义动作生成的物理约束。这些锚点代表增量物理变化（如末端执行器的 Δ-位置），并在训练目标中构建一个“容差走廊”。流匹配动作头生成的轨迹会与走廊进行比较：
- 若轨迹的空间演化超出走廊，则施加修正梯度以将其拉回约束范围。
- 若轨迹在走廊内，则通过一致性目标进行细化，保持动作的平滑与合理。

### 实验设置与关键数字
- **基准测试**：在 LIBERO 和更具挑战性的 LIBERO-Plus 基准上进行评估。
- **性能提升**：
  - 在 LIBERO 上，CorridorVLA 将 SmolVLA 提升 4.45 个百分点。
  - 在 LIBERO-Plus 上，CorridorVLA 将 SmolVLA 提升 12.37 个百分点，将 GR00T 提升 7.98 个百分点。
- **单策略 4-in-1 设置**：在联合训练与评估所有任务套件的设置下，GR00T-Corr 达到 83.21% 的成功率。

### 结论
实验结果表明，动作对齐的物理线索（如稀疏空间锚点定义的容差走廊）能够为生成式动作策略提供直接且可解释的约束，有效补充了视觉或隐式特征中编码的空间引导。代码和模型检查点已开源。

## Overview
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $Δ$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## Overview
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## Content
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## 参考
- http://arxiv.org/abs/2604.21241v2

## 개요
CorridorVLA의 핵심 혁신은 공간 안내를 암시적 잠재 특징에서 명시적으로 전환하여, 희소 공간 앵커를 예측함으로써 물리적 변화의 허용 회랑(tolerance corridor)을 정의하는 데 있습니다. 이러한 앵커는 증분 물리적 변화(예: 엔드 이펙터의 Δ-위치)로 작용하며, 훈련 목표에 명시적 제약을 부과합니다: 플로우 매칭 액션 헤드가 생성한 궤적의 공간적 진화가 회랑을 벗어나면 수정 기울기를 적용하고, 회랑 내에 있으면 일관성 목표를 통해 세밀화합니다. 실험 결과, 이 방법은 LIBERO 벤치마크에서 SmolVLA를 4.45퍼센트 포인트 향상시키고, 더 도전적인 LIBERO-Plus 벤치마크에서 SmolVLA와 GR00T를 각각 12.37 및 7.98퍼센트 포인트 향상시킵니다. 단일 정책 4-in-1 공동 훈련 및 평가 설정에서 GR00T-Corr는 83.21%의 성공률을 달성하여, 동작 정렬 물리적 단서가 생성적 동작 정책에 직접적이고 해석 가능한 제약을 제공할 수 있음을 검증합니다.

## 핵심 내용
### 방법 개요
CorridorVLA는 희소 공간 앵커를 예측하여 동작 생성의 물리적 제약을 명시적으로 정의합니다. 이러한 앵커는 증분 물리적 변화(예: 엔드 이펙터의 Δ-위치)를 나타내며, 훈련 목표에 "허용 회랑"을 구축합니다. 플로우 매칭 액션 헤드가 생성한 궤적은 회랑과 비교됩니다:
- 궤적의 공간적 진화가 회랑을 벗어나면, 이를 제약 범위로 끌어오기 위해 수정 기울기가 적용됩니다.
- 궤적이 회랑 내에 있으면, 일관성 목표를 통해 세밀화되어 동작의 매끄러움과 합리성을 유지합니다.

### 실험 설정 및 주요 수치
- **벤치마크 테스트**: LIBERO 및 더 도전적인 LIBERO-Plus 벤치마크에서 평가되었습니다.
- **성능 향상**:
  - LIBERO에서 CorridorVLA는 SmolVLA를 4.45퍼센트 포인트 향상시킵니다.
  - LIBERO-Plus에서 CorridorVLA는 SmolVLA를 12.37퍼센트 포인트, GR00T를 7.98퍼센트 포인트 향상시킵니다.
- **단일 정책 4-in-1 설정**: 모든 작업 세트를 공동 훈련 및 평가하는 설정에서 GR00T-Corr는 83.21%의 성공률을 달성합니다.

### 결론
실험 결과는 희소 공간 앵커로 정의된 허용 회랑과 같은 동작 정렬 물리적 단서가 생성적 동작 정책에 직접적이고 해석 가능한 제약을 제공할 수 있으며, 시각적 또는 잠재 특징에 인코딩된 공간 안내를 효과적으로 보완함을 보여줍니다. 코드와 모델 체크포인트는 오픈소스로 공개되었습니다.
