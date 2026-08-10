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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.06575v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (915 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.06575v2

## 개요
기존 VLA 모델은 일반적으로 고유수용감각을 후기 조건 신호로 주입하는데, 이는 로봇 상태가 명령 이해나 시각적 주의를 유도하는 역할을 제한합니다. ThinkProprio는 고유수용감각을 VLM 어휘 토큰으로 이산화하고, 명령과 함께 시각 패치의 게이트 선택에 사용하여 VLM 계산 전에 모델이 행동 관련 증거에 주목하고 중복 토큰을 폐기하도록 유도합니다. 실험에 따르면 수동 조건 신호로서의 고유수용감각은 성능에 거의 영향을 미치지 않으며, 토큰 형태의 상태가 능동 쿼리로 사용될 때만 가치를 발휘합니다. 시스템 소거 실험은 학습형 프로젝터보다 VLM 어휘 토큰이 상태 인코딩으로 더 우수하며, 시각 토큰의 약 12%만 유지해도 CALVIN ABC→D에서 전체 토큰 기준선을 능가함을 보여줍니다. CALVIN, LIBERO 및 실제 세계 조작 작업에서 ThinkProprio는 성능을 향상시키면서 엔드투엔드 추론 지연 시간을 줄였습니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: 고유수용감각(관절 각도, 엔드 이펙터 포즈 등)을 VLM 어휘의 토큰으로 이산화하고, 자연어 명령과 함께 능동 쿼리로 사용하여 VLM 계산 전에 시각 패치를 게이트 선택합니다.
- **상태 인코딩**: 학습형 프로젝터 대신 VLM 어휘 토큰으로 고유수용감각을 인코딩하며, 소거 실험을 통해 이 방식이 더 우수함을 입증합니다.
- **토큰 선택 메커니즘**: 시각 토큰의 약 12%만 유지하여 CALVIN ABC→D 작업에서 전체 토큰 기준선보다 성능이 뛰어납니다.

### 실험 설정
- **벤치마크**: CALVIN(ABC→D 설정), LIBERO(다중 작업), 실제 세계 조작.
- **기준선 비교**: 일치하는 전체 토큰 기준선(즉, 모든 시각 토큰을 처리하는 VLA 모델).
- **핵심 지표**: 작업 성공률, 엔드투엔드 추론 지연 시간.

### 핵심 결과
- **성능 향상**: CALVIN ABC→D에서 시각 토큰의 12%만 유지한 ThinkProprio가 전체 토큰 기준선을 능가합니다.
- **지연 시간 감소**: 모든 테스트 시나리오에서 엔드투엔드 추론 지연 시간이 전체 토큰 기준선보다 낮습니다.
- **소거 실험**: VLM 어휘 토큰이 상태 인코딩으로 학습형 프로젝터보다 우수하며, 수동 조건 신호로서의 고유수용감각은 성능을 거의 변화시키지 않습니다.

### 결론
ThinkProprio는 고유수용감각을 능동 쿼리 토큰으로 변환하여 VLM이 행동 관련 시각 정보에 주목하도록 효과적으로 유도하고, 계산 오버헤드를 줄이면서 작업 성능을 향상시켜 상태 기반 시각 주의 선택의 가능성을 검증합니다.
