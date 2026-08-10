---
$id: ent_paper_zhou_chatvla_2_vision_language_acti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge'
  zh: ChatVLA-2
  ko: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge'
summary:
  en: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (ChatVLA-2), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea
    Group, Shanghai University, and published at NIPS25.'
  zh: ChatVLA-2 是华东师范大学、美的集团、上海大学联合提出的 2025 年大型视觉-语言-动作模型，发表于 NIPS25。其核心贡献在于通过混合专家架构与两阶段训练流程，保留并扩展预训练 VLM 的开放世界具身推理能力，在数学推理、OCR
    和空间推理任务上显著超越 OpenVLA、DexVLA 等现有方法。
  ko: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (ChatVLA-2), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by East China Normal University, Midea
    Group, Shanghai University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- chatvla_2
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.21906v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (945 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ChatVLA-2: Vision-Language-Action Model with Open-World Embodied Reasoning from Pretrained Knowledge (arXiv)'
  url: https://arxiv.org/abs/2505.21906
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ChatVLA-2 source
  url: https://doi.org/10.48550/arXiv.2505.21906
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ChatVLA-2 旨在解决现有端到端 VLA 系统在微调过程中丢失预训练 VLM 关键能力的问题。该模型采用混合专家架构，配合专门设计的两阶段训练流程，确保模型既能继承 VLM 的开放世界知识（如物体识别、数学解题、视觉空间智能），又能将推理结果转化为机器人可执行的动作。在数学匹配任务中，机器人能解读白板上的数学问题并从桌上选取对应数字卡片完成方程求解，展现出未经显式训练的数学推理与 OCR 能力。此外，模型还能理解涉及未见物体的新型方向指令，具备强大的空间推理能力。

## 核心内容
### 方法
- **混合专家架构**：ChatVLA-2 采用 mixture-of-expert 设计，通过多个专家模块协同处理视觉、语言和动作信息，避免单一模型在微调时丢失预训练知识。
- **两阶段训练流程**：
  - 第一阶段：保留 VLM 的开放世界推理能力，包括物体识别、数学问题求解和视觉空间智能。
  - 第二阶段：将推理结果转化为机器人可执行的动作步骤，实现 reasoning following。

### 实验设置
- **数学匹配任务**：机器人需解读白板上的数学问题，从桌上选取对应数字卡片完成方程求解。该任务测试模型的数学推理与 OCR 能力，且这些能力未在 VLA 训练中显式提供。
- **空间推理任务**：模型需理解涉及未见物体的新型方向指令，例如“将红色方块移动到蓝色圆柱的左侧”。

### 关键结果
- **数学推理与 OCR**：ChatVLA-2 在数学匹配任务中表现出色，能准确识别白板上的数学表达式并选取正确数字卡片，尽管这些能力未在 VLA 训练中显式训练。
- **空间推理**：模型能理解涉及未见物体的新型方向指令，展现出强大的视觉空间智能。
- **对比结果**：在推理与理解能力上，ChatVLA-2 显著超越当前最先进的模仿学习方法，包括 OpenVLA、DexVLA 和 pi-zero。

### 结论
ChatVLA-2 通过混合专家架构与两阶段训练流程，成功保留了 VLM 的开放世界推理能力，并将其转化为机器人可执行的动作。该工作为开发真正可泛化的机器人基础模型提供了重要进展，尤其在高阶推理与理解能力方面。

## Overview
Vision-language-action (VLA) models have emerged as the next generation of models in robotics. However, despite leveraging powerful pre-trained Vision-Language Models (VLMs), existing end-to-end VLA systems often lose key capabilities during fine-tuning as the model adapts to specific robotic tasks. We argue that a generalizable VLA model should retain and expand upon the VLM's core competencies: 1) Open-world embodied reasoning - the VLA should inherit the knowledge from VLM, i.e., recognize anything that the VLM can recognize, be capable of solving math problems, and possess visual-spatial intelligence, 2) Reasoning following - effectively translating the open-world reasoning into actionable steps for the robot. In this work, we introduce ChatVLA-2, a novel mixture-of-expert VLA model coupled with a specialized two-stage training pipeline designed to preserve the VLM's original strengths while enabling actionable reasoning. To validate our approach, we design a math-matching task wherein a robot interprets math problems written on a whiteboard and picks corresponding number cards from a table to solve equations. Remarkably, our method exhibits exceptional mathematical reasoning and OCR capabilities, despite these abilities not being explicitly trained within the VLA. Furthermore, we demonstrate that the VLA possesses strong spatial reasoning skills, enabling it to interpret novel directional instructions involving previously unseen objects. Overall, our method showcases reasoning and comprehension abilities that significantly surpass state-of-the-art imitation learning methods such as OpenVLA, DexVLA, and pi-zero. This work represents a substantial advancement toward developing truly generalizable robotic foundation models endowed with robust reasoning capacities.

## 参考
- http://arxiv.org/abs/2505.21906v2

## 개요
ChatVLA-2는 기존 엔드투엔드 VLA 시스템이 미세 조정 과정에서 사전 훈련된 VLM의 핵심 능력을 상실하는 문제를 해결하는 것을 목표로 합니다. 이 모델은 혼합 전문가 아키텍처를 채택하고, 특별히 설계된 2단계 훈련 프로세스를 통해 모델이 VLM의 개방형 세계 지식(예: 객체 인식, 수학 문제 해결, 시각적 공간 지능)을 상속하면서도 추론 결과를 로봇이 실행 가능한 동작으로 변환할 수 있도록 보장합니다. 수학 매칭 작업에서 로봇은 화이트보드의 수학 문제를 해석하고 테이블에서 해당 숫자 카드를 선택하여 방정식을 완성하며, 명시적으로 훈련되지 않은 수학 추론 및 OCR 능력을 보여줍니다. 또한 모델은 보지 못한 객체를 포함한 새로운 방향 지시를 이해할 수 있어 강력한 공간 추론 능력을 갖추고 있습니다.

## 핵심 내용
### 방법
- **혼합 전문가 아키텍처**: ChatVLA-2는 mixture-of-expert 설계를 채택하여 여러 전문가 모듈이 시각, 언어, 동작 정보를 협력적으로 처리함으로써 단일 모델이 미세 조정 시 사전 훈련 지식을 잃는 것을 방지합니다.
- **2단계 훈련 프로세스**:
  - 1단계: VLM의 개방형 세계 추론 능력(객체 인식, 수학 문제 해결, 시각적 공간 지능 포함)을 유지합니다.
  - 2단계: 추론 결과를 로봇이 실행 가능한 동작 단계로 변환하여 reasoning following을 구현합니다.

### 실험 설정
- **수학 매칭 작업**: 로봇은 화이트보드의 수학 문제를 해석하고 테이블에서 해당 숫자 카드를 선택하여 방정식을 완성해야 합니다. 이 작업은 모델의 수학 추론 및 OCR 능력을 테스트하며, 이러한 능력은 VLA 훈련에서 명시적으로 제공되지 않습니다.
- **공간 추론 작업**: 모델은 보지 못한 객체를 포함한 새로운 방향 지시(예: "빨간 블록을 파란 원통의 왼쪽으로 이동")를 이해해야 합니다.

### 주요 결과
- **수학 추론 및 OCR**: ChatVLA-2는 수학 매칭 작업에서 뛰어난 성능을 보이며, VLA 훈련에서 명시적으로 훈련되지 않았음에도 화이트보드의 수학 표현식을 정확히 인식하고 올바른 숫자 카드를 선택합니다.
- **공간 추론**: 모델은 보지 못한 객체를 포함한 새로운 방향 지시를 이해할 수 있어 강력한 시각적 공간 지능을 보여줍니다.
- **비교 결과**: 추론 및 이해 능력에서 ChatVLA-2는 OpenVLA, DexVLA, pi-zero를 포함한 현재 최첨단 모방 학습 방법을 크게 능가합니다.

### 결론
ChatVLA-2는 혼합 전문가 아키텍처와 2단계 훈련 프로세스를 통해 VLM의 개방형 세계 추론 능력을 성공적으로 유지하고 이를 로봇이 실행 가능한 동작으로 변환합니다. 이 작업은 특히 고차원 추론 및 이해 능력 측면에서 진정으로 일반화 가능한 로봇 기반 모델을 개발하는 데 중요한 진전을 제공합니다.
