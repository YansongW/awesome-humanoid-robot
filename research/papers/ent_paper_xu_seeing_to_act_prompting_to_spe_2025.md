---
$id: ent_paper_xu_seeing_to_act_prompting_to_spe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Seeing to Act Prompting to Specify
  zh: BayesVLA
  ko: Seeing to Act Prompting to Specify
summary:
  en: Seeing to Act Prompting to Specify (BayesVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Zhejiang University, UC Berkeley.
  zh: Seeing to Act Prompting to Specify (BayesVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Zhejiang University, UC Berkeley.
  ko: Seeing to Act Prompting to Specify (BayesVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Zhejiang University, UC Berkeley.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bayesvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11218v1.
sources:
- id: src_001
  type: paper
  title: Seeing to Act Prompting to Specify (arXiv)
  url: https://arxiv.org/abs/2512.11218
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BayesVLA source
  url: https://doi.org/10.48550/arXiv.2512.11218
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## 核心内容
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## 参考
- http://arxiv.org/abs/2512.11218v1

## Overview
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## Content
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## 개요
Vision-Language-Action(VLA) 모델에서 분포 외 일반화를 추구하는 과정은 종종 미세 조정 중 Vision-Language Model(VLM) 백본의 치명적 망각으로 인해 방해를 받습니다. 외부 추론 데이터와의 공동 학습이 도움이 되지만, 숙련된 튜닝과 데이터 관련 오버헤드가 필요합니다. 이러한 외부 의존성을 넘어, 우리는 VLA 데이터셋 내에서 본질적 원인을 식별합니다: 언어 다양성이 시각 및 행동 다양성보다 훨씬 낮은 모달리티 불균형입니다. 이 불균형은 모델을 시각적 지름길과 언어 망각으로 편향시킵니다. 이를 해결하기 위해, 우리는 BayesVLA를 소개합니다. 이는 정책을 시각-행동 사전(seeing-to-act 지원)과 언어 조건부 가능도(prompt-to-specify 촉진)로 분해하는 베이지안 분해법입니다. 이는 본질적으로 일반화를 보존하고 명령 수행을 촉진합니다. 또한 사전 접촉 및 사후 접촉 단계를 통합하여 사전 훈련된 기반 모델을 더 잘 활용합니다. 정보 이론적 분석은 지름길 학습 완화에서의 효과를 공식적으로 검증합니다. 광범위한 실험은 기존 방법에 비해 보이지 않는 명령, 객체 및 환경에 대한 우수한 일반화를 보여줍니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://xukechun.github.io/papers/BayesVLA.

## 핵심 내용
Vision-Language-Action(VLA) 모델에서 분포 외 일반화를 추구하는 과정은 종종 미세 조정 중 Vision-Language Model(VLM) 백본의 치명적 망각으로 인해 방해를 받습니다. 외부 추론 데이터와의 공동 학습이 도움이 되지만, 숙련된 튜닝과 데이터 관련 오버헤드가 필요합니다. 이러한 외부 의존성을 넘어, 우리는 VLA 데이터셋 내에서 본질적 원인을 식별합니다: 언어 다양성이 시각 및 행동 다양성보다 훨씬 낮은 모달리티 불균형입니다. 이 불균형은 모델을 시각적 지름길과 언어 망각으로 편향시킵니다. 이를 해결하기 위해, 우리는 BayesVLA를 소개합니다. 이는 정책을 시각-행동 사전(seeing-to-act 지원)과 언어 조건부 가능도(prompt-to-specify 촉진)로 분해하는 베이지안 분해법입니다. 이는 본질적으로 일반화를 보존하고 명령 수행을 촉진합니다. 또한 사전 접촉 및 사후 접촉 단계를 통합하여 사전 훈련된 기반 모델을 더 잘 활용합니다. 정보 이론적 분석은 지름길 학습 완화에서의 효과를 공식적으로 검증합니다. 광범위한 실험은 기존 방법에 비해 보이지 않는 명령, 객체 및 환경에 대한 우수한 일반화를 보여줍니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://xukechun.github.io/papers/BayesVLA.
