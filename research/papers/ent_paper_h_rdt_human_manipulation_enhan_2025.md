---
$id: ent_paper_h_rdt_human_manipulation_enhan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
  zh: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
  ko: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation'
summary:
  en: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
  zh: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
  ko: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation is a 2025 work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- h_rdt
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23523v2.
sources:
- id: src_001
  type: paper
  title: 'H-RDT: Human Manipulation Enhanced Bimanual Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2507.23523
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## 核心内容
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## 参考
- http://arxiv.org/abs/2507.23523v2

## Overview
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## Content
Imitation learning for robotic manipulation faces a fundamental challenge: the scarcity of large-scale, high-quality robot demonstration data. Recent robotic foundation models often pre-train on cross-embodiment robot datasets to increase data scale, while they face significant limitations as the diverse morphologies and action spaces across different robot embodiments make unified training challenging. In this paper, we present H-RDT (Human to Robotics Diffusion Transformer), a novel approach that leverages human manipulation data to enhance robot manipulation capabilities. Our key insight is that large-scale egocentric human manipulation videos with paired 3D hand pose annotations provide rich behavioral priors that capture natural manipulation strategies and can benefit robotic policy learning. We introduce a two-stage training paradigm: (1) pre-training on large-scale egocentric human manipulation data, and (2) cross-embodiment fine-tuning on robot-specific data with modular action encoders and decoders. Built on a diffusion transformer architecture with 2B parameters, H-RDT uses flow matching to model complex action distributions. Extensive evaluations encompassing both simulation and real-world experiments, single-task and multitask scenarios, as well as few-shot learning and robustness assessments, demonstrate that H-RDT outperforms training from scratch and existing state-of-the-art methods, including Pi0 and RDT, achieving significant improvements of 13.9% and 40.5% over training from scratch in simulation and real-world experiments, respectively. The results validate our core hypothesis that human manipulation data can serve as a powerful foundation for learning bimanual robotic manipulation policies.

## 개요
로봇 조작을 위한 모방 학습은 대규모 고품질 로봇 시연 데이터의 부족이라는 근본적인 과제에 직면해 있습니다. 최근 로봇 기반 모델들은 데이터 규모를 늘리기 위해 교차 체형 로봇 데이터셋으로 사전 학습을 수행하는 경우가 많지만, 다양한 로봇 체형과 행동 공간으로 인해 통합 학습이 어려워 상당한 한계를 보입니다. 본 논문에서는 인간 조작 데이터를 활용하여 로봇 조작 능력을 향상시키는 새로운 접근 방식인 H-RDT(Human to Robotics Diffusion Transformer)를 제시합니다. 우리의 핵심 통찰은 대규모 자기중심적 인간 조작 비디오와 쌍을 이루는 3D 손 자세 주석이 자연스러운 조작 전략을 포착하는 풍부한 행동 사전 정보를 제공하며, 로봇 정책 학습에 도움이 될 수 있다는 점입니다. 우리는 두 단계의 학습 패러다임을 도입합니다: (1) 대규모 자기중심적 인간 조작 데이터로 사전 학습, (2) 모듈식 행동 인코더와 디코더를 사용한 로봇 특화 데이터로의 교차 체형 미세 조정. 2B 파라미터의 확산 트랜스포머 아키텍처를 기반으로 구축된 H-RDT는 플로우 매칭을 사용하여 복잡한 행동 분포를 모델링합니다. 시뮬레이션 및 실제 실험, 단일 작업 및 다중 작업 시나리오, 퓨샷 학습 및 견고성 평가를 포함한 광범위한 평가를 통해 H-RDT가 처음부터 학습하는 방식과 Pi0 및 RDT를 포함한 기존 최첨단 방법보다 우수하며, 시뮬레이션 및 실제 실험에서 각각 13.9% 및 40.5%의 유의미한 개선을 달성함을 입증했습니다. 이러한 결과는 인간 조작 데이터가 양손 로봇 조작 정책 학습을 위한 강력한 기반이 될 수 있다는 핵심 가설을 검증합니다.

## 핵심 내용
로봇 조작을 위한 모방 학습은 대규모 고품질 로봇 시연 데이터의 부족이라는 근본적인 과제에 직면해 있습니다. 최근 로봇 기반 모델들은 데이터 규모를 늘리기 위해 교차 체형 로봇 데이터셋으로 사전 학습을 수행하는 경우가 많지만, 다양한 로봇 체형과 행동 공간으로 인해 통합 학습이 어려워 상당한 한계를 보입니다. 본 논문에서는 인간 조작 데이터를 활용하여 로봇 조작 능력을 향상시키는 새로운 접근 방식인 H-RDT(Human to Robotics Diffusion Transformer)를 제시합니다. 우리의 핵심 통찰은 대규모 자기중심적 인간 조작 비디오와 쌍을 이루는 3D 손 자세 주석이 자연스러운 조작 전략을 포착하는 풍부한 행동 사전 정보를 제공하며, 로봇 정책 학습에 도움이 될 수 있다는 점입니다. 우리는 두 단계의 학습 패러다임을 도입합니다: (1) 대규모 자기중심적 인간 조작 데이터로 사전 학습, (2) 모듈식 행동 인코더와 디코더를 사용한 로봇 특화 데이터로의 교차 체형 미세 조정. 2B 파라미터의 확산 트랜스포머 아키텍처를 기반으로 구축된 H-RDT는 플로우 매칭을 사용하여 복잡한 행동 분포를 모델링합니다. 시뮬레이션 및 실제 실험, 단일 작업 및 다중 작업 시나리오, 퓨샷 학습 및 견고성 평가를 포함한 광범위한 평가를 통해 H-RDT가 처음부터 학습하는 방식과 Pi0 및 RDT를 포함한 기존 최첨단 방법보다 우수하며, 시뮬레이션 및 실제 실험에서 각각 13.9% 및 40.5%의 유의미한 개선을 달성함을 입증했습니다. 이러한 결과는 인간 조작 데이터가 양손 로봇 조작 정책 학습을 위한 강력한 기반이 될 수 있다는 핵심 가설을 검증합니다.
