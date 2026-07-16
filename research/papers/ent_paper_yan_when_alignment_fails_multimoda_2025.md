---
$id: ent_paper_yan_when_alignment_fails_multimoda_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models'
  zh: VLA-Fool
  ko: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models'
summary:
  en: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
  zh: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
  ko: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (VLA-Fool), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Westlake University, Pennsylvania State University, Sony Research, Xidian
    University.'
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
- vision_language_action
- vla
- vla_fool
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16203v3.
sources:
- id: src_001
  type: paper
  title: 'When Alignment Fails: Multimodal Adversarial Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.16203
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Fool source
  url: https://doi.org/10.48550/arXiv.2511.16203
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## 核心内容
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## 参考
- http://arxiv.org/abs/2511.16203v3

## Overview
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## Content
Vision-Language-Action models (VLAs) have recently demonstrated remarkable progress in embodied environments, enabling robots to perceive, reason, and act through unified multimodal understanding. Despite their impressive capabilities, the adversarial robustness of these systems remains largely unexplored, especially under realistic multimodal and black-box conditions. Existing studies mainly focus on single-modality perturbations and overlook the cross-modal misalignment that fundamentally affects embodied reasoning and decision-making. In this paper, we introduce VLA-Fool, a comprehensive study of multimodal adversarial robustness in embodied VLA models under both white-box and black-box settings. VLA-Fool unifies three levels of multimodal adversarial attacks: (1) textual perturbations through gradient-based and prompt-based manipulations, (2) visual perturbations via patch and noise distortions, and (3) cross-modal misalignment attacks that intentionally disrupt the semantic correspondence between perception and instruction. We further incorporate a VLA-aware semantic space into linguistic prompts, developing the first automatically crafted and semantically guided prompting framework. Experiments on the LIBERO benchmark using a fine-tuned OpenVLA model reveal that even minor multimodal perturbations can cause significant behavioral deviations, demonstrating the fragility of embodied multimodal alignment.

## 개요
Vision-Language-Action 모델(VLA)은 최근 임베디드 환경에서 놀라운 발전을 보여주며, 로봇이 통합된 다중 모드 이해를 통해 인지, 추론 및 행동을 수행할 수 있게 했습니다. 이러한 인상적인 능력에도 불구하고, 이러한 시스템의 적대적 강건성은 특히 현실적인 다중 모드 및 블랙박스 조건에서 거의 탐구되지 않았습니다. 기존 연구는 주로 단일 모드 교란에 초점을 맞추고 있으며, 임베디드 추론과 의사 결정에 근본적으로 영향을 미치는 교차 모드 불일치를 간과하고 있습니다. 본 논문에서는 화이트박스 및 블랙박스 설정 모두에서 임베디드 VLA 모델의 다중 모드 적대적 강건성에 대한 포괄적인 연구인 VLA-Fool을 소개합니다. VLA-Fool은 세 가지 수준의 다중 모드 적대적 공격을 통합합니다: (1) 그래디언트 기반 및 프롬프트 기반 조작을 통한 텍스트 교란, (2) 패치 및 노이즈 왜곡을 통한 시각적 교란, (3) 인식과 명령 간의 의미적 대응을 의도적으로 방해하는 교차 모드 불일치 공격입니다. 또한 VLA 인식 의미 공간을 언어 프롬프트에 통합하여 최초의 자동 생성 및 의미 기반 프롬프팅 프레임워크를 개발했습니다. 미세 조정된 OpenVLA 모델을 사용한 LIBERO 벤치마크 실험은 사소한 다중 모드 교란조차도 상당한 행동 편차를 유발할 수 있음을 보여주며, 임베디드 다중 모드 정렬의 취약성을 입증합니다.

## 핵심 내용
Vision-Language-Action 모델(VLA)은 최근 임베디드 환경에서 놀라운 발전을 보여주며, 로봇이 통합된 다중 모드 이해를 통해 인지, 추론 및 행동을 수행할 수 있게 했습니다. 이러한 인상적인 능력에도 불구하고, 이러한 시스템의 적대적 강건성은 특히 현실적인 다중 모드 및 블랙박스 조건에서 거의 탐구되지 않았습니다. 기존 연구는 주로 단일 모드 교란에 초점을 맞추고 있으며, 임베디드 추론과 의사 결정에 근본적으로 영향을 미치는 교차 모드 불일치를 간과하고 있습니다. 본 논문에서는 화이트박스 및 블랙박스 설정 모두에서 임베디드 VLA 모델의 다중 모드 적대적 강건성에 대한 포괄적인 연구인 VLA-Fool을 소개합니다. VLA-Fool은 세 가지 수준의 다중 모드 적대적 공격을 통합합니다: (1) 그래디언트 기반 및 프롬프트 기반 조작을 통한 텍스트 교란, (2) 패치 및 노이즈 왜곡을 통한 시각적 교란, (3) 인식과 명령 간의 의미적 대응을 의도적으로 방해하는 교차 모드 불일치 공격입니다. 또한 VLA 인식 의미 공간을 언어 프롬프트에 통합하여 최초의 자동 생성 및 의미 기반 프롬프팅 프레임워크를 개발했습니다. 미세 조정된 OpenVLA 모델을 사용한 LIBERO 벤치마크 실험은 사소한 다중 모드 교란조차도 상당한 행동 편차를 유발할 수 있음을 보여주며, 임베디드 다중 모드 정렬의 취약성을 입증합니다.
