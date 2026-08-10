---
$id: ent_paper_phyagentos_self_evolving_operating_syste_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution'
  zh: 'PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution'
  ko: 'PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution'
summary:
  en: Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition
    lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous
    embodiments. We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and
    safety as system-level services..
  zh: PhyAgentOS 是一个面向具身智能体的自进化操作系统，由 X-Era Lab、中山大学 HCP Lab 和鹏城实验室联合提出。其核心贡献在于将认知-物理边界设计为文件系统接口（State-as-a-File），通过会话中心运行时和分层安全架构，实现无需重训练神经模型的闭环试错与跨具身迁移。
  ko: Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition
    lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous
    embodiments. We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and
    safety as system-level services..
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
- phyagentos
- self
- evolving
- operating
- syste
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.16636 PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled '
  url: https://arxiv.org/abs/2607.16636
  date: '2026-07-18'
  accessed_at: '2026-08-05'
---

## 概述

PhyAgentOS 是一个面向具身智能体的自进化操作系统，由 X-Era Lab、中山大学 HCP Lab 和鹏城实验室联合提出。其核心贡献在于将认知-物理边界设计为文件系统接口（State-as-a-File），通过会话中心运行时和分层安全架构，实现无需重训练神经模型的闭环试错与跨具身迁移。

## 它改变了什么

当前具身智能系统存在一个根本性的验证鸿沟：当机器人被指令抓取杯子时，夹爪可能在空处闭合，但 VLA 控制器记录轨迹在容差内完成、世界模型确认预测状态与观测一致、规划器报告所有工具调用无错误——每一层都报告成功，但杯子不在机器人手中。这种系统性自我欺骗源于执行终止被混同为任务完成，控制器返回的成功码被错误解释为目标达成的证据。

三个范式（VLA 模型、世界模型、智能体系统）各自解决子问题但相对孤立，简单组合它们会失败于三个结构性原因：各层抽象级别不兼容（像素级输出、潜状态、符号工具调用需要临时转换器）、不透明性被放大（失败时根因搜索空间横跨推理、工具调用和物理执行）、栈缺乏持久记忆（会话知识在结束时被丢弃）。ROS 仅提供发布-订阅通信，不原生提供任务级调度、跨会话记忆或语义验证。PhyAgentOS 真正改变的是：将验证从各层内部的可选步骤提升为系统级的一等公民，通过文件协议让意图与物理证据在共同状态空间中可比较。

## 方法拆解

### 核心架构：认知-物理边界即文件系统
所有跨进程数据（目标、技能、会话、观测、教训、知识）物化为带嵌入 YAML 块的人类可读 Markdown 文件。State-as-a-File 协议产生追加式审计轨迹，支持语言无关交互。会话（session）而非单个动作是调度、预检、监控和验证的最小单元。

### 双执行流
- **PolicySkillRuntime**：策略负责产生智能动作，PhyAgentOS 负责使动作可执行、安全、可追踪。公式：A_t = Policy(I, O_t, S_t, H_t)，其中 A 为动作或动作块，I 为指令，O 为观测，S 为状态，H 为历史。Agent 在编译会话后退出低层循环。
- **BuiltinSkillRuntime**：无独立策略服务器，Agent 通过受控的 TargetSessionHandle 参与在线工具循环。公式：T_t = Agent(I, O_t, S_t, H_t)。适用于离散游戏交互、基准编排、脚本化程序。

### Runtime 层四阶段链
WatchdogSupervisor → SessionRunner → SkillRuntime → Target，每阶段缩小责任范围。WatchdogSupervisor 认领 SESSIONS.md 中的待处理会话，验证适配器契约，监控执行心跳，写回结果；执行监督而非控制，不执行观测-动作循环。

### 五层安全架构
1. 兼容性预检（compatibility preflight）：会话到达目标前解析观测模态、动作表示、策略端点、目标能力、时序约束和安全配置，结果物化为 AdapterPlan 和 TargetToolManifest。
2. 动作桥（action bridges）：强制执行独立于模型和目标的变换与约束（坐标转换、维度投影、夹取限制）。
3. SafetyGuard：传输前检查数据类型和维度验证、拒绝 NaN 和无穷值、关节和工作空间限制、速度加速度边界、急停状态。
4. 心跳监控：覆盖 SessionRunner、策略服务和目标运行时，缺失心跳触发超时处理和受控终止。
5. 目标本地约束：真实机器人的关节限制、碰撞检测、扭矩约束；模拟器的动作有效性策略；游戏目标限制特权命令。

