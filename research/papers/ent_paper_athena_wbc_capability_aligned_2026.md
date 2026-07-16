---
$id: ent_paper_athena_wbc_capability_aligned_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control'
  zh: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control'
  ko: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control'
summary:
  en: 'arXiv:2607.04837v1 Announce Type: new Abstract: Large-scale humanoid motion-tracking controllers are commonly improved
    by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned
    to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of
    feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical
    motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and
    the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline
    with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused,
    constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility
    constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged
    teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations
    followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions
    and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.'
  zh: 'arXiv:2607.04837v1 Announce Type: new Abstract: Large-scale humanoid motion-tracking controllers are commonly improved
    by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned
    to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of
    feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical
    motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and
    the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline
    with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused,
    constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility
    constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged
    teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations
    followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions
    and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.'
  ko: 'arXiv:2607.04837v1 Announce Type: new Abstract: Large-scale humanoid motion-tracking controllers are commonly improved
    by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned
    to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of
    feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical
    motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and
    the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline
    with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused,
    constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility
    constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged
    teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations
    followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions
    and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.'
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
- athena_wbc
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04837v2.
sources:
- id: src_001
  type: paper
  title: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2607.04837
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.

## 核心内容
Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.

## 参考
- http://arxiv.org/abs/2607.04837v2

## Overview
Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.

## Content
Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.

## 개요
대규모 휴머노이드 동작 추적 컨트롤러는 일반적으로 훈련 노력을 재분배하여 개선됩니다. 즉, 어려운 동작을 더 자주 샘플링하거나, 더 작은 하위 집합으로 분리하거나, 전문가에게 할당합니다. 우리는 이러한 관점이 불완전함을 보여줍니다. 강력한 전신 제어 기준선에서도, 특히 고역학적 전환 및 균형이 중요한 동작의 경우, 목표 훈련을 수행하더라도 실행 가능한 훈련 클립의 잔여 집합이 해결되지 않은 상태로 남아 있습니다. 이러한 실패는 단순히 노출 부족뿐만 아니라, 동작 요구 사항과 기본 훈련 방식에 의해 유도된 유효 능력 간의 불일치에서 비롯됩니다. 우리는 롱테일 휴머노이드 전신 제어를 위한 능력 정렬 정책 전문가를 갖춘 소형 교사-학생 파이프라인인 Athena-WBC를 제안합니다. 동적 전문가는 추적 중심의 제약 인식 목표를 사용하여 보수적인 노력 및 시간 제어 패널티를 제거하면서 물리적 실행 가능성 제약을 유지합니다. 균형 전문가는 중력 커리큘럼을 사용하여 초기 훈련 생존성을 향상시킵니다. 결과적으로 얻어진 특권 교사는 DAgger 증류를 위해 동작 라우팅된 후, 배포 가능한 관측값을 갖춘 단일 컨트롤러로 압축되고 RL 미세 조정이 이어집니다. 전체 크기 휴머노이드 실험에서 소수의 전문가만 사용하여 강력한 SONIC 레시피 기준선보다 훈련 세트 롱테일 동작의 복구 및 보류된 추적 성능이 향상됨을 보여줍니다.

## 핵심 내용
대규모 휴머노이드 동작 추적 컨트롤러는 일반적으로 훈련 노력을 재분배하여 개선됩니다. 즉, 어려운 동작을 더 자주 샘플링하거나, 더 작은 하위 집합으로 분리하거나, 전문가에게 할당합니다. 우리는 이러한 관점이 불완전함을 보여줍니다. 강력한 전신 제어 기준선에서도, 특히 고역학적 전환 및 균형이 중요한 동작의 경우, 목표 훈련을 수행하더라도 실행 가능한 훈련 클립의 잔여 집합이 해결되지 않은 상태로 남아 있습니다. 이러한 실패는 단순히 노출 부족뿐만 아니라, 동작 요구 사항과 기본 훈련 방식에 의해 유도된 유효 능력 간의 불일치에서 비롯됩니다. 우리는 롱테일 휴머노이드 전신 제어를 위한 능력 정렬 정책 전문가를 갖춘 소형 교사-학생 파이프라인인 Athena-WBC를 제안합니다. 동적 전문가는 추적 중심의 제약 인식 목표를 사용하여 보수적인 노력 및 시간 제어 패널티를 제거하면서 물리적 실행 가능성 제약을 유지합니다. 균형 전문가는 중력 커리큘럼을 사용하여 초기 훈련 생존성을 향상시킵니다. 결과적으로 얻어진 특권 교사는 DAgger 증류를 위해 동작 라우팅된 후, 배포 가능한 관측값을 갖춘 단일 컨트롤러로 압축되고 RL 미세 조정이 이어집니다. 전체 크기 휴머노이드 실험에서 소수의 전문가만 사용하여 강력한 SONIC 레시피 기준선보다 훈련 세트 롱테일 동작의 복구 및 보류된 추적 성능이 향상됨을 보여줍니다.
