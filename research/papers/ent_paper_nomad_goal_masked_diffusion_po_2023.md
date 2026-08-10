---
$id: ent_paper_nomad_goal_masked_diffusion_po_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
  zh: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
  ko: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration'
summary:
  en: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration is a 2023 work on navigation for humanoid robots.'
  zh: NoMaD 是 2023 年提出的一种用于机器人导航与探索的统一扩散策略模型。该工作由相关研究团队完成，核心贡献在于使用单一 Transformer 架构的扩散策略，同时处理目标导向导航与无目标探索任务，并在真实机器人平台上验证了其相较于五种对比方法的性能优势与更低的碰撞率。
  ko: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration is a 2023 work on navigation for humanoid robots.'
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
- navigation
- nomad
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.07896v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (912 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration (arXiv)'
  url: https://arxiv.org/abs/2310.07896
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
NoMaD 旨在解决机器人在陌生环境中导航时，通常需要为任务导向导航（到达已定位目标）与任务无关探索（搜索新目标）分别训练不同模型的问题。该研究提出训练一个统一的扩散策略，通过大规模 Transformer 架构与扩散模型解码器，使单一模型能同时处理这两种导航模式。实验在真实移动机器人平台上进行，结果表明，与使用生成模型子目标提议或基于潜变量模型的先前方法相比，NoMaD 在陌生环境中导航至视觉指定目标时表现更优，且尽管模型规模更小，仍实现了性能提升与碰撞率降低。

## 核心内容
### 方法概述
NoMaD 的核心思想是训练一个统一的扩散策略，将目标导向导航与无目标探索整合到单一模型中。该模型基于大规模 Transformer 架构，使用扩散模型解码器来灵活处理两种模式：当目标位置已知时，模型执行目标条件导航；当目标未知时，模型执行无目标探索以搜索新环境。

### 架构细节
- **策略网络**：采用 Transformer 作为主干网络，处理来自多个地面机器人的训练数据。
- **扩散模型解码器**：通过去噪过程生成动作序列，能够根据输入条件（是否包含目标信息）切换导航模式。
- **训练数据**：使用多机器人收集的导航数据，涵盖目标导向与探索场景。

### 实验设置
- **平台**：真实移动机器人平台。
- **对比方法**：包括基于生成模型的子目标提议方法、基于潜变量模型的先前方法，以及另外三种替代方案，共五种对比方法。
- **评估指标**：导航成功率、碰撞率、到达目标所需时间。

### 关键结果
- **性能提升**：在陌生环境中导航至视觉指定目标时，NoMaD 的整体性能优于所有对比方法。
- **碰撞率**：尽管模型规模小于当前最先进方法，NoMaD 仍实现了显著更低的碰撞率。
- **效率**：统一策略避免了多模型切换的开销，提升了导航效率。

### 结论
NoMaD 证明了单一扩散策略可以同时处理目标导向导航与无目标探索，在真实机器人平台上展现出优于现有方法的性能。该工作为机器人导航提供了一种更简洁、高效的解决方案，相关代码、预训练模型及视频已开源。

## Overview
Robotic learning for navigation in unfamiliar environments needs to provide policies for both task-oriented navigation (i.e., reaching a goal that the robot has located), and task-agnostic exploration (i.e., searching for a goal in a novel setting). Typically, these roles are handled by separate models, for example by using subgoal proposals, planning, or separate navigation strategies. In this paper, we describe how we can train a single unified diffusion policy to handle both goal-directed navigation and goal-agnostic exploration, with the latter providing the ability to search novel environments, and the former providing the ability to reach a user-specified goal once it has been located. We show that this unified policy results in better overall performance when navigating to visually indicated goals in novel environments, as compared to approaches that use subgoal proposals from generative models, or prior methods based on latent variable models. We instantiate our method by using a large-scale Transformer-based policy trained on data from multiple ground robots, with a diffusion model decoder to flexibly handle both goal-conditioned and goal-agnostic navigation. Our experiments, conducted on a real-world mobile robot platform, show effective navigation in unseen environments in comparison with five alternative methods, and demonstrate significant improvements in performance and lower collision rates, despite utilizing smaller models than state-of-the-art approaches. For more videos, code, and pre-trained model checkpoints, see https://general-navigation-models.github.io/nomad/

## 参考
- http://arxiv.org/abs/2310.07896v1

## 개요
NoMaD는 로봇이 익숙하지 않은 환경에서 탐색할 때, 일반적으로 작업 지향 내비게이션(위치가 확인된 목표에 도달)과 작업 무관 탐색(새로운 목표 검색)을 위해 각각 다른 모델을 훈련해야 하는 문제를 해결하는 것을 목표로 합니다. 이 연구는 대규모 Transformer 아키텍처와 확산 모델 디코더를 통해 단일 모델이 두 내비게이션 모드를 동시에 처리할 수 있도록 하는 통합 확산 정책을 훈련하는 것을 제안합니다. 실험은 실제 이동 로봇 플랫폼에서 수행되었으며, 결과는 생성 모델 하위 목표 제안 또는 잠재 변수 모델 기반의 이전 방법과 비교하여 NoMaD가 익숙하지 않은 환경에서 시각적으로 지정된 목표로 내비게이션할 때 더 우수한 성능을 보였고, 모델 규모가 더 작음에도 불구하고 성능 향상과 충돌률 감소를 달성했음을 보여줍니다.

## 핵심 내용
### 방법 개요
NoMaD의 핵심 아이디어는 목표 지향 내비게이션과 무목표 탐색을 단일 모델에 통합하는 통합 확산 정책을 훈련하는 것입니다. 이 모델은 대규모 Transformer 아키텍처를 기반으로 하며, 확산 모델 디코더를 사용하여 두 모드를 유연하게 처리합니다: 목표 위치가 알려진 경우 모델은 목표 조건 내비게이션을 수행하고, 목표가 알려지지 않은 경우 모델은 새로운 환경을 탐색하기 위해 무목표 탐색을 수행합니다.

### 아키텍처 세부 사항
- **정책 네트워크**: Transformer를 백본 네트워크로 사용하여 여러 지상 로봇의 훈련 데이터를 처리합니다.
- **확산 모델 디코더**: 노이즈 제거 과정을 통해 행동 시퀀스를 생성하며, 입력 조건(목표 정보 포함 여부)에 따라 내비게이션 모드를 전환할 수 있습니다.
- **훈련 데이터**: 목표 지향 및 탐색 시나리오를 포함하는 다중 로봇 수집 내비게이션 데이터를 사용합니다.

### 실험 설정
- **플랫폼**: 실제 이동 로봇 플랫폼.
- **비교 방법**: 생성 모델 기반 하위 목표 제안 방법, 잠재 변수 모델 기반의 이전 방법, 그리고 추가로 세 가지 대안 방법을 포함한 총 다섯 가지 비교 방법.
- **평가 지표**: 내비게이션 성공률, 충돌률, 목표 도달 시간.

### 주요 결과
- **성능 향상**: 익숙하지 않은 환경에서 시각적으로 지정된 목표로 내비게이션할 때 NoMaD의 전체 성능이 모든 비교 방법보다 우수했습니다.
- **충돌률**: 모델 규모가 현재 최첨단 방법보다 작음에도 불구하고 NoMaD는 현저히 낮은 충돌률을 달성했습니다.
- **효율성**: 통합 정책은 다중 모델 전환의 오버헤드를 피하여 내비게이션 효율성을 향상시켰습니다.

### 결론
NoMaD는 단일 확산 정책이 목표 지향 내비게이션과 무목표 탐색을 동시에 처리할 수 있음을 입증했으며, 실제 로봇 플랫폼에서 기존 방법보다 우수한 성능을 보여주었습니다. 이 작업은 로봇 내비게이션을 위한 더 간결하고 효율적인 솔루션을 제공하며, 관련 코드, 사전 훈련된 모델 및 비디오가 오픈소스로 공개되었습니다.