### SessionVerifier 与自进化闭环
实现判断函数 V(G, S_0, S_T, τ, H) → {success, failure, replan}，其中 G 为任务目标和验收标准，S_0 和 S_T 为初始和终止环境状态，τ 为执行轨迹，H 为历史上下文。证据包包含初始和终止观测、原始任务定义、ENVIRONMENT.md 快照、动作-观测历史。replan 时原始尝试保持不可变，编译子会话并更新前置条件。

闭环试错六阶段：Execute → Verify → Diagnose → Revise → Re-verify → Consolidate。仅在结果验证后才将知识提交到持久记忆。经验三级抽象：情节级（单个会话记录）、语义级（聚合重复情节）、方法论级（跨多样初始状态有效的程序可提升为可复用技能规范）。

### 多层级记忆架构
SESSIONS.md 存储情景记忆，ENVIRONMENT.md 提供工作记忆，LESSONS.md 和 KNOWLEDGE.md 构成语义记忆，SKILL.md 和 SKILLRUNTIME.md 编码程序性记忆。双知识接口：KNOWLEDGE.md 存储已验证的成功模式及适用条件；LESSONS.md 存储失败中心记录（失败目标、证据、诊断原因、尝试修正及后续是否验证）。

## 关键创新

**1. 将认知-物理边界建模为文件系统而非函数调用接口**：这是最根本的设计决策。所有跨进程数据物化为人类可读的 Markdown 文件，产生追加式审计轨迹。相比私有内存对象或成对 RPC 接口，文件协议让系统对当前信念、执行内容和已产生证据保持单一可检查记录，且天然支持语言无关交互和版本控制。

**2. 用语义接受取代二元完成信号**：SessionVerifier 基于共享状态，用证据束而非控制器返回码渲染成功、失败或重规划的裁决，区分执行终止与语义任务完成。这直接闭合了意图与成就之间的开环，是解决验证鸿沟的关键机制。

**3. 自进化不涉及任何神经模型权重更新**：验证结果通过认知记忆整合为可复用知识和纠正性教训，跨会话闭环试错。基准测试复用与部署相同的会话、运行时和验证路径，测量增益可追溯到实际执行过程。这意味着系统改进完全发生在协议层，与底层模型无关。

## 实验与结果

### 认知规划基准（游戏层）
**Optimus-67**（Minecraft，67 个长时程任务，7 个难度组）：

| 模型 | Wood | Stone | Iron | Gold | Diamond | RedStone | Armor |
|---|---|---|---|---|---|---|---|
| GPT-4o | 0.47 | 0.23 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 |
| Optimus-3 | 0.99 | 0.95 | 0.55 | 0.10 | 0.15 | 0.29 | 0.23 |
| PhyAgentOS | 0.99 | 0.96 | 0.52 | 0.06 | 0.19 | 0.30 | 0.15 |

PhyAgentOS 在 Wood 和 Stone 上接近饱和（99% 和 96%），RedStone 达 30% 超过所有报告基线，但 Gold 和 Diamond 分别仅 6% 和 19%。

**StarDojo Lite-100**：PhyAgentOS 使用纯文本模型 deepseek-v4-flash，总体成功率 22.0%，超过 SPIKE 基线 18.0%。Crafting 类别最大提升：50.0% 对比最强基线 23.8%。简单任务成功率 37.5%，中等任务 3.7%，困难任务 0.0%。

**DST-Dojo**（Don't Starve，10 个 episode）：存活天数从 1.02 提升至 2.10（+106%），第 3 天存活率从 0% 提升至 30%。

### 物理执行层（LIBERO/CALVIN/RoboCasa365）
LIBERO 上各 VLA 模型增益较小（+0.0 至 +2.0 个百分点），CALVIN 上 π₀ 链式成功率从 38.9% 提升至 45.6%（+6.7）。RoboCasa365 上增益显著：π₀.₅ 的 Atomic 从 41.1% 提升至 56.7%（+15.6），Composite 从 4.4% 提升至 10.0%（+5.6）。

