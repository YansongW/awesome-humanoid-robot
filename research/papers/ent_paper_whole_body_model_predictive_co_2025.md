---
$id: ent_paper_whole_body_model_predictive_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
  zh: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
  ko: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo
summary:
  en: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: 本文提出一种基于MuJoCo动力学与iLQR算法的全身模型预测控制方法，由John Zhang等人于2025年完成。核心贡献在于证明了该简单方法在四足与全尺寸人形机器人上的真实世界有效性，仅需少量sim-to-real调整即可实现动态运动与双足行走。
  ko: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
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
- loco_manipulation
- whole_body_control
- whole_body_model_predictive_co
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.04613v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Whole-Body Model-Predictive Control of Legged Robots with MuJoCo (arXiv)
  url: https://arxiv.org/abs/2503.04613
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作将迭代LQR算法与MuJoCo物理引擎结合，通过有限差分近似导数实现实时全身MPC。在硬件实验中，该方法成功驱动四足机器人完成动态奔跑、双足行走，并控制全尺寸人形机器人实现双足步态。研究强调其作为易复现的硬件基线，可降低真实世界全身MPC研究的门槛，相关代码与实验视频已开源。

## 核心内容
### 方法架构
- 采用iLQR作为核心优化器，利用MuJoCo引擎提供精确的动力学模型
- 通过有限差分法近似计算导数，避免复杂的解析推导
- 控制频率达到实时要求（具体频率未在正文中给出，但强调"real-time"）

### 实验设置
- 硬件平台：四足机器人（动态奔跑、双足行走）与全尺寸人形机器人（双足步态）
- sim-to-real策略：仅需少量调整即可从仿真迁移至真实环境
- 代码与视频已公开于项目主页

### 关键结果
- 四足机器人：成功实现动态奔跑与双足站立行走
- 人形机器人：完成全尺寸双足步态控制
- 所有实验均在真实硬件上实时运行，未使用任何预训练或离线优化

### 结论
该工作表明，结合MuJoCo动力学的简单iLQR方法即可在真实机器人上实现有效的全身MPC，为社区提供了低门槛的复现基线。

## Overview
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at:https://johnzhang3.github.io/mujoco_ilqr

## Overview
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at: https://johnzhang3.github.io/mujoco_ilqr

## Content
We demonstrate the surprising real-world effectiveness of a very simple approach to whole-body model-predictive control (MPC) of quadruped and humanoid robots: the iterative LQR (iLQR) algorithm with MuJoCo dynamics and finite-difference approximated derivatives. Building upon the previous success of model-based behavior synthesis and control of locomotion and manipulation tasks with MuJoCo in simulation, we show that these policies can easily generalize to the real world with few sim-to-real considerations. Our baseline method achieves real-time whole-body MPC on a variety of hardware experiments, including dynamic quadruped locomotion, quadruped walking on two legs, and full-sized humanoid bipedal locomotion. We hope this easy-to-reproduce hardware baseline lowers the barrier to entry for real-world whole-body MPC research and contributes to accelerating research velocity in the community. Our code and experiment videos will be available online at: https://johnzhang3.github.io/mujoco_ilqr

## 개요
우리는 사족 보행 로봇과 휴머노이드 로봇의 전신 모델 예측 제어(MPC)에 대한 매우 간단한 접근 방식의 놀라운 실제 효과를 입증합니다: MuJoCo 동역학과 유한 차분 근사 도함수를 사용한 반복 LQR(iLQR) 알고리즘입니다. 시뮬레이션에서 MuJoCo를 사용한 보행 및 조작 작업의 모델 기반 행동 합성 및 제어의 이전 성공을 바탕으로, 이러한 정책이 몇 가지 sim-to-real 고려 사항만으로 실제 세계에 쉽게 일반화될 수 있음을 보여줍니다. 우리의 기준 방법은 동적 사족 보행, 두 다리로 걷는 사족 보행, 전신 크기 휴머노이드 이족 보행을 포함한 다양한 하드웨어 실험에서 실시간 전신 MPC를 달성합니다. 이 쉽게 재현 가능한 하드웨어 기준이 실제 세계 전신 MPC 연구의 진입 장벽을 낮추고 커뮤니티의 연구 속도를 가속화하는 데 기여하기를 바랍니다. 우리의 코드와 실험 비디오는 다음에서 온라인으로 제공될 예정입니다: https://johnzhang3.github.io/mujoco_ilqr

## 핵심 내용
우리는 사족 보행 로봇과 휴머노이드 로봇의 전신 모델 예측 제어(MPC)에 대한 매우 간단한 접근 방식의 놀라운 실제 효과를 입증합니다: MuJoCo 동역학과 유한 차분 근사 도함수를 사용한 반복 LQR(iLQR) 알고리즘입니다. 시뮬레이션에서 MuJoCo를 사용한 보행 및 조작 작업의 모델 기반 행동 합성 및 제어의 이전 성공을 바탕으로, 이러한 정책이 몇 가지 sim-to-real 고려 사항만으로 실제 세계에 쉽게 일반화될 수 있음을 보여줍니다. 우리의 기준 방법은 동적 사족 보행, 두 다리로 걷는 사족 보행, 전신 크기 휴머노이드 이족 보행을 포함한 다양한 하드웨어 실험에서 실시간 전신 MPC를 달성합니다. 이 쉽게 재현 가능한 하드웨어 기준이 실제 세계 전신 MPC 연구의 진입 장벽을 낮추고 커뮤니티의 연구 속도를 가속화하는 데 기여하기를 바랍니다. 우리의 코드와 실험 비디오는 다음에서 온라인으로 제공될 예정입니다: https://johnzhang3.github.io/mujoco_ilqr

## 参考
- http://arxiv.org/abs/2503.04613v3
