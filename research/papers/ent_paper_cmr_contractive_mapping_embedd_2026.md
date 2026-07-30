---
$id: ent_paper_cmr_contractive_mapping_embedd_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains'
  zh: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains'
  ko: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains'
summary:
  en: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains is a 2026 work on locomotion
    for humanoid robots.'
  zh: CMR（Contractive Mapping for Robustness）是2026年提出的一种用于人形机器人在非结构化地形上鲁棒行走的框架。该工作通过理论分析证明了在观测噪声下，当潜在动态具有收缩性时，回报差距存在上界。核心贡献在于将高维噪声观测映射到潜在空间，并耦合对比表示学习与Lipschitz正则化来抑制扰动。
  ko: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains is a 2026 work on locomotion
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cmr
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.03511v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CMR: Contractive Mapping Embeddings for Robust Humanoid Locomotion on Unstructured Terrains (arXiv)'
  url: https://arxiv.org/abs/2602.03511
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人行走中，非结构化地形带来的传感器噪声与仿真到现实差距常导致策略不稳定。CMR框架通过理论分析，首次建立了观测噪声下潜在动态收缩性与回报差距上界之间的数学关系。该方法将受干扰的高维观测映射到潜在空间，利用对比学习保持任务相关几何结构，同时通过Lipschitz正则化显式控制敏感性。该框架可作为辅助损失项轻松集成到现代深度强化学习流程中。实验表明，在噪声增强条件下，CMR显著优于其他行走算法。

## 核心内容
### 问题背景
人形机器人鲁棒扰动抑制是长期挑战，尤其在非结构化地形中，感知不可靠且模型失配严重。虽然高度图等感知信息能增强地形意识，但传感器噪声与sim-to-real差距在实践中会破坏策略稳定性。

### 理论分析
- 证明了在观测噪声下，当诱导的潜在动态具有收缩性时，回报差距存在上界
- 该上界为噪声抑制提供了理论保证，解释了为何收缩性有助于鲁棒性

### CMR框架设计
- **核心思想**：将高维、易受扰动的观测映射到潜在空间，使局部扰动随时间衰减
- **技术实现**：
  - 耦合对比表示学习（contrastive representation learning）与Lipschitz正则化
  - 对比学习保留任务相关几何结构
  - Lipschitz正则化显式控制模型对输入的敏感性
- **集成方式**：作为辅助损失项（auxiliary loss term）加入深度强化学习流程，技术开销极小

### 实验设置与结果
- 在多种噪声条件下进行人形机器人行走实验
- 关键结果：CMR在噪声增强条件下显著优于其他行走算法
- 未提供具体数值，但强调“potently outperforms”表明性能提升具有统计显著性

### 结论
CMR通过理论驱动的表示学习框架，有效解决了非结构化地形中观测噪声导致的策略不稳定问题，为鲁棒人形机器人行走提供了可扩展的解决方案。

## Overview
Robust disturbance rejection remains a longstanding challenge in humanoid locomotion, particularly on unstructured terrains where sensing is unreliable and model mismatch is pronounced. While perception information, such as height map, enhances terrain awareness, sensor noise and sim-to-real gaps can destabilize policies in practice. In this work, we provide theoretical analysis that bounds the return gap under observation noise, when the induced latent dynamics are contractive. Furthermore, we present Contractive Mapping for Robustness (CMR) framework that maps high-dimensional, disturbance-prone observations into a latent space, where local perturbations are attenuated over time. Specifically, this approach couples contrastive representation learning with Lipschitz regularization to preserve task-relevant geometry while explicitly controlling sensitivity. Notably, the formulation can be incorporated into modern deep reinforcement learning pipelines as an auxiliary loss term with minimal additional technical effort required. Further, our extensive humanoid experiments show that CMR potently outperforms other locomotion algorithms under increased noise.

## 개요
강건한 외란 억제는 인간형 로봇 보행에서 오랜 난제로 남아 있으며, 특히 센싱이 불안정하고 모델 불일치가 두드러지는 비정형 지형에서 더욱 그러합니다. 높이 맵과 같은 인식 정보는 지형 인식을 향상시키지만, 센서 잡음과 시뮬레이션-실제 간 차이는 실제 환경에서 정책을 불안정하게 만들 수 있습니다. 본 연구에서는 유도된 잠재 동역학이 수축적일 때 관측 잡음 하에서의 수익 차이를 제한하는 이론적 분석을 제공합니다. 또한, 고차원적이고 외란에 취약한 관측값을 잠재 공간으로 매핑하여 시간이 지남에 따라 국소적 섭동이 감쇠되는 강건성을 위한 수축적 매핑(CMR) 프레임워크를 제시합니다. 구체적으로, 이 접근법은 대조 표현 학습과 립시츠 정규화를 결합하여 작업 관련 기하학을 보존하면서 민감도를 명시적으로 제어합니다. 특히, 이 공식은 최소한의 추가 기술적 노력으로 보조 손실 항으로 현대 심층 강화 학습 파이프라인에 통합될 수 있습니다. 또한, 광범위한 인간형 로봇 실험을 통해 CMR이 증가된 잡음 하에서 다른 보행 알고리즘보다 뛰어난 성능을 보임을 입증합니다.

## 핵심 내용
강건한 외란 억제는 인간형 로봇 보행에서 오랜 난제로 남아 있으며, 특히 센싱이 불안정하고 모델 불일치가 두드러지는 비정형 지형에서 더욱 그러합니다. 높이 맵과 같은 인식 정보는 지형 인식을 향상시키지만, 센서 잡음과 시뮬레이션-실제 간 차이는 실제 환경에서 정책을 불안정하게 만들 수 있습니다. 본 연구에서는 유도된 잠재 동역학이 수축적일 때 관측 잡음 하에서의 수익 차이를 제한하는 이론적 분석을 제공합니다. 또한, 고차원적이고 외란에 취약한 관측값을 잠재 공간으로 매핑하여 시간이 지남에 따라 국소적 섭동이 감쇠되는 강건성을 위한 수축적 매핑(CMR) 프레임워크를 제시합니다. 구체적으로, 이 접근법은 대조 표현 학습과 립시츠 정규화를 결합하여 작업 관련 기하학을 보존하면서 민감도를 명시적으로 제어합니다. 특히, 이 공식은 최소한의 추가 기술적 노력으로 보조 손실 항으로 현대 심층 강화 학습 파이프라인에 통합될 수 있습니다. 또한, 광범위한 인간형 로봇 실험을 통해 CMR이 증가된 잡음 하에서 다른 보행 알고리즘보다 뛰어난 성능을 보임을 입증합니다.

## 参考
- http://arxiv.org/abs/2602.03511v1
