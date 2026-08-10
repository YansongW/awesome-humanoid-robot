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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17900v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (820 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.17900v2

## 개요
MAGNet은 다중 에이전트 상호작용 모델링에서 시간 범위가 길고, 에이전트 의존성이 강하며, 그룹 규모가 가변적인 문제를 해결하기 위해 통합된 자기회귀 확산 프레임워크를 제안한다. 이 프레임워크는 유연한 조건 설정과 샘플링을 통해 단일 모델에서 쌍(pair) 및 다중 인물 예측, 파트너 보완, 에이전트 생성 등 다양한 상호작용 작업을 지원하며, 수백 단계에 달하는 초장기 시퀀스를 자기회귀적으로 생성할 수 있다. 핵심 혁신은 자기회귀 노이즈 제거 과정에서 에이전트 간 결합을 명시적으로 모델링하여 춤, 권투와 같은 긴밀하게 동기화된 활동과 느슨한 구조의 사회적 상호작용을 생성하는 데 있다. 실험 결과, MAGNet은 쌍(pair) 벤치마크에서 전용 방법과 동등한 성능을 달성했으며, 3인 이상 시나리오로 자연스럽게 확장된다.

## 핵심 내용
### 방법 아키텍처
MAGNet은 자기회귀 확산 프레임워크를 기반으로 다중 에이전트 모션 생성을 시퀀스 조건부 생성 문제로 모델링한다. 핵심 설계는 다음과 같다:
- **통합 프레임워크**: 유연한 조건 설정과 샘플링을 통해 단일 모델에서 쌍(pair) 예측, 다중 인물 예측, 파트너 보완, 파트너 예측, 에이전트 생성 등 다양한 작업을 지원한다.
- **에이전트 결합 모델링**: 자기회귀 노이즈 제거 과정에서 에이전트 간 의존 관계를 명시적으로 모델링하여 생성된 동작의 조정성을 보장한다.
- **초장기 시퀀스 생성**: 수백 단계에 달하는 모션 시퀀스를 자기회귀적으로 생성하여 긴 시간 범위의 상호작용을 포괄한다.

### 실험 설정
- **벤치마크 테스트**: 쌍(pair) 상호작용 벤치마크(춤, 권투 등)에서 평가하고 전용 방법과 비교한다.
- **확장 시나리오**: 3인 이상 시나리오로 자연스럽게 확장하여 프레임워크의 일반화 능력을 검증한다.
- **평가 지표**: 생성된 동작의 시간적 역학과 공간적 조정성에 중점을 두며, 보충 비디오를 통해 효과를 시연한다.

### 주요 결과
- **성능**: 쌍(pair) 벤치마크에서 전용 방법과 동등한 성능을 달성하며, 작업별 조정이 필요 없다.
- **일반화 능력**: 3인 이상 시나리오를 성공적으로 처리하며, 긴밀하게 동기화된 활동(춤, 권투 등)과 느슨한 구조의 사회적 상호작용을 지원한다.
- **시퀀스 길이**: 수백 단계의 초장기 시퀀스 생성을 지원하여 기존 방법의 시간적 한계를 돌파한다.

### 결론
MAGNet은 통합된 자기회귀 확산 프레임워크를 통해 다중 에이전트 상호작용 모델링의 핵심 과제를 해결하며, 로봇 공학 및 사회 컴퓨팅 분야의 다중 인물 모션 생성을 위한 유연하고 확장 가능한 솔루션을 제공한다. 프로젝트 페이지에서는 생성된 상호작용의 시간적 역학과 공간적 조정성을 보여주는 보충 비디오를 제공한다.
