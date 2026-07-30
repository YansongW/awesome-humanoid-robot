---
$id: ent_paper_think_proprioceptively_state_g_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
  zh: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
  ko: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies'
summary:
  en: 'arXiv:2602.06575v2 Announce Type: replace Abstract: Vision-language-action (VLA) models typically inject proprioception
    only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual
    attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly
    with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence
    while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance
    essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects
    which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors
    as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D.
    Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving
    the matched full-token baseline.'
  zh: ThinkProprio 是一种将本体感觉离散化为 VLM 词汇令牌并与指令共同引导视觉注意力选择的 VLA 策略。该方法由研究团队提出，核心贡献在于将本体感觉从被动条件信号转变为主动查询，仅保留约 12% 的视觉令牌即可在 CALVIN
    ABC→D 上超越全令牌基线，同时降低端到端推理延迟。
  ko: 'arXiv:2602.06575v2 Announce Type: replace Abstract: Vision-language-action (VLA) models typically inject proprioception
    only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual
    attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly
    with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence
    while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance
    essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects
    which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors
    as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D.
    Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving
    the matched full-token baseline.'
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
- robotics
- think_proprioceptively
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06575v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Think Proprioceptively: State-Grounded Visual Token Selection for VLA Policies (arXiv)'
  url: https://arxiv.org/abs/2602.06575
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
现有 VLA 模型通常将本体感觉作为后期条件信号注入，这限制了机器人状态对指令理解或视觉注意力的引导作用。ThinkProprio 通过将本体感觉离散化为 VLM 词汇令牌，并与指令联合用于视觉补丁的门控选择，在 VLM 计算前引导模型关注与动作相关的证据并丢弃冗余令牌。实验表明，被动条件信号的本体感觉几乎不影响性能，而令牌形式的状态作为主动查询时才能发挥价值。系统消融实验显示，VLM 词汇令牌作为状态编码优于学习型投影器，仅保留约 12% 的视觉令牌即可在 CALVIN ABC→D 上超越全令牌基线。在 CALVIN、LIBERO 和真实世界操作任务中，ThinkProprio 在提升性能的同时降低了端到端推理延迟。

## 核心内容
### 方法
- **核心思想**：将本体感觉（如关节角度、末端执行器位姿）离散化为 VLM 词汇表中的令牌，与自然语言指令共同作为主动查询，在 VLM 计算前对视觉补丁进行门控选择。
- **状态编码**：使用 VLM 词汇令牌（而非学习型投影器）编码本体感觉，消融实验证明该方式更优。
- **令牌选择机制**：仅保留约 12% 的视觉令牌，在 CALVIN ABC→D 任务上性能超越全令牌基线。

### 实验设置
- **基准测试**：CALVIN（ABC→D 设置）、LIBERO（多个任务）、真实世界操作。
- **基线对比**：匹配的全令牌基线（即处理所有视觉令牌的 VLA 模型）。
- **关键指标**：任务成功率、端到端推理延迟。

### 关键结果
- **性能提升**：在 CALVIN ABC→D 上，仅保留 12% 视觉令牌的 ThinkProprio 超越全令牌基线。
- **延迟降低**：在所有测试场景中，端到端推理延迟均低于全令牌基线。
- **消融实验**：VLM 词汇令牌作为状态编码优于学习型投影器；被动条件信号的本体感觉几乎不改变性能。

### 结论
ThinkProprio 通过将本体感觉转化为主动查询令牌，有效引导 VLM 关注动作相关视觉信息，在减少计算开销的同时提升任务性能，验证了状态引导视觉注意力选择的可行性。

## Overview
Vision-language-action (VLA) models typically inject proprioception only as a late conditioning signal, preventing robot state from grounding instruction understanding or directing visual attention. We introduce ThinkProprio, which discretizes proprioception into VLM-vocabulary tokens and uses them jointly with the instruction to gate visual patches before VLM computation, steering the model toward action-relevant evidence while discarding redundant tokens early. We find that proprioception added as a passive conditioning signal leaves performance essentially unchanged; its value emerges when token-form state acts as an active query that, with the instruction, selects which visual patches the VLM processes. Systematic ablations show that VLM-vocabulary tokens outperform learned projectors as the state encoding, and that retaining only about \SI{12}{\percent} of the visual tokens surpasses on CALVIN ABC$\to$D. Across CALVIN, LIBERO, and real-world manipulation, ThinkProprio reduces end-to-end inference latency while improving the matched full-token baseline.

## 개요
Vision-language-action (VLA) 모델은 일반적으로 고유 감각(proprioception)을 단순히 후기 조건화 신호(late conditioning signal)로만 주입하여, 로봇 상태가 명령 이해를 근거하거나 시각적 주의를 유도하지 못하게 합니다. 우리는 ThinkProprio를 소개합니다. 이는 고유 감각을 VLM 어휘 토큰(VLM-vocabulary tokens)으로 이산화하고, 이를 명령과 함께 사용하여 VLM 계산 전에 시각 패치를 게이팅(gating)함으로써, 모델이 행동 관련 증거에 집중하고 중복 토큰을 조기에 폐기하도록 유도합니다. 우리는 고유 감각이 수동적 조건화 신호로 추가될 때 성능이 거의 변하지 않음을 발견했습니다. 그 가치는 토큰 형태의 상태가 명령과 함께 VLM이 처리할 시각 패치를 선택하는 능동적 질의(active query)로 작용할 때 나타납니다. 체계적 절제 실험(systematic ablations)은 VLM 어휘 토큰이 학습된 프로젝터(learned projectors)보다 상태 인코딩으로 더 우수하며, 시각 토큰의 약 \SI{12}{\percent}만 유지해도 CALVIN ABC$\to$D에서 더 나은 성능을 보임을 입증합니다. CALVIN, LIBERO 및 실제 세계 조작 작업에서 ThinkProprio는 일치하는 전체 토큰 기준선(matched full-token baseline)을 개선하면서 종단 간 추론 지연 시간(end-to-end inference latency)을 줄입니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 일반적으로 고유 감각(proprioception)을 단순히 후기 조건화 신호(late conditioning signal)로만 주입하여, 로봇 상태가 명령 이해를 근거하거나 시각적 주의를 유도하지 못하게 합니다. 우리는 ThinkProprio를 소개합니다. 이는 고유 감각을 VLM 어휘 토큰(VLM-vocabulary tokens)으로 이산화하고, 이를 명령과 함께 사용하여 VLM 계산 전에 시각 패치를 게이팅(gating)함으로써, 모델이 행동 관련 증거에 집중하고 중복 토큰을 조기에 폐기하도록 유도합니다. 우리는 고유 감각이 수동적 조건화 신호로 추가될 때 성능이 거의 변하지 않음을 발견했습니다. 그 가치는 토큰 형태의 상태가 명령과 함께 VLM이 처리할 시각 패치를 선택하는 능동적 질의(active query)로 작용할 때 나타납니다. 체계적 절제 실험(systematic ablations)은 VLM 어휘 토큰이 학습된 프로젝터(learned projectors)보다 상태 인코딩으로 더 우수하며, 시각 토큰의 약 \SI{12}{\percent}만 유지해도 CALVIN ABC$\to$D에서 더 나은 성능을 보임을 입증합니다. CALVIN, LIBERO 및 실제 세계 조작 작업에서 ThinkProprio는 일치하는 전체 토큰 기준선(matched full-token baseline)을 개선하면서 종단 간 추론 지연 시간(end-to-end inference latency)을 줄입니다.

## 参考
- http://arxiv.org/abs/2602.06575v2
