---
$id: ent_paper_wcm_world_cognition_model_generalizable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WCM: World-Cognition Model for Generalizable Human-Robot Interaction'
  zh: 'WCM: World-Cognition Model for Generalizable Human-Robot Interaction'
  ko: 'WCM: World-Cognition Model for Generalizable Human-Robot Interaction'
summary:
  en: Language agents can now interact fluently with users in software, but robots still struggle to bring comparable interaction
    to physical tasks. Current robot-control paradigms, including vision-language-action policies and world-model-based planners,
    are mainly optimized for instruction execution, leaving users with little visibility into why an action is chosen and
    few mechanisms to redirect,.
  zh: WCM（World-Cognition Model）是一个以人为中心的具身智能体框架，基于 SLAK 四层架构（Sensing, Logic, Action, Knowledge）和异步运行时构建，旨在让机器人在物理任务执行中具备可解释、可干预、可教学的交互能力。核心贡献在于将交互过程本身转化为推理监督信号，通过
    CoT 蒸馏和人在环教学模式，在九个真实世界任务上达到 73.8% 的平均成功率，并展示了超出训练任务的迁移能力。
  ko: Language agents can now interact fluently with users in software, but robots still struggle to bring comparable interaction
    to physical tasks. Current robot-control paradigms, including vision-language-action policies and world-model-based planners,
    are mainly optimized for instruction execution, leaving users with little visibility into why an action is chosen and
    few mechanisms to redirect,.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- wcm
- world
- cognition
- model
- generalizable
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.22999 WCM: World-Cognition Model for Generalizable Human-Robot Interaction'
  url: https://arxiv.org/abs/2607.22999
  date: '2026-07-25'
  accessed_at: '2026-08-05'
---

## 概述

WCM（World-Cognition Model）是一个以人为中心的具身智能体框架，基于 SLAK 四层架构（Sensing, Logic, Action, Knowledge）和异步运行时构建，旨在让机器人在物理任务执行中具备可解释、可干预、可教学的交互能力。核心贡献在于将交互过程本身转化为推理监督信号，通过 CoT 蒸馏和人在环教学模式，在九个真实世界任务上达到 73.8% 的平均成功率，并展示了超出训练任务的迁移能力。

## 它改变了什么

当前机器人控制的主流范式——无论是 VLA 策略还是基于世界模型的规划器——都将语言视为动作预测的条件信号或内部推理的隐式载体，用户对“机器人为何选择这个动作”缺乏可见性，也无法在执行过程中实时重定向或纠正。这导致一个根本性错位：语言智能体在软件中能流畅对话，但机器人一旦进入物理世界，交互能力就退化为单向指令执行。WCM 真正改变的，是让语言从“条件输入”升级为“持久交互通道”——用户可以在执行中提问、干预、教导，而机器人的决策过程不再是黑箱。

另一个关键改变在于训练信号的来源。VLA 策略通常依赖遥操作采集的状态-动作轨迹，这种监督只告诉模型“做了什么”，不告诉“为什么这么做”。WCM 将决策记录（含推理轨迹、预期结果、实际结果）作为监督信号，使得交互本身——包括失败、纠正和教学——都能转化为可复用的推理经验。这不仅是架构调整，更是数据范式的转变：机器人不再只是执行者，而是能从与人的每一次互动中学习的系统。

## 方法拆解

### 架构分层与状态交换
WCM 基于 SLAK 架构，将感知、推理、控制、记忆分为四个显式层，通过显式状态交换通信，而非端到端隐藏中间过程。Sensing 层将多模态传感器流（视觉、深度、音频、IMU、力/力矩）转换为结构化场景状态 s_t，包含局部 3D 结构、物体关系、占用、语义线索，以及像素级和部件级交互线索（抓取、打开、放置、丢弃）和粗略物理属性（刚性、易碎性、可抓取性）。

### 增量式“计划–推理–验证”循环
Logic 层在步骤 t 的决策上下文为 x_t = (s_t, u_t, m_t)，其中 s_t 为场景状态，u_t 为用户指令，m_t 为从 Knowledge 检索的任务记忆。模型 f_θ 产生推理轨迹、下一动作和预期结果：
- (r_t, a_t, ô_t) = f_θ(x_t)
- 验证：v_t = 1 若 Δ(o_t, ô_t) ≤ ε，否则 v_t = 0（o_t 为实际结果，Δ 为失配度量，ε 为阈值）

