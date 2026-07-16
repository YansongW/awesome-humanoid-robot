---
$id: ent_paper_yu_forcevla_enhancing_vla_models_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation'
  zh: ForceVLA
  ko: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation'
summary:
  en: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
  zh: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
  ko: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (ForceVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Lab, National University of Singapore, Shanghai University,
    Xi’an Jiaotong University, Noematrix Intelligence, Fudan University, Shanghai Jiao Tong University, Shanghai Innovation
    Institute, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- forcevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.22159v3.
sources:
- id: src_001
  type: paper
  title: 'ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation (arXiv)'
  url: https://arxiv.org/abs/2505.22159
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ForceVLA source
  url: https://doi.org/10.48550/arXiv.2505.22159
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 核心内容
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 参考
- http://arxiv.org/abs/2505.22159v3

## Overview
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## Content
Vision-Language-Action (VLA) models have advanced general-purpose robotic manipulation by leveraging pretrained visual and linguistic representations. However, they struggle with contact-rich tasks that require fine-grained control involving force, especially under visual occlusion or dynamic uncertainty. To address these limitations, we propose ForceVLA, a novel end-to-end manipulation framework that treats external force sensing as a first-class modality within VLA systems. ForceVLA introduces FVLMoE, a force-aware Mixture-of-Experts fusion module that dynamically integrates pretrained visual-language embeddings with real-time 6-axis force feedback during action decoding. This enables context-aware routing across modality-specific experts, enhancing the robot's ability to adapt to subtle contact dynamics. We also introduce \textbf{ForceVLA-Data}, a new dataset comprising synchronized vision, proprioception, and force-torque signals across five contact-rich manipulation tasks. ForceVLA improves average task success by 23.2% over strong pi_0-based baselines, achieving up to 80% success in tasks such as plug insertion. Our approach highlights the importance of multimodal integration for dexterous manipulation and sets a new benchmark for physically intelligent robotic control. Code and data will be released at https://sites.google.com/view/forcevla2025.

## 개요
Vision-Language-Action (VLA) 모델은 사전 학습된 시각 및 언어 표현을 활용하여 범용 로봇 조작을 발전시켰습니다. 그러나 시각적 폐색이나 동적 불확실성 하에서 힘과 관련된 세밀한 제어가 필요한 접촉이 많은 작업에서는 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 외부 힘 감지를 VLA 시스템 내에서 일급 모달리티로 취급하는 새로운 엔드투엔드 조작 프레임워크인 ForceVLA를 제안합니다. ForceVLA는 FVLMoE를 도입합니다. 이는 힘 인식 Mixture-of-Experts 융합 모듈로, 행동 디코딩 중에 사전 학습된 시각-언어 임베딩과 실시간 6축 힘 피드백을 동적으로 통합합니다. 이를 통해 모달리티별 전문가 간의 상황 인식 라우팅이 가능해져, 로봇이 미세한 접촉 역학에 적응하는 능력을 향상시킵니다. 또한, 우리는 5가지 접촉이 많은 조작 작업에 걸쳐 동기화된 시각, 고유수용감각, 힘-토크 신호로 구성된 새로운 데이터셋인 \textbf{ForceVLA-Data}를 소개합니다. ForceVLA는 강력한 pi_0 기반 기준선 대비 평균 작업 성공률을 23.2% 향상시켜, 플러그 삽입과 같은 작업에서 최대 80%의 성공률을 달성합니다. 우리의 접근 방식은 정교한 조작을 위한 다중 모달 통합의 중요성을 강조하며, 물리적으로 지능적인 로봇 제어를 위한 새로운 기준을 제시합니다. 코드와 데이터는 https://sites.google.com/view/forcevla2025에서 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 사전 학습된 시각 및 언어 표현을 활용하여 범용 로봇 조작을 발전시켰습니다. 그러나 시각적 폐색이나 동적 불확실성 하에서 힘과 관련된 세밀한 제어가 필요한 접촉이 많은 작업에서는 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 외부 힘 감지를 VLA 시스템 내에서 일급 모달리티로 취급하는 새로운 엔드투엔드 조작 프레임워크인 ForceVLA를 제안합니다. ForceVLA는 FVLMoE를 도입합니다. 이는 힘 인식 Mixture-of-Experts 융합 모듈로, 행동 디코딩 중에 사전 학습된 시각-언어 임베딩과 실시간 6축 힘 피드백을 동적으로 통합합니다. 이를 통해 모달리티별 전문가 간의 상황 인식 라우팅이 가능해져, 로봇이 미세한 접촉 역학에 적응하는 능력을 향상시킵니다. 또한, 우리는 5가지 접촉이 많은 조작 작업에 걸쳐 동기화된 시각, 고유수용감각, 힘-토크 신호로 구성된 새로운 데이터셋인 \textbf{ForceVLA-Data}를 소개합니다. ForceVLA는 강력한 pi_0 기반 기준선 대비 평균 작업 성공률을 23.2% 향상시켜, 플러그 삽입과 같은 작업에서 최대 80%의 성공률을 달성합니다. 우리의 접근 방식은 정교한 조작을 위한 다중 모달 통합의 중요성을 강조하며, 물리적으로 지능적인 로봇 제어를 위한 새로운 기준을 제시합니다. 코드와 데이터는 https://sites.google.com/view/forcevla2025에서 공개될 예정입니다.
