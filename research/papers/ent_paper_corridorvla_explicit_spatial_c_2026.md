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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21241v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision--Language--Action (VLA) 모델은 종종 중간 표현을 사용하여 다중 모드 입력과 연속 제어를 연결하지만, 공간적 안내는 종종 잠재 특징을 통해 암시적으로 주입됩니다. 우리는 CorridorVLA를 제안합니다. 이는 희소 공간 앵커를 점진적 물리적 변화(예: 엔드 이펙터 $Δ$-위치)로 예측하고, 이를 사용하여 행동 생성을 위한 훈련 목표에 명시적 허용 영역을 부과합니다. 앵커는 흐름 매칭 행동 헤드를 안내하는 허용 회랑을 정의합니다: 암시된 공간적 진화가 회랑 밖에 있는 궤적은 수정 그래디언트를 받고, 회랑 내의 궤적은 일관성 목표에 의해 정제됩니다. CorridorVLA는 LIBERO에서 SmolVLA를 4.45% 포인트 개선하고, 더 어려운 LIBERO-Plus 벤치마크에서 SmolVLA와 GR00T를 각각 12.37%와 7.98% 포인트 개선합니다. 특히, 하나의 정책이 모든 작업 제품군에서 공동으로 훈련되고 평가되는 동일한 단일 정책 4-in-1 설정에서 GR00T-Corr는 83.21%의 성공률을 달성합니다. 이러한 결과는 행동 정렬 물리적 단서가 생성적 행동 정책에 직접적이고 해석 가능한 제약을 제공하여 시각적 또는 잠재적 형태로 인코딩된 공간적 안내를 보완할 수 있음을 나타냅니다. 코드와 공개된 모델 체크포인트는 https://github.com/lidc54/corridorVLA 및 https://huggingface.co/lidc/CorridorVLA에서 확인할 수 있습니다.

## 핵심 내용
Vision--Language--Action (VLA) 모델은 종종 중간 표현을 사용하여 다중 모드 입력과 연속 제어를 연결하지만, 공간적 안내는 종종 잠재 특징을 통해 암시적으로 주입됩니다. 우리는 CorridorVLA를 제안합니다. 이는 희소 공간 앵커를 점진적 물리적 변화(예: 엔드 이펙터 $Δ$-위치)로 예측하고, 이를 사용하여 행동 생성을 위한 훈련 목표에 명시적 허용 영역을 부과합니다. 앵커는 흐름 매칭 행동 헤드를 안내하는 허용 회랑을 정의합니다: 암시된 공간적 진화가 회랑 밖에 있는 궤적은 수정 그래디언트를 받고, 회랑 내의 궤적은 일관성 목표에 의해 정제됩니다. CorridorVLA는 LIBERO에서 SmolVLA를 4.45% 포인트 개선하고, 더 어려운 LIBERO-Plus 벤치마크에서 SmolVLA와 GR00T를 각각 12.37%와 7.98% 포인트 개선합니다. 특히, 하나의 정책이 모든 작업 제품군에서 공동으로 훈련되고 평가되는 동일한 단일 정책 4-in-1 설정에서 GR00T-Corr는 83.21%의 성공률을 달성합니다. 이러한 결과는 행동 정렬 물리적 단서가 생성적 행동 정책에 직접적이고 해석 가능한 제약을 제공하여 시각적 또는 잠재적 형태로 인코딩된 공간적 안내를 보완할 수 있음을 나타냅니다. 코드와 공개된 모델 체크포인트는 https://github.com/lidc54/corridorVLA 및 https://huggingface.co/lidc/CorridorVLA에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2604.21241v2