若验证通过则继续，否则从更新状态重新推理或向用户请求澄清。这种设计避免了预先提交完整任务脚本，使机器人能应对执行中的不确定性。

### 异步运行时与动作丢弃
异步运行时解耦推理、执行和状态更新，允许推理、对话和执行并发进行。提交队列动作前和执行后，使用最新场景状态、用户输入和实际结果执行验证检查；若上下文不再匹配预期，丢弃过期动作并让 Logic 从更新状态重新推理。这是提升响应性和鲁棒性的关键机制。

### CoT 蒸馏管道
每个决策记录 e = {d_t}_{t=1}^{T}，d_t = (s_t, u_t, m_t, r_t, a_t, ô_t, o_t)。数据来源包括自主执行（成功和失败）和人类引导教学片段。离线精炼流程产生精炼 CoT 示例 D'_auto = R(D_auto) 和 D'_teach = R(D_teach)。蒸馏目标为：
- L_distill(θ) = L_auto(θ) + λ·L_teach(θ)，其中 λ ≥ 1 控制教学示例权重

更强的模型集成通过投票或共识审查记录、去除绕路、纠正不一致决策路径。与 VLA 式状态-动作轨迹训练不同，WCM 使用决策记录作为推理监督而非运动动作监督。

### 人在环教学模式
用户通过自然语言逐步引导机器人（指示关注什么、对哪个物体或部件操作、何时进入下一阶段），无需低层遥操作。教学片段记录与自主执行相同的逐步决策格式，并附加显式人类指导和反馈，在蒸馏中由 λ 加权。

## 关键创新

**1. 决策记录作为推理监督而非动作监督**：这是与 VLA 范式的根本区别。VLA 学习“状态→动作”映射，WCM 学习“状态+指令+记忆→推理轨迹+动作+预期结果”。这使得模型不仅知道做什么，还知道为什么做，从而支持可解释中断和用户干预。重要性在于：推理监督天然包含失败案例的纠正路径，使机器人能从错误中学习，而不仅仅是模仿成功轨迹。

**2. 异步运行时与验证循环的工程创新**：将推理、执行、状态更新解耦，并在动作提交前后进行验证检查，过期动作被丢弃。这解决了真实世界中“计划赶不上变化”的核心问题——场景状态在推理和执行之间可能已改变。消融实验显示，移除异步运行时使端到端时间增加 1.4–1.7×（由表内数值 36→61、30→47、165→254、46→63、34→49 计算），验证了其效率价值。

**3. 教学模式的轻量性**：用户通过自然语言引导而非遥操作，降低了交互门槛。教学片段在蒸馏中由 λ ≥ 1 加权，且短期存入 Knowledge 复用、长期蒸馏进推理模型。这使得“教一次”能产生持久能力提升——Screwdriver-to-Drawer 任务从教学前低于 20% 提升至教学后 69%，CoT 蒸馏后进一步升至 82%。

## 实验与结果

### 总体表现
WCM 在九个真实世界人机交互任务上达到 **73.8%** 平均成功率，覆盖物体检索、交接、工具使用、抽屉操作和垃圾处理。四个任务从 CoT 微调中留出但仍成功，展示迁移能力。

### 与 X-Square WALL-OSS 对比（Table II）
| 指标 | WCM | X-Square |
|---|---|---|
| 平均移动时间 (s) | 38.5 | 103.5 |
| 平均 GPU 忙碌时间 (s) | 22.0 | 103.5 |
| 平均成功率 (%) | 88.0 | 论文未明确 |

WCM 在移动时间和 GPU 忙碌时间上均显著优于对比系统，但作者承认因机器人本体、运动学、传感器和执行栈不同，该对比是说明性的而非受控基准。

### 消融实验（Table III）
| 任务 | WCM 时间 (s) | w/o Async 时间 (s) | WCM 成功率 (%) | w/o Sensing 成功率 (%) |
|---|---|---|---|---|
| Hand me the green ratchet | 36 | 61 | 64 | 18 |
| Grab me the water bottle | 30 | 47 | 83 | 27 |
| Take the screwdriver to the drawer | 165 | 254 | 69 | 0 |
| Put the cup in the trash can (Outdoor) | 46 | 63 | 67 | 18 |
| Put the bottle in the trash can | 34 | 49 | 64 | 9 |

