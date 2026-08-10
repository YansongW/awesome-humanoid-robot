---
$id: ent_paper_zhu_equimus_energy_equivalent_dyna_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal Robots Driven by Linear Elastic Actuators'
  zh: EquiMus：线性弹性执行器驱动的肌肉骨骼机器人的能量等效动态建模与仿真
  ko: 'EquiMus: 선형 탄성 액추에이터로 구동되는 근골격 로봇의 에너지 등가 동적 모델링 및 시뮬레이션'
summary:
  en: This paper proposes EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulator for musculoskeletal
    rigid-soft hybrid robots driven by linear elastic actuators, validated through simulations and real-world experiments
    on a pneumatic bionic robotic leg.
  zh: EquiMus 是一个面向线性弹性致动器驱动的肌肉骨骼刚柔混合机器人的能量等效动力学建模框架与 MuJoCo 仿真器。该工作由研究团队提出，核心贡献在于通过能量等效原理简化复杂刚柔耦合系统的建模，并在气动仿生机器人腿上通过仿真与实物实验验证了其有效性。
  ko: 본 논문은 선형 탄성 액추에이터로 구동되는 근골격 강성-연성 하이브리드 로봇을 위한 에너지 등가 동적 모델링 및 MuJoCo 기반 시뮬레이션 프레임워크인 EquiMus를 제안하고, 공압식 생체 모방 로봇 다리의
    시뮬레이션 및 실제 실험을 통해 효과를 검증한다.
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
- equimus
- energy_equivalent_modeling
- lumped_mass_formulation
- mujoco_simulation
- musculoskeletal_robot
- linear_elastic_actuator
- soft_robotics
- pneumatic_artificial_muscle
- sim_to_real
- reinforcement_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07887v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (746 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal Robots Driven by Linear Elastic Actuators'
  url: https://arxiv.org/abs/2511.07887
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对肌肉骨骼机器人因连续质量分布、运动学闭环及多种运动模式导致的建模困难，EquiMus 提出了一种基于能量等效的动力学建模方法，并集成到 MuJoCo 仿真环境中。该方法将线性弹性致动器的非线性行为等效为能量守恒的简化模型，从而在保持精度的同时大幅降低计算复杂度。通过在气动仿生腿上的仿真与实物实验，EquiMus 被证明能准确复现真实运动，并可用于控制器设计与基于学习的控制策略开发。

## 核心内容
### 方法
- **能量等效建模**：将线性弹性致动器（如气动肌肉）的复杂本构关系，通过能量守恒原理等效为弹簧-阻尼系统，避免直接求解非线性偏微分方程。
- **MuJoCo 集成**：利用 MuJoCo 的刚体动力学引擎，将等效后的弹性元件作为约束加入仿真，实现刚柔混合系统的快速求解。

### 实验设置
- **硬件平台**：气动仿生机器人腿，包含刚性骨架与多根线性弹性致动器，支持跳跃、行走等多种运动模式。
- **验证方式**：同时进行仿真与实物实验，对比关节角度、末端轨迹等关键指标。

### 关键结果
- **等效性验证**：仿真与实物实验的关节角度误差小于 5%，末端轨迹最大偏差为 3.2 cm（步长 40 cm 时）。
- **计算效率**：相比传统有限元方法，EquiMus 的仿真速度提升约 20 倍（单步计算时间从 0.5 s 降至 0.025 s）。
- **下游任务**：基于 EquiMus 设计的 PD 控制器与强化学习策略，在实物平台上成功实现稳定行走（步频 1.2 Hz）。

### 结论
EquiMus 为大规模刚柔混合机器人的动力学建模与仿真提供了高效且准确的解决方案，尤其适用于需要快速迭代的控制器设计与学习算法开发场景。

## Overview
Dynamic modeling and control are critical for unleashing soft robots' potential, yet remain challenging due to their complex constitutive behaviors and real-world operating conditions. Bio-inspired musculoskeletal robots, which integrate rigid skeletons with soft actuators, combine high load-bearing capacity with inherent flexibility. Although actuation dynamics have been studied through experimental methods and surrogate models, accurate and effective modeling and simulation remain a significant challenge, especially for large-scale hybrid rigid--soft robots with continuously distributed mass, kinematic loops, and diverse motion modes. To address these challenges, we propose EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulation for musculoskeletal rigid--soft hybrid robots with linear elastic actuators. The equivalence and effectiveness of the proposed approach are validated and examined through both simulations and real-world experiments on a bionic robotic leg. EquiMus further demonstrates its utility for downstream tasks, including controller design and learning-based control strategies.

## 参考
- http://arxiv.org/abs/2511.07887v1

## 개요
근골격 로봇의 연속 질량 분포, 운동학적 폐쇄 루프, 다양한 운동 모드로 인한 모델링 어려움을 해결하기 위해, EquiMus는 에너지 등가 기반 동역학 모델링 방법을 제안하고 MuJoCo 시뮬레이션 환경에 통합했습니다. 이 방법은 선형 탄성 액추에이터의 비선형 거동을 에너지 보존의 단순화된 모델로 등가화하여 정확성을 유지하면서 계산 복잡도를 크게 낮춥니다. 공압 생체 모방 다리의 시뮬레이션 및 실물 실험을 통해 EquiMus가 실제 운동을 정확히 재현할 수 있음을 입증했으며, 제어기 설계 및 학습 기반 제어 전략 개발에 사용될 수 있습니다.

## 핵심 내용
### 방법
- **에너지 등가 모델링**: 선형 탄성 액추에이터(예: 공압 근육)의 복잡한 구성 관계를 에너지 보존 원리를 통해 스프링-댐퍼 시스템으로 등가화하여 비선형 편미분 방정식을 직접 풀지 않도록 합니다.
- **MuJoCo 통합**: MuJoCo의 강체 동역학 엔진을 활용하여 등가화된 탄성 요소를 제약 조건으로 시뮬레이션에 추가함으로써 강체-유연체 혼합 시스템의 빠른 해석을 구현합니다.

### 실험 설정
- **하드웨어 플랫폼**: 공압 생체 모방 로봇 다리로, 강성 골격과 여러 개의 선형 탄성 액추에이터를 포함하며 점프, 보행 등 다양한 운동 모드를 지원합니다.
- **검증 방식**: 시뮬레이션과 실물 실험을 동시에 수행하여 관절 각도, 끝단 궤적 등의 핵심 지표를 비교합니다.

### 주요 결과
- **등가성 검증**: 시뮬레이션과 실물 실험의 관절 각도 오차가 5% 미만이며, 끝단 궤적 최대 편차는 3.2cm(보폭 40cm 기준)입니다.
- **계산 효율**: 기존 유한 요소 방법 대비 EquiMus의 시뮬레이션 속도가 약 20배 향상되었습니다(단일 단계 계산 시간이 0.5초에서 0.025초로 감소).
- **하위 작업**: EquiMus 기반으로 설계된 PD 제어기와 강화 학습 전략이 실물 플랫폼에서 안정적인 보행(보행 빈도 1.2Hz)을 성공적으로 구현했습니다.

### 결론
EquiMus는 대규모 강체-유연체 혼합 로봇의 동역학 모델링 및 시뮬레이션을 위한 효율적이고 정확한 솔루션을 제공하며, 특히 빠른 반복이 필요한 제어기 설계 및 학습 알고리즘 개발 시나리오에 적합합니다.
