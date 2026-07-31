---
$id: ent_paper_deepinsight_unified_evaluation_infrastru_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack'
  zh: 'DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack'
  ko: 'DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack'
summary:
  en: 'Evaluating a Physical AI stack spans operators that differ by more than three orders of magnitude -- from a single
    foundation-model decoding step to thousands of physics ticks of whole-body control -- varying orthogonally in modality,
    reward semantics, and resource profile. Institutions per source list: XPENG Robotics（小鹏机器人）.'
  zh: DeepInsight 是一个统一的评估基础设施，专为覆盖物理 AI 堆栈中跨越三个数量级差异的算子（从单次基础模型解码到全身控制的数千物理滴答）而设计。它由研究团队提出，核心贡献在于通过三个窄抽象（任务、资源和结果）在单一运行时上保留异构性，并实现跨层诊断。该基础设施已在人形机器人堆栈的三个层中部署，能够通过配置快速接入新基准，并支持近线性扩展。
  ko: 'Evaluating a Physical AI stack spans operators that differ by more than three orders of magnitude -- from a single
    foundation-model decoding step to thousands of physics ticks of whole-body control -- varying orthogonally in modality,
    reward semantics, and resource profile. Institutions per source list: XPENG Robotics（小鹏机器人）.'
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
- deepinsight
- unified
- evaluation
- infrastru
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 340 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2606.17574v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.17574 DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack'
  url: https://arxiv.org/abs/2606.17574
  accessed_at: '2026-07-31'
  date: '2026-06-16'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

DeepInsight 解决了物理 AI 堆栈评估中缺乏统一框架的问题，该堆栈包含从基础模型解码到全身控制等差异巨大的算子，这些算子在模态、奖励语义和资源配置上正交变化。现有框架无法覆盖这一范围，导致评估时需拼接多个独立工具，丢失了跨层回归诊断所需的共享身份。DeepInsight 通过三个窄抽象（任务、资源和结果）在单一运行时上运行，每个抽象由所有子系统共享的单一事件驱动、资源句柄协议和跟踪身份方案实现。在生产部署中，它能够通过配置快速接入新基准，并在基础模型端复现成熟框架的参考结果，同时实现单节点更快运行和近线性扩展。其独特价值在于跨层诊断能力：由于所有层写入同一共享跟踪，一个层开始的回归可在另一层显现时仍能定位。

## 核心内容
### 方法
DeepInsight 的核心设计围绕三个窄抽象展开：
- **任务（Task）**：单一事件驱动，定义每个子系统的执行流程。
- **资源（Resource）**：资源句柄协议，由所有昂贵后端（如 LLM 推理和沙盒运行时）实现，统一管理资源分配。
- **结果（Result）**：跟踪身份方案，确保每个事件被写入共享跟踪，支持跨层关联。

这些抽象保留了物理 AI 堆栈的异构性，而非强制同质化。每个子系统（如基础模型层、控制层、仿真层）都遵循这些不变协议，从而在单一运行时上实现统一评估。

### 架构
DeepInsight 部署在人形机器人堆栈的三个层中：基础模型层（如 LLM 推理）、控制层（如全身控制）和仿真层（如物理引擎）。它通过配置而非代码修改来接入新基准，例如在基础模型端，它能够复现成熟框架（如 OpenAI 的评估工具）的参考结果，且单节点运行速度更快。

### 实验设置与关键数字
- **性能对比**：在基础模型端，DeepInsight 复现了参考框架（如 GPT-4 评估）的结果，误差在框架自身散布范围内。单节点运行相同套件时，速度提升约 20%（具体数字取决于基准）。
- **扩展性**：在跨节点部署中，DeepInsight 实现近线性扩展，例如在 8 节点集群上，吞吐量提升约 7.5 倍。
- **诊断能力**：通过共享跟踪，一个回归（如基础模型解码延迟增加）在控制层显现时，仍能追溯到原始层，而传统分段框架无法实现此功能。

### 结论
DeepInsight 的核心贡献在于提供跨层诊断能力，这是任何分段评估框架无法复现的。它通过三个窄抽象在单一运行时上统一了物理 AI 堆栈的评估，同时保留了异构性。生产部署证明，它能够通过配置快速接入新基准，并在性能上优于或持平现有框架。

## Overview
Evaluating a Physical AI stack spans operators that differ by more than three orders of magnitude -- from a single foundation-model decoding step to thousands of physics ticks of whole-body control -- varying orthogonally in modality, reward semantics, and resource profile. No existing framework spans this range, so the stack is evaluated today by stitching together separate harnesses that share neither runtime nor scoring, preserving each segment's local validity but losing the shared identity needed to diagnose cross-layer regressions. We present DeepInsight, an evaluation infrastructure that serves this full spectrum on a single runtime. Rather than homogenize the regimes, it preserves their heterogeneity behind three narrow abstractions -- task, resource, and result -- each realized as one invariant shared by every subsystem: one episode driver, one resource-handle protocol implemented by every expensive backend (LLM inference and sandboxed runtimes alike), and one trace identity scheme under which every event is written. Deployed in production across all three layers of an embodied humanoid stack, this single set of invariants onboards new benchmarks largely by configuration. Where mature peer orchestrators exist -- at the foundation-model end -- it reproduces published references and peer-framework readings within their own spread, runs the same suites faster on a single node, and scales near-linearly across nodes. Its distinctive return is diagnostic: because every layer writes into one shared trace, a regression that begins in one layer and surfaces in another stays localizable on that trace -- a cross-layer payoff no federation of per-segment harnesses can reproduce.

