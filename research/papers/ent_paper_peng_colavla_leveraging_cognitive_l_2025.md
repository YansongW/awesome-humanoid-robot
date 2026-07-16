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
  zh: 'ColaVLA: Leveraging Cognitive Latent Reasoning for Hierarchical Parallel Trajectory Planning in Autonomous Driving
    (ColaVLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, CUHK
    MMLab, Voyager Research, Didi Chuxing.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22939v3.
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
Autonomous driving requires generating safe and reliable trajectories from complex multimodal inputs. Traditional modular pipelines separate perception, prediction, and planning, while recent end-to-end (E2E) systems learn them jointly. Vision-language models (VLMs) further enrich this paradigm by introducing cross-modal priors and commonsense reasoning, yet current VLM-based planners face three key challenges: (i) a mismatch between discrete text reasoning and continuous control, (ii) high latency from autoregressive chain-of-thought decoding, and (iii) inefficient or non-causal planners that limit real-time deployment. We propose ColaVLA, a unified vision-language-action framework that transfers reasoning from text to a unified latent space and couples it with a hierarchical, parallel trajectory decoder. The Cognitive Latent Reasoner compresses scene understanding into compact, decision-oriented meta-action embeddings through ego-adaptive selection and only two VLM forward passes. The Hierarchical Parallel Planner then generates multi-scale, causality-consistent trajectories in a single forward pass. Together, these components preserve the generalization and interpretability of VLMs while enabling efficient, accurate and safe trajectory generation. Experiments on the nuScenes benchmark show that ColaVLA achieves state-of-the-art performance in both open-loop and closed-loop settings with favorable efficiency and robustness.

## 核心内容
Autonomous driving requires generating safe and reliable trajectories from complex multimodal inputs. Traditional modular pipelines separate perception, prediction, and planning, while recent end-to-end (E2E) systems learn them jointly. Vision-language models (VLMs) further enrich this paradigm by introducing cross-modal priors and commonsense reasoning, yet current VLM-based planners face three key challenges: (i) a mismatch between discrete text reasoning and continuous control, (ii) high latency from autoregressive chain-of-thought decoding, and (iii) inefficient or non-causal planners that limit real-time deployment. We propose ColaVLA, a unified vision-language-action framework that transfers reasoning from text to a unified latent space and couples it with a hierarchical, parallel trajectory decoder. The Cognitive Latent Reasoner compresses scene understanding into compact, decision-oriented meta-action embeddings through ego-adaptive selection and only two VLM forward passes. The Hierarchical Parallel Planner then generates multi-scale, causality-consistent trajectories in a single forward pass. Together, these components preserve the generalization and interpretability of VLMs while enabling efficient, accurate and safe trajectory generation. Experiments on the nuScenes benchmark show that ColaVLA achieves state-of-the-art performance in both open-loop and closed-loop settings with favorable efficiency and robustness.

## 参考
- http://arxiv.org/abs/2512.22939v3

## Overview
Autonomous driving requires generating safe and reliable trajectories from complex multimodal inputs. Traditional modular pipelines separate perception, prediction, and planning, while recent end-to-end (E2E) systems learn them jointly. Vision-language models (VLMs) further enrich this paradigm by introducing cross-modal priors and commonsense reasoning, yet current VLM-based planners face three key challenges: (i) a mismatch between discrete text reasoning and continuous control, (ii) high latency from autoregressive chain-of-thought decoding, and (iii) inefficient or non-causal planners that limit real-time deployment. We propose ColaVLA, a unified vision-language-action framework that transfers reasoning from text to a unified latent space and couples it with a hierarchical, parallel trajectory decoder. The Cognitive Latent Reasoner compresses scene understanding into compact, decision-oriented meta-action embeddings through ego-adaptive selection and only two VLM forward passes. The Hierarchical Parallel Planner then generates multi-scale, causality-consistent trajectories in a single forward pass. Together, these components preserve the generalization and interpretability of VLMs while enabling efficient, accurate and safe trajectory generation. Experiments on the nuScenes benchmark show that ColaVLA achieves state-of-the-art performance in both open-loop and closed-loop settings with favorable efficiency and robustness.

## Content
Autonomous driving requires generating safe and reliable trajectories from complex multimodal inputs. Traditional modular pipelines separate perception, prediction, and planning, while recent end-to-end (E2E) systems learn them jointly. Vision-language models (VLMs) further enrich this paradigm by introducing cross-modal priors and commonsense reasoning, yet current VLM-based planners face three key challenges: (i) a mismatch between discrete text reasoning and continuous control, (ii) high latency from autoregressive chain-of-thought decoding, and (iii) inefficient or non-causal planners that limit real-time deployment. We propose ColaVLA, a unified vision-language-action framework that transfers reasoning from text to a unified latent space and couples it with a hierarchical, parallel trajectory decoder. The Cognitive Latent Reasoner compresses scene understanding into compact, decision-oriented meta-action embeddings through ego-adaptive selection and only two VLM forward passes. The Hierarchical Parallel Planner then generates multi-scale, causality-consistent trajectories in a single forward pass. Together, these components preserve the generalization and interpretability of VLMs while enabling efficient, accurate and safe trajectory generation. Experiments on the nuScenes benchmark show that ColaVLA achieves state-of-the-art performance in both open-loop and closed-loop settings with favorable efficiency and robustness.

## 개요
자율주행은 복잡한 다중 모달 입력으로부터 안전하고 신뢰할 수 있는 궤적을 생성해야 합니다. 기존의 모듈식 파이프라인은 인식, 예측, 계획을 분리하는 반면, 최근의 엔드투엔드(E2E) 시스템은 이를 통합적으로 학습합니다. 비전-언어 모델(VLM)은 교차 모달 사전 지식과 상식 추론을 도입하여 이 패러다임을 더욱 풍부하게 하지만, 현재 VLM 기반 계획자는 세 가지 주요 과제에 직면합니다: (i) 이산적인 텍스트 추론과 연속적인 제어 간의 불일치, (ii) 자기회귀적 사고 사슬 디코딩으로 인한 높은 지연 시간, (iii) 실시간 배치를 제한하는 비효율적이거나 인과적이지 않은 계획자. 우리는 ColaVLA를 제안합니다. 이는 통합된 비전-언어-행동 프레임워크로, 추론을 텍스트에서 통합된 잠재 공간으로 전환하고 이를 계층적 병렬 궤적 디코더와 결합합니다. 인지 잠재 추론기는 자아 적응형 선택과 단 두 번의 VLM 순방향 패스를 통해 장면 이해를 간결하고 결정 지향적인 메타-행동 임베딩으로 압축합니다. 그런 다음 계층적 병렬 계획자는 단일 순방향 패스로 다중 스케일, 인과성 일관된 궤적을 생성합니다. 이러한 구성 요소들은 VLM의 일반화와 해석 가능성을 유지하면서 효율적이고 정확하며 안전한 궤적 생성을 가능하게 합니다. nuScenes 벤치마크 실험에서 ColaVLA는 개방 루프와 폐쇄 루프 설정 모두에서 최첨단 성능을 달성하며 유리한 효율성과 강건성을 보여줍니다.

## 핵심 내용
자율주행은 복잡한 다중 모달 입력으로부터 안전하고 신뢰할 수 있는 궤적을 생성해야 합니다. 기존의 모듈식 파이프라인은 인식, 예측, 계획을 분리하는 반면, 최근의 엔드투엔드(E2E) 시스템은 이를 통합적으로 학습합니다. 비전-언어 모델(VLM)은 교차 모달 사전 지식과 상식 추론을 도입하여 이 패러다임을 더욱 풍부하게 하지만, 현재 VLM 기반 계획자는 세 가지 주요 과제에 직면합니다: (i) 이산적인 텍스트 추론과 연속적인 제어 간의 불일치, (ii) 자기회귀적 사고 사슬 디코딩으로 인한 높은 지연 시간, (iii) 실시간 배치를 제한하는 비효율적이거나 인과적이지 않은 계획자. 우리는 ColaVLA를 제안합니다. 이는 통합된 비전-언어-행동 프레임워크로, 추론을 텍스트에서 통합된 잠재 공간으로 전환하고 이를 계층적 병렬 궤적 디코더와 결합합니다. 인지 잠재 추론기는 자아 적응형 선택과 단 두 번의 VLM 순방향 패스를 통해 장면 이해를 간결하고 결정 지향적인 메타-행동 임베딩으로 압축합니다. 그런 다음 계층적 병렬 계획자는 단일 순방향 패스로 다중 스케일, 인과성 일관된 궤적을 생성합니다. 이러한 구성 요소들은 VLM의 일반화와 해석 가능성을 유지하면서 효율적이고 정확하며 안전한 궤적 생성을 가능하게 합니다. nuScenes 벤치마크 실험에서 ColaVLA는 개방 루프와 폐쇄 루프 설정 모두에서 최첨단 성능을 달성하며 유리한 효율성과 강건성을 보여줍니다.
