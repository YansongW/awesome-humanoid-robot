---
$id: ent_paper_liu_trivla_a_triple_system_based_u_0
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control'
  zh: TriVLA
  ko: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control'
summary:
  en: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
  zh: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
  ko: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (TriVLA), is a 0 large
    vision-language-action model for robotic manipulation, introduced by Fudan University, Shanghai Innovation Institute.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- trivla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.01424v3.
sources:
- id: src_001
  type: paper
  title: 'TriVLA: A Triple-System-Based Unified Vision-Language-Action Model for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2507.01424
  date: '0'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TriVLA source
  url: https://doi.org/10.48550/arXiv.2507.01424
  date: '0'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## 核心内容
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## 参考
- http://arxiv.org/abs/2507.01424v3

## Overview
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## Content
Recent advances in vision-language models (VLMs) have enabled robots to follow open-ended instructions and demonstrate impressive commonsense reasoning. However, current vision-language-action (VLA) frameworks primarily rely on static representations and limited temporal context, restricting agents to short-horizon, reactive behaviors and hindering robust generalization in dynamic embodied environments. Inspired by cognitive neuroscience theories of episodic memory, we propose, to our knowledge, one of the first formalized episodic world models in VLA, enabling embodied robots to accumulate, recall, and predict sequential experiences. As an instantiation of this concept, our unified TriVLA realizes the episodic world model through a triple-system architecture: integrating multimodal grounding from a pretrained VLM (System 2) and temporally rich dynamics perception from a video diffusion model (System 3). This enables the agent to accumulate and recall sequential experiences, interpret current contexts, and predict future environmental evolution. Guided by episodic representations that span both the past and anticipated future, the downstream policy (System 1) generates coherent, context-aware action sequences through flow-matching and cross-modal attention mechanisms. Experimental results show that TriVLA operates efficiently at approximately 36 Hz and consistently outperforms baseline models on standard benchmarks and challenging real-world manipulation tasks. It demonstrates strong long-horizon planning and open-ended intent understanding, showcasing the advantages of episodic world model-inspired reasoning for robust, generalizable robot intelligence. Project Page: https://zhenyangliu.github.io/TriVLA/.

## 개요
최근 비전-언어 모델(VLM)의 발전으로 로봇이 개방형 명령을 따르고 인상적인 상식 추론 능력을 보여줄 수 있게 되었습니다. 그러나 현재의 비전-언어-행동(VLA) 프레임워크는 주로 정적 표현과 제한된 시간적 맥락에 의존하여, 에이전트를 단기적이고 반응적인 행동에 국한시키고 동적 환경에서의 강건한 일반화를 저해합니다. 인지 신경과학의 일화 기억 이론에서 영감을 받아, 우리는 VLA에서 최초로 공식화된 일화적 세계 모델 중 하나를 제안하여, 내장형 로봇이 순차적 경험을 축적, 회상 및 예측할 수 있도록 합니다. 이 개념의 구체화로서, 우리의 통합된 TriVLA는 삼중 시스템 아키텍처를 통해 일화적 세계 모델을 구현합니다: 사전 훈련된 VLM(시스템 2)의 다중 모달 접지와 비디오 확산 모델(시스템 3)의 시간적으로 풍부한 역학 인식을 통합합니다. 이를 통해 에이전트는 순차적 경험을 축적하고 회상하며, 현재 맥락을 해석하고, 미래 환경 변화를 예측할 수 있습니다. 과거와 예상되는 미래를 아우르는 일화적 표현에 의해 안내되어, 하위 정책(시스템 1)은 흐름 매칭 및 교차 모달 주의 메커니즘을 통해 일관되고 맥락을 인식하는 행동 시퀀스를 생성합니다. 실험 결과는 TriVLA가 약 36Hz로 효율적으로 작동하며, 표준 벤치마크와 도전적인 실제 세계 조작 작업에서 기준 모델을 일관되게 능가함을 보여줍니다. 이는 강력한 장기 계획 및 개방형 의도 이해를 입증하며, 강건하고 일반화 가능한 로봇 지능을 위한 일화적 세계 모델 기반 추론의 장점을 보여줍니다. 프로젝트 페이지: https://zhenyangliu.github.io/TriVLA/.

## 핵심 내용
최근 비전-언어 모델(VLM)의 발전으로 로봇이 개방형 명령을 따르고 인상적인 상식 추론 능력을 보여줄 수 있게 되었습니다. 그러나 현재의 비전-언어-행동(VLA) 프레임워크는 주로 정적 표현과 제한된 시간적 맥락에 의존하여, 에이전트를 단기적이고 반응적인 행동에 국한시키고 동적 환경에서의 강건한 일반화를 저해합니다. 인지 신경과학의 일화 기억 이론에서 영감을 받아, 우리는 VLA에서 최초로 공식화된 일화적 세계 모델 중 하나를 제안하여, 내장형 로봇이 순차적 경험을 축적, 회상 및 예측할 수 있도록 합니다. 이 개념의 구체화로서, 우리의 통합된 TriVLA는 삼중 시스템 아키텍처를 통해 일화적 세계 모델을 구현합니다: 사전 훈련된 VLM(시스템 2)의 다중 모달 접지와 비디오 확산 모델(시스템 3)의 시간적으로 풍부한 역학 인식을 통합합니다. 이를 통해 에이전트는 순차적 경험을 축적하고 회상하며, 현재 맥락을 해석하고, 미래 환경 변화를 예측할 수 있습니다. 과거와 예상되는 미래를 아우르는 일화적 표현에 의해 안내되어, 하위 정책(시스템 1)은 흐름 매칭 및 교차 모달 주의 메커니즘을 통해 일관되고 맥락을 인식하는 행동 시퀀스를 생성합니다. 실험 결과는 TriVLA가 약 36Hz로 효율적으로 작동하며, 표준 벤치마크와 도전적인 실제 세계 조작 작업에서 기준 모델을 일관되게 능가함을 보여줍니다. 이는 강력한 장기 계획 및 개방형 의도 이해를 입증하며, 강건하고 일반화 가능한 로봇 지능을 위한 일화적 세계 모델 기반 추론의 장점을 보여줍니다. 프로젝트 페이지: https://zhenyangliu.github.io/TriVLA/.
