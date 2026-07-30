---
$id: ent_paper_a_co_design_framework_for_high_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Co-Design Framework for High-Performance Jumping of a Five-Bar Monoped with Actuator Optimization
  zh: A Co-Design Framework for High-Performance Jumping of a Five-Bar Monoped with Actuator Optimization
  ko: A Co-Design Framework for High-Performance Jumping of a Five-Bar Monoped with Actuator Optimization
summary:
  en: 'arXiv:2604.06025v2 Announce Type: replace Abstract: The performance of legged robots depends strongly on both mechanical
    design and control, motivating co-design approaches that jointly optimize these parameters. However, most existing co-design
    studies focus on link dimensions and transmission ratios while neglecting detailed actuator design, particularly motor
    and gearbox parameter optimization, and are largely limited to serial open-chain mechanisms. In this work, we present
    a co-design framework for a planar closed-chain five-bar monoped that jointly optimizes mechanical design, motor and gearbox
    parameters, and control parameters for dynamic jumping. The objective is to maximize jump distance while minimizing mechanical
    energy consumption. The framework employs a two-stage optimization approach, where actuator optimization generates a mapping
    from gear ratio to actuator mass, efficiency, and peak torque, which is then incorporated into CMA-ES-based co-design
    optimization of the robot design and control parameters. Simulation results demonstrate an improvement of approximately
    30.4% in jump distance and an 11.5% reduction in mechanical energy consumption compared to a nominal design, highlighting
    the effectiveness of the proposed framework for high-performance and energy-efficient planar jumping.'
  zh: 本文提出了一种面向平面闭链五杆单足机器人的协同设计框架，联合优化机械设计、电机与减速器参数以及控制参数，以最大化跳跃距离并最小化机械能耗。该框架采用两阶段优化方法，先通过执行器优化生成速比到质量、效率与峰值扭矩的映射，再结合CMA-ES进行协同设计优化。仿真结果显示，与标称设计相比，跳跃距离提升约30.4%，机械能耗降低11.5%。
  ko: 'arXiv:2604.06025v2 Announce Type: replace Abstract: The performance of legged robots depends strongly on both mechanical
    design and control, motivating co-design approaches that jointly optimize these parameters. However, most existing co-design
    studies focus on link dimensions and transmission ratios while neglecting detailed actuator design, particularly motor
    and gearbox parameter optimization, and are largely limited to serial open-chain mechanisms. In this work, we present
    a co-design framework for a planar closed-chain five-bar monoped that jointly optimizes mechanical design, motor and gearbox
    parameters, and control parameters for dynamic jumping. The objective is to maximize jump distance while minimizing mechanical
    energy consumption. The framework employs a two-stage optimization approach, where actuator optimization generates a mapping
    from gear ratio to actuator mass, efficiency, and peak torque, which is then incorporated into CMA-ES-based co-design
    optimization of the robot design and control parameters. Simulation results demonstrate an improvement of approximately
    30.4% in jump distance and an 11.5% reduction in mechanical energy consumption compared to a nominal design, highlighting
    the effectiveness of the proposed framework for high-performance and energy-efficient planar jumping.'
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
- a_co_design_framework_for_high
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.06025v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A Co-Design Framework for High-Performance Jumping of a Five-Bar Monoped with Actuator Optimization (arXiv)
  url: https://arxiv.org/abs/2604.06025
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有腿式机器人协同设计研究多聚焦于连杆尺寸与传动比，忽略了执行器细节（如电机与减速器参数），且主要限于串联开链机构。本文针对平面闭链五杆单足机器人，提出一种同时优化机械设计、执行器参数与控制参数的协同设计框架，目标是在动态跳跃中最大化跳跃距离并最小化机械能耗。框架采用两阶段优化：首先通过执行器优化建立速比与执行器质量、效率及峰值扭矩的映射关系，随后将该映射集成到基于CMA-ES的协同设计优化中，以优化机器人设计与控制参数。仿真结果表明，该方法在跳跃性能与能效上均显著优于标称设计。

## 核心内容
### 方法概述
本文提出一种针对平面闭链五杆单足机器人的协同设计框架，核心创新在于将执行器参数（电机与减速器）纳入联合优化，突破了现有研究仅优化连杆尺寸与传动比的局限。

### 两阶段优化架构
- **第一阶段：执行器优化**  
  生成从速比到执行器质量、效率及峰值扭矩的映射关系。该映射作为后续优化的输入，确保执行器设计在物理约束下实现最优性能。
- **第二阶段：CMA-ES协同设计优化**  
  基于CMA-ES算法，联合优化机器人机械设计参数（如连杆长度、关节配置）与控制参数（如跳跃轨迹、力矩分配），目标函数为最大化跳跃距离与最小化机械能耗。

