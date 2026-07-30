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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.08303v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇은 다양한 전신 기술을 실행하면서 장시간 안정적으로 작동할 것으로 기대됩니다. 그러나 강화 학습(RL) 기반 동작 정책은 장기 작동, 센서/액추에이터 노이즈, 실제 환경의 교란 하에서 일반적으로 안정성을 잃습니다. 본 연구에서는 동작 기술의 강건성을 향상시키기 위해 선택적 적대적 공격을 통한 강건 훈련(SA2RT)을 제안합니다. 적대자는 공격 예산 제약 하에서 가장 취약한 상태와 행동을 식별하고 드물게 교란하여, 보수적인 과적합을 유발하지 않으면서 실제 약점을 드러내도록 학습됩니다. 결과적으로 비영합, 교대 최적화는 발견된 가장 강력한 공격에 대해 지속적으로 동작 정책을 강화합니다. 우리는 Unitree G1 휴머노이드 로봇에서 인지적 보행 및 전신 제어 작업을 통해 접근법을 검증합니다. 실험 결과, 적대적 훈련을 받은 정책은 지형 이동 성공률을 40% 향상시키고, 궤적 추적 오차를 32% 감소시키며, 장기 이동성 및 추적 성능을 유지합니다. 이러한 결과는 선택적 적대적 공격이 강건하고 장기적인 휴머노이드 동작 기술을 학습하는 효과적인 동인임을 보여줍니다.

## 핵심 내용
휴머노이드 로봇은 다양한 전신 기술을 실행하면서 장시간 안정적으로 작동할 것으로 기대됩니다. 그러나 강화 학습(RL) 기반 동작 정책은 장기 작동, 센서/액추에이터 노이즈, 실제 환경의 교란 하에서 일반적으로 안정성을 잃습니다. 본 연구에서는 동작 기술의 강건성을 향상시키기 위해 선택적 적대적 공격을 통한 강건 훈련(SA2RT)을 제안합니다. 적대자는 공격 예산 제약 하에서 가장 취약한 상태와 행동을 식별하고 드물게 교란하여, 보수적인 과적합을 유발하지 않으면서 실제 약점을 드러내도록 학습됩니다. 결과적으로 비영합, 교대 최적화는 발견된 가장 강력한 공격에 대해 지속적으로 동작 정책을 강화합니다. 우리는 Unitree G1 휴머노이드 로봇에서 인지적 보행 및 전신 제어 작업을 통해 접근법을 검증합니다. 실험 결과, 적대적 훈련을 받은 정책은 지형 이동 성공률을 40% 향상시키고, 궤적 추적 오차를 32% 감소시키며, 장기 이동성 및 추적 성능을 유지합니다. 이러한 결과는 선택적 적대적 공격이 강건하고 장기적인 휴머노이드 동작 기술을 학습하는 효과적인 동인임을 보여줍니다.

## 参考
- http://arxiv.org/abs/2507.08303v3
