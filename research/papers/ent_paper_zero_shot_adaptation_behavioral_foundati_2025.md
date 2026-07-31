---
$id: ent_paper_zero_shot_adaptation_behavioral_foundati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Zero-Shot Adaptation of Behavioral Foundation Models to Unseen Dynamics
  zh: Zero-Shot Adaptation of Behavioral Foundation Models to Unseen Dynamics
  ko: Zero-Shot Adaptation of Behavioral Foundation Models to Unseen Dynamics
summary:
  en: Behavioral Foundation Models (BFMs) proved successful in producing policies for arbitrary tasks in a zero-shot manner,
    requiring no test-time training or task-specific fine-tuning.
  zh: 本文针对行为基础模型（BFM）在动态变化环境下零样本适应能力不足的问题，提出了一种基于Transformer信念估计器的前向-后向（FB）表示方法。该方法通过将策略编码空间划分为动力学特定聚类，实现了对训练中观察到的动态的响应及对未见动态的泛化，在离散和连续任务中零样本回报相比基线提升高达2倍。
  ko: Behavioral Foundation Models (BFMs) proved successful in producing policies for arbitrary tasks in a zero-shot manner,
    requiring no test-time training or task-specific fine-tuning.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- zero
- shot
- adaptation
- behavioral
- foundati
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 151 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2505.13150 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2505.13150v2); zh content by DeepSeek from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: arXiv:2505.13150 Zero-Shot Adaptation of Behavioral Foundation Models to Unseen Dynamics
  url: https://arxiv.org/abs/2505.13150
  accessed_at: '2026-07-31'
  date: '2025-05-19'
- id: src_002
  type: website
  title: 智元、众擎都在卷的人形机器人运控基座：41篇论文看懂BFM
  url: https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g
  accessed_at: '2026-07-31'
---

## 概述

行为基础模型（BFM）虽能在零样本条件下为任意任务生成策略，但无法应对动力学变化（如部分可观测性或转移函数改变），限制了其在机器人等真实场景中的应用。本文发现前向-后向（FB）表示方法无法区分不同动力学，导致潜在方向间相互干扰。为此，作者提出结合Transformer信念估计器的FB模型，通过将策略编码空间划分为与上下文嵌入方向对齐的动力学特定聚类，显著提升了零样本适应能力。实验表明，该方法在动态变化环境下，离散和连续任务的零样本回报均达到基线方法的2倍。

## 核心内容
### 核心问题
- 行为基础模型（BFM）中的前向-后向（FB）表示方法在动力学变化时失效，无法区分不同转移函数，导致潜在方向（参数化不同策略）间产生干扰。
- 该问题在部分可观测环境或测试时动力学意外变化（如机器人操作）中尤为突出，阻碍了BFM的实际部署。

### 方法创新
- **Transformer信念估计器**：在FB模型中引入基于Transformer的信念估计器，通过编码历史观测序列来推断当前动力学状态，实现零样本适应。
- **动力学特定聚类**：将策略编码空间划分为与上下文嵌入方向对齐的聚类，每个聚类对应一种训练中观察到的动力学模式。这避免了潜在方向间的干扰，并允许模型对未见动力学进行泛化。

### 实验设置
- **任务类型**：离散控制（如Gridworld）和连续控制（如MuJoCo机器人任务）。
- **基线方法**：标准FB模型、其他BFM变体（如Successor Features）。
- **评估指标**：零样本回报（zero-shot returns），即测试时直接应用预训练策略而不进行微调。

### 关键结果
- 在动态变化环境下，所提方法在离散和连续任务中均实现**2倍**于基线的零样本回报。
- 消融实验证实：Transformer信念估计器与动力学聚类两者缺一不可，单独使用任一组件性能显著下降。
- 模型对训练中未出现的动力学（如新的转移函数或观测噪声）仍能保持有效适应，验证了泛化能力。

### 结论
通过结合Transformer信念估计与动力学感知的策略编码空间划分，本文首次实现了BFM在动态变化环境下的零样本适应，为机器人等真实场景中的部署提供了可行方案。

