---
$id: ent_paper_arai_covla_comprehensive_vision_lan_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoVLA: Comprehensive Vision-Language-Action Dataset for Autonomous Driving'
  zh: CoVLA
  ko: 'CoVLA: Comprehensive Vision-Language-Action Dataset for Autonomous Driving'
summary:
  en: 'CoVLA: Comprehensive Vision-Language-Action Dataset for Autonomous Driving (CoVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Turing Inc., and published at WACV 2024.'
  zh: CoVLA 是由 Turing Inc. 于 2024 年 WACV 会议提出的一个大规模视觉-语言-动作数据集，专为自动驾驶中的端到端路径规划而设计。其核心贡献在于通过自动化数据处理与描述生成流水线，提供了超过 80 小时的真实驾驶视频，并配有精确的行驶轨迹与详细自然语言描述。该数据集旨在推动多模态大语言模型在自动驾驶中同时处理视觉、语言与动作的能力。
  ko: 'CoVLA: Comprehensive Vision-Language-Action Dataset for Autonomous Driving (CoVLA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Turing Inc., and published at WACV 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- covla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.10845v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: CoVLA source
  url: https://doi.org/10.1109/WACV61041.2025.00195
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
CoVLA 数据集旨在解决自动驾驶中端到端路径规划缺乏大规模标注数据的问题。现有研究多局限于利用多模态大语言模型理解环境或生成高级驾驶指令，而 CoVLA 通过创新的自动化流程，从原始车载传感器数据中生成与驾驶场景和操作相匹配的轨迹与语言描述。该数据集在规模和标注丰富度上超越了现有资源，为训练和评估能够同时输出连贯语言与动作的 VLA 模型提供了平台。实验结果表明，基于 CoVLA 训练的模型在多种驾驶场景中展现出强大的推理与规划能力，为构建更安全、可解释的自动驾驶系统奠定了基础。

## 核心内容
### 方法
- 采用基于原始车载传感器数据的自动化处理流程，无需人工逐帧标注。
- 设计了一个描述生成流水线，能够将驾驶环境与操作转化为详细的自然语言描述，并与精确的行驶轨迹配对。

### 架构
- 数据集本身不定义模型架构，而是为多模态大语言模型提供训练与评估的输入输出对。
- 支持将视觉输入（视频帧）、语言指令（环境描述）与动作输出（轨迹）联合建模。

### 实验设置
- 数据集包含超过 80 小时的真实世界驾驶视频，覆盖多种复杂与突发场景。
- 使用 CoVLA 训练并测试了能够同时处理视觉、语言与动作的 MLLM。

### 关键数字
- 数据集规模：超过 80 小时驾驶视频。
- 标注类型：行驶轨迹与自然语言描述。
- 发表信息：2024 年 WACV 会议，由 Turing Inc. 提出。

### 结论
- 实验表明，基于 CoVLA 训练的模型能够生成连贯的语言与动作输出，验证了 VLA 模型在自动驾驶中的潜力。
- 该数据集为可解释、数据驱动的自动驾驶系统提供了训练与评估框架，有助于提升自动驾驶的安全性与可靠性。
- 数据集已面向学术界开放。

## Overview
Autonomous driving, particularly navigating complex and unanticipated scenarios, demands sophisticated reasoning and planning capabilities. While Multi-modal Large Language Models (MLLMs) offer a promising avenue for this, their use has been largely confined to understanding complex environmental contexts or generating high-level driving commands, with few studies extending their application to end-to-end path planning. A major research bottleneck is the lack of large-scale annotated datasets encompassing vision, language, and action. To address this issue, we propose CoVLA (Comprehensive Vision-Language-Action) Dataset, an extensive dataset comprising real-world driving videos spanning more than 80 hours. This dataset leverages a novel, scalable approach based on automated data processing and a caption generation pipeline to generate accurate driving trajectories paired with detailed natural language descriptions of driving environments and maneuvers. This approach utilizes raw in-vehicle sensor data, allowing it to surpass existing datasets in scale and annotation richness. Using CoVLA, we investigate the driving capabilities of MLLMs that can handle vision, language, and action in a variety of driving scenarios. Our results illustrate the strong proficiency of our model in generating coherent language and action outputs, emphasizing the potential of Vision-Language-Action (VLA) models in the field of autonomous driving. This dataset establishes a framework for robust, interpretable, and data-driven autonomous driving systems by providing a comprehensive platform for training and evaluating VLA models, contributing to safer and more reliable self-driving vehicles. The dataset is released for academic purpose.

