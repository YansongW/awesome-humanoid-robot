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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02549v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (812 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.02549v1

## 개요
VulcanVoxel은 블레이드 삽입의 통과 가능성 추론을 기존의 SE(3) 포즈 분포 문제에서 3D 공간 추론 문제로 재정의합니다. 이 방법은 마스크 오토인코더를 사용하여 3D 점유 필드를 처리하고, 장면 기하학에 따라 블레이드 점유 상황을 조건부로 재구성하며, 각 복셀에서 국소적으로 실행 가능성을 계산하여 단일 모드 데이터에서 다중 모드 예측을 복구합니다. 10,000개의 실제 창고 장면에서 훈련한 후, VulcanVoxel의 top-5 커버리지는 0.89에 도달한 반면, 최고의 포즈 기준선의 커버리지는 0.71이었습니다. 증류된 학생 모델은 RGB에서 복셀로의 추론에 30밀리초가 걸리며, 복셀에서 복셀로의 추론에는 1.4초가 필요합니다.

## 핵심 내용
### 핵심 문제
많은 조작 작업은 자유 공간 통과 가능성을 추론해야 하며, 즉 강체 도구가 안전하게 이동할 수 있는 체적 영역을 발견해야 합니다. 이는 파지에 필요한 표면 접촉 통과 가능성과 상호 보완적입니다. 로봇 창고 조작이 전형적인 예로, 블레이드는 복잡한 직물 상자 내부에서 물체를 밀어내어 삽입 공간을 만들어야 합니다.

### 기존 방법의 한계
- 표준 방법은 단일 모드 데이터를 사용하여 통과 가능성을 SE(3) 포즈 분포로 추론하며, 이는 잘못된 영역에서의 기하학적 문제입니다
- 포즈 매개변수는 관찰되지 않은 배치가 실행 가능한지 추론할 구조가 부족합니다
- 흐름 매칭을 포함한 표준 생성 목표는 실행 정책이 생성한 단일 모드 분포만 충실히 학습할 수 있으며, 기하학적 대안을 복구할 수 없습니다

### VulcanVoxel 방법
- 통과 가능성을 공간 추론으로 유지: 3D 점유 필드에서 마스크 오토인코더 사용
- 장면 기하학에 따라 블레이드 점유 상황을 조건부로 재구성
- 각 복셀에서 국소적으로 실행 가능성 계산
- 단일 모드 데이터에서 다중 모드 예측 복구
- 블레이드 통과 가능성은 공간 객체, 즉 기하학적 실행 가능성으로 정의된 3D 공간 부분집합입니다

### 실험 설정 및 결과
- 훈련 데이터: 10,000개의 실제 창고 조작 장면, 수동 주석 불필요
- 성능 지표: top-5 커버리지
- VulcanVoxel은 0.89에 도달, 최고 포즈 기준선은 0.71
- 증류 학생 모델: RGB에서 복셀로의 추론은 30밀리초만 필요, 복셀에서 복셀로의 추론은 1.4초 필요

### 데이터셋 공개
실제 블레이드 삽입 루프 데이터셋을 공개했으며, RGB-D 관측 및 포즈 궤적을 포함합니다. 접속 주소: https://www.armbench.com/blade_insertion.html
