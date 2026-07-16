---
$id: ent_paper_volumedp_modeling_volumetric_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning'
  zh: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning'
  ko: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning'
summary:
  en: 'arXiv:2603.17720v2 Announce Type: replace Abstract: Imitation learning is a prominent paradigm for robotic manipulation.
    However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch
    that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial
    alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention.
    It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly
    reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire
    token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single
    descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming
    the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods
    on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust
    generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available
    on the project page: https://yzc0731.github.io/VolumeDP/'
  zh: 'arXiv:2603.17720v2 Announce Type: replace Abstract: Imitation learning is a prominent paradigm for robotic manipulation.
    However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch
    that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial
    alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention.
    It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly
    reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire
    token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single
    descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming
    the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods
    on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust
    generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available
    on the project page: https://yzc0731.github.io/VolumeDP/'
  ko: 'arXiv:2603.17720v2 Announce Type: replace Abstract: Imitation learning is a prominent paradigm for robotic manipulation.
    However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch
    that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial
    alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention.
    It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly
    reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire
    token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single
    descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming
    the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods
    on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust
    generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available
    on the project page: https://yzc0731.github.io/VolumeDP/'
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
- volumedp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.17720v2.
sources:
- id: src_001
  type: paper
  title: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning (arXiv)'
  url: https://arxiv.org/abs/2603.17720
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## 核心内容
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## 参考
- http://arxiv.org/abs/2603.17720v2

## Overview
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## Content
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## 개요
Imitation learning은 로봇 조작을 위한 주요 패러다임입니다. 그러나 기존의 시각적 모방 방법은 2D 이미지 관측을 직접 3D 행동 출력으로 매핑하여, 공간 추론을 방해하고 강건성을 저하시키는 2D-3D 불일치를 초래합니다. 본 논문에서는 3D에서 명시적으로 추론함으로써 공간 정렬을 복원하는 정책 아키텍처인 VolumeDP를 제안합니다. VolumeDP는 먼저 교차 주의를 통해 이미지 특징을 체적 표현(Volumetric Representation)으로 변환합니다. 그런 다음 학습 가능한 모듈로 작업 관련 복셀을 선택하고 이를 압축된 공간 토큰 집합으로 변환하여, 행동에 중요한 기하학적 정보를 유지하면서 계산량을 현저히 줄입니다. 마지막으로, 다중 토큰 디코더가 전체 토큰 집합을 조건으로 행동을 예측함으로써, 여러 공간 토큰을 단일 설명자로 축소하는 손실 있는 집계를 방지합니다. VolumeDP는 LIBERO 시뮬레이션 벤치마크에서 최첨단 평균 성공률 88.8%를 달성하여, 가장 강력한 기준선보다 14.8%의 큰 개선을 보였습니다. 또한 ManiSkill 및 LIBERO-Plus 벤치마크에서 이전 방법들보다 큰 성능 향상을 제공합니다. 실제 환경 실험은 더 높은 성공률과 새로운 공간 배치, 카메라 시점, 환경 배경에 대한 강건한 일반화를 추가로 입증합니다. 코드와 비디오는 프로젝트 페이지에서 확인할 수 있습니다: https://yzc0731.github.io/VolumeDP/

## 핵심 내용
Imitation learning은 로봇 조작을 위한 주요 패러다임입니다. 그러나 기존의 시각적 모방 방법은 2D 이미지 관측을 직접 3D 행동 출력으로 매핑하여, 공간 추론을 방해하고 강건성을 저하시키는 2D-3D 불일치를 초래합니다. 본 논문에서는 3D에서 명시적으로 추론함으로써 공간 정렬을 복원하는 정책 아키텍처인 VolumeDP를 제안합니다. VolumeDP는 먼저 교차 주의를 통해 이미지 특징을 체적 표현(Volumetric Representation)으로 변환합니다. 그런 다음 학습 가능한 모듈로 작업 관련 복셀을 선택하고 이를 압축된 공간 토큰 집합으로 변환하여, 행동에 중요한 기하학적 정보를 유지하면서 계산량을 현저히 줄입니다. 마지막으로, 다중 토큰 디코더가 전체 토큰 집합을 조건으로 행동을 예측함으로써, 여러 공간 토큰을 단일 설명자로 축소하는 손실 있는 집계를 방지합니다. VolumeDP는 LIBERO 시뮬레이션 벤치마크에서 최첨단 평균 성공률 88.8%를 달성하여, 가장 강력한 기준선보다 14.8%의 큰 개선을 보였습니다. 또한 ManiSkill 및 LIBERO-Plus 벤치마크에서 이전 방법들보다 큰 성능 향상을 제공합니다. 실제 환경 실험은 더 높은 성공률과 새로운 공간 배치, 카메라 시점, 환경 배경에 대한 강건한 일반화를 추가로 입증합니다. 코드와 비디오는 프로젝트 페이지에서 확인할 수 있습니다: https://yzc0731.github.io/VolumeDP/
