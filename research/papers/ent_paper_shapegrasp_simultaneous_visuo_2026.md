---
$id: ent_paper_shapegrasp_simultaneous_visuo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
  zh: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
  ko: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
summary:
  en: 'arXiv:2605.02347v2 Announce Type: replace Abstract: Humans grasp unfamiliar objects by combining an initial visual
    estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation
    of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic
    shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single
    RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body
    simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile
    surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger
    pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different
    robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following
    a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger
    gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics
    used.'
  zh: ShapeGrasp 是一种结合视觉与触觉的机器人抓取方法，由研究团队提出。其核心贡献在于首次在真实世界中通过抓取尝试更新物体形状表示，并实现了84%（三指夹爪）和91%（两指夹爪）的抓取成功率，同时提升了3D形状重建质量。
  ko: 'arXiv:2605.02347v2 Announce Type: replace Abstract: Humans grasp unfamiliar objects by combining an initial visual
    estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation
    of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic
    shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single
    RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body
    simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile
    surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger
    pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different
    robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following
    a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger
    gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics
    used.'
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
- shapegrasp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.02347v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (845 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation'
  url: https://arxiv.org/abs/2605.02347
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
ShapeGrasp 模拟人类抓取陌生物体时的策略，将初始视觉估计与交互中的触觉和本体感觉反馈相结合。该方法构建了一个迭代的抓取与形状补全流程，利用隐式表面表示融合视觉与触觉信息，从单张RGB-D图像推断完整形状，并通过刚体仿真生成候选抓取。每次抓取尝试都会产生新的几何约束（如触觉接触点和夹爪占据空间），这些信息被用于更新物体形状；若抓取失败，则基于更新后的形状重新估计位姿并再次尝试。在真实机器人上的实验表明，该方法在两种不同夹爪上均优于基线，且在所有评估指标上改善了3D形状重建。

## 核心内容
### 方法架构
ShapeGrasp 的核心是一个迭代的“抓取-补全”管道，包含以下步骤：
- **初始形状推断**：从单张RGB-D图像出发，利用隐式表面表示（implicit surface）完成部分到完整的3D形状重建，输出点云或三角网格。
- **抓取规划**：通过刚体仿真（rigid-body simulation）生成候选抓取，并选择最佳可行抓取执行。
- **触觉-视觉融合更新**：每次抓取尝试提供额外的几何约束，包括触觉表面接触点和夹爪本体占据的空间。这些信息被融合到形状表示中，更新物体模型。
- **失败处理**：若抓取失败，基于更新后的形状重新估计物体位姿并执行重新抓取。

### 实验设置
- **硬件**：使用两种不同的机器人和夹爪（三指夹爪和两指夹爪）在真实世界中进行评估。
- **基线**：与现有方法对比，ShapeGrasp 在所有评估指标上均表现更优。
- **关键数字**：
  - 三指夹爪抓取成功率：84%
  - 两指夹爪抓取成功率：91%
  - 3D形状重建质量在所有评估指标上均有提升

### 结论
ShapeGrasp 是首个在真实世界抓取后更新形状表示的方法，通过迭代融合视觉与触觉信息，显著提升了抓取成功率和形状重建精度。该方法验证了触觉反馈在机器人操作中的关键作用，为复杂环境下的自适应抓取提供了新思路。

## Overview
Humans grasp unfamiliar objects by combining an initial visual estimate with tactile and proprioceptive feedback during interaction. We present ShapeGrasp, a robotic implementation of this approach. The proposed method is an iterative grasp-and-complete pipeline that couples implicit surface visuo-haptic shape completion (creation of full 3D shape from partial information) with physics-based grasp planning. From a single RGB-D view, ShapeGrasp infers a complete shape (point cloud or triangular mesh), generates candidate grasps via rigid-body simulation, and executes the best feasible grasp. Each grasp attempt yields additional geometric constraints -- tactile surface contacts and space occupied by the gripper body -- which are fused to update the object shape. Failures trigger pose re-estimation and regrasping using the refined shape. We evaluate ShapeGrasp in the real world using two different robots and grippers. To the best of our knowledge, this is the first approach that updates shape representations following a real-world grasp. We achieved superior results over baselines for both grippers (grasp success rate of 84% with a three-finger gripper and 91% with a two-finger gripper), while improving the 3D shape reconstruction quality in all evaluation metrics used.

## 参考
- http://arxiv.org/abs/2605.02347v2

## 개요
ShapeGrasp는 인간이 익숙하지 않은 물체를 잡을 때의 전략을 모방하여, 초기 시각적 추정과 상호작용 중의 촉각 및 고유수용성 피드백을 결합합니다. 이 방법은 반복적인 파지 및 형상 완성 파이프라인을 구축하며, 암시적 표면 표현을 사용하여 시각 및 촉각 정보를 융합하고, 단일 RGB-D 이미지에서 완전한 형상을 추론하며, 강체 시뮬레이션을 통해 후보 파지를 생성합니다. 각 파지 시도는 새로운 기하학적 제약(예: 촉각 접촉점 및 그리퍼 점유 공간)을 생성하며, 이 정보는 물체 형상을 업데이트하는 데 사용됩니다. 파지가 실패하면 업데이트된 형상을 기반으로 자세를 다시 추정하고 다시 시도합니다. 실제 로봇에서의 실험은 이 방법이 두 가지 다른 그리퍼에서 기준선보다 우수하며, 모든 평가 지표에서 3D 형상 재구성을 개선함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
ShapeGrasp의 핵심은 반복적인 "파지-완성" 파이프라인으로, 다음 단계를 포함합니다:
- **초기 형상 추론**: 단일 RGB-D 이미지에서 암시적 표면 표현을 사용하여 부분-전체 3D 형상 재구성을 수행하고, 포인트 클라우드 또는 삼각 메시를 출력합니다.
- **파지 계획**: 강체 시뮬레이션을 통해 후보 파지를 생성하고, 실행 가능한 최상의 파지를 선택합니다.
- **촉각-시각 융합 업데이트**: 각 파지 시도는 추가적인 기하학적 제약을 제공하며, 여기에는 촉각 표면 접촉점과 그리퍼 본체가 점유하는 공간이 포함됩니다. 이 정보는 형상 표현에 융합되어 물체 모델을 업데이트합니다.
- **실패 처리**: 파지가 실패하면 업데이트된 형상을 기반으로 물체 자세를 다시 추정하고 재파지를 수행합니다.

### 실험 설정
- **하드웨어**: 두 가지 다른 로봇 및 그리퍼(세 손가락 그리퍼 및 두 손가락 그리퍼)를 사용하여 실제 환경에서 평가합니다.
- **기준선**: 기존 방법과 비교하여 ShapeGrasp는 모든 평가 지표에서 더 우수한 성능을 보입니다.
- **주요 수치**:
  - 세 손가락 그리퍼 파지 성공률: 84%
  - 두 손가락 그리퍼 파지 성공률: 91%
  - 3D 형상 재구성 품질이 모든 평가 지표에서 향상됨

### 결론
ShapeGrasp는 실제 세계에서 파지 후 형상 표현을 업데이트하는 최초의 방법으로, 시각 및 촉각 정보를 반복적으로 융합하여 파지 성공률과 형상 재구성 정확도를 크게 향상시킵니다. 이 방법은 로봇 조작에서 촉각 피드백의 핵심 역할을 검증하며, 복잡한 환경에서의 적응형 파지에 새로운 접근 방식을 제공합니다.
