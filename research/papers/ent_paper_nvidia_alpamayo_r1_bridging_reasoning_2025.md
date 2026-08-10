---
$id: ent_paper_nvidia_alpamayo_r1_bridging_reasoning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail'
  zh: Alpamayo-R1
  ko: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail'
summary:
  en: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (Alpamayo-R1),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore.'
  zh: Alpamayo-R1 是新加坡国立大学于2025年提出的大型视觉-语言-动作模型，专为自动驾驶中的长尾场景设计。其核心贡献在于将因果推理链与轨迹规划相结合，通过混合自动标注与人工参与的流程构建了因果推理数据集，并采用模块化架构与多阶段训练策略，显著提升了复杂场景下的规划准确性与安全性。
  ko: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (Alpamayo-R1),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by National University of Singapore.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- alpamayo_r1
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00088v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1018 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail (arXiv)'
  url: https://arxiv.org/abs/2511.00088
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Alpamayo-R1 source
  url: https://doi.org/10.48550/arXiv.2511.00088
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Alpamayo-R1 针对端到端模仿学习在安全关键的长尾场景中表现脆弱的问题，提出了一种融合因果推理与轨迹规划的视觉-语言-动作模型。该模型包含三大创新：通过混合自动标注与人工参与流程构建的因果推理数据集，结合预训练视觉语言模型与扩散轨迹解码器的模块化架构，以及采用监督微调与强化学习相结合的多阶段训练策略。实验表明，该模型在挑战性场景中规划准确率提升12%，闭环仿真中近距离接触率降低35%，强化学习后推理质量提升45%，推理-动作一致性提升37%，并在实车测试中实现99毫秒延迟的实时性能。

## 核心内容
### 方法概述
Alpamayo-R1 采用模块化视觉-语言-动作架构，将因果推理与轨迹规划解耦为两个协同模块：
- **Cosmos-Reason 视觉语言模型**：基于为 Physical AI 预训练的模型，负责从多视角图像输入中生成因果推理链，解释驾驶决策的因果逻辑。
- **扩散轨迹解码器**：基于扩散模型，将推理结果转化为动态可行的轨迹，支持实时生成。

### 数据集构建
- **Chain of Causation 数据集**：通过混合自动标注与人工参与的流程生成，包含决策驱动的因果推理轨迹，与驾驶行为对齐。该流程确保推理链的因果一致性，覆盖长尾场景中的稀疏监督问题。

### 训练策略
采用多阶段训练：
1. **监督微调**：在 CoC 数据集上微调，使模型学会生成因果推理链。
2. **强化学习**：通过奖励函数优化推理质量与推理-动作一致性，奖励设计同时考虑推理逻辑的合理性（如因果链的完整性）与轨迹执行的安全性（如碰撞避免）。

### 实验设置与关键结果
- **基准对比**：在挑战性长尾场景中，AR1 相比纯轨迹基线（trajectory-only baseline）规划准确率提升12%。
- **闭环仿真**：近距离接触率降低35%，表明安全性显著提升。
- **推理质量**：RL 后训练使推理质量提升45%，推理-动作一致性提升37%。
- **模型缩放**：从0.5B到7B参数规模，性能持续提升，验证了架构的可扩展性。
- **实车测试**：在城区道路部署中实现99毫秒延迟，满足实时性要求。

### 结论
Alpamayo-R1 通过将可解释的因果推理与精确轨迹控制相结合，为 Level 4 自动驾驶提供了一条实用路径。模型权重与推理代码已开源。

## Overview
End-to-end architectures trained via imitation learning have advanced autonomous driving by scaling model size and data, yet performance remains brittle in safety-critical long-tail scenarios where supervision is sparse and causal understanding is limited. We introduce Alpamayo-R1 (AR1), a vision-language-action model (VLA) that integrates Chain of Causation reasoning with trajectory planning for complex driving scenarios. Our approach features three key innovations: (1) the Chain of Causation (CoC) dataset, built through a hybrid auto-labeling and human-in-the-loop pipeline producing decision-grounded, causally linked reasoning traces aligned with driving behaviors; (2) a modular VLA architecture combining Cosmos-Reason, a vision-language model pre-trained for Physical AI, with a diffusion-based trajectory decoder that generates dynamically feasible trajectories in real time; (3) a multi-stage training strategy using supervised fine-tuning to elicit reasoning and reinforcement learning (RL) to enforce reasoning-action consistency and optimize reasoning quality. AR1 achieves up to a 12% improvement in planning accuracy on challenging cases compared to a trajectory-only baseline, with a 35% reduction in close encounter rate in closed-loop simulation. RL post-training improves reasoning quality by 45% and reasoning-action consistency by 37%. Model scaling from 0.5B to 7B parameters shows consistent improvements. On-vehicle road tests confirm real-time performance (99 ms latency) and successful urban deployment. By bridging interpretable reasoning with precise control, AR1 demonstrates a practical path towards Level 4 autonomous driving. Model weights are available at https://huggingface.co/nvidia/Alpamayo-R1-10B with inference code at https://github.com/NVlabs/alpamayo.