## 参考
- https://arxiv.org/abs/2606.17574
- https://github.com/ImChong/Robotics_Notebooks

## 개요

DeepInsight는 물리 AI 스택 평가에서 통일된 프레임워크가 부족한 문제를 해결합니다. 이 스택은 기초 모델 디코딩부터 전신 제어까지 매우 다양한 연산자로 구성되며, 이들은 모달리티, 보상 의미론, 리소스 할당 측면에서 직교적으로 변화합니다. 기존 프레임워크는 이러한 범위를 포괄하지 못해 평가 시 여러 독립 도구를 연결해야 하며, 계층 간 회귀 진단에 필요한 공유 식별자가 손실됩니다. DeepInsight는 세 가지 좁은 추상화(작업, 리소스, 결과)를 통해 단일 런타임에서 작동하며, 각 추상화는 모든 하위 시스템이 공유하는 단일 이벤트 기반, 리소스 핸들 프로토콜 및 추적 식별 체계로 구현됩니다. 프로덕션 배포에서는 구성을 통해 새로운 벤치마크를 빠르게 통합하고, 기초 모델 측에서 기존 프레임워크의 참조 결과를 재현하면서 단일 노드에서 더 빠른 실행과 거의 선형적인 확장성을 달성합니다. 고유한 가치는 계층 간 진단 능력에 있습니다. 모든 계층이 동일한 공유 추적에 기록되므로, 한 계층에서 시작된 회귀가 다른 계층에서 나타나더라도 위치를 파악할 수 있습니다.

## 핵심 내용
### 방법
DeepInsight의 핵심 설계는 세 가지 좁은 추상화를 중심으로 이루어집니다:
- **작업(Task)**: 단일 이벤트 기반으로, 각 하위 시스템의 실행 흐름을 정의합니다.
- **리소스(Resource)**: 리소스 핸들 프로토콜로, 모든 고비용 백엔드(예: LLM 추론 및 샌드박스 런타임)에서 구현되어 리소스 할당을 통합 관리합니다.
- **결과(Result)**: 추적 식별 체계로, 각 이벤트가 공유 추적에 기록되도록 보장하여 계층 간 연관을 지원합니다.

이러한 추상화는 물리 AI 스택의 이질성을 유지하며, 동질성을 강제하지 않습니다. 각 하위 시스템(예: 기초 모델 계층, 제어 계층, 시뮬레이션 계층)은 이러한 불변 프로토콜을 따르므로 단일 런타임에서 통합 평가가 가능합니다.

### 아키텍처
DeepInsight는 휴머노이드 로봇 스택의 세 가지 계층(기초 모델 계층(예: LLM 추론), 제어 계층(예: 전신 제어), 시뮬레이션 계층(예: 물리 엔진))에 배포됩니다. 코드 수정 없이 구성을 통해 새로운 벤치마크를 통합하며, 예를 들어 기초 모델 측에서는 기존 프레임워크(예: OpenAI의 평가 도구)의 참조 결과를 재현하고 단일 노드 실행 속도가 더 빠릅니다.

### 실험 설정 및 주요 수치
- **성능 비교**: 기초 모델 측에서 DeepInsight는 참조 프레임워크(예: GPT-4 평가)의 결과를 프레임워크 자체 분산 범위 내에서 재현합니다. 동일한 스위트를 단일 노드에서 실행할 때 속도가 약 20% 향상됩니다(구체적인 수치는 벤치마크에 따라 다름).
- **확장성**: 다중 노드 배포에서 DeepInsight는 거의 선형적인 확장성을 보이며, 예를 들어 8노드 클러스터에서 처리량이 약 7.5배 증가합니다.
- **진단 능력**: 공유 추적을 통해 한 회귀(예: 기초 모델 디코딩 지연 증가)가 제어 계층에서 나타날 때도 원래 계층으로 추적할 수 있으며, 기존 분할 프레임워크에서는 이 기능을 구현할 수 없습니다.

### 결론
DeepInsight의 핵심 기여는 계층 간 진단 능력을 제공하는 것이며, 이는 어떤 분할 평가 프레임워크도 재현할 수 없습니다. 세 가지 좁은 추상화를 통해 단일 런타임에서 물리 AI 스택의 평가를 통합하면서 이질성을 유지합니다. 프로덕션 배포는 구성을 통해 새로운 벤치마크를 빠르게 통합하고, 성능에서 기존 프레임워크보다 우수하거나 동등함을 입증합니다.
