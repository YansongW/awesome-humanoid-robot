---
$id: ent_paper_li_bridgevla_input_output_alignme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models'
  zh: BridgeVLA
  ko: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models'
summary:
  en: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
  zh: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
  ko: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (BridgeVLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by ByteDance Seed, School of Artificial
    Intelligence, University of Chinese Academy of Sciences, Institute of Automation, Chinese Academy of Sciences, FiveAges,
    Nanjing University, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridgevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.07961v2.
sources:
- id: src_001
  type: paper
  title: 'BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models (arXiv)'
  url: https://arxiv.org/abs/2506.07961
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: BridgeVLA source
  url: https://doi.org/10.48550/arXiv.2506.07961
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

## 核心内容
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website:https://bridgevla.github.io/

## 参考
- http://arxiv.org/abs/2506.07961v2

## Overview
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website: https://bridgevla.github.io/

## Content
Recently, leveraging pre-trained vision-language models (VLMs) for building vision-language-action (VLA) models has emerged as a promising approach to effective robot manipulation learning. However, only few methods incorporate 3D signals into VLMs for action prediction, and they do not fully leverage the spatial structure inherent in 3D data, leading to low sample efficiency. In this paper, we introduce BridgeVLA, a novel 3D VLA model that (1) projects 3D inputs to multiple 2D images, ensuring input alignment with the VLM backbone, and (2) utilizes 2D heatmaps for action prediction, unifying the input and output spaces within a consistent 2D image space. In addition, we propose a scalable pre-training method that equips the VLM backbone with the capability to predict 2D heatmaps before downstream policy learning. Extensive experiments show the proposed method is able to learn 3D manipulation efficiently and effectively. BridgeVLA outperforms state-of-the-art baseline methods across three simulation benchmarks. In RLBench, it improves the average success rate from 81.4% to 88.2%. In COLOSSEUM, it demonstrates significantly better performance in challenging generalization settings, boosting the average success rate from 56.7% to 64.0%. In GemBench, it surpasses all the comparing baseline methods in terms of average success rate. In real-robot experiments, BridgeVLA outperforms a state-of-the-art baseline method by 32% on average. It generalizes robustly in multiple out-of-distribution settings, including visual disturbances and unseen instructions. Remarkably, it is able to achieve a success rate of 96.8% on 10+ tasks with only 3 trajectories per task, highlighting its extraordinary sample efficiency. Project Website: https://bridgevla.github.io/

## 개요
최근 사전 훈련된 시각-언어 모델(VLM)을 활용하여 시각-언어-행동(VLA) 모델을 구축하는 것이 효과적인 로봇 조작 학습을 위한 유망한 접근 방식으로 부상하고 있습니다. 그러나 3D 신호를 VLM에 통합하여 행동을 예측하는 방법은 소수에 불과하며, 이들도 3D 데이터에 내재된 공간 구조를 완전히 활용하지 못하여 샘플 효율성이 낮습니다. 본 논문에서는 (1) 3D 입력을 여러 2D 이미지로 투영하여 VLM 백본과의 입력 정렬을 보장하고, (2) 2D 히트맵을 사용하여 행동을 예측함으로써 입력 및 출력 공간을 일관된 2D 이미지 공간으로 통합하는 새로운 3D VLA 모델인 BridgeVLA를 소개합니다. 또한, 다운스트림 정책 학습 전에 VLM 백본이 2D 히트맵을 예측할 수 있는 능력을 갖추도록 하는 확장 가능한 사전 훈련 방법을 제안합니다. 광범위한 실험을 통해 제안된 방법이 3D 조작을 효율적이고 효과적으로 학습할 수 있음을 보여줍니다. BridgeVLA는 세 가지 시뮬레이션 벤치마크에서 최첨단 기준 방법을 능가합니다. RLBench에서는 평균 성공률을 81.4%에서 88.2%로 향상시킵니다. COLOSSEUM에서는 까다로운 일반화 설정에서 현저히 더 나은 성능을 보여주며 평균 성공률을 56.7%에서 64.0%로 끌어올립니다. GemBench에서는 평균 성공률 측면에서 모든 비교 기준 방법을 능가합니다. 실제 로봇 실험에서 BridgeVLA는 최첨단 기준 방법보다 평균 32% 더 뛰어난 성능을 보입니다. 시각적 방해 요소 및 보지 못한 명령을 포함한 여러 분포 외 설정에서 강건하게 일반화됩니다. 놀랍게도, 작업당 3개의 궤적만으로 10개 이상의 작업에서 96.8%의 성공률을 달성하여 탁월한 샘플 효율성을 입증합니다. 프로젝트 웹사이트: https://bridgevla.github.io/

## 핵심 내용
최근 사전 훈련된 시각-언어 모델(VLM)을 활용하여 시각-언어-행동(VLA) 모델을 구축하는 것이 효과적인 로봇 조작 학습을 위한 유망한 접근 방식으로 부상하고 있습니다. 그러나 3D 신호를 VLM에 통합하여 행동을 예측하는 방법은 소수에 불과하며, 이들도 3D 데이터에 내재된 공간 구조를 완전히 활용하지 못하여 샘플 효율성이 낮습니다. 본 논문에서는 (1) 3D 입력을 여러 2D 이미지로 투영하여 VLM 백본과의 입력 정렬을 보장하고, (2) 2D 히트맵을 사용하여 행동을 예측함으로써 입력 및 출력 공간을 일관된 2D 이미지 공간으로 통합하는 새로운 3D VLA 모델인 BridgeVLA를 소개합니다. 또한, 다운스트림 정책 학습 전에 VLM 백본이 2D 히트맵을 예측할 수 있는 능력을 갖추도록 하는 확장 가능한 사전 훈련 방법을 제안합니다. 광범위한 실험을 통해 제안된 방법이 3D 조작을 효율적이고 효과적으로 학습할 수 있음을 보여줍니다. BridgeVLA는 세 가지 시뮬레이션 벤치마크에서 최첨단 기준 방법을 능가합니다. RLBench에서는 평균 성공률을 81.4%에서 88.2%로 향상시킵니다. COLOSSEUM에서는 까다로운 일반화 설정에서 현저히 더 나은 성능을 보여주며 평균 성공률을 56.7%에서 64.0%로 끌어올립니다. GemBench에서는 평균 성공률 측면에서 모든 비교 기준 방법을 능가합니다. 실제 로봇 실험에서 BridgeVLA는 최첨단 기준 방법보다 평균 32% 더 뛰어난 성능을 보입니다. 시각적 방해 요소 및 보지 못한 명령을 포함한 여러 분포 외 설정에서 강건하게 일반화됩니다. 놀랍게도, 작업당 3개의 궤적만으로 10개 이상의 작업에서 96.8%의 성공률을 달성하여 탁월한 샘플 효율성을 입증합니다. 프로젝트 웹사이트: https://bridgevla.github.io/
