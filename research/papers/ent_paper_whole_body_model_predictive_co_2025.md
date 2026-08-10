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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.04613v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (525 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2503.04613v3

## 개요
이 연구는 반복 LQR 알고리즘을 MuJoCo 물리 엔진과 결합하고, 유한 차분 근사를 통해 도함수를 계산하여 실시간 전신 MPC를 구현합니다. 하드웨어 실험에서 이 방법은 네 발 달린 로봇의 동적 달리기, 이족 보행을 성공적으로 구동했으며, 전신 크기 휴머노이드 로봇의 이족 보행 자세를 제어했습니다. 연구는 이 방법이 재현하기 쉬운 하드웨어 기준선으로서 실제 세계 전신 MPC 연구의 진입 장벽을 낮출 수 있음을 강조하며, 관련 코드와 실험 영상은 오픈소스로 공개되었습니다.

## 핵심 내용
### 방법 아키텍처
- 핵심 최적화 도구로 iLQR을 채택하고, MuJoCo 엔진을 사용하여 정확한 동역학 모델을 제공
- 유한 차분법을 통해 도함수를 근사 계산하여 복잡한 해석적 유도를 피함
- 제어 주파수가 실시간 요구 사항을 충족 (본문에 구체적인 주파수는 명시되지 않았지만 "실시간"을 강조)

### 실험 설정
- 하드웨어 플랫폼: 네 발 달린 로봇(동적 달리기, 이족 보행) 및 전신 크기 휴머노이드 로봇(이족 보행 자세)
- sim-to-real 전략: 시뮬레이션에서 실제 환경으로 전환 시 약간의 조정만 필요
- 코드와 영상은 프로젝트 홈페이지에 공개

### 주요 결과
- 네 발 달린 로봇: 동적 달리기와 이족 서기 보행 성공
- 휴머노이드 로봇: 전신 크기 이족 보행 자세 제어 완료
- 모든 실험은 사전 훈련이나 오프라인 최적화 없이 실제 하드웨어에서 실시간으로 실행

### 결론
이 연구는 MuJoCo 동역학과 결합된 간단한 iLQR 방법이 실제 로봇에서 효과적인 전신 MPC를 구현할 수 있음을 보여주며, 커뮤니티에 낮은 진입 장벽의 재현 기준선을 제공합니다.
