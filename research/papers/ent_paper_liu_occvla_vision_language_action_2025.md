---
$id: ent_paper_liu_occvla_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision'
  zh: OccVLA
  ko: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision'
summary:
  en: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
  zh: OccVLA 是由上海期智研究院、西安交通大学、复旦大学、上海交通大学和清华大学联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于将隐式 3D 占用监督融入多模态推理，无需额外计算开销即可提升空间理解能力。该模型在
    nuScenes 基准的轨迹规划任务上达到最优，并在 3D 视觉问答中表现优异。
  ko: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
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
- occvla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05578v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (644 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (arXiv)'
  url: https://arxiv.org/abs/2509.05578
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OccVLA source
  url: https://doi.org/10.48550/arXiv.2509.05578
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
OccVLA 针对多模态大语言模型在自动驾驶中缺乏鲁棒 3D 空间理解的问题，提出了一种创新框架。它通过将密集 3D 占用同时作为预测输出和监督信号，使模型能从 2D 视觉输入直接学习精细空间结构，避免了昂贵的人工标注。在推理阶段，占用预测可作为隐式过程被跳过而不影响性能，从而不增加计算负担。实验表明，OccVLA 在 nuScenes 轨迹规划基准上取得领先结果，并在 3D 视觉问答任务中展现卓越能力，为自动驾驶提供了可扩展、可解释且完全基于视觉的解决方案。

## 核心内容
### 方法
- OccVLA 将 3D 占用表示整合到统一的多模态推理流程中，不同于依赖显式 3D 输入的先前方法。
- 模型将密集 3D 占用视为预测输出和监督信号，从 2D 视觉输入学习空间结构，无需手动标注。
- 占用预测作为隐式推理过程，可在推理时跳过，不增加额外计算开销。

### 架构
- 基于大型视觉-语言-动作模型架构，融合视觉、语言和动作模态。
- 通过隐式 3D 占用监督增强空间理解，保持端到端可训练性。

### 实验设置
- 在 nuScenes 基准上评估轨迹规划性能，并与现有方法对比。
- 在 3D 视觉问答任务上测试空间推理能力。

### 关键数字与结论
- 在 nuScenes 轨迹规划任务上达到 state-of-the-art 结果。
- 在 3D 视觉问答任务中表现优于基线模型。
- 无需额外计算开销，实现可扩展、可解释的自动驾驶解决方案。

## Overview
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## 参考
- http://arxiv.org/abs/2509.05578v1

## 개요
OccVLA는 자율주행에서 다중모달 대형 언어 모델의 견고한 3D 공간 이해 부족 문제를 해결하기 위해 혁신적인 프레임워크를 제안한다. 이는 밀집 3D 점유를 예측 출력이자 감독 신호로 동시에 활용하여, 모델이 2D 시각 입력만으로 정밀한 공간 구조를 직접 학습할 수 있게 하여 값비싼 수동 주석을 피한다. 추론 단계에서는 점유 예측을 암시적 과정으로 간주하여 성능에 영향을 주지 않고 건너뛸 수 있으므로 계산 부담이 증가하지 않는다. 실험 결과, OccVLA는 nuScenes 궤적 계획 벤치마크에서 선도적인 결과를 달성하고 3D 시각 질의응답 작업에서 뛰어난 능력을 보여주며, 자율주행을 위한 확장 가능하고 해석 가능하며 완전히 시각 기반의 솔루션을 제공한다.

## 핵심 내용
### 방법
- OccVLA는 명시적 3D 입력에 의존하는 이전 방법과 달리, 3D 점유 표현을 통합된 다중모달 추론 흐름에 통합한다.
- 모델은 밀집 3D 점유를 예측 출력이자 감독 신호로 간주하여, 수동 주석 없이 2D 시각 입력에서 공간 구조를 학습한다.
- 점유 예측은 암시적 추론 과정으로 작동하며, 추론 시 건너뛸 수 있어 추가 계산 오버헤드가 발생하지 않는다.

### 아키텍처
- 대규모 시각-언어-행동 모델 아키텍처를 기반으로, 시각, 언어, 행동 양식을 융합한다.
- 암시적 3D 점유 감독을 통해 공간 이해를 강화하면서도 종단 간 훈련 가능성을 유지한다.

### 실험 설정
- nuScenes 벤치마크에서 궤적 계획 성능을 평가하고 기존 방법과 비교한다.
- 3D 시각 질의응답 작업에서 공간 추론 능력을 테스트한다.

### 주요 수치 및 결론
- nuScenes 궤적 계획 작업에서 state-of-the-art 결과를 달성한다.
- 3D 시각 질의응답 작업에서 기준 모델보다 우수한 성능을 보인다.
- 추가 계산 오버헤드 없이 확장 가능하고 해석 가능한 자율주행 솔루션을 구현한다.
