---
$id: ent_paper_rapt_model_predictive_out_of_d_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots'
  zh: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots'
  ko: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots'
summary:
  en: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots is a 2026
    work on sim-to-real for humanoid robots.'
  zh: RAPT 是 2026 年提出的一种轻量级、自监督的部署时监控方法，用于解决人形机器人从仿真到现实（Sim-to-Real）迁移中的分布外（OOD）检测与故障诊断问题。其核心贡献在于：通过概率时空流形学习实现高帧率（50Hz）下的校准化
    OOD 检测，并利用梯度时间显著性与大语言模型（LLM）推理结合，实现零样本的根因故障诊断。在 Unitree G1 人形机器人上，RAPT 在仿真中相比最强基线提升了 37% 的真阳性率（TPR），在真实部署中实现了 12.5% 的
    TPR 提升和 75% 的根因分类准确率。
  ko: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots is a 2026
    work on sim-to-real for humanoid robots.'
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
- rapt
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.01515v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RAPT: Model-Predictive Out-of-Distribution Detection and Failure Diagnosis for Sim-to-Real Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2602.01515
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
RAPT 针对人形机器人 Sim-to-Real 迁移中策略在分布外状态下自信执行但导致硬件损坏的问题，设计了一种部署时监控器。它从仿真中学习标称执行的概率时空流形，并在执行时计算预测偏差作为校准化的逐维度信号，从而在极低假阳性率约束下实现可靠的在线 OOD 检测。此外，RAPT 还提供连续、可解释的 Sim-to-Real 失配度量，并通过结合梯度时间显著性与 LLM 推理的自动化事后根因分析管道，生成语义化的故障诊断。在 Unitree G1 人形机器人的四个复杂任务中，RAPT 在仿真和真实硬件上均显著优于基线方法，并展示了实际部署中的可解释性。

## 核心内容
### 方法架构
RAPT 的核心是一个轻量级、自监督的部署时监控器，运行于 50Hz 的人形机器人控制频率下。其方法分为两个阶段：
- **离线训练**：在仿真环境中，RAPT 学习标称执行（nominal execution）的概率时空流形。具体地，它通过自监督方式建模机器人状态序列的联合分布，捕捉时间与空间上的依赖关系。
- **在线检测**：在执行时，RAPT 计算当前状态相对于所学流形的预测偏差（predictive deviation），并将其作为校准化的逐维度信号。该信号用于：
  - **OOD 检测**：在严格的假阳性率约束下（如 0.5% 的 episode 级假阳性率），可靠地识别分布外状态。
  - **失配度量**：提供连续、可解释的 Sim-to-Real 失配度量，可随时间追踪以量化部署偏离训练的程度。

### 故障诊断
RAPT 引入了一个自动化的事后根因分析管道，结合两种技术：
- **梯度时间显著性**：基于 RAPT 的重建目标（reconstruction objective），计算每个时间步的梯度显著性，突出对偏差贡献最大的状态维度。
- **LLM 推理**：将梯度显著性与关节运动学（joint kinematics）作为条件输入大语言模型（LLM），在零样本（zero-shot）设置下生成语义化的故障诊断。

### 实验设置与结果
实验在 Unitree G1 人形机器人上进行，涵盖四个复杂任务（具体任务未在正文中列出），包括仿真和真实硬件部署。
- **仿真实验**：在大型仿真中，RAPT 在固定 episode 级假阳性率 0.5% 的条件下，真阳性率（TPR）相比最强基线提升了 37%。
- **真实世界部署**：在物理硬件上，RAPT 实现了 12.5% 的 TPR 提升，并提供了可操作的（actionable）可解释性。在 16 个真实世界故障中，仅使用本体感受数据（proprioceptive data）就达到了 75% 的根因分类准确率。

## Overview
Deploying learned control policies on humanoid robots is challenging: policies that appear robust in simulation can execute confidently in out-of-distribution (OOD) states after Sim-to-Real transfer, leading to silent failures that risk hardware damage. Although anomaly detection can mitigate these failures, prior methods are often incompatible with high-rate control, poorly calibrated at the extremely low false-positive rates required for practical deployment, or operate as black boxes that provide a binary stop signal without explaining why the robot drifted from nominal behavior. We present RAPT, a lightweight, self-supervised deployment-time monitor for 50Hz humanoid control. RAPT learns a probabilistic spatio-temporal manifold of nominal execution from simulation and evaluates execution-time predictive deviation as a calibrated, per-dimension signal. This yields (i) reliable online OOD detection under strict false-positive constraints and (ii) a continuous, interpretable measure of Sim-to-Real mismatch that can be tracked over time to quantify how far deployment has drifted from training. Beyond detection, we introduce an automated post-hoc root-cause analysis pipeline that combines gradient-based temporal saliency derived from RAPT's reconstruction objective with LLM-based reasoning conditioned on saliency and joint kinematics to produce semantic failure diagnoses in a zero-shot setting. We evaluate RAPT on a Unitree G1 humanoid across four complex tasks in simulation and on physical hardware. In large-scale simulation, RAPT improves True Positive Rate (TPR) by 37% over the strongest baseline at a fixed episode-level false positive rate of 0.5%. On real-world deployments, RAPT achieves a 12.5% TPR improvement and provides actionable interpretability, reaching 75% root-cause classification accuracy across 16 real-world failures using only proprioceptive data.

