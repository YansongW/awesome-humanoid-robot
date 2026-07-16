---
$id: ent_paper_qu_spatialvla_exploring_spatial_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model'
  zh: SpatialVLA
  ko: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model'
summary:
  en: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (SpatialVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, ShanghaiTech, TeleAI.'
  zh: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (SpatialVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, ShanghaiTech, TeleAI.'
  ko: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (SpatialVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, ShanghaiTech, TeleAI.'
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
- spatialvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.15830v5.
sources:
- id: src_001
  type: paper
  title: 'SpatialVLA: Exploring Spatial Representations for Visual-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2501.15830
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SpatialVLA source
  url: https://doi.org/10.48550/arXiv.2501.15830
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control. SpatialVLA is first pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner. The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability. We further show the proposed Adaptive Action Grids offer a new and effective way to fine-tune the pre-trained SpatialVLA model for new simulation and real-world setups, where the pre-learned action grids are re-discretized to capture robot-specific spatial action movements of new setups. The superior results from extensive evaluations demonstrate the exceptional in-distribution generalization and out-of-distribution adaptation capability, highlighting the crucial benefit of the proposed spatial-aware representations for generalist robot policy learning. All the details and codes will be open-sourced.

## 核心内容
In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control. SpatialVLA is first pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner. The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability. We further show the proposed Adaptive Action Grids offer a new and effective way to fine-tune the pre-trained SpatialVLA model for new simulation and real-world setups, where the pre-learned action grids are re-discretized to capture robot-specific spatial action movements of new setups. The superior results from extensive evaluations demonstrate the exceptional in-distribution generalization and out-of-distribution adaptation capability, highlighting the crucial benefit of the proposed spatial-aware representations for generalist robot policy learning. All the details and codes will be open-sourced.

## 参考
- http://arxiv.org/abs/2501.15830v5

## Overview
In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control. SpatialVLA is first pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner. The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability. We further show the proposed Adaptive Action Grids offer a new and effective way to fine-tune the pre-trained SpatialVLA model for new simulation and real-world setups, where the pre-learned action grids are re-discretized to capture robot-specific spatial action movements of new setups. The superior results from extensive evaluations demonstrate the exceptional in-distribution generalization and out-of-distribution adaptation capability, highlighting the crucial benefit of the proposed spatial-aware representations for generalist robot policy learning. All the details and codes will be open-sourced.

## Content
In this paper, we claim that spatial understanding is the keypoint in robot manipulation, and propose SpatialVLA to explore effective spatial representations for the robot foundation model. Specifically, we introduce Ego3D Position Encoding to inject 3D information into the input observations of the visual-language-action model, and propose Adaptive Action Grids to represent spatial robot movement actions with adaptive discretized action grids, facilitating learning generalizable and transferrable spatial action knowledge for cross-robot control. SpatialVLA is first pre-trained on top of a vision-language model with 1.1 Million real-world robot episodes, to learn a generalist manipulation policy across multiple robot environments and tasks. After pre-training, SpatialVLA is directly applied to perform numerous tasks in a zero-shot manner. The superior results in both simulation and real-world robots demonstrate its advantage of inferring complex robot motion trajectories and its strong in-domain multi-task generalization ability. We further show the proposed Adaptive Action Grids offer a new and effective way to fine-tune the pre-trained SpatialVLA model for new simulation and real-world setups, where the pre-learned action grids are re-discretized to capture robot-specific spatial action movements of new setups. The superior results from extensive evaluations demonstrate the exceptional in-distribution generalization and out-of-distribution adaptation capability, highlighting the crucial benefit of the proposed spatial-aware representations for generalist robot policy learning. All the details and codes will be open-sourced.

## 개요
본 논문에서는 공간 이해가 로봇 조작의 핵심이라고 주장하며, 로봇 기초 모델을 위한 효과적인 공간 표현을 탐구하기 위해 SpatialVLA를 제안합니다. 구체적으로, Ego3D Position Encoding을 도입하여 시각-언어-행동 모델의 입력 관측값에 3D 정보를 주입하고, Adaptive Action Grids를 제안하여 적응형 이산화된 행동 그리드로 공간 로봇 움직임 행동을 표현함으로써, 로봇 간 제어를 위한 일반화 가능하고 전이 가능한 공간 행동 지식을 학습하는 것을 용이하게 합니다. SpatialVLA는 먼저 110만 개의 실제 로봇 에피소드를 사용하여 시각-언어 모델 위에서 사전 학습되어, 다양한 로봇 환경과 작업에 걸친 일반주의 조작 정책을 학습합니다. 사전 학습 후, SpatialVLA는 제로샷 방식으로 수많은 작업을 직접 수행합니다. 시뮬레이션과 실제 로봇 모두에서의 우수한 결과는 복잡한 로봇 움직임 궤적을 추론하는 장점과 강력한 도메인 내 다중 작업 일반화 능력을 입증합니다. 또한, 제안된 Adaptive Action Grids는 사전 학습된 SpatialVLA 모델을 새로운 시뮬레이션 및 실제 설정에 미세 조정하는 새롭고 효과적인 방법을 제공하며, 여기서 사전 학습된 행동 그리드는 새로운 설정의 로봇 특정 공간 행동 움직임을 포착하기 위해 재이산화됩니다. 광범위한 평가를 통한 우수한 결과는 탁월한 분포 내 일반화 및 분포 외 적응 능력을 보여주며, 일반주의 로봇 정책 학습을 위한 제안된 공간 인식 표현의 중요한 이점을 강조합니다. 모든 세부 사항과 코드는 오픈소스로 공개될 예정입니다.

## 핵심 내용
본 논문에서는 공간 이해가 로봇 조작의 핵심이라고 주장하며, 로봇 기초 모델을 위한 효과적인 공간 표현을 탐구하기 위해 SpatialVLA를 제안합니다. 구체적으로, Ego3D Position Encoding을 도입하여 시각-언어-행동 모델의 입력 관측값에 3D 정보를 주입하고, Adaptive Action Grids를 제안하여 적응형 이산화된 행동 그리드로 공간 로봇 움직임 행동을 표현함으로써, 로봇 간 제어를 위한 일반화 가능하고 전이 가능한 공간 행동 지식을 학습하는 것을 용이하게 합니다. SpatialVLA는 먼저 110만 개의 실제 로봇 에피소드를 사용하여 시각-언어 모델 위에서 사전 학습되어, 다양한 로봇 환경과 작업에 걸친 일반주의 조작 정책을 학습합니다. 사전 학습 후, SpatialVLA는 제로샷 방식으로 수많은 작업을 직접 수행합니다. 시뮬레이션과 실제 로봇 모두에서의 우수한 결과는 복잡한 로봇 움직임 궤적을 추론하는 장점과 강력한 도메인 내 다중 작업 일반화 능력을 입증합니다. 또한, 제안된 Adaptive Action Grids는 사전 학습된 SpatialVLA 모델을 새로운 시뮬레이션 및 실제 설정에 미세 조정하는 새롭고 효과적인 방법을 제공하며, 여기서 사전 학습된 행동 그리드는 새로운 설정의 로봇 특정 공간 행동 움직임을 포착하기 위해 재이산화됩니다. 광범위한 평가를 통한 우수한 결과는 탁월한 분포 내 일반화 및 분포 외 적응 능력을 보여주며, 일반주의 로봇 정책 학습을 위한 제안된 공간 인식 표현의 중요한 이점을 강조합니다. 모든 세부 사항과 코드는 오픈소스로 공개될 예정입니다.