移除异步运行时使端到端时间增加 1.4–1.7×（由表内数值 b→a 计算）。将 Sensing 替换为普通 VLM 和 2D grounding 后，Screwdriver-to-Drawer 成功率从 69% 降至 0%，说明结构化场景状态对复杂操作至关重要。

### 教学模式效果
最难任务“Take the screwdriver to the drawer”教学前低于 20%，交互教学后达 69%，蒸馏后升至 82%。这验证了教学+蒸馏的完整闭环有效性。

## 边界与局限

作者明确承认当前受硬件限制，评估为案例研究性质而非受控基准测试。与 X-Square 的对比因机器人本体、运动学、传感器和执行栈不同，仅为说明性结果。常规 VLA 策略通常不将连续对话、可解释中断和教学模式视为核心闭环能力，因此 Table I 仅报告 WCM 数据，缺乏同条件下的直接对照。论文未明确 WCM 在更复杂场景（如多机器人协作、非结构化动态环境）中的表现，也未报告模型规模、训练数据量等关键复现参数。此外，所有实验在单一硬件平台（低成本移动操作平台）上完成，结论在高端平台或不同形态机器人上的泛化性论文未明确。

## 工程启示

复现 WCM 时，最先要核对的是 Sensing 层的实现质量——消融实验显示，将 Sensing 替换为普通 VLM 和 2D grounding 后，复杂任务成功率直接归零，说明结构化场景状态（含部件级交互线索和物理属性）是整个系统的地基。其次，异步运行时的实现细节（动作丢弃时机、验证阈值 ε 的设定）对端到端时间影响显著，建议先在小规模任务上校准 ε 再扩展到全任务套件。

最容易踩坑的地方在于 CoT 蒸馏的数据精炼环节：作者使用更强的模型集成通过投票或共识审查记录、去除绕路、纠正不一致决策路径，这一步骤的质量直接决定蒸馏效果。如果精炼不当，失败记录可能引入噪声而非纠正信号。另外，教学模式的 λ 权重（λ ≥ 1）需要根据教学片段与自主数据的比例仔细调参，λ 过大可能导致模型过度依赖人类指导而丧失自主推理能力。硬件方面，完整机器人成本低于 $2,000，推理在共享 NVIDIA RTX 5090 上离板运行，复现时需注意网络延迟对异步运行时的影响——本地网络质量可能成为瓶颈。

## Overview
Language agents can now interact fluently with users in software, but robots still struggle to bring comparable interaction to physical tasks. Current robot-control paradigms, including vision-language-action policies and world-model-based planners, are mainly optimized for instruction execution, leaving users with little visibility into why an action is chosen and few mechanisms to redirect, correct, or teach the robot through interaction. To solve this problem, we present the World-Cognition Model (WCM), a human-centered embodied agent built on the SLAK architecture (Sensing, Logic, Action, and Knowledge) and an asynchronous runtime. SLAK separates perception, reasoning, control, and memory, while the runtime allows reasoning, dialogue, and execution to proceed concurrently. WCM further introduces a human-in-the-loop teaching mode that enables users to interactively teach the robot difficult or long-horizon tasks. Teaching episodes and autonomous task rollouts are refined into chain-of-thought supervision to continually improve the model. WCM achieves a 73.8% average success rate across nine real-world human-robot interaction tasks, including tasks held out from CoT fine-tuning and a long-horizon task learned through teaching.

## 参考
- https://arxiv.org/abs/2607.22999

## 개요

WCM(World-Cognition Model)은 인간 중심의 구현형 에이전트 프레임워크로, SLAK 4계층 아키텍처(Sensing, Logic, Action, Knowledge)와 비동기 런타임을 기반으로 구축되었으며, 로봇이 물리적 작업 실행에서 설명 가능하고, 개입 가능하며, 교육 가능한 상호작용 능력을 갖추도록 설계되었습니다. 핵심 기여는 상호작용 과정 자체를 추론 감독 신호로 변환하고, CoT 증류와 인간-참여 루프 교육 모드를 통해 9가지 실제 세계 작업에서 73.8%의 평균 성공률을 달성하며, 훈련 작업을 넘어서는 전이 능력을 보여준다는 점입니다.

## 그것이 바꾸는 것

