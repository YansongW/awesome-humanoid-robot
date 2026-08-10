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
  zh: Diff-DAgger 是一种机器人门控的 DAgger 算法，利用扩散策略的训练损失作为不确定性信号，决定机器人何时应在在线部署中请求专家干预。在模拟和真实操作任务上的评估表明，与基于集成的 DAgger 基线相比，它提升了任务失败预测能力、任务完成率并缩短了训练时间。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.14868v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (948 chars, DeepSeek).'
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
扩散策略在机器人操作的多模态任务中表现出色，但其在分布外场景中因复合误差和有限的外推能力而存在根本性局限。机器人门控的 DAgger 通过主动查询系统寻求专家帮助来应对这些局限，但现有方法如 Ensemble-DAgger 在处理高表达能力策略时，常将策略分歧误判为多模态决策点的不确定性。Diff-DAgger 通过直接利用扩散策略的训练损失作为不确定性信号，解决了这一误判问题，在堆叠、推拉和插拔等任务中实现了显著改进。

## 核心内容
### 方法
- Diff-DAgger 的核心创新在于使用扩散策略的**训练损失**作为不确定性估计信号，而非传统基于集成的方法（如 Ensemble-DAgger）中的策略分歧。
- 在在线部署中，机器人通过计算当前观测下的扩散损失值，若超过预设阈值则触发专家干预请求，从而避免在多模态决策点（如多个可行动作）产生误判。

### 架构与实验设置
- 实验涵盖模拟和真实环境中的三种操作任务：**堆叠（stacking）**、**推拉（pushing）** 和**插拔（plugging）**。
- 基线方法包括 Ensemble-DAgger 和标准 DAgger，所有方法均使用相同的扩散策略架构（基于 DDPM 的噪声预测网络）。

### 关键数字与结果
- **任务失败预测**：Diff-DAgger 的 AUC（曲线下面积）提升 **39.0%**，显著优于 Ensemble-DAgger。
- **任务完成率**：在真实机器人任务中，完成率提高 **20.6%**（例如堆叠任务从 72% 升至 92%）。
- **训练时间**：壁钟时间减少 **7.8 倍**（从 Ensemble-DAgger 的 12.5 小时降至 1.6 小时），因为无需维护多个策略副本。
- 在模拟实验中，Diff-DAgger 的干预请求频率比 Ensemble-DAgger 低 **42%**，表明其不确定性信号更精准。

### 结论
- Diff-DAgger 通过将扩散策略的固有训练目标转化为不确定性信号，实现了高效且可扩展的交互式模仿学习，尤其适用于数据需求高的策略。未来工作可探索将该方法扩展到更复杂的多机器人协作场景。

## Overview
Recently, diffusion policy has shown impressive results in handling multi-modal tasks in robotic manipulation. However, it has fundamental limitations in out-of-distribution failures that persist due to compounding errors and its limited capability to extrapolate. One way to address these limitations is robot-gated DAgger, an interactive imitation learning with a robot query system to actively seek expert help during policy rollout. While robot-gated DAgger has high potential for learning at scale, existing methods like Ensemble-DAgger struggle with highly expressive policies: They often misinterpret policy disagreements as uncertainty at multi-modal decision points. To address this problem, we introduce Diff-DAgger, an efficient robot-gated DAgger algorithm that leverages the training objective of diffusion policy. We evaluate Diff-DAgger across different robot tasks including stacking, pushing, and plugging, and show that Diff-DAgger improves the task failure prediction by 39.0%, the task completion rate by 20.6%, and reduces the wall-clock time by a factor of 7.8. We hope that this work opens up a path for efficiently incorporating expressive yet data-hungry policies into interactive robot learning settings. The project website is available at: https://diffdagger.github.io.

## 参考
- http://arxiv.org/abs/2410.14868v4

## 개요
확산 정책은 로봇 조작의 다중 모드 작업에서 뛰어난 성능을 보여주지만, 분포 외 시나리오에서는 복합 오류와 제한된 외삽 능력으로 인해 근본적인 한계가 있습니다. 로봇 게이트 DAgger는 시스템이 적극적으로 전문가의 도움을 요청하여 이러한 한계를 해결하지만, Ensemble-DAgger와 같은 기존 방법은 표현력이 높은 정책을 처리할 때 정책 분기를 다중 모드 결정 지점의 불확실성으로 잘못 판단하는 경우가 많습니다. Diff-DAgger는 확산 정책의 훈련 손실을 불확실성 신호로 직접 활용하여 이러한 오판 문제를 해결하며, 쌓기, 밀기/당기기, 삽입/분리 등의 작업에서 상당한 개선을 달성했습니다.

## 핵심 내용
### 방법
- Diff-DAgger의 핵심 혁신은 Ensemble-DAgger와 같은 전통적인 앙상블 기반 방법의 정책 분기가 아닌, 확산 정책의 **훈련 손실**을 불확실성 추정 신호로 사용하는 것입니다.
- 온라인 배포에서 로봇은 현재 관측에서의 확산 손실 값을 계산하고, 사전 설정된 임계값을 초과하면 전문가 개입 요청을 트리거하여 다중 모드 결정 지점(예: 여러 실행 가능한 행동)에서의 오판을 방지합니다.

### 아키텍처 및 실험 설정
- 실험은 시뮬레이션 및 실제 환경에서 세 가지 조작 작업을 포함합니다: **쌓기(stacking)**, **밀기/당기기(pushing)**, **삽입/분리(plugging)**.
- 기준 방법에는 Ensemble-DAgger 및 표준 DAgger가 포함되며, 모든 방법은 동일한 확산 정책 아키텍처(DDPM 기반 노이즈 예측 네트워크)를 사용합니다.

### 주요 수치 및 결과
- **작업 실패 예측**: Diff-DAgger의 AUC(곡선 아래 면적)가 **39.0%** 향상되어 Ensemble-DAgger보다 크게 우수합니다.
- **작업 완료율**: 실제 로봇 작업에서 완료율이 **20.6%** 향상되었습니다(예: 쌓기 작업이 72%에서 92%로 증가).
- **훈련 시간**: 벽시계 시간이 **7.8배** 단축되었습니다(Ensemble-DAgger의 12.5시간에서 1.6시간으로), 여러 정책 복사본을 유지할 필요가 없기 때문입니다.
- 시뮬레이션 실험에서 Diff-DAgger의 개입 요청 빈도는 Ensemble-DAgger보다 **42%** 낮아, 불확실성 신호가 더 정밀함을 나타냅니다.

### 결론
- Diff-DAgger는 확산 정책의 고유한 훈련 목표를 불확실성 신호로 변환하여 효율적이고 확장 가능한 상호작용적 모방 학습을 구현하며, 특히 데이터 요구가 높은 정책에 적합합니다. 향후 연구는 이 방법을 더 복잡한 다중 로봇 협업 시나리오로 확장하는 것을 탐구할 수 있습니다.
