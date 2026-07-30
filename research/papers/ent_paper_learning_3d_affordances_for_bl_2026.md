---
$id: ent_paper_learning_3d_affordances_for_bl_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning 3D Affordances for Blade Insertion in Cluttered Stowing
  zh: Learning 3D Affordances for Blade Insertion in Cluttered Stowing
  ko: Learning 3D Affordances for Blade Insertion in Cluttered Stowing
summary:
  en: 'arXiv:2607.02549v1 Announce Type: cross Abstract: Many manipulation tasks require reasoning about free-space affordances:
    discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for
    grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to
    create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal
    data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps
    inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry,
    computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances
    are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning
    whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn
    the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000
    real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the
    best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel.
    We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion.
    html.'
  zh: 本文提出VulcanVoxel，一种用于杂乱仓储环境中刀片插入操作的空间可通行性推理方法。该方法将可通行性建模为3D空间子集，通过掩码自编码器从单峰数据中恢复多模态预测，在10,000个真实仓储场景上训练后，top-5覆盖率达到0.89，显著优于基于位姿的基线方法。
  ko: 'arXiv:2607.02549v1 Announce Type: cross Abstract: Many manipulation tasks require reasoning about free-space affordances:
    discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for
    grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to
    create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal
    data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps
    inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry,
    computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances
    are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning
    whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn
    the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000
    real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the
    best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel.
    We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion.
    html.'
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
- learning_3d_affordances_for_bl
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02549v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning 3D Affordances for Blade Insertion in Cluttered Stowing (arXiv)
  url: https://arxiv.org/abs/2607.02549
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
VulcanVoxel将刀片插入的可通行性推理从传统的SE(3)位姿分布问题重新定义为3D空间推理问题。该方法使用掩码自编码器处理3D占据场，根据场景几何条件重建刀片占据情况，在每个体素局部计算可行性，从而从单峰数据中恢复多模态预测。在10,000个真实仓储场景上训练后，VulcanVoxel的top-5覆盖率达到0.89，而最佳位姿基线的覆盖率为0.71。蒸馏后的学生模型可实现30毫秒的RGB到体素推理，而体素到体素推理需要1.4秒。

## 核心内容
### 核心问题
许多操作任务需要推理自由空间可通行性，即发现刚性工具可以安全导航的体积区域，这与抓取所需的表面接触可通行性互补。机器人仓储操作是典型实例，刀片需要在杂乱织物箱内扫开物品以创造插入空间。

### 现有方法局限
- 标准方法使用单峰数据将可通行性推断为SE(3)位姿分布，这是错误域中的几何问题
- 位姿参数缺乏结构来推理未观测放置是否可行
- 包括流匹配在内的标准生成目标只能忠实学习执行策略产生的单峰分布，无法恢复几何替代方案

### VulcanVoxel方法
- 将可通行性保持为空间推理：使用3D占据场上的掩码自编码器
- 根据场景几何条件重建刀片占据情况
- 在每个体素局部计算可行性
- 从单峰数据中恢复多模态预测
- 刀片可通行性是空间对象，即由几何可行性定义的3D空间子集

### 实验设置与结果
- 训练数据：10,000个真实仓储操作场景，无需人工标注
- 性能指标：top-5覆盖率
- VulcanVoxel达到0.89，最佳位姿基线为0.71
- 蒸馏学生模型：RGB到体素推理仅需30毫秒，而体素到体素推理需要1.4秒

### 数据集发布
已发布真实刀片插入循环数据集，包含RGB-D观测和位姿轨迹，访问地址：https://www.armbench.com/blade_insertion.html

## Overview
Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion. html.

## Overview
Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion.html.

## Content
Many manipulation tasks require reasoning about free-space affordances: discovering volumes where an extended rigid tool can safely navigate, complementary to surface contact affordances for grasping. Robotic stowing is a canonical instance, where a blade must sweep items aside inside cluttered fabric bins to create insertion space. Production stow systems generate millions of such episodes, but standard approaches with unimodal data infer affordances as SE(3) pose distributions, a geometric question asked in the wrong domain. VulcanVoxel keeps inference spatial: a masked autoencoder over 3D occupancy fields reconstructs blade occupancy conditioned on scene geometry, computing feasibility locally at each voxel and recovering multi-modal predictions from unimodal data. Blade affordances are spatial objects, subsets of 3D space defined by geometric feasibility. Pose parameters carry no structure for reasoning whether unobserved placements are feasible, and standard generative objectives including flow matching faithfully learn the unimodal distribution produced by execution policies and cannot recover geometric alternatives. Trained on 10,000 real warehouse stow episodes without human annotation, VulcanVoxel achieves top-5 coverage of 0.89 versus 0.71 for the best pose-based baseline, with a distilled student providing RGB-to-voxel inference in 30 ms. vs. 1.4 s. for voxel-to-voxel. We have released a dataset of real blade insertion cycles with RGB-D observations and pose trajectories at https://www.armbench.com/blade_insertion.html.