## 参考
- http://arxiv.org/abs/2511.00088v2

## 개요
Alpamayo-R1은 안전이 중요한 장기(long-tail) 시나리오에서 엔드투엔드 모방 학습의 취약성 문제를 해결하기 위해, 인과 추론과 궤적 계획을 융합한 비전-언어-행동 모델을 제안합니다. 이 모델은 세 가지 주요 혁신을 포함합니다: 혼합 자동 주석 및 수동 참여 프로세스로 구축된 인과 추론 데이터셋, 사전 훈련된 비전-언어 모델과 확산 궤적 디코더를 결합한 모듈형 아키텍처, 그리고 지도 미세 조정과 강화 학습을 결합한 다단계 훈련 전략입니다. 실험 결과, 이 모델은 도전적인 시나리오에서 계획 정확도를 12% 향상시키고, 폐루프 시뮬레이션에서 근접 접촉률을 35% 감소시켰으며, 강화 학습 후 추론 품질을 45% 향상시키고 추론-행동 일관성을 37% 개선했으며, 실차 테스트에서 99밀리초 지연 시간의 실시간 성능을 달성했습니다.

## 핵심 내용
### 방법 개요
Alpamayo-R1은 모듈형 비전-언어-행동 아키텍처를 채택하여 인과 추론과 궤적 계획을 두 개의 협력 모듈로 분리합니다:
- **Cosmos-Reason 비전-언어 모델**: Physical AI용으로 사전 훈련된 모델을 기반으로, 다중 시점 이미지 입력에서 인과 추론 체인을 생성하여 운전 결정의 인과 논리를 설명합니다.
- **확산 궤적 디코더**: 확산 모델을 기반으로 추론 결과를 동적으로 실행 가능한 궤적으로 변환하며, 실시간 생성을 지원합니다.

### 데이터셋 구축
- **Chain of Causation 데이터셋**: 혼합 자동 주석 및 수동 참여 프로세스를 통해 생성되며, 운전 행동과 정렬된 결정 중심의 인과 추론 궤적을 포함합니다. 이 프로세스는 추론 체인의 인과 일관성을 보장하고, 장기 시나리오에서의 희소 감독 문제를 다룹니다.

### 훈련 전략
다단계 훈련을 채택합니다:
1. **지도 미적분**: CoC 데이터셋에서 미세 조정하여 모델이 인과 추론 체인을 생성하도록 학습시킵니다.
2. **강화 학습**: 보상 함수를 통해 추론 품질과 추론-행동 일관성을 최적화하며, 보상 설계는 추론 논리의 합리성(예: 인과 체인의 완전성)과 궤적 실행의 안전성(예: 충돌 회피)을 동시에 고려합니다.

### 실험 설정 및 주요 결과
- **기준 비교**: 도전적인 장기 시나리오에서 AR1은 순수 궤적 기준선(trajectory-only baseline) 대비 계획 정확도를 12% 향상시킵니다.
- **폐루프 시뮬레이션**: 근접 접촉률이 35% 감소하여 안전성이 크게 향상되었음을 나타냅니다.
- **추론 품질**: RL 후 훈련으로 추론 품질이 45% 향상되고, 추론-행동 일관성이 37% 개선됩니다.
- **모델 확장**: 0.5B에서 7B 파라미터 규모까지 성능이 지속적으로 향상되어 아키텍처의 확장성을 검증합니다.
- **실차 테스트**: 도시 도로 배치에서 99밀리초 지연 시간을 달성하여 실시간 요구 사항을 충족합니다.

### 결론
Alpamayo-R1은 해석 가능한 인과 추론과 정밀한 궤적 제어를 결합하여 Level 4 자율 주행을 위한 실용적인 경로를 제공합니다. 모델 가중치와 추론 코드는 오픈소스로 공개되었습니다.
