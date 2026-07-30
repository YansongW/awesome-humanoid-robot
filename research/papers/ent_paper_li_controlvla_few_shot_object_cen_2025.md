---
$id: ent_paper_li_controlvla_few_shot_object_cen_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models'
  zh: ControlVLA
  ko: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models'
summary:
  en: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (ControlVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, State Key Lab of General
    Artiﬁcial Intelligence, BIGAI, Peking University, Astribot, and published at CoRL25.'
  zh: ControlVLA 是由清华大学、北京大学等机构联合提出的 2025 年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过 ControlNet 风格的架构，将预训练 VLA 模型与以物体为中心的表示相结合，实现仅需 10-20
    次演示的少样本高效微调。在 6 项真实世界任务中，该方法取得了 76.7% 的成功率，远超传统方法。
  ko: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (ControlVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, State Key Lab of General
    Artiﬁcial Intelligence, BIGAI, Peking University, Astribot, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- controlvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16211v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.16211
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ControlVLA source
  url: https://doi.org/10.48550/arXiv.2506.16211
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ControlVLA 旨在解决真实世界机器人操作中演示数据稀缺的挑战。现有少样本方法依赖仿真增强数据或预构建模块，存在仿真到现实差距且扩展性不足。该框架通过零初始化的投影层引入以物体为中心的条件，在不覆盖预训练知识的前提下逐步适应新任务。实验表明，ControlVLA 在倒立方体、叠衣服等任务中仅需 10-20 次演示即可达到 76.7% 的成功率，而传统方法通常需要超过 100 次演示才能获得类似表现。此外，该模型还展现出对长时域任务和未见物体及背景的鲁棒性。

## 核心内容
### 方法架构
- ControlVLA 采用 ControlNet 风格架构，在预训练 VLA 模型基础上引入一组零初始化的投影层。
- 这些投影层负责将物体中心表示（如目标物体的位置、姿态等）作为条件输入，逐步调整预训练的操作策略，而不会覆盖原有知识。
- 这种设计使得模型能够高效适应新任务，同时保留预训练阶段获得的通用操作能力。

### 实验设置
- 在 6 项真实世界任务上进行评估，包括倒立方体、叠衣服等多样化操作。
- 每项任务仅提供 10-20 次演示作为训练数据，测试环境包含不同物体和背景。

### 关键结果
- ControlVLA 在 6 项任务中平均成功率达到 76.7%，显著优于传统方法。
- 传统方法通常需要超过 100 次演示才能达到类似成功率，而 ControlVLA 仅需 10-20 次。
- 额外实验表明，ControlVLA 能够扩展到长时域任务（如多步骤操作），并对未见物体和背景保持鲁棒性。

### 结论
ControlVLA 通过物体中心表示与 ControlNet 风格微调，有效解决了少样本机器人操作中的适应性问题，为预训练 VLA 模型在数据稀缺场景下的应用提供了可行方案。

## Overview
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## 개요
실제 세계의 로봇 조작 학습은 특히 제한된 시연 데이터만 제공될 때 어려운 과제입니다. 기존의 퓨샷 조작 방법은 종종 시뮬레이션 증강 데이터나 파지 및 자세 추정과 같은 사전 구축 모듈에 의존하지만, 이는 시뮬레이션-실제 간극 문제를 겪고 확장성이 부족합니다. 대규모 모방 사전 학습이 유망함에도 불구하고, 이러한 범용 정책을 데이터가 부족한 환경에서 특정 작업에 적용하는 방법은 아직 탐구되지 않았습니다. 이를 해결하기 위해, 우리는 ControlNet 스타일 아키텍처를 통해 사전 학습된 VLA 모델과 객체 중심 표현을 연결하여 효율적인 미세 조정을 가능하게 하는 새로운 프레임워크인 ControlVLA를 제안합니다. 구체적으로, 기존 지식을 덮어쓰지 않으면서 객체 중심 조건을 도입하기 위해 ControlVLA는 일련의 투영 레이어를 0으로 초기화하여 사전 학습된 조작 정책을 점진적으로 적응시킵니다. 큐브 따르기와 옷 접기를 포함한 6가지 다양한 작업에 걸친 실제 실험에서, 우리 방법은 10-20회의 시연만으로 76.7%의 성공률을 달성했습니다. 이는 유사한 성공률을 위해 100회 이상의 시연이 필요한 전통적인 접근 방식에 비해 큰 개선입니다. 추가 실험은 ControlVLA의 장기 작업에 대한 확장성과 보이지 않는 객체 및 배경에 대한 강건성을 강조합니다.

## 핵심 내용
실제 세계의 로봇 조작 학습은 특히 제한된 시연 데이터만 제공될 때 어려운 과제입니다. 기존의 퓨샷 조작 방법은 종종 시뮬레이션 증강 데이터나 파지 및 자세 추정과 같은 사전 구축 모듈에 의존하지만, 이는 시뮬레이션-실제 간극 문제를 겪고 확장성이 부족합니다. 대규모 모방 사전 학습이 유망함에도 불구하고, 이러한 범용 정책을 데이터가 부족한 환경에서 특정 작업에 적용하는 방법은 아직 탐구되지 않았습니다. 이를 해결하기 위해, 우리는 ControlNet 스타일 아키텍처를 통해 사전 학습된 VLA 모델과 객체 중심 표현을 연결하여 효율적인 미세 조정을 가능하게 하는 새로운 프레임워크인 ControlVLA를 제안합니다. 구체적으로, 기존 지식을 덮어쓰지 않으면서 객체 중심 조건을 도입하기 위해 ControlVLA는 일련의 투영 레이어를 0으로 초기화하여 사전 학습된 조작 정책을 점진적으로 적응시킵니다. 큐브 따르기와 옷 접기를 포함한 6가지 다양한 작업에 걸친 실제 실험에서, 우리 방법은 10-20회의 시연만으로 76.7%의 성공률을 달성했습니다. 이는 유사한 성공률을 위해 100회 이상의 시연이 필요한 전통적인 접근 방식에 비해 큰 개선입니다. 추가 실험은 ControlVLA의 장기 작업에 대한 확장성과 보이지 않는 객체 및 배경에 대한 강건성을 강조합니다.

## 参考
- http://arxiv.org/abs/2506.16211v1
