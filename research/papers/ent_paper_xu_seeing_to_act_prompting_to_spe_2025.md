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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11218v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1000 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.11218v1

## 개요
BayesVLA는 VLA 모델 미세 조정 시 언어 다양성이 시각 및 행동 다양성보다 훨씬 낮아 발생하는 모달리티 불균형 문제를 해결하기 위해 베이즈 분해 전략을 제안한다. 이 전략은 정책을 시각-행동 사전(‘보면 즉시 행동’ 지원)과 언어 조건부 우도(‘지시하면 지정’ 지원)로 분해하여 VLM의 일반화 능력을 보존하고 명령 수행 성능을 강화한다. 모델은 또한 사전 접촉 및 접촉 후 단계를 도입하여 사전 훈련된 기반 모델을 최대한 활용하며, 정보 이론 분석을 통해 지름길 학습 완화 효과를 검증한다. 실험 결과, BayesVLA는 보지 못한 명령, 객체 및 환경에서의 일반화 성능이 기존 방법보다 크게 우수함을 보여준다.

## 핵심 내용
### 방법
- **베이즈 분해**: 정책 \( \pi(a|o, l) \)을 시각-행동 사전 \( P(a|o) \)과 언어 조건부 우도 \( P(l|a, o) \)의 곱으로 분해한다. 여기서 \( o \)는 관측, \( l \)은 언어 명령, \( a \)는 행동이다. 이 분해는 미세 조정 시 VLM의 시각-행동 연관 능력을 보존하면서 언어 우도 항을 통해 명령 수행을 강화한다.
- **접촉 단계 설계**: 사전 접촉(pre-contact) 및 접촉 후(post-contact) 단계를 도입하여 각각 조작 전 계획과 조작 중 조정에 대응하며, 사전 훈련된 기반 모델의 시공간 추론 능력을 최대한 활용한다.

### 실험 설정
- **벤치마크 및 데이터셋**: 여러 로봇 조작 벤치마크에서 테스트하며, 보지 못한 명령(예: “빨간 블록을 파란 컵 옆에 놓기”), 보지 못한 객체(예: 새로운 모양의 블록), 및 보지 못한 환경(예: 다른 조명과 배경)을 포함한다.
- **비교 방법**: RT-2, Octo, VIMA 등 기존 VLA 모델과 비교하며, 평가 지표는 작업 성공률, 명령 수행 정확도 및 일반화 견고성을 포함한다.

### 주요 결과
- **일반화 성능**: 보지 못한 명령에서 성공률 18.7% 향상, 보지 못한 객체에서 22.3% 향상, 보지 못한 환경에서 15.2% 향상(최고 기준선 대비).
- **정보 이론 분석**: 베이즈 분해는 상호 정보 \( I(a; l|o) \)를 34% 감소시켜 언어 지름길 학습 억제 효과를 검증한다.
- **절제 실험**: 접촉 단계 설계를 제거하면 일반화 성능이 12.5% 하락하고, 베이즈 분해를 제거하면 명령 수행 정확도가 27.1% 하락한다.

### 결론
BayesVLA는 베이즈 분해와 접촉 단계 설계를 통해 외부 추론 데이터에 의존하지 않고 VLA 모델 미세 조정에서의 모달리티 불균형과 파괴적 망각 문제를 해결하여 로봇 조작에 더 강력한 일반화 능력을 제공한다. 프로젝트 페이지: https://xukechun.github.io/papers/BayesVLA.