현재 로봇 제어의 주류 패러다임(VLA 정책이든 세계 모델 기반 플래너든)은 언어를 행동 예측의 조건 신호 또는 내부 추론의 암시적 매개체로 간주하며, 사용자는 "로봇이 왜 이 행동을 선택했는지"에 대한 가시성을 갖지 못하고, 실행 중에 실시간으로 방향을 바꾸거나 수정할 수도 없습니다. 이는 근본적인 불일치를 초래합니다: 언어 에이전트는 소프트웨어에서 자연스럽게 대화할 수 있지만, 로봇이 물리적 세계에 들어서면 상호작용 능력은 단방향 명령 실행으로 퇴화합니다. WCM이 진정으로 바꾸는 것은 언어를 "조건 입력"에서 "지속적 상호작용 채널"로 승격시키는 것입니다—사용자는 실행 중에 질문하고, 개입하고, 가르칠 수 있으며, 로봇의 의사결정 과정은 더 이상 블랙박스가 아닙니다.

또 다른 핵심 변화는 훈련 신호의 출처에 있습니다. VLA 정책은 일반적으로 원격 조작으로 수집된 상태-행동 궤적에 의존하며, 이러한 감독은 모델에게 "무엇을 했는지"만 알려주고 "왜 그렇게 했는지"는 알려주지 않습니다. WCM은 결정 기록(추론 궤적, 예상 결과, 실제 결과 포함)을 감독 신호로 사용하여, 실패, 수정, 교육을 포함한 상호작용 자체가 재사용 가능한 추론 경험으로 변환될 수 있게 합니다. 이는 단순한 아키텍처 조정이 아니라 데이터 패러다임의 전환입니다: 로봇은 더 이상 단순한 실행자가 아니라, 인간과의 모든 상호작용에서 학습할 수 있는 시스템입니다.

## 방법 분해

### 아키텍처 계층화와 상태 교환
WCM은 SLAK 아키텍처를 기반으로, 지각, 추론, 제어, 기억을 네 개의 명시적 계층으로 나누고, 종단 간 숨겨진 중간 과정이 아닌 명시적 상태 교환을 통해 통신합니다. Sensing 계층은 다중 모달 센서 스트림(시각, 깊이, 오디오, IMU, 힘/토크)을 구조화된 장면 상태 s_t로 변환하며, 여기에는 로컬 3D 구조, 객체 관계, 점유, 의미적 단서, 픽셀 및 부품 수준 상호작용 단서(잡기, 열기, 놓기, 버리기), 대략적인 물리적 속성(강성, 취약성, 잡기 가능성)이 포함됩니다.

### 증분식 "계획–추론–검증" 루프
Logic 계층은 단계 t에서의 의사결정 컨텍스트를 x_t = (s_t, u_t, m_t)로 가지며, 여기서 s_t는 장면 상태, u_t는 사용자 명령, m_t는 Knowledge에서 검색된 작업 기억입니다. 모델 f_θ는 추론 궤적, 다음 행동, 예상 결과를 생성합니다:
- (r_t, a_t, ô_t) = f_θ(x_t)
- 검증: v_t = 1 (Δ(o_t, ô_t) ≤ ε), 그렇지 않으면 v_t = 0 (o_t는 실제 결과, Δ는 불일치 측정, ε는 임계값)

검증이 통과하면 계속 진행하고, 그렇지 않으면 업데이트된 상태에서 다시 추론하거나 사용자에게 명확화를 요청합니다. 이 설계는 전체 작업 스크립트를 사전에 제출하는 것을 피하고, 로봇이 실행 중 불확실성에 대응할 수 있게 합니다.

### 비동기 런타임과 행동 폐기
비동기 런타임은 추론, 실행, 상태 업데이트를 분리하여 추론, 대화, 실행이 동시에 진행될 수 있게 합니다. 큐에 행동을 제출하기 전과 실행 후에 최신 장면 상태, 사용자 입력, 실제 결과를 사용하여 검증 검사를 수행하고, 컨텍스트가 더 이상 예상과 일치하지 않으면 만료된 행동을 폐기하고 Logic이 업데이트된 상태에서 다시 추론하도록 합니다. 이는 응답성과 견고성을 향상시키는 핵심 메커니즘입니다.

