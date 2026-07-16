---
$id: ent_paper_lee_diff_dagger_uncertainty_estima_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation'
  zh: Diff-DAgger：面向机器人操作的扩散策略不确定性估计
  ko: 'Diff-DAgger: 로봇 조작을 위한 확산 정책의 불확실성 추정'
summary:
  en: Diff-DAgger is a robot-gated DAgger algorithm that uses the diffusion policy training loss as an uncertainty signal
    to decide when a robot should request expert intervention during online rollout. Evaluations on simulated and real manipulation
    tasks show that it improves task-failure prediction, task completion rate, and wall-clock training time compared to ensemble-based
    DAgger baselines.
  zh: Diff-DAgger是一种机器人门控DAgger算法，将扩散策略的训练损失作为不确定信号，用于在在线展开过程中决定机器人何时请求专家干预。在仿真和真实操作任务上的评估表明，与基于集成的DAgger基线相比，它提高了任务失败预测、任务完成率并缩短了训练挂钟时间。
  ko: Diff-DAgger는 확산 정책의 훈련 손실을 불확실성 신호로 사용하여 온라인 롤아웃 중 로봇이 전문가 개입을 요청해야 하는 시점을 결정하는 로봇 게이트 DAgger 알고리즘이다. 시뮬레이션 및 실제 조작
    작업에 대한 평가에서 앙상블 기반 DAgger 기준과 비교하여 작업 실패 예측, 작업 완료율 및 훈련 벽시계 시간을 개선한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_policy
- daggar
- robot_gated_dagger
- interactive_imitation_learning
- uncertainty_estimation
- visuomotor_policy
- out_of_distribution_detection
- manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14868v4.
sources:
- id: src_001
  type: paper
  title: 'Diff-DAgger: Uncertainty Estimation with Diffusion Policy for Robotic Manipulation'
  url: https://arxiv.org/abs/2410.14868
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation. However, it has fundamental limitations in out-of-distribution failures that persist due to compounding errors and its limited capability to extrapolate. One way to address these limitations is robot-gated DAgger, an interactive imitation learning with a robot query system to actively seek expert help during policy rollout. While robot-gated DAgger has high potential for learning at scale, existing methods like Ensemble-DAgger struggle with highly expressive policies: They often misinterpret policy disagreements as uncertainty at multi-modal decision points. To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy. We evaluate Diff-DAgger across different robot tasks including stacking, pushing, and plugging, and show that Diff-DAgger improves the task failure prediction by 39.0%, the task completion rate by 20.6%, and reduces the wall-clock time by a factor of 7.8. We hope that this work opens up a path for efficiently incorporating expressive yet data-hungry policies into interactive robot learning settings. The project website is available at: https://diffdagger.github.io.

## 核心内容
Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation. However, it has fundamental limitations in out-of-distribution failures that persist due to compounding errors and its limited capability to extrapolate. One way to address these limitations is robot-gated DAgger, an interactive imitation learning with a robot query system to actively seek expert help during policy rollout. While robot-gated DAgger has high potential for learning at scale, existing methods like Ensemble-DAgger struggle with highly expressive policies: They often misinterpret policy disagreements as uncertainty at multi-modal decision points. To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy. We evaluate Diff-DAgger across different robot tasks including stacking, pushing, and plugging, and show that Diff-DAgger improves the task failure prediction by 39.0%, the task completion rate by 20.6%, and reduces the wall-clock time by a factor of 7.8. We hope that this work opens up a path for efficiently incorporating expressive yet data-hungry policies into interactive robot learning settings. The project website is available at: https://diffdagger.github.io.

## 参考
- http://arxiv.org/abs/2410.14868v4

## Overview
Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation. However, it has fundamental limitations in out-of-distribution failures that persist due to compounding errors and its limited capability to extrapolate. One way to address these limitations is robot-gated DAgger, an interactive imitation learning with a robot query system to actively seek expert help during policy rollout. While robot-gated DAgger has high potential for learning at scale, existing methods like Ensemble-DAgger struggle with highly expressive policies: They often misinterpret policy disagreements as uncertainty at multi-modal decision points. To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy. We evaluate Diff-DAgger across different robot tasks including stacking, pushing, and plugging, and show that Diff-DAgger improves the task failure prediction by 39.0%, the task completion rate by 20.6%, and reduces the wall-clock time by a factor of 7.8. We hope that this work opens up a path for efficiently incorporating expressive yet data-hungry policies into interactive robot learning settings. The project website is available at: https://diffdagger.github.io.

