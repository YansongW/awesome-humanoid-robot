---
$id: ent_paper_shi_memoryvla_perceptual_cognitive_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation'
  zh: MemoryVLA
  ko: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation'
summary:
  en: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (MemoryVLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Dexmal, MEGVII Technology,
    Tianjin University, Harbin Institute of Technology, StepFun.'
  zh: MemoryVLA 是由清华大学、Dexmal、MEGVII Technology、天津大学、哈尔滨工业大学及 StepFun 联合提出的 2025 年大型视觉-语言-动作模型，专为机器人操作设计。其核心贡献在于引入基于认知科学的感知-认知记忆机制，通过工作记忆与长期记忆库的协同，解决传统
    VLA 模型在长时域任务中的时序依赖问题。在 SimplerEnv-Bridge、Fractal、LIBERO-5 及 Mikasa-Robo 基准上分别取得 71.9%、72.7%、96.5% 和 41.2% 的成功率，均超越当前最优基线
    CogACT 和 pi-0。
  ko: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (MemoryVLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Dexmal, MEGVII Technology,
    Tianjin University, Harbin Institute of Technology, StepFun.'
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
- memoryvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19236v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.19236
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MemoryVLA source
  url: https://doi.org/10.48550/arXiv.2508.19236
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MemoryVLA 提出了一种认知-记忆-动作框架，模仿人类工作记忆与海马体系统的协作方式。它利用预训练视觉语言模型将观测编码为感知与认知令牌，形成工作记忆；同时通过感知-认知记忆库存储低层细节与高层语义。工作记忆从库中检索决策相关条目，与当前令牌自适应融合，并通过合并冗余更新记忆库。最终，记忆条件化的扩散动作专家生成时序感知的动作序列。该模型在 150 多项仿真与真实世界任务中验证，涵盖三种机器人平台，在长时域任务上相比基线提升显著。

## 核心内容
### 方法架构
- **认知-记忆-动作框架**：基于认知科学中工作记忆与海马体系统的双存储机制设计。
- **工作记忆**：由预训练 VLM 编码当前观测生成的感知令牌（低层细节）与认知令牌（高层语义）构成，用于即时控制。
- **感知-认知记忆库**：从工作记忆整合并存储低层细节与高层语义，形成长期记忆。
- **记忆检索与融合**：工作记忆从库中检索决策相关条目，通过自适应融合机制与当前令牌结合，并合并冗余以更新库。
- **动作生成**：记忆条件化的扩散动作专家利用融合后的令牌生成时序感知的动作序列。

### 实验设置
- **仿真任务**：在 SimplerEnv-Bridge、Fractal、LIBERO-5 及 Mikasa-Robo 四个基准上评估，涵盖 150 多项任务。
- **真实世界任务**：12 项任务，包括通用技能与长时域时序依赖任务。
- **机器人平台**：三种不同机器人。
- **基线模型**：对比 CogACT 和 pi-0 等当前最优模型。

### 关键结果
- **仿真性能**：
  - SimplerEnv-Bridge：71.9% 成功率，相比基线 CogACT 提升 +14.6。
  - Fractal：72.7% 成功率。
  - LIBERO-5：96.5% 成功率。
  - Mikasa-Robo：41.2% 成功率，相比基线 pi-0 提升 +11.8。
- **真实世界性能**：
  - 12 项任务平均成功率 84.0%。
  - 长时域任务相比基线提升 +26。
- **结论**：MemoryVLA 通过显式建模时序记忆，显著提升了长时域机器人操作任务的性能，验证了认知启发记忆机制在 VLA 模型中的有效性。

## Overview
Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and semantic gist of past experience for long-term memory. Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation. A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and high-level semantics consolidated from it. Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies. Using these tokens, a memory-conditioned diffusion action expert yields temporally aware action sequences. We evaluate MemoryVLA on 150+ simulation and real-world tasks across three robots. On SimplerEnv-Bridge, Fractal, LIBERO-5 suites and Mikasa-Robo, it achieves 71.9%, 72.7%, 96.5%, and 41.2% success rates, respectively, all outperforming state-of-the-art baselines CogACT and pi-0, with a notable +14.6 gain on Bridge and +11.8 gain on Mikasa-Robo. On 12 real-world tasks spanning general skills and long-horizon temporal dependencies, MemoryVLA achieves 84.0% success rate, with long-horizon tasks showing a +26 improvement over state-of-the-art baseline. Project Page: https://shihao1895.github.io/MemoryVLA

## 개요
로봇 조작 작업은 본질적으로 비마르코프적이기 때문에 시간적 맥락이 필수적이지만, 주류 VLA 모델은 일반적으로 이를 간과하고 장기적이고 시간 의존적인 작업에 어려움을 겪습니다. 인지 과학에 따르면 인간은 즉각적인 제어를 위해 단기적인 표현을 버퍼링하는 작업 기억에 의존하는 반면, 해마 시스템은 장기 기억을 위해 과거 경험의 축어적 에피소드 세부 사항과 의미적 요지를 보존합니다. 이러한 메커니즘에서 영감을 받아, 우리는 장기 로봇 조작을 위한 MemoryVLA, 즉 인지-기억-행동 프레임워크를 제안합니다. 사전 훈련된 VLM은 관찰을 작업 기억을 형성하는 지각 및 인지 토큰으로 인코딩하는 반면, 지각-인지 메모리 뱅크는 여기에서 통합된 저수준 세부 사항과 고수준 의미를 저장합니다. 작업 기억은 뱅크에서 의사 결정 관련 항목을 검색하고, 이를 현재 토큰과 적응적으로 융합하며, 중복을 병합하여 뱅크를 업데이트합니다. 이러한 토큰을 사용하여, 메모리 조건부 확산 행동 전문가가 시간 인식 행동 시퀀스를 생성합니다. 우리는 세 대의 로봇에 걸쳐 150개 이상의 시뮬레이션 및 실제 작업에서 MemoryVLA를 평가합니다. SimplerEnv-Bridge, Fractal, LIBERO-5 제품군 및 Mikasa-Robo에서 각각 71.9%, 72.7%, 96.5%, 41.2%의 성공률을 달성하여, 최첨단 기준 모델인 CogACT 및 pi-0을 모두 능가하며, Bridge에서 +14.6, Mikasa-Robo에서 +11.8의 주목할 만한 향상을 보였습니다. 일반 기술과 장기 시간 의존성을 아우르는 12개의 실제 작업에서 MemoryVLA는 84.0%의 성공률을 달성했으며, 장기 작업은 최첨단 기준 모델 대비 +26의 개선을 보였습니다. 프로젝트 페이지: https://shihao1895.github.io/MemoryVLA

## 핵심 내용
로봇 조작 작업은 본질적으로 비마르코프적이기 때문에 시간적 맥락이 필수적이지만, 주류 VLA 모델은 일반적으로 이를 간과하고 장기적이고 시간 의존적인 작업에 어려움을 겪습니다. 인지 과학에 따르면 인간은 즉각적인 제어를 위해 단기적인 표현을 버퍼링하는 작업 기억에 의존하는 반면, 해마 시스템은 장기 기억을 위해 과거 경험의 축어적 에피소드 세부 사항과 의미적 요지를 보존합니다. 이러한 메커니즘에서 영감을 받아, 우리는 장기 로봇 조작을 위한 MemoryVLA, 즉 인지-기억-행동 프레임워크를 제안합니다. 사전 훈련된 VLM은 관찰을 작업 기억을 형성하는 지각 및 인지 토큰으로 인코딩하는 반면, 지각-인지 메모리 뱅크는 여기에서 통합된 저수준 세부 사항과 고수준 의미를 저장합니다. 작업 기억은 뱅크에서 의사 결정 관련 항목을 검색하고, 이를 현재 토큰과 적응적으로 융합하며, 중복을 병합하여 뱅크를 업데이트합니다. 이러한 토큰을 사용하여, 메모리 조건부 확산 행동 전문가가 시간 인식 행동 시퀀스를 생성합니다. 우리는 세 대의 로봇에 걸쳐 150개 이상의 시뮬레이션 및 실제 작업에서 MemoryVLA를 평가합니다. SimplerEnv-Bridge, Fractal, LIBERO-5 제품군 및 Mikasa-Robo에서 각각 71.9%, 72.7%, 96.5%, 41.2%의 성공률을 달성하여, 최첨단 기준 모델인 CogACT 및 pi-0을 모두 능가하며, Bridge에서 +14.6, Mikasa-Robo에서 +11.8의 주목할 만한 향상을 보였습니다. 일반 기술과 장기 시간 의존성을 아우르는 12개의 실제 작업에서 MemoryVLA는 84.0%의 성공률을 달성했으며, 장기 작업은 최첨단 기준 모델 대비 +26의 개선을 보였습니다. 프로젝트 페이지: https://shihao1895.github.io/MemoryVLA

## 参考
- http://arxiv.org/abs/2508.19236v2
