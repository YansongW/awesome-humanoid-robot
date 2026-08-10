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
  zh: Athena-WBC 是一种用于人形机器人全身控制的长尾运动跟踪方法，由研究团队提出。其核心贡献在于通过能力对齐的策略专家（动态专家与平衡专家）解决训练中运动需求与默认训练能力不匹配的问题，仅用少量专家即可在全身控制中超越SONIC基线。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04837v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (957 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control (arXiv)'
  url: https://arxiv.org/abs/2607.04837
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有大规模人形运动跟踪控制器通常通过重新分配训练努力（如对困难运动增加采样、隔离子集或分配专家）来改进，但Athena-WBC发现这种观点不完整。即使在强基线中，仍有可行训练片段无法解决，尤其是高动态过渡和平衡关键运动，这源于运动需求与默认训练能力的不匹配。为此，Athena-WBC提出紧凑的教师-学生流水线，包含动态专家（使用跟踪聚焦、约束感知的目标，去除保守努力和时间控制惩罚，保留物理可行性约束）和平衡专家（使用重力课程提高早期训练生存能力）。特权教师通过DAgger蒸馏进行运动路由，压缩为单一控制器，再经RL微调。在全尺寸人形机器人实验中，Athena-WBC在训练集长尾运动恢复和未见运动跟踪上均优于SONIC基线。

## 核心内容
### 方法架构
- **教师-学生流水线**：Athena-WBC采用紧凑的教师-学生结构，包含两类能力对齐的策略专家。
- **动态专家**：使用跟踪聚焦、约束感知的目标函数，移除保守努力和时间控制惩罚，同时保留物理可行性约束，专注于高动态运动。
- **平衡专家**：引入重力课程（gravity curriculum），在早期训练阶段提高生存能力，针对平衡关键运动。
- **蒸馏与压缩**：特权教师通过DAgger蒸馏进行运动路由（motion-routed），将多个专家知识压缩为单一控制器，使用可部署观测（deployable observations），随后进行RL微调。

### 实验设置
- **平台**：全尺寸人形机器人。
- **基线**：与强SONIC基线对比。
- **专家数量**：仅使用少量专家（具体数量未在摘要中给出，但强调“small number of experts”）。

### 关键结果
- **长尾运动恢复**：Athena-WBC在训练集中长尾运动的恢复上显著优于SONIC基线。
- **未见运动跟踪**：在未见运动（held-out tracking）上表现更好，表明泛化能力提升。
- **效率**：仅用少量专家即实现性能改进，验证了能力对齐策略的有效性。

### 结论
Athena-WBC通过能力对齐的专家设计，解决了运动需求与训练能力不匹配的问题，为长尾人形全身控制提供了高效解决方案。

## Overview
Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.

## 参考
- http://arxiv.org/abs/2607.04837v2

## 개요
기존 대규모 휴머노이드 동작 추적 컨트롤러는 일반적으로 훈련 노력을 재분배(예: 어려운 동작에 샘플링 증가, 하위 집합 격리, 또는 전문가 할당)하여 개선하지만, Athena-WBC는 이러한 관점이 불완전하다는 것을 발견했습니다. 강력한 기준선에서도 해결되지 않는 실행 가능한 훈련 세그먼트가 여전히 존재하며, 특히 고동적 전환 및 균형 핵심 동작에서 그러합니다. 이는 동작 요구 사항과 기본 훈련 능력 간의 불일치에서 비롯됩니다. 이를 위해 Athena-WBC는 동적 전문가(추적 중심, 제약 인식 목표를 사용하고 보수적 노력 및 시간 제어 페널티를 제거하며 물리적 실현 가능성 제약을 유지)와 균형 전문가(중력 커리큘럼을 사용하여 초기 훈련 생존성을 향상)를 포함하는 컴팩트한 교사-학생 파이프라인을 제안합니다. 특권 교사는 DAgger 증류를 통해 동작 라우팅을 수행하고 단일 컨트롤러로 압축한 후 RL 미세 조정을 거칩니다. 전신 휴머노이드 실험에서 Athena-WBC는 훈련 세트의 긴 꼬리 동작 복구 및 미지 동작 추적 모두에서 SONIC 기준선보다 우수했습니다.

## 핵심 내용
### 방법 아키텍처
- **교사-학생 파이프라인**: Athena-WBC는 두 가지 능력 정렬 정책 전문가를 포함하는 컴팩트한 교사-학생 구조를 채택합니다.
- **동적 전문가**: 추적 중심, 제약 인식 목표 함수를 사용하고 보수적 노력 및 시간 제어 페널티를 제거하면서 물리적 실현 가능성 제약을 유지하여 고동적 동작에 집중합니다.
- **균형 전문가**: 중력 커리큘럼(gravity curriculum)을 도입하여 초기 훈련 단계에서 생존성을 향상시키고 균형 핵심 동작을 대상으로 합니다.
- **증류 및 압축**: 특권 교사는 DAgger 증류를 통해 동작 라우팅(motion-routed)을 수행하고 여러 전문가 지식을 단일 컨트롤러로 압축하며 배포 가능한 관측(deployable observations)을 사용한 후 RL 미세 조정을 진행합니다.

### 실험 설정
- **플랫폼**: 전신 휴머노이드 로봇.
- **기준선**: 강력한 SONIC 기준선과 비교.
- **전문가 수**: 소수의 전문가만 사용(구체적인 수는 초록에 명시되지 않았지만 "small number of experts"를 강조).

### 주요 결과
- **긴 꼬리 동작 복구**: Athena-WBC는 훈련 세트의 긴 꼬리 동작 복구에서 SONIC 기준선보다 현저히 우수했습니다.
- **미지 동작 추적**: 미지 동작(held-out tracking) 추적에서 더 나은 성능을 보여 일반화 능력이 향상되었음을 나타냅니다.
- **효율성**: 소수의 전문가만으로 성능 개선을 달성하여 능력 정렬 정책의 효과를 검증했습니다.

### 결론
Athena-WBC는 능력 정렬 전문가 설계를 통해 동작 요구 사항과 훈련 능력 간의 불일치 문제를 해결하여 긴 꼬리 휴머노이드 전신 제어를 위한 효율적인 솔루션을 제공합니다.
