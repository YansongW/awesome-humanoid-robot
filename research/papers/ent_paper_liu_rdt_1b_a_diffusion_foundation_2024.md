---
$id: ent_paper_liu_rdt_1b_a_diffusion_foundation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'
  zh: RDT-1B
  ko: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'
summary:
  en: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (RDT-1B), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at ICLR 2024.'
  zh: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (RDT-1B), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at ICLR 2024.'
  ko: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (RDT-1B), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at ICLR 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- rdt_1b
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.07864v2.
sources:
- id: src_001
  type: paper
  title: RDT-1B source
  url: https://openreview.net/forum?id=yAzN4tz7oI
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over 6K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1~5 demonstrations, and effectively handles complex, dexterous tasks. We refer to https://rdt-robotics.github.io/rdt-robotics/ for the code and videos.

## 核心内容
Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over 6K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1~5 demonstrations, and effectively handles complex, dexterous tasks. We refer to https://rdt-robotics.github.io/rdt-robotics/ for the code and videos.

## 参考
- http://arxiv.org/abs/2410.07864v2

## Overview
Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over 6K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1~5 demonstrations, and effectively handles complex, dexterous tasks. We refer to https://rdt-robotics.github.io/rdt-robotics/ for the code and videos.

## Content
Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over 6K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1~5 demonstrations, and effectively handles complex, dexterous tasks. We refer to https://rdt-robotics.github.io/rdt-robotics/ for the code and videos.

## 개요
이매뉴얼 조작은 로봇 공학에서 필수적이지만, 두 로봇 팔을 조정하는 본질적인 복잡성(다중 모드 동작 분포 초래)과 훈련 데이터 부족으로 인해 기초 모델 개발은 매우 어렵습니다. 본 논문에서는 이매뉴얼 조작을 위한 선구적인 확산 기초 모델인 Robotics Diffusion Transformer(RDT)를 제시합니다. RDT는 확산 모델을 기반으로 다중 모드를 효과적으로 표현하며, 확장 가능한 Transformer의 혁신적인 설계를 통해 다중 모드 입력의 이질성을 처리하고 로봇 데이터의 비선형성과 고주파 특성을 포착합니다. 데이터 부족 문제를 해결하기 위해, 우리는 물리적으로 해석 가능한 통합 동작 공간(Physically Interpretable Unified Action Space)을 추가로 도입합니다. 이는 다양한 로봇의 동작 표현을 통합하면서 원래 동작의 물리적 의미를 보존하여 전이 가능한 물리적 지식 학습을 촉진합니다. 이러한 설계를 통해 우리는 현재까지 가장 큰 멀티 로봇 데이터셋 모음에서 RDT를 사전 훈련하고 12억 개의 파라미터로 확장하여, 로봇 조작을 위한 가장 큰 확산 기반 기초 모델을 구축했습니다. 마지막으로, 6000개 이상의 에피소드를 포함하는 자체 제작 멀티태스크 이매뉴얼 데이터셋에서 RDT를 미세 조정하여 조작 능력을 개선했습니다. 실제 로봇 실험을 통해 RDT가 기존 방법을 크게 능가함을 입증했습니다. 이는 보지 못한 물체와 장면에 대한 제로샷 일반화, 언어 명령 이해 및 따르기, 단 1~5개의 시연으로 새로운 기술 학습, 복잡하고 정교한 작업의 효과적 처리를 보여줍니다. 코드와 비디오는 https://rdt-robotics.github.io/rdt-robotics/ 를 참조하십시오.

## 핵심 내용
이매뉴얼 조작은 로봇 공학에서 필수적이지만, 두 로봇 팔을 조정하는 본질적인 복잡성(다중 모드 동작 분포 초래)과 훈련 데이터 부족으로 인해 기초 모델 개발은 매우 어렵습니다. 본 논문에서는 이매뉴얼 조작을 위한 선구적인 확산 기초 모델인 Robotics Diffusion Transformer(RDT)를 제시합니다. RDT는 확산 모델을 기반으로 다중 모드를 효과적으로 표현하며, 확장 가능한 Transformer의 혁신적인 설계를 통해 다중 모드 입력의 이질성을 처리하고 로봇 데이터의 비선형성과 고주파 특성을 포착합니다. 데이터 부족 문제를 해결하기 위해, 우리는 물리적으로 해석 가능한 통합 동작 공간(Physically Interpretable Unified Action Space)을 추가로 도입합니다. 이는 다양한 로봇의 동작 표현을 통합하면서 원래 동작의 물리적 의미를 보존하여 전이 가능한 물리적 지식 학습을 촉진합니다. 이러한 설계를 통해 우리는 현재까지 가장 큰 멀티 로봇 데이터셋 모음에서 RDT를 사전 훈련하고 12억 개의 파라미터로 확장하여, 로봇 조작을 위한 가장 큰 확산 기반 기초 모델을 구축했습니다. 마지막으로, 6000개 이상의 에피소드를 포함하는 자체 제작 멀티태스크 이매뉴얼 데이터셋에서 RDT를 미세 조정하여 조작 능력을 개선했습니다. 실제 로봇 실험을 통해 RDT가 기존 방법을 크게 능가함을 입증했습니다. 이는 보지 못한 물체와 장면에 대한 제로샷 일반화, 언어 명령 이해 및 따르기, 단 1~5개의 시연으로 새로운 기술 학습, 복잡하고 정교한 작업의 효과적 처리를 보여줍니다. 코드와 비디오는 https://rdt-robotics.github.io/rdt-robotics/ 를 참조하십시오.
