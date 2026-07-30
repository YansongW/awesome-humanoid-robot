---
$id: ent_paper_ye_learning_to_feel_the_future_dr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation'
  zh: DreamTacVLA
  ko: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation'
summary:
  en: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (DreamTacVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Northwestern University.'
  zh: DreamTacVLA 是西北大学于2025年提出的大型视觉-语言-动作模型，专为接触密集操作任务设计。其核心贡献在于通过分层感知架构和触觉世界模型，将触觉物理感知融入VLA模型，在接触密集操作任务中成功率最高达95%。
  ko: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (DreamTacVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Northwestern University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dreamtacvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23864v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.23864
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DreamTacVLA source
  url: https://doi.org/10.48550/arXiv.2512.23864
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型虽能利用网络知识实现泛化，但缺乏对物理接触的感知能力，难以处理需要推理力、纹理和滑移的接触密集操作。DreamTacVLA通过分层感知方案，将高分辨率触觉图像作为微视觉输入，与腕部局部视觉和第三人称宏观视觉协同工作。模型采用分层空间对齐损失统一多尺度感知流，并利用触觉世界模型预测未来触觉信号，从而深入理解接触动力学。为缓解触觉数据稀缺问题，研究团队构建了结合数字孪生和真实实验的混合大规模数据集。

## 核心内容
### 方法架构
- **分层感知方案**：将高分辨率触觉图像作为微视觉输入，与腕部局部视觉（local vision）和第三人称宏观视觉（macro vision）构成三级感知体系。
- **分层空间对齐损失（HSA loss）**：训练统一策略时，将触觉token与腕部及第三人称视角的空间对应token对齐，实现多尺度感知流融合。
- **触觉世界模型**：通过微调系统预测未来触觉信号，使模型能基于真实观测和想象后果共同决定动作，从而获得丰富的接触物理模型。

### 实验设置
- **数据集构建**：采用混合大规模数据集，包含高保真数字孪生（digital twin）数据和真实实验数据，以缓解触觉传感器数据稀缺和易磨损问题。
- **任务类型**：聚焦接触密集操作任务，如需要力、纹理和滑移推理的场景。

### 关键结果
- **性能对比**：在接触密集操作任务中，DreamTacVLA超越现有最先进VLA基线模型，成功率最高达95%。
- **核心结论**：理解物理接触对于构建鲁棒、具备触觉感知能力的机器人智能体至关重要。

## Overview
Vision-Language-Action (VLA) models have shown remarkable generalization by mapping web-scale knowledge to robotic control, yet they remain blind to physical contact. Consequently, they struggle with contact-rich manipulation tasks that require reasoning about force, texture, and slip. While some approaches incorporate low-dimensional tactile signals, they fail to capture the high-resolution dynamics essential for such interactions. To address this limitation, we introduce DreamTacVLA, a framework that grounds VLA models in contact physics by learning to feel the future. Our model adopts a hierarchical perception scheme in which high-resolution tactile images serve as micro-vision inputs coupled with wrist-camera local vision and third-person macro vision. To reconcile these multi-scale sensory streams, we first train a unified policy with a Hierarchical Spatial Alignment (HSA) loss that aligns tactile tokens with their spatial counterparts in the wrist and third-person views. To further deepen the model's understanding of fine-grained contact dynamics, we finetune the system with a tactile world model that predicts future tactile signals. To mitigate tactile data scarcity and the wear-prone nature of tactile sensors, we construct a hybrid large-scale dataset sourced from both high-fidelity digital twin and real-world experiments. By anticipating upcoming tactile states, DreamTacVLA acquires a rich model of contact physics and conditions its actions on both real observations and imagined consequences. Across contact-rich manipulation tasks, it outperforms state-of-the-art VLA baselines, achieving up to 95% success, highlighting the importance of understanding physical contact for robust, touch-aware robotic agents.

## 개요
Vision-Language-Action (VLA) 모델은 웹 규모의 지식을 로봇 제어에 매핑하여 놀라운 일반화 능력을 보여주었지만, 물리적 접촉에는 여전히 무지합니다. 결과적으로, 힘, 질감, 미끄러짐에 대한 추론이 필요한 접촉이 많은 조작 작업에 어려움을 겪습니다. 일부 접근 방식은 저차원 촉각 신호를 통합하지만, 이러한 상호작용에 필수적인 고해상도 동역학을 포착하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 미래를 느끼는 학습을 통해 VLA 모델을 접촉 물리학에 기반하는 프레임워크인 DreamTacVLA를 소개합니다. 우리 모델은 고해상도 촉각 이미지를 손목 카메라의 로컬 비전 및 3인칭 매크로 비전과 결합된 마이크로 비전 입력으로 사용하는 계층적 인식 방식을 채택합니다. 이러한 다중 스케일 감각 스트림을 조화시키기 위해, 먼저 촉각 토큰을 손목 및 3인칭 뷰의 공간적 대응물과 정렬하는 계층적 공간 정렬(HSA) 손실로 통합 정책을 훈련합니다. 미세한 접촉 동역학에 대한 모델의 이해를 더욱 심화하기 위해, 미래 촉각 신호를 예측하는 촉각 세계 모델로 시스템을 미세 조정합니다. 촉각 데이터 부족과 촉각 센서의 마모 특성을 완화하기 위해, 고충실도 디지털 트윈과 실제 실험에서 얻은 하이브리드 대규모 데이터셋을 구축합니다. 다가오는 촉각 상태를 예측함으로써, DreamTacVLA는 풍부한 접촉 물리학 모델을 획득하고 실제 관찰과 상상된 결과 모두에 따라 행동을 조건화합니다. 접촉이 많은 조작 작업에서 최첨단 VLA 기준선을 능가하며 최대 95%의 성공률을 달성하여, 강건하고 촉각 인식이 가능한 로봇 에이전트를 위한 물리적 접촉 이해의 중요성을 강조합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 웹 규모의 지식을 로봇 제어에 매핑하여 놀라운 일반화 능력을 보여주었지만, 물리적 접촉에는 여전히 무지합니다. 결과적으로, 힘, 질감, 미끄러짐에 대한 추론이 필요한 접촉이 많은 조작 작업에 어려움을 겪습니다. 일부 접근 방식은 저차원 촉각 신호를 통합하지만, 이러한 상호작용에 필수적인 고해상도 동역학을 포착하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 미래를 느끼는 학습을 통해 VLA 모델을 접촉 물리학에 기반하는 프레임워크인 DreamTacVLA를 소개합니다. 우리 모델은 고해상도 촉각 이미지를 손목 카메라의 로컬 비전 및 3인칭 매크로 비전과 결합된 마이크로 비전 입력으로 사용하는 계층적 인식 방식을 채택합니다. 이러한 다중 스케일 감각 스트림을 조화시키기 위해, 먼저 촉각 토큰을 손목 및 3인칭 뷰의 공간적 대응물과 정렬하는 계층적 공간 정렬(HSA) 손실로 통합 정책을 훈련합니다. 미세한 접촉 동역학에 대한 모델의 이해를 더욱 심화하기 위해, 미래 촉각 신호를 예측하는 촉각 세계 모델로 시스템을 미세 조정합니다. 촉각 데이터 부족과 촉각 센서의 마모 특성을 완화하기 위해, 고충실도 디지털 트윈과 실제 실험에서 얻은 하이브리드 대규모 데이터셋을 구축합니다. 다가오는 촉각 상태를 예측함으로써, DreamTacVLA는 풍부한 접촉 물리학 모델을 획득하고 실제 관찰과 상상된 결과 모두에 따라 행동을 조건화합니다. 접촉이 많은 조작 작업에서 최첨단 VLA 기준선을 능가하며 최대 95%의 성공률을 달성하여, 강건하고 촉각 인식이 가능한 로봇 에이전트를 위한 물리적 접촉 이해의 중요성을 강조합니다.

## 参考
- http://arxiv.org/abs/2512.23864v4
