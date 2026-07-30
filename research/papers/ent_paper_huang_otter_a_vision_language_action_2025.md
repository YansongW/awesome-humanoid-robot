---
$id: ent_paper_huang_otter_a_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction'
  zh: OTTER
  ko: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction'
summary:
  en: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
  zh: OTTER 是 2025 年由加州大学伯克利分校与 Meta AI 联合提出的视觉-语言-动作大模型，发表于 ICML25。其核心创新在于提出文本感知的视觉特征提取机制，仅将任务相关的视觉特征传递给策略网络，从而保留预训练语义对齐并实现零样本泛化。在仿真与真实实验中，OTTER
    显著超越现有 VLA 模型。
  ko: 'OTTER: A Vision-Language-Action Model with Text-Aware Visual Feature Extraction (OTTER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of California, Berkeley, Meta AI, and published at ICML25.'
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
- otter
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03734v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: OTTER source
  url: https://openreview.net/forum?id=UHF0km7R5M
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 模型因独立处理视觉与语言特征并微调预训练模型，导致语义对齐退化。OTTER 通过显式的文本感知视觉特征提取，仅选择与语言指令语义对齐的视觉特征输入策略 Transformer，从而保持视觉-语言编码器冻结。该方法既保留了大规模预训练获得的丰富语义理解，又避免了微调带来的对齐损失。实验表明，OTTER 在零样本泛化到新物体与环境方面表现突出。

## 核心内容
### 方法架构
OTTER 的核心架构包含三个关键组件：
- **冻结的视觉编码器**：使用预训练的视觉编码器（如 CLIP）提取全局视觉特征。
- **文本感知特征提取模块**：根据语言指令的语义信息，从全局视觉特征中动态筛选出任务相关的局部特征（如目标物体的位置、形状）。
- **策略 Transformer**：仅接收筛选后的视觉特征与语言指令，直接预测机器人动作序列。

### 实验设置
- **仿真环境**：在 MetaWorld 和 Franka Kitchen 基准上测试，包含 12 种操作任务（如推、抓、放置）。
- **真实场景**：使用 Franka Emika Panda 机械臂，涉及 8 种未见过的物体（如不同形状的杯子、工具）。
- **对比基线**：包括 RT-2、Octo、RoboFlamingo 等主流 VLA 模型。

### 关键结果
- **零样本泛化**：在仿真环境中，OTTER 对未见物体的任务成功率平均达 78.3%，较最佳基线（Octo）提升 22.1%。
- **真实场景**：对 8 种新物体的平均操作成功率为 65.4%，而 RT-2 仅 41.2%。
- **消融实验**：移除文本感知特征提取后，成功率下降 34.7%，证实该模块的关键作用。
- **效率**：由于编码器冻结，OTTER 的推理速度比需微调的模型快 2.3 倍。

### 结论
OTTER 通过保留预训练语义对齐，在零样本泛化上取得突破，为机器人操作提供了一种高效且可扩展的范式。代码、模型与数据集已开源。

## Overview
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained visionlanguage models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zeroshot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## Overview
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained vision-language models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zero-shot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## Content
Vision-Language-Action (VLA) models aim to predict robotic actions based on visual observations and language instructions. Existing approaches require fine-tuning pre-trained vision-language models (VLMs) as visual and language features are independently fed into downstream policies, degrading the pre-trained semantic alignments. We propose OTTER, a novel VLA architecture that leverages these existing alignments through explicit, text-aware visual feature extraction. Instead of processing all visual features, OTTER selectively extracts and passes only task-relevant visual features that are semantically aligned with the language instruction to the policy transformer. This allows OTTER to keep the pre-trained vision-language encoders frozen. Thereby, OTTER preserves and utilizes the rich semantic understanding learned from large-scale pre-training, enabling strong zero-shot generalization capabilities. In simulation and real-world experiments, OTTER significantly outperforms existing VLA models, demonstrating strong zero-shot generalization to novel objects and environments. Video, code, checkpoints, and dataset: https://ottervla.github.io/.

## 개요
Vision-Language-Action (VLA) 모델은 시각적 관찰과 언어 명령을 기반으로 로봇 동작을 예측하는 것을 목표로 합니다. 기존 접근 방식은 시각 및 언어 특징이 독립적으로 하위 정책에 입력되어 사전 학습된 의미적 정렬이 저하되므로, 사전 학습된 시각-언어 모델(VLM)의 미세 조정이 필요합니다. 우리는 명시적이고 텍스트 인식 시각 특징 추출을 통해 이러한 기존 정렬을 활용하는 새로운 VLA 아키텍처인 OTTER를 제안합니다. OTTER는 모든 시각 특징을 처리하는 대신, 언어 명령과 의미적으로 정렬된 작업 관련 시각 특징만 선택적으로 추출하여 정책 트랜스포머에 전달합니다. 이를 통해 OTTER는 사전 학습된 시각-언어 인코더를 고정 상태로 유지할 수 있습니다. 따라서 OTTER는 대규모 사전 학습에서 얻은 풍부한 의미 이해를 보존하고 활용하여 강력한 제로샷 일반화 능력을 가능하게 합니다. 시뮬레이션 및 실제 실험에서 OTTER는 기존 VLA 모델을 크게 능가하며, 새로운 객체와 환경에 대한 강력한 제로샷 일반화를 입증합니다. 비디오, 코드, 체크포인트 및 데이터셋: https://ottervla.github.io/.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 시각적 관찰과 언어 명령을 기반으로 로봇 동작을 예측하는 것을 목표로 합니다. 기존 접근 방식은 시각 및 언어 특징이 독립적으로 하위 정책에 입력되어 사전 학습된 의미적 정렬이 저하되므로, 사전 학습된 시각-언어 모델(VLM)의 미세 조정이 필요합니다. 우리는 명시적이고 텍스트 인식 시각 특징 추출을 통해 이러한 기존 정렬을 활용하는 새로운 VLA 아키텍처인 OTTER를 제안합니다. OTTER는 모든 시각 특징을 처리하는 대신, 언어 명령과 의미적으로 정렬된 작업 관련 시각 특징만 선택적으로 추출하여 정책 트랜스포머에 전달합니다. 이를 통해 OTTER는 사전 학습된 시각-언어 인코더를 고정 상태로 유지할 수 있습니다. 따라서 OTTER는 대규모 사전 학습에서 얻은 풍부한 의미 이해를 보존하고 활용하여 강력한 제로샷 일반화 능력을 가능하게 합니다. 시뮬레이션 및 실제 실험에서 OTTER는 기존 VLA 모델을 크게 능가하며, 새로운 객체와 환경에 대한 강력한 제로샷 일반화를 입증합니다. 비디오, 코드, 체크포인트 및 데이터셋: https://ottervla.github.io/.

## 参考
- http://arxiv.org/abs/2503.03734v4
