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
  zh: StemVLA 是一个开源的视觉-语言-动作（VLA）模型，由研究团队提出，旨在通过显式引入未来3D空间几何知识与历史4D时空表征来提升机器人操作任务的性能。其核心贡献在于预测未来场景的3D结构，并利用VideoFormer模块聚合历史帧的4D动态信息，在LIBERO基准上达到92.0%的平均准确率，长时域子集上为86.0%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23721v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (825 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  url: https://arxiv.org/abs/2602.23721
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型多依赖2D视觉到动作的直接映射，缺乏对3D空间结构与时间动态的显式建模，限制了动态环境中的空间推理与长时域决策。StemVLA通过两个关键创新解决此问题：一是预测未来3D空间几何知识，使模型能预判场景几何与物体配置；二是利用预训练的视频几何Transformer骨干提取历史帧的隐式3D表征，并通过VideoFormer模块进行时间聚合，形成统一的4D历史时空表征。该框架联合建模2D观测、预测的3D未来结构与聚合的4D时间动态，从而增强机器人操作中的世界理解能力。

## 核心内容
### 方法架构
StemVLA 的核心框架包含三个主要组件：
- **未来3D空间几何知识预测**：模型不依赖当前观测图像，而是预测结构化的未来3D空间几何世界知识，从而预判即将发生的场景几何与物体配置变化。
- **历史4D时空表征提取**：将历史图像帧输入预训练的视频几何Transformer骨干（VideoFormer），提取隐式3D世界表征，并通过时间注意力模块（VideoFormer [20]）跨时间聚合，形成统一的4D历史时空表征。
- **联合建模**：同时处理2D观测、预测的3D未来结构以及聚合的4D时间动态，实现更全面的世界理解。

### 实验设置与关键结果
- **基准测试**：在LIBERO模拟环境中的多个子集上进行评估。
- **性能数据**：
  - 平均准确率：在所有LIBERO子集上达到92.0%。
  - 长时域任务：在LIBERO-Long子集上达到86.0%，验证了模型在长时域决策中的有效性。
- **对比基线**：通过显式建模3D空间与4D时间信息，StemVLA优于仅依赖2D视觉输入的现有方法。

### 结论
StemVLA 通过引入未来3D空间几何知识与历史4D时空表征，显著提升了VLA模型在动态环境中的空间推理与长时域操作能力，开源框架为机器人操作领域提供了新的研究方向。

## Overview
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## 参考
- http://arxiv.org/abs/2602.23721v2

## 개요
기존 VLA 모델은 대부분 2D 비전에서 동작으로의 직접 매핑에 의존하며, 3D 공간 구조와 시간적 역학에 대한 명시적 모델링이 부족하여 동적 환경에서의 공간 추론과 장기적 의사 결정이 제한됩니다. StemVLA는 두 가지 핵심 혁신을 통해 이 문제를 해결합니다: 첫째, 미래 3D 공간 기하학 지식을 예측하여 모델이 장면 기하학과 객체 구성을 사전에 파악할 수 있게 합니다; 둘째, 사전 훈련된 비디오 기하학 Transformer 백본을 활용하여 과거 프레임의 암시적 3D 표현을 추출하고, VideoFormer 모듈을 통해 시간적 집계를 수행하여 통합된 4D 과거-현재 시공간 표현을 형성합니다. 이 프레임워크는 2D 관측, 예측된 3D 미래 구조, 집계된 4D 시간적 역학을 공동으로 모델링하여 로봇 조작에서의 세계 이해 능력을 강화합니다.

## 핵심 내용
### 방법 아키텍처
StemVLA의 핵심 프레임워크는 세 가지 주요 구성 요소를 포함합니다:
- **미래 3D 공간 기하학 지식 예측**: 모델은 현재 관측 이미지에 의존하지 않고 구조화된 미래 3D 공간 기하학 세계 지식을 예측하여 다가올 장면 기하학과 객체 구성 변화를 사전에 파악합니다.
- **과거 4D 시공간 표현 추출**: 과거 이미지 프레임을 사전 훈련된 비디오 기하학 Transformer 백본(VideoFormer)에 입력하여 암시적 3D 세계 표현을 추출하고, 시간적 주의 모듈(VideoFormer [20])을 통해 시간에 걸쳐 집계하여 통합된 4D 과거-현재 시공간 표현을 형성합니다.
- **공동 모델링**: 2D 관측, 예측된 3D 미래 구조, 집계된 4D 시간적 역학을 동시에 처리하여 더 포괄적인 세계 이해를 달성합니다.

### 실험 설정 및 주요 결과
- **벤치마크**: LIBERO 시뮬레이션 환경의 여러 하위 집합에서 평가를 수행합니다.
- **성능 데이터**:
  - 평균 정확도: 모든 LIBERO 하위 집합에서 92.0% 달성.
  - 장기적 작업: LIBERO-Long 하위 집합에서 86.0% 달성, 장기적 의사 결정에서 모델의 효과성을 검증.
- **비교 기준선**: 3D 공간 및 4D 시간 정보를 명시적으로 모델링함으로써 StemVLA는 2D 비전 입력에만 의존하는 기존 방법보다 우수합니다.

### 결론
StemVLA는 미래 3D 공간 기하학 지식과 과거 4D 시공간 표현을 도입하여 동적 환경에서 VLA 모델의 공간 추론 및 장기적 조작 능력을 크게 향상시켰으며, 오픈소스 프레임워크는 로봇 조작 분야에 새로운 연구 방향을 제시합니다.
