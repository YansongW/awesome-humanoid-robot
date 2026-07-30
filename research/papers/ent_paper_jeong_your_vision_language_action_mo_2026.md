---
$id: ent_paper_jeong_your_vision_language_action_mo_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection
  zh: 你的视觉-语言-动作模型已具备路径偏离检测的注意力头
  ko: 당신의 비전-언어-액션 모델에는 이미 경로 편차 탐지를 위한 어텐션 헤드가 있다
summary:
  en: This paper identifies sparse 'Navigation Heads' in a frozen Vision-Language-Action model whose attention-entropy signals
    indicate trajectory deviations, enabling a training-free anomaly detector and lightweight RL rollback for navigation.
    It reports a 44.6% deviation-detection rate with an 11.7% false-positive rate on VLN-CE R2R and RxR, and validates the
    full detection-to-recovery pipeline on an AgileX Scout 2.0 mobile robot.
  zh: 本文发现冻结的Vision-Language-Action (VLA)模型中存在稀疏的“Navigation Heads”，其注意力熵信号可指示轨迹偏差，从而无需训练即可实现异常检测，并配合轻量级RL回滚策略完成导航恢复。该方法在VLN-CE
    R2R和RxR基准上达到44.6%的偏差检测率与11.7%的假阳性率，并在AgileX Scout 2.0移动机器人上验证了完整检测-恢复流程。
  ko: 본 논문은 고정된 비전-언어-액션(VLA) 모델 내 어텐션 엔트로피 신호가 궤적 편차를 나타내는 소수의 '네비게이션 헤드(Navigation Heads)'를 식별하여, 학습 불필요 이상 탐지기와 경량 RL 롤백을
    제안한다. VLN-CE R2R 및 RxR에서 44.6%의 편차 탐지율과 11.7%의 오탐률을 보였으며, AgileX Scout 2.0 이동 로봇에서 탐지-회복 파이프라인을 검증했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- navigation_heads
- attention_entropy
- hallucination_detection
- anomaly_detection
- reinforcement_learning
- robot_navigation
- vln_ce
- r2r
- rxr
- navila
- ros2
- mobile_robot
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.13782v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection
  url: https://arxiv.org/abs/2603.13782
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
本研究针对VLA模型在导航任务中因视觉推理幻觉导致的轨迹偏差问题，提出一种无需额外训练的检测方法。通过分析冻结VLA模型中上千个注意力头，发现仅需组合三个特定头（称为Navigation Heads）即可实时监测偏差信号，其注意力熵变化能有效区分正常与异常轨迹。该方法在VLN-CE基准上以低假阳性率实现高检测率，并在检测到偏差后切换至轻量级强化学习策略执行最短路径回滚，最终在实体机器人上验证了端到端管线的鲁棒性。

## 核心内容
### 核心发现与Navigation Heads
- 在冻结的VLA模型中，存在少量注意力头（Navigation Heads）能捕捉历史视觉序列与语言指令之间的时空因果关系，其注意力熵在轨迹偏离时显著变化。
- 实验表明，仅需组合3个Navigation Heads即可实现有效检测，无需训练额外模块或依赖复杂不确定性估计。

### 方法架构
- **训练无关的异常检测**：实时监控Navigation Heads的注意力熵信号，当熵值超过阈值时触发偏差警报。
- **轻量级RL回滚策略**：检测到偏差后，绕过计算密集的VLA模型，启用预训练的强化学习策略执行最短路径回滚，恢复至正确轨迹。

### 实验设置与关键结果
- **基准测试**：在VLN-CE的R2R和RxR数据集上评估，检测率达44.6%，假阳性率仅11.7%。
- **实体机器人验证**：在AgileX Scout 2.0移动机器人上部署完整检测-恢复管线，验证了实际场景中的鲁棒性。
- **对比优势**：相比传统方法（需训练外部评论模块或依赖启发式规则），本方法零额外训练成本且计算开销极低。

### 结论
本文证明冻结VLA模型中稀疏的Navigation Heads可作为高效偏差检测器，结合轻量级RL回滚策略形成完整的导航纠错方案，为降低VLA模型幻觉影响提供了实用路径。所有代码将开源。

## Overview
Vision-Language-Action (VLA) models have demonstrated strong potential for predicting semantic actions in navigation tasks, demonstrating the ability to reason over complex linguistic instructions and visual contexts. However, they are fundamentally hindered by visual-reasoning hallucinations that lead to trajectory deviations. Addressing this issue has conventionally required training external critic modules or relying on complex uncertainty heuristics. In this work, we discover that monitoring a few attention heads within a frozen VLA model can accurately detect path deviations without incurring additional computational overhead. We refer to these heads, which inherently capture the spatiotemporal causality between historical visual sequences and linguistic instructions, as Navigation Heads. Using these heads, we propose an intuitive, training-free anomaly-detection framework that monitors their signals to detect hallucinations in real time. Surprisingly, among over a thousand attention heads, a combination of just three is sufficient to achieve a 44.6 % deviation detection rate with a low false-positive rate of 11.7 %. Furthermore, upon detecting a deviation, we bypass the heavy VLA model and trigger a lightweight Reinforcement Learning (RL) policy to safely execute a shortest-path rollback. By integrating this entire detection-to-recovery pipeline onto a physical robot, we demonstrate its practical robustness. All source code will be publicly available.