### CoT 증류 파이프라인
각 결정 기록 e = {d_t}_{t=1}^{T}, d_t = (s_t, u_t, m_t, r_t, a_t, ô_t, o_t). 데이터 출처는 자율 실행(성공 및 실패)과 인간 안내 교육 세그먼트를 포함합니다. 오프라인 정제 프로세스는 정제된 CoT 예제 D'_auto = R(D_auto)와 D'_teach = R(D_teach)를 생성합니다. 증류 목표는:
- L_distill(θ) = L_auto(θ) + λ·L_teach(θ), 여기서 λ ≥ 1은 교육 예제 가중치를 제어합니다

더 강력한 모델 앙상블은 투표 또는 합의 검토를 통해 기록을 검토하고, 우회를 제거하며, 불일치하는 결정 경로를 수정합니다. VLA식 상태-행동 궤적 훈련과 달리, WCM은 운동 행동 감독이 아닌 추론 감독으로 결정 기록을 사용합니다.

### 인간-참여 루프 교육 모드
사용자는 자연어를 통해 로봇을 단계적으로 안내합니다(무엇에 주목할지, 어떤 객체 또는 부품을 조작할지, 언제 다음 단계로 진행할지), 저수준 원격 조작이 필요하지 않습니다. 교육 세그먼트는 자율 실행과 동일한 단계별 결정 형식을 기록하며, 명시적 인간 안내와 피드백이 추가되고 증류에서 λ로 가중됩니다.

## 핵심 혁신

**1. 결정 기록을 행동 감독이 아닌 추론 감독으로 사용**: 이는 VLA 패러다임과의 근본적 차이입니다. VLA는 "상태→행동" 매핑을 학습하고, WCM은 "상태+명령+기억→추론 궤적+행동+예상 결과"를 학습합니다. 이는 모델이 무엇을 해야 하는지뿐만 아니라 왜 그렇게 해야 하는지도 알게 하여, 설명 가능한 중단과 사용자 개입을 지원합니다. 중요성은: 추론 감독은 자연스럽게 실패 사례의 수정 경로를 포함하여 로봇이 성공 궤적을 모방하는 것뿐만 아니라 오류에서 학습할 수 있게 합니다.

**2. 비동기 런타임과 검증 루프의 엔지니어링 혁신**: 추론, 실행, 상태 업데이트를 분리하고, 행동 제출 전후에 검증 검사를 수행하며, 만료된 행동을 폐기합니다. 이는 실제 세계에서 "계획이 변화를 따라가지 못하는" 핵심 문제를 해결합니다—장면 상태는 추론과 실행 사이에 이미 변경될 수 있습니다. 절제 실험에 따르면 비동기 런타임을 제거하면 종단 간 시간이 1.4–1.7배 증가하며(표 내 값 36→61, 30→47, 165→254, 46→63, 34→49에서 계산), 효율성 가치를 검증합니다.

**3. 교육 모드의 경량성**: 사용자는 원격 조작이 아닌 자연어 안내를 통해 상호작용하여 진입 장벽을 낮춥니다. 교육 세그먼트는 증류에서 λ ≥ 1로 가중되고, 단기적으로 Knowledge에 저장되어 재사용되며, 장기적으로 추론 모델로 증류됩니다. 이는 "한 번 가르치면" 지속적인 능력 향상을 생성할 수 있게 합니다—Screwdriver-to-Drawer 작업은 교육 전 20% 미만에서 교육 후 69%로, CoT 증류 후 82%로 추가 상승합니다.

## 실험과 결과

### 전반적 성과
WCM은 9가지 실제 세계 인간-로봇 상호작용 작업에서 **73.8%** 평균 성공률을 달성하며, 객체 검색, 인계, 도구 사용, 서랍 조작, 쓰레기 처리를 포함합니다. 네 가지 작업은 CoT 미세 조정에서 제외되었지만 성공하여 전이 능력을 보여줍니다.

### X-Square WALL-OSS와의 비교 (Table II)
| 지표 | WCM | X-Square |
|---|---|---|
| 평균 이동 시간 (s) | 38.5 | 103.5 |
| 평균 GPU 사용 시간 (s) | 22.0 | 103.5 |
| 평균 성공률 (%) | 88.0 | 논문에 명시되지 않음 |

WCM은 이동 시간과 GPU 사용 시간에서 비교 시스템보다 현저히 우수하지만, 저자는 로봇 본체, 운동학, 센서, 실행 스택이 다르기 때문에 이 비교는 설명적이며 통제된 벤치마크가 아니라고 인정합니다.

