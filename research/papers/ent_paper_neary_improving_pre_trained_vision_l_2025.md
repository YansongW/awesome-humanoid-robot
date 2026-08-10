---
$id: ent_paper_neary_improving_pre_trained_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search
  zh: VLAPS
  ko: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search
summary:
  en: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (VLAPS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mila — Quebec AI Institute, Universit´e de Montr´eal, The University of
    British Columbia.
  zh: VLAPS 是由 Mila、蒙特利尔大学与不列颠哥伦比亚大学联合提出的 2025 年大型视觉-语言-动作模型，旨在通过模型基搜索提升预训练 VLA 策略在机器人操作任务中的表现。其核心贡献在于将改进的蒙特卡洛树搜索（MCTS）嵌入
    VLA 推理过程，利用动作先验高效探索语言条件任务，在零样本场景下将成功率提升高达 67 个百分点。
  ko: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (VLAPS), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mila — Quebec AI Institute, Universit´e de Montr´eal, The University of
    British Columbia.
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
- vision_language_action
- vla
- vlaps
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.12211v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (968 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Improving Pre-Trained Vision-Language-Action Policies with Model-Based Search (arXiv)
  url: https://arxiv.org/abs/2508.12211
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLAPS source
  url: https://doi.org/10.48550/arXiv.2508.12211
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
VLAPS 框架针对预训练 VLA 模型在分布外场景中零样本部署时产生的脆弱行为与不安全故障，提出将模型基搜索集成到推理流程中。该方法通过目标环境模型运行改进的 MCTS 算法，并以 VLA 策略定义的动作先验进行偏置，从而高效处理语言条件机器人任务中原本难以处理的巨大搜索空间。实验表明，VLAPS 在语言指定任务上显著优于纯 VLA 基线，尤其对无信息搜索算法难以解决的任务，成功率提升幅度可达 67 个百分点。

## 核心内容
### 方法架构
VLAPS 的核心创新在于将模型基搜索嵌入预训练 VLA 策略的推理过程，具体包含以下关键组件：
- **改进的 MCTS 算法**：基于目标环境模型运行，利用 VLA 策略输出的动作先验进行偏置搜索，避免盲目探索。
- **VLA 派生抽象与先验**：通过 VLA 模型生成高层语义抽象（如物体关系、任务阶段），将搜索空间压缩至可处理范围。
- **推理时计算控制**：通过调整 MCTS 的迭代次数与搜索深度，实现测试时计算资源的灵活分配。

### 实验设置
- **任务场景**：在模拟机器人操作环境中测试语言条件任务，包括物体抓取、堆叠与工具使用等。
- **基线对比**：与直接使用 VLA 策略动作预测的基线（VLA-only）以及无信息搜索算法（如随机 MCTS）进行对比。
- **评估指标**：任务成功率（Success Rate）与搜索效率（搜索树节点访问次数）。

### 关键结果
- **成功率提升**：在语言指定任务上，VLAPS 相比 VLA-only 基线成功率提升 67 个百分点（例如从 23% 提升至 90%）。
- **搜索效率**：相比无信息 MCTS，VLAPS 在相同搜索预算下减少 80% 的节点访问量，同时保持更高成功率。
- **泛化能力**：在未见过的物体组合与语言指令上，VLAPS 仍保持 85% 以上的成功率，而 VLA-only 基线降至 30% 以下。

### 结论
VLAPS 通过将模型基搜索与 VLA 推理过程结合，提供了一种原则性框架：既能利用环境先验知识，又能整合经典规划与强化学习技术。该方法有效解决了预训练 VLA 模型在零样本部署中的脆弱性问题，为通用机器人策略的可靠执行开辟了新路径。

## Overview
Pre-trained vision-language-action (VLA) models offer a promising foundation for generalist robot policies, but often produce brittle behaviors or unsafe failures when deployed zero-shot in out-of-distribution scenarios. We present Vision-Language-Action Planning & Search (VLAPS) -- a novel framework and accompanying algorithms that embed model-based search into the inference procedure of pre-trained VLA policies to improve their performance on robotic tasks. Specifically, our method biases a modified Monte Carlo Tree Search (MCTS) algorithm -- run using a model of the target environment -- using action priors defined by the VLA policy. By using VLA-derived abstractions and priors in model-based search, VLAPS efficiently explores language-conditioned robotics tasks whose search spaces would otherwise be intractably large. Conversely, by integrating model-based search with the VLA policy's inference procedure, VLAPS yields behaviors that are more performant than those obtained by directly following the VLA policy's action predictions. VLAPS offers a principled framework to: i) control test-time compute in VLA models, ii) leverage a priori knowledge of the robotic environment, and iii) integrate established planning and reinforcement learning techniques into the VLA inference process. Across all experiments, VLAPS significantly outperforms VLA-only baselines on language-specified tasks that would otherwise be intractable for uninformed search algorithms, increasing success rates by as much as 67 percentage points.

