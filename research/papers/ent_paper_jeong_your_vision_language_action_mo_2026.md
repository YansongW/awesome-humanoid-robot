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
  zh: 本文在冻结的视觉-语言-动作模型中识别出稀疏的“导航头”，其注意力熵信号可指示轨迹偏离，从而实现了无需训练的异常检测器和轻量强化学习回退机制。在VLN-CE R2R与RxR上达到44.6%的偏离检测率和11.7%的误检率，并在AgileX
    Scout 2.0移动机器人上验证了完整的检测-恢复流程。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.13782v1.
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
Vision-Language-Action (VLA) models have demonstrated strong potential for predicting semantic actions in navigation tasks, demonstrating the ability to reason over complex linguistic instructions and visual contexts. However, they are fundamentally hindered by visual-reasoning hallucinations that lead to trajectory deviations. Addressing this issue has conventionally required training external critic modules or relying on complex uncertainty heuristics. In this work, we discover that monitoring a few attention heads within a frozen VLA model can accurately detect path deviations without incurring additional computational overhead. We refer to these heads, which inherently capture the spatiotemporal causality between historical visual sequences and linguistic instructions, as Navigation Heads. Using these heads, we propose an intuitive, training-free anomaly-detection framework that monitors their signals to detect hallucinations in real time. Surprisingly, among over a thousand attention heads, a combination of just three is sufficient to achieve a 44.6 % deviation detection rate with a low false-positive rate of 11.7 %. Furthermore, upon detecting a deviation, we bypass the heavy VLA model and trigger a lightweight Reinforcement Learning (RL) policy to safely execute a shortest-path rollback. By integrating this entire detection-to-recovery pipeline onto a physical robot, we demonstrate its practical robustness. All source code will be publicly available.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated strong potential for predicting semantic actions in navigation tasks, demonstrating the ability to reason over complex linguistic instructions and visual contexts. However, they are fundamentally hindered by visual-reasoning hallucinations that lead to trajectory deviations. Addressing this issue has conventionally required training external critic modules or relying on complex uncertainty heuristics. In this work, we discover that monitoring a few attention heads within a frozen VLA model can accurately detect path deviations without incurring additional computational overhead. We refer to these heads, which inherently capture the spatiotemporal causality between historical visual sequences and linguistic instructions, as Navigation Heads. Using these heads, we propose an intuitive, training-free anomaly-detection framework that monitors their signals to detect hallucinations in real time. Surprisingly, among over a thousand attention heads, a combination of just three is sufficient to achieve a 44.6 % deviation detection rate with a low false-positive rate of 11.7 %. Furthermore, upon detecting a deviation, we bypass the heavy VLA model and trigger a lightweight Reinforcement Learning (RL) policy to safely execute a shortest-path rollback. By integrating this entire detection-to-recovery pipeline onto a physical robot, we demonstrate its practical robustness. All source code will be publicly available.

## 参考
- http://arxiv.org/abs/2603.13782v1

