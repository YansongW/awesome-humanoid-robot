---
$id: ent_paper_tendon_actuated_robots_with_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Tendon-Actuated Robots with a Tapered, Flexible Polymer Backbone: Design, Fabrication, and Modeling'
  zh: 'Tendon-Actuated Robots with a Tapered, Flexible Polymer Backbone: Design, Fabrication, and Modeling'
  ko: 'Tendon-Actuated Robots with a Tapered, Flexible Polymer Backbone: Design, Fabrication, and Modeling'
summary:
  en: 'arXiv:2603.19124v3 Announce Type: replace Abstract: This paper presents the design, modeling, and fabrication of 3D-printed,
    tendon-actuated continuum robots featuring a flexible, tapered backbone constructed from thermoplastic polyurethane (TPU).
    Our scalable design incorporates an integrated electronics base housing that enables direct tendon tension control and
    sensing via actuators and compression load cells. Unlike many continuum robots that are single-purpose and costly, the
    proposed design prioritizes customizability, rapid assembly, and low cost while enabling high curvature and enhanced distal
    compliance through geometric tapering, thereby supporting a broad range of compliant robotic inspection and manipulation
    tasks. We develop a generalized forward kinetostatic model of the tapered backbone based on Cosserat rod theory using
    a Newtonian approach, extending existing tendon-actuated Cosserat rod formulations to explicitly account for spatially
    varying backbone cross-sectional geometry. The model captures the graded stiffness profile induced by the tapering and
    enables systematic exploration of the configuration space as a function of the geometric design parameters. Specifically,
    we analyze how the backbone taper angle influences the robot''s configuration space and manipulability. The model is validated
    against motion capture data, achieving centimeter-level shape prediction accuracy after calibrating Young''s modulus via
    a line search that minimizes modeling error. We further demonstrate teleoperated grasping using an endoscopic gripper
    routed along the continuum robot, mounted on a 6-DoF robotic arm. Parameterized iLogic/CAD scripts are provided for rapid
    geometry generation and scaling. The presented framework establishes a simple, rapid, and reproducible pathway from parametric
    design to controlled tendon actuation for tapered, tendon-driven continuum robots manufactured using fused deposition
    modeling 3D printers.'
  zh: 本文提出了一种基于热塑性聚氨酯（TPU）柔性锥形骨架的3D打印肌腱驱动连续体机器人设计。该设计通过集成电子底座实现肌腱张力直接控制与传感，并基于Cosserat杆理论建立了考虑截面空间变化的广义正向运动静力学模型。实验验证了模型在厘米级形状预测精度下的有效性，并展示了远程操作抓取能力。
  ko: 'arXiv:2603.19124v3 Announce Type: replace Abstract: This paper presents the design, modeling, and fabrication of 3D-printed,
    tendon-actuated continuum robots featuring a flexible, tapered backbone constructed from thermoplastic polyurethane (TPU).
    Our scalable design incorporates an integrated electronics base housing that enables direct tendon tension control and
    sensing via actuators and compression load cells. Unlike many continuum robots that are single-purpose and costly, the
    proposed design prioritizes customizability, rapid assembly, and low cost while enabling high curvature and enhanced distal
    compliance through geometric tapering, thereby supporting a broad range of compliant robotic inspection and manipulation
    tasks. We develop a generalized forward kinetostatic model of the tapered backbone based on Cosserat rod theory using
    a Newtonian approach, extending existing tendon-actuated Cosserat rod formulations to explicitly account for spatially
    varying backbone cross-sectional geometry. The model captures the graded stiffness profile induced by the tapering and
    enables systematic exploration of the configuration space as a function of the geometric design parameters. Specifically,
    we analyze how the backbone taper angle influences the robot''s configuration space and manipulability. The model is validated
    against motion capture data, achieving centimeter-level shape prediction accuracy after calibrating Young''s modulus via
    a line search that minimizes modeling error. We further demonstrate teleoperated grasping using an endoscopic gripper
    routed along the continuum robot, mounted on a 6-DoF robotic arm. Parameterized iLogic/CAD scripts are provided for rapid
    geometry generation and scaling. The presented framework establishes a simple, rapid, and reproducible pathway from parametric
    design to controlled tendon actuation for tapered, tendon-driven continuum robots manufactured using fused deposition
    modeling 3D printers.'
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
- tendon_actuated_robots_with_a
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.19124v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Tendon-Actuated Robots with a Tapered, Flexible Polymer Backbone: Design, Fabrication, and Modeling (arXiv)'
  url: https://arxiv.org/abs/2603.19124
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
该研究聚焦于低成本、可定制的连续体机器人，其核心创新在于采用锥形TPU骨架实现高曲率与远端柔顺性。通过集成压缩力传感器与执行器，系统可直接控制肌腱张力。基于牛顿法的Cosserat杆模型首次显式处理了锥形骨架的截面几何变化，能够捕捉刚度梯度分布并分析锥角对构型空间与可操作性的影响。模型经运动捕捉数据校准后，形状预测精度达厘米级。研究还展示了将内窥镜夹爪沿机器人本体布线并安装于6自由度机械臂的远程操作抓取实验。

