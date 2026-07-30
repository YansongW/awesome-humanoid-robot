---
$id: ent_paper_diffusion_forcing_for_multi_ag_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
  zh: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
  ko: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
summary:
  en: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  zh: MAGNet 是一个统一的自回归扩散框架，用于多智能体交互序列建模，由研究团队于2025年提出。其核心贡献在于通过显式建模智能体间耦合，在单一模型中支持成对与多人预测、伙伴补全、智能体生成等任务，并能自回归生成长达数百步的超长序列，在成对基准上达到与专用方法相当的性能，同时自然扩展到三人及以上场景。
  ko: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_forcing_for_multi_ag
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17900v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling (arXiv)
  url: https://arxiv.org/abs/2512.17900
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MAGNet 针对多人交互建模中时间跨度长、智能体依赖强、群体规模可变等挑战，提出了一种统一的自回归扩散框架。该框架通过灵活的条件设置与采样，在单一模型中支持成对与多人预测、伙伴补全、智能体生成等多种交互任务，并能自回归生成长达数百步的超长序列。其关键创新在于在自回归去噪过程中显式建模智能体间耦合，从而生成紧密同步的活动（如舞蹈、拳击）和松散结构的社会互动。实验表明，MAGNet 在成对基准上达到与专用方法相当的性能，并自然扩展到三人及以上场景。

## 核心内容
### 方法架构
MAGNet 基于自回归扩散框架，将多智能体运动生成建模为序列条件生成问题。其核心设计包括：
- **统一框架**：通过灵活的条件设置与采样，在单一模型中支持成对预测、多人预测、伙伴补全、伙伴预测和智能体生成等多种任务。
- **智能体耦合建模**：在自回归去噪过程中显式建模智能体间依赖关系，确保生成动作的协调性。
- **超长序列生成**：能够自回归生成长达数百步的运动序列，覆盖长时间跨度的交互。

### 实验设置
- **基准测试**：在成对交互基准（如舞蹈、拳击）上评估，并与专用方法对比。
- **扩展场景**：自然扩展到三人及以上场景，验证框架的泛化能力。
- **评估指标**：关注生成动作的时间动态和空间协调性，通过补充视频展示效果。

### 关键结果
- **性能**：在成对基准上达到与专用方法相当的性能，无需任务特定调整。
- **泛化能力**：成功处理三人及以上场景，支持紧密同步活动（如舞蹈、拳击）和松散结构社会互动。
- **序列长度**：支持数百步的超长序列生成，突破现有方法的时间限制。

### 结论
MAGNet 通过统一的自回归扩散框架，解决了多智能体交互建模中的关键挑战，为机器人和社会计算中的多人运动生成提供了灵活、可扩展的解决方案。项目页面提供补充视频以展示生成交互的时间动态和空间协调性。

## Overview
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## 개요
다중 인물 상호작용을 이해하고 생성하는 것은 로보틱스와 사회 컴퓨팅에 광범위한 영향을 미치는 근본적인 도전 과제입니다. 인간은 자연스럽게 그룹으로 협력하지만, 긴 시간적 범위, 강한 에이전트 간 의존성, 그리고 다양한 그룹 크기로 인해 이러한 상호작용을 모델링하는 것은 여전히 어렵습니다. 기존의 모션 생성 방법은 대부분 작업별로 특화되어 있으며 유연한 다중 에이전트 생성으로 일반화되지 않습니다. 우리는 MAGNet(Multi-Agent Generative Network)을 소개합니다. 이는 통합된 자기회귀 확산 프레임워크로, 유연한 조건화와 샘플링을 통해 다양한 상호작용 작업을 지원합니다. MAGNet은 단일 모델 내에서 이인칭 및 다인칭 예측, 파트너 인페인팅, 파트너 예측, 에이전트 생성을 모두 수행하며, 수백 개의 모션 단계에 걸친 초장기 시퀀스를 자기회귀적으로 생성할 수 있습니다. 우리는 자기회귀 잡음 제거 과정에서 에이전트 간 결합을 명시적으로 모델링하여 에이전트 간의 일관된 조정을 가능하게 합니다. 그 결과, MAGNet은 긴밀하게 동기화된 활동(예: 춤, 복싱)과 느슨하게 구조화된 사회적 상호작용을 모두 포착합니다. 우리의 접근 방식은 이인칭 벤치마크에서 특화된 방법과 동등한 성능을 보이면서도 세 명 이상의 상호작용하는 사람들이 포함된 다인칭 시나리오로 자연스럽게 확장됩니다. 생성된 상호작용의 시간적 역학과 공간적 조정이 가장 잘 드러나는 보충 비디오를 시청해 주시기 바랍니다. 프로젝트 페이지: https://von31.github.io/MAGNet/

## 핵심 내용
다중 인물 상호작용을 이해하고 생성하는 것은 로보틱스와 사회 컴퓨팅에 광범위한 영향을 미치는 근본적인 도전 과제입니다. 인간은 자연스럽게 그룹으로 협력하지만, 긴 시간적 범위, 강한 에이전트 간 의존성, 그리고 다양한 그룹 크기로 인해 이러한 상호작용을 모델링하는 것은 여전히 어렵습니다. 기존의 모션 생성 방법은 대부분 작업별로 특화되어 있으며 유연한 다중 에이전트 생성으로 일반화되지 않습니다. 우리는 MAGNet(Multi-Agent Generative Network)을 소개합니다. 이는 통합된 자기회귀 확산 프레임워크로, 유연한 조건화와 샘플링을 통해 다양한 상호작용 작업을 지원합니다. MAGNet은 단일 모델 내에서 이인칭 및 다인칭 예측, 파트너 인페인팅, 파트너 예측, 에이전트 생성을 모두 수행하며, 수백 개의 모션 단계에 걸친 초장기 시퀀스를 자기회귀적으로 생성할 수 있습니다. 우리는 자기회귀 잡음 제거 과정에서 에이전트 간 결합을 명시적으로 모델링하여 에이전트 간의 일관된 조정을 가능하게 합니다. 그 결과, MAGNet은 긴밀하게 동기화된 활동(예: 춤, 복싱)과 느슨하게 구조화된 사회적 상호작용을 모두 포착합니다. 우리의 접근 방식은 이인칭 벤치마크에서 특화된 방법과 동등한 성능을 보이면서도 세 명 이상의 상호작용하는 사람들이 포함된 다인칭 시나리오로 자연스럽게 확장됩니다. 생성된 상호작용의 시간적 역학과 공간적 조정이 가장 잘 드러나는 보충 비디오를 시청해 주시기 바랍니다. 프로젝트 페이지: https://von31.github.io/MAGNet/

## 参考
- http://arxiv.org/abs/2512.17900v2
