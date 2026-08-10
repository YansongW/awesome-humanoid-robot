---
$id: ent_paper_feeling_the_unexpected_restacv_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation'
  zh: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation'
  ko: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation'
summary:
  en: 'arXiv:2607.03387v1 Announce Type: new Abstract: Tactile perception is indispensable for contact-rich manipulation,
    yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual
    features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates
    predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input,
    we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations.
    By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value
    information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector
    Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the
    neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing
    residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results
    show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while
    remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA-Website/'
  zh: ResTacVLA 是一种受预测编码启发的新型触觉-视觉-语言动作模型，由研究团队提出。其核心创新在于将触觉数据重构为残差触觉表示，通过向量量化瓶颈提取潜在接触基元，并利用视觉先验的不确定性自适应门控触觉融合，从而解决视觉模态主导问题。实验表明，该模型在多种接触密集操作任务中持续优于所有基线方法，并对意外动态扰动保持鲁棒性。
  ko: 'arXiv:2607.03387v1 Announce Type: new Abstract: Tactile perception is indispensable for contact-rich manipulation,
    yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual
    features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates
    predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input,
    we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations.
    By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value
    information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector
    Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the
    neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing
    residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results
    show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while
    remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA-Website/'
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
- feeling_the_unexpected
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03387v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (766 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Feeling the Unexpected: ResTacVLA for Contact-Rich Manipulation via Residual Tactile Representation (arXiv)'
  url: https://arxiv.org/abs/2607.03387
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
触觉感知对接触密集操作至关重要，但将其集成到VLA模型中常导致模态坍塌，即高带宽视觉特征压制稀疏触觉线索。受预测编码启发，ResTacVLA将触觉数据重新定义为残差触觉表示，捕捉视觉先验与物理感觉之间的差异。通过滤除视觉可预测的动态，该表示将稀疏触觉信号转化为密集的高价值信息增益，从根本上解决带宽不匹配问题。这些残差通过向量量化瓶颈离散化为潜在接触基元，捕获视觉遗漏的关键事件。模型利用视觉先验的不确定性自适应门控触觉集成，在视觉不可靠阶段优先处理残差，明确防止视觉主导。

## 核心内容
### 方法架构
- **残差触觉表示**：基于预测编码原理，将触觉数据重构为视觉先验与物理感觉之间的差异信号，滤除视觉可预测的动态成分，使稀疏触觉信号转化为密集信息增益。
- **向量量化瓶颈**：通过VQ瓶颈将残差离散化为潜在接触基元，这些基元专门捕获视觉遗漏的关键接触事件。
- **自适应门控机制**：利用视觉先验的不确定性作为神经惊喜信号，在视觉不可靠阶段自适应地增强触觉集成权重，明确抑制视觉主导。

### 实验设置
- **任务范围**：涵盖多种接触密集操作任务，包括动态扰动场景。
- **基线对比**：与标准VLA模型及触觉融合基线进行系统比较。
- **评估指标**：任务成功率、对意外动态扰动的鲁棒性。

### 关键结果
- ResTacVLA在所有接触密集操作任务中持续优于所有基线方法。
- 对意外动态扰动表现出显著鲁棒性，验证了自适应门控机制的有效性。
- 残差触觉表示成功解决了模态坍塌问题，使触觉信息在视觉主导场景中仍能发挥关键作用。

### 结论
ResTacVLA通过预测编码启发的残差表示和自适应门控机制，为触觉-视觉融合提供了新范式，在接触密集操作中实现了性能与鲁棒性的双重提升。

## Overview
Tactile perception is indispensable for contact-rich manipulation, yet integrating it into Vision-Language-Action (VLA) models often induces modality collapse, where high-bandwidth visual features overshadow sparse tactile cues. Inspired by Predictive Coding, a neural mechanism where the brain attenuates predictable inputs to prioritize surprising stimuli, we propose ResTacVLA. Rather than treating tactile data as raw input, we reformulate it as a Residual Tactile Representation capturing the discrepancy between visual priors and physical sensations. By filtering out visually predictable dynamics, this formulation transforms sparse tactile signals into dense, high-value information gain, thereby inherently resolving the bandwidth mismatch. These residuals are discretized through a Vector Quantized (VQ) bottleneck into Latent Contact Primitives that capture critical events missed by vision. Analogous to the neural surprise signal, we leverage the uncertainty of the visual prior to adaptively gate tactile integration, prioritizing residuals specifically during visually unreliable phases to explicitly prevent visual dominance. Experimental results show that ResTacVLA consistently outperforms all baselines on a diverse set of contact-rich manipulation tasks, while remaining robust to unexpected dynamic disturbances. Project page: https://awilekong.github.io/ResTacVLA/

## 参考
- http://arxiv.org/abs/2607.03387v2

## 개요
촉각 인식은 접촉이 빈번한 조작 작업에 필수적이지만, 이를 VLA 모델에 통합하면 고대역폭 시각 특징이 희소한 촉각 신호를 압도하는 모달리티 붕괴가 자주 발생합니다. 예측 코딩에서 영감을 얻은 ResTacVLA는 촉각 데이터를 잔차 촉각 표현으로 재정의하여 시각적 사전 지식과 물리적 감각 간의 차이를 포착합니다. 시각적으로 예측 가능한 동역학을 걸러냄으로써, 이 표현은 희소한 촉각 신호를 밀집된 고가치 정보 이득으로 변환하여 대역폭 불일치 문제를 근본적으로 해결합니다. 이러한 잔차는 벡터 양자화 병목을 통해 이산적인 잠재 접촉 원시 요소로 이산화되어, 시각이 놓치는 핵심 이벤트를 포착합니다. 모델은 시각적 사전 지식의 불확실성을 활용하여 촉각 통합을 적응적으로 게이팅하며, 시각이 불확실한 단계에서 잔차를 우선 처리하여 시각적 지배를 명시적으로 방지합니다.

## 핵심 내용
### 방법 아키텍처
- **잔차 촉각 표현**: 예측 코딩 원리에 기반하여 촉각 데이터를 시각적 사전 지식과 물리적 감각 간의 차이 신호로 재구성하고, 시각적으로 예측 가능한 동역학 성분을 걸러내어 희소한 촉각 신호를 밀집된 정보 이득으로 변환합니다.
- **벡터 양자화 병목**: VQ 병목을 통해 잔차를 이산적인 잠재 접촉 원시 요소로 이산화하며, 이러한 원시 요소는 시각이 놓치는 핵심 접촉 이벤트를 특별히 포착합니다.
- **적응형 게이팅 메커니즘**: 시각적 사전 지식의 불확실성을 신경 놀람 신호로 활용하여, 시각이 불확실한 단계에서 촉각 통합 가중치를 적응적으로 강화하고 시각적 지배를 명시적으로 억제합니다.

### 실험 설정
- **작업 범위**: 동적 교란 시나리오를 포함한 다양한 접촉이 빈번한 조작 작업을 포괄합니다.
- **기준선 비교**: 표준 VLA 모델 및 촉각 융합 기준선과 체계적으로 비교합니다.
- **평가 지표**: 작업 성공률, 예기치 않은 동적 교란에 대한 강건성.

### 주요 결과
- ResTacVLA는 모든 접촉이 빈번한 조작 작업에서 모든 기준선 방법을 지속적으로 능가합니다.
- 예기치 않은 동적 교란에 대해 현저한 강건성을 보여주며, 적응형 게이팅 메커니즘의 효과를 검증합니다.
- 잔차 촉각 표현은 모달리티 붕괴 문제를 성공적으로 해결하여, 시각이 지배적인 시나리오에서도 촉각 정보가 핵심 역할을 수행할 수 있게 합니다.

### 결론
ResTacVLA는 예측 코딩에서 영감을 얻은 잔차 표현과 적응형 게이팅 메커니즘을 통해 촉각-시각 융합의 새로운 패러다임을 제시하며, 접촉이 빈번한 조작에서 성능과 강건성의 이중 향상을 달성합니다.
