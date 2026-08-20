---
$id: ent_paper_ace_agentic_control_for_embodi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning'
  zh: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning'
  ko: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning'
summary:
  en: 'arXiv:2607.04162v1 Announce Type: new Abstract: Open-ended tabletop manipulation requires agents to not only understand
    natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied
    Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than
    relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills:
    a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning and physical control,
    the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask specifies the target object
    and destination, is tracked over time, exposed for human verification, and ultimately passed to a task-agnostic downstream
    policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale memory. After an action
    is executed, the system automatically verifies whether the intended sub-goal succeeded, using the outcome to advance,
    retry, repair, or replan. This enables online adaptation to user corrections, scene changes, and physical failures. We
    evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation formation with number cubes
    and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization on novel semantic constraints
    and randomized tabletop scenes without task-specific retraining. Specifically, while standard end-to-end baselines struggle
    to complete these logically demanding tasks, ACE achieves a 50% success rate in equation formation and a 70% success rate
    in constraint retrieval. This contrast demonstrates that explicit workflow reasoning and mask-mediated control offer a
    robust, practical route toward adaptable robotic manipulation.'
  zh: ACE 是一个零样本工作流推理框架，用于桌面拾放操作的机器人控制。它由研究团队提出，核心贡献在于将智能体工作流推理与视觉接地接口和可复用拾放原语结合，并通过掩码介导的视觉-动作接口实现语义推理与物理控制的桥接。ACE 在逻辑复杂的长期任务中实现了
    50% 的等式形成成功率和 70% 的约束检索成功率，展示了无需任务特定重训练的零样本泛化能力。
  ko: 'arXiv:2607.04162v1 Announce Type: new Abstract: Open-ended tabletop manipulation requires agents to not only understand
    natural language but also adapt to dynamic environments and execution failures. We present ACE (Agentic Control for Embodied
    Manipulation), a zero-shot workflow reasoning framework for tabletop pick-and-place from natural language. Rather than
    relying on direct low-level action mapping, ACE combines agentic workflow reasoning with two robot-facing executable skills:
    a visual grounding interface and a reusable pick-and-place primitive. To bridge semantic reasoning and physical control,
    the active sub-goal is grounded into a mask-mediated vision-action interface. This unified mask specifies the target object
    and destination, is tracked over time, exposed for human verification, and ultimately passed to a task-agnostic downstream
    policy for execution. Crucially, ACE operates in a closed loop supported by a multi-timescale memory. After an action
    is executed, the system automatically verifies whether the intended sub-goal succeeded, using the outcome to advance,
    retry, repair, or replan. This enables online adaptation to user corrections, scene changes, and physical failures. We
    evaluate ACE on logically complex, long-horizon tasks, including zero-shot multi-step equation formation with number cubes
    and constraint-based object retrieval. ACE demonstrates task-level zero-shot generalization on novel semantic constraints
    and randomized tabletop scenes without task-specific retraining. Specifically, while standard end-to-end baselines struggle
    to complete these logically demanding tasks, ACE achieves a 50% success rate in equation formation and a 70% success rate
    in constraint retrieval. This contrast demonstrates that explicit workflow reasoning and mask-mediated control offer a
    robust, practical route toward adaptable robotic manipulation.'
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
- ace
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04162v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (800 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'ACE: Agentic Control for Embodied Manipulation via Zero-shot Workflow Reasoning (arXiv)'
  url: https://arxiv.org/abs/2607.04162
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述

ACE 提出将开放式操作重构为“工作流推理”问题，而非逐任务策略学习。系统由智能体规划器（Qwen3.6-35B-A3B 驱动）生成零样本语义子目标序列，并通过两个外部技能（掩码介导接口与可复用拾放原语）解耦高层推理与低层物理控制。核心贡献在于证明任务级零样本泛化可通过纯空间掩码表征与在线重规划实现，在语义公式组装与约束检索任务上显著超越端到端 VLA 基线。

## 它改变了什么

传统具身操作研究将每个新任务视为策略学习问题，导致在目标变化时需重新收集演示数据。ACE 真正改变的是问题定义本身：它主张开放式操作的核心瓶颈不在运动控制，而在工作流推理——即如何将自然语言指令分解为可执行的语义子目标序列，并在执行失败时动态重规划。这一转变将下游策略从“理解任务”中解放出来，使其仅需掌握通用的掩码条件拾放原语，从而将任务级泛化从数据驱动转向推理驱动。

该框架同时挑战了端到端 VLA 范式的假设。作者通过实验表明，在低数据机制（约一小时演示）下，ACT 与 π0.5 在长时程组合任务上完全失败（SR 为 0.0%），而 ACE 通过显式工作流分解与人工验证机制，将成功率提升至 50.0%–70.0%。这暗示语言到动作的直接映射可能缺乏组合推理所需的符号操作能力，而模块化架构能更有效地利用有限数据。

## 方法拆解

### 工作流生成与重规划
给定指令 \( u \) 与上下文 \( c \)，规划器生成零样本工作流 \( W = \mathcal{P}(u,c) = (w_1, \dots, w_K) \)，每步 \( w_k \) 为显式语义子目标（如“拾取数字 3 立方体”）。执行中支持重规划 \( W' = \mathcal{R}(W, \Delta) \)，其中 \( \Delta \) 包含新观察、用户反馈或执行结果；重规划可为局部（修改活动子目标接地）或全局（重新生成剩余工作流）。

### 掩码介导接口
对活动步骤 \( w_k \)，预测视觉目标 \( M_k = \mathcal{G}(w_k, I_t, m_t) \)，其中 \( M_k \in \{0,127,255\}^{H \times W} \) 为 8 位灰度掩码：127 表示拾取目标，255 表示放置目标，0 为背景。该掩码经历三阶段：
1. **人工验证**：执行前渲染给用户批准；
2. **持久跟踪**：初始化跟踪器 \( T_k = \mathcal{T}_{\text{init}}(I_t, M_k) \) 并持续更新；
3. **任务无关执行**：跟踪掩码直接输入下游 VA 策略。

### 可复用拾放技能
给定子目标 \( w_k \)，接地为掩码 \( M_k \) 后，VA 策略输出动作块 \( \hat{a}_{t:t+K-1} = \pi_{\mathrm{VA}}(I_t, q_t, M_{k,t}) \)，其中 \( K \) 为动作块地平线，\( q_t \) 为本体感知状态。执行后返回报告，使 ACE 能推进、重试、修复掩码或重规划。

### 多时间尺度记忆
包含实时执行记忆（工作流位置、活动掩码）、任务范围语义-视觉记忆（对象名称、别名）、外观参考记忆（图像特征）与对话上下文记忆（有界历史）。验证机制通过计算目标掩码间空间重叠并交叉参考更新视觉观察，发现错误后触发重规划。

### 关键设计决策
解耦推理与物理控制，使下游 VA 策略仅训练于通用掩码条件拾放原语（约一小时演示），不暴露于完整语义任务。纯空间掩码表征过滤环境噪声，提供稳定语义视觉先验，避免策略过拟合原始 RGB 输入。

## 关键创新

1. **工作流推理范式**：首次将开放式操作明确建模为工作流推理而非策略学习，使任务级零样本泛化成为可能。这一抽象将组合推理从物理执行中剥离，允许规划器利用 LLM 的语义能力处理未见任务。

2. **纯空间掩码接口**：仅使用 8 位灰度掩码（127/255）作为视觉表征，完全丢弃原始 RGB 输入。消融显示，掩码+原始图像导致抓取成功率降至 30.0%，而仅掩码达到 90.0%，证明纯空间表征对视觉泛化的关键作用——它迫使策略关注任务相关几何信息，忽略无关纹理与光照变化。

3. **人类在环验证机制**：在执行前渲染掩码供用户批准，将智能体幻觉率显式纳入系统设计。消融显示，去除人工验证使约束检索 SR 从 70.0% 降至 20.0%，GA 从 90.0% 降至 60.0%，量化了人类监督的安全裕度价值。

## 实验与结果

实验在真实 SO-101 臂上评估两个任务：语义公式组装（多步顺序操作）与约束检索（逻辑/数值约束识别）。基线 ACT 与 π0.5 均使用约一小时完整任务演示训练，ACE 的 VA 策略仅训练约一小时通用掩码条件拾放原语。每任务 10 次独立试验，随机化初始配置与指令措辞。

| 任务 | 方法 | 平均 FGS | SR | GA |
|------|------|---------|-----|-----|
| 公式组装 | ACT | 3.2 | 0.0% | – |
| 公式组装 | π0.5 | 3.0 | 0.0% | – |
| 公式组装 | ACE | 17.8 | 50.0% | 90.0% |
| 约束检索 | ACT | – | 0.0% | – |
| 约束检索 | π0.5 | – | 0.0% | – |
| 约束检索 | ACE | – | 70.0% | 90.0% |

消融实验显示：策略级消融中，DP（掩码+原始图像）抓取成功率 30.0%，DP（仅掩码）达 90.0%；系统级消融中，无智能体规划器时两任务 SR 均为 0.0%，无人工验证时公式组装 SR 从 50.0% 降至 30.0%，约束检索从 70.0% 降至 20.0%。结果表明，高层推理与人工验证是任务成功的必要条件，而纯掩码表征是物理执行鲁棒性的核心。

## 边界与局限

论文未明确讨论以下边界：当前系统依赖人类执行前批准，增加交互开销，未探索自动化置信度校准方案。工作流质量受限于规划器推理能力与视觉接地保真度，当掩码不精确或下游策略抓取困难时失败主要源于感知/执行而非认知规划。方法聚焦于拾放操作，未扩展至接触丰富操作（如拧螺丝、插拔）。基线比较限于低数据机制（约一小时演示），扩展 VLA 基线的任务级演示可能提升其性能，但论文未验证。在更复杂的公式组装任务中，推理错误略有增加，但未量化具体比例。

## 工程启示

复现 ACE 时，首先核对掩码接口的像素值约定（127 拾取、255 放置、0 背景）是否与下游 VA 策略的训练数据一致——这是最容易出错处，若策略训练时掩码语义混淆，抓取成功率将急剧下降。其次，人工验证环节不可省略：消融显示去除后约束检索 SR 下降 50 个百分点（由表内 70.0%→20.0% 计算），说明该机制是系统安全裕度的主要来源。硬件部署上，智能体推理引擎需 4×RTX 3090 云服务器，而掩码接口与 VA 策略可单卡运行，需确保两者通信延迟可控。训练数据仅需通用掩码条件拾放演示（约一小时），但需保证演示覆盖随机物体到区域转移的多样性，避免策略对特定物体外观过拟合。最后，重规划逻辑应优先实现局部掩码修复而非全局工作流重生成，因为实验表明多数失败源于接地误差而非任务排序错误。

## 参考
- http://arxiv.org/abs/2607.04162v1

## 개요
ACE 프레임워크는 직접적인 저수준 동작 매핑 대신 에이전트 워크플로 추론을 통해, 시각적 접지 인터페이스와 재사용 가능한 픽앤플레이스 프리미티브를 로봇 실행 가능 스킬로 활용합니다. 마스크 매개 시각-동작 인터페이스를 사용하여 활성 하위 목표를 접지하며, 이 마스크는 대상 객체와 목적지를 지정하고 시간에 따라 추적되며 인간 검증에 노출된 후 최종적으로 작업에 구애받지 않는 하위 정책 실행에 전달됩니다. ACE는 폐루프로 작동하며, 다중 시간 규모 메모리에 의해 지원되어 하위 목표 성공 여부를 자동으로 검증하고 결과에 따라 진행, 재시도, 수리 또는 재계획을 수행하여 사용자 수정, 장면 변화 및 물리적 오류에 온라인으로 적응합니다.

## 핵심 내용
### 방법
ACE 프레임워크의 핵심은 제로샷 워크플로 추론으로, 다음 구성 요소를 결합합니다:
- **에이전트 워크플로 추론**: 자연어 지시를 일련의 하위 목표로 분해하여 워크플로를 형성합니다.
- **로봇 실행 가능 스킬**: 대상 객체와 목적지를 식별하기 위한 시각적 접지 인터페이스와 물리적 조작을 수행하기 위한 재사용 가능한 픽앤플레이스 프리미티브를 포함합니다.
- **마스크 매개 시각-동작 인터페이스**: 활성 하위 목표를 대상 객체와 목적지를 지정하는 통합 마스크에 접지하고, 시간에 따라 추적하며 인간 검증에 노출한 후 최종적으로 작업에 구애받지 않는 하위 정책 실행에 전달합니다.

### 아키텍처
ACE는 다중 시간 규모 메모리에 의해 지원되는 폐루프 아키텍처를 채택합니다:
- **실행 후 검증**: 시스템은 하위 목표 성공 여부를 자동으로 검증하고 결과에 따라 진행, 재시도, 수리 또는 재계획을 수행합니다.
- **온라인 적응**: 사용자 수정, 장면 변화 및 물리적 오류에 대한 온라인 적응을 지원합니다.

### 실험 설정
ACE는 논리적으로 복잡한 장기 작업에서 평가됩니다:
- **제로샷 다단계 등식 형성**: 숫자 큐브를 사용하여 등식을 형성합니다.
- **제약 기반 객체 검색**: 특정 제약 조건에 따라 객체를 검색합니다.

### 주요 수치
- **등식 형성 성공률**: 50%
- **제약 검색 성공률**: 70%
- **비교 기준선**: 표준 종단 간 기준선은 이러한 논리 요구가 높은 작업에서 성능이 저조합니다.

### 결론
ACE는 명시적 워크플로 추론과 마스크 매개 제어가 적응형 로봇 조작을 위한 견고하고 실용적인 경로를 제공함을 보여줍니다. 작업별 재훈련 없이 작업 수준 제로샷 일반화를 달성하며, 새로운 의미론적 제약과 무작위 테이블탑 장면에 적용됩니다.
