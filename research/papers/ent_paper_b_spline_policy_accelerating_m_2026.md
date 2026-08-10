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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09648v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (915 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.09648v1

## 개요
B-spline Policy (BSP)는 로봇 조작 정책에서 동작을 연속적인 B-spline 곡선으로 표현하여, 기존의 이산 시간 단계 동작 블록 예측 방법을 대체합니다. 이러한 표현은 일련의 노드와 제어점으로 정의되며, 매끄럽고 시간 연속적인 궤적을 생성하고 시간 스케일링을 지원하여 하위 제어기가 더 높은 주파수와 속도로 실행할 수 있게 합니다. BSP는 표준 정책 학습 흐름에 원활하게 통합될 수 있으며, B-spline 파라미터를 직접 예측하기만 하면 됩니다. 시뮬레이션 및 실제 세계 실험에서 BSP는 기준 방법에 비해 작업 완료 시간을 크게 줄이면서도 강력한 성공률을 유지했습니다.

## 핵심 내용
### 방법 개요
B-spline Policy (BSP)의 핵심 혁신은 동작 표현 방식의 변화에 있습니다:
- **기존 방법**: 이산 시간 단계의 동작 블록(action chunks)을 예측하여 궤적이 불연속적이고 실행 주파수가 제한됩니다.
- **BSP 방법**: 동작을 일련의 노드(knots)와 제어점(control points)으로 정의된 연속적인 B-spline 곡선으로 매개변수화합니다. 이러한 표현은 매끄럽고 시간 연속적인 궤적을 생성하며, 하위 제어기가 더 높은 주파수와 속도로 실행할 수 있고 시간 스케일링을 지원합니다.

### 통합 및 구현
- BSP는 표준 정책 학습 흐름에 직접 통합될 수 있으며, 모델이 B-spline 파라미터(노드 및 제어점)를 직접 예측하기만 하면 기존 아키텍처를 수정할 필요가 없습니다.
- 이러한 설계는 정책 출력을 하위 제어기가 더 쉽게 해석하고 실행할 수 있게 하여 전체 조작 프로세스를 가속화합니다.

### 실험 설정 및 결과
- **시뮬레이션 작업**: 여러 시뮬레이션 환경에서 테스트한 결과, BSP는 기준 방법(예: 이산 동작 블록 예측)에 비해 작업 완료 시간을 크게 줄였습니다.
- **실제 세계 작업**: 실제 로봇 조작 작업에서도 BSP는 뛰어난 성능을 보였으며, 작업 완료 시간이 단축되고 성공률은 기준 방법과 동등하거나 더 우수했습니다.
- **주요 수치**: 구체적인 개선 폭은 작업에 따라 다르지만, 전반적으로 BSP는 시간 효율성에서 상당한 개선을 달성하면서 높은 성공률을 유지했습니다(구체적인 수치는 논문 원문을 참조하세요).

### 결론
BSP는 B-spline 동작 표현을 도입하여 로봇 조작 정책에 효율적이고 매끄러우며 통합이 용이한 가속화 방안을 제공합니다. 시간 연속성과 확장성 덕분에 시뮬레이션 및 실제 시나리오 모두에서 기존의 이산 동작 표현 방법보다 우수합니다. 더 많은 결과와 데모는 프로젝트 웹사이트에서 확인할 수 있습니다: https://b-spline-policy.github.io
