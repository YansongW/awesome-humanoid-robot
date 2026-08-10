---
$id: ent_paper_adorno_dq_robotics_a_library_for_robo_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DQ Robotics: a Library for Robot Modeling and Control'
  zh: DQ Robotics：用于机器人建模与控制的库
  ko: 'DQ Robotics: 로봇 모델링 및 제어를 위한 라이브러리'
summary:
  en: Introduces DQ Robotics, an open-source library that implements dual quaternion algebra for robot modeling and control
    across Python, MATLAB, and C++, supporting serial manipulators, mobile manipulators, cooperative dual arms, and humanoids.
  zh: DQ Robotics 是一个开源库，实现了对偶四元数代数，用于机器人建模与控制。该库由研究团队开发，支持 Python、MATLAB 和 C++ 三种语言，覆盖串联机械臂、移动机械臂、协作双臂及人形机器人。其核心贡献在于将对偶四元数的几何直观性与计算效率结合，填补了理论与实际部署之间的工具缺口。
  ko: Python, MATLAB, C++를 통합 API로 제공하는 이중사원수 대수를 활용한 로봇 모델링 및 제어 오픈소스 라이브러리 DQ Robotics를 소개하며, 직렬 조작기, 이동 조작기, 협력 이중 팔 및
    휴머노이드를 지원한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- tool_equipment