## 개요
자율주행, 특히 복잡하고 예측 불가능한 시나리오를 탐색하는 것은 정교한 추론 및 계획 능력을 요구합니다. 멀티모달 대규모 언어 모델(MLLM)이 이를 위한 유망한 방안을 제시하지만, 그 사용은 주로 복잡한 환경 맥락을 이해하거나 높은 수준의 운전 명령을 생성하는 데 국한되어 있으며, 종단 간 경로 계획에 적용한 연구는 거의 없습니다. 주요 연구 병목 현상은 시각, 언어, 행동을 포괄하는 대규모 주석 데이터셋의 부족입니다. 이 문제를 해결하기 위해, 우리는 80시간 이상의 실제 주행 비디오를 포함하는 광범위한 데이터셋인 CoVLA(Comprehensive Vision-Language-Action) 데이터셋을 제안합니다. 이 데이터셋은 자동화된 데이터 처리와 캡션 생성 파이프라인에 기반한 새롭고 확장 가능한 접근 방식을 활용하여, 정확한 주행 궤적과 상세한 자연어 설명(주행 환경 및 조작)을 쌍으로 생성합니다. 이 접근 방식은 차량 내 센서 원시 데이터를 사용하여, 규모와 주석 풍부성 면에서 기존 데이터셋을 능가합니다. CoVLA를 사용하여, 다양한 주행 시나리오에서 시각, 언어, 행동을 처리할 수 있는 MLLM의 주행 능력을 조사합니다. 우리의 결과는 모델이 일관된 언어 및 행동 출력을 생성하는 데 뛰어난 능력을 보여주며, 자율주행 분야에서 VLA(Vision-Language-Action) 모델의 잠재력을 강조합니다. 이 데이터셋은 VLA 모델을 훈련하고 평가하기 위한 포괄적인 플랫폼을 제공함으로써 강력하고 해석 가능하며 데이터 기반의 자율주행 시스템을 위한 프레임워크를 구축하며, 더 안전하고 신뢰할 수 있는 자율주행 차량에 기여합니다. 데이터셋은 학술 목적으로 공개됩니다.

## 핵심 내용
자율주행, 특히 복잡하고 예측 불가능한 시나리오를 탐색하는 것은 정교한 추론 및 계획 능력을 요구합니다. 멀티모달 대규모 언어 모델(MLLM)이 이를 위한 유망한 방안을 제시하지만, 그 사용은 주로 복잡한 환경 맥락을 이해하거나 높은 수준의 운전 명령을 생성하는 데 국한되어 있으며, 종단 간 경로 계획에 적용한 연구는 거의 없습니다. 주요 연구 병목 현상은 시각, 언어, 행동을 포괄하는 대규모 주석 데이터셋의 부족입니다. 이 문제를 해결하기 위해, 우리는 80시간 이상의 실제 주행 비디오를 포함하는 광범위한 데이터셋인 CoVLA(Comprehensive Vision-Language-Action) 데이터셋을 제안합니다. 이 데이터셋은 자동화된 데이터 처리와 캡션 생성 파이프라인에 기반한 새롭고 확장 가능한 접근 방식을 활용하여, 정확한 주행 궤적과 상세한 자연어 설명(주행 환경 및 조작)을 쌍으로 생성합니다. 이 접근 방식은 차량 내 센서 원시 데이터를 사용하여, 규모와 주석 풍부성 면에서 기존 데이터셋을 능가합니다. CoVLA를 사용하여, 다양한 주행 시나리오에서 시각, 언어, 행동을 처리할 수 있는 MLLM의 주행 능력을 조사합니다. 우리의 결과는 모델이 일관된 언어 및 행동 출력을 생성하는 데 뛰어난 능력을 보여주며, 자율주행 분야에서 VLA(Vision-Language-Action) 모델의 잠재력을 강조합니다. 이 데이터셋은 VLA 모델을 훈련하고 평가하기 위한 포괄적인 플랫폼을 제공함으로써 강력하고 해석 가능하며 데이터 기반의 자율주행 시스템을 위한 프레임워크를 구축하며, 더 안전하고 신뢰할 수 있는 자율주행 차량에 기여합니다. 데이터셋은 학술 목적으로 공개됩니다.

## 参考
- http://arxiv.org/abs/2408.10845v3