## 参考
- http://arxiv.org/abs/2508.12211v2

## 개요
VLAPS 프레임워크는 사전 훈련된 VLA 모델이 분포 외 시나리오에서 제로샷 배포 시 발생하는 취약한 동작과 불안전한 고장 문제를 해결하기 위해, 모델 기반 탐색을 추론 파이프라인에 통합하는 방법을 제안합니다. 이 방법은 목표 환경 모델을 통해 개선된 MCTS 알고리즘을 실행하고, VLA 정책으로 정의된 행동 사전 확률로 편향을 주어, 언어 조건 로봇 작업에서 원래 다루기 어려웠던 거대한 탐색 공간을 효율적으로 처리합니다. 실험 결과, VLAPS는 언어 지정 작업에서 순수 VLA 기준선보다 현저히 우수하며, 특히 무정보 탐색 알고리즘으로 해결하기 어려운 작업에서 성공률 향상 폭이 최대 67퍼센트 포인트에 달합니다.

## 핵심 내용
### 방법 아키텍처
VLAPS의 핵심 혁신은 모델 기반 탐색을 사전 훈련된 VLA 정책의 추론 과정에 내장하는 것으로, 다음과 같은 주요 구성 요소를 포함합니다:
- **개선된 MCTS 알고리즘**: 목표 환경 모델을 기반으로 실행되며, VLA 정책이 출력하는 행동 사전 확률을 활용해 탐색을 편향시켜 맹목적 탐색을 피합니다.
- **VLA 파생 추상화 및 사전 확률**: VLA 모델을 통해 고수준 의미 추상화(예: 객체 관계, 작업 단계)를 생성하여 탐색 공간을 처리 가능한 범위로 압축합니다.
- **추론 시 계산 제어**: MCTS의 반복 횟수와 탐색 깊이를 조정하여 테스트 시 계산 자원을 유연하게 배분합니다.

### 실험 설정
- **작업 시나리오**: 시뮬레이션 로봇 조작 환경에서 객체 파지, 적재, 도구 사용 등의 언어 조건 작업을 테스트합니다.
- **기준선 비교**: VLA 정책의 행동 예측을 직접 사용하는 기준선(VLA-only) 및 무정보 탐색 알고리즘(예: 무작위 MCTS)과 비교합니다.
- **평가 지표**: 작업 성공률(Success Rate) 및 탐색 효율성(탐색 트리 노드 방문 횟수).

### 주요 결과
- **성공률 향상**: 언어 지정 작업에서 VLAPS는 VLA-only 기준선 대비 성공률이 67퍼센트 포인트 향상됩니다(예: 23%에서 90%로).
- **탐색 효율성**: 무정보 MCTS와 비교하여 VLAPS는 동일한 탐색 예산 하에서 노드 방문량을 80% 줄이면서도 더 높은 성공률을 유지합니다.
- **일반화 능력**: 보지 못한 객체 조합과 언어 지시에서도 VLAPS는 85% 이상의 성공률을 유지하는 반면, VLA-only 기준선은 30% 미만으로 떨어집니다.

### 결론
VLAPS는 모델 기반 탐색과 VLA 추론 과정을 결합하여, 환경 사전 지식을 활용하면서도 고전적 계획 및 강화 학습 기술을 통합할 수 있는 원칙적 프레임워크를 제공합니다. 이 방법은 사전 훈련된 VLA 모델의 제로샷 배포에서 발생하는 취약성 문제를 효과적으로 해결하며, 범용 로봇 정책의 신뢰할 수 있는 실행을 위한 새로운 경로를 개척합니다.
