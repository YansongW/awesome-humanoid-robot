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

