---
$id: ent_paper_shi_koopman_operators_for_modeling_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Koopman Operators for Modeling and Control of Soft Robotics
  zh: 用于软体机器人建模与控制的Koopman算子
  ko: 소프트 로봇 모델링 및 제어를 위한 쿱만 연산자
summary:
  en: A 2023 review of Koopman operator theory and its data-driven approximations
    (EDMD/gEDMD) for modeling and control of soft robots, emphasizing lifting-function
    design, robustness, and integration with MPC and LQR control structures.
  zh: 2023年发表的一篇综述，回顾Koopman算子理论及其数据驱动近似方法（EDMD/gEDMD）在软体机器人建模与控制中的应用，重点讨论提升函数设计、鲁棒性以及与模型预测控制（MPC）和线性二次调节器（LQR）控制结构的结合。
  ko: 2023년 발표된 리뷰로, 데이터 기반 근사법(EDMD/gEDMD)을 활용한 쿱만 연산자 이론을 소프트 로봇의 모델링 및 제어에 적용한
    최신 연구를 정리하며, 리프팅 함수 설계, 강건성, MPC 및 LQR 제어 구조와의 통합을 강조한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- koopman_operator
- soft_robotics
- edmd
- gedmd
- lifting_functions
- model_predictive_control
- linear_quadratic_regulator
- data_driven_modeling
- global_linearization
- compliant_robots
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from the arXiv full text; factual claims should be human-reviewed
    against the final published version before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Koopman Operators for Modeling and Control of Soft Robotics
  url: https://arxiv.org/abs/2301.09708
  date: '2023'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

This paper is a review of how Koopman operator theory has been applied to the modeling and control of soft robots. The authors identify three major trends: the design of lifting functions is critical for accurate data-driven approximation; robustness to noise, uncertainty, and sparse measurements is increasingly emphasized; and Koopman linear models are being embedded into model-based controllers such as MPC and LQR. Because soft robots are built from compliant materials and exhibit infinite-dimensional, highly nonlinear behavior, first-principles modeling is difficult, motivating data-driven linearization through the Koopman operator.

The review introduces the Koopman operator, its generator, and the EDMD/gEDMD approximation schemes. In EDMD, a dictionary of observables lifts the original state into a higher-dimensional space where dynamics are approximately linear, and a least-squares fit over snapshot pairs yields a finite-dimensional K operator. The generator version, gEDMD, estimates the infinitesimal generator directly from continuous-time data and derivatives. A central implementation issue is the choice of lifting dictionary; the authors categorize approaches as empirical (monomials/polynomials), mechanics-inspired (using rigid-robot analogies or topology-informed bases), and machine-learning-based (neural-network dictionaries/eigenfunctions learned from offline data).

The second half of the review focuses on control. Koopman models can be embedded in MPC as prediction constraints, and in LQR as linear state-space models for state-feedback design. The authors note that most soft-robot demonstrations remain relatively simple, often rely on offline training or open-loop input sequences, and face sensing limitations because accurate velocity or higher-order derivatives are hard to measure directly. They also highlight open problems such as principled selection of lifting functions and optimal sampling rates.

## Key Contributions

- Reviews Koopman operator theory and EDMD/gEDMD data-driven approximation in the context of soft robotics.
- Categorizes lifting-function design into empirical, mechanics-inspired, and machine-learning-based strategies.
- Discusses robustness considerations including noise, uncertainty, sparse models, stability guarantees, and Kalman-filter-based disturbance estimation.
- Surveys Koopman-based control frameworks, especially MPC and LQR, with concrete soft-robot implementations such as grippers, continuum robots, and a soft inverted pendulum.
- Identifies open challenges: complex multi-DOF systems, online closed-loop robust control, limited sensing, and lack of general methods for choosing lifting functions and sampling rates.

## Relevance to Humanoid Robotics

Humanoid robots increasingly incorporate soft and compliant components—such as soft fingertips, compliant limbs, and padded contact surfaces—to enable safe physical human interaction and tolerate impacts during deployment. The Koopman-operator methods reviewed here offer a data-driven path to obtain linear, control-oriented models of these compliant subsystems without deriving detailed first-principles models. This can simplify controller synthesis and re-tuning during mass production and real-world deployment, where component variability and nonlinear deformation are common.

Because the review covers model identification (lifting-function design, EDMD/gEDMD), robustness to noise and uncertainty, and integration with standard model-based controllers (MPC/LQR), its content is directly applicable to the design of control stacks for humanoids that use soft hardware. The limitations it notes—especially sensing constraints, offline training dependence, and lack of general tuning rules—are also highly relevant engineering constraints for humanoid systems.