## 核心内容
### 设计与制造
- 采用熔融沉积成型（FDM）3D打印技术制造TPU锥形骨架，骨架截面沿长度方向渐变。
- 集成电子底座包含执行器与压缩力传感器，实现肌腱张力的闭环控制与实时感知。
- 提供参数化iLogic/CAD脚本，支持快速几何生成与尺寸缩放。

### 运动静力学建模
- 基于Cosserat杆理论，采用牛顿法建立广义正向运动静力学模型。
- 模型显式考虑锥形骨架的截面空间变化，扩展了现有肌腱驱动Cosserat杆公式。
- 通过捕捉锥形引起的刚度梯度分布，系统分析锥角对机器人构型空间与可操作性的影响。

### 实验验证
- 使用运动捕捉系统采集数据，通过线搜索法校准杨氏模量以最小化建模误差。
- 形状预测精度达到厘米级，验证了模型的有效性。

### 应用演示
- 将内窥镜夹爪沿连续体机器人本体布线，并安装于6自由度机械臂。
- 成功实现远程操作抓取任务，展示了机器人在柔顺检测与操作中的潜力。

## Overview
This paper presents the design, modeling, and fabrication of 3D-printed, tendon-actuated continuum robots featuring a flexible, tapered backbone constructed from thermoplastic polyurethane (TPU). Our scalable design incorporates an integrated electronics base housing that enables direct tendon tension control and sensing via actuators and compression load cells. Unlike many continuum robots that are single-purpose and costly, the proposed design prioritizes customizability, rapid assembly, and low cost while enabling high curvature and enhanced distal compliance through geometric tapering, thereby supporting a broad range of compliant robotic inspection and manipulation tasks. We develop a generalized forward kinetostatic model of the tapered backbone based on Cosserat rod theory using a Newtonian approach, extending existing tendon-actuated Cosserat rod formulations to explicitly account for spatially varying backbone cross-sectional geometry. The model captures the graded stiffness profile induced by the tapering and enables systematic exploration of the configuration space as a function of the geometric design parameters. Specifically, we analyze how the backbone taper angle influences the robot's configuration space and manipulability. The model is validated against motion capture data, achieving centimeter-level shape prediction accuracy after calibrating Young's modulus via a line search that minimizes modeling error. We further demonstrate teleoperated grasping using an endoscopic gripper routed along the continuum robot, mounted on a 6-DoF robotic arm. Parameterized iLogic/CAD scripts are provided for rapid geometry generation and scaling. The presented framework establishes a simple, rapid, and reproducible pathway from parametric design to controlled tendon actuation for tapered, tendon-driven continuum robots manufactured using fused deposition modeling 3D printers.

