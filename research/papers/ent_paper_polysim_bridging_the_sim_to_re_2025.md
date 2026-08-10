---
$id: ent_paper_polysim_bridging_the_sim_to_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization'
  zh: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization'
  ko: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization'
summary:
  en: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization is a 2025 work
    on sim-to-real for humanoid robots.'
  zh: PolySim 是一个2025年提出的面向人形机器人控制的 sim-to-real 训练平台，由研究团队开发。其核心贡献是通过多模拟器联合训练实现动力学域随机化，从而缩小模拟与现实之间的差距。关键参数显示，在 MuJoCo 上执行成功率比
    IsaacSim 基线提升 52.8%，并支持零样本部署到真实 Unitree G1 机器人。
  ko: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization is a 2025 work
    on sim-to-real for humanoid robots.'
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
- polysim
- sim_to_real
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01708v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (762 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PolySim: Bridging the Sim-to-Real Gap for Humanoid Control via Multi-Simulator Dynamics Randomization (arXiv)'
  url: https://arxiv.org/abs/2510.01708
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人全身控制策略在单一模拟器中训练时，常因模拟器归纳偏置（即每个模拟器固有的假设与局限）导致模拟与现实间的显著差异。PolySim 通过整合多个异构模拟器，在单次训练中并行启动不同引擎的环境，实现动力学层面的域随机化。理论分析表明，该方法比单模拟器训练能更紧地约束归纳偏置的上界。实验结果显示，PolySim 在 sim-to-sim 评估中大幅降低运动跟踪误差，并在真实 Unitree G1 机器人上实现零样本部署，无需额外微调。

## 核心内容
### 方法
- **核心思想**：通过跨多个模拟器联合训练策略，迫使控制器学习超越单一模拟器假设的通用动力学特征，从而缓解模拟器归纳偏置。
- **实现方式**：PolySim 平台集成多个异构模拟器（如 MuJoCo、IsaacSim 等），在单次训练中并行启动不同引擎的环境，实现动力学域随机化。

### 理论分析
- 证明多模拟器训练能产生比单模拟器训练更紧的归纳偏置上界，即更有效地限制模拟器假设带来的误差。

### 实验设置
- **评估指标**：运动跟踪误差（motion-tracking error）和执行成功率（execution success）。
- **基线对比**：以 IsaacSim 为基线，在 MuJoCo 上进行 sim-to-sim 评估。

### 关键数字
- 在 MuJoCo 上，PolySim 的执行成功率比 IsaacSim 基线提升 52.8%。
- 零样本部署到真实 Unitree G1 机器人，无需额外微调。

### 结论
- PolySim 有效缩小了 sim-to-real 差距，在 sim-to-sim 和 sim-to-real 场景中均表现优异。
- 代码将在论文接收后开源。

## Overview
Humanoid whole-body control (WBC) policies trained in simulation often suffer from the sim-to-real gap, which fundamentally arises from simulator inductive bias, the inherent assumptions and limitations of any single simulator. These biases lead to nontrivial discrepancies both across simulators and between simulation and the real world. To mitigate the effect of simulator inductive bias, the key idea is to train policies jointly across multiple simulators, encouraging the learned controller to capture dynamics that generalize beyond any single simulator's assumptions. We thus introduce PolySim, a WBC training platform that integrates multiple heterogeneous simulators. PolySim can launch parallel environments from different engines simultaneously within a single training run, thereby realizing dynamics-level domain randomization. Theoretically, we show that PolySim yields a tighter upper bound on simulator inductive bias than single-simulator training. In experiments, PolySim substantially reduces motion-tracking error in sim-to-sim evaluations; for example, on MuJoCo, it improves execution success by 52.8 over an IsaacSim baseline. PolySim further enables zero-shot deployment on a real Unitree G1 without additional fine-tuning, showing effective transfer from simulation to the real world. We will release the PolySim code upon acceptance of this work.

## 参考
- http://arxiv.org/abs/2510.01708v3

## 개요
휴머노이드 로봇 전신 제어 정책을 단일 시뮬레이터에서 훈련할 때, 시뮬레이터의 귀납적 편향(즉, 각 시뮬레이터에 내재된 가정과 한계)으로 인해 시뮬레이션과 현실 간의 상당한 차이가 발생하는 경우가 많습니다. PolySim은 여러 이기종 시뮬레이터를 통합하여 단일 훈련 중에 서로 다른 엔진의 환경을 병렬로 실행함으로써 동역학 수준의 도메인 무작위화를 구현합니다. 이론적 분석에 따르면, 이 방법은 단일 시뮬레이터 훈련보다 귀납적 편향의 상한을 더 엄격하게 제한할 수 있습니다. 실험 결과, PolySim은 sim-to-sim 평가에서 운동 추적 오류를 크게 줄였으며, 실제 Unitree G1 로봇에서 추가 미세 조정 없이 제로샷 배포를 달성했습니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 여러 시뮬레이터를 걸쳐 정책을 공동 훈련함으로써, 컨트롤러가 단일 시뮬레이터의 가정을 초월하는 일반적인 동역학 특성을 학습하도록 강제하여 시뮬레이터의 귀납적 편향을 완화합니다.
- **구현 방식**: PolySim 플랫폼은 여러 이기종 시뮬레이터(예: MuJoCo, IsaacSim 등)를 통합하며, 단일 훈련 중에 서로 다른 엔진의 환경을 병렬로 실행하여 동역학 수준의 도메인 무작위화를 구현합니다.

### 이론적 분석
- 다중 시뮬레이터 훈련이 단일 시뮬레이터 훈련보다 더 엄격한 귀납적 편향 상한을 생성할 수 있음을 증명합니다. 즉, 시뮬레이터 가정으로 인한 오류를 더 효과적으로 제한합니다.

### 실험 설정
- **평가 지표**: 운동 추적 오류(motion-tracking error) 및 실행 성공률(execution success).
- **기준 비교**: IsaacSim을 기준으로 MuJoCo에서 sim-to-sim 평가를 수행합니다.

### 주요 수치
- MuJoCo에서 PolySim의 실행 성공률은 IsaacSim 기준 대비 52.8% 향상되었습니다.
- 추가 미세 조정 없이 실제 Unitree G1 로봇에 제로샷 배포가 가능합니다.

### 결론
- PolySim은 sim-to-real 격차를 효과적으로 줄였으며, sim-to-sim 및 sim-to-real 시나리오 모두에서 우수한 성능을 보여줍니다.
- 코드는 논문 게재 후 오픈소스로 공개될 예정입니다.