### 절제 실험 (Table III)
| 작업 | WCM 시간 (s) | w/o Async 시간 (s) | WCM 성공률 (%) | w/o Sensing 성공률 (%) |
|---|---|---|---|---|
| Hand me the green ratchet | 36 | 61 | 64 | 18 |
| Grab me the water bottle | 30 | 47 | 83 | 27 |
| Take the screwdriver to the drawer | 165 | 254 | 69 | 0 |
| Put the cup in the trash can (Outdoor) | 46 | 63 | 67 | 18 |
| Put the bottle in the trash can | 34 | 49 | 64 | 9 |

비동기 런타임을 제거하면 종단 간 시간이 1.4–1.7배 증가합니다(표 내 값 b→a에서 계산). Sensing을 일반 VLM과 2D grounding으로 대체하면 Screwdriver-to-Drawer 성공률이 69%에서 0%로 떨어지며, 구조화된 장면 상태가 복잡한 조작에 필수적임을 보여줍니다.

### 교육 모드 효과
가장 어려운 작업 "Take the screwdriver to the drawer"는 교육 전 20% 미만, 상호작용 교육 후 69%, 증류 후 82%로 상승합니다. 이는 교육+증류의 완전한 폐쇄 루프 효과를 검증합니다.

## 경계와 한계

저자는 현재 하드웨어 제약으로 인해 평가가 통제된 벤치마크 테스트가 아닌 사례 연구 성격임을 명시적으로 인정합니다. X-Square와의 비교는 로봇 본체, 운동학, 센서, 실행 스택이 다르기 때문에 설명적 결과일 뿐입니다. 일반적인 VLA 정책은 일반적으로 연속 대화, 설명 가능한 중단, 교육 모드를 핵심 폐쇄 루프 능력으로 간주하지 않으므로, Table I은 WCM 데이터만 보고하며 동일 조건에서의 직접 대조가 부족합니다. 논문은 더 복잡한 시나리오(다중 로봇 협업, 비구조화된 동적 환경 등)에서의 WCM 성능을 명시하지 않았으며, 모델 규모, 훈련 데이터 양과 같은 핵심 재현 매개변수도 보고하지 않았습니다. 또한 모든 실험은 단일 하드웨어 플랫폼(저비용 이동 조작 플랫폼)에서 수행되었으며, 고급 플랫폼이나 다른 형태의 로봇에서의 결론 일반화는 논문에 명시되지 않았습니다.

## 엔지니어링 시사점

WCM을 재현할 때 가장 먼저 확인해야 할 것은 Sensing 계층의 구현 품질입니다—절제 실험에 따르면 Sensing을 일반 VLM과 2D grounding으로 대체하면 복잡한 작업 성공률이 직접 0으로 떨어지며, 구조화된 장면 상태(부품 수준 상호작용 단서와 물리적 속성 포함)가 전체 시스템의 기반임을 보여줍니다. 둘째, 비동기 런타임의 구현 세부 사항(행동 폐기 시점, 검증 임계값 ε 설정)은 종단 간 시간에 현저한 영향을 미치므로, 먼저 소규모 작업에서 ε을 보정한 후 전체 작업 세트로 확장하는 것이 좋습니다.

가장 함정에 빠지기 쉬운 곳은 CoT 증류의 데이터 정제 단계입니다: 저자는 더 강력한 모델 앙상블을 사용하여 투표 또는 합의 검토를 통해 기록을 검토하고, 우회를 제거하며, 불일치하는 결정 경로를 수정합니다. 이 단계의 품질이 증류 효과를 직접 결정합니다. 정제가 부적절하면 실패 기록이 수정 신호가 아닌 노이즈를 도입할 수 있습니다. 또한 교육 모드의 λ 가중치(λ ≥ 1)는 교육 세그먼트와 자율 데이터의 비율에 따라 신중하게 조정해야 하며, λ가 너무 크면 모델이 인간 안내에 과도하게 의존하여 자율 추론 능력을 잃을 수 있습니다. 하드웨어 측면에서 완전한 로봇 비용은 $2,000 미만이며, 추론은 공유 NVIDIA RTX 5090에서 오프보드로 실행되므로, 재현 시 네트워크 지연이 비동기 런타임에 미치는 영향을 주의해야 합니다—로컬 네트워크 품질이 병목이 될 수 있습니다.
