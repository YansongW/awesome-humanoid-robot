---
$id: ent_paper_learning_aerodynamics_for_the_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Aerodynamics for the Control of Flying Humanoid Robots
  zh: Learning Aerodynamics for the Control of Flying Humanoid Robots
  ko: Learning Aerodynamics for the Control of Flying Humanoid Robots
summary:
  en: Learning Aerodynamics for the Control of Flying Humanoid Robots is a 2025 work on locomotion for humanoid robots.
  zh: 本文是2025年关于飞行人形机器人运动控制的研究。意大利技术研究院（IIT）团队提出了iRonCub-Mk1喷气动力人形机器人，核心贡献在于结合经典方法与深度学习技术建模与控制空气动力，并通过风洞实验与飞行仿真验证了方法的有效性。
  ko: Learning Aerodynamics for the Control of Flying Humanoid Robots is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_aerodynamics_for_the
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.00305v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Aerodynamics for the Control of Flying Humanoid Robots (arXiv)
  url: https://arxiv.org/abs/2506.00305
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究聚焦于多模态运动人形机器人的空气动力学挑战。技术层面，团队设计了专为喷气发动机集成的iRonCub-Mk1机器人，并对其硬件进行改造以支持风洞实验，从而精确测量空气动力与表面压力。科学层面，研究结合计算流体动力学（CFD）仿真与深度学习，构建了空气动力数据集并训练了深度神经网络与线性回归模型，最终将这些模型集成到仿真器中，用于设计空气动力感知控制器，并通过飞行仿真与实物平衡实验验证了控制效果。

## 核心内容
### 研究背景与挑战
- 多模态运动机器人因环境适应性成为研究热点，但人形机器人增加飞行能力后，面临空气动力建模与控制的特殊难题。

### 技术贡献：iRonCub-Mk1硬件设计
- 机械设计针对喷气发动机集成进行优化，包括结构强化与热管理。
- 硬件改造支持风洞实验，可精确测量空气动力与表面压力分布。

### 科学贡献：空气动力建模与控制
- **CFD仿真与验证**：使用计算流体动力学（CFD）仿真计算空气动力，并通过iRonCub-Mk1风洞实验验证仿真精度。
- **数据集扩展**：开发自动化CFD框架，生成大规模空气动力数据集。
- **模型训练**：基于数据集训练深度神经网络（DNN）与线性回归模型，用于预测空气动力。
- **控制器集成**：将训练好的模型集成到仿真器中，设计空气动力感知控制器。

### 实验验证
- **飞行仿真**：验证控制器在飞行场景中的稳定性与响应能力。
- **实物实验**：在iRonCub-Mk1原型机上完成平衡实验，进一步确认模型与控制器在实际硬件上的有效性。

## Overview
Robots with multi-modal locomotion are an active research field due to their versatility in diverse environments. In this context, additional actuation can provide humanoid robots with aerial capabilities. Flying humanoid robots face challenges in modeling and control, particularly with aerodynamic forces. This paper addresses these challenges from a technological and scientific standpoint. The technological contribution includes the mechanical design of iRonCub-Mk1, a jet-powered humanoid robot, optimized for jet engine integration, and hardware modifications for wind tunnel experiments on humanoid robots for precise aerodynamic forces and surface pressure measurements. The scientific contribution offers a comprehensive approach to model and control aerodynamic forces using classical and learning techniques. Computational Fluid Dynamics (CFD) simulations calculate aerodynamic forces, validated through wind tunnel experiments on iRonCub-Mk1. An automated CFD framework expands the aerodynamic dataset, enabling the training of a Deep Neural Network and a linear regression model. These models are integrated into a simulator for designing aerodynamic-aware controllers, validated through flight simulations and balancing experiments on the iRonCub-Mk1 physical prototype.

## 개요
다중 모드 이동 능력을 갖춘 로봇은 다양한 환경에서의 다재다능함 덕분에 활발한 연구 분야입니다. 이러한 맥락에서 추가적인 구동 장치는 휴머노이드 로봇에 비행 능력을 부여할 수 있습니다. 비행 휴머노이드 로봇은 모델링 및 제어, 특히 공기역학적 힘과 관련된 문제에 직면합니다. 본 논문은 이러한 문제를 기술적 및 과학적 관점에서 다룹니다. 기술적 기여로는 제트 엔진 통합에 최적화된 제트 구동 휴머노이드 로봇 iRonCub-Mk1의 기계적 설계와, 정밀한 공기역학적 힘 및 표면 압력 측정을 위한 휴머노이드 로봇 풍동 실험을 위한 하드웨어 개조가 포함됩니다. 과학적 기여는 고전적 및 학습 기법을 사용하여 공기역학적 힘을 모델링하고 제어하는 포괄적인 접근 방식을 제공합니다. 전산유체역학(CFD) 시뮬레이션은 공기역학적 힘을 계산하며, iRonCub-Mk1에 대한 풍동 실험을 통해 검증됩니다. 자동화된 CFD 프레임워크는 공기역학 데이터 세트를 확장하여 심층 신경망 및 선형 회귀 모델의 훈련을 가능하게 합니다. 이러한 모델은 공기역학 인식 제어기를 설계하기 위한 시뮬레이터에 통합되며, iRonCub-Mk1 물리적 프로토타입에 대한 비행 시뮬레이션 및 균형 실험을 통해 검증됩니다.

## 핵심 내용
다중 모드 이동 능력을 갖춘 로봇은 다양한 환경에서의 다재다능함 덕분에 활발한 연구 분야입니다. 이러한 맥락에서 추가적인 구동 장치는 휴머노이드 로봇에 비행 능력을 부여할 수 있습니다. 비행 휴머노이드 로봇은 모델링 및 제어, 특히 공기역학적 힘과 관련된 문제에 직면합니다. 본 논문은 이러한 문제를 기술적 및 과학적 관점에서 다룹니다. 기술적 기여로는 제트 엔진 통합에 최적화된 제트 구동 휴머노이드 로봇 iRonCub-Mk1의 기계적 설계와, 정밀한 공기역학적 힘 및 표면 압력 측정을 위한 휴머노이드 로봇 풍동 실험을 위한 하드웨어 개조가 포함됩니다. 과학적 기여는 고전적 및 학습 기법을 사용하여 공기역학적 힘을 모델링하고 제어하는 포괄적인 접근 방식을 제공합니다. 전산유체역학(CFD) 시뮬레이션은 공기역학적 힘을 계산하며, iRonCub-Mk1에 대한 풍동 실험을 통해 검증됩니다. 자동화된 CFD 프레임워크는 공기역학 데이터 세트를 확장하여 심층 신경망 및 선형 회귀 모델의 훈련을 가능하게 합니다. 이러한 모델은 공기역학 인식 제어기를 설계하기 위한 시뮬레이터에 통합되며, iRonCub-Mk1 물리적 프로토타입에 대한 비행 시뮬레이션 및 균형 실험을 통해 검증됩니다.

## 参考
- http://arxiv.org/abs/2506.00305v2
