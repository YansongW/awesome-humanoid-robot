---
$id: ent_paper_stemvlaan_open_source_vision_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  zh: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  ko: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
summary:
  en: 'arXiv:2602.23721v2 Announce Type: replace Abstract: Vision-language-action (VLA) models integrate visual observations
    and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However,
    most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly
    modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning
    and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework
    that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations
    into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric
    world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture
    temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer
    backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention
    module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D
    observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world
    understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average
    accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.'
  zh: 'arXiv:2602.23721v2 Announce Type: replace Abstract: Vision-language-action (VLA) models integrate visual observations
    and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However,
    most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly
    modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning
    and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework
    that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations
    into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric
    world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture
    temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer
    backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention
    module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D
    observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world
    understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average
    accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.'
  ko: 'arXiv:2602.23721v2 Announce Type: replace Abstract: Vision-language-action (VLA) models integrate visual observations
    and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However,
    most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly
    modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning
    and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework
    that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations
    into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric
    world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture
    temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer
    backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention
    module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D
    observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world
    understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average
    accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- stemvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23721v2.
sources:
- id: src_001
  type: paper
  title: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  url: https://arxiv.org/abs/2602.23721
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## 核心内容
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## 参考
- http://arxiv.org/abs/2602.23721v2

## Overview
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## Content
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## 개요
Vision-language-action (VLA) 모델은 시각적 관찰과 언어 명령을 통합하여 로봇의 행동을 예측하며, 조작 작업에서 유망한 일반화 능력을 보여줍니다. 그러나 기존 접근법 대부분은 주로 2D 시각적 입력에서 행동 시퀀스로의 직접적인 매핑에 의존하며, 기본적인 3D 공간 구조나 시간적 세계 역학을 명시적으로 모델링하지 않습니다. 이러한 표현은 동적 환경에서의 공간 추론과 장기적 의사 결정을 제한할 수 있습니다. 이러한 한계를 해결하기 위해, 우리는 미래 지향적 3D 공간 지식과 과거 4D 시공간 표현을 행동 예측에 명시적으로 통합하는 새로운 프레임워크인 StemVLA를 제안합니다. 첫째, 관찰된 이미지에만 의존하는 대신, StemVLA는 구조화된 3D 미래 공간-기하학적 세계 지식을 예측하여 모델이 다가올 장면 기하학과 객체 구성을 예측할 수 있도록 합니다. 둘째, 시간적 일관성과 운동 역학을 포착하기 위해, 과거 이미지 프레임을 사전 훈련된 비디오-기하학 트랜스포머 백본에 입력하여 암시적 3D 세계 표현을 추출하고, 이를 VideoFormer [20]라는 시간적 주의 모듈을 사용하여 시간에 걸쳐 집계하여 통합된 4D 과거 시공간 표현을 형성합니다. 2D 관찰, 예측된 3D 미래 구조, 집계된 4D 시간적 역학을 공동으로 모델링함으로써, StemVLA는 로봇 조작을 위한 보다 포괄적인 세계 이해를 가능하게 합니다. 시뮬레이션에서의 광범위한 실험을 통해 Stem-VLA는 LIBERO 하위 집합에서 평균 정확도 92.0%, 장기적 LIBERO-Long 하위 집합에서 86.0%를 달성함을 보여줍니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 시각적 관찰과 언어 명령을 통합하여 로봇의 행동을 예측하며, 조작 작업에서 유망한 일반화 능력을 보여줍니다. 그러나 기존 접근법 대부분은 주로 2D 시각적 입력에서 행동 시퀀스로의 직접적인 매핑에 의존하며, 기본적인 3D 공간 구조나 시간적 세계 역학을 명시적으로 모델링하지 않습니다. 이러한 표현은 동적 환경에서의 공간 추론과 장기적 의사 결정을 제한할 수 있습니다. 이러한 한계를 해결하기 위해, 우리는 미래 지향적 3D 공간 지식과 과거 4D 시공간 표현을 행동 예측에 명시적으로 통합하는 새로운 프레임워크인 StemVLA를 제안합니다. 첫째, 관찰된 이미지에만 의존하는 대신, StemVLA는 구조화된 3D 미래 공간-기하학적 세계 지식을 예측하여 모델이 다가올 장면 기하학과 객체 구성을 예측할 수 있도록 합니다. 둘째, 시간적 일관성과 운동 역학을 포착하기 위해, 과거 이미지 프레임을 사전 훈련된 비디오-기하학 트랜스포머 백본에 입력하여 암시적 3D 세계 표현을 추출하고, 이를 VideoFormer [20]라는 시간적 주의 모듈을 사용하여 시간에 걸쳐 집계하여 통합된 4D 과거 시공간 표현을 형성합니다. 2D 관찰, 예측된 3D 미래 구조, 집계된 4D 시간적 역학을 공동으로 모델링함으로써, StemVLA는 로봇 조작을 위한 보다 포괄적인 세계 이해를 가능하게 합니다. 시뮬레이션에서의 광범위한 실험을 통해 Stem-VLA는 LIBERO 하위 집합에서 평균 정확도 92.0%, 장기적 LIBERO-Long 하위 집합에서 86.0%를 달성함을 보여줍니다.