### 真实机器人
已测试平台包括 Agilex PIPER、Huibo Astra-Pro、HuggingFace SO101、Stella Gaia Hand 20 等 6 种；另有 13 种仅仿真验证。安全验证方法包括预检拒绝率（注入故意不兼容的适配器配置）、SafetyGuard 有效性（注入违反工作空间边界的动作块）、急停延迟测量。

## 边界与局限

**轮询式协议延迟**：当前文件协议实现使用轮询（Watchdog 周期性读取 SESSIONS.md），引入与轮询间隔成比例的延迟；事件驱动方案需保持单写者语义和原子文件更新，论文未明确实现方案。

**长时程记忆无界**：Epistemic Memory 无原则性压缩边界，LESSONS.md 和 KNOWLEDGE.md 随会话数单调增长。当前选择启发式（任务类型匹配+近因加权）缺乏对抗性任务序列下相关经验召回的理论保证，技能质量保证仍半手动。

**真实机器人评估覆盖有限**：仅限硬件可用平台，侧重安全关键验证而非大规模任务完成统计。完整渐进流水线仅在代表性具身（Franka、PIPER、Dobot）上演示，未扩展到机队级多样性。

**未完全实现组件**：Goal Graph 和 Session Compiler 架构中已描述但尚未完全实现；世界模型仅视为外部推理资源，未深度集成到会话规划循环。未在真实机器人上大规模测量任务完成统计，未将零样本迁移扩展到腿式运动、飞行器、软体操纵器等大幅不同形态。

## 工程启示

**复现优先核对三件事**：第一，确认协议文件路径和格式完全一致——SESSIONS.md、SKILLRUNTIME.md、TARGETS.md、ENVIRONMENT.md、LESSONS.md 五个 Markdown 文档加四个 YAML 文件（sensors.yaml、perception.yaml、runtime_contract.yaml、safety.yaml）缺一不可；第二，验证 WatchdogSupervisor 的轮询间隔设置，它直接决定系统延迟上限；第三，检查 SessionVerifier 的证据包完整性——初始和终止观测、ENVIRONMENT.md 快照、动作-观测历史缺一不可，否则裁决不可信。

**最容易踩坑的地方**：一是将 BuiltinSkillRuntime 与 PolicySkillRuntime 混用——前者要求 Agent 在线参与工具循环，后者要求 Agent 编译会话后退出，混淆会导致控制权冲突；二是 SafetyGuard 的维度验证——VLA 输出在到达物理目标前必须经过动作桥的坐标转换和维度投影，跳过这一步会引入 NaN 或越界动作；三是记忆写入时机——仅在验证通过后才将知识提交到持久记忆，否则推测性解释会被当作既定经验。

**下游团队选型建议**：如果主要诉求是提升 VLA 模型在长时程任务上的成功率，PhyAgentOS 的增益在 RoboCasa365 这类复合任务上最显著（+5.6 至 +15.6 个百分点），在 LIBERO 这类短时程任务上增益有限（+0.0 至 +2.0 个百分点）。如果关注跨具身迁移，更换具身只需替换 TargetAdapter 和 PolicyAdapter，认知层和协议文件保持不变——但需注意零样本迁移未在腿式运动、飞行器等大幅不同形态上验证。

## Overview
Vision-language-action models, world models, and agentic planners each advance physical intelligence, yet their composition lacks a common execution abstraction, shared state, semantic verification, and persistent experience across heterogeneous embodiments. We present PhyAgentOS, a runtime foundation delivering scheduling, verification, memory, benchmarking, and safety as system-level services. Its Session-Centered Runtime treats a session, not an action, as the minimum unit of scheduling, compatibility preflight, supervised execution, evidence collection, and acceptance. To decouple cognition from physical execution, the cognition-physics boundary is a file system: the State-as-a-File protocol materializes cross-layer state as Markdown with YAML, yielding inspectable, versionable records without code dependencies between Agent and Runtime layers. These views form a unified cognitive state space aligning intent, capabilities, environment, execution, and experience. The SessionVerifier distinguishes execution termination from semantic task completion via evidence-grounded verdicts of success, failure, or replan. Verified outcomes are consolidated through epistemic memory into reusable knowledge and corrective lessons, closing a trial-and-error loop without retraining. Benchmarking reuses the deployment session and verification path, so results trace to real execution. Layered safety constrains both policy-driven and agent-driven execution: preflight, action bridges, SafetyGuard, heartbeat monitoring, and target-local constraints. Validation is progressive: games test cognitive planning, simulation adds dynamics and control, real robots add hardware noise, with the cognitive layer held constant. PhyAgentOS is benchmarked on Optimus-67, StarDojo, and DST-Dojo, validated on 19+ simulated and physical embodiments, and gains on LIBERO, Calvin, and RoboCasa365 across multiple VLA models.

