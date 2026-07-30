---
$id: ent_paper_ficht_online_balanced_motion_generat_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Online Balanced Motion Generation for Humanoid Robots
  zh: 人形机器人在线平衡运动生成
  ko: 휴머노이드 로봇을 위한 온라인 균형 모션 생성
summary:
  en: Proposes an analytic whole-body motion generator for low-cost humanoid robots with position-controlled joints and limited
    sensing, approximating the body and limbs with triangle centroid masses and representing the full pose as a five point-mass
    inverted pendulum; validated on the igus Humanoid Open Platform with balanced posing, kicking, and simple PD feedback.
  zh: 本文提出一种面向低成本、位置控制关节人形机器人的解析式全身运动生成方法。该方法将人体近似为五个质点（躯干与四肢）构成的倒立摆模型，通过分析肢体运动与质心关系生成静态稳定姿态。在igus Humanoid Open Platform上验证了平衡站立、踢腿等动作，并可通过简单PD反馈增强鲁棒性。
  ko: 위치 제어 관절과 제한된 센서를 갖춘 저비용 휴머노이드 로봇을 위한 해석적 전신 모션 생성 기법을 제안하며, 몸통과 사지를 삼각형 중심 질량으로 근사하고 전체 자세를 5개 점질량으로 된 역진자 모델로 표현;
    igus Humanoid Open Platform에서 균형 자세, 킥킹 동작 및 단순 PD 피드백으로 검증되었다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
- 06_design_engineering
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_motion_generation
- inverted_pendulum_model
- triangle_centroid_mass
- static_balance
- position_controlled_joints
- low_cost_humanoid
- com_tracking
- quasi_static_motion
- pd_stabilization
- igus_humanoid_open_platform
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1810.08388v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Online Balanced Motion Generation for Humanoid Robots
  url: https://arxiv.org/abs/1810.08388
  date: '2018'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该研究针对传感器有限、关节位置控制型低成本人形机器人，提出一种解析式全身运动生成方案。核心创新在于将人体质量分布简化为三角形质心模型，用五个质点（躯干+四肢）描述完整姿态，并与接触点构成倒立摆系统。通过指定倒立摆朝向和躯干姿态，结合肢体与躯干的位置调整策略，可生成满足质心参考位置的静态稳定姿态序列。实验在igus Humanoid Open Platform上完成，展示了平衡姿态、踢腿动作及基础PD反馈下的抗干扰能力。

## 核心内容
### 方法架构
- **质量分布建模**：将人体近似为五个质点（躯干+四肢），每个肢体视为三角形质心，通过分析肢体运动与对应质心位置的关系简化计算。
- **倒立摆系统**：五个质点加权求和后与地面接触点构成倒立摆模型，通过指定摆杆朝向（竖直方向）和躯干姿态生成静态稳定姿态。
- **姿态生成策略**：利用肢体与躯干的位置调整策略，使合成质心（CoM）达到参考位置；通过插值一组静态姿态序列实现全身运动。

### 实验设置
- **平台**：igus Humanoid Open Platform（低成本、位置控制关节、有限传感反馈）
- **验证动作**：平衡站立、踢腿动作
- **反馈机制**：采用基础PD控制器进行扰动抑制与轨迹跟踪误差最小化

### 关键结果
- 成功生成静态稳定姿态并实现连续运动
- 通过PD反馈可有效补偿外部扰动（如推搡）和关节位置跟踪误差
- 方法计算效率高（解析解），无需复杂优化或学习过程

### 结论
该解析式方法为低成本人形机器人提供了一种轻量级运动生成方案，在保证实时性的同时具备可扩展性（如集成反馈控制）。未来可结合更复杂的接触规划（如行走）或动态平衡策略。

## Overview
Reducing the complexity of higher order problems can enable solving them in analytical ways. In this paper, we propose an analytic whole body motion generator for humanoid robots. Our approach targets inexpensive platforms that possess position controlled joints and have limited feedback capabilities. By analysing the mass distribution in a humanoid-like body, we find relations between limb movement and their respective CoM positions. A full pose of a humanoid robot is then described with five point-masses, with one attached to the trunk and the remaining four assigned to each limb. The weighted sum of these masses in combination with a contact point form an inverted pendulum. We then generate statically stable poses by specifying a desired upright pendulum orientation, and any desired trunk orientation. Limb and trunk placement strategies are utilised to meet the reference CoM position. A set of these poses is interpolated to achieve stable whole body motions. The approach is evaluated by performing several motions with an igus Humanoid Open Platform robot. We demonstrate the extendability of the approach by applying basic feedback mechanisms for disturbance rejection and tracking error minimisation.

## 개요
고차 문제의 복잡성을 줄이면 이를 해석적 방식으로 해결할 수 있습니다. 본 논문에서는 휴머노이드 로봇을 위한 해석적 전신 동작 생성기를 제안합니다. 우리의 접근 방식은 위치 제어 조인트를 갖추고 제한된 피드백 기능을 가진 저가형 플랫폼을 대상으로 합니다. 휴머노이드 형태의 질량 분포를 분석함으로써, 사지 움직임과 각각의 CoM(질량 중심) 위치 간의 관계를 찾아냅니다. 휴머노이드 로봇의 전체 자세는 5개의 점 질량으로 설명되며, 하나는 몸통에 부착되고 나머지 네 개는 각 사지에 할당됩니다. 이 질량들의 가중 합과 접촉점이 결합하여 역진자를 형성합니다. 그런 다음 원하는 수직 진자 방향과 원하는 몸통 방향을 지정하여 정적으로 안정적인 자세를 생성합니다. 사지 및 몸통 배치 전략을 활용하여 기준 CoM 위치를 충족시킵니다. 이러한 자세 집합을 보간하여 안정적인 전신 동작을 구현합니다. 이 접근 방식은 igus Humanoid Open Platform 로봇으로 여러 동작을 수행하여 평가됩니다. 외란 제거 및 추적 오차 최소화를 위한 기본 피드백 메커니즘을 적용하여 접근 방식의 확장성을 입증합니다.

## 핵심 내용
고차 문제의 복잡성을 줄이면 이를 해석적 방식으로 해결할 수 있습니다. 본 논문에서는 휴머노이드 로봇을 위한 해석적 전신 동작 생성기를 제안합니다. 우리의 접근 방식은 위치 제어 조인트를 갖추고 제한된 피드백 기능을 가진 저가형 플랫폼을 대상으로 합니다. 휴머노이드 형태의 질량 분포를 분석함으로써, 사지 움직임과 각각의 CoM 위치 간의 관계를 찾아냅니다. 휴머노이드 로봇의 전체 자세는 5개의 점 질량으로 설명되며, 하나는 몸통에 부착되고 나머지 네 개는 각 사지에 할당됩니다. 이 질량들의 가중 합과 접촉점이 결합하여 역진자를 형성합니다. 그런 다음 원하는 수직 진자 방향과 원하는 몸통 방향을 지정하여 정적으로 안정적인 자세를 생성합니다. 사지 및 몸통 배치 전략을 활용하여 기준 CoM 위치를 충족시킵니다. 이러한 자세 집합을 보간하여 안정적인 전신 동작을 구현합니다. 이 접근 방식은 igus Humanoid Open Platform 로봇으로 여러 동작을 수행하여 평가됩니다. 외란 제거 및 추적 오차 최소화를 위한 기본 피드백 메커니즘을 적용하여 접근 방식의 확장성을 입증합니다.

## 参考
- http://arxiv.org/abs/1810.08388v1
