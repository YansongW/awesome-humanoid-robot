---
$id: ent_paper_pro_crisp_compliant_ros2_controlle_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation
  zh: CRISP
  ko: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation
summary:
  en: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (CRISP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Technical University of Munich (TUM), TUM School
    of Computation, Information and Technology.
  zh: CRISP 是慕尼黑工业大学（TUM）于 2025 年提出的轻量级 C++ 控制器实现，专为 ROS2 control 标准设计。其核心贡献在于为基于学习的操控策略（如扩散策略、视觉-语言-动作模型）和遥操作提供统一的低层控制接口，实现平滑的参考轨迹跟踪与柔顺行为。该系统已在
    Franka Robotics FR3 硬件及 Kuka IIWA14、Kinova Gen3 仿真环境中得到验证。
  ko: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (CRISP), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Technical University of Munich (TUM), TUM School
    of Computation, Information and Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- crisp
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06819v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation (arXiv)
  url: https://arxiv.org/abs/2509.06819
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CRISP source
  url: https://doi.org/10.48550/arXiv.2509.06819
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
基于学习的控制器（如扩散策略和视觉-语言-动作模型）常产生低频或不连续的机器人状态变化，需要低层控制器将高层目标指令转换为关节力矩以实现柔顺交互。CRISP 通过轻量级 C++ 实现，为 ROS2 control 标准提供笛卡尔空间与关节空间的柔顺控制器，可无缝集成高层学习策略与遥操作。该系统兼容任何暴露关节力矩接口的机械臂，并通过 Python 和 Gymnasium 接口提供从硬件/仿真数据采集到策略部署的统一流程，显著降低了在 ROS2 兼容机械臂上应用学习方法的门槛。

## 核心内容
### 方法
CRISP 采用轻量级 C++ 实现，针对 ROS2 control 标准设计，提供笛卡尔空间与关节空间的柔顺控制器。其核心功能是将高层学习策略（如扩散策略、视觉-语言-动作模型）生成的低频或非连续目标指令，转换为平滑的关节力矩指令，实现接触交互中的柔顺行为。

### 架构
- **控制器类型**：支持笛卡尔空间与关节空间的柔顺控制，兼容任何暴露关节力矩接口的机械臂。
- **接口设计**：通过 Python 和 Gymnasium 接口提供统一的数据采集与策略执行管线，支持硬件与仿真环境的无缝切换。
- **系统验证**：已在 Franka Robotics FR3 硬件平台、Kuka IIWA14 和 Kinova Gen3 仿真环境中完成验证。

### 实验设置
- **硬件平台**：Franka Robotics FR3（真实机器人）
- **仿真环境**：Kuka IIWA14、Kinova Gen3
- **集成方式**：通过 ROS2 control 标准与高层学习策略及遥操作接口对接

### 关键数字
- 控制器实现为轻量级 C++ 代码，专为实时性能优化
- 提供统一的数据采集与策略执行管线，支持快速实验迭代
- 详细文档与开源代码已发布于项目网站：https://utiasDSL.github.io/crisp_controllers

### 结论
CRISP 通过提供标准化的低层控制接口，有效降低了在 ROS2 兼容机械臂上应用基于学习方法（如扩散策略、视觉-语言-动作模型）的难度。其轻量级设计与统一管线特性，为机器人操控领域的快速实验与部署提供了实用工具。

## Overview
Learning-based controllers, such as diffusion policies and vision-language action models, often generate low-frequency or discontinuous robot state changes. Achieving smooth reference tracking requires a low-level controller that converts high-level targets commands into joint torques, enabling compliant behavior during contact interactions. We present CRISP, a lightweight C++ implementation of compliant Cartesian and joint-space controllers for the ROS2 control standard, designed for seamless integration with high-level learning-based policies as well as teleoperation. The controllers are compatible with any manipulator that exposes a joint-torque interface. Through our Python and Gymnasium interfaces, CRISP provides a unified pipeline for recording data from hardware and simulation and deploying high-level learning-based policies seamlessly, facilitating rapid experimentation. The system has been validated on hardware with the Franka Robotics FR3 and in simulation with the Kuka IIWA14 and Kinova Gen3. Designed for rapid integration, flexible deployment, and real-time performance, our implementation provides a unified pipeline for data collection and policy execution, lowering the barrier to applying learning-based methods on ROS2-compatible manipulators. Detailed documentation is available at the project website - https://utiasDSL.github.io/crisp_controllers.

## Overview
Learning-based controllers, such as diffusion policies and vision-language action models, often generate low-frequency or discontinuous robot state changes. Achieving smooth reference tracking requires a low-level controller that converts high-level target commands into joint torques, enabling compliant behavior during contact interactions. We present CRISP, a lightweight C++ implementation of compliant Cartesian and joint-space controllers for the ROS2 control standard, designed for seamless integration with high-level learning-based policies as well as teleoperation. The controllers are compatible with any manipulator that exposes a joint-torque interface. Through our Python and Gymnasium interfaces, CRISP provides a unified pipeline for recording data from hardware and simulation and deploying high-level learning-based policies seamlessly, facilitating rapid experimentation. The system has been validated on hardware with the Franka Robotics FR3 and in simulation with the Kuka IIWA14 and Kinova Gen3. Designed for rapid integration, flexible deployment, and real-time performance, our implementation provides a unified pipeline for data collection and policy execution, lowering the barrier to applying learning-based methods on ROS2-compatible manipulators. Detailed documentation is available at the project website - https://utiasDSL.github.io/crisp_controllers.

## Content
Learning-based controllers, such as diffusion policies and vision-language action models, often generate low-frequency or discontinuous robot state changes. Achieving smooth reference tracking requires a low-level controller that converts high-level target commands into joint torques, enabling compliant behavior during contact interactions. We present CRISP, a lightweight C++ implementation of compliant Cartesian and joint-space controllers for the ROS2 control standard, designed for seamless integration with high-level learning-based policies as well as teleoperation. The controllers are compatible with any manipulator that exposes a joint-torque interface. Through our Python and Gymnasium interfaces, CRISP provides a unified pipeline for recording data from hardware and simulation and deploying high-level learning-based policies seamlessly, facilitating rapid experimentation. The system has been validated on hardware with the Franka Robotics FR3 and in simulation with the Kuka IIWA14 and Kinova Gen3. Designed for rapid integration, flexible deployment, and real-time performance, our implementation provides a unified pipeline for data collection and policy execution, lowering the barrier to applying learning-based methods on ROS2-compatible manipulators. Detailed documentation is available at the project website - https://utiasDSL.github.io/crisp_controllers.

## 개요
학습 기반 제어기(예: 확산 정책 및 시각-언어 행동 모델)는 종종 저주파수 또는 불연속적인 로봇 상태 변화를 생성합니다. 원활한 참조 추적을 위해서는 고수준 목표 명령을 관절 토크로 변환하여 접촉 상호작용 중 순응적 동작을 가능하게 하는 저수준 제어기가 필요합니다. 본 논문에서는 ROS2 제어 표준을 위한 순응형 카르테시안 및 관절 공간 제어기의 경량 C++ 구현인 CRISP를 제시합니다. 이는 고수준 학습 기반 정책 및 원격 조작과의 원활한 통합을 위해 설계되었습니다. 이 제어기는 관절 토크 인터페이스를 제공하는 모든 매니퓰레이터와 호환됩니다. Python 및 Gymnasium 인터페이스를 통해 CRISP는 하드웨어 및 시뮬레이션에서 데이터를 기록하고 고수준 학습 기반 정책을 원활하게 배포하는 통합 파이프라인을 제공하여 신속한 실험을 촉진합니다. 이 시스템은 Franka Robotics FR3 하드웨어와 Kuka IIWA14 및 Kinova Gen3 시뮬레이션에서 검증되었습니다. 신속한 통합, 유연한 배포 및 실시간 성능을 위해 설계된 본 구현은 데이터 수집 및 정책 실행을 위한 통합 파이프라인을 제공하여 ROS2 호환 매니퓰레이터에 학습 기반 방법을 적용하는 장벽을 낮춥니다. 자세한 문서는 프로젝트 웹사이트(https://utiasDSL.github.io/crisp_controllers)에서 확인할 수 있습니다.

## 핵심 내용
학습 기반 제어기(예: 확산 정책 및 시각-언어 행동 모델)는 종종 저주파수 또는 불연속적인 로봇 상태 변화를 생성합니다. 원활한 참조 추적을 위해서는 고수준 목표 명령을 관절 토크로 변환하여 접촉 상호작용 중 순응적 동작을 가능하게 하는 저수준 제어기가 필요합니다. 본 논문에서는 ROS2 제어 표준을 위한 순응형 카르테시안 및 관절 공간 제어기의 경량 C++ 구현인 CRISP를 제시합니다. 이는 고수준 학습 기반 정책 및 원격 조작과의 원활한 통합을 위해 설계되었습니다. 이 제어기는 관절 토크 인터페이스를 제공하는 모든 매니퓰레이터와 호환됩니다. Python 및 Gymnasium 인터페이스를 통해 CRISP는 하드웨어 및 시뮬레이션에서 데이터를 기록하고 고수준 학습 기반 정책을 원활하게 배포하는 통합 파이프라인을 제공하여 신속한 실험을 촉진합니다. 이 시스템은 Franka Robotics FR3 하드웨어와 Kuka IIWA14 및 Kinova Gen3 시뮬레이션에서 검증되었습니다. 신속한 통합, 유연한 배포 및 실시간 성능을 위해 설계된 본 구현은 데이터 수집 및 정책 실행을 위한 통합 파이프라인을 제공하여 ROS2 호환 매니퓰레이터에 학습 기반 방법을 적용하는 장벽을 낮춥니다. 자세한 문서는 프로젝트 웹사이트(https://utiasDSL.github.io/crisp_controllers)에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2509.06819v2