## 参考
- https://arxiv.org/abs/2607.16636

## 개요

PhyAgentOS는 X-Era Lab, 중산대학교 HCP Lab, 펑청연구소가 공동으로 제안한, 구현지능 에이전트를 위한 자가 진화 운영체제입니다. 핵심 기여는 인지-물리 경계를 파일시스템 인터페이스(State-as-a-File)로 설계하고, 세션 중심 런타임과 계층적 보안 아키텍처를 통해 신경 모델 재훈련 없이 폐루프 시행착오와 교차 구현 전이를 가능하게 한 것입니다.

## 무엇을 바꾸는가

현재 구현지능 시스템에는 근본적인 검증 격차가 존재합니다. 로봇이 컵을 집으라는 지시를 받았을 때, 그리퍼가 빈 공간에서 닫힐 수 있지만 VLA 컨트롤러는 궤적이 허용 오차 내에서 완료되었다고 기록하고, 월드 모델은 예측 상태가 관측과 일치한다고 확인하며, 플래너는 모든 도구 호출에 오류가 없다고 보고합니다—각 계층은 모두 성공을 보고하지만, 컵은 로봇 손에 없습니다. 이러한 체계적 자기기만은 실행 종료가 작업 완료로 혼동되고, 컨트롤러가 반환하는 성공 코드가 목표 달성의 증거로 잘못 해석되기 때문에 발생합니다.

세 가지 패러다임(VLA 모델, 월드 모델, 에이전트 시스템)은 각각 하위 문제를 해결하지만 상대적으로 고립되어 있으며, 단순히 결합하면 세 가지 구조적 이유로 실패합니다: 각 계층의 추상화 수준이 호환되지 않고(픽셀 수준 출력, 잠재 상태, 기호 도구 호출은 임시 변환기가 필요), 불투명성이 증폭되며(실패 시 근본 원인 탐색 공간이 추론, 도구 호출, 물리적 실행에 걸쳐 있음), 스택에 지속적 메모리가 부족합니다(세션 지식이 종료 시 폐기됨). ROS는 발행-구독 통신만 제공할 뿐, 작업 수준 스케줄링, 세션 간 메모리 또는 의미론적 검증을 기본 제공하지 않습니다. PhyAgentOS가 진정으로 바꾸는 것은 검증을 각 계층 내부의 선택적 단계에서 시스템 수준의 일급 시민으로 승격시키고, 파일 프로토콜을 통해 의도와 물리적 증거가 공통 상태 공간에서 비교 가능하게 만드는 것입니다.

## 방법 분석

### 핵심 아키텍처: 인지-물리 경계 = 파일시스템
모든 프로세스 간 데이터(목표, 스킬, 세션, 관측, 교훈, 지식)는 임베디드 YAML 블록이 포함된 사람이 읽을 수 있는 Markdown 파일로 구체화됩니다. State-as-a-File 프로토콜은 추가 전용 감사 궤적을 생성하며, 언어 독립적 상호작용을 지원합니다. 개별 동작이 아닌 세션(session)이 스케줄링, 사전 점검, 모니터링, 검증의 최소 단위입니다.

