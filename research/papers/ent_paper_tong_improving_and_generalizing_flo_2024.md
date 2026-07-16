---
$id: ent_paper_tong_improving_and_generalizing_flo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport
  zh: 基于小批量最优传输的流式生成模型改进与泛化
  ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
summary:
  en: This paper introduces generalized conditional flow matching (CFM), a simulation-free regression objective for training
    continuous normalizing flows (CNFs), and proposes optimal transport CFM (OT-CFM), which uses minibatch optimal transport
    couplings to produce straighter flows and faster inference.
  zh: 本文提出了广义条件流匹配（CFM），一种用于训练连续归一化流的免模拟回归目标，并引入了最优传输条件流匹配（OT-CFM），利用小批量最优传输耦合生成更直的流并实现更快的推理。
  ko: 본 논문은 연속 정규화 흐름(CNF)을 학습하기 위한 시뮬레이션 없는 회귀 목적함수인 일반화된 조건부 플로우 매칭(CFM)을 제안하고, 미니배치 최적 수송 결합을 사용하여 더 직선적인 플로우와 더 빠른 추론을
    가능하게 하는 최적 수송 조건부 플로우 매칭(OT-CFM)을 제시한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flow_matching
- optimal_transport
- continuous_normalizing_flow
- generative_model
- diffusion_model
- world_model
- synthetic_data
- motion_generation
- minibatch_optimal_transport
- torchcfm
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.00482v4.
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
Continuous normalizing flows (CNFs) are an attractive generative modeling technique, but they have been held back by limitations in their simulation-based maximum likelihood training. We introduce the generalized conditional flow matching (CFM) technique, a family of simulation-free training objectives for CNFs. CFM features a stable regression objective like that used to train the stochastic flow in diffusion models but enjoys the efficient inference of deterministic flow models. In contrast to both diffusion models and prior CNF training algorithms, CFM does not require the source distribution to be Gaussian or require evaluation of its density. A variant of our objective is optimal transport CFM (OT-CFM), which creates simpler flows that are more stable to train and lead to faster inference, as evaluated in our experiments. Furthermore, we show that when the true OT plan is available, our OT-CFM method approximates dynamic OT. Training CNFs with CFM improves results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrödinger bridge inference.

## 核心内容
Continuous normalizing flows (CNFs) are an attractive generative modeling technique, but they have been held back by limitations in their simulation-based maximum likelihood training. We introduce the generalized conditional flow matching (CFM) technique, a family of simulation-free training objectives for CNFs. CFM features a stable regression objective like that used to train the stochastic flow in diffusion models but enjoys the efficient inference of deterministic flow models. In contrast to both diffusion models and prior CNF training algorithms, CFM does not require the source distribution to be Gaussian or require evaluation of its density. A variant of our objective is optimal transport CFM (OT-CFM), which creates simpler flows that are more stable to train and lead to faster inference, as evaluated in our experiments. Furthermore, we show that when the true OT plan is available, our OT-CFM method approximates dynamic OT. Training CNFs with CFM improves results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrödinger bridge inference.

## 参考
- http://arxiv.org/abs/2302.00482v4

## Overview
Continuous normalizing flows (CNFs) are an attractive generative modeling technique, but they have been held back by limitations in their simulation-based maximum likelihood training. We introduce the generalized conditional flow matching (CFM) technique, a family of simulation-free training objectives for CNFs. CFM features a stable regression objective like that used to train the stochastic flow in diffusion models but enjoys the efficient inference of deterministic flow models. In contrast to both diffusion models and prior CNF training algorithms, CFM does not require the source distribution to be Gaussian or require evaluation of its density. A variant of our objective is optimal transport CFM (OT-CFM), which creates simpler flows that are more stable to train and lead to faster inference, as evaluated in our experiments. Furthermore, we show that when the true OT plan is available, our OT-CFM method approximates dynamic OT. Training CNFs with CFM improves results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrödinger bridge inference.

## Content
Continuous normalizing flows (CNFs) are an attractive generative modeling technique, but they have been held back by limitations in their simulation-based maximum likelihood training. We introduce the generalized conditional flow matching (CFM) technique, a family of simulation-free training objectives for CNFs. CFM features a stable regression objective like that used to train the stochastic flow in diffusion models but enjoys the efficient inference of deterministic flow models. In contrast to both diffusion models and prior CNF training algorithms, CFM does not require the source distribution to be Gaussian or require evaluation of its density. A variant of our objective is optimal transport CFM (OT-CFM), which creates simpler flows that are more stable to train and lead to faster inference, as evaluated in our experiments. Furthermore, we show that when the true OT plan is available, our OT-CFM method approximates dynamic OT. Training CNFs with CFM improves results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrödinger bridge inference.

## 개요
연속 정규화 흐름(CNF)은 매력적인 생성 모델링 기법이지만, 시뮬레이션 기반 최대 우도 훈련의 한계로 인해 제약을 받아왔습니다. 우리는 CNF를 위한 시뮬레이션 없는 훈련 목적 함수군인 일반화된 조건부 흐름 매칭(CFM) 기법을 소개합니다. CFM은 확산 모델에서 확률적 흐름을 훈련하는 데 사용되는 안정적인 회귀 목적 함수를 특징으로 하면서도 결정적 흐름 모델의 효율적인 추론을 누릴 수 있습니다. 확산 모델 및 기존 CNF 훈련 알고리즘과 달리, CFM은 소스 분포가 가우시안일 필요가 없거나 그 밀도 평가를 요구하지 않습니다. 우리 목적 함수의 변형 중 하나는 최적 수송 CFM(OT-CFM)으로, 훈련이 더 안정적이고 추론 속도가 빠른 더 단순한 흐름을 생성하며, 이는 실험을 통해 평가되었습니다. 또한, 실제 OT 계획이 가능할 때 우리의 OT-CFM 방법이 동적 OT를 근사함을 보여줍니다. CFM으로 CNF를 훈련하면 단일 세포 역학 추론, 비지도 이미지 변환, 슈뢰딩거 브리지 추론 등 다양한 조건부 및 비조건부 생성 작업에서 결과가 개선됩니다.

## 핵심 내용
연속 정규화 흐름(CNF)은 매력적인 생성 모델링 기법이지만, 시뮬레이션 기반 최대 우도 훈련의 한계로 인해 제약을 받아왔습니다. 우리는 CNF를 위한 시뮬레이션 없는 훈련 목적 함수군인 일반화된 조건부 흐름 매칭(CFM) 기법을 소개합니다. CFM은 확산 모델에서 확률적 흐름을 훈련하는 데 사용되는 안정적인 회귀 목적 함수를 특징으로 하면서도 결정적 흐름 모델의 효율적인 추론을 누릴 수 있습니다. 확산 모델 및 기존 CNF 훈련 알고리즘과 달리, CFM은 소스 분포가 가우시안일 필요가 없거나 그 밀도 평가를 요구하지 않습니다. 우리 목적 함수의 변형 중 하나는 최적 수송 CFM(OT-CFM)으로, 훈련이 더 안정적이고 추론 속도가 빠른 더 단순한 흐름을 생성하며, 이는 실험을 통해 평가되었습니다. 또한, 실제 OT 계획이 가능할 때 우리의 OT-CFM 방법이 동적 OT를 근사함을 보여줍니다. CFM으로 CNF를 훈련하면 단일 세포 역학 추론, 비지도 이미지 변환, 슈뢰딩거 브리지 추론 등 다양한 조건부 및 비조건부 생성 작업에서 결과가 개선됩니다.
