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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.19124v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (632 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2603.19124v3

## 개요
본 연구는 저비용·맞춤형 연속체 로봇에 초점을 맞추며, 핵심 혁신은 테이퍼형 TPU 골격을 통해 높은 곡률과 원위부 유연성을 구현한 점입니다. 압축력 센서와 액추에이터를 통합하여 시스템이 직접 힘줄 장력을 제어할 수 있습니다. 뉴턴법 기반의 Cosserat 막대 모델은 테이퍼형 골격의 단면 기하 변화를 처음으로 명시적으로 처리하여, 강성 구배 분포를 포착하고 원뿔 각도가 형상 공간과 조작성에 미치는 영향을 분석할 수 있습니다. 모델은 모션 캡처 데이터로 보정된 후, 형상 예측 정확도가 센티미터 수준에 도달했습니다. 또한 내시경 그리퍼를 로봇 본체를 따라 배선하고 6자유도 로봇 팔에 장착한 원격 조작 파지 실험을 시연했습니다.

## 핵심 내용
### 설계 및 제조
- 용융 적층 모델링(FDM) 3D 프린팅 기술로 TPU 테이퍼형 골격을 제조하며, 골격 단면은 길이 방향을 따라 점진적으로 변화합니다.
- 통합 전자 베이스에는 액추에이터와 압축력 센서가 포함되어 힘줄 장력의 폐루프 제어와 실시간 감지를 구현합니다.
- 매개변수화된 iLogic/CAD 스크립트를 제공하여 빠른 기하 생성과 크기 조정을 지원합니다.

### 운동 정역학 모델링
- Cosserat 막대 이론을 기반으로 뉴턴법을 사용하여 일반화된 순방향 운동 정역학 모델을 구축합니다.
- 모델은 테이퍼형 골격의 단면 공간 변화를 명시적으로 고려하여 기존 힘줄 구동 Cosserat 막대 공식을 확장합니다.
- 테이퍼로 인한 강성 구배 분포를 포착하여 원뿔 각도가 로봇의 형상 공간과 조작성에 미치는 영향을 체계적으로 분석합니다.

### 실험 검증
- 모션 캡처 시스템으로 데이터를 수집하고, 라인 서치 방법을 통해 영률을 보정하여 모델링 오차를 최소화합니다.
- 형상 예측 정확도가 센티미터 수준에 도달하여 모델의 유효성을 검증합니다.

### 응용 시연
- 내시경 그리퍼를 연속체 로봇 본체를 따라 배선하고 6자유도 로봇 팔에 장착합니다.
- 원격 조작 파지 작업을 성공적으로 수행하여 유연한 검사와 조작에서의 로봇 잠재력을 보여줍니다.
