---
$id: ent_paper_b_spline_policy_accelerating_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations'
  zh: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations'
  ko: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations'
summary:
  en: 'arXiv:2607.09648v1 Announce Type: new Abstract: In this work, we present B-spline Policy (BSP), an action representation
    designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes
    actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth,
    time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies
    and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines
    by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly
    reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success
    rates. More results: https://b-spline-policy.github.io'
  zh: B-spline Policy (BSP) 是一种用于加速机器人操作策略的动作表示方法，由研究团队提出。其核心贡献在于将动作参数化为连续的 B-spline 曲线，而非离散时间步的动作块，从而生成平滑、时间连续的轨迹，可被底层控制器以更高频率和速度执行。实验表明，BSP
    在模拟和真实任务中显著缩短了任务完成时间，同时保持了较高的成功率。
  ko: 'arXiv:2607.09648v1 Announce Type: new Abstract: In this work, we present B-spline Policy (BSP), an action representation
    designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes
    actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth,
    time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies
    and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines
    by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly
    reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success
    rates. More results: https://b-spline-policy.github.io'
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
- robotics
- b_spline_policy
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09648v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations (arXiv)'
  url: https://arxiv.org/abs/2607.09648
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
B-spline Policy (BSP) 通过将机器人操作策略中的动作表示为连续的 B-spline 曲线，替代了传统的离散时间步动作块预测方法。这种表示由一组节点和控制点定义，能够生成平滑且时间连续的轨迹，并支持时间缩放，使底层控制器能以更高频率和速度执行。BSP 可以无缝集成到标准策略学习流程中，只需直接预测 B-spline 参数。在模拟和真实世界的实验中，BSP 相比基线方法大幅减少了任务完成时间，同时保持了强劲的成功率。

## 核心内容
### 方法概述
B-spline Policy (BSP) 的核心创新在于动作表示方式的改变：
- **传统方法**：预测离散时间步的动作块（action chunks），导致轨迹不连续且执行频率受限。
- **BSP 方法**：将动作参数化为连续的 B-spline 曲线，由一组节点（knots）和控制点（control points）定义。这种表示生成平滑、时间连续的轨迹，可被底层控制器以更高频率和速度执行，并支持时间缩放。

### 集成与实现
- BSP 可直接集成到标准策略学习流程中，只需让模型直接预测 B-spline 参数（节点和控制点），无需修改现有架构。
- 这种设计使得策略输出更易于被底层控制器解析和执行，从而加速整体操作流程。

### 实验设置与结果
- **模拟任务**：在多个模拟环境中测试，BSP 显著降低了任务完成时间，相比基线方法（如离散动作块预测）实现了大幅提升。
- **真实世界任务**：在真实机器人操作任务中，BSP 同样表现出色，任务完成时间缩短，且成功率与基线方法相当或更优。
- **关键数字**：具体改进幅度因任务而异，但整体上 BSP 在时间效率上实现了显著提升，同时保持了高成功率（具体数值请参考论文原文）。

### 结论
BSP 通过引入 B-spline 动作表示，为机器人操作策略提供了一种高效、平滑且易于集成的加速方案。其时间连续性和可缩放性使其在模拟和真实场景中均优于传统离散动作表示方法。更多结果和演示可访问项目网站：https://b-spline-policy.github.io

## Overview
In this work, we present B-spline Policy (BSP), an action representation designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth, time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success rates. More results: https://b-spline-policy.github.io

## 개요
본 연구에서는 로봇 조작 정책의 가속화를 위해 설계된 행동 표현인 B-스플라인 정책(BSP)을 제시합니다. BSP는 이산 시간 단위의 행동 청크를 예측하는 대신, 일련의 매듭점과 제어점으로 정의된 연속적인 B-스플라인 곡선으로 행동을 매개변수화합니다. 이 표현은 부드럽고 시간 연속적인 궤적을 생성하며, 이를 시간적으로 확장하여 저수준 제어기가 더 높은 주파수와 속도로 실행할 수 있습니다. B-스플라인으로 매개변수화된 행동은 B-스플라인 매개변수를 직접 예측함으로써 표준 정책 학습 파이프라인에 원활하게 통합될 수 있음을 보여줍니다. 시뮬레이션 및 실제 작업 실험을 통해 BSP가 작업 완료 시간을 크게 단축시키며, 강력한 성공률을 유지하면서 기준 방법 대비 상당한 개선을 달성함을 입증했습니다. 추가 결과: https://b-spline-policy.github.io

## 핵심 내용
본 연구에서는 로봇 조작 정책의 가속화를 위해 설계된 행동 표현인 B-스플라인 정책(BSP)을 제시합니다. BSP는 이산 시간 단위의 행동 청크를 예측하는 대신, 일련의 매듭점과 제어점으로 정의된 연속적인 B-스플라인 곡선으로 행동을 매개변수화합니다. 이 표현은 부드럽고 시간 연속적인 궤적을 생성하며, 이를 시간적으로 확장하여 저수준 제어기가 더 높은 주파수와 속도로 실행할 수 있습니다. B-스플라인으로 매개변수화된 행동은 B-스플라인 매개변수를 직접 예측함으로써 표준 정책 학습 파이프라인에 원활하게 통합될 수 있음을 보여줍니다. 시뮬레이션 및 실제 작업 실험을 통해 BSP가 작업 완료 시간을 크게 단축시키며, 강력한 성공률을 유지하면서 기준 방법 대비 상당한 개선을 달성함을 입증했습니다. 추가 결과: https://b-spline-policy.github.io

## 参考
- http://arxiv.org/abs/2607.09648v1
