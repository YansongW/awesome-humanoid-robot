---
$id: ent_paper_wang_openha_a_series_of_open_source_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft'
  zh: OpenHA
  ko: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft'
summary:
  en: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (OpenHA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
  zh: OpenHA 是由北京大学提出的 2025 年大型视觉-语言-动作模型系列，专为 Minecraft 中的机器人操作设计。其核心贡献是提出 Chain of Action (CoA) 框架，将高层规划与低层控制统一在单一 VLA 模型中，并通过混合动作空间训练实现新的最优性能。该工作还发布了包含
    800 多个任务的综合基准、数据集、源代码和预训练模型。
  ko: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (OpenHA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University.'
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
- openha
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13347v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (765 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'OpenHA: A Series of Open-Source Hierarchical Agentic Models in Minecraft (arXiv)'
  url: https://arxiv.org/abs/2509.13347
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenHA source
  url: https://doi.org/10.48550/arXiv.2509.13347
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
OpenHA 系统性地比较了 Minecraft 中多种抽象动作空间与分词器，发现没有单一动作空间普遍最优，最佳抽象高度依赖具体任务。为解决这一通用智能体构建困境，作者提出 Chain of Action (CoA) 框架，将抽象动作视为中间推理步骤而非独立策略命令，类似思维链引导最终可执行动作生成。实验表明，基于 CoA 范式在多样化动作空间上训练的 All-in-One 智能体，其策略更鲁棒且泛化性更强，在整体任务成功率上超越了强专用基线，达到新最优水平。

## 核心内容
### 核心问题与动机
- 动作空间选择是开发端到端可训练智能体的关键未解难题，尤其在开放世界 Minecraft 中。
- 现有 VLA 或分层智能体模型依赖特定抽象动作空间，但缺乏系统性比较。

### 方法：Chain of Action (CoA)
- CoA 将高层规划与低层控制统一在单一 VLA 模型中，抽象动作不再作为独立策略的命令，而是作为中间推理步骤（类似 chain of thought），引导最终可执行动作的生成。
- 该框架允许智能体在推理时动态调整动作抽象层级，无需预定义分层结构。

### 实验设置与关键数字
- 构建了包含 800 多个不同任务的综合基准，覆盖多种动作空间（如离散、连续、混合）。
- 训练 All-in-One 智能体时，混合使用多种动作空间数据，基于 CoA 范式进行联合训练。
- 结果：该统一智能体在整体任务成功率上超越强专用基线，达到新最优水平（具体数字需参考原文，但摘要未提供精确数值）。

### 开源资源
- 发布 OpenHA 套件，包括基准、数据集、源代码和所有预训练模型检查点，地址：https://github.com/CraftJarvis/OpenHA。

## Overview
The choice of action spaces is a critical yet unresolved challenge in developing capable, end-to-end trainable agents. This paper first presents a large-scale, systematic comparison of prominent abstracted action spaces and tokenizers for Vision-Language-Action (VLA) or hierarchical agent models in the open-ended Minecraft. Our analysis reveals that no single action space is universally optimal; instead, the most effective abstraction is highly task-dependent, creating a dilemma for building generalist agents. To resolve this, we introduce Chain of Action (CoA), a novel framework that unifies high-level planning and low-level control within a single, monolithic VLA model. CoA treats an abstracted action not as a command for a separate policy, but as an intermediate reasoning step--akin to a chain of thought--that guides the generation of the final, executable action. Furthermore, we demonstrate that an All-in-One agent trained on a diverse mixture of action spaces using the CoA paradigm learns a more robust and generalizable policy. This unified agent achieves a new state-of-the-art, improving the overall task success rate over strong, specialized baselines. To foster reproducible research, we release the OpenHA (Open Hierarchical Agents) suite, which includes our comprehensive benchmark of over 800 distinct tasks, curated datasets, source code, and all pretrained model checkpoints at https://github.com/CraftJarvis/OpenHA

## 参考
- http://arxiv.org/abs/2509.13347v1

## 개요
OpenHA는 Minecraft에서 다양한 추상 행동 공간과 토크나이저를 체계적으로 비교하여, 단일 행동 공간이 보편적으로 최적이 아니며 최상의 추상화가 특정 작업에 크게 의존한다는 것을 발견했습니다. 이러한 범용 에이전트 구축의 난제를 해결하기 위해 저자들은 Chain of Action (CoA) 프레임워크를 제안합니다. 이는 추상 행동을 독립적인 정책 명령이 아닌 중간 추론 단계로 간주하며, 사고의 사슬(chain of thought)과 유사하게 최종 실행 가능한 행동 생성을 유도합니다. 실험 결과, CoA 패러다임을 기반으로 다양한 행동 공간에서 훈련된 All-in-One 에이전트는 더 강건하고 일반화 가능한 정책을 보여주며, 전체 작업 성공률에서 강력한 전용 베이스라인을 능가하여 새로운 최적 수준에 도달했습니다.

## 핵심 내용
### 핵심 문제 및 동기
- 행동 공간 선택은 엔드투엔드 훈련 가능한 에이전트 개발의 핵심 미해결 과제이며, 특히 개방형 세계 Minecraft에서 두드러집니다.
- 기존 VLA 또는 계층적 에이전트 모델은 특정 추상 행동 공간에 의존하지만, 체계적인 비교가 부족합니다.

### 방법: Chain of Action (CoA)
- CoA는 고수준 계획과 저수준 제어를 단일 VLA 모델에 통합하며, 추상 행동은 독립적인 정책 명령이 아닌 중간 추론 단계(사고의 사슬과 유사)로 작용하여 최종 실행 가능한 행동 생성을 안내합니다.
- 이 프레임워크는 에이전트가 추론 시 행동 추상화 수준을 동적으로 조정할 수 있게 하며, 사전 정의된 계층 구조가 필요 없습니다.

### 실험 설정 및 주요 수치
- 800개 이상의 다양한 작업을 포함하는 종합 벤치마크를 구축했으며, 여러 행동 공간(예: 이산, 연속, 혼합)을 포괄합니다.
- All-in-One 에이전트 훈련 시 여러 행동 공간 데이터를 혼합하고 CoA 패러다임을 기반으로 공동 훈련을 수행합니다.
- 결과: 이 통합 에이전트는 전체 작업 성공률에서 강력한 전용 베이스라인을 능가하여 새로운 최적 수준에 도달했습니다(구체적인 수치는 원문 참조 필요, 초록에는 정확한 값이 제공되지 않음).

### 오픈소스 리소스
- OpenHA 스위트를 공개하며, 벤치마크, 데이터셋, 소스 코드 및 모든 사전 훈련된 모델 체크포인트를 포함합니다. 주소: https://github.com/CraftJarvis/OpenHA.
