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
  zh: 本文提出广义条件流匹配（CFM）技术，这是一种用于训练连续归一化流（CNF）的无模拟回归目标。其变体最优传输CFM（OT-CFM）通过小批量最优传输耦合生成更直的流，从而实现更快的推理速度。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.00482v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (747 chars, DeepSeek).'
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
连续归一化流（CNF）是一种有吸引力的生成建模技术，但受限于基于模拟的最大似然训练。本文引入广义条件流匹配（CFM）技术，这是一类无模拟训练目标，兼具扩散模型稳定回归目标和确定性流模型高效推理的优势。与扩散模型和现有CNF训练算法不同，CFM不要求源分布为高斯分布，也无需评估其密度。其变体最优传输CFM（OT-CFM）能创建更简单的流，训练更稳定且推理更快。实验表明，当真实最优传输计划可用时，OT-CFM可近似动态最优传输。

## 核心内容
### 核心方法
- **广义条件流匹配（CFM）**：提出一种无模拟回归目标，用于训练连续归一化流（CNF）。该目标函数稳定，类似扩散模型中随机流的训练方式，但保留了确定性流模型的高效推理特性。
- **关键优势**：CFM不要求源分布为高斯分布，也无需评估其密度，这使其比扩散模型和现有CNF训练算法更具灵活性。

### 最优传输CFM（OT-CFM）
- **机制**：通过小批量最优传输耦合，生成更直的流路径，从而简化训练过程并加速推理。
- **理论联系**：当真实最优传输计划可用时，OT-CFM可近似动态最优传输（dynamic OT），实现更优的生成质量。

### 实验设置与结果
- **任务覆盖**：在多种条件生成和无条件生成任务上验证了CFM的有效性，包括：
  - 单细胞动态推断（single cell dynamics）
  - 无监督图像翻译（unsupervised image translation）
  - Schrödinger桥推断（Schrödinger bridge inference）
- **性能提升**：与现有方法相比，CFM训练出的CNF在生成质量和推理速度上均有显著改进。

## Overview
Continuous normalizing flows (CNFs) are an attractive generative modeling technique, but they have been held back by limitations in their simulation-based maximum likelihood training. We introduce the generalized conditional flow matching (CFM) technique, a family of simulation-free training objectives for CNFs. CFM features a stable regression objective like that used to train the stochastic flow in diffusion models but enjoys the efficient inference of deterministic flow models. In contrast to both diffusion models and prior CNF training algorithms, CFM does not require the source distribution to be Gaussian or require evaluation of its density. A variant of our objective is optimal transport CFM (OT-CFM), which creates simpler flows that are more stable to train and lead to faster inference, as evaluated in our experiments. Furthermore, we show that when the true OT plan is available, our OT-CFM method approximates dynamic OT. Training CNFs with CFM improves results on a variety of conditional and unconditional generation tasks, such as inferring single cell dynamics, unsupervised image translation, and Schrödinger bridge inference.

## 参考
- http://arxiv.org/abs/2302.00482v4

## 개요
연속 정규화 흐름(CNF)은 매력적인 생성 모델링 기법이지만, 시뮬레이션 기반 최대 우도 학습에 제한적입니다. 본 논문은 일반화 조건부 흐름 매칭(CFM) 기법을 소개하며, 이는 시뮬레이션 없는 학습 목표의 한 종류로, 확산 모델의 안정적인 회귀 목표와 결정적 흐름 모델의 효율적인 추론 장점을 결합합니다. 확산 모델 및 기존 CNF 학습 알고리즘과 달리, CFM은 소스 분포가 가우시안일 필요가 없으며 밀도 평가도 요구하지 않습니다. 그 변형인 최적 수송 CFM(OT-CFM)은 더 단순한 흐름을 생성하여 학습이 더 안정적이고 추론이 더 빠릅니다. 실험은 실제 최적 수송 계획이 사용 가능할 때 OT-CFM이 동적 최적 수송을 근사할 수 있음을 보여줍니다.

## 핵심 내용
### 핵심 방법
- **일반화 조건부 흐름 매칭(CFM)**: 연속 정규화 흐름(CNF)을 학습하기 위한 시뮬레이션 없는 회귀 목표를 제안합니다. 이 목표 함수는 안정적이며, 확산 모델의 확률적 흐름 학습 방식과 유사하지만 결정적 흐름 모델의 효율적인 추론 특성을 유지합니다.
- **주요 장점**: CFM은 소스 분포가 가우시안일 필요가 없으며 밀도 평가도 요구하지 않아, 확산 모델 및 기존 CNF 학습 알고리즘보다 더 유연합니다.

### 최적 수송 CFM(OT-CFM)
- **메커니즘**: 미니배치 최적 수송 결합을 통해 더 직선적인 흐름 경로를 생성하여 학습 과정을 단순화하고 추론을 가속화합니다.
- **이론적 연관성**: 실제 최적 수송 계획이 사용 가능할 때, OT-CFM은 동적 최적 수송(dynamic OT)을 근사하여 더 우수한 생성 품질을 달성할 수 있습니다.

### 실험 설정 및 결과
- **작업 범위**: 다양한 조건부 생성 및 무조건부 생성 작업에서 CFM의 효과를 검증했습니다. 포함 사항:
  - 단일 세포 동적 추론(single cell dynamics)
  - 비지도 이미지 변환(unsupervised image translation)
  - 슈뢰딩거 다리 추론(Schrödinger bridge inference)
- **성능 향상**: 기존 방법과 비교하여 CFM으로 학습된 CNF는 생성 품질과 추론 속도 모두에서 현저한 개선을 보였습니다.
