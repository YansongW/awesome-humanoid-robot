---
$id: ent_paper_tong_improving_and_generalizing_flo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  zh: 基于小批量最优传输的流式生成模型改进与泛化
  ko: 미니배치 최적 수송을 활용한 플로우 기반 생성 모델의 개선 및 일반화
summary:
  en: This paper introduces generalized conditional flow matching (CFM), a simulation-free
    regression objective for training continuous normalizing flows (CNFs), and proposes
    optimal transport CFM (OT-CFM), which uses minibatch optimal transport couplings
    to produce straighter flows and faster inference.
  zh: 本文提出了广义条件流匹配（CFM），一种用于训练连续归一化流的免模拟回归目标，并引入了最优传输条件流匹配（OT-CFM），利用小批量最优传输耦合生成更直的流并实现更快的推理。
  ko: 본 논문은 연속 정규화 흐름(CNF)을 학습하기 위한 시뮬레이션 없는 회귀 목적함수인 일반화된 조건부 플로우 매칭(CFM)을 제안하고,
    미니배치 최적 수송 결합을 사용하여 더 직선적인 플로우와 더 빠른 추론을 가능하게 하는 최적 수송 조건부 플로우 매칭(OT-CFM)을 제시한다.
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
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Improving and Generalizing Flow-Based Generative Models with Minibatch Optimal
    Transport
  url: https://arxiv.org/abs/2302.00482
  date: '2024'
  accessed_at: '2026-06-25'
related_entities:
- id: entity_flow_matching_lipman_2023
  relationship: extends
  description:
    en: Extends the flow matching (FM) framework of Lipman et al. (2023) to arbitrary
      source-target couplings.
    zh: 将Lipman等人（2023）的流匹配（FM）框架扩展到任意源-目标耦合。
    ko: Lipman et al. (2023)의 플로우 매칭(FM) 프레임워크를 임의의 소스-타겟 결합으로 확장한다.
- id: entity_continuous_normalizing_flows
  relationship: builds_on
  description:
    en: Provides a simulation-free training objective for continuous normalizing flows
      (CNFs).
    zh: 为连续归一化流（CNF）提供了免模拟的训练目标。
    ko: 연속 정규화 흐름(CNF)을 위한 시뮬레이션 없는 학습 목적함수를 제공한다.
- id: entity_diffusion_models
  relationship: is_alternative_to
  description:
    en: Contrasts with diffusion models by using a deterministic flow while retaining
      a stable regression objective.
    zh: 通过使用确定性流同时保留稳定的回归目标，与扩散模型形成对比。
    ko: 확정론적 플로우를 사용하면서 안정적인 회귀 목적함수를 유지하여 확산 모델과 대조된다.
- id: entity_optimal_transport
  relationship: uses
  description:
    en: Applies optimal transport theory via minibatch couplings to approximate dynamic
      optimal transport.
    zh: 通过小批量耦合应用最优传输理论来近似动态最优传输。
    ko: 미니배치 결합을 통해 최적 수송 이론을 적용하여 동적 최적 수송을 근사한다.
- id: entity_schrodinger_bridge
  relationship: extends
  description:
    en: Extends the CFM framework to simulation-free Schrödinger bridge inference
      (SB-CFM).
    zh: 将CFM框架扩展到免模拟的薛定谔桥推断（SB-CFM）。
    ko: CFM 프레임워크를 시뮬레이션 없는 슈뢰딩거 브리지 추론(SB-CFM)으로 확장한다.
- id: entity_torchcfm
  relationship: instantiates
  description:
    en: Implements CFM and OT-CFM algorithms in the open-source torchcfm Python package.
    zh: 在开源的torchcfm Python包中实现了CFM和OT-CFM算法。
    ko: 오픈소스 torchcfm Python 패키지에서 CFM 및 OT-CFM 알고리즘을 구현한다.
---

## Overview

Continuous normalizing flows (CNFs) model a data distribution by integrating a neural ordinary differential equation (ODE), but traditional maximum-likelihood training requires expensive simulation and backpropagation through the ODE solver. The paper proposes generalized conditional flow matching (CFM), a family of simulation-free regression objectives that directly regress a neural vector field against tractable conditional probability paths. Unlike prior CNF training, CFM does not require the source distribution to be Gaussian or require evaluation of its density, and it unifies several recent flow-matching and diffusion-style training objectives under one framework.

A key special case is optimal transport CFM (OT-CFM). OT-CFM constructs source-target sample pairs via a minibatch optimal transport coupling, which induces straighter probability paths and lower-variance regression targets. The authors prove that when the true optimal transport plan is available, OT-CFM approximates dynamic optimal transport; an entropic variant, SB-CFM, approximates Schrödinger bridge probability flows without simulation. The method is compatible with arbitrary empirical source and target distributions.

The authors evaluate CFM and OT-CFM on low-dimensional synthetic densities, single-cell trajectory interpolation, unconditional CIFAR-10 image generation, and CelebA attribute-based image translation. Across tasks, OT-CFM accelerates training, reduces inference cost, and improves sample quality. They also release the torchcfm Python package and improved reproducible training recipes for high-dimensional flow models.

## Key Contributions

- A unified conditional flow matching framework that generalizes and subsumes many existing flow matching and diffusion training objectives (Table 1).
- OT-CFM and SB-CFM variants that solve dynamic optimal transport and Schrödinger bridge problems in a simulation-free manner using only static couplings between marginal distributions.
- Empirical demonstration that OT-CFM reduces training variance, accelerates convergence, and enables faster inference with fewer function evaluations across 2D densities, single-cell data, CIFAR-10, and CelebA.
- Release of the torchcfm Python package and improved, reproducible training practices for high-dimensional flow-based generative models.

## Relevance to Humanoid Robotics

Efficient, simulation-free generative modeling is directly relevant to humanoid robotics, where world models must forecast high-dimensional state distributions for perception, motion planning, and control. OT-CFM's ability to learn straight, fast-to-integrate flows can accelerate generative world-model training and reduce the number of function evaluations needed at deployment, which matters for real-time robot inference.

The framework can also support synthetic data generation and domain translation pipelines used to augment robot perception datasets or generate diverse motion trajectories. While the paper does not evaluate on humanoid platforms, its algorithms provide a general-purpose building block for generative intelligence, synthetic-data tools, and probabilistic planning components that appear in humanoid robot software stacks.
