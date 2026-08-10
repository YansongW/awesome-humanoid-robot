---
$id: ent_paper_wu_do_what_you_say_steering_visio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification'
  zh: SEAL
  ko: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification'
summary:
  en: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
  zh: SEAL 是 2025 年由犹他大学与 NVIDIA 提出的视觉-语言-动作模型，旨在解决推理型 VLA 模型在执行时动作与文本计划不一致的问题。其核心贡献是一种无需训练的运行时策略引导方法，通过模拟候选动作序列并用预训练 VLM
    验证其与文本计划的对齐程度，从而提升机器人操作在分布外场景下的鲁棒性，并在行为组合任务上取得最高 15% 的性能提升。
  ko: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (SEAL),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Utah, NVIDIA.'
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
- seal
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.16281v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1194 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Do What You Say: Steering Vision-Language-Action Models via Runtime Reasoning-Action Alignment Verification (arXiv)'
  url: https://arxiv.org/abs/2510.16281
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SEAL source
  url: https://doi.org/10.48550/arXiv.2510.16281
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
推理型视觉-语言-动作模型通过生成逐步文本计划来改进机器人指令跟随，但即使文本计划正确，生成的动作仍可能偏离预期结果，尤其在分布外场景中。SEAL 将这一现象形式化为具身 CoT 忠实度缺失问题，并提出一种无需训练的运行时策略引导方法：从同一模型中采样多个候选动作序列，通过仿真预测其执行结果，再利用预训练 VLM 选择与文本计划最匹配的序列。该方法将基础 VLA 模型的动作多样性从误差来源转化为优势，显著提升对语义和视觉分布外扰动的鲁棒性，并支持无需重新训练的新行为组合。研究还贡献了带推理标注的 LIBERO-100 扩展版本及专为分布外评估设计的环境变体，在行为组合任务上相比先前工作提升最高 15%，且性能随计算量与数据多样性扩展。

## 核心内容
### 问题定义
- 推理型 VLA 模型（如基于 CoT 的模型）在生成文本计划后，执行的动作可能无法忠实反映计划意图，尤其在分布外场景中。
- 该现象被形式化为“具身 CoT 忠实度缺失”，即文本推理与动作执行之间的对齐失败。

### 方法：SEAL 框架
- **核心思想**：无需训练，在运行时通过验证动作序列与文本计划的对齐程度来引导策略选择。
- **步骤**：
  1. 从同一推理 VLA 模型中采样多个候选动作序列。
  2. 通过仿真预测每个序列的执行结果（如物体位置变化）。
  3. 使用预训练 VLM（如 CLIP 或 GPT-4V）评估仿真结果与原始文本计划的一致性，选择最匹配的序列执行。
- **关键创新**：将基础 VLA 模型的动作多样性从误差来源转化为优势——仅执行与文本推理对齐的动作，从而提升鲁棒性。

### 实验设置
- **基准**：在 LIBERO-100 数据集基础上扩展，添加推理标注（文本计划），并设计多种分布外场景变体（语义扰动、视觉扰动、行为组合）。
- **对比方法**：与标准 VLA 模型（如 RT-2、Octo）及 CoT 增强版本对比。
- **评估指标**：任务成功率、对齐准确率、分布外鲁棒性。

### 关键结果
- **性能提升**：在行为组合任务上，SEAL 相比先前工作提升最高 15%。
- **鲁棒性**：在语义扰动（如物体名称替换）和视觉扰动（如背景变化）下，SEAL 保持稳定性能，而基线模型显著下降。
- **可扩展性**：性能随候选动作序列采样数量（计算量）和训练数据多样性增加而提升。
- **无需重训练**：SEAL 可直接应用于现有推理 VLA 模型，无需额外微调或数据收集。

### 结论
SEAL 通过运行时推理-动作对齐验证，有效解决了推理型 VLA 模型的忠实度问题，为机器人操作提供了一种轻量级、可扩展的鲁棒性增强方案。其方法在分布外场景和行为组合中表现出显著优势，且与计算资源及数据多样性呈正相关。

## Overview
Reasoning Vision Language Action (VLA) models improve robotic instruction-following by generating step-by-step textual plans before low-level actions, an approach inspired by Chain-of-Thought (CoT) reasoning in language models. Yet even with a correct textual plan, the generated actions can still miss the intended outcomes in the plan, especially in out-of-distribution (OOD) scenarios. We formalize this phenomenon as a lack of embodied CoT faithfulness, and introduce a training-free, runtime policy steering method for reasoning-action alignment. Given a reasoning VLA's intermediate textual plan, our framework samples multiple candidate action sequences from the same model, predicts their outcomes via simulation, and uses a pre-trained Vision-Language Model (VLM) to select the sequence whose outcome best aligns with the VLA's own textual plan. Only executing action sequences that align with the textual reasoning turns our base VLA's natural action diversity from a source of error into a strength, boosting robustness to semantic and visual OOD perturbations and enabling novel behavior composition without costly re-training. We also contribute a reasoning-annotated extension of LIBERO-100, environment variations tailored for OOD evaluation, and demonstrate up to 15% performance gain over prior work on behavior composition tasks and scales with compute and data diversity. Project Website at: https://yilin-wu98.github.io/steering-reasoning-vla/

