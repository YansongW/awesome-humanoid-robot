---
$id: ent_paper_baek_toward_control_of_wheeled_huma_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium Point Estimation via Real-to-Sim Adaptation'
  zh: 面向未知载荷轮式人形机器人的控制：通过实到仿自适应估计平衡点
  ko: 미지의 페이로드를 가진 휠형 휴머노이드 로봇 제어를 향한 실제-시뮬레이션 적응 기반 평형점 추정
summary:
  en: This paper presents a framework that estimates the total mass and center of mass of a wheeled-legged robot from its
    proprioceptive response to unknown payloads, explicitly predicts the new equilibrium point, and uses a nonlinear dynamics
    model injected into RaiSim whose parameters are optimized by Particle Swarm Optimization for real-to-sim adaptation.
  zh: 本文提出一种框架，用于在轮式人形机器人搬运未知负载时，通过本体感知响应估计系统总质量与质心，并显式预测新的平衡点。该框架采用基于Particle Swarm Optimization优化的非线性动力学模型注入RaiSim仿真，通过real-to-sim自适应缩小仿真与现实差距，无需额外力/力矩传感器即可提升模型控制器对未知动态的适应能力。
  ko: 본 논문은 휠-다리 로봇이 미지의 페이로드에 대한 본체감각 응답으로부터 전체 질량과 질량 중심을 추정하고, 새로운 평형점을 명시적으로 예측하며, 입자 군집 최적화로 매개변수를 최적화한 비선형 동역학 모델을 RaiSim에
    주입하여 실제-시뮬레이션 적응을 실현하는 프레임워크를 제시한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- wheeled_humanoid
