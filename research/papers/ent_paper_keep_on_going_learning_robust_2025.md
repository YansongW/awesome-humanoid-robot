---
$id: ent_paper_keep_on_going_learning_robust_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training'
  zh: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training'
  ko: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training'
summary:
  en: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 本文提出选择性对抗攻击鲁棒训练（SA2RT）方法，用于提升人形机器人运动技能的鲁棒性。该方法通过学习在攻击预算约束下稀疏扰动最脆弱的状态与动作，避免保守过拟合，并在Unitree G1人形机器人上验证了效果。实验表明，对抗训练策略使地形穿越成功率提升40%，轨迹跟踪误差降低32%，并保持了长时域运动性能。
  ko: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- keep_on_going
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.08303v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (583 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Keep on Going: Learning Robust Humanoid Motion Skills via Selective Adversarial Training (arXiv)'
  url: https://arxiv.org/abs/2507.08303
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人在长时间运行中，强化学习运动策略常因传感器/执行器噪声和真实世界干扰而失去稳定性。为此，研究者提出SA2RT框架，通过非零和交替优化，让对抗器学习识别并稀疏攻击最脆弱的状态与动作，从而暴露真实弱点而不引发保守过拟合。该方法在Unitree G1人形机器人的感知运动与全身控制任务中验证，显著提升了地形穿越成功率和轨迹跟踪精度，并维持了长时域运动能力。

## 核心内容
### 方法
- **SA2RT框架**：采用选择性对抗攻击，在攻击预算约束下，对抗器学习识别并稀疏扰动最脆弱的状态与动作，避免传统对抗训练中的保守过拟合。
- **非零和交替优化**：运动策略与对抗器交替优化，策略持续强化以对抗最强发现的攻击，形成动态博弈。

### 实验设置
- **平台**：Unitree G1人形机器人。
- **任务**：感知运动（地形穿越）与全身控制（轨迹跟踪）。
- **对比**：与标准RL策略及传统对抗训练方法对比。

### 关键结果
- **地形穿越成功率**：对抗训练策略提升40%。
- **轨迹跟踪误差**：降低32%。
- **长时域性能**：在长时间运行中保持运动与跟踪稳定性，未出现性能退化。

### 结论
选择性对抗攻击是驱动学习鲁棒、长时域人形机器人运动技能的有效方法，SA2RT框架在真实机器人上验证了其优越性。

## Overview
Humanoid robots are expected to operate reliably over long horizons while executing versatile whole-body skills. Yet Reinforcement Learning (RL) motion policies typically lose stability under prolonged operation, sensor/actuator noise, and real world disturbances. In this work, we propose a Selective Adversarial Attack for Robust Training (SA2RT) to enhance the robustness of motion skills. The adversary is learned to identify and sparsely perturb the most vulnerable states and actions under an attack-budget constraint, thereby exposing true weakness without inducing conservative overfitting. The resulting non-zero sum, alternating optimization continually strengthens the motion policy against the strongest discovered attacks. We validate our approach on the Unitree G1 humanoid robot across perceptive locomotion and whole-body control tasks. Experimental results show that adversarially trained policies improve the terrain traversal success rate by 40%, reduce the trajectory tracking error by 32%, and maintain long horizon mobility and tracking performance. Together, these results demonstrate that selective adversarial attacks are an effective driver for learning robust, long horizon humanoid motion skills.

## 参考
- http://arxiv.org/abs/2507.08303v3

## 개요
휴머노이드 로봇이 장시간 작동할 때, 강화학습 운동 정책은 종종 센서/액추에이터 노이즈와 실제 세계의 간섭으로 인해 안정성을 잃습니다. 이를 해결하기 위해 연구자들은 SA2RT 프레임워크를 제안했으며, 비제로섬 교대 최적화를 통해 적대자가 가장 취약한 상태와 행동을 식별하고 희소하게 공격하도록 학습시켜, 보수적 과적합을 유발하지 않으면서 실제 약점을 드러내게 합니다. 이 방법은 Unitree G1 휴머노이드 로봇의 지각 운동 및 전신 제어 작업에서 검증되었으며, 지형 통과 성공률과 궤적 추적 정밀도를 크게 향상시키고 장시간 운동 능력을 유지했습니다.

## 핵심 내용
### 방법
- **SA2RT 프레임워크**: 선택적 적대 공격을 채택하여, 공격 예산 제약 하에 적대자가 가장 취약한 상태와 행동을 식별하고 희소하게 교란시켜, 전통적인 적대 훈련에서의 보수적 과적합을 피합니다.
- **비제로섬 교대 최적화**: 운동 정책과 적대자가 교대로 최적화되며, 정책은 발견된 가장 강한 공격에 대응하기 위해 지속적으로 강화되어 동적 게임을 형성합니다.

### 실험 설정
- **플랫폼**: Unitree G1 휴머노이드 로봇.
- **작업**: 지각 운동(지형 통과) 및 전신 제어(궤적 추적).
- **비교**: 표준 RL 정책 및 전통적인 적대 훈련 방법과 비교.

### 주요 결과
- **지형 통과 성공률**: 적대 훈련 정책이 40% 향상.
- **궤적 추적 오차**: 32% 감소.
- **장시간 성능**: 장시간 작동 중에도 운동 및 추적 안정성을 유지하며, 성능 저하가 나타나지 않음.

### 결론
선택적 적대 공격은 학습된 견고하고 장시간 지속 가능한 휴머노이드 로봇 운동 기술을 구동하는 효과적인 방법이며, SA2RT 프레임워크는 실제 로봇에서 그 우수성을 검증했습니다.
