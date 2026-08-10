---
$id: ent_paper_lin_evo_1_lightweight_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment'
  zh: Evo-1
  ko: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment'
summary:
  en: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (Evo-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Imperial College London.'
  zh: Evo-1 是帝国理工学院于 2025 年提出的轻量级视觉-语言-动作模型，专为机器人操作任务设计。其核心贡献在于无需大规模机器人数据预训练，仅凭 7.7 亿参数便在 Meta-World 和 RoboTwin 基准上超越此前最佳模型
    12.4% 和 6.9%，并在 LIBERO 上达到 94.8% 的竞争性结果。该模型通过创新的交叉调制扩散变压器和两阶段训练范式，在降低计算成本的同时保持了视觉-语言骨干网络的语义对齐能力。
  ko: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (Evo-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Imperial College London.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- evo_1
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.04555v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (723 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (arXiv)'
  url: https://arxiv.org/abs/2511.04555
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Evo-1 source
  url: https://doi.org/10.48550/arXiv.2511.04555
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Evo-1 旨在解决当前 VLA 模型参数庞大、依赖大规模机器人数据预训练导致计算成本高、部署困难以及感知表征退化等问题。该模型基于原生多模态视觉-语言模型，引入交叉调制扩散变压器和优化集成模块，形成高效架构。其两阶段训练范式逐步对齐动作与感知，有效保留了 VLM 的语义表征。在真实世界评估中，Evo-1 以 78% 的成功率、高推理频率和低内存开销，全面超越基线方法。

## 核心内容
### 方法架构
Evo-1 构建于原生多模态视觉-语言模型之上，核心创新包括：
- **交叉调制扩散变压器**：一种新颖的模块，用于在视觉、语言和动作模态间进行高效信息交互。
- **优化集成模块**：将 VLM 的感知输出与动作生成无缝衔接，避免表征退化。

### 训练范式
采用两阶段训练策略：
1. **第一阶段**：在保持 VLM 语义对齐的前提下，初步对齐动作与感知。
2. **第二阶段**：进一步微调，强化动作生成与视觉-语言表征的协同，防止过拟合。

### 实验设置与关键数字
- **参数规模**：仅 0.77B（7.7 亿）参数，远低于同类模型。
- **基准测试**：
  - **Meta-World**：超越此前最佳模型 12.4%。
  - **RoboTwin**：提升 6.9%。
  - **LIBERO**：达到 94.8% 的竞争性结果。
- **真实世界评估**：在机器人操作任务中取得 78% 成功率，推理频率高且内存开销低。

### 结论
Evo-1 证明了轻量级 VLA 模型无需大规模机器人数据预训练即可实现顶尖性能，为高效、可部署的机器人学习提供了新方向。代码、数据和模型权重已开源。

## Overview
Vision-Language-Action (VLA) models have emerged as a powerful framework that unifies perception, language, and control, enabling robots to perform diverse tasks through multimodal understanding. However, current VLA models typically contain massive parameters and rely heavily on large-scale robot data pretraining, leading to high computational costs during training, as well as limited deployability for real-time inference. Moreover, most training paradigms often degrade the perceptual representations of the vision-language backbone, resulting in overfitting and poor generalization to downstream tasks. In this work, we present Evo-1, a lightweight VLA model that reduces computation and improves deployment efficiency, while maintaining strong performance without pretraining on robot data. Evo-1 builds on a native multimodal Vision-Language model (VLM), incorporating a novel cross-modulated diffusion transformer along with an optimized integration module, together forming an effective architecture. We further introduce a two-stage training paradigm that progressively aligns action with perception, preserving the representations of the VLM. Notably, with only 0.77 billion parameters, Evo-1 achieves state-of-the-art results on the Meta-World and RoboTwin suite, surpassing the previous best models by 12.4% and 6.9%, respectively, and also attains a competitive result of 94.8% on LIBERO. In real-world evaluations, Evo-1 attains a 78% success rate with high inference frequency and low memory overhead, outperforming all baseline methods. We release code, data, and model weights to facilitate future research on lightweight and efficient VLA models.

## 参考
- http://arxiv.org/abs/2511.04555v2

## 개요
Evo-1은 현재 VLA 모델의 방대한 파라미터 규모, 대규모 로봇 데이터 사전 학습에 따른 높은 계산 비용, 배포의 어려움, 그리고 지각 표현의 퇴화 문제를 해결하고자 설계되었습니다. 이 모델은 네이티브 멀티모달 비전-언어 모델을 기반으로, 교차 변조 확산 트랜스포머와 최적화 통합 모듈을 도입하여 효율적인 아키텍처를 구성합니다. 두 단계 훈련 패러다임은 동작과 지각을 점진적으로 정렬하여 VLM의 의미 표현을 효과적으로 보존합니다. 실제 세계 평가에서 Evo-1은 78%의 성공률, 높은 추론 빈도, 낮은 메모리 오버헤드로 기준 방법을 전반적으로 능가합니다.

## 핵심 내용
### 방법 아키텍처
Evo-1은 네이티브 멀티모달 비전-언어 모델 위에 구축되며, 핵심 혁신은 다음과 같습니다:
- **교차 변조 확산 트랜스포머**: 비전, 언어, 동작 모달리티 간의 효율적인 정보 상호작용을 위한 새로운 모듈.
- **최적화 통합 모듈**: VLM의 지각 출력과 동작 생성을 원활하게 연결하여 표현 퇴화를 방지합니다.

### 훈련 패러다임
두 단계 훈련 전략을 채택합니다:
1. **1단계**: VLM의 의미 정렬을 유지하면서 동작과 지각을 초기 정렬합니다.
2. **2단계**: 추가 미세 조정을 통해 동작 생성과 비전-언어 표현의 협력을 강화하고 과적합을 방지합니다.

### 실험 설정 및 주요 수치
- **파라미터 규모**: 단 0.77B(7.7억) 파라미터로, 유사 모델보다 훨씬 적습니다.
- **벤치마크 테스트**:
  - **Meta-World**: 이전 최고 모델보다 12.4% 향상.
  - **RoboTwin**: 6.9% 향상.
  - **LIBERO**: 94.8%의 경쟁력 있는 결과 달성.
- **실제 세계 평가**: 로봇 조작 작업에서 78% 성공률을 달성하며, 높은 추론 빈도와 낮은 메모리 오버헤드를 보여줍니다.

### 결론
Evo-1은 경량 VLA 모델이 대규모 로봇 데이터 사전 학습 없이도 최고 수준의 성능을 달성할 수 있음을 입증하며, 효율적이고 배포 가능한 로봇 학습의 새로운 방향을 제시합니다. 코드, 데이터, 모델 가중치는 오픈소스로 공개되었습니다.