### 이중 실행 흐름
- **PolicySkillRuntime**: 정책은 지능적 동작을 생성하고, PhyAgentOS는 동작을 실행 가능하고 안전하며 추적 가능하게 만듭니다. 공식: A_t = Policy(I, O_t, S_t, H_t), 여기서 A는 동작 또는 동작 블록, I는 지시, O는 관측, S는 상태, H는 기록입니다. 에이전트는 세션 컴파일 후 저수준 루프에서 종료됩니다.
- **BuiltinSkillRuntime**: 독립적인 정책 서버가 없으며, 에이전트는 제어된 TargetSessionHandle을 통해 온라인 도구 루프에 참여합니다. 공식: T_t = Agent(I, O_t, S_t, H_t). 이산 게임 상호작용, 벤치마크 오케스트레이션, 스크립트 프로그램에 적합합니다.

### Runtime 계층 4단계 체인
WatchdogSupervisor → SessionRunner → SkillRuntime → Target, 각 단계는 책임 범위를 좁힙니다. WatchdogSupervisor는 SESSIONS.md의 대기 중인 세션을 인계받고, 어댑터 계약을 검증하며, 실행 하트비트를 모니터링하고, 결과를 기록합니다. 실행 감독을 수행할 뿐 제어하지 않으며, 관측-동작 루프를 실행하지 않습니다.

### 5계층 보안 아키텍처
1. 호환성 사전 점검(compatibility preflight): 세션이 대상에 도달하기 전에 관측 양식, 동작 표현, 정책 엔드포인트, 대상 능력, 시간 제약, 안전 구성을 해석하며, 결과는 AdapterPlan과 TargetToolManifest로 구체화됩니다.
2. 동작 브리지(action bridges): 모델과 대상과 무관한 변환 및 제약을 강제합니다(좌표 변환, 차원 투영, 그리핑 제한).
3. SafetyGuard: 전송 전 데이터 유형 및 차원 검증, NaN 및 무한대 값 거부, 관절 및 작업 공간 제한, 속도 및 가속도 경계, 비상 정지 상태 확인.
4. 하트비트 모니터링: SessionRunner, 정책 서비스, 대상 런타임을 포괄하며, 하트비트 누락 시 타임아웃 처리 및 통제된 종료를 트리거합니다.
5. 대상 로컬 제약: 실제 로봇의 관절 제한, 충돌 감지, 토크 제약; 시뮬레이터의 동작 유효성 정책; 게임 대상의 특권 명령 제한.

### SessionVerifier와 자가 진화 폐루프
판정 함수 V(G, S_0, S_T, τ, H) → {success, failure, replan}을 구현합니다. 여기서 G는 작업 목표 및 수용 기준, S_0와 S_T는 초기 및 종료 환경 상태, τ는 실행 궤적, H는 기록 컨텍스트입니다. 증거 패키지에는 초기 및 종료 관측, 원시 작업 정의, ENVIRONMENT.md 스냅샷, 동작-관측 기록이 포함됩니다. replan 시 원래 시도는 불변으로 유지되며, 하위 세션이 컴파일되고 전제 조건이 업데이트됩니다.

폐루프 시행착오 6단계: Execute → Verify → Diagnose → Revise → Re-verify → Consolidate. 결과 검증 후에만 지식이 지속 메모리에 커밋됩니다. 경험 3단계 추상화: 에피소드 수준(단일 세션 기록), 의미 수준(반복 에피소드 집계), 방법론 수준(다양한 초기 상태에서 유효한 절차는 재사용 가능한 스킬 사양으로 승격 가능).

### 다계층 메모리 아키텍처
SESSIONS.md는 상황 메모리를 저장하고, ENVIRONMENT.md는 작업 메모리를 제공하며, LESSONS.md와 KNOWLEDGE.md는 의미 메모리를 구성하고, SKILL.md와 SKILLRUNTIME.md는 절차적 메모리를 인코딩합니다. 이중 지식 인터페이스: KNOWLEDGE.md는 검증된 성공 패턴과 적용 조건을 저장하고, LESSONS.md는 실패 중심 기록(실패 목표, 증거, 진단 원인, 시도된 수정, 이후 검증 여부)을 저장합니다.

## 핵심 혁신