## 개요
본 논문은 열가소성 폴리우레탄(TPU)으로 제작된 유연하고 테이퍼진 백본을 특징으로 하는 3D 프린팅 텐던 구동 연속체 로봇의 설계, 모델링 및 제작을 제시합니다. 확장 가능한 설계에는 액추에이터와 압축 로드셀을 통해 직접적인 텐던 장력 제어 및 감지를 가능하게 하는 통합 전자 기반 하우징이 포함됩니다. 단일 목적에 고비용인 많은 연속체 로봇과 달리, 제안된 설계는 맞춤화, 신속한 조립 및 저비용을 우선시하면서 기하학적 테이퍼링을 통해 높은 곡률과 향상된 말단 순응성을 가능하게 하여 광범위한 순응형 로봇 검사 및 조작 작업을 지원합니다. 우리는 뉴턴 접근법을 사용하여 Cosserat 막대 이론에 기반한 테이퍼진 백본의 일반화된 순방향 운동정역학 모델을 개발하며, 기존의 텐던 구동 Cosserat 막대 공식을 확장하여 공간적으로 변화하는 백본 단면 형상을 명시적으로 고려합니다. 이 모델은 테이퍼링에 의해 유도된 점진적 강성 프로파일을 포착하고 기하학적 설계 매개변수의 함수로서 구성 공간의 체계적 탐색을 가능하게 합니다. 특히, 백본 테이퍼 각도가 로봇의 구성 공간과 조작성에 미치는 영향을 분석합니다. 모델은 모션 캡처 데이터에 대해 검증되었으며, 모델링 오차를 최소화하는 선 탐색을 통해 영률을 보정한 후 센티미터 수준의 형상 예측 정확도를 달성합니다. 또한 6자유도 로봇 팔에 장착된 연속체 로봇을 따라 경로가 설정된 내시경 그리퍼를 사용한 원격 조작 파지를 시연합니다. 신속한 형상 생성 및 스케일링을 위한 매개변수화된 iLogic/CAD 스크립트가 제공됩니다. 제시된 프레임워크는 용융 증착 모델링 3D 프린터로 제조된 테이퍼진 텐던 구동 연속체 로봇을 위한 매개변수 설계에서 제어된 텐던 구동까지의 간단하고 신속하며 재현 가능한 경로를 확립합니다.

## 핵심 내용
본 논문은 열가소성 폴리우레탄(TPU)으로 제작된 유연하고 테이퍼진 백본을 특징으로 하는 3D 프린팅 텐던 구동 연속체 로봇의 설계, 모델링 및 제작을 제시합니다. 확장 가능한 설계에는 액추에이터와 압축 로드셀을 통해 직접적인 텐던 장력 제어 및 감지를 가능하게 하는 통합 전자 기반 하우징이 포함됩니다. 단일 목적에 고비용인 많은 연속체 로봇과 달리, 제안된 설계는 맞춤화, 신속한 조립 및 저비용을 우선시하면서 기하학적 테이퍼링을 통해 높은 곡률과 향상된 말단 순응성을 가능하게 하여 광범위한 순응형 로봇 검사 및 조작 작업을 지원합니다. 우리는 뉴턴 접근법을 사용하여 Cosserat 막대 이론에 기반한 테이퍼진 백본의 일반화된 순방향 운동정역학 모델을 개발하며, 기존의 텐던 구동 Cosserat 막대 공식을 확장하여 공간적으로 변화하는 백본 단면 형상을 명시적으로 고려합니다. 이 모델은 테이퍼링에 의해 유도된 점진적 강성 프로파일을 포착하고 기하학적 설계 매개변수의 함수로서 구성 공간의 체계적 탐색을 가능하게 합니다. 특히, 백본 테이퍼 각도가 로봇의 구성 공간과 조작성에 미치는 영향을 분석합니다. 모델은 모션 캡처 데이터에 대해 검증되었으며, 모델링 오차를 최소화하는 선 탐색을 통해 영률을 보정한 후 센티미터 수준의 형상 예측 정확도를 달성합니다. 또한 6자유도 로봇 팔에 장착된 연속체 로봇을 따라 경로가 설정된 내시경 그리퍼를 사용한 원격 조작 파지를 시연합니다. 신속한 형상 생성 및 스케일링을 위한 매개변수화된 iLogic/CAD 스크립트가 제공됩니다. 제시된 프레임워크는 용융 증착 모델링 3D 프린터로 제조된 테이퍼진 텐던 구동 연속체 로봇을 위한 매개변수 설계에서 제어된 텐던 구동까지의 간단하고 신속하며 재현 가능한 경로를 확립합니다.

## 参考
- http://arxiv.org/abs/2603.19124v3
