---
$id: ent_paper_jorgensen_thermal_recovery_of_multi_limb_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Thermal Recovery of Multi-Limbed Robots with Electric Actuators
  zh: 具有电动执行器的多肢机器人的热恢复
  ko: 전기 액추에이터를 갖춘 다지체 로봇의 열 회복
summary:
  en: Proposes a data-driven, effort-based thermal model and a contact-constrained thermal inverse-kinematics approach to
    find robot configurations that cool overheated actuators, validated experimentally on the NASA Valkyrie humanoid.
  zh: 本文提出一种数据驱动的、基于力矩的热模型，并结合接触约束热逆运动学方法，为多肢体机器人寻找能冷却过热执行器的构型。该方法在NASA Valkyrie人形机器人硬件上得到实验验证，核心贡献在于通过构型优化实现执行器的热恢复。
  ko: 과열된 액추에이터를 냉각시키는 로봇 구형을 찾기 위해 데이터 기반의 노력 기반 1차 열 모델과 접촉 제약 열 역기구학 방법을 제안하고 NASA Valkyrie 휴머노이드에서 실험적으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- thermal_recovery
- actuator_thermal_model
- contact_constrained_thermal_ik
- gradient_descent
- nasa_valkyrie
- series_elastic_actuator
- effort_based_model
- humanoid_thermal_management
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1902.00187v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (556 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Thermal Recovery of Multi-Limbed Robots with Electric Actuators
  url: https://arxiv.org/abs/1902.00187
  date: '2019'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2019.2894068
theoretical_depth:
- method
---
## 概述
该研究针对人形机器人执行器过热的安全问题，设计了一种一阶数据驱动热模型，该模型基于执行器力矩预测未来热状态。在此基础上，通过建立构型与未来温度之间的映射关系，在满足有效接触约束的前提下，寻找能最小化未来温度的当前构型。这一过程本质上是接触约束热逆运动学（IK）的实现。实验在NASA Valkyrie机器人硬件上完成，验证了方法的有效性。

## 核心内容
### 方法
- 提出一阶数据驱动热模型，基于执行器力矩（effort）预测未来热状态，避免复杂物理建模。
- 建立构型与未来温度的映射，通过优化当前构型（受接触约束限制）来最小化未来温度。
- 该方法本质上是接触约束热逆运动学（IK）的实现，将热恢复问题转化为构型优化问题。

### 实验设置
- 在NASA Valkyrie人形机器人硬件上进行实验验证。
- 实验场景包括机器人处于特定接触状态（如站立或支撑），执行器处于过热状态。

### 关键结果
- 实验表明，优化后的构型能有效降低执行器温度，使其从不安全热状态恢复。
- 方法在真实硬件上运行，验证了其在实际应用中的可行性。

### 结论
- 该数据驱动热模型结合接触约束热IK，为多肢体机器人的热管理提供了实用方案。
- 未来工作可扩展至更复杂的接触场景或不同机器人平台。

## 参考
- http://arxiv.org/abs/1902.00187v4

## Overview
This study addresses the safety issue of actuator overheating in humanoid robots by designing a first-order data-driven thermal model that predicts future thermal states based on actuator effort. Building on this, a mapping between configuration and future temperature is established to find the current configuration that minimizes future temperature while satisfying effective contact constraints. This process is essentially an implementation of contact-constrained thermal inverse kinematics (IK). Experiments were conducted on the NASA Valkyrie robot hardware, validating the effectiveness of the method.

## Content
### Method
- Proposes a first-order data-driven thermal model that predicts future thermal states based on actuator effort, avoiding complex physical modeling.
- Establishes a mapping between configuration and future temperature, optimizing the current configuration (subject to contact constraints) to minimize future temperature.
- This method is essentially an implementation of contact-constrained thermal inverse kinematics (IK), transforming the thermal recovery problem into a configuration optimization problem.

### Experimental Setup
- Experimental validation was performed on the NASA Valkyrie humanoid robot hardware.
- Experimental scenarios include the robot in specific contact states (e.g., standing or supporting) with actuators in an overheated state.

### Key Results
- Experiments show that the optimized configuration effectively reduces actuator temperature, enabling recovery from unsafe thermal states.
- The method runs on real hardware, demonstrating its feasibility in practical applications.

### Conclusion
- The data-driven thermal model combined with contact-constrained thermal IK provides a practical solution for thermal management in multi-limbed robots.
- Future work could extend to more complex contact scenarios or different robot platforms.

## 개요
본 연구는 휴머노이드 로봇 액추에이터의 과열 안전 문제를 해결하기 위해, 액추에이터 토크(effort)를 기반으로 미래 열 상태를 예측하는 1차 데이터 기반 열 모델을 설계하였다. 이를 바탕으로, 자세(configuration)와 미래 온도 간의 매핑 관계를 구축하고, 유효 접촉 제약 조건을 충족하는 범위 내에서 미래 온도를 최소화할 수 있는 현재 자세를 탐색한다. 이 과정은 본질적으로 접촉 제약 열 역운동학(IK)의 구현이다. 실험은 NASA Valkyrie 로봇 하드웨어에서 수행되었으며, 방법의 유효성을 검증하였다.

## 핵심 내용
### 방법
- 액추에이터 토크(effort)를 기반으로 미래 열 상태를 예측하는 1차 데이터 기반 열 모델을 제안하여, 복잡한 물리 모델링을 피한다.
- 자세와 미래 온도 간의 매핑을 구축하고, 접촉 제약 조건의 제한을 받는 현재 자세를 최적화하여 미래 온도를 최소화한다.
- 이 방법은 본질적으로 접촉 제약 열 역운동학(IK)의 구현으로, 열 회복 문제를 자세 최적화 문제로 변환한다.

### 실험 설정
- NASA Valkyrie 휴머노이드 로봇 하드웨어에서 실험 검증을 수행한다.
- 실험 시나리오에는 로봇이 특정 접촉 상태(예: 서 있거나 지지하는 상태)에 있고, 액추에이터가 과열 상태인 경우가 포함된다.

### 주요 결과
- 실험 결과, 최적화된 자세가 액추에이터 온도를 효과적으로 낮추어 불안전한 열 상태에서 회복시킬 수 있음을 보여준다.
- 이 방법은 실제 하드웨어에서 실행되어 실제 응용에서의 실현 가능성을 검증한다.

### 결론
- 데이터 기반 열 모델과 접촉 제약 열 IK를 결합한 이 방법은 다중 팔다리 로봇의 열 관리를 위한 실용적인 솔루션을 제공한다.
- 향후 작업은 더 복잡한 접촉 시나리오나 다양한 로봇 플랫폼으로 확장할 수 있다.