**1. 인지-물리 경계를 함수 호출 인터페이스가 아닌 파일시스템으로 모델링**: 이것이 가장 근본적인 설계 결정입니다. 모든 프로세스 간 데이터는 사람이 읽을 수 있는 Markdown 파일로 구체화되어 추가 전용 감사 궤적을 생성합니다. 개인 메모리 객체나 쌍방 RPC 인터페이스와 달리, 파일 프로토콜은 시스템이 현재 신념, 실행 내용, 생성된 증거에 대한 단일 검사 가능한 기록을 유지하며, 언어 독립적 상호작용과 버전 관리를 자연스럽게 지원합니다.

**2. 이진 완료 신호를 의미론적 수용으로 대체**: SessionVerifier는 공유 상태를 기반으로 컨트롤러 반환 코드가 아닌 증거 묶음으로 성공, 실패 또는 재계획의 판정을 렌더링하여 실행 종료와 의미론적 작업 완료를 구분합니다. 이는 의도와 성취 사이의 개루프를 직접 폐쇄하며, 검증 격차를 해결하는 핵심 메커니즘입니다.

**3. 자가 진화는 어떤 신경 모델 가중치 업데이트도 포함하지 않음**: 검증 결과는 인지 메모리 통합을 통해 재사용 가능한 지식과 교정적 교훈으로 변환되어 세션 간 폐루프 시행착오를 수행합니다. 벤치마크 테스트는 배포와 동일한 세션, 런타임, 검증 경로를 재사용하며, 측정된 이득은 실제 실행 과정으로 추적 가능합니다. 이는 시스템 개선이 완전히 프로토콜 계층에서 발생하며, 하위 모델과 무관함을 의미합니다.

## 실험 및 결과

### 인지 계획 벤치마크(게임 계층)
**Optimus-67**(Minecraft, 67개 장기 작업, 7개 난이도 그룹):

| 모델 | Wood | Stone | Iron | Gold | Diamond | RedStone | Armor |
|---|---|---|---|---|---|---|---|
| GPT-4o | 0.47 | 0.23 | 0.05 | 0.00 | 0.00 | 0.00 | 0.00 |
| Optimus-3 | 0.99 | 0.95 | 0.55 | 0.10 | 0.15 | 0.29 | 0.23 |
| PhyAgentOS | 0.99 | 0.96 | 0.52 | 0.06 | 0.19 | 0.30 | 0.15 |

PhyAgentOS는 Wood와 Stone에서 포화에 근접하며(99% 및 96%), RedStone은 30%로 보고된 모든 기준선을 초과하지만, Gold와 Diamond는 각각 6%와 19%에 불과합니다.

**StarDojo Lite-100**: PhyAgentOS는 순수 텍스트 모델 deepseek-v4-flash를 사용하여 전체 성공률 22.0%로 SPIKE 기준선 18.0%를 초과합니다. Crafting 카테고리에서 가장 큰 향상: 50.0% 대 최강 기준선 23.8%. 단순 작업 성공률 37.5%, 중간 작업 3.7%, 어려운 작업 0.0%.

