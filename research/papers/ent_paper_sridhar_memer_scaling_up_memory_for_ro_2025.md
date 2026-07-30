---
$id: ent_paper_sridhar_memer_scaling_up_memory_for_ro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval'
  zh: MemER
  ko: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval'
summary:
  en: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
  zh: MemER 是斯坦福大学于 2025 年提出的一种大型视觉-语言-动作模型，旨在通过经验检索为机器人控制扩展记忆能力。其核心贡献在于设计了一个分层策略框架，其中高层策略从历史经验中选择并跟踪相关关键帧，以生成文本指令供低层策略执行，从而高效处理长时域依赖。实验表明，MemER
    在需要数分钟记忆的三个真实世界长时域机器人操作任务上优于先前方法。
  ko: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
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
- memer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.20328v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (arXiv)'
  url: https://arxiv.org/abs/2510.20328
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MemER source
  url: https://doi.org/10.48550/arXiv.2510.20328
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人类在执行任务时通常依赖记忆，但大多数机器人策略缺乏这一能力。直接基于长观测历史进行条件化计算成本高且易受协变量偏移影响，而随意对历史进行子采样则会导致信息冗余或无关。为此，MemER 提出了一种分层策略框架：高层策略负责从经验中选择并跟踪相关关键帧，结合最新帧生成文本指令；低层策略则执行这些指令。该设计兼容现有视觉-语言-动作模型，并能在长时域依赖上高效推理。在实验中，研究者分别使用 Qwen2.5-VL-7B-Instruct 和 π₀.₅ 作为高层和低层策略进行微调，并辅以最小语言标注的演示数据。

## 核心内容
### 方法
- **分层策略框架**：高层策略（基于 Qwen2.5-VL-7B-Instruct）从历史经验中检索并跟踪相关关键帧，结合最新帧生成文本指令；低层策略（基于 π₀.₅）执行这些指令。
- **关键帧选择**：高层策略通过训练学会选择与当前任务相关的历史帧，避免计算冗余或无关信息。
- **兼容性**：该设计可直接适配现有视觉-语言-动作模型，无需修改底层架构。

### 实验设置
- **模型微调**：使用 Qwen2.5-VL-7B-Instruct 作为高层策略，π₀.₅ 作为低层策略，均通过演示数据（辅以最小语言标注）进行微调。
- **任务**：三个真实世界长时域机器人操作任务，每个任务需要数分钟的记忆跨度。
- **对比基线**：包括直接基于长历史条件化的方法以及随机子采样历史的方法。

### 关键结果
- MemER 在所有三个任务上均优于先前方法，尤其在需要长时间记忆的场景中表现显著。
- 高层策略的关键帧选择机制有效减少了计算开销，同时提升了任务成功率。
- 与直接使用完整历史相比，MemER 在协变量偏移下更具鲁棒性。

### 结论
MemER 通过经验检索实现了机器人策略的长期记忆扩展，其分层设计在保持计算效率的同时提升了长时域任务性能。代码和视频已开源。

## Overview
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## 개요
인간은 작업을 수행할 때 일상적으로 기억에 의존하지만, 대부분의 로봇 정책에는 이러한 능력이 부족합니다. 본 연구의 목표는 로봇 정책에 동일한 능력을 부여하는 것입니다. 긴 관찰 이력을 단순히 조건화하는 것은 계산 비용이 많이 들고 공변량 이동(covariate shift)에 취약하며, 이력을 무분별하게 서브샘플링하면 관련 없거나 중복된 정보가 발생합니다. 우리는 계층적 정책 프레임워크를 제안합니다. 여기서 상위 수준 정책은 경험에서 이전의 관련 키프레임을 선택하고 추적하도록 훈련됩니다. 상위 수준 정책은 하위 수준 정책이 실행할 텍스트 명령을 생성할 때 선택된 키프레임과 가장 최근 프레임을 사용합니다. 이 설계는 기존의 시각-언어-행동(VLA) 모델과 호환되며, 시스템이 장기 의존성을 효율적으로 추론할 수 있게 합니다. 실험에서 우리는 Qwen2.5-VL-7B-Instruct와 $π_{0.5}$를 각각 상위 수준 및 하위 수준 정책으로 미세 조정했으며, 최소한의 언어 주석이 추가된 시연 데이터를 사용했습니다. 우리의 접근 방식인 MemER는 수 분의 기억을 필요로 하는 세 가지 실제 장기 로봇 조작 작업에서 이전 방법보다 뛰어난 성능을 보였습니다. 비디오와 코드는 https://jen-pan.github.io/memer/에서 확인할 수 있습니다.

## 핵심 내용
인간은 작업을 수행할 때 일상적으로 기억에 의존하지만, 대부분의 로봇 정책에는 이러한 능력이 부족합니다. 본 연구의 목표는 로봇 정책에 동일한 능력을 부여하는 것입니다. 긴 관찰 이력을 단순히 조건화하는 것은 계산 비용이 많이 들고 공변량 이동(covariate shift)에 취약하며, 이력을 무분별하게 서브샘플링하면 관련 없거나 중복된 정보가 발생합니다. 우리는 계층적 정책 프레임워크를 제안합니다. 여기서 상위 수준 정책은 경험에서 이전의 관련 키프레임을 선택하고 추적하도록 훈련됩니다. 상위 수준 정책은 하위 수준 정책이 실행할 텍스트 명령을 생성할 때 선택된 키프레임과 가장 최근 프레임을 사용합니다. 이 설계는 기존의 시각-언어-행동(VLA) 모델과 호환되며, 시스템이 장기 의존성을 효율적으로 추론할 수 있게 합니다. 실험에서 우리는 Qwen2.5-VL-7B-Instruct와 $π_{0.5}$를 각각 상위 수준 및 하위 수준 정책으로 미세 조정했으며, 최소한의 언어 주석이 추가된 시연 데이터를 사용했습니다. 우리의 접근 방식인 MemER는 수 분의 기억을 필요로 하는 세 가지 실제 장기 로봇 조작 작업에서 이전 방법보다 뛰어난 성능을 보였습니다. 비디오와 코드는 https://jen-pan.github.io/memer/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2510.20328v1
