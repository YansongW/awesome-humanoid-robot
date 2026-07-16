---
$id: ent_paper_wen_tinyvla_towards_fast_data_effi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
  zh: TinyVLA
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation'
summary:
  en: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
  zh: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
  ko: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (TinyVLA), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Shanghai University, Syracuse University, Beijing
    Innovation Center of Humanoid Robotics, East China Normal University, Midea Group AI Lab.'
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
- tinyvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.12514v5.
sources:
- id: src_001
  type: paper
  title: 'TinyVLA: Towards Fast, Data-Efficient Vision-Language-Action Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TinyVLA source
  url: https://doi.org/10.48550/arXiv.2409.12514
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 核心内容
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 参考
- http://arxiv.org/abs/2409.12514v5

## Overview
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## Content
Vision-Language-Action (VLA) models have shown remarkable potential in visuomotor control and instruction comprehension through end-to-end learning processes. However, current VLA models face significant challenges: they are slow during inference and require extensive pre-training on large amounts of robotic data, making real-world deployment difficult. In this paper, we introduce a new family of compact vision-language-action models, called TinyVLA, which offers two key advantages over existing VLA models: (1) faster inference speeds, and (2) improved data efficiency, eliminating the need for pre-training stage. Our framework incorporates two essential components to build TinyVLA: (1) initializing the policy backbone with robust, high-speed multimodal models, and (2) integrating a diffusion policy decoder during fine-tuning to enable precise robot actions. We conducted extensive evaluations of TinyVLA in both simulation and on real robots, demonstrating that our approach significantly outperforms the state-of-the-art VLA model, OpenVLA, in terms of speed and data efficiency, while delivering comparable or superior performance. Additionally, TinyVLA exhibits strong generalization capabilities across various dimensions, including language instructions, novel objects, unseen positions, changes in object appearance, background variations, and environmental shifts, often matching or exceeding the performance of OpenVLA. We believe that \methodname offers an interesting perspective on utilizing pre-trained multimodal models for policy learning. Our project is at https://tiny-vla.github.io.

## 개요
Vision-Language-Action (VLA) 모델은 종단간 학습 과정을 통해 시각-운동 제어 및 명령 이해에서 놀라운 잠재력을 보여주었습니다. 그러나 현재의 VLA 모델은 추론 속도가 느리고 대량의 로봇 데이터에 대한 광범위한 사전 학습이 필요하여 실제 환경 배포가 어렵다는 심각한 문제에 직면해 있습니다. 본 논문에서는 TinyVLA라는 새로운 소형 비전-언어-행동 모델군을 소개합니다. 이 모델은 기존 VLA 모델에 비해 두 가지 주요 장점을 제공합니다: (1) 더 빠른 추론 속도, (2) 사전 학습 단계가 필요 없는 향상된 데이터 효율성입니다. 우리의 프레임워크는 TinyVLA 구축을 위해 두 가지 필수 구성 요소를 통합합니다: (1) 강력하고 고속의 멀티모달 모델로 정책 백본을 초기화하고, (2) 미세 조정 중 확산 정책 디코더를 통합하여 정밀한 로봇 동작을 가능하게 합니다. 우리는 시뮬레이션과 실제 로봇 모두에서 TinyVLA를 광범위하게 평가했으며, 우리의 접근 방식이 속도와 데이터 효율성 측면에서 최첨단 VLA 모델인 OpenVLA를 크게 능가하면서도 비슷하거나 더 뛰어난 성능을 제공함을 입증했습니다. 또한 TinyVLA는 언어 명령, 새로운 객체, 보지 못한 위치, 객체 외형 변화, 배경 변화 및 환경 변화를 포함한 다양한 차원에서 강력한 일반화 능력을 보여주며, 종종 OpenVLA의 성능과 일치하거나 이를 초과합니다. 우리는 \methodname이 사전 학습된 멀티모달 모델을 정책 학습에 활용하는 흥미로운 관점을 제공한다고 믿습니다. 프로젝트는 https://tiny-vla.github.io에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 종단간 학습 과정을 통해 시각-운동 제어 및 명령 이해에서 놀라운 잠재력을 보여주었습니다. 그러나 현재의 VLA 모델은 추론 속도가 느리고 대량의 로봇 데이터에 대한 광범위한 사전 학습이 필요하여 실제 환경 배포가 어렵다는 심각한 문제에 직면해 있습니다. 본 논문에서는 TinyVLA라는 새로운 소형 비전-언어-행동 모델군을 소개합니다. 이 모델은 기존 VLA 모델에 비해 두 가지 주요 장점을 제공합니다: (1) 더 빠른 추론 속도, (2) 사전 학습 단계가 필요 없는 향상된 데이터 효율성입니다. 우리의 프레임워크는 TinyVLA 구축을 위해 두 가지 필수 구성 요소를 통합합니다: (1) 강력하고 고속의 멀티모달 모델로 정책 백본을 초기화하고, (2) 미세 조정 중 확산 정책 디코더를 통합하여 정밀한 로봇 동작을 가능하게 합니다. 우리는 시뮬레이션과 실제 로봇 모두에서 TinyVLA를 광범위하게 평가했으며, 우리의 접근 방식이 속도와 데이터 효율성 측면에서 최첨단 VLA 모델인 OpenVLA를 크게 능가하면서도 비슷하거나 더 뛰어난 성능을 제공함을 입증했습니다. 또한 TinyVLA는 언어 명령, 새로운 객체, 보지 못한 위치, 객체 외형 변화, 배경 변화 및 환경 변화를 포함한 다양한 차원에서 강력한 일반화 능력을 보여주며, 종종 OpenVLA의 성능과 일치하거나 이를 초과합니다. 우리는 \methodname이 사전 학습된 멀티모달 모델을 정책 학습에 활용하는 흥미로운 관점을 제공한다고 믿습니다. 프로젝트는 https://tiny-vla.github.io에서 확인할 수 있습니다.