## 개요
휴머노이드 로봇에 학습된 제어 정책을 배포하는 것은 어려운 과제입니다. 시뮬레이션에서 강건해 보이는 정책도 Sim-to-Real 전환 후 분포 외(OOD) 상태에서 자신 있게 실행되어 하드웨어 손상 위험이 있는 무음 오류를 초래할 수 있습니다. 이상 탐지가 이러한 오류를 완화할 수 있지만, 기존 방법은 고속 제어와 호환되지 않거나, 실제 배포에 필요한 극도로 낮은 거짓 양성률에서 제대로 보정되지 않거나, 로봇이 정상 동작에서 벗어난 이유를 설명하지 않고 이진 중단 신호만 제공하는 블랙박스로 작동하는 경우가 많습니다. 본 논문에서는 50Hz 휴머노이드 제어를 위한 경량의 자가 지도 배포 시간 모니터인 RAPT를 제시합니다. RAPT는 시뮬레이션에서 정상 실행의 확률적 시공간 다양체를 학습하고, 실행 시간 예측 편차를 보정된 차원별 신호로 평가합니다. 이를 통해 (i) 엄격한 거짓 양성 제약 조건 하에서 신뢰할 수 있는 온라인 OOD 탐지와 (ii) 시간에 따라 추적하여 배포가 훈련에서 얼마나 벗어났는지 정량화할 수 있는 연속적이고 해석 가능한 Sim-to-Real 불일치 측정값을 제공합니다. 탐지 외에도, RAPT의 재구성 목표에서 파생된 그래디언트 기반 시간적 중요도와 중요도 및 관절 운동학에 기반한 LLM 추론을 결합하여 제로샷 설정에서 의미론적 오류 진단을 생성하는 자동화된 사후 원인 분석 파이프라인을 도입합니다. RAPT를 Unitree G1 휴머노이드에서 시뮬레이션과 실제 하드웨어에서 네 가지 복잡한 작업에 걸쳐 평가했습니다. 대규모 시뮬레이션에서 RAPT는 고정된 에피소드 수준 거짓 양성률 0.5%에서 가장 강력한 기준선 대비 진양성률(TPR)을 37% 향상시켰습니다. 실제 배포에서 RAPT는 12.5%의 TPR 향상을 달성하고 실행 가능한 해석 가능성을 제공하여, 고유 감각 데이터만으로 16개의 실제 오류에서 75%의 근본 원인 분류 정확도를 달성했습니다.

## 핵심 내용
휴머노이드 로봇에 학습된 제어 정책을 배포하는 것은 어려운 과제입니다. 시뮬레이션에서 강건해 보이는 정책도 Sim-to-Real 전환 후 분포 외(OOD) 상태에서 자신 있게 실행되어 하드웨어 손상 위험이 있는 무음 오류를 초래할 수 있습니다. 이상 탐지가 이러한 오류를 완화할 수 있지만, 기존 방법은 고속 제어와 호환되지 않거나, 실제 배포에 필요한 극도로 낮은 거짓 양성률에서 제대로 보정되지 않거나, 로봇이 정상 동작에서 벗어난 이유를 설명하지 않고 이진 중단 신호만 제공하는 블랙박스로 작동하는 경우가 많습니다. 본 논문에서는 50Hz 휴머노이드 제어를 위한 경량의 자가 지도 배포 시간 모니터인 RAPT를 제시합니다. RAPT는 시뮬레이션에서 정상 실행의 확률적 시공간 다양체를 학습하고, 실행 시간 예측 편차를 보정된 차원별 신호로 평가합니다. 이를 통해 (i) 엄격한 거짓 양성 제약 조건 하에서 신뢰할 수 있는 온라인 OOD 탐지와 (ii) 시간에 따라 추적하여 배포가 훈련에서 얼마나 벗어났는지 정량화할 수 있는 연속적이고 해석 가능한 Sim-to-Real 불일치 측정값을 제공합니다. 탐지 외에도, RAPT의 재구성 목표에서 파생된 그래디언트 기반 시간적 중요도와 중요도 및 관절 운동학에 기반한 LLM 추론을 결합하여 제로샷 설정에서 의미론적 오류 진단을 생성하는 자동화된 사후 원인 분석 파이프라인을 도입합니다. RAPT를 Unitree G1 휴머노이드에서 시뮬레이션과 실제 하드웨어에서 네 가지 복잡한 작업에 걸쳐 평가했습니다. 대규모 시뮬레이션에서 RAPT는 고정된 에피소드 수준 거짓 양성률 0.5%에서 가장 강력한 기준선 대비 진양성률(TPR)을 37% 향상시켰습니다. 실제 배포에서 RAPT는 12.5%의 TPR 향상을 달성하고 실행 가능한 해석 가능성을 제공하여, 고유 감각 데이터만으로 16개의 실제 오류에서 75%의 근본 원인 분류 정확도를 달성했습니다.

## 参考
- http://arxiv.org/abs/2602.01515v1
