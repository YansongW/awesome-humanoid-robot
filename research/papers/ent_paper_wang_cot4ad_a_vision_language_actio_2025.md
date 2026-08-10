---
$id: ent_paper_wang_cot4ad_a_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving'
  zh: CoT4AD
  ko: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving'
summary:
  en: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
  zh: CoT4AD 是北京大学于 2025 年提出的一种面向自动驾驶的大规模视觉-语言-动作模型。其核心贡献在于将显式的思维链推理引入 VLA 框架，以增强数值推理与因果推理能力，并在 nuScenes 和 Bench2Drive 基准上取得了开环与闭环评估的最优性能。
  ko: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cot4ad
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22532v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (649 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.22532
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoT4AD source
  url: https://doi.org/10.48550/arXiv.2511.22532
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有视觉-语言-动作模型在端到端自动驾驶中虽具备强大推理能力，但常因数值推理能力有限及输入-输出映射过于简化，难以应对需要逐步因果推理的复杂驾驶场景。CoT4AD 通过引入显式的思维链推理来解决这一问题：训练时，模型显式建模“感知-问题-预测-动作”的推理链条，将推理空间与动作空间对齐；推理时，则执行隐式思维链推理，确保在动态环境中实现一致的数值推理与稳健决策。该方法在真实世界与模拟基准上的实验均验证了其有效性。

## 核心内容
### 方法概述
CoT4AD 是一个端到端的视觉-语言-动作模型，其核心创新在于将思维链推理显式地整合到自动驾驶决策流程中。模型输入包括视觉观测与语言指令，输出为轨迹规划结果。

### 架构设计
- **训练阶段**：模型显式建模一个四步推理链：感知（Perception）→ 问题（Question）→ 预测（Prediction）→ 动作（Action）。该设计旨在将推理空间与动作空间对齐，从而在多个驾驶任务中保持一致的推理逻辑。
- **推理阶段**：模型执行隐式思维链推理，无需显式输出中间步骤，即可在动态环境中实现稳健的数值推理与决策。

### 实验设置与结果
- **基准测试**：在真实世界数据集 nuScenes 上进行开环评估，在模拟环境 Bench2Drive 上进行闭环评估。
- **性能表现**：CoT4AD 在两项基准测试中均达到当前最优水平，具体数值在论文中详述。
- **代码开源**：代码将在论文接收后发布。

## Overview
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## 参考
- http://arxiv.org/abs/2511.22532v1

## 개요
기존의 비전-언어-행동 모델은 엔드투엔드 자율주행에서 강력한 추론 능력을 갖추고 있지만, 수치 추론 능력의 한계와 입력-출력 매핑의 과도한 단순화로 인해 단계적 인과 추론이 필요한 복잡한 주행 시나리오를 처리하는 데 어려움을 겪는 경우가 많습니다. CoT4AD는 명시적 사고 사슬 추론을 도입하여 이 문제를 해결합니다: 훈련 시 모델은 "지각-문제-예측-행동"의 추론 체인을 명시적으로 모델링하여 추론 공간과 행동 공간을 정렬하고, 추론 시에는 암시적 사고 사슬 추론을 수행하여 동적 환경에서 일관된 수치 추론과 견고한 의사 결정을 보장합니다. 이 방법은 실제 세계 및 시뮬레이션 벤치마크에서의 실험을 통해 그 효과가 검증되었습니다.

## 핵심 내용
### 방법 개요
CoT4AD는 엔드투엔드 비전-언어-행동 모델로, 핵심 혁신은 사고 사슬 추론을 자율주행 의사 결정 프로세스에 명시적으로 통합한 것입니다. 모델 입력에는 시각적 관측과 언어 명령이 포함되며, 출력은 궤적 계획 결과입니다.

### 아키텍처 설계
- **훈련 단계**: 모델은 4단계 추론 체인을 명시적으로 모델링합니다: 지각(Perception) → 문제(Question) → 예측(Prediction) → 행동(Action). 이 설계는 추론 공간과 행동 공간을 정렬하여 여러 주행 작업에서 일관된 추론 논리를 유지하는 것을 목표로 합니다.
- **추론 단계**: 모델은 암시적 사고 사슬 추론을 수행하며, 중간 단계를 명시적으로 출력하지 않고도 동적 환경에서 견고한 수치 추론과 의사 결정을 달성합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: 실제 세계 데이터셋 nuScenes에서 개루프 평가를, 시뮬레이션 환경 Bench2Drive에서 폐루프 평가를 수행했습니다.
- **성능**: CoT4AD는 두 벤치마크 모두에서 최신 최고 수준에 도달했으며, 구체적인 수치는 논문에 자세히 설명되어 있습니다.
- **코드 공개**: 코드는 논문 수락 후 공개될 예정입니다.
