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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.06819v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (968 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.06819v2

## 개요
학습 기반 컨트롤러(예: 확산 정책, 비전-언어-행동 모델)는 종종 저주파 또는 불연속적인 로봇 상태 변화를 생성하므로, 고수준 목표 명령을 관절 토크로 변환하여 유연한 상호작용을 구현하는 저수준 컨트롤러가 필요합니다. CRISP는 경량 C++ 구현을 통해 ROS2 control 표준에 맞는 데카르트 공간 및 관절 공간의 유연한 컨트롤러를 제공하며, 고수준 학습 정책 및 원격 조작과 원활하게 통합할 수 있습니다. 이 시스템은 관절 토크 인터페이스를 노출하는 모든 로봇 팔과 호환되며, Python 및 Gymnasium 인터페이스를 통해 하드웨어/시뮬레이션 데이터 수집부터 정책 배포까지의 통합 워크플로우를 제공하여 ROS2 호환 로봇 팔에 학습 방법을 적용하는 진입 장벽을 크게 낮춥니다.

## 핵심 내용
### 방법
CRISP는 경량 C++ 구현을 채택하여 ROS2 control 표준을 위해 설계되었으며, 데카르트 공간 및 관절 공간의 유연한 컨트롤러를 제공합니다. 핵심 기능은 고수준 학습 정책(예: 확산 정책, 비전-언어-행동 모델)이 생성하는 저주파 또는 비연속 목표 명령을 부드러운 관절 토크 명령으로 변환하여 접촉 상호작용에서 유연한 동작을 구현하는 것입니다.

### 아키텍처
- **컨트롤러 유형**: 데카르트 공간 및 관절 공간의 유연한 제어를 지원하며, 관절 토크 인터페이스를 노출하는 모든 로봇 팔과 호환됩니다.
- **인터페이스 설계**: Python 및 Gymnasium 인터페이스를 통해 통합 데이터 수집 및 정책 실행 파이프라인을 제공하며, 하드웨어와 시뮬레이션 환경 간의 원활한 전환을 지원합니다.
- **시스템 검증**: Franka Robotics FR3 하드웨어 플랫폼, Kuka IIWA14 및 Kinova Gen3 시뮬레이션 환경에서 검증이 완료되었습니다.

### 실험 설정
- **하드웨어 플랫폼**: Franka Robotics FR3 (실제 로봇)
- **시뮬레이션 환경**: Kuka IIWA14, Kinova Gen3
- **통합 방식**: ROS2 control 표준을 통해 고수준 학습 정책 및 원격 조작 인터페이스와 연결

### 주요 수치
- 컨트롤러는 실시간 성능 최적화를 위해 설계된 경량 C++ 코드로 구현됨
- 통합 데이터 수집 및 정책 실행 파이프라인을 제공하여 빠른 실험 반복 지원
- 상세 문서 및 오픈 소스 코드는 프로젝트 웹사이트에서 공개: https://utiasDSL.github.io/crisp_controllers

### 결론
CRISP는 표준화된 저수준 제어 인터페이스를 제공함으로써 ROS2 호환 로봇 팔에 학습 기반 방법(예: 확산 정책, 비전-언어-행동 모델)을 적용하는 난이도를 효과적으로 낮춥니다. 경량 설계와 통합 파이프라인 특성은 로봇 조작 분야의 빠른 실험 및 배포를 위한 실용적인 도구를 제공합니다.
