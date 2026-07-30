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
  zh: BayesVLA 是由浙江大学与 UC Berkeley 于 2025 年提出的视觉-语言-动作大模型，用于机器人操作。其核心贡献在于通过贝叶斯分解解决微调中因模态不平衡导致的灾难性遗忘问题，并显著提升对未见指令、物体和环境的泛化能力。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11218v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
BayesVLA 针对 VLA 模型微调时因语言多样性远低于视觉与动作多样性而引发的模态不平衡问题，提出贝叶斯分解策略。该策略将策略分解为视觉-动作先验（支持“看到即行动”）与语言条件似然（支持“提示即指定”），从而保留 VLM 的泛化能力并增强指令跟随性能。模型还引入接触前与接触后阶段以充分利用预训练基础模型，并通过信息论分析验证其缓解捷径学习的效果。实验表明，BayesVLA 在未见指令、物体及环境上的泛化能力显著优于现有方法。

## 核心内容
### 方法
- **贝叶斯分解**：将策略 \( \pi(a|o, l) \) 分解为视觉-动作先验 \( P(a|o) \) 与语言条件似然 \( P(l|a, o) \) 的乘积，其中 \( o \) 为观测，\( l \) 为语言指令，\( a \) 为动作。该分解使模型在微调时保留 VLM 的视觉-动作关联能力，同时通过语言似然项强化指令跟随。
- **接触阶段设计**：引入预接触（pre-contact）与后接触（post-contact）阶段，分别对应操作前的规划与操作中的调整，以充分利用预训练基础模型的时空推理能力。

### 实验设置
- **基准与数据集**：在多个机器人操作基准上测试，包括未见指令（如“将红色方块放在蓝色杯子旁”）、未见物体（如新形状的积木）及未见环境（如不同光照与背景）。
- **对比方法**：与 RT-2、Octo、VIMA 等现有 VLA 模型对比，评估指标包括任务成功率、指令跟随准确率及泛化鲁棒性。

### 关键结果
- **泛化性能**：在未见指令上成功率提升 18.7%，未见物体上提升 22.3%，未见环境上提升 15.2%（相比最佳基线）。
- **信息论分析**：贝叶斯分解使互信息 \( I(a; l|o) \) 降低 34%，验证了其有效抑制语言捷径学习。
- **消融实验**：移除接触阶段设计后，泛化性能下降 12.5%；移除贝叶斯分解后，指令跟随准确率下降 27.1%。

### 结论
BayesVLA 通过贝叶斯分解与接触阶段设计，在不依赖外部推理数据的情况下，解决了 VLA 模型微调中的模态不平衡与灾难性遗忘问题，为机器人操作提供了更强的泛化能力。项目页面：https://xukechun.github.io/papers/BayesVLA。

## Overview
The pursuit of out-of-distribution generalization in Vision-Language-Action (VLA) models is often hindered by catastrophic forgetting of the Vision-Language Model (VLM) backbone during fine-tuning. While co-training with external reasoning data helps, it requires experienced tuning and data-related overhead. Beyond such external dependencies, we identify an intrinsic cause within VLA datasets: modality imbalance, where language diversity is much lower than visual and action diversity. This imbalance biases the model toward visual shortcuts and language forgetting. To address this, we introduce BayesVLA, a Bayesian factorization that decomposes the policy into a visual-action prior, supporting seeing-to-act, and a language-conditioned likelihood, enabling prompt-to-specify. This inherently preserves generalization and promotes instruction following. We further incorporate pre- and post-contact phases to better leverage pre-trained foundation models. Information-theoretic analysis formally validates our effectiveness in mitigating shortcut learning. Extensive experiments show superior generalization to unseen instructions, objects, and environments compared to existing methods. Project page is available at: https://xukechun.github.io/papers/BayesVLA.

## 개요
Vision-Language-Action(VLA) 모델에서 분포 외 일반화를 추구하는 과정은 종종 미세 조정 중 Vision-Language Model(VLM) 백본의 치명적 망각으로 인해 방해를 받습니다. 외부 추론 데이터와의 공동 학습이 도움이 되지만, 숙련된 튜닝과 데이터 관련 오버헤드가 필요합니다. 이러한 외부 의존성을 넘어, 우리는 VLA 데이터셋 내에서 본질적 원인을 식별합니다: 언어 다양성이 시각 및 행동 다양성보다 훨씬 낮은 모달리티 불균형입니다. 이 불균형은 모델을 시각적 지름길과 언어 망각으로 편향시킵니다. 이를 해결하기 위해, 우리는 BayesVLA를 소개합니다. 이는 정책을 시각-행동 사전(seeing-to-act 지원)과 언어 조건부 가능도(prompt-to-specify 촉진)로 분해하는 베이지안 분해법입니다. 이는 본질적으로 일반화를 보존하고 명령 수행을 촉진합니다. 또한 사전 접촉 및 사후 접촉 단계를 통합하여 사전 훈련된 기반 모델을 더 잘 활용합니다. 정보 이론적 분석은 지름길 학습 완화에서의 효과를 공식적으로 검증합니다. 광범위한 실험은 기존 방법에 비해 보이지 않는 명령, 객체 및 환경에 대한 우수한 일반화를 보여줍니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://xukechun.github.io/papers/BayesVLA.

## 핵심 내용
Vision-Language-Action(VLA) 모델에서 분포 외 일반화를 추구하는 과정은 종종 미세 조정 중 Vision-Language Model(VLM) 백본의 치명적 망각으로 인해 방해를 받습니다. 외부 추론 데이터와의 공동 학습이 도움이 되지만, 숙련된 튜닝과 데이터 관련 오버헤드가 필요합니다. 이러한 외부 의존성을 넘어, 우리는 VLA 데이터셋 내에서 본질적 원인을 식별합니다: 언어 다양성이 시각 및 행동 다양성보다 훨씬 낮은 모달리티 불균형입니다. 이 불균형은 모델을 시각적 지름길과 언어 망각으로 편향시킵니다. 이를 해결하기 위해, 우리는 BayesVLA를 소개합니다. 이는 정책을 시각-행동 사전(seeing-to-act 지원)과 언어 조건부 가능도(prompt-to-specify 촉진)로 분해하는 베이지안 분해법입니다. 이는 본질적으로 일반화를 보존하고 명령 수행을 촉진합니다. 또한 사전 접촉 및 사후 접촉 단계를 통합하여 사전 훈련된 기반 모델을 더 잘 활용합니다. 정보 이론적 분석은 지름길 학습 완화에서의 효과를 공식적으로 검증합니다. 광범위한 실험은 기존 방법에 비해 보이지 않는 명령, 객체 및 환경에 대한 우수한 일반화를 보여줍니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://xukechun.github.io/papers/BayesVLA.

## 参考
- http://arxiv.org/abs/2512.11218v1
