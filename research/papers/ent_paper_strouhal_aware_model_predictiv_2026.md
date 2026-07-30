---
$id: ent_paper_strouhal_aware_model_predictiv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion
  zh: Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion
  ko: Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion
summary:
  en: 'arXiv:2607.03216v1 Announce Type: new Abstract: Efficient flapping propulsion hinges on operating within a narrow Strouhal
    number window, a principle nature has converged upon for maximum thrust-to-power ratio. We translate this bioinspired
    empirical rule into real-time control, demonstrating it on an autonomous underwater vehicle driven by four soft fins.
    The proposed Strouhal-aware Model Predictive Control (MPC) enhances a quasi-steady hydrodynamic model with an explicit
    penalty for Strouhal deviation, solving the resulting nonconvex problem via a two-stage sampling and gradient optimization
    that runs onboard at 25 Hz. Pool and field trials show that the controller keeps each fin within the optimal Strouhal
    corridor (0.25-0.35) while precisely tracking commanded forces. This results in a mean reduction in mechanical power of
    8.8\% to 32\% throughout the cruising range of 0.1 to 0.3 m/s. The proposed method also allows for a velocity of 0.4 m/s,
    which is unattainable for a baseline of the conventional inverse model. The results confirm that embedding first-principle
    flow physics into an MPC objective yields tangible endurance gains without sacrificing agility, offering a generic pathway
    to energy-aware locomotion in next-generation multifin robots.'
  zh: 本文提出一种斯特劳哈尔数感知模型预测控制（Strouhal-aware MPC），用于四软鳍自主水下航行器的高效扑翼推进。该方法将生物启发的斯特劳哈尔数经验规则嵌入实时控制，通过两阶段采样与梯度优化在板载运行，使各鳍保持在最优斯特劳哈尔数区间（0.25-0.35），在巡航速度0.1-0.3
    m/s范围内实现机械功率平均降低8.8%至32%，并达到传统逆模型无法实现的0.4 m/s速度。
  ko: 'arXiv:2607.03216v1 Announce Type: new Abstract: Efficient flapping propulsion hinges on operating within a narrow Strouhal
    number window, a principle nature has converged upon for maximum thrust-to-power ratio. We translate this bioinspired
    empirical rule into real-time control, demonstrating it on an autonomous underwater vehicle driven by four soft fins.
    The proposed Strouhal-aware Model Predictive Control (MPC) enhances a quasi-steady hydrodynamic model with an explicit
    penalty for Strouhal deviation, solving the resulting nonconvex problem via a two-stage sampling and gradient optimization
    that runs onboard at 25 Hz. Pool and field trials show that the controller keeps each fin within the optimal Strouhal
    corridor (0.25-0.35) while precisely tracking commanded forces. This results in a mean reduction in mechanical power of
    8.8\% to 32\% throughout the cruising range of 0.1 to 0.3 m/s. The proposed method also allows for a velocity of 0.4 m/s,
    which is unattainable for a baseline of the conventional inverse model. The results confirm that embedding first-principle
    flow physics into an MPC objective yields tangible endurance gains without sacrificing agility, offering a generic pathway
    to energy-aware locomotion in next-generation multifin robots.'
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
- strouhal_aware_model_predictiv
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03216v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion (arXiv)
  url: https://arxiv.org/abs/2607.03216
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该研究将自然界中扑翼推进效率与斯特劳哈尔数（Strouhal number）的窄窗口关联规律转化为实时控制策略。研究者提出一种斯特劳哈尔数感知模型预测控制（MPC），在准稳态水动力学模型中显式加入斯特劳哈尔数偏离惩罚项，通过两阶段采样与梯度优化求解非凸问题，以25 Hz频率在板载运行。在泳池和实地试验中，该控制器使每个软鳍保持在最优斯特劳哈尔数区间（0.25-0.35），同时精确跟踪指令力。实验结果显示，在0.1-0.3 m/s巡航范围内，机械功率平均降低8.8%至32%，并实现传统逆模型无法达到的0.4 m/s速度。结果表明，将第一性原理流动物理嵌入MPC目标函数可在不牺牲敏捷性的前提下显著提升续航能力。

## 核心内容
### 方法
- **核心原理**：基于自然界扑翼推进效率与斯特劳哈尔数（Strouhal number）的窄窗口关联规律（0.25-0.35区间内推力-功率比最优），将这一生物启发经验规则转化为实时控制约束。
- **控制架构**：提出斯特劳哈尔数感知模型预测控制（Strouhal-aware MPC），在准稳态水动力学模型基础上，显式加入斯特劳哈尔数偏离惩罚项，构建非凸优化问题。
- **求解策略**：采用两阶段采样与梯度优化方法，以25 Hz频率在板载运行，确保实时性。

### 实验设置
- **平台**：四软鳍自主水下航行器（AUV），在泳池和实地环境中进行试验。
- **对比基线**：传统逆模型控制方法。
- **性能指标**：机械功率降低率、速度范围、斯特劳哈尔数保持精度。

