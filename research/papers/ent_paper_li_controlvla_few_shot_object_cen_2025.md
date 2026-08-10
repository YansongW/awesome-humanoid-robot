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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16211v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (768 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.16211v1

## 개요
ControlVLA는 실제 로봇 조작에서 시연 데이터가 부족한 문제를 해결하기 위해 설계되었습니다. 기존의 퓨샷 방법은 시뮬레이션 증강 데이터나 사전 구축 모듈에 의존하며, 시뮬레이션-현실 격차와 확장성 부족 문제가 있습니다. 이 프레임워크는 제로 초기화 투영 레이어를 통해 객체 중심 조건을 도입하여, 사전 학습 지식을 덮어쓰지 않으면서 새로운 작업에 점진적으로 적응합니다. 실험 결과, ControlVLA는 큐브 뒤집기, 옷 접기 등의 작업에서 단 10-20회의 시연만으로 76.7%의 성공률을 달성했으며, 기존 방법은 일반적으로 유사한 성능을 얻기 위해 100회 이상의 시연이 필요했습니다. 또한, 이 모델은 장기간 작업과 보지 못한 객체 및 배경에 대한 견고성도 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- ControlVLA는 ControlNet 스타일 아키텍처를 채택하여, 사전 학습된 VLA 모델에 제로 초기화 투영 레이어 세트를 도입합니다.
- 이 투영 레이어는 객체 중심 표현(예: 대상 객체의 위치, 자세 등)을 조건 입력으로 사용하여, 사전 학습된 조작 정책을 점진적으로 조정하며 기존 지식을 덮어쓰지 않습니다.
- 이러한 설계는 모델이 사전 학습 단계에서 얻은 일반적인 조작 능력을 유지하면서 새로운 작업에 효율적으로 적응할 수 있게 합니다.

### 실험 설정
- 큐브 뒤집기, 옷 접기 등 다양한 조작을 포함한 6가지 실제 세계 작업에서 평가되었습니다.
- 각 작업에는 훈련 데이터로 10-20회의 시연만 제공되며, 테스트 환경은 서로 다른 객체와 배경을 포함합니다.

### 주요 결과
- ControlVLA는 6가지 작업에서 평균 성공률 76.7%를 달성하여 기존 방법보다 크게 우수합니다.
- 기존 방법은 일반적으로 유사한 성공률을 얻기 위해 100회 이상의 시연이 필요하지만, ControlVLA는 10-20회만 필요합니다.
- 추가 실험은 ControlVLA가 장기간 작업(예: 다단계 조작)으로 확장될 수 있으며, 보지 못한 객체와 배경에 대한 견고성을 유지함을 보여줍니다.

### 결론
ControlVLA는 객체 중심 표현과 ControlNet 스타일 미세 조정을 통해 퓨샷 로봇 조작의 적응 문제를 효과적으로 해결하며, 데이터가 부족한 시나리오에서 사전 학습된 VLA 모델의 적용을 위한 실현 가능한 솔루션을 제공합니다.