## Content
Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation. However, it has fundamental limitations in out-of-distribution failures that persist due to compounding errors and its limited capability to extrapolate. One way to address these limitations is robot-gated DAgger, an interactive imitation learning with a robot query system to actively seek expert help during policy rollout. While robot-gated DAgger has high potential for learning at scale, existing methods like Ensemble-DAgger struggle with highly expressive policies: They often misinterpret policy disagreements as uncertainty at multi-modal decision points. To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy. We evaluate Diff-DAgger across different robot tasks including stacking, pushing, and plugging, and show that Diff-DAgger improves the task failure prediction by 39.0%, the task completion rate by 20.6%, and reduces the wall-clock time by a factor of 7.8. We hope that this work opens up a path for efficiently incorporating expressive yet data-hungry policies into interactive robot learning settings. The project website is available at: https://diffdagger.github.io.

## 개요
최근 확산 정책(diffusion policy)은 로봇 조작 분야에서 다중 모드 작업을 처리하는 데 인상적인 결과를 보여주고 있습니다. 그러나 이는 오류 누적과 제한된 외삽 능력으로 인해 지속되는 분포 외 실패(out-of-distribution failures)라는 근본적인 한계를 가지고 있습니다. 이러한 한계를 해결하는 한 가지 방법은 로봇 게이트 DAgger(robot-gated DAgger)로, 정책 롤아웃 중에 전문가의 도움을 적극적으로 요청하는 로봇 질의 시스템을 갖춘 상호작용적 모방 학습입니다. 로봇 게이트 DAgger는 대규모 학습에 높은 잠재력을 가지고 있지만, Ensemble-DAgger와 같은 기존 방법은 표현력이 높은 정책에서 어려움을 겪습니다. 이들은 종종 다중 모드 의사 결정 지점에서 정책 불일치를 불확실성으로 잘못 해석합니다. 이 문제를 해결하기 위해, 우리는 확산 정책의 훈련 목표를 활용하는 효율적인 로봇 게이트 DAgger 알고리즘인 Diff-DAgger를 소개합니다. 우리는 쌓기(stacking), 밀기(pushing), 끼우기(plugging)를 포함한 다양한 로봇 작업에서 Diff-DAgger를 평가했으며, Diff-DAgger가 작업 실패 예측을 39.0% 개선하고, 작업 완료율을 20.6% 향상시키며, 벽시계 시간(wall-clock time)을 7.8배 단축함을 보여줍니다. 이 연구가 표현력이 높지만 데이터를 많이 필요로 하는 정책을 상호작용적 로봇 학습 환경에 효율적으로 통합하는 길을 열기를 바랍니다. 프로젝트 웹사이트는 https://diffdagger.github.io 에서 확인할 수 있습니다.

## 핵심 내용
최근 확산 정책(diffusion policy)은 로봇 조작 분야에서 다중 모드 작업을 처리하는 데 인상적인 결과를 보여주고 있습니다. 그러나 이는 오류 누적과 제한된 외삽 능력으로 인해 지속되는 분포 외 실패(out-of-distribution failures)라는 근본적인 한계를 가지고 있습니다. 이러한 한계를 해결하는 한 가지 방법은 로봇 게이트 DAgger(robot-gated DAgger)로, 정책 롤아웃 중에 전문가의 도움을 적극적으로 요청하는 로봇 질의 시스템을 갖춘 상호작용적 모방 학습입니다. 로봇 게이트 DAgger는 대규모 학습에 높은 잠재력을 가지고 있지만, Ensemble-DAgger와 같은 기존 방법은 표현력이 높은 정책에서 어려움을 겪습니다. 이들은 종종 다중 모드 의사 결정 지점에서 정책 불일치를 불확실성으로 잘못 해석합니다. 이 문제를 해결하기 위해, 우리는 확산 정책의 훈련 목표를 활용하는 효율적인 로봇 게이트 DAgger 알고리즘인 Diff-DAgger를 소개합니다. 우리는 쌓기(stacking), 밀기(pushing), 끼우기(plugging)를 포함한 다양한 로봇 작업에서 Diff-DAgger를 평가했으며, Diff-DAgger가 작업 실패 예측을 39.0% 개선하고, 작업 완료율을 20.6% 향상시키며, 벽시계 시간(wall-clock time)을 7.8배 단축함을 보여줍니다. 이 연구가 표현력이 높지만 데이터를 많이 필요로 하는 정책을 상호작용적 로봇 학습 환경에 효율적으로 통합하는 길을 열기를 바랍니다. 프로젝트 웹사이트는 https://diffdagger.github.io 에서 확인할 수 있습니다.
