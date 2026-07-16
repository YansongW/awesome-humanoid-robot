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
  zh: 'arXiv:2604.21241v2 Announce Type: replace Abstract: Vision--Language--Action (VLA) models often use intermediate representations
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21241v2.
sources:
- id: src_001
  type: paper
  title: 'CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors (arXiv)'
  url: https://arxiv.org/abs/2604.21241
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $Δ$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## 核心内容
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $Δ$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## 参考
- http://arxiv.org/abs/2604.21241v2

## Overview
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## Content
Vision--Language--Action (VLA) models often use intermediate representations to connect multimodal inputs with continuous control, yet spatial guidance is often injected implicitly through latent features. We propose CorridorVLA, which predicts sparse spatial anchors as incremental physical changes (e.g., end-effector $\Delta$-positions) and uses them to impose an explicit tolerance region in the training objective for action generation. The anchors define a tolerance corridor that guides a flow-matching action head: trajectories whose implied spatial evolution falls outside the corridor receive corrective gradients, while trajectories within the corridor are refined by a consistency objective. CorridorVLA improves SmolVLA by 4.45 percentage points on LIBERO and improves SmolVLA and GR00T by 12.37 and 7.98 percentage points, respectively, on the more challenging LIBERO-Plus benchmark. Notably, under the same single-policy 4-in-1 setting, where one policy is jointly trained and evaluated across all task suites, GR00T-Corr achieves an 83.21% success rate. These results indicate that action-aligned physical cues can provide direct and interpretable constraints for generative action policies, complementing spatial guidance encoded in visual or latent forms. Code and released model checkpoints are available at https://github.com/lidc54/corridorVLA and https://huggingface.co/lidc/CorridorVLA.

## 개요
Vision--Language--Action (VLA) 모델은 종종 중간 표현을 사용하여 다중 모드 입력과 연속 제어를 연결하지만, 공간적 안내는 종종 잠재 특징을 통해 암시적으로 주입됩니다. 우리는 CorridorVLA를 제안합니다. 이는 희소 공간 앵커를 점진적 물리적 변화(예: 엔드 이펙터 $Δ$-위치)로 예측하고, 이를 사용하여 행동 생성을 위한 훈련 목표에 명시적 허용 영역을 부과합니다. 앵커는 흐름 매칭 행동 헤드를 안내하는 허용 회랑을 정의합니다: 암시된 공간적 진화가 회랑 밖에 있는 궤적은 수정 그래디언트를 받고, 회랑 내의 궤적은 일관성 목표에 의해 정제됩니다. CorridorVLA는 LIBERO에서 SmolVLA를 4.45% 포인트 개선하고, 더 어려운 LIBERO-Plus 벤치마크에서 SmolVLA와 GR00T를 각각 12.37%와 7.98% 포인트 개선합니다. 특히, 하나의 정책이 모든 작업 제품군에서 공동으로 훈련되고 평가되는 동일한 단일 정책 4-in-1 설정에서 GR00T-Corr는 83.21%의 성공률을 달성합니다. 이러한 결과는 행동 정렬 물리적 단서가 생성적 행동 정책에 직접적이고 해석 가능한 제약을 제공하여 시각적 또는 잠재적 형태로 인코딩된 공간적 안내를 보완할 수 있음을 나타냅니다. 코드와 공개된 모델 체크포인트는 https://github.com/lidc54/corridorVLA 및 https://huggingface.co/lidc/CorridorVLA에서 확인할 수 있습니다.

## 핵심 내용
Vision--Language--Action (VLA) 모델은 종종 중간 표현을 사용하여 다중 모드 입력과 연속 제어를 연결하지만, 공간적 안내는 종종 잠재 특징을 통해 암시적으로 주입됩니다. 우리는 CorridorVLA를 제안합니다. 이는 희소 공간 앵커를 점진적 물리적 변화(예: 엔드 이펙터 $Δ$-위치)로 예측하고, 이를 사용하여 행동 생성을 위한 훈련 목표에 명시적 허용 영역을 부과합니다. 앵커는 흐름 매칭 행동 헤드를 안내하는 허용 회랑을 정의합니다: 암시된 공간적 진화가 회랑 밖에 있는 궤적은 수정 그래디언트를 받고, 회랑 내의 궤적은 일관성 목표에 의해 정제됩니다. CorridorVLA는 LIBERO에서 SmolVLA를 4.45% 포인트 개선하고, 더 어려운 LIBERO-Plus 벤치마크에서 SmolVLA와 GR00T를 각각 12.37%와 7.98% 포인트 개선합니다. 특히, 하나의 정책이 모든 작업 제품군에서 공동으로 훈련되고 평가되는 동일한 단일 정책 4-in-1 설정에서 GR00T-Corr는 83.21%의 성공률을 달성합니다. 이러한 결과는 행동 정렬 물리적 단서가 생성적 행동 정책에 직접적이고 해석 가능한 제약을 제공하여 시각적 또는 잠재적 형태로 인코딩된 공간적 안내를 보완할 수 있음을 나타냅니다. 코드와 공개된 모델 체크포인트는 https://github.com/lidc54/corridorVLA 및 https://huggingface.co/lidc/CorridorVLA에서 확인할 수 있습니다.