## 개요
많은 조작 작업은 자유 공간 어포던스(free-space affordances)에 대한 추론을 필요로 합니다. 즉, 확장된 강체 도구가 안전하게 이동할 수 있는 부피를 발견하는 것이며, 이는 파지를 위한 표면 접촉 어포던스와 상호 보완적입니다. 로봇 수납(robotic stowing)은 대표적인 예로, 블레이드가 어수선한 천 재질의 빈 내부에서 물체를 밀어내어 삽입 공간을 만드는 작업입니다. 생산 수납 시스템은 수백만 건의 이러한 에피소드를 생성하지만, 단일 모드 데이터를 사용하는 표준 접근 방식은 어포던스를 SE(3) 자세 분포로 추론하며, 이는 잘못된 영역에서 제기된 기하학적 질문입니다. VulcanVoxel은 추론을 공간적으로 유지합니다. 3D 점유 필드에 대한 마스크 오토인코더가 장면 기하학에 조건화된 블레이드 점유를 재구성하여 각 복셀에서 국소적으로 실행 가능성을 계산하고 단일 모드 데이터에서 다중 모드 예측을 복구합니다. 블레이드 어포던스는 공간 객체로, 기하학적 실행 가능성에 의해 정의된 3D 공간의 부분 집합입니다. 자세 매개변수는 관찰되지 않은 배치가 실행 가능한지 추론하는 구조를 가지지 않으며, 흐름 매칭을 포함한 표준 생성 목표는 실행 정책에 의해 생성된 단일 모드 분포를 충실히 학습하지만 기하학적 대안을 복구할 수 없습니다. 인간 주석 없이 10,000개의 실제 창고 수납 에피소드로 훈련된 VulcanVoxel은 최상위 5개 커버리지에서 0.89를 달성하여 최고의 자세 기반 기준선의 0.71을 능가하며, 증류된 학생 모델은 RGB-복셀 추론을 30ms에 제공하는 반면 복셀-복셀은 1.4초가 소요됩니다. 우리는 RGB-D 관찰과 자세 궤적을 포함한 실제 블레이드 삽입 주기 데이터셋을 https://www.armbench.com/blade_insertion.html에서 공개했습니다.

## 핵심 내용
많은 조작 작업은 자유 공간 어포던스(free-space affordances)에 대한 추론을 필요로 합니다. 즉, 확장된 강체 도구가 안전하게 이동할 수 있는 부피를 발견하는 것이며, 이는 파지를 위한 표면 접촉 어포던스와 상호 보완적입니다. 로봇 수납(robotic stowing)은 대표적인 예로, 블레이드가 어수선한 천 재질의 빈 내부에서 물체를 밀어내어 삽입 공간을 만드는 작업입니다. 생산 수납 시스템은 수백만 건의 이러한 에피소드를 생성하지만, 단일 모드 데이터를 사용하는 표준 접근 방식은 어포던스를 SE(3) 자세 분포로 추론하며, 이는 잘못된 영역에서 제기된 기하학적 질문입니다. VulcanVoxel은 추론을 공간적으로 유지합니다. 3D 점유 필드에 대한 마스크 오토인코더가 장면 기하학에 조건화된 블레이드 점유를 재구성하여 각 복셀에서 국소적으로 실행 가능성을 계산하고 단일 모드 데이터에서 다중 모드 예측을 복구합니다. 블레이드 어포던스는 공간 객체로, 기하학적 실행 가능성에 의해 정의된 3D 공간의 부분 집합입니다. 자세 매개변수는 관찰되지 않은 배치가 실행 가능한지 추론하는 구조를 가지지 않으며, 흐름 매칭을 포함한 표준 생성 목표는 실행 정책에 의해 생성된 단일 모드 분포를 충실히 학습하지만 기하학적 대안을 복구할 수 없습니다. 인간 주석 없이 10,000개의 실제 창고 수납 에피소드로 훈련된 VulcanVoxel은 최상위 5개 커버리지에서 0.89를 달성하여 최고의 자세 기반 기준선의 0.71을 능가하며, 증류된 학생 모델은 RGB-복셀 추론을 30ms에 제공하는 반면 복셀-복셀은 1.4초가 소요됩니다. 우리는 RGB-D 관찰과 자세 궤적을 포함한 실제 블레이드 삽입 주기 데이터셋을 https://www.armbench.com/blade_insertion.html에서 공개했습니다.

## 参考
- http://arxiv.org/abs/2607.02549v1
