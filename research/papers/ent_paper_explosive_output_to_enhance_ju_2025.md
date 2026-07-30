---
$id: ent_paper_explosive_output_to_enhance_ju_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint'
  zh: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint'
  ko: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint'
summary:
  en: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint
    is a 2025 work on hardware design for humanoid robots.'
  zh: 本文提出一种用于人形机器人膝关节的可变减速比设计范式，通过动态降低减速比来增强跳跃时的爆发力输出。该设计由紧凑的线性驱动导杆机构实现，在单关节平台上实现了63厘米垂直跳跃，相比最优固定减速比关节提升28.1%。集成到人形机器人后，该设计支持1.1米跳远、0.5米垂直跳和0.5米跳箱。
  ko: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint
    is a 2025 work on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- explosive_output_to_enhance_ju
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12314v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee
    Joint (arXiv)'
  url: https://arxiv.org/abs/2506.12314
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对人形机器人膝关节爆发力输出不足的问题，本文分析了膝关节到质心传动比与跳跃需求不匹配、以及电机高速性能下降对高功率输出持续时间的限制。受电机输出特性和跳跃运动学分析启发，作者提出一种减速比随关节伸展逐渐减小的耦合策略：初始高减速比在起跳瞬间快速提升扭矩，随后减速比逐渐降低以抑制电机转速增长和功率损失，从而维持持续的高功率输出。通过紧凑高效的线性驱动导杆机构实现该策略，并基于爆发式跳跃控制策略进行参数优化。

## 核心内容
### 核心问题
- 人形机器人膝关节爆发力不足限制了敏捷性和越障能力
- 膝关节到质心传动比与跳跃需求不匹配
- 电机高速运行时性能下降，高功率输出持续时间受限

### 方法设计
- **变减速比耦合策略**：减速比随关节伸展动态降低，初始高减速比在起跳瞬间提供大扭矩，随后逐渐减小以抑制电机转速增长和功率损失
- **机构实现**：采用紧凑高效的线性驱动导杆机构，通过参数优化匹配爆发式跳跃控制策略
- 分析电机输出特性和跳跃运动学，推导出减速比变化规律

### 实验验证
- **单关节平台测试**：实现63厘米垂直跳跃，相比最优固定减速比关节理论提升28.1%
- **整机集成测试**：集成到人形机器人后，实现1.1米跳远、0.5米垂直跳和0.5米跳箱
- 实验验证了变减速比设计在维持高功率输出和提升跳跃性能方面的有效性

## Overview
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1\% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## Overview
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## Content
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## 개요
인간형 로봇의 기민성과 장애물 통과 능력을 향상시키기 위해서는 무릎 관절의 폭발적인 출력 향상이 중요합니다. 그러나 무릎과 질량 중심(CoM) 간의 전달비와 점프 요구 사이의 불일치, 그리고 고속에서의 모터 성능 저하로 인해 고출력 지속 시간이 제한되어 점프 성능이 저하됩니다. 이러한 문제를 해결하기 위해, 본 논문은 점프 중 폭발적 출력을 위해 동적으로 감소하는 감속비를 사용하는 새로운 무릎 관절 설계 패러다임을 소개합니다. 점프 중 모터 출력 특성과 무릎 운동학을 분석한 결과, 관절이 펴짐에 따라 감속비가 점차 감소하는 결합 전략이 도출되었습니다. 높은 초기 감속비는 점프 시작 시 토크를 빠르게 증가시키고, 점진적인 감소는 모터 속도 증가와 전력 손실을 최소화하여 지속적인 고출력을 유지합니다. 이 결합 전략은 폭발적 점프 제어 전략에 따른 매개변수 최적화를 통해 소형 및 효율적인 선형 액추에이터 구동 가이드 로드 메커니즘으로 구현됩니다. 실험 검증 결과, 단일 관절 플랫폼에서 63cm 수직 점프를 달성했으며(최적 고정비 관절 대비 이론적 28.1% 향상), 인간형 로봇에 통합되어 1.1m 멀리뛰기, 0.5m 수직 점프, 0.5m 박스 점프를 가능하게 했습니다.

## 핵심 내용
인간형 로봇의 기민성과 장애물 통과 능력을 향상시키기 위해서는 무릎 관절의 폭발적인 출력 향상이 중요합니다. 그러나 무릎과 질량 중심(CoM) 간의 전달비와 점프 요구 사이의 불일치, 그리고 고속에서의 모터 성능 저하로 인해 고출력 지속 시간이 제한되어 점프 성능이 저하됩니다. 이러한 문제를 해결하기 위해, 본 논문은 점프 중 폭발적 출력을 위해 동적으로 감소하는 감속비를 사용하는 새로운 무릎 관절 설계 패러다임을 소개합니다. 점프 중 모터 출력 특성과 무릎 운동학을 분석한 결과, 관절이 펴짐에 따라 감속비가 점차 감소하는 결합 전략이 도출되었습니다. 높은 초기 감속비는 점프 시작 시 토크를 빠르게 증가시키고, 점진적인 감소는 모터 속도 증가와 전력 손실을 최소화하여 지속적인 고출력을 유지합니다. 이 결합 전략은 폭발적 점프 제어 전략에 따른 매개변수 최적화를 통해 소형 및 효율적인 선형 액추에이터 구동 가이드 로드 메커니즘으로 구현됩니다. 실험 검증 결과, 단일 관절 플랫폼에서 63cm 수직 점프를 달성했으며(최적 고정비 관절 대비 이론적 28.1% 향상), 인간형 로봇에 통합되어 1.1m 멀리뛰기, 0.5m 수직 점프, 0.5m 박스 점프를 가능하게 했습니다.

## 参考
- http://arxiv.org/abs/2506.12314v1