### 实验设置与关键结果
- **仿真环境**：在平面闭链五杆单足机器人模型上进行动态跳跃仿真。
- **对比基准**：与未进行执行器优化的标称设计对比。
- **关键数字**：
  - 跳跃距离提升约 **30.4%**
  - 机械能耗降低 **11.5%**
- **结论**：该框架有效提升了平面跳跃机器人的性能与能效，验证了将执行器参数纳入协同设计的必要性。

## Overview
The performance of legged robots depends strongly on both mechanical design and control, motivating co-design approaches that jointly optimize these parameters. However, most existing co-design studies focus on link dimensions and transmission ratios while neglecting detailed actuator design, particularly motor and gearbox parameter optimization, and are largely limited to serial open-chain mechanisms. In this work, we present a co-design framework for a planar closed-chain five-bar monoped that jointly optimizes mechanical design, motor and gearbox parameters, and control parameters for dynamic jumping. The objective is to maximize jump distance while minimizing mechanical energy consumption. The framework employs a two-stage optimization approach, where actuator optimization generates a mapping from gear ratio to actuator mass, efficiency, and peak torque, which is then incorporated into CMA-ES-based co-design optimization of the robot design and control parameters. Simulation results demonstrate an improvement of approximately 30.4% in jump distance and an 11.5% reduction in mechanical energy consumption compared to a nominal design, highlighting the effectiveness of the proposed framework for high-performance and energy-efficient planar jumping.

## 개요
다리 로봇의 성능은 기계 설계와 제어 모두에 크게 의존하므로, 이러한 매개변수를 공동으로 최적화하는 공동 설계 접근법이 동기를 부여합니다. 그러나 기존의 대부분의 공동 설계 연구는 링크 치수와 변속비에 초점을 맞추고 있으며, 특히 모터와 기어박스 매개변수 최적화와 같은 세부 액추에이터 설계를 간과하고 있으며, 대부분 직렬 개방 체인 메커니즘으로 제한됩니다. 본 연구에서는 동적 점프를 위해 기계 설계, 모터 및 기어박스 매개변수, 제어 매개변수를 공동으로 최적화하는 평면 폐쇄 체인 5바 모노페드용 공동 설계 프레임워크를 제시합니다. 목표는 기계적 에너지 소비를 최소화하면서 점프 거리를 최대화하는 것입니다. 이 프레임워크는 2단계 최적화 접근법을 사용하며, 여기서 액추에이터 최적화는 기어비를 액추에이터 질량, 효율 및 최대 토크에 매핑하는 관계를 생성한 다음, 이를 CMA-ES 기반 로봇 설계 및 제어 매개변수의 공동 설계 최적화에 통합합니다. 시뮬레이션 결과는 기준 설계와 비교하여 점프 거리가 약 30.4% 향상되고 기계적 에너지 소비가 11.5% 감소함을 보여주며, 고성능 및 에너지 효율적인 평면 점프를 위한 제안된 프레임워크의 효과성을 강조합니다.

## 핵심 내용
다리 로봇의 성능은 기계 설계와 제어 모두에 크게 의존하므로, 이러한 매개변수를 공동으로 최적화하는 공동 설계 접근법이 동기를 부여합니다. 그러나 기존의 대부분의 공동 설계 연구는 링크 치수와 변속비에 초점을 맞추고 있으며, 특히 모터와 기어박스 매개변수 최적화와 같은 세부 액추에이터 설계를 간과하고 있으며, 대부분 직렬 개방 체인 메커니즘으로 제한됩니다. 본 연구에서는 동적 점프를 위해 기계 설계, 모터 및 기어박스 매개변수, 제어 매개변수를 공동으로 최적화하는 평면 폐쇄 체인 5바 모노페드용 공동 설계 프레임워크를 제시합니다. 목표는 기계적 에너지 소비를 최소화하면서 점프 거리를 최대화하는 것입니다. 이 프레임워크는 2단계 최적화 접근법을 사용하며, 여기서 액추에이터 최적화는 기어비를 액추에이터 질량, 효율 및 최대 토크에 매핑하는 관계를 생성한 다음, 이를 CMA-ES 기반 로봇 설계 및 제어 매개변수의 공동 설계 최적화에 통합합니다. 시뮬레이션 결과는 기준 설계와 비교하여 점프 거리가 약 30.4% 향상되고 기계적 에너지 소비가 11.5% 감소함을 보여주며, 고성능 및 에너지 효율적인 평면 점프를 위한 제안된 프레임워크의 효과성을 강조합니다.

## 参考
- http://arxiv.org/abs/2604.06025v2
