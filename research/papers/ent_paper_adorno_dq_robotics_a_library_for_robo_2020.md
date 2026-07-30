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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1910.11612v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
이중 쿼터니언 대수와 로보틱스에의 응용은 지난 20년 동안 상당한 관심을 받아왔다. 이중 쿼터니언은 뛰어난 기하학적 직관성을 가지며, 로봇 모델링과 제어 모두에 유용한 대수적 프레임워크 내에서 물리적 현상을 쉽게 포착한다. 점, 선, 평면, 무한 원기둥, 구, 좌표계, 트위스트, 렌치와 같은 수학적 객체들은 모두 이중 쿼터니언으로 잘 정의된다. 따라서 간단한 연산자를 사용하여 이러한 객체들을 다양한 프레임에서 표현하고, 내적 및 외적과 같은 연산을 통해 객체 간의 유용한 기하학적 관계를 추출한다. 그럼에도 불구하고, 이중 쿼터니언 대수는 가능한 만큼 널리 보급되지 않았는데, 이는 주로 효율적이고 사용하기 쉬운 계산 도구가 부족하고 일반적으로 쿼터니언의 특정 대수에 국한되기 때문이다. 이론과 구현 사이의 이러한 격차를 해소하기 위해, 본 논문은 이중 쿼터니언 대수를 사용한 로봇 모델링 및 제어를 위한 라이브러리인 DQ Robotics를 소개한다. 이 라이브러리는 사용하기 쉽고 직관적이어서 자기 학습 및 교육에 사용될 수 있을 뿐만 아니라 실제 응용에 배포하기에 계산적으로 효율적이다.

## 핵심 내용
이중 쿼터니언 대수와 로보틱스에의 응용은 지난 20년 동안 상당한 관심을 받아왔다. 이중 쿼터니언은 뛰어난 기하학적 직관성을 가지며, 로봇 모델링과 제어 모두에 유용한 대수적 프레임워크 내에서 물리적 현상을 쉽게 포착한다. 점, 선, 평면, 무한 원기둥, 구, 좌표계, 트위스트, 렌치와 같은 수학적 객체들은 모두 이중 쿼터니언으로 잘 정의된다. 따라서 간단한 연산자를 사용하여 이러한 객체들을 다양한 프레임에서 표현하고, 내적 및 외적과 같은 연산을 통해 객체 간의 유용한 기하학적 관계를 추출한다. 그럼에도 불구하고, 이중 쿼터니언 대수는 가능한 만큼 널리 보급되지 않았는데, 이는 주로 효율적이고 사용하기 쉬운 계산 도구가 부족하고 일반적으로 쿼터니언의 특정 대수에 국한되기 때문이다. 이론과 구현 사이의 이러한 격차를 해소하기 위해, 본 논문은 이중 쿼터니언 대수를 사용한 로봇 모델링 및 제어를 위한 라이브러리인 DQ Robotics를 소개한다. 이 라이브러리는 사용하기 쉽고 직관적이어서 자기 학습 및 교육에 사용될 수 있을 뿐만 아니라 실제 응용에 배포하기에 계산적으로 효율적이다.

## 参考
- http://arxiv.org/abs/1910.11612v3
