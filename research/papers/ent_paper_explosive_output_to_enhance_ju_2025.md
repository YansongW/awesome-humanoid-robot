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
  zh: 'Explosive Output to Enhance Jumping Ability: A Variable Reduction Ratio Design Paradigm for Humanoid Robots Knee Joint
    is a 2025 work on hardware design for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.12314v1.
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
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1\% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## 核心内容
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1\% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## 参考
- http://arxiv.org/abs/2506.12314v1

## Overview
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## Content
Enhancing the explosive power output of the knee joints is critical for improving the agility and obstacle-crossing capabilities of humanoid robots. However, a mismatch between the knee-to-center-of-mass (CoM) transmission ratio and jumping demands, coupled with motor performance degradation at high speeds, restricts the duration of high-power output and limits jump performance. To address these problems, this paper introduces a novel knee joint design paradigm employing a dynamically decreasing reduction ratio for explosive output during jump. Analysis of motor output characteristics and knee kinematics during jumping inspired a coupling strategy in which the reduction ratio gradually decreases as the joint extends. A high initial ratio rapidly increases torque at jump initiation, while its gradual reduction minimizes motor speed increments and power losses, thereby maintaining sustained high-power output. A compact and efficient linear actuator-driven guide-rod mechanism realizes this coupling strategy, supported by parameter optimization guided by explosive jump control strategies. Experimental validation demonstrated a 63 cm vertical jump on a single-joint platform (a theoretical improvement of 28.1% over the optimal fixed-ratio joints). Integrated into a humanoid robot, the proposed design enabled a 1.1 m long jump, a 0.5 m vertical jump, and a 0.5 m box jump.

## 개요
인간형 로봇의 기민성과 장애물 통과 능력을 향상시키기 위해서는 무릎 관절의 폭발적인 출력 향상이 중요합니다. 그러나 무릎과 질량 중심(CoM) 간의 전달비와 점프 요구 사이의 불일치, 그리고 고속에서의 모터 성능 저하로 인해 고출력 지속 시간이 제한되어 점프 성능이 저하됩니다. 이러한 문제를 해결하기 위해, 본 논문은 점프 중 폭발적 출력을 위해 동적으로 감소하는 감속비를 사용하는 새로운 무릎 관절 설계 패러다임을 소개합니다. 점프 중 모터 출력 특성과 무릎 운동학을 분석한 결과, 관절이 펴짐에 따라 감속비가 점차 감소하는 결합 전략이 도출되었습니다. 높은 초기 감속비는 점프 시작 시 토크를 빠르게 증가시키고, 점진적인 감소는 모터 속도 증가와 전력 손실을 최소화하여 지속적인 고출력을 유지합니다. 이 결합 전략은 폭발적 점프 제어 전략에 따른 매개변수 최적화를 통해 소형 및 효율적인 선형 액추에이터 구동 가이드 로드 메커니즘으로 구현됩니다. 실험 검증 결과, 단일 관절 플랫폼에서 63cm 수직 점프를 달성했으며(최적 고정비 관절 대비 이론적 28.1% 향상), 인간형 로봇에 통합되어 1.1m 멀리뛰기, 0.5m 수직 점프, 0.5m 박스 점프를 가능하게 했습니다.

## 핵심 내용
인간형 로봇의 기민성과 장애물 통과 능력을 향상시키기 위해서는 무릎 관절의 폭발적인 출력 향상이 중요합니다. 그러나 무릎과 질량 중심(CoM) 간의 전달비와 점프 요구 사이의 불일치, 그리고 고속에서의 모터 성능 저하로 인해 고출력 지속 시간이 제한되어 점프 성능이 저하됩니다. 이러한 문제를 해결하기 위해, 본 논문은 점프 중 폭발적 출력을 위해 동적으로 감소하는 감속비를 사용하는 새로운 무릎 관절 설계 패러다임을 소개합니다. 점프 중 모터 출력 특성과 무릎 운동학을 분석한 결과, 관절이 펴짐에 따라 감속비가 점차 감소하는 결합 전략이 도출되었습니다. 높은 초기 감속비는 점프 시작 시 토크를 빠르게 증가시키고, 점진적인 감소는 모터 속도 증가와 전력 손실을 최소화하여 지속적인 고출력을 유지합니다. 이 결합 전략은 폭발적 점프 제어 전략에 따른 매개변수 최적화를 통해 소형 및 효율적인 선형 액추에이터 구동 가이드 로드 메커니즘으로 구현됩니다. 실험 검증 결과, 단일 관절 플랫폼에서 63cm 수직 점프를 달성했으며(최적 고정비 관절 대비 이론적 28.1% 향상), 인간형 로봇에 통합되어 1.1m 멀리뛰기, 0.5m 수직 점프, 0.5m 박스 점프를 가능하게 했습니다.
