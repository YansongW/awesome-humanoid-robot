---
$id: ent_paper_peng_colavla_leveraging_cognitive_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving'
  zh: ColaVLA
  ko: 'ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving'
summary:
  en: 'ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving
    (ColaVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, CUHK
    MMLab, Voyager Research, Didi Chuxing.'
  zh: ColaVLA 是清华大学、CUHK MMLab、Voyager Research 和滴滴出行于 2025 年提出的统一视觉-语言-动作框架，用于自动驾驶分层并行轨迹规划。其核心贡献在于将推理从文本空间转移到统一潜在空间，并结合分层并行轨迹解码器，解决了现有
    VLM 规划器在离散推理与连续控制不匹配、高延迟及效率低下的问题。在 nuScenes 基准上，ColaVLA 在开环和闭环设置中均达到了最先进性能。
  ko: 'ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving
    (ColaVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, CUHK
    MMLab, Voyager Research, Didi Chuxing.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- colavla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22939v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (844 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving
    (arXiv)'
  url: https://arxiv.org/abs/2512.22939
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ColaVLA source
  url: https://doi.org/10.48550/arXiv.2512.22939
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ColaVLA 通过认知潜在推理器（Cognitive Latent Reasoner）将场景理解压缩为紧凑的、面向决策的元动作嵌入，仅需两次 VLM 前向传递即可完成。随后，分层并行规划器（Hierarchical Parallel Planner）在单次前向传递中生成多尺度、因果一致的轨迹。该设计保留了 VLM 的泛化能力和可解释性，同时实现了高效、准确且安全的轨迹生成。实验表明，ColaVLA 在 nuScenes 基准上取得了开环与闭环设置下的最佳结果，并展现出优异的效率和鲁棒性。

## 核心内容
### 方法概述
ColaVLA 由两个核心组件构成：
- **认知潜在推理器（Cognitive Latent Reasoner）**：通过自我自适应选择机制，将多模态场景理解压缩为紧凑的、面向决策的元动作嵌入。该过程仅需两次 VLM 前向传递，避免了传统自回归链式推理的高延迟。
- **分层并行规划器（Hierarchical Parallel Planner）**：在单次前向传递中生成多尺度、因果一致的轨迹。该规划器确保轨迹的因果一致性，支持实时部署。

### 实验设置与结果
- **基准测试**：在 nuScenes 数据集上进行评估，涵盖开环（open-loop）和闭环（closed-loop）两种设置。
- **性能表现**：ColaVLA 在两种设置下均达到最先进水平，具体指标包括轨迹精度、安全性和效率。
- **效率优势**：相比现有 VLM 规划器，ColaVLA 的推理延迟显著降低，得益于仅两次 VLM 前向传递和单次并行解码。
- **鲁棒性**：在多种复杂场景下保持稳定性能，验证了其泛化能力。

### 结论
ColaVLA 通过将推理从文本空间转移到潜在空间，并采用分层并行解码，有效解决了 VLM 规划器在自动驾驶中的关键挑战。其设计兼顾了 VLM 的语义理解优势与实时控制需求，为端到端自动驾驶轨迹规划提供了新范式。

## Overview
Autonomous driving requires generating safe and reliable trajectories from complex multimodal inputs. Traditional modular pipelines separate perception, prediction, and planning, while recent end-to-end (E2E) systems learn them jointly. Vision-language models (VLMs) further enrich this paradigm by introducing cross-modal priors and commonsense reasoning, yet current VLM-based planners face three key challenges: (i) a mismatch between discrete text reasoning and continuous control, (ii) high latency from autoregressive chain-of-thought decoding, and (iii) inefficient or non-causal planners that limit real-time deployment. We propose ColaVLA, a unified vision-language-action framework that transfers reasoning from text to a unified latent space and couples it with a hierarchical, parallel trajectory decoder. The Cognitive Latent Reasoner compresses scene understanding into compact, decision-oriented meta-action embeddings through ego-adaptive selection and only two VLM forward passes. The Hierarchical Parallel Planner then generates multi-scale, causality-consistent trajectories in a single forward pass. Together, these components preserve the generalization and interpretability of VLMs while enabling efficient, accurate and safe trajectory generation. Experiments on the nuScenes benchmark show that ColaVLA achieves state-of-the-art performance in both open-loop and closed-loop settings with favorable efficiency and robustness.

## 参考
- http://arxiv.org/abs/2512.22939v3

## 개요
ColaVLA는 인지 잠재 추론기(Cognitive Latent Reasoner)를 통해 장면 이해를 압축된 의사결정 중심의 메타 행동 임베딩으로 축소하며, 단 두 번의 VLM 순방향 전달만으로 완료합니다. 이후, 계층적 병렬 계획기(Hierarchical Parallel Planner)는 단일 순방향 전달에서 다중 스케일, 인과적으로 일관된 궤적을 생성합니다. 이 설계는 VLM의 일반화 능력과 해석 가능성을 유지하면서도 효율적이고 정확하며 안전한 궤적 생성을 실현합니다. 실험 결과, ColaVLA는 nuScenes 벤치마크에서 개루프 및 폐루프 설정 모두에서 최고 성능을 달성했으며, 뛰어난 효율성과 견고성을 입증했습니다.

## 핵심 내용
### 방법 개요
ColaVLA는 두 가지 핵심 구성 요소로 이루어져 있습니다:
- **인지 잠재 추론기(Cognitive Latent Reasoner)**: 자기 적응형 선택 메커니즘을 통해 다중 모달 장면 이해를 압축된 의사결정 중심의 메타 행동 임베딩으로 축소합니다. 이 과정은 단 두 번의 VLM 순방향 전달만 필요로 하여, 기존의 자기회귀 체인 추론의 높은 지연 시간을 피합니다.
- **계층적 병렬 계획기(Hierarchical Parallel Planner)**: 단일 순방향 전달에서 다중 스케일, 인과적으로 일관된 궤적을 생성합니다. 이 계획기는 궤적의 인과적 일관성을 보장하며 실시간 배포를 지원합니다.

### 실험 설정 및 결과
- **벤치마크 테스트**: nuScenes 데이터셋에서 평가되었으며, 개루프(open-loop) 및 폐루프(closed-loop) 두 가지 설정을 포함합니다.
- **성능**: ColaVLA는 두 설정 모두에서 최첨단 수준에 도달했으며, 구체적인 지표로는 궤적 정확도, 안전성 및 효율성이 포함됩니다.
- **효율성 이점**: 기존 VLM 계획기와 비교하여 ColaVLA의 추론 지연 시간은 단 두 번의 VLM 순방향 전달과 단일 병렬 디코딩 덕분에 크게 감소했습니다.
- **견고성**: 다양한 복잡한 시나리오에서 안정적인 성능을 유지하여 일반화 능력을 검증했습니다.

### 결론
ColaVLA는 추론을 텍스트 공간에서 잠재 공간으로 전환하고 계층적 병렬 디코딩을 채택함으로써, 자율주행에서 VLM 계획기의 핵심 과제를 효과적으로 해결합니다. 이 설계는 VLM의 의미 이해 이점과 실시간 제어 요구를 모두 고려하여, 엔드투엔드 자율주행 궤적 계획에 새로운 패러다임을 제공합니다.
