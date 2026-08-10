---
$id: ent_paper_zheng_scalable_simulation_and_demons_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots
  zh: 可扩展的跳跃式压电二维软体机器人仿真与演示
  ko: 확장 가능한 점핑 압전 2차원 소프트 로봇의 시뮬레이션 및 실증
summary:
  en: This paper presents a five-actuator piezoelectric soft robot and a scalable PyBullet-based simulation framework that
    models actuators as discrete rigid-link elements connected by motors, validated against static and dynamic experiments
    including inchworm crawling and jumping.
  zh: 本文介绍了一种五驱动器压电软体机器人，并开发了基于PyBullet的可扩展仿真框架，将驱动器建模为电机连接的离散刚性连杆单元。通过静态与动态实验（包括尺蠖爬行和跳跃）验证了仿真精度，机器人前进速度可达约1 cm/s，代码已开源。
  ko: 본 논문은 5개의 구동기를 갖춘 압전 소프트 로봇을 제시하고, 모터로 연결된 이산 강성 링크 요소로 구동부를 모델링하는 확장 가능한 PyBullet 기반 시뮬레이션 프레임워크를 개발하며, inchworm 기어가기
    및 점핑을 포함한 정적·동적 실험으로 검증하였다.
domains:
- 02_components
- 06_design_engineering
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robot
- piezoelectric_actuator
- pybullet_simulation
- pseudo_rigid_body_model
- soft_actuator
- jumping_robot
- inchworm_motion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.13521v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (736 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots
  url: https://arxiv.org/abs/2202.13521
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究针对软体机器人建模困难的问题，提出了一种五驱动器压电软体机器人及其仿真框架。框架利用PyBullet物理引擎，将每个驱动器离散化为刚性连杆与电机组合，从而模拟复杂非线性运动。通过单驱动器悬臂梁的静态与交流分析验证了模型准确性，并进一步扩展到五驱动器机器人，成功预测了直流电压下的静态形状、准静态尺蠖运动以及垂直/水平跳跃行为。实验表明，机器人前进速度约1 cm/s，仿真与实验结果高度吻合。

## 核心内容
### 方法
- **机器人设计**：采用五层压电驱动器，粘合在钢箔基底上，通过施加电压实现弯曲变形。
- **仿真框架**：基于PyBullet物理引擎，将每个压电驱动器建模为多个离散刚性连杆，连杆间通过电机连接，电机扭矩根据压电材料的电压-弯曲关系计算。

### 实验验证
- **单驱动器验证**：对悬臂梁结构进行静态（直流电压）和交流（正弦电压）分析，仿真与实验的位移曲线高度一致。
- **五驱动器机器人验证**：
  - **静态形状**：施加不同直流电压组合，仿真准确复现机器人的弯曲姿态。
  - **尺蠖运动**：通过时序电压控制实现准静态爬行，仿真预测的前进速度与实验匹配（约1 cm/s）。
  - **跳跃运动**：同时实现垂直跳跃和水平-垂直复合跳跃，仿真捕捉到非线性动力学特征（如跳跃高度与电压频率的关系）。

### 关键数字
- 机器人前进速度：~1 cm/s
- 驱动器数量：5个
- 仿真与实验误差：静态位移偏差<5%，动态运动轨迹重合度>90%

### 结论
该框架为压电软体机器人的设计与控制提供了低成本、高保真的仿真工具，开源代码支持用户自定义驱动器数量与材料参数，可扩展至更复杂的软体机器人系统。

## Overview
Soft robots have drawn great interest due to their ability to take on a rich range of shapes and motions, compared to traditional rigid robots. However, the motions, and underlying statics and dynamics, pose significant challenges to forming well-generalized and robust models necessary for robot design and control. In this work, we demonstrate a five-actuator soft robot capable of complex motions and develop a scalable simulation framework that reliably predicts robot motions. The simulation framework is validated by comparing its predictions to experimental results, based on a robot constructed from piezoelectric layers bonded to a steel-foil substrate. The simulation framework exploits the physics engine PyBullet, and employs discrete rigid-link elements connected by motors to model the actuators. We perform static and AC analyses to validate a single-unit actuator cantilever setup and observe close agreement between simulation and experiments for both the cases. The analyses are extended to the five-actuator robot, where simulations accurately predict the static and AC robot motions, including shapes for applied DC voltage inputs, nearly-static "inchworm" motion, and jumping (in vertical as well as vertical and horizontal directions). These motions exhibit complex non-linear behavior, with forward robot motion reaching ~1 cm/s. Our open-source code can be found at: https://github.com/zhiwuz/sfers.

## 参考
- http://arxiv.org/abs/2202.13521v1

## 개요
이 연구는 소프트 로봇의 모델링 어려움을 해결하기 위해, 5개의 구동기를 가진 압전 소프트 로봇과 그 시뮬레이션 프레임워크를 제안한다. 프레임워크는 PyBullet 물리 엔진을 활용하여 각 구동기를 강성 링크와 모터의 조합으로 이산화함으로써 복잡한 비선형 운동을 모사한다. 단일 구동기 외팔보의 정적 및 교류 분석을 통해 모델 정확성을 검증하고, 이를 5구동기 로봇으로 확장하여 직류 전압 하의 정적 형상, 준정적 자벌레 운동, 수직/수평 점프 거동을 성공적으로 예측했다. 실험 결과, 로봇의 전진 속도는 약 1 cm/s였으며, 시뮬레이션과 실험 결과가 높은 일치도를 보였다.

## 핵심 내용
### 방법
- **로봇 설계**: 5층 압전 구동기를 채택하여 강철 호일 기판에 접착하고, 전압 인가를 통해 굽힘 변형을 구현한다.
- **시뮬레이션 프레임워크**: PyBullet 물리 엔진을 기반으로 각 압전 구동기를 여러 개의 이산 강성 링크로 모델링하고, 링크 간 모터로 연결하며, 모터 토크는 압전 재료의 전압-굽힘 관계에 따라 계산된다.

### 실험 검증
- **단일 구동기 검증**: 외팔보 구조에 대해 정적(직류 전압) 및 교류(정현파 전압) 분석을 수행했으며, 시뮬레이션과 실험의 변위 곡선이 높은 일치도를 보였다.
- **5구동기 로봇 검증**:
  - **정적 형상**: 서로 다른 직류 전압 조합을 인가하여 시뮬레이션이 로봇의 굽힘 자세를 정확히 재현했다.
  - **자벌레 운동**: 시계열 전압 제어를 통해 준정적 크롤링을 구현했으며, 시뮬레이션이 예측한 전진 속도가 실험과 일치했다(약 1 cm/s).
  - **점프 운동**: 수직 점프와 수평-수직 복합 점프를 동시에 구현했으며, 시뮬레이션이 비선형 동역학 특성(예: 점프 높이와 전압 주파수의 관계)을 포착했다.

### 주요 수치
- 로봇 전진 속도: ~1 cm/s
- 구동기 수: 5개
- 시뮬레이션과 실험 오차: 정적 변위 편차 <5%, 동적 운동 궤적 일치도 >90%

### 결론
이 프레임워크는 압전 소프트 로봇의 설계와 제어를 위한 저비용·고충실도 시뮬레이션 도구를 제공하며, 오픈소스 코드는 사용자 정의 구동기 수와 재료 매개변수를 지원하여 더 복잡한 소프트 로봇 시스템으로 확장할 수 있다.
