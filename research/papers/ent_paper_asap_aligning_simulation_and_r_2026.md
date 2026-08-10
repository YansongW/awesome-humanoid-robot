---
$id: ent_paper_asap_aligning_simulation_and_r_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
  zh: sim-to-real 对齐不是调参数那么简单
  ko: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills'
summary:
  en: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills is a knowledge node
    related to paper in the humanoid robot value chain.'
  zh: ASAP 是一个两阶段框架，由研究团队提出，旨在解决人形机器人从仿真到现实部署时的动力学不匹配问题。其核心贡献是通过训练残差动作模型来补偿仿真与真实物理之间的差异，从而显著提升机器人全身运动的敏捷性与协调性。
  ko: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills is a knowledge node
    related to paper in the humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- sim_to_real
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.01143v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (885 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills (arXiv)'
  url: https://arxiv.org/abs/2502.01143
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: sim-to-real 对齐不是调参数那么简单 project page
  url: https://agile.human2humanoid.com
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
ASAP 框架首先利用重定向的人类运动数据在仿真环境中预训练运动跟踪策略。随后，将策略部署到真实机器人上收集数据，并基于这些数据训练一个残差动作模型来补偿动力学差异。最后，将该残差模型集成到仿真器中微调预训练策略，使其更贴近真实物理。该方法在 IsaacGym 到 IsaacSim、Genesis 以及真实 Unitree G1 机器人三种迁移场景中均降低了跟踪误差，并实现了此前难以达成的敏捷动作。

## 核心内容
### 方法架构
ASAP 采用两阶段框架解决仿真到现实（sim-to-real）的动力学不匹配问题：
- **第一阶段**：在仿真环境中使用重定向的人类运动数据预训练全身运动跟踪策略。
- **第二阶段**：
  1. 将预训练策略部署到真实机器人上，收集真实世界数据。
  2. 基于收集的数据训练一个残差动作模型（delta action model），用于补偿仿真与真实物理之间的动力学差异。
  3. 将训练好的残差动作模型集成到仿真器中，对预训练策略进行微调，使其与真实世界动力学对齐。

### 实验设置与评估
- **迁移场景**：在三种场景下评估 ASAP 的性能：
  - IsaacGym 到 IsaacSim
  - IsaacGym 到 Genesis
  - IsaacGym 到真实 Unitree G1 人形机器人
- **对比基线**：与系统辨识（SysID）、域随机化（DR）以及残差动力学学习基线进行对比。
- **关键指标**：跟踪误差（tracking error）显著降低，尤其在动态运动任务中。

### 关键结果与结论
- ASAP 在多种动态运动中显著提升了敏捷性和全身协调能力。
- 相比 SysID、DR 和残差动力学学习基线，ASAP 有效降低了跟踪误差。
- 该框架使机器人能够执行此前难以实现的敏捷动作，展示了残差动作学习在弥合仿真与真实动力学差异方面的潜力。
- 研究结果表明，ASAP 为开发更具表现力和敏捷性的人形机器人提供了一种有前景的 sim-to-real 方向。

## Overview
Humanoid robots hold the potential for unparalleled versatility in performing human-like, whole-body skills. However, achieving agile and coordinated whole-body motions remains a significant challenge due to the dynamics mismatch between simulation and the real world. Existing approaches, such as system identification (SysID) and domain randomization (DR) methods, often rely on labor-intensive parameter tuning or result in overly conservative policies that sacrifice agility. In this paper, we present ASAP (Aligning Simulation and Real-World Physics), a two-stage framework designed to tackle the dynamics mismatch and enable agile humanoid whole-body skills. In the first stage, we pre-train motion tracking policies in simulation using retargeted human motion data. In the second stage, we deploy the policies in the real world and collect real-world data to train a delta (residual) action model that compensates for the dynamics mismatch. Then, ASAP fine-tunes pre-trained policies with the delta action model integrated into the simulator to align effectively with real-world dynamics. We evaluate ASAP across three transfer scenarios: IsaacGym to IsaacSim, IsaacGym to Genesis, and IsaacGym to the real-world Unitree G1 humanoid robot. Our approach significantly improves agility and whole-body coordination across various dynamic motions, reducing tracking error compared to SysID, DR, and delta dynamics learning baselines. ASAP enables highly agile motions that were previously difficult to achieve, demonstrating the potential of delta action learning in bridging simulation and real-world dynamics. These results suggest a promising sim-to-real direction for developing more expressive and agile humanoids.

## 参考
- http://arxiv.org/abs/2502.01143v3

## 개요
ASAP 프레임워크는 먼저 리타게팅된 인간 모션 데이터를 활용하여 시뮬레이션 환경에서 운동 추적 정책을 사전 학습합니다. 이후, 정책을 실제 로봇에 배포하여 데이터를 수집하고, 이 데이터를 기반으로 잔차 동작 모델을 학습하여 역학 차이를 보상합니다. 마지막으로, 이 잔차 모델을 시뮬레이터에 통합하여 사전 학습된 정책을 미세 조정함으로써 실제 물리 현상에 더 가깝게 만듭니다. 이 방법은 IsaacGym에서 IsaacSim, Genesis, 그리고 실제 Unitree G1 로봇까지의 세 가지 전이 시나리오에서 추적 오류를 줄였으며, 이전에는 달성하기 어려웠던 민첩한 동작을 구현했습니다.

## 핵심 내용
### 방법 아키텍처
ASAP는 시뮬레이션에서 실제(sim-to-real)로의 역학 불일치 문제를 해결하기 위해 2단계 프레임워크를 채택합니다:
- **1단계**: 시뮬레이션 환경에서 리타게팅된 인간 모션 데이터를 사용하여 전신 운동 추적 정책을 사전 학습합니다.
- **2단계**:
  1. 사전 학습된 정책을 실제 로봇에 배포하여 실제 세계 데이터를 수집합니다.
  2. 수집된 데이터를 기반으로 잔차 동작 모델(delta action model)을 학습하여 시뮬레이션과 실제 물리 간의 역학 차이를 보상합니다.
  3. 학습된 잔차 동작 모델을 시뮬레이터에 통합하여 사전 학습된 정책을 미세 조정함으로써 실제 세계 역학과 정렬시킵니다.

### 실험 설정 및 평가
- **전이 시나리오**: 세 가지 시나리오에서 ASAP의 성능을 평가합니다:
  - IsaacGym에서 IsaacSim
  - IsaacGym에서 Genesis
  - IsaacGym에서 실제 Unitree G1 휴머노이드 로봇
- **비교 기준**: 시스템 식별(SysID), 도메인 무작위화(DR) 및 잔차 역학 학습 기준선과 비교합니다.
- **핵심 지표**: 추적 오류(tracking error)가 크게 감소하며, 특히 동적 운동 작업에서 두드러집니다.

### 핵심 결과 및 결론
- ASAP는 다양한 동적 운동에서 민첩성과 전신 협응 능력을 크게 향상시킵니다.
- SysID, DR 및 잔차 역학 학습 기준선과 비교하여 ASAP는 추적 오류를 효과적으로 줄입니다.
- 이 프레임워크는 로봇이 이전에는 구현하기 어려웠던 민첩한 동작을 수행할 수 있게 하여, 잔차 동작 학습이 시뮬레이션과 실제 역학 차이를 메우는 데 있어 잠재력을 보여줍니다.
- 연구 결과는 ASAP가 더 표현력 있고 민첩한 휴머노이드 로봇을 개발하기 위한 유망한 sim-to-real 방향을 제공함을 시사합니다.
