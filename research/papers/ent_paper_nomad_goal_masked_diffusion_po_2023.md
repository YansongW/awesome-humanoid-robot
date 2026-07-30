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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.07896v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
익숙하지 않은 환경에서의 로봇 내비게이션을 위한 로봇 학습은 작업 지향 내비게이션(즉, 로봇이 위치한 목표에 도달하는 것)과 작업 무관 탐색(즉, 새로운 환경에서 목표를 찾는 것) 모두를 위한 정책을 제공해야 합니다. 일반적으로 이러한 역할은 하위 목표 제안, 계획 또는 별도의 내비게이션 전략을 사용하는 등 별도의 모델로 처리됩니다. 본 논문에서는 단일 통합 확산 정책(diffusion policy)을 훈련하여 목표 지향 내비게이션과 목표 무관 탐색을 모두 처리하는 방법을 설명합니다. 후자는 새로운 환경을 탐색하는 능력을 제공하고, 전자는 목표가 위치한 후 사용자가 지정한 목표에 도달하는 능력을 제공합니다. 우리는 이 통합 정책이 생성 모델의 하위 목표 제안이나 잠재 변수 모델 기반의 이전 방법을 사용하는 접근 방식과 비교하여 새로운 환경에서 시각적으로 표시된 목표로 내비게이션할 때 전반적으로 더 나은 성능을 보임을 입증합니다. 우리는 여러 지상 로봇의 데이터로 훈련된 대규모 Transformer 기반 정책을 사용하고, 확산 모델 디코더를 통해 목표 조건부 및 목표 무관 내비게이션을 유연하게 처리하여 방법을 구현합니다. 실제 모바일 로봇 플랫폼에서 수행된 실험은 다섯 가지 대체 방법과 비교하여 보이지 않는 환경에서 효과적인 내비게이션을 보여주며, 최첨단 접근 방식보다 더 작은 모델을 사용했음에도 불구하고 성능이 크게 향상되고 충돌률이 낮아짐을 입증합니다. 더 많은 비디오, 코드 및 사전 훈련된 모델 체크포인트는 https://general-navigation-models.github.io/nomad/ 에서 확인할 수 있습니다.

## 핵심 내용
익숙하지 않은 환경에서의 로봇 내비게이션을 위한 로봇 학습은 작업 지향 내비게이션(즉, 로봇이 위치한 목표에 도달하는 것)과 작업 무관 탐색(즉, 새로운 환경에서 목표를 찾는 것) 모두를 위한 정책을 제공해야 합니다. 일반적으로 이러한 역할은 하위 목표 제안, 계획 또는 별도의 내비게이션 전략을 사용하는 등 별도의 모델로 처리됩니다. 본 논문에서는 단일 통합 확산 정책(diffusion policy)을 훈련하여 목표 지향 내비게이션과 목표 무관 탐색을 모두 처리하는 방법을 설명합니다. 후자는 새로운 환경을 탐색하는 능력을 제공하고, 전자는 목표가 위치한 후 사용자가 지정한 목표에 도달하는 능력을 제공합니다. 우리는 이 통합 정책이 생성 모델의 하위 목표 제안이나 잠재 변수 모델 기반의 이전 방법을 사용하는 접근 방식과 비교하여 새로운 환경에서 시각적으로 표시된 목표로 내비게이션할 때 전반적으로 더 나은 성능을 보임을 입증합니다. 우리는 여러 지상 로봇의 데이터로 훈련된 대규모 Transformer 기반 정책을 사용하고, 확산 모델 디코더를 통해 목표 조건부 및 목표 무관 내비게이션을 유연하게 처리하여 방법을 구현합니다. 실제 모바일 로봇 플랫폼에서 수행된 실험은 다섯 가지 대체 방법과 비교하여 보이지 않는 환경에서 효과적인 내비게이션을 보여주며, 최첨단 접근 방식보다 더 작은 모델을 사용했음에도 불구하고 성능이 크게 향상되고 충돌률이 낮아짐을 입증합니다. 더 많은 비디오, 코드 및 사전 훈련된 모델 체크포인트는 https://general-navigation-models.github.io/nomad/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2310.07896v1
