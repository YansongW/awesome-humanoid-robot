---
$id: ent_paper_abdolmalaki_development_of_direct_kinemati_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Development of Direct Kinematics and Workspace Representation for Smokie Robot Manipulator & the Barrett WAM
  zh: Smokie机器人机械臂与Barrett WAM的直接运动学与工作空间表示研究
  ko: Smokie 로봇 매니퓰레이터 및 Barrett WAM의 직접운동학과 작업공간 표현 개발
summary:
  en: This paper derives Denavit-Hartenberg parameters and direct-kinematics transformation matrices for the 6-DOF Smokie
    Robot and a 6-DOF configuration of the Barrett WAM, then uses a MATLAB Monte Carlo sampler to visualize their 3-D workspaces
    from multiple views.
  zh: 本文为Smokie Robot与Barrett WAM两款六自由度机械臂推导了Denavit-Hartenberg参数与正运动学变换矩阵，并利用MATLAB蒙特卡洛采样法从多视角可视化其三维工作空间。
  ko: 본 논문은 6자유도 Smokie 로봇과 6자유도 Barrett WAM 구성의 Denavit-Hartenberg 매개변수 및 직접운동학 변환 행렬을 도출한 후, MATLAB 몬테카를로 샘플러를 사용하여 여러 시점에서
    3차원 작업공간을 시각화한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- direct_kinematics
- denavit_hartenberg_parameters
- workspace_representation
- serial_manipulator
- barrett_wam
- smokie_robot
- monte_carlo_sampling
- upper_limb
- motion_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1707.04820v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Development of Direct Kinematics and Workspace Representation for Smokie Robot Manipulator & the Barrett WAM
  url: https://arxiv.org/abs/1707.04820
  date: '2017'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
研究聚焦于两款六自由度机械臂的建模：Smokie Robot与Barrett WAM。首先为每个连杆建立合适的坐标系并确定精确尺寸，从而推导出Denavit-Hartenberg参数。基于这些参数构建变换矩阵后，通过MATLAB编程实现正运动学计算。最后采用蒙特卡洛采样法对工作空间进行三维可视化，从多个视角展示机械臂可达区域。

## 核心内容
### 方法
- 为Smokie Robot与Barrett WAM（六自由度配置）分别建立Denavit-Hartenberg参数，包括每个连杆的坐标系分配与尺寸测量。
- 基于D-H参数推导正运动学变换矩阵，实现从关节空间到笛卡尔空间的映射。

### 实验设置
- 使用MATLAB编程实现运动学计算与工作空间生成。
- 采用蒙特卡洛采样法：在关节角度范围内随机生成大量样本点，通过正运动学变换得到末端执行器位置，从而构建工作空间点云。

### 关键结果
- 成功获得两款机械臂的完整D-H参数表与变换矩阵。
- 三维工作空间可视化从多个视角（如俯视、侧视、等轴测视图）呈现，清晰展示了Smokie Robot与Barrett WAM的可达区域形状与范围。

### 结论
- 所提方法为后续运动学分析、轨迹规划及避障研究提供了基础模型。
- MATLAB蒙特卡洛采样法可有效生成高分辨率工作空间表示，适用于不同构型机械臂的对比分析。

## Overview
This paper discusses modelling two 6 DOF arm robots. The first step of modelling a robot is establishing its Denavit-Hartenberg parameters. It requires assigning proper coordinates for each link and finding their exact dimensions. In this project we will develop the direct kinematics and workspace representations for two manipulators: the Smokie Robot and the Barrett WAM. After finding the D-H parameters and creating Transformation Matrices,MATLAB programming is used to represent their workspaces.

## Overview
This paper discusses modeling two 6 DOF arm robots. The first step of modeling a robot is establishing its Denavit-Hartenberg parameters. It requires assigning proper coordinates for each link and finding their exact dimensions. In this project we will develop the direct kinematics and workspace representations for two manipulators: the Smokie Robot and the Barrett WAM. After finding the D-H parameters and creating Transformation Matrices, MATLAB programming is used to represent their workspaces.

## Content
This paper discusses modeling two 6 DOF arm robots. The first step of modeling a robot is establishing its Denavit-Hartenberg parameters. It requires assigning proper coordinates for each link and finding their exact dimensions. In this project we will develop the direct kinematics and workspace representations for two manipulators: the Smokie Robot and the Barrett WAM. After finding the D-H parameters and creating Transformation Matrices, MATLAB programming is used to represent their workspaces.

## 개요
본 논문은 두 개의 6 자유도(DOF) 암 로봇을 모델링하는 방법에 대해 논의합니다. 로봇 모델링의 첫 번째 단계는 Denavit-Hartenberg 매개변수를 설정하는 것입니다. 이를 위해서는 각 링크에 적절한 좌표를 할당하고 정확한 치수를 찾아야 합니다. 이 프로젝트에서는 Smokie Robot과 Barrett WAM이라는 두 매니퓰레이터의 직접 기구학(direct kinematics)과 작업 공간(workspace) 표현을 개발할 것입니다. D-H 매개변수를 찾고 변환 행렬(Transformation Matrices)을 생성한 후, MATLAB 프로그래밍을 사용하여 이들의 작업 공간을 표현합니다.

## 핵심 내용
본 논문은 두 개의 6 자유도(DOF) 암 로봇을 모델링하는 방법에 대해 논의합니다. 로봇 모델링의 첫 번째 단계는 Denavit-Hartenberg 매개변수를 설정하는 것입니다. 이를 위해서는 각 링크에 적절한 좌표를 할당하고 정확한 치수를 찾아야 합니다. 이 프로젝트에서는 Smokie Robot과 Barrett WAM이라는 두 매니퓰레이터의 직접 기구학(direct kinematics)과 작업 공간(workspace) 표현을 개발할 것입니다. D-H 매개변수를 찾고 변환 행렬(Transformation Matrices)을 생성한 후, MATLAB 프로그래밍을 사용하여 이들의 작업 공간을 표현합니다.

## 参考
- http://arxiv.org/abs/1707.04820v2