**DST-Dojo**(Don't Starve, 10개 에피소드): 생존 일수가 1.02에서 2.10으로 향상(+106%), 3일차 생존율이 0%에서 30%로 향상.

### 물리 실행 계층(LIBERO/CALVIN/RoboCasa365)
LIBERO에서 각 VLA 모델의 이득은 작으며(+0.0 ~ +2.0 퍼센트 포인트), CALVIN에서 π₀ 체인 성공률은 38.9%에서 45.6%로 향상(+6.7). RoboCasa365에서 이득이 두드러짐: π₀.₅의 Atomic은 41.1%에서 56.7%로 향상(+15.6), Composite은 4.4%에서 10.0%로 향상(+5.6).

### 실제 로봇
테스트된 플랫폼에는 Agilex PIPER, Huibo Astra-Pro, HuggingFace SO101, Stella Gaia Hand 20 등 6종이 포함되며, 추가로 13종은 시뮬레이션으로만 검증되었습니다. 안전 검증 방법에는 사전 점검 거부율(의도적으로 비호환 어댑터 구성 주입), SafetyGuard 유효성(작업 공간 경계를 위반하는 동작 블록 주입), 비상 정지 지연 측정이 포함됩니다.

## 경계 및 한계

**폴링 기반 프로토콜 지연**: 현재 파일 프로토콜 구현은 폴링(Watchdog가 주기적으로 SESSIONS.md를 읽음)을 사용하여 폴링 간격에 비례하는 지연을 도입합니다. 이벤트 기반 방식은 단일 작성자 의미론과 원자적 파일 업데이트를 유지해야 하며, 논문은 구현 방식을 명확히 제시하지 않습니다.

**장기 메모리 무경계**: 인식 메모리(Epistemic Memory)에는 원칙적 압축 경계가 없으며, LESSONS.md와 KNOWLEDGE.md는 세션 수에 따라 단조 증가합니다. 현재 선택 휴리스틱(작업 유형 매칭 + 최근성 가중치)은 적대적 작업 시퀀스에서 관련 경험 회상에 대한 이론적 보장이 부족하며, 스킬 품질 보증은 여전히 반자동입니다.

**실제 로봇 평가 범위 제한**: 하드웨어 사용 가능 플랫폼에만 국한되며, 대규모 작업 완료 통계보다 안전 핵심 검증에 중점을 둡니다. 완전한 점진적 파이프라인은 대표적 구현(Franka, PIPER, Dobot)에서만 시연되었으며, 함대 수준 다양성으로 확장되지 않았습니다.

**완전히 구현되지 않은 구성 요소**: Goal Graph와 Session Compiler는 아키텍처에서 설명되었지만 아직 완전히 구현되지 않았습니다. 월드 모델은 외부 추론 리소스로만 간주되며 세션 계획 루프에 깊이 통합되지 않았습니다. 실제 로봇에서 대규모 작업 완료 통계를 측정하지 않았으며, 제로샷 전이를 다리 운동, 비행체, 소프트 매니퓰레이터 등 크게 다른 형태로 확장하지 않았습니다.

## 엔지니어링 시사점

**재현 시 우선 확인할 세 가지**: 첫째, 프로토콜 파일 경로와 형식이 완전히 일치하는지 확인—SESSIONS.md, SKILLRUNTIME.md, TARGETS.md, ENVIRONMENT.md, LESSONS.md 다섯 개 Markdown 문서와 네 개 YAML 파일(sensors.yaml, perception.yaml, runtime_contract.yaml, safety.yaml)이 하나도 빠짐없이 필요합니다. 둘째, WatchdogSupervisor의 폴링 간격 설정을 검증하세요. 이는 시스템 지연 상한을 직접 결정합니다. 셋째, SessionVerifier의 증거 패키지 완전성을 확인하세요—초기 및 종료 관측, ENVIRONMENT.md 스냅샷, 동작-관측 기록이 하나도 빠짐없이 필요하며, 그렇지 않으면 판정을 신뢰할 수 없습니다.

**가장 함정에 빠지기 쉬운 부분**: 첫째, BuiltinSkillRuntime과 PolicySkillRuntime을 혼용하는 것—전자는 에이전트가 온라인 도구 루프에 참여해야 하고, 후자는 에이전트가 세션 컴파일 후 종료해야 하며, 혼동하면 제어권 충돌이 발생합니다. 둘째, SafetyGuard의 차원 검증—VLA 출력은 물리적 대상에 도달하기 전에 반드시 동작 브리지의 좌표 변환과 차원 투영을 거쳐야 하며, 이 단계를 건너뛰면 NaN 또는 경계 초과 동작이 발생합니다. 셋째, 메모리 기록 시점—검증 통과 후에만 지식을 지속 메모리에 커밋해야 하며, 그렇지 않으면 추측성 설명이 확립된 경험으로 취급됩니다.

**하위 팀 선택 제안**: 주요 목표가 VLA 모델의 장기 작업 성공률 향상이라면, PhyAgentOS의 이득은 RoboCasa365와 같은 복합 작업에서 가장 두드러지며(+5.6 ~ +15.6 퍼센트 포인트), LIBERO와 같은 단기 작업에서는 이득이 제한적입니다(+0.0 ~ +2.0 퍼센트 포인트). 교차 구현 전이에 관심이 있다면, 구현 교체는 TargetAdapter와 PolicyAdapter만 교체하면 되며 인지 계층과 프로토콜 파일은 변경되지 않습니다—단, 제로샷 전이는 다리 운동, 비행체 등 크게 다른 형태에서 검증되지 않았음을 유의하세요.