### 关键结果
- **斯特劳哈尔数保持**：控制器使每个鳍的斯特劳哈尔数稳定在最优区间0.25-0.35内，同时精确跟踪指令力。
- **功率降低**：在0.1-0.3 m/s巡航速度范围内，机械功率平均降低8.8%至32%。
- **速度提升**：实现0.4 m/s速度，而传统逆模型基线无法达到该速度。
- **结论**：将第一性原理流动物理嵌入MPC目标函数，可在不牺牲敏捷性的前提下显著提升续航能力，为下一代多鳍机器人的能量感知运动控制提供通用路径。

## Overview
Efficient flapping propulsion hinges on operating within a narrow Strouhal number window, a principle nature has converged upon for maximum thrust-to-power ratio. We translate this bioinspired empirical rule into real-time control, demonstrating it on an autonomous underwater vehicle driven by four soft fins. The proposed Strouhal-aware Model Predictive Control (MPC) enhances a quasi-steady hydrodynamic model with an explicit penalty for Strouhal deviation, solving the resulting nonconvex problem via a two-stage sampling and gradient optimization that runs onboard at 25 Hz. Pool and field trials show that the controller keeps each fin within the optimal Strouhal corridor (0.25-0.35) while precisely tracking commanded forces. This results in a mean reduction in mechanical power of 8.8\% to 32\% throughout the cruising range of 0.1 to 0.3 m/s. The proposed method also allows for a velocity of 0.4 m/s, which is unattainable for a baseline of the conventional inverse model. The results confirm that embedding first-principle flow physics into an MPC objective yields tangible endurance gains without sacrificing agility, offering a generic pathway to energy-aware locomotion in next-generation multifin robots.

## 개요
효율적인 날개 추진은 좁은 스트로우할 수 범위 내에서 작동하는 데 달려 있으며, 이는 최대 추력 대 출력비를 위해 자연이 수렴한 원리입니다. 우리는 이 생체 모방 경험적 규칙을 실시간 제어로 변환하여, 4개의 소프트 핀으로 구동되는 자율 수중 차량에서 이를 시연합니다. 제안된 스트로우할 인식 모델 예측 제어(MPC)는 준정상 유체역학 모델에 스트로우할 편차에 대한 명시적 패널티를 추가하고, 25Hz로 온보드에서 실행되는 2단계 샘플링 및 그래디언트 최적화를 통해 발생하는 비볼록 문제를 해결합니다. 수조 및 현장 시험에서 제어기가 각 핀을 최적 스트로우할 범위(0.25-0.35) 내로 유지하면서 명령된 힘을 정밀하게 추적함을 보여줍니다. 이는 0.1~0.3 m/s의 순항 범위에서 기계적 출력을 평균 8.8%~32% 감소시킵니다. 제안된 방법은 또한 기존 역모델 기준으로는 도달할 수 없는 0.4 m/s의 속도를 가능하게 합니다. 결과는 MPC 목적 함수에 제1원리 유체 물리학을 내장하면 민첩성을 희생하지 않고 실질적인 내구성 향상을 가져오며, 차세대 다중 핀 로봇의 에너지 인식 운동을 위한 일반적인 경로를 제공함을 확인합니다.

## 핵심 내용
효율적인 날개 추진은 좁은 스트로우할 수 범위 내에서 작동하는 데 달려 있으며, 이는 최대 추력 대 출력비를 위해 자연이 수렴한 원리입니다. 우리는 이 생체 모방 경험적 규칙을 실시간 제어로 변환하여, 4개의 소프트 핀으로 구동되는 자율 수중 차량에서 이를 시연합니다. 제안된 스트로우할 인식 모델 예측 제어(MPC)는 준정상 유체역학 모델에 스트로우할 편차에 대한 명시적 패널티를 추가하고, 25Hz로 온보드에서 실행되는 2단계 샘플링 및 그래디언트 최적화를 통해 발생하는 비볼록 문제를 해결합니다. 수조 및 현장 시험에서 제어기가 각 핀을 최적 스트로우할 범위(0.25-0.35) 내로 유지하면서 명령된 힘을 정밀하게 추적함을 보여줍니다. 이는 0.1~0.3 m/s의 순항 범위에서 기계적 출력을 평균 8.8%~32% 감소시킵니다. 제안된 방법은 또한 기존 역모델 기준으로는 도달할 수 없는 0.4 m/s의 속도를 가능하게 합니다. 결과는 MPC 목적 함수에 제1원리 유체 물리학을 내장하면 민첩성을 희생하지 않고 실질적인 내구성 향상을 가져오며, 차세대 다중 핀 로봇의 에너지 인식 운동을 위한 일반적인 경로를 제공함을 확인합니다.

## 参考
- http://arxiv.org/abs/2607.03216v1