## Overview
Vision-Language-Action (VLA) models have demonstrated strong potential for predicting semantic actions in navigation tasks, demonstrating the ability to reason over complex linguistic instructions and visual contexts. However, they are fundamentally hindered by visual-reasoning hallucinations that lead to trajectory deviations. Addressing this issue has conventionally required training external critic modules or relying on complex uncertainty heuristics. In this work, we discover that monitoring a few attention heads within a frozen VLA model can accurately detect path deviations without incurring additional computational overhead. We refer to these heads, which inherently capture the spatiotemporal causality between historical visual sequences and linguistic instructions, as Navigation Heads. Using these heads, we propose an intuitive, training-free anomaly-detection framework that monitors their signals to detect hallucinations in real time. Surprisingly, among over a thousand attention heads, a combination of just three is sufficient to achieve a 44.6% deviation detection rate with a low false-positive rate of 11.7%. Furthermore, upon detecting a deviation, we bypass the heavy VLA model and trigger a lightweight Reinforcement Learning (RL) policy to safely execute a shortest-path rollback. By integrating this entire detection-to-recovery pipeline onto a physical robot, we demonstrate its practical robustness. All source code will be publicly available.

## Content
Vision-Language-Action (VLA) models have demonstrated strong potential for predicting semantic actions in navigation tasks, demonstrating the ability to reason over complex linguistic instructions and visual contexts. However, they are fundamentally hindered by visual-reasoning hallucinations that lead to trajectory deviations. Addressing this issue has conventionally required training external critic modules or relying on complex uncertainty heuristics. In this work, we discover that monitoring a few attention heads within a frozen VLA model can accurately detect path deviations without incurring additional computational overhead. We refer to these heads, which inherently capture the spatiotemporal causality between historical visual sequences and linguistic instructions, as Navigation Heads. Using these heads, we propose an intuitive, training-free anomaly-detection framework that monitors their signals to detect hallucinations in real time. Surprisingly, among over a thousand attention heads, a combination of just three is sufficient to achieve a 44.6% deviation detection rate with a low false-positive rate of 11.7%. Furthermore, upon detecting a deviation, we bypass the heavy VLA model and trigger a lightweight Reinforcement Learning (RL) policy to safely execute a shortest-path rollback. By integrating this entire detection-to-recovery pipeline onto a physical robot, we demonstrate its practical robustness. All source code will be publicly available.

## 개요
Vision-Language-Action (VLA) 모델은 탐색 작업에서 의미론적 행동을 예측하는 데 강력한 잠재력을 보여주며, 복잡한 언어 명령과 시각적 맥락을 추론하는 능력을 입증했습니다. 그러나 이들은 궤적 이탈을 초래하는 시각적 추론 환각(visual-reasoning hallucinations)에 의해 근본적으로 제약을 받습니다. 이 문제를 해결하기 위해 기존에는 외부 비평가 모듈을 학습시키거나 복잡한 불확실성 휴리스틱에 의존해야 했습니다. 본 연구에서는 고정된 VLA 모델 내의 몇몇 어텐션 헤드를 모니터링함으로써 추가적인 계산 오버헤드 없이 경로 이탈을 정확히 감지할 수 있음을 발견했습니다. 우리는 역사적 시각 시퀀스와 언어 명령 간의 시공간적 인과성을 본질적으로 포착하는 이러한 헤드를 내비게이션 헤드(Navigation Heads)라고 명명합니다. 이 헤드들을 활용하여, 우리는 직관적이고 학습이 필요 없는 이상 탐지 프레임워크를 제안하며, 이는 헤드의 신호를 모니터링하여 실시간으로 환각을 감지합니다. 놀랍게도, 수천 개의 어텐션 헤드 중 단 세 개의 조합만으로도 44.6%의 이탈 감지율과 11.7%의 낮은 오탐률을 달성할 수 있습니다. 또한, 이탈이 감지되면 무거운 VLA 모델을 우회하고 경량 강화 학습(RL) 정책을 트리거하여 안전하게 최단 경로 롤백을 실행합니다. 이 전체 감지-복구 파이프라인을 물리적 로봇에 통합함으로써, 우리는 그 실용적 견고성을 입증합니다. 모든 소스 코드는 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 탐색 작업에서 의미론적 행동을 예측하는 데 강력한 잠재력을 보여주며, 복잡한 언어 명령과 시각적 맥락을 추론하는 능력을 입증했습니다. 그러나 이들은 궤적 이탈을 초래하는 시각적 추론 환각에 의해 근본적으로 제약을 받습니다. 이 문제를 해결하기 위해 기존에는 외부 비평가 모듈을 학습시키거나 복잡한 불확실성 휴리스틱에 의존해야 했습니다. 본 연구에서는 고정된 VLA 모델 내의 몇몇 어텐션 헤드를 모니터링함으로써 추가적인 계산 오버헤드 없이 경로 이탈을 정확히 감지할 수 있음을 발견했습니다. 우리는 역사적 시각 시퀀스와 언어 명령 간의 시공간적 인과성을 본질적으로 포착하는 이러한 헤드를 내비게이션 헤드라고 명명합니다. 이 헤드들을 활용하여, 우리는 직관적이고 학습이 필요 없는 이상 탐지 프레임워크를 제안하며, 이는 헤드의 신호를 모니터링하여 실시간으로 환각을 감지합니다. 놀랍게도, 수천 개의 어텐션 헤드 중 단 세 개의 조합만으로도 44.6%의 이탈 감지율과 11.7%의 낮은 오탐률을 달성할 수 있습니다. 또한, 이탈이 감지되면 무거운 VLA 모델을 우회하고 경량 강화 학습 정책을 트리거하여 안전하게 최단 경로 롤백을 실행합니다. 이 전체 감지-복구 파이프라인을 물리적 로봇에 통합함으로써, 우리는 그 실용적 견고성을 입증합니다. 모든 소스 코드는 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2603.13782v1
