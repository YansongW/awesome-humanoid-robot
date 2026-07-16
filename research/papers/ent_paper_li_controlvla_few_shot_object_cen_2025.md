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
  zh: 'ControlVLA: Few-shot Object-centric Adaptation for Pre-trained Vision-Language-Action Models (ControlVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Tsinghua University, State Key Lab of General
    Artiﬁcial Intelligence, BIGAI, Peking University, Astribot, and published at CoRL25.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.16211v1.
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
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## 核心内容
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## 参考
- http://arxiv.org/abs/2506.16211v1

## Overview
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## Content
Learning real-world robotic manipulation is challenging, particularly when limited demonstrations are available. Existing methods for few-shot manipulation often rely on simulation-augmented data or pre-built modules like grasping and pose estimation, which struggle with sim-to-real gaps and lack extensibility. While large-scale imitation pre-training shows promise, adapting these general-purpose policies to specific tasks in data-scarce settings remains unexplored. To achieve this, we propose ControlVLA, a novel framework that bridges pre-trained VLA models with object-centric representations via a ControlNet-style architecture for efficient fine-tuning. Specifically, to introduce object-centric conditions without overwriting prior knowledge, ControlVLA zero-initializes a set of projection layers, allowing them to gradually adapt the pre-trained manipulation policies. In real-world experiments across 6 diverse tasks, including pouring cubes and folding clothes, our method achieves a 76.7% success rate while requiring only 10-20 demonstrations -- a significant improvement over traditional approaches that require more than 100 demonstrations to achieve comparable success. Additional experiments highlight ControlVLA's extensibility to long-horizon tasks and robustness to unseen objects and backgrounds.

## 개요
실제 세계의 로봇 조작 학습은 특히 제한된 시연 데이터만 제공될 때 어려운 과제입니다. 기존의 퓨샷 조작 방법은 종종 시뮬레이션 증강 데이터나 파지 및 자세 추정과 같은 사전 구축 모듈에 의존하지만, 이는 시뮬레이션-실제 간극 문제를 겪고 확장성이 부족합니다. 대규모 모방 사전 학습이 유망함에도 불구하고, 이러한 범용 정책을 데이터가 부족한 환경에서 특정 작업에 적용하는 방법은 아직 탐구되지 않았습니다. 이를 해결하기 위해, 우리는 ControlNet 스타일 아키텍처를 통해 사전 학습된 VLA 모델과 객체 중심 표현을 연결하여 효율적인 미세 조정을 가능하게 하는 새로운 프레임워크인 ControlVLA를 제안합니다. 구체적으로, 기존 지식을 덮어쓰지 않으면서 객체 중심 조건을 도입하기 위해 ControlVLA는 일련의 투영 레이어를 0으로 초기화하여 사전 학습된 조작 정책을 점진적으로 적응시킵니다. 큐브 따르기와 옷 접기를 포함한 6가지 다양한 작업에 걸친 실제 실험에서, 우리 방법은 10-20회의 시연만으로 76.7%의 성공률을 달성했습니다. 이는 유사한 성공률을 위해 100회 이상의 시연이 필요한 전통적인 접근 방식에 비해 큰 개선입니다. 추가 실험은 ControlVLA의 장기 작업에 대한 확장성과 보이지 않는 객체 및 배경에 대한 강건성을 강조합니다.

## 핵심 내용
실제 세계의 로봇 조작 학습은 특히 제한된 시연 데이터만 제공될 때 어려운 과제입니다. 기존의 퓨샷 조작 방법은 종종 시뮬레이션 증강 데이터나 파지 및 자세 추정과 같은 사전 구축 모듈에 의존하지만, 이는 시뮬레이션-실제 간극 문제를 겪고 확장성이 부족합니다. 대규모 모방 사전 학습이 유망함에도 불구하고, 이러한 범용 정책을 데이터가 부족한 환경에서 특정 작업에 적용하는 방법은 아직 탐구되지 않았습니다. 이를 해결하기 위해, 우리는 ControlNet 스타일 아키텍처를 통해 사전 학습된 VLA 모델과 객체 중심 표현을 연결하여 효율적인 미세 조정을 가능하게 하는 새로운 프레임워크인 ControlVLA를 제안합니다. 구체적으로, 기존 지식을 덮어쓰지 않으면서 객체 중심 조건을 도입하기 위해 ControlVLA는 일련의 투영 레이어를 0으로 초기화하여 사전 학습된 조작 정책을 점진적으로 적응시킵니다. 큐브 따르기와 옷 접기를 포함한 6가지 다양한 작업에 걸친 실제 실험에서, 우리 방법은 10-20회의 시연만으로 76.7%의 성공률을 달성했습니다. 이는 유사한 성공률을 위해 100회 이상의 시연이 필요한 전통적인 접근 방식에 비해 큰 개선입니다. 추가 실험은 ControlVLA의 장기 작업에 대한 확장성과 보이지 않는 객체 및 배경에 대한 강건성을 강조합니다.