- wheeled_legged_robot
- unknown_payload
- equilibrium_point_estimation
- real_to_sim
- sim_to_real
- particle_swarm_optimization
- model_based_control
- lqr_control
- wheeled_inverted_pendulum
- raisim
- system_identification
- center_of_mass_estimation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.10948v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (871 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium Point Estimation via Real-to-Sim Adaptation'
  url: https://arxiv.org/abs/2403.10948
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
针对轮式人形机器人搬运未知物体时因缺乏动力学知识导致的控制难题，本文提出一种无需额外传感器的平衡点预测框架。该方法通过机器人对未知负载的本体感知响应，实时估计系统总质量与质心位置，并据此显式计算新的平衡点。为降低对昂贵真实数据的依赖，研究团队采用数据驱动方法实现real-to-sim自适应，将经Particle Swarm Optimization优化的非线性动力学模型注入RaiSim物理引擎。实验在轮式倒立摆（轮式人形机器人的简化模型）上验证，结果表明优化后的精确解析模型能显著缩小仿真与现实的差距，从而提升模型控制器对未知动态的控制效率。

## 核心内容
### 核心挑战与解决方案
- 传统模型控制器依赖平衡点附近的线性化模型，虽计算量小且便于稳定性分析，但面对未知负载时因缺乏动力学知识而失效。
- 本文提出显式预测新平衡点的框架，通过估计系统总质量与质心位置，直接计算平衡点变化。

### 方法架构
- **参数估计**：利用机器人对未知负载的本体感知响应（如关节力矩、姿态变化），实时估计总质量与质心位置，无需额外力/力矩传感器。
- **平衡点计算**：基于估计参数显式计算新的平衡点，为控制器提供参考。
- **Real-to-Sim自适应**：
  - 将更接近真实物理的非线性动力学模型注入RaiSim刚体仿真环境。
  - 采用Particle Swarm Optimization优化模型参数，最小化仿真与真实机器人响应之间的差异。
  - 该数据驱动方法减少了对昂贵真实数据的采集需求。

### 实验验证
- **平台**：物理轮式倒立摆（作为轮式人形机器人的简化模型）。
- **关键结果**：
  - 优化后的非线性模型显著缩小了仿真与现实的差距。
  - 模型控制器在未知动态下的控制效率得到提升，验证了框架的有效性。

### 结论
本文通过real-to-sim自适应与参数优化，使模型控制器能够有效应对未知负载带来的动力学变化，为轮式人形机器人在实际场景中的鲁棒控制提供了可行方案。

## Overview
Model-based controllers using a linearized model around the system's equilibrium point is a common approach in the control of a wheeled humanoid due to their less computational load and ease of stability analysis. However, controlling a wheeled humanoid robot while it lifts an unknown object presents significant challenges, primarily due to the lack of knowledge in object dynamics. This paper presents a framework designed for predicting the new equilibrium point explicitly to control a wheeled-legged robot with unknown dynamics. We estimated the total mass and center of mass of the system from its response to initially unknown dynamics, then calculated the new equilibrium point accordingly. To avoid using additional sensors (e.g., force torque sensor) and reduce the effort of obtaining expensive real data, a data-driven approach is utilized with a novel real-to-sim adaptation. A more accurate nonlinear dynamics model, offering a closer representation of real-world physics, is injected into a rigid-body simulation for real-to-sim adaptation. The nonlinear dynamics model parameters were optimized using Particle Swarm Optimization. The efficacy of this framework was validated on a physical wheeled inverted pendulum, a simplified model of a wheeled-legged robot. The experimental results indicate that employing a more precise analytical model with optimized parameters significantly reduces the gap between simulation and reality, thus improving the efficiency of a model-based controller in controlling a wheeled robot with unknown dynamics

## Overview
Model-based controllers using a linearized model around the system's equilibrium point is a common approach in the control of a wheeled humanoid due to their less computational load and ease of stability analysis. However, controlling a wheeled humanoid robot while it lifts an unknown object presents significant challenges, primarily due to the lack of knowledge in object dynamics. This paper presents a framework designed for predicting the new equilibrium point explicitly to control a wheeled-legged robot with unknown dynamics. We estimated the total mass and center of mass of the system from its response to initially unknown dynamics, then calculated the new equilibrium point accordingly. To avoid using additional sensors (e.g., force torque sensor) and reduce the effort of obtaining expensive real data, a data-driven approach is utilized with a novel real-to-sim adaptation. A more accurate nonlinear dynamics model, offering a closer representation of real-world physics, is injected into a rigid-body simulation for real-to-sim adaptation. The nonlinear dynamics model parameters were optimized using Particle Swarm Optimization. The efficacy of this framework was validated on a physical wheeled inverted pendulum, a simplified model of a wheeled-legged robot. The experimental results indicate that employing a more precise analytical model with optimized parameters significantly reduces the gap between simulation and reality, thus improving the efficiency of a model-based controller in controlling a wheeled robot with unknown dynamics.

## Content
Model-based controllers using a linearized model around the system's equilibrium point is a common approach in the control of a wheeled humanoid due to their less computational load and ease of stability analysis. However, controlling a wheeled humanoid robot while it lifts an unknown object presents significant challenges, primarily due to the lack of knowledge in object dynamics. This paper presents a framework designed for predicting the new equilibrium point explicitly to control a wheeled-legged robot with unknown dynamics. We estimated the total mass and center of mass of the system from its response to initially unknown dynamics, then calculated the new equilibrium point accordingly. To avoid using additional sensors (e.g., force torque sensor) and reduce the effort of obtaining expensive real data, a data-driven approach is utilized with a novel real-to-sim adaptation. A more accurate nonlinear dynamics model, offering a closer representation of real-world physics, is injected into a rigid-body simulation for real-to-sim adaptation. The nonlinear dynamics model parameters were optimized using Particle Swarm Optimization. The efficacy of this framework was validated on a physical wheeled inverted pendulum, a simplified model of a wheeled-legged robot. The experimental results indicate that employing a more precise analytical model with optimized parameters significantly reduces the gap between simulation and reality, thus improving the efficiency of a model-based controller in controlling a wheeled robot with unknown dynamics.

## 参考
- http://arxiv.org/abs/2403.10948v2

## 개요
바퀴형 휴머노이드 로봇이未知 물체를 운반할 때 동역학 지식 부족으로 발생하는 제어 문제를 해결하기 위해, 본 논문은 추가 센서 없이 평형점을 예측하는 프레임워크를 제안한다. 이 방법은 로봇이未知 부하에 대한 본체 인식 응답을 통해 시스템 총 질량과 질량 중심 위치를 실시간으로 추정하고, 이를 기반으로 새로운 평형점을 명시적으로 계산한다. 고가의 실제 데이터 의존도를 낮추기 위해 연구팀은 데이터 기반 방법으로 real-to-sim 적응을 구현하고, Particle Swarm Optimization으로 최적화된 비선형 동역학 모델을 RaiSim 물리 엔진에 주입한다. 실험은 바퀴형 도립진자(바퀴형 휴머노이드 로봇의 단순화 모델)에서 검증되었으며, 최적화된 정밀 해석 모델이 시뮬레이션과 현실 간의 차이를 크게 줄여 모델 기반 제어기의未知 동역학에 대한 제어 효율을 향상시킬 수 있음을 보여준다.

## 핵심 내용
### 핵심 도전 과제 및 해결 방안
- 기존 모델 기반 제어기는 평형점 주변의 선형화 모델에 의존하며, 계산량이 적고 안정성 분석이 용이하지만未知 부하에 직면했을 때 동역학 지식 부족으로 실패한다.
- 본 논문은 시스템 총 질량과 질량 중심 위치를 추정하여 평형점 변화를 직접 계산하는 새로운 평형점 명시적 예측 프레임워크를 제안한다.

### 방법 구조
- **파라미터 추정**: 로봇이未知 부하에 대한 본체 인식 응답(예: 관절 토크, 자세 변화)을 활용하여 총 질량과 질량 중심 위치를 실시간으로 추정하며, 추가 힘/토크 센서가 필요 없다.
- **평형점 계산**: 추정된 파라미터를 기반으로 새로운 평형점을 명시적으로 계산하여 제어기에 참조를 제공한다.
- **Real-to-Sim 적응**:
  - 실제 물리 현상에 더 가까운 비선형 동역학 모델을 RaiSim 강체 시뮬레이션 환경에 주입한다.
  - Particle Swarm Optimization을 사용하여 모델 파라미터를 최적화하고, 시뮬레이션과 실제 로봇 응답 간의 차이를 최소화한다.
  - 이 데이터 기반 방법은 고가의 실제 데이터 수집 요구를 줄인다.

### 실험 검증
- **플랫폼**: 물리 바퀴형 도립진자(바퀴형 휴머노이드 로봇의 단순화 모델).
- **주요 결과**:
  - 최적화된 비선형 모델이 시뮬레이션과 현실 간의 차이를 크게 줄였다.
  - 모델 기반 제어기가未知 동역학에서 제어 효율이 향상되어 프레임워크의 유효성을 검증했다.

### 결론
본 논문은 real-to-sim 적응과 파라미터 최적화를 통해 모델 기반 제어기가未知 부하로 인한 동역학 변화에 효과적으로 대응할 수 있게 하여, 바퀴형 휴머노이드 로봇의 실제 환경에서의 강건한 제어를 위한 실현 가능한 솔루션을 제공한다.