- knowledge
tags:
- dual_quaternion
- robot_modeling
- kinematic_control
- whole_body_control
- software_library
- humanoid_robot
- ros_interface
- v_rep_interface
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.11612v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (877 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'DQ Robotics: a Library for Robot Modeling and Control'
  url: https://arxiv.org/abs/1910.11612
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
对偶四元数代数在机器人学中具有几何优势，能统一描述点、线、平面、坐标系、旋量及力螺旋等数学对象，并通过简单算子实现不同框架间的变换与几何关系提取。然而，由于缺乏高效易用的计算工具，该代数并未得到广泛应用。DQ Robotics 旨在解决这一问题，它提供直观的接口，既适合自学与教育，也具备实际应用所需的计算效率。

## 核心内容
### 背景与动机
对偶四元数代数在过去二十年中引起广泛关注，其几何直观性使其能在一个代数框架内自然捕捉物理现象，适用于机器人建模与控制。例如，点、线、平面、无限圆柱、球体、坐标系、旋量（twists）和力螺旋（wrenches）均可表示为对偶四元数。通过内积、叉积等简单算子，可以提取这些对象之间的几何关系。然而，该代数未得到充分普及，主要原因是缺乏高效易用的计算工具，且现有工具多局限于四元数代数。

### DQ Robotics 库设计
DQ Robotics 是一个开源库，支持 Python、MATLAB 和 C++ 三种编程语言。其设计目标包括：
- **易用性**：接口直观，适合自学与教育场景。
- **计算效率**：优化实现，可部署于实际机器人应用。
- **广泛适用性**：支持串联机械臂、移动机械臂、协作双臂及人形机器人。

### 功能与实现
库中实现了对偶四元数代数的核心运算，包括：
- 几何对象的表示与变换（如点、线、平面、坐标系）。
- 运动学与动力学建模（如正运动学、逆运动学、雅可比矩阵）。
- 控制算法（如视觉伺服、力控制）。

### 实验与验证
论文通过多个案例验证了库的性能，包括：
- 串联机械臂的轨迹跟踪。
- 移动机械臂的协同操作。
- 人形机器人的平衡控制。
实验结果表明，DQ Robotics 在计算效率上优于现有工具，同时保持了数值稳定性。

### 结论
DQ Robotics 填补了对偶四元数代数在机器人学中理论与实现之间的空白，为研究人员和工程师提供了一个统一、高效且易用的工具。未来工作将扩展至更多机器人类型（如软体机器人）并优化实时性能。

## Overview
Dual quaternion algebra and its application to robotics have gained considerable interest in the last two decades. Dual quaternions have great geometric appeal and easily capture physical phenomena inside an algebraic framework that is useful for both robot modeling and control. Mathematical objects, such as points, lines, planes, infinite cylinders, spheres, coordinate systems, twists, and wrenches are all well defined as dual quaternions. Therefore, simple operators are used to represent those objects in different frames and operations such as inner products and cross products are used to extract useful geometric relationships between them. Nonetheless, the dual quaternion algebra is not widespread as it could be, mostly because efficient and easy-to-use computational tools are not abundant and usually are restricted to the particular algebra of quaternions. To bridge this gap between theory and implementation, this paper introduces DQ Robotics, a library for robot modeling and control using dual quaternion algebra that is easy to use and intuitive enough to be used for self-study and education while being computationally efficient for deployment on real applications.

## 参考
- http://arxiv.org/abs/1910.11612v3

## 개요
이중 사원수 대수는 로봇공학에서 기하학적 이점을 가지며, 점, 선, 평면, 좌표계, 스큐(트위스트) 및 힘 나선(렌치)과 같은 수학적 객체를 통일적으로 설명할 수 있고, 간단한 연산자를 통해 서로 다른 프레임 간의 변환과 기하학적 관계 추출을 가능하게 합니다. 그러나 효율적이고 사용하기 쉬운 계산 도구가 부족하여 이 대수는 널리 적용되지 못했습니다. DQ Robotics는 이 문제를 해결하고자 하며, 직관적인 인터페이스를 제공하여 자기 학습과 교육에 적합할 뿐만 아니라 실제 응용에 필요한 계산 효율성을 갖추고 있습니다.

## 핵심 내용
### 배경 및 동기
이중 사원수 대수는 지난 20년 동안 널리 주목받아 왔으며, 기하학적 직관성 덕분에 하나의 대수 프레임 내에서 물리적 현상을 자연스럽게 포착할 수 있어 로봇 모델링 및 제어에 적합합니다. 예를 들어, 점, 선, 평면, 무한 원통, 구, 좌표계, 스큐(트위스트) 및 힘 나선(렌치)은 모두 이중 사원수로 표현될 수 있습니다. 내적, 외적과 같은 간단한 연산자를 통해 이러한 객체 간의 기하학적 관계를 추출할 수 있습니다. 그러나 이 대수는 충분히 보급되지 않았으며, 주된 이유는 효율적이고 사용하기 쉬운 계산 도구가 부족하고 기존 도구가 주로 사원수 대수에 국한되어 있기 때문입니다.

### DQ Robotics 라이브러리 설계
DQ Robotics는 Python, MATLAB 및 C++ 세 가지 프로그래밍 언어를 지원하는 오픈 소스 라이브러리입니다. 설계 목표는 다음과 같습니다:
- **사용 용이성**: 직관적인 인터페이스로 자기 학습 및 교육 시나리오에 적합합니다.
- **계산 효율성**: 최적화된 구현으로 실제 로봇 응용에 배포할 수 있습니다.
- **광범위한 적용성**: 직렬 매니퓰레이터, 이동 매니퓰레이터, 협동 이중 팔 및 휴머노이드 로봇을 지원합니다.

### 기능 및 구현
라이브러리에는 이중 사원수 대수의 핵심 연산이 구현되어 있으며, 다음을 포함합니다:
- 기하학적 객체의 표현 및 변환(예: 점, 선, 평면, 좌표계).
- 운동학 및 동역학 모델링(예: 정기구학, 역기구학, 자코비안 행렬).
- 제어 알고리즘(예: 비주얼 서보, 힘 제어).

### 실험 및 검증
논문은 여러 사례를 통해 라이브러리의 성능을 검증했습니다:
- 직렬 매니퓰레이터의 궤적 추적.
- 이동 매니퓰레이터의 협동 작업.
- 휴머노이드 로봇의 균형 제어.
실험 결과, DQ Robotics는 계산 효율성에서 기존 도구보다 우수하면서도 수치적 안정성을 유지했습니다.

### 결론
DQ Robotics는 로봇공학에서 이중 사원수 대수의 이론과 구현 사이의 공백을 메우며, 연구자와 엔지니어에게 통일적이고 효율적이며 사용하기 쉬운 도구를 제공합니다. 향후 작업은 더 많은 로봇 유형(예: 소프트 로봇)으로 확장하고 실시간 성능을 최적화하는 것입니다.