## 参考
- http://arxiv.org/abs/2510.16281v2

## 개요
추론 기반 비전-언어-행동 모델은 단계별 텍스트 계획을 생성하여 로봇의 지시 따르기를 개선하지만, 텍스트 계획이 정확하더라도 생성된 행동이 예상 결과에서 벗어날 수 있으며, 특히 분포 외 시나리오에서 두드러진다. SEAL은 이러한 현상을 구현된 CoT 충실도 결여 문제로 형식화하고, 훈련 없이 런타임에 정책을 안내하는 방법을 제안한다: 동일한 모델에서 여러 후보 행동 시퀀스를 샘플링하고, 시뮬레이션을 통해 실행 결과를 예측한 뒤, 사전 훈련된 VLM을 사용하여 텍스트 계획과 가장 일치하는 시퀀스를 선택한다. 이 방법은 기본 VLA 모델의 행동 다양성을 오류 원인에서 장점으로 전환하여 의미적 및 시각적 분포 외 교란에 대한 견고성을 크게 향상시키고, 재훈련 없이 새로운 행동 조합을 지원한다. 연구는 또한 추론 주석이 포함된 LIBERO-100 확장 버전과 분포 외 평가를 위해 설계된 환경 변형을 제공하며, 행동 조합 작업에서 이전 연구 대비 최대 15% 향상된 성능을 보이고, 성능은 계산량과 데이터 다양성에 따라 확장된다.

## 핵심 내용
### 문제 정의
- 추론 기반 VLA 모델(예: CoT 기반 모델)은 텍스트 계획을 생성한 후, 실행된 행동이 계획의 의도를 충실히 반영하지 못할 수 있으며, 특히 분포 외 시나리오에서 두드러진다.
- 이 현상은 "구현된 CoT 충실도 결여"로 형식화되며, 이는 텍스트 추론과 행동 실행 간의 정렬 실패를 의미한다.

### 방법: SEAL 프레임워크
- **핵심 아이디어**: 훈련 없이 런타임에 행동 시퀀스와 텍스트 계획 간의 정렬 정도를 검증하여 정책 선택을 안내한다.
- **단계**:
  1. 동일한 추론 VLA 모델에서 여러 후보 행동 시퀀스를 샘플링한다.
  2. 시뮬레이션을 통해 각 시퀀스의 실행 결과(예: 객체 위치 변화)를 예측한다.
  3. 사전 훈련된 VLM(예: CLIP 또는 GPT-4V)을 사용하여 시뮬레이션 결과와 원본 텍스트 계획의 일관성을 평가하고, 가장 일치하는 시퀀스를 선택하여 실행한다.
- **핵심 혁신**: 기본 VLA 모델의 행동 다양성을 오류 원인에서 장점으로 전환한다—텍스트 추론과 정렬된 행동만 실행하여 견고성을 향상시킨다.

### 실험 설정
- **벤치마크**: LIBERO-100 데이터셋을 확장하여 추론 주석(텍스트 계획)을 추가하고, 다양한 분포 외 시나리오 변형(의미적 교란, 시각적 교란, 행동 조합)을 설계한다.
- **비교 방법**: 표준 VLA 모델(예: RT-2, Octo) 및 CoT 강화 버전과 비교한다.
- **평가 지표**: 작업 성공률, 정렬 정확도, 분포 외 견고성.

### 핵심 결과
- **성능 향상**: 행동 조합 작업에서 SEAL은 이전 연구 대비 최대 15% 향상된 성능을 보인다.
- **견고성**: 의미적 교란(예: 객체 이름 대체) 및 시각적 교란(예: 배경 변화) 하에서 SEAL은 안정적인 성능을 유지하는 반면, 기준 모델은 크게 저하된다.
- **확장성**: 성능은 후보 행동 시퀀스 샘플링 수(계산량)와 훈련 데이터 다양성에 따라 향상된다.
- **재훈련 불필요**: SEAL은 추가 미세 조정이나 데이터 수집 없이 기존 추론 VLA 모델에 직접 적용할 수 있다.

### 결론
SEAL은 런타임 추론-행동 정렬 검증을 통해 추론 기반 VLA 모델의 충실도 문제를 효과적으로 해결하며, 로봇 조작을 위한 경량화되고 확장 가능한 견고성 향상 방안을 제공한다. 이 방법은 분포 외 시나리오와 행동 조합에서 뚜렷한 이점을 보이며, 계산 자원 및 데이터 다양성과 양의 상관관계를 가진다.
