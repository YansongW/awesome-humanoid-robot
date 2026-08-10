---
$id: ent_paper_rgmp_recurrent_geometric_prior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation'
  zh: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation'
  ko: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation'
summary:
  en: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  zh: RGMP 是一个面向人形机器人的端到端操作框架，由研究团队提出，旨在解决数据驱动方法在几何推理和机器人-目标关系建模上的不足。其核心贡献在于通过几何先验技能选择器和自适应递归高斯网络，实现了跨域泛化能力与数据效率的显著提升。
  ko: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation is a 2025 work on manipulation
    for humanoid robots.'
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
- manipulation
- rgmp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09141v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (872 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2511.09141
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前人形机器人操作研究主要依赖数据驱动方法，但这类方法在未见场景中缺乏几何推理能力，且对机器人-目标关系的建模效率低下，导致训练资源浪费。为此，RGMP 框架统一了几何-语义技能推理与数据高效的视觉运动控制。它通过几何先验技能选择器将几何归纳偏置注入视觉语言模型，使机器人能在未见场景中自适应生成技能序列；同时，自适应递归高斯网络将机器人-目标交互参数化为紧凑的高斯过程层级，递归编码多尺度空间关系，从而从稀疏演示中实现灵巧且数据高效的运动合成。在真实人形机器人和桌面双臂机器人上的评估显示，RGMP 在泛化测试中达到 87% 的任务成功率，数据效率比现有最优模型高出 5 倍。

## 核心内容
### 方法概述
RGMP 是一个端到端框架，包含两个核心模块：
- **几何先验技能选择器 (Geometric-prior Skill Selector)**：将几何归纳偏置注入视觉语言模型 (VLM)，使模型在未见场景中仅需极少的空间常识微调即可生成自适应技能序列。这解决了传统数据驱动方法在几何推理上的缺失。
- **自适应递归高斯网络 (Adaptive Recursive Gaussian Network)**：将机器人-目标交互参数化为紧凑的高斯过程层级，通过递归编码多尺度空间关系，从稀疏演示中合成灵巧且数据高效的运动。该设计避免了传统方法对大量训练数据的依赖。

### 实验设置
- **平台**：在自研人形机器人和桌面双臂机器人上评估。
- **任务**：涵盖多种操作任务，重点测试跨域泛化能力。
- **对比基线**：与当前最优模型 (state-of-the-art) 进行数据效率和任务成功率对比。

### 关键结果
- **泛化测试成功率**：RGMP 在未见场景中达到 87% 的任务成功率。
- **数据效率**：相比最优模型，RGMP 的数据效率提升 5 倍，即仅需 1/5 的训练数据即可达到同等性能。
- **核心优势**：几何-语义推理与递归高斯自适应机制共同支撑了其卓越的跨域泛化能力。

## Overview
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussion adaptation.

## Overview
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussian adaptation.

## Content
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussian adaptation.

## 参考
- http://arxiv.org/abs/2511.09141v2

## 개요
현재 휴머노이드 로봇 조작 연구는 주로 데이터 기반 방법에 의존하지만, 이러한 방법은 미지의 장면에서 기하학적 추론 능력이 부족하고 로봇-목표 관계 모델링의 효율성이 낮아 훈련 자원이 낭비됩니다. 이를 해결하기 위해 RGMP 프레임워크는 기하학-의미론적 스킬 추론과 데이터 효율적인 시각 운동 제어를 통합합니다. 기하학적 사전 스킬 선택기를 통해 기하학적 귀납 편향을 비전 언어 모델에 주입하여 로봇이 미지의 장면에서 적응형 스킬 시퀀스를 생성할 수 있게 합니다. 동시에 적응형 재귀 가우시안 네트워크는 로봇-목표 상호작용을 컴팩트한 가우시안 프로세스 계층으로 매개변수화하고, 다중 스케일 공간 관계를 재귀적으로 인코딩하여 희소 시연에서 정교하고 데이터 효율적인 운동 합성을 구현합니다. 실제 휴머노이드 로봇과 데스크톱 이중 팔 로봇에서의 평가 결과, RGMP는 일반화 테스트에서 87%의 작업 성공률을 달성했으며, 데이터 효율성은 기존 최적 모델보다 5배 높습니다.

## 핵심 내용
### 방법 개요
RGMP는 두 가지 핵심 모듈을 포함하는 엔드투엔드 프레임워크입니다:
- **기하학적 사전 스킬 선택기 (Geometric-prior Skill Selector)**: 기하학적 귀납 편향을 비전 언어 모델(VLM)에 주입하여 모델이 미지의 장면에서 최소한의 공간 상식 미세 조정만으로 적응형 스킬 시퀀스를 생성할 수 있게 합니다. 이는 전통적인 데이터 기반 방법의 기하학적 추론 부족 문제를 해결합니다.
- **적응형 재귀 가우시안 네트워크 (Adaptive Recursive Gaussian Network)**: 로봇-목표 상호작용을 컴팩트한 가우시안 프로세스 계층으로 매개변수화하고, 다중 스케일 공간 관계를 재귀적으로 인코딩하여 희소 시연에서 정교하고 데이터 효율적인 운동을 합성합니다. 이 설계는 전통적인 방법의 대량 훈련 데이터 의존성을 피합니다.

### 실험 설정
- **플랫폼**: 자체 개발 휴머노이드 로봇과 데스크톱 이중 팔 로봇에서 평가.
- **작업**: 다양한 조작 작업을 포함하며, 교차 도메인 일반화 능력을 중점적으로 테스트.
- **비교 기준**: 현재 최적 모델(state-of-the-art)과 데이터 효율성 및 작업 성공률을 비교.

### 핵심 결과
- **일반화 테스트 성공률**: RGMP는 미지의 장면에서 87%의 작업 성공률을 달성.
- **데이터 효율성**: 최적 모델 대비 RGMP의 데이터 효율성은 5배 향상, 즉 동일한 성능을 달성하기 위해 1/5의 훈련 데이터만 필요.
- **핵심 장점**: 기하학-의미론적 추론과 재귀 가우시안 적응 메커니즘이 함께 우수한 교차 도메인 일반화 능력을 뒷받침합니다.
