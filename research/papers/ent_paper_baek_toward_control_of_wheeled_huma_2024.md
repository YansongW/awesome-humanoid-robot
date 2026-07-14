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
  zh: 本文提出了一种框架，该框架根据轮腿机器人对未知载荷的本体感觉响应估计系统总质量和质心，显式预测新的平衡点，并将经粒子群优化参数化后的非线性动力学模型嵌入RaiSim以实现实到仿自适应。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.10948v2.
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
Model-based controllers using a linearized model around the system's equilibrium point is a common approach in the control of a wheeled humanoid due to their less computational load and ease of stability analysis. However, controlling a wheeled humanoid robot while it lifts an unknown object presents significant challenges, primarily due to the lack of knowledge in object dynamics. This paper presents a framework designed for predicting the new equilibrium point explicitly to control a wheeled-legged robot with unknown dynamics. We estimated the total mass and center of mass of the system from its response to initially unknown dynamics, then calculated the new equilibrium point accordingly. To avoid using additional sensors (e.g., force torque sensor) and reduce the effort of obtaining expensive real data, a data-driven approach is utilized with a novel real-to-sim adaptation. A more accurate nonlinear dynamics model, offering a closer representation of real-world physics, is injected into a rigid-body simulation for real-to-sim adaptation. The nonlinear dynamics model parameters were optimized using Particle Swarm Optimization. The efficacy of this framework was validated on a physical wheeled inverted pendulum, a simplified model of a wheeled-legged robot. The experimental results indicate that employing a more precise analytical model with optimized parameters significantly reduces the gap between simulation and reality, thus improving the efficiency of a model-based controller in controlling a wheeled robot with unknown dynamics

## 核心内容
Model-based controllers using a linearized model around the system's equilibrium point is a common approach in the control of a wheeled humanoid due to their less computational load and ease of stability analysis. However, controlling a wheeled humanoid robot while it lifts an unknown object presents significant challenges, primarily due to the lack of knowledge in object dynamics. This paper presents a framework designed for predicting the new equilibrium point explicitly to control a wheeled-legged robot with unknown dynamics. We estimated the total mass and center of mass of the system from its response to initially unknown dynamics, then calculated the new equilibrium point accordingly. To avoid using additional sensors (e.g., force torque sensor) and reduce the effort of obtaining expensive real data, a data-driven approach is utilized with a novel real-to-sim adaptation. A more accurate nonlinear dynamics model, offering a closer representation of real-world physics, is injected into a rigid-body simulation for real-to-sim adaptation. The nonlinear dynamics model parameters were optimized using Particle Swarm Optimization. The efficacy of this framework was validated on a physical wheeled inverted pendulum, a simplified model of a wheeled-legged robot. The experimental results indicate that employing a more precise analytical model with optimized parameters significantly reduces the gap between simulation and reality, thus improving the efficiency of a model-based controller in controlling a wheeled robot with unknown dynamics

## 参考
- http://arxiv.org/abs/2403.10948v2

