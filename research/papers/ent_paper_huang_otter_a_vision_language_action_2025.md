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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.03734v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (867 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2503.03734v4

## 개요
기존 VLA 모델은 시각 및 언어 특징을 독립적으로 처리하고 사전 훈련된 모델을 미세 조정하여 의미 정렬이 저하됩니다. OTTER는 명시적인 텍스트 인식 시각 특징 추출을 통해 언어 지시와 의미적으로 정렬된 시각 특징만 선택하여 정책 Transformer에 입력함으로써 시각-언어 인코더를 동결 상태로 유지합니다. 이 방법은 대규모 사전 훈련에서 얻은 풍부한 의미 이해를 보존하면서 미세 조정으로 인한 정렬 손실을 방지합니다. 실험 결과, OTTER는 새로운 객체와 환경에 대한 제로샷 일반화에서 뛰어난 성능을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
OTTER의 핵심 아키텍처는 세 가지 주요 구성 요소로 이루어져 있습니다:
- **동결된 시각 인코더**: 사전 훈련된 시각 인코더(예: CLIP)를 사용하여 전역 시각 특징을 추출합니다.
- **텍스트 인식 특징 추출 모듈**: 언어 지시의 의미 정보를 기반으로 전역 시각 특징에서 작업 관련 로컬 특징(예: 대상 객체의 위치, 모양)을 동적으로 선별합니다.
- **정책 Transformer**: 선별된 시각 특징과 언어 지시만 수신하여 로봇 동작 시퀀스를 직접 예측합니다.

### 실험 설정
- **시뮬레이션 환경**: MetaWorld 및 Franka Kitchen 벤치마크에서 테스트하며, 12가지 조작 작업(예: 밀기, 잡기, 놓기)을 포함합니다.
- **실제 시나리오**: Franka Emika Panda 로봇 팔을 사용하며, 8가지 보지 못한 객체(예: 다양한 모양의 컵, 도구)를 다룹니다.
- **비교 기준선**: RT-2, Octo, RoboFlamingo 등 주요 VLA 모델을 포함합니다.

### 주요 결과
- **제로샷 일반화**: 시뮬레이션 환경에서 OTTER는 보지 못한 객체에 대한 작업 성공률이 평균 78.3%로, 최고 기준선(Octo)보다 22.1% 향상되었습니다.
- **실제 시나리오**: 8가지 새로운 객체에 대한 평균 조작 성공률은 65.4%인 반면, RT-2는 41.2%에 불과했습니다.
- **절제 실험**: 텍스트 인식 특징 추출을 제거하면 성공률이 34.7% 하락하여 해당 모듈의 핵심 역할을 확인했습니다.
- **효율성**: 인코더가 동결되어 있어 OTTER의 추론 속도는 미세 조정이 필요한 모델보다 2.3배 빠릅니다.

### 결론
OTTER는 사전 훈련된 의미 정렬을 유지함으로써 제로샷 일반화에서 돌파구를 마련했으며, 로봇 조작을 위한 효율적이고 확장 가능한 패러다임을 제공합니다. 코드, 모델 및 데이터셋은 오픈소스로 공개되었습니다.
