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
  zh: VolumeDP 是一种面向机器人操作模仿学习的策略架构，由研究团队提出。其核心贡献在于通过显式的三维空间推理，将图像特征提升为体素表示，并利用可学习模块选择任务相关体素生成紧凑空间令牌，最终由多令牌解码器预测动作。在 LIBERO
    仿真基准上达到 88.8% 的平均成功率，相比最强基线提升 14.8%，并在 ManiSkill 和 LIBERO-Plus 基准上取得显著性能提升。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.17720v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (797 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'VolumeDP: Modeling Volumetric Representation for Manipulation Policy Learning (arXiv)'
  url: https://arxiv.org/abs/2603.17720
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
VolumeDP 旨在解决现有视觉模仿方法中 2D 图像观测与 3D 动作输出之间的空间不匹配问题。该方法首先通过交叉注意力机制将图像特征提升为体素表示，然后利用可学习模块选择任务相关的体素，并将其转换为紧凑的空间令牌集，从而在保留动作关键几何信息的同时大幅降低计算量。最后，多令牌解码器基于整个令牌集预测动作，避免了将多个空间令牌聚合为单一描述符的信息损失。在 LIBERO 仿真基准上，VolumeDP 以 88.8% 的平均成功率超越最强基线 14.8%，并在 ManiSkill 和 LIBERO-Plus 基准上实现大幅性能提升。真实世界实验进一步验证了其更高的成功率和在新型空间布局、相机视角及环境背景下的鲁棒泛化能力。

## 核心内容
### 方法架构
VolumeDP 的策略架构包含三个核心阶段：
- **体素表示构建**：通过交叉注意力机制将 2D 图像特征提升为 3D 体素表示，实现空间对齐。
- **任务相关体素选择**：利用可学习模块筛选出与任务相关的体素，并将其转换为紧凑的空间令牌集，显著降低计算开销，同时保留对动作关键几何信息。
- **多令牌解码器**：基于整个令牌集进行动作预测，避免将多个空间令牌聚合为单一描述符导致的信息损失。

### 实验设置与关键数字
- **LIBERO 仿真基准**：VolumeDP 达到 88.8% 的平均成功率，相比最强基线提升 14.8%。
- **ManiSkill 和 LIBERO-Plus 基准**：相比先前方法实现大幅性能提升。
- **真实世界实验**：在新型空间布局、相机视角和环境背景下，均表现出更高的成功率和鲁棒泛化能力。

### 结论
VolumeDP 通过显式三维空间推理和紧凑令牌表示，有效解决了 2D-3D 不匹配问题，在多个仿真和真实场景中均取得领先性能。代码和视频已开源。

## Overview
Imitation learning is a prominent paradigm for robotic manipulation. However, existing visual imitation methods map 2D image observations directly to 3D action outputs, imposing a 2D-3D mismatch that hinders spatial reasoning and degrades robustness. We present VolumeDP, a policy architecture that restores spatial alignment by explicitly reasoning in 3D. VolumeDP first lifts image features into a Volumetric Representation via cross-attention. It then selects task-relevant voxels with a learnable module and converts them into a compact set of spatial tokens, markedly reducing computation while preserving action-critical geometry. Finally, a multi-token decoder conditions on the entire token set to predict actions, thereby avoiding lossy aggregation that collapses multiple spatial tokens into a single descriptor. VolumeDP achieves a state-of-the-art average success rate of 88.8% on the LIBERO simulation benchmark, outperforming the strongest baseline by a substantial 14.8% improvement. It also delivers large performance gains over prior methods on the ManiSkill and LIBERO-Plus benchmarks. Real-world experiments further demonstrate higher success rates and robust generalization to novel spatial layouts, camera viewpoints, and environment backgrounds. Code and videos are available on the project page: https://yzc0731.github.io/VolumeDP/

## 参考
- http://arxiv.org/abs/2603.17720v2

## 개요
VolumeDP는 기존 시각적 모방 방법에서 2D 이미지 관측과 3D 동작 출력 간의 공간적 불일치 문제를 해결하기 위해 설계되었습니다. 이 방법은 먼저 교차 주의 메커니즘을 통해 이미지 특징을 복셀 표현으로 승격시킨 다음, 학습 가능한 모듈을 사용하여 작업 관련 복셀을 선택하고 이를 압축된 공간 토큰 집합으로 변환하여 동작에 중요한 기하학적 정보를 유지하면서 계산량을 크게 줄입니다. 마지막으로, 다중 토큰 디코더는 전체 토큰 집합을 기반으로 동작을 예측하여 여러 공간 토큰을 단일 설명자로 집계할 때 발생하는 정보 손실을 방지합니다. LIBERO 시뮬레이션 벤치마크에서 VolumeDP는 88.8%의 평균 성공률로 가장 강력한 기준선을 14.8% 초과하며, ManiSkill 및 LIBERO-Plus 벤치마크에서도 큰 성능 향상을 달성했습니다. 실제 세계 실험은 더 높은 성공률과 새로운 공간 배치, 카메라 시점 및 환경 배경에서의 강건한 일반화 능력을 추가로 검증합니다.

## 핵심 내용
### 방법 아키텍처
VolumeDP의 정책 아키텍처는 세 가지 핵심 단계로 구성됩니다:
- **복셀 표현 구축**: 교차 주의 메커니즘을 통해 2D 이미지 특징을 3D 복셀 표현으로 승격시켜 공간 정렬을 구현합니다.
- **작업 관련 복셀 선택**: 학습 가능한 모듈을 사용하여 작업 관련 복셀을 필터링하고 이를 압축된 공간 토큰 집합으로 변환하여 계산 오버헤드를 크게 줄이면서 동작에 중요한 기하학적 정보를 유지합니다.
- **다중 토큰 디코더**: 전체 토큰 집합을 기반으로 동작을 예측하여 여러 공간 토큰을 단일 설명자로 집계할 때 발생하는 정보 손실을 방지합니다.

### 실험 설정 및 주요 수치
- **LIBERO 시뮬레이션 벤치마크**: VolumeDP는 88.8%의 평균 성공률을 달성하여 가장 강력한 기준선보다 14.8% 향상되었습니다.
- **ManiSkill 및 LIBERO-Plus 벤치마크**: 이전 방법 대비 큰 성능 향상을 달성했습니다.
- **실제 세계 실험**: 새로운 공간 배치, 카메라 시점 및 환경 배경에서 더 높은 성공률과 강건한 일반화 능력을 보여주었습니다.

### 결론
VolumeDP는 명시적 3D 공간 추론과 압축된 토큰 표현을 통해 2D-3D 불일치 문제를 효과적으로 해결하며, 여러 시뮬레이션 및 실제 시나리오에서 선도적인 성능을 달성합니다. 코드와 비디오는 오픈소스로 공개되었습니다.
