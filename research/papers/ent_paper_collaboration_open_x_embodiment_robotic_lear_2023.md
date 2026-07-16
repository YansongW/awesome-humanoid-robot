---
$id: ent_paper_collaboration_open_x_embodiment_robotic_lear_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'
  zh: RT-X
  ko: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models'
summary:
  en: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models (RT-X), is a 2023 large vision-language-action model for
    robotic manipulation, introduced by Open X-Embodiment Collaboration, and published at ICRA 2023.'
  zh: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models (RT-X), is a 2023 large vision-language-action model for
    robotic manipulation, introduced by Open X-Embodiment Collaboration, and published at ICRA 2023.'
  ko: 'Open X-Embodiment: Robotic Learning Datasets and RT-X Models (RT-X), is a 2023 large vision-language-action model for
    robotic manipulation, introduced by Open X-Embodiment Collaboration, and published at ICRA 2023.'
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
- rt_x
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.08864v9.
sources:
- id: src_001
  type: website
  title: RT-X source
  url: https://doi.org/10.1109/ICRA57147.2024.10611477
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## 核心内容
Large, high-capacity models trained on diverse datasets have shown remarkable successes on efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## 参考
- http://arxiv.org/abs/2310.08864v9

## Overview
Large, high-capacity models trained on diverse datasets have shown remarkable successes in efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train a generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160,266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## Content
Large, high-capacity models trained on diverse datasets have shown remarkable successes in efficiently tackling downstream applications. In domains from NLP to Computer Vision, this has led to a consolidation of pretrained models, with general pretrained backbones serving as a starting point for many applications. Can such a consolidation happen in robotics? Conventionally, robotic learning methods train a separate model for every application, every robot, and even every environment. Can we instead train a generalist X-robot policy that can be adapted efficiently to new robots, tasks, and environments? In this paper, we provide datasets in standardized data formats and models to make it possible to explore this possibility in the context of robotic manipulation, alongside experimental results that provide an example of effective X-robot policies. We assemble a dataset from 22 different robots collected through a collaboration between 21 institutions, demonstrating 527 skills (160,266 tasks). We show that a high-capacity model trained on this data, which we call RT-X, exhibits positive transfer and improves the capabilities of multiple robots by leveraging experience from other platforms. More details can be found on the project website https://robotics-transformer-x.github.io.

## 개요
다양한 데이터셋으로 학습된 대규모 고용량 모델은 다운스트림 애플리케이션을 효율적으로 처리하는 데 놀라운 성공을 거두었습니다. NLP부터 컴퓨터 비전에 이르는 분야에서 이는 사전 학습된 모델의 통합으로 이어졌으며, 일반적인 사전 학습 백본이 많은 애플리케이션의 출발점 역할을 하고 있습니다. 이러한 통합이 로봇공학에서도 가능할까요? 전통적으로 로봇 학습 방법은 모든 애플리케이션, 모든 로봇, 심지어 모든 환경에 대해 별도의 모델을 학습시킵니다. 대신 새로운 로봇, 작업, 환경에 효율적으로 적응할 수 있는 제너럴리스트 X-로봇 정책을 학습시킬 수 있을까요? 본 논문에서는 로봇 조작 맥락에서 이러한 가능성을 탐구할 수 있도록 표준화된 데이터 형식의 데이터셋과 모델을 제공하며, 효과적인 X-로봇 정책의 예시를 보여주는 실험 결과를 함께 제시합니다. 우리는 21개 기관 간 협력을 통해 수집된 22개의 서로 다른 로봇으로 구성된 데이터셋을 구축하여 527개의 스킬(160266개의 작업)을 시연합니다. 이 데이터로 학습된 RT-X라고 불리는 고용량 모델이 긍정적 전이를 보이며 다른 플랫폼의 경험을 활용하여 여러 로봇의 능력을 향상시킨다는 것을 보여줍니다. 자세한 내용은 프로젝트 웹사이트 https://robotics-transformer-x.github.io에서 확인할 수 있습니다.

## 핵심 내용
다양한 데이터셋으로 학습된 대규모 고용량 모델은 다운스트림 애플리케이션을 효율적으로 처리하는 데 놀라운 성공을 거두었습니다. NLP부터 컴퓨터 비전에 이르는 분야에서 이는 사전 학습된 모델의 통합으로 이어졌으며, 일반적인 사전 학습 백본이 많은 애플리케이션의 출발점 역할을 하고 있습니다. 이러한 통합이 로봇공학에서도 가능할까요? 전통적으로 로봇 학습 방법은 모든 애플리케이션, 모든 로봇, 심지어 모든 환경에 대해 별도의 모델을 학습시킵니다. 대신 새로운 로봇, 작업, 환경에 효율적으로 적응할 수 있는 제너럴리스트 X-로봇 정책을 학습시킬 수 있을까요? 본 논문에서는 로봇 조작 맥락에서 이러한 가능성을 탐구할 수 있도록 표준화된 데이터 형식의 데이터셋과 모델을 제공하며, 효과적인 X-로봇 정책의 예시를 보여주는 실험 결과를 함께 제시합니다. 우리는 21개 기관 간 협력을 통해 수집된 22개의 서로 다른 로봇으로 구성된 데이터셋을 구축하여 527개의 스킬(160266개의 작업)을 시연합니다. 이 데이터로 학습된 RT-X라고 불리는 고용량 모델이 긍정적 전이를 보이며 다른 플랫폼의 경험을 활용하여 여러 로봇의 능력을 향상시킨다는 것을 보여줍니다. 자세한 내용은 프로젝트 웹사이트 https://robotics-transformer-x.github.io에서 확인할 수 있습니다.
