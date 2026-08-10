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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.10845v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (750 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2408.10845v3

## 개요
CoVLA 데이터셋은 자율주행에서 엔드투엔드 경로 계획을 위한 대규모 주석 데이터가 부족한 문제를 해결하기 위해 설계되었습니다. 기존 연구는 주로 다중 모달 대규모 언어 모델을 활용하여 환경을 이해하거나 고수준 운전 명령을 생성하는 데 국한되어 있었지만, CoVLA는 혁신적인 자동화 프로세스를 통해 원시 차량 센서 데이터에서 운전 시나리오 및 조작과 일치하는 궤적과 언어 설명을 생성합니다. 이 데이터셋은 규모와 주석의 풍부함에서 기존 자원을 능가하며, 일관된 언어와 행동을 동시에 출력할 수 있는 VLA 모델을 훈련하고 평가하기 위한 플랫폼을 제공합니다. 실험 결과, CoVLA 기반으로 훈련된 모델은 다양한 운전 시나리오에서 강력한 추론 및 계획 능력을 보여주며, 더 안전하고 해석 가능한 자율주행 시스템 구축의 기반을 마련합니다.

## 핵심 내용
### 방법
- 원시 차량 센서 데이터 기반의 자동화 처리 프로세스를 채택하여, 프레임별 수동 주석이 필요 없음.
- 운전 환경과 조작을 상세한 자연어 설명으로 변환하고 정밀한 주행 궤적과 짝지을 수 있는 설명 생성 파이프라인을 설계.

### 아키텍처
- 데이터셋 자체는 모델 아키텍처를 정의하지 않으며, 다중 모달 대규모 언어 모델을 위한 입력-출력 쌍을 훈련 및 평가용으로 제공.
- 시각 입력(비디오 프레임), 언어 명령(환경 설명), 행동 출력(궤적)을 결합한 모델링을 지원.

### 실험 설정
- 데이터셋은 80시간 이상의 실제 세계 운전 비디오를 포함하며, 다양한 복잡하고 돌발적인 시나리오를 포괄.
- CoVLA를 사용하여 시각, 언어, 행동을 동시에 처리할 수 있는 MLLM을 훈련하고 테스트.

### 주요 수치
- 데이터셋 규모: 80시간 이상의 운전 비디오.
- 주석 유형: 주행 궤적 및 자연어 설명.
- 발표 정보: 2024년 WACV 컨퍼런스, Turing Inc. 제안.

### 결론
- 실험 결과, CoVLA 기반으로 훈련된 모델은 일관된 언어와 행동 출력을 생성할 수 있어, 자율주행에서 VLA 모델의 잠재력을 검증.
- 이 데이터셋은 해석 가능하고 데이터 기반의 자율주행 시스템을 위한 훈련 및 평가 프레임워크를 제공하며, 자율주행의 안전성과 신뢰성 향상에 기여.
- 데이터셋은 학계에 공개되어 있음.