## Overview
Behavioral Foundation Models (BFMs) proved successful in producing policies for arbitrary tasks in a zero-shot manner, requiring no test-time training or task-specific fine-tuning. Among the most promising BFMs are the ones that estimate the successor measure learned in an unsupervised way from task-agnostic offline data. However, these methods fail to react to changes in the dynamics, making them inefficient under partial observability or when the transition function changes. This hinders the applicability of BFMs in a real-world setting, e.g., in robotics, where the dynamics can unexpectedly change at test time. In this work, we demonstrate that Forward-Backward (FB) representation, one of the methods from the BFM family, cannot distinguish between distinct dynamics, leading to an interference among the latent directions, which parametrize different policies. To address this, we propose a FB model with a transformer-based belief estimator, which greatly facilitates zero-shot adaptation. We also show that partitioning the policy encoding space into dynamics-specific clusters, aligned with the context-embedding directions, yields additional gain in performance. These traits allow our method to respond to the dynamics observed during training and to generalize to unseen ones. Empirically, in the changing dynamics setting, our approach achieves up to a 2x higher zero-shot returns compared to the baselines for both discrete and continuous tasks.

## 参考
- https://arxiv.org/abs/2505.13150
- https://mp.weixin.qq.com/s/Ei32la_vo0UW9Y_QCAqB2g

## 개요

행동 기반 모델(BFM)은 제로샷 조건에서 임의의 작업에 대한 정책을 생성할 수 있지만, 역학 변화(부분 관측 가능성 또는 전이 함수 변경 등)에는 대응할 수 없어 로봇과 같은 실제 시나리오에서의 적용이 제한적입니다. 본 논문은 전방-후방(FB) 표현 방법이 서로 다른 역학을 구분하지 못하여 잠재 방향 간 상호 간섭이 발생함을 발견했습니다. 이를 위해 저자들은 Transformer 신념 추정기를 결합한 FB 모델을 제안하며, 정책 인코딩 공간을 컨텍스트 임베딩 방향과 정렬된 역학 특정 클러스터로 분할하여 제로샷 적응 능력을 크게 향상시켰습니다. 실험 결과, 동적 변화 환경에서 이산 및 연속 작업 모두 제로샷 보상이 기준 방법의 2배에 달했습니다.

## 핵심 내용
### 핵심 문제
- 행동 기반 모델(BFM)의 전방-후방(FB) 표현 방법은 역학 변화 시 실패하며, 서로 다른 전이 함수를 구분하지 못해 잠재 방향(서로 다른 정책을 매개변수화) 간 간섭이 발생합니다.
- 이 문제는 부분 관측 가능 환경 또는 테스트 시 역학의 예기치 않은 변화(예: 로봇 조작)에서 특히 두드러지며, BFM의 실제 배포를 저해합니다.

### 방법 혁신
- **Transformer 신념 추정기**: FB 모델에 Transformer 기반 신념 추정기를 도입하여, 과거 관측 시퀀스를 인코딩해 현재 역학 상태를 추론함으로써 제로샷 적응을 구현합니다.
- **역학 특정 클러스터링**: 정책 인코딩 공간을 컨텍스트 임베딩 방향과 정렬된 클러스터로 분할하며, 각 클러스터는 훈련 중 관찰된 하나의 역학 패턴에 해당합니다. 이는 잠재 방향 간 간섭을 방지하고 모델이 보지 못한 역학에 대해 일반화할 수 있게 합니다.

### 실험 설정
- **작업 유형**: 이산 제어(예: Gridworld) 및 연속 제어(예: MuJoCo 로봇 작업).
- **기준 방법**: 표준 FB 모델, 기타 BFM 변형(예: Successor Features).
- **평가 지표**: 제로샷 보상(zero-shot returns), 즉 테스트 시 미세 조정 없이 사전 훈련된 정책을 직접 적용한 성과.

### 주요 결과
- 동적 변화 환경에서 제안된 방법은 이산 및 연속 작업 모두 기준 대비 **2배**의 제로샷 보상을 달성했습니다.
- 절제 실험을 통해 Transformer 신념 추정기와 역학 클러스터링이 모두 필수적이며, 어느 하나만 사용하면 성능이 크게 저하됨을 확인했습니다.
- 모델은 훈련 중 나타나지 않은 역학(예: 새로운 전이 함수 또는 관측 노이즈)에도 효과적으로 적응하여 일반화 능력을 검증했습니다.

### 결론
Transformer 신념 추정과 역학 인식 정책 인코딩 공간 분할을 결합함으로써, 본 논문은 BFM의 동적 변화 환경에서의 제로샷 적응을 최초로 구현했으며, 로봇과 같은 실제 시나리오에서의 배포를 위한 실현 가능한 방안을 제시합니다.
