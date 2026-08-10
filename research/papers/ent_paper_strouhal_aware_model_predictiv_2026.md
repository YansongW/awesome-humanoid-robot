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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03216v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (904 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03216v1

## 개요
이 연구는 자연계에서 날갯짓 추진 효율과 스트로할 수(Strouhal number)의 좁은 창 연관성을 실시간 제어 전략으로 전환한다. 연구진은 스트로할 수 인식 모델 예측 제어(MPC)를 제안하며, 준정상 유체역학 모델에 스트로할 수 이탈 패널티 항을 명시적으로 추가하고, 2단계 샘플링과 경사 최적화를 통해 비볼록 문제를 풀어 25 Hz 주파수로 온보드에서 실행한다. 수영장 및 현장 실험에서 이 제어기는 각 소프트 핀을 최적 스트로할 수 구간(0.25-0.35)에 유지하면서 지령 힘을 정밀 추적한다. 실험 결과, 0.1-0.3 m/s 순항 범위에서 기계적 동력이 평균 8.8%에서 32%까지 감소했으며, 기존 역모델로는 도달할 수 없었던 0.4 m/s 속도를 달성했다. 결과는 제1원리 유동 물리학을 MPC 목적 함수에 내장함으로써 민첩성을 희생하지 않고 항속 능력을 크게 향상시킬 수 있음을 보여준다.

## 핵심 내용
### 방법
- **핵심 원리**: 자연계에서 날갯짓 추진 효율과 스트로할 수(Strouhal number)의 좁은 창 연관성(0.25-0.35 구간에서 추력-동력 비율 최적)을 기반으로, 이 생물학적 영감 경험 규칙을 실시간 제어 제약으로 변환한다.
- **제어 아키텍처**: 스트로할 수 인식 모델 예측 제어(Strouhal-aware MPC)를 제안하며, 준정상 유체역학 모델 위에 스트로할 수 이탈 패널티 항을 명시적으로 추가하여 비볼록 최적화 문제를 구성한다.
- **해법 전략**: 2단계 샘플링과 경사 최적화 방법을 사용하여 25 Hz 주파수로 온보드에서 실행하며 실시간성을 보장한다.

### 실험 설정
- **플랫폼**: 4-소프트 핀 자율 수중 항해기(AUV)로, 수영장 및 현장 환경에서 실험을 수행한다.
- **비교 기준선**: 기존 역모델 제어 방법.
- **성능 지표**: 기계적 동력 감소율, 속도 범위, 스트로할 수 유지 정밀도.

### 주요 결과
- **스트로할 수 유지**: 제어기는 각 핀의 스트로할 수를 최적 구간 0.25-0.35 내로 안정화하면서 지령 힘을 정밀 추적한다.
- **동력 감소**: 0.1-0.3 m/s 순항 속도 범위에서 기계적 동력이 평균 8.8%에서 32%까지 감소한다.
- **속도 향상**: 0.4 m/s 속도를 달성하며, 기존 역모델 기준선은 이 속도에 도달할 수 없다.
- **결론**: 제1원리 유동 물리학을 MPC 목적 함수에 내장함으로써 민첩성을 희생하지 않고 항속 능력을 크게 향상시킬 수 있으며, 차세대 다중 핀 로봇의 에너지 인식 운동 제어를 위한 일반적인 경로를 제공한다.
