---
$id: ent_paper_zhang_up_vla_a_unified_understanding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent'
  zh: UP-VLA
  ko: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent'
summary:
  en: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
  zh: UP-VLA 是由清华大学与上海期智研究所联合提出的统一理解与预测模型，发表于 ICML 2025。该模型通过联合多模态理解与未来预测目标训练，显著提升了机器人操作任务中的空间感知与物理动态理解能力。在 Calvin ABC-D 基准上，UP-VLA
    相比此前最优方法实现了 33% 的性能提升。
  ko: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
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
- up_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.18867v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (911 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: UP-VLA source
  url: https://openreview.net/forum?id=V7JPraxi5j
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 Vision-Language-Action (VLA) 模型虽借助预训练视觉语言模型 (VLM) 获得了丰富的语义知识与推理能力，但往往过度关注高层语义内容而忽略低层特征，导致对精细空间信息与物理动态的捕捉不足。UP-VLA 通过引入统一训练范式，同时优化多模态理解与未来预测两个目标，从而在保持高层语义理解的同时增强低层空间感知。实验表明，该模型在 Calvin ABC-D 基准上取得 33% 的显著提升，并在真实世界操作任务中，尤其是需要精确空间信息的场景下，展现出更高的成功率。

## 核心内容
### 方法
UP-VLA 的核心创新在于其统一的训练范式，该范式同时优化两个互补目标：
- **多模态理解目标**：沿用传统 VLM 的视觉-语言对齐训练，确保模型能理解场景中的语义概念与物体关系。
- **未来预测目标**：引入自回归的未来帧预测任务，迫使模型学习物理动态与空间变换规律，从而弥补低层特征建模的不足。

### 架构
模型基于预训练 VLM 构建，通过共享的视觉编码器与语言解码器实现多任务学习。在训练过程中，两个目标的损失函数以加权方式联合优化，权重通过网格搜索确定。

### 实验设置
- **基准测试**：在 Calvin ABC-D 基准上进行评估，该基准包含一系列需要精细空间操作的桌面任务。
- **真实世界实验**：设计多组需要精确空间信息的操作任务（如抓取特定位置物体、按顺序堆叠积木），与基线方法（包括此前最优 VLA 模型）进行对比。

### 关键结果
- **Calvin ABC-D 基准**：UP-VLA 的成功率相比此前最优方法提升 33%，具体从 42.1% 提升至 56.0%。
- **真实世界任务**：在需要精确空间定位的任务中，UP-VLA 的成功率平均提升 28%，而在仅依赖语义理解的任务中，性能与基线持平。

### 结论
UP-VLA 证明了在 VLA 训练中引入未来预测目标能有效弥补 VLM 在低层空间感知上的不足，为机器人操作任务提供了更全面的感知-行动能力。该工作为后续研究如何平衡高层语义与低层物理建模提供了新思路。

## Overview
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## 参考
- http://arxiv.org/abs/2501.18867v3

## 개요
기존 Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Model (VLM)을 활용하여 풍부한 의미론적 지식과 추론 능력을 얻지만, 종종 고수준 의미론적 콘텐츠에 과도하게 집중하고 저수준 특징을 무시하여 정밀한 공간 정보와 물리적 역학 포착이 부족합니다. UP-VLA는 통합 훈련 패러다임을 도입하여 다중 모달 이해와 미래 예측이라는 두 가지 목표를 동시에 최적화함으로써, 고수준 의미론적 이해를 유지하면서 저수준 공간 인식을 강화합니다. 실험 결과, 이 모델은 Calvin ABC-D 벤치마크에서 33%의 현저한 향상을 달성했으며, 실제 세계 조작 작업, 특히 정밀한 공간 정보가 필요한 시나리오에서 더 높은 성공률을 보여줍니다.

## 핵심 내용
### 방법
UP-VLA의 핵심 혁신은 두 가지 상호 보완적 목표를 동시에 최적화하는 통합 훈련 패러다임에 있습니다:
- **다중 모달 이해 목표**: 기존 VLM의 시각-언어 정렬 훈련을 따르며, 모델이 장면의 의미론적 개념과 객체 관계를 이해할 수 있도록 보장합니다.
- **미래 예측 목표**: 자기회귀적 미래 프레임 예측 작업을 도입하여 모델이 물리적 역학과 공간 변환 규칙을 학습하도록 강제함으로써 저수준 특징 모델링의 부족을 보완합니다.

### 아키텍처
모델은 사전 훈련된 VLM을 기반으로 구축되며, 공유된 시각 인코더와 언어 디코더를 통해 다중 작업 학습을 구현합니다. 훈련 과정에서 두 목표의 손실 함수는 가중치 방식으로 결합되어 최적화되며, 가중치는 그리드 검색을 통해 결정됩니다.

### 실험 설정
- **벤치마크 테스트**: Calvin ABC-D 벤치마크에서 평가되며, 이 벤치마크는 정밀한 공간 조작이 필요한 일련의 데스크톱 작업을 포함합니다.
- **실제 세계 실험**: 정밀한 공간 정보가 필요한 여러 조작 작업(예: 특정 위치의 객체 잡기, 순서대로 블록 쌓기)을 설계하고, 기준 방법(이전 최고 성능의 VLA 모델 포함)과 비교합니다.

### 주요 결과
- **Calvin ABC-D 벤치마크**: UP-VLA의 성공률은 이전 최고 방법 대비 33% 향상되어, 구체적으로 42.1%에서 56.0%로 증가했습니다.
- **실제 세계 작업**: 정밀한 공간 위치 파악이 필요한 작업에서 UP-VLA의 성공률은 평균 28% 향상되었으며, 의미론적 이해에만 의존하는 작업에서는 기준선과 성능이 동일했습니다.

### 결론
UP-VLA는 VLA 훈련에 미래 예측 목표를 도입하면 VLM의 저수준 공간 인식 부족을 효과적으로 보완할 수 있음을 입증하여, 로봇 조작 작업에 더 포괄적인 인식-행동 능력을 제공합니다. 이 연구는 고수준 의미론과 저수준 물리적 모델링의 균형을 어떻게 맞출지에 대한 후속 연구에 새로운 방향을 제시합니다.
