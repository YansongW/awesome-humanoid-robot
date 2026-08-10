---
$id: ent_paper_step_signal_temporal_logic_precise_speci_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models'
  zh: 'STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models'
  ko: 'STeP: Signal Temporal Logic for Precise Specifications for Action Generation with Vision Language Models'
summary:
  en: Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle
    to follow precise natural language instructions that encode spatial, temporal, and logical requirements. We propose a
    hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language
    understanding with low-level robot.
  zh: STeP 是一个混合式语言条件机器人规划框架，由作者团队提出，核心贡献在于将信号时序逻辑（STL）作为高层语言理解与低层动作执行之间的形式化接口，贯穿任务分解、策略选择、底层控制、运行时监控与重规划全流程。系统通过 System 2（语言到
    STL 任务规划）与 System 1（STL 引导执行与监控）的协同，使 VLA 模型能够精确遵循包含空间、时间与逻辑约束的自然语言指令。
  ko: Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle
    to follow precise natural language instructions that encode spatial, temporal, and logical requirements. We propose a
    hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language
    understanding with low-level robot.
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
- step
- signal
- temporal
- logic
- precise
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
  title: 'arXiv:2607.18580 STeP: Signal Temporal Logic for Precise Specifications for Action Generation wit'
  url: https://arxiv.org/abs/2607.18580
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

STeP 是一个混合式语言条件机器人规划框架，由作者团队提出，核心贡献在于将信号时序逻辑（STL）作为高层语言理解与低层动作执行之间的形式化接口，贯穿任务分解、策略选择、底层控制、运行时监控与重规划全流程。系统通过 System 2（语言到 STL 任务规划）与 System 1（STL 引导执行与监控）的协同，使 VLA 模型能够精确遵循包含空间、时间与逻辑约束的自然语言指令。

## 它改变了什么

现有 VLA 模型虽泛化能力强，但缺乏可解释性，且无法内在表示或强制执行指令中的精确空间、时间与逻辑要求。双系统架构（System 2 慢速推理 + System 1 快速动作）的分离本身并未解决“如何表示与执行语言指令中的精确约束”这一核心问题。作者的关键判断是：System 2 不应只做规划，而应将语言派生的任务要求形式化为 System 1 可以监控并在可能时强制执行的表示。

这项工作真正改变的是将 STL 从“规范生成或可行性检查”的静态工具，转变为贯穿整个控制管线的持久表示。此前工作多聚焦于自然语言到 STL 的翻译质量或执行前的公式验证，而 STeP 让 STL 成为任务分解、策略选择、底层控制、运行时监控与重规划的统一接口。这解决了学习型策略不暴露优化接口、难以直接强制执行 STL 约束的问题，也弥补了 MPC 在感知复杂或接触丰富场景中表现不佳的短板，从而提出混合执行模型。

## 方法拆解

### 系统架构
STeP 由两个模块组成：
- **System 2**：负责任务解释、任务规范验证、STL 编译和基于回忆的计划修订。输入为语言指令、当前观测、可用技能与谓词库、回忆上下文；输出为高层子任务序列，每个子任务包含技能名称、接地参数、可选约束与自然语言描述。
- **System 1**：使用选定的底层执行器执行活动子任务，并通过 STL 鲁棒性监控进度，在偏离规范时触发回忆。

### STL 语法与谓词库
- 公式递归定义为 φ ::= ⊤ | μ_c | ¬φ | φ₁∧φ₂ | φ₁∨φ₂ | φ₁⇒φ₂ | F_[a,b]φ | G_[a,b]φ | φ₁ U_[a,b] φ₂，其中 F 为“最终”、G 为“总是”、U 为“直到”。蕴含谓词被显式包含，因为条件结构在语言指令中自然出现。
- 预定义谓词库 P = {μ₁, …, μ_M}，每个 μ_j: Z × Θ_j → ℝ。原子谓词 μ_{j,c}(z_t) := μ_j(z_t) ≥ c，鲁棒性为 ρ(z_t, μ_{j,c}) = μ_j(z_t) − c。语言模型从库中选择谓词而非生成任意信号函数，但添加了灵活的 GoalPosition 谓词以防定义谓词不足。用于梯度优化的谓词需可微。

### 鲁棒性平滑
为将定量语义纳入梯度优化，用 softmax 平滑 max/min 算子：max(x) ≈ Σᵢ xᵢ exp(βxᵢ) / Σᵢ exp(βxᵢ)，min(x) = −max(−x)，β > 0 控制近似尖锐度。

### System 2 流程
1. 执行前运行静态任务规范检查：验证 JSON 模式匹配、技能存在于技能库、参数类型正确、引用对象或区域存在于当前场景、约束受所选技能支持。失败则带错误消息返回 VLM。
2. 确定性 STL 编译器将每个技能模板及其接地参数映射为预定义谓词库上的 STL 公式，插入局部与全局约束（安全约束或时间窗口），将秒级时间间隔转换为控制器时间步。
3. 可选 LLM 一致性检查用于标记公式中的明显逻辑问题（矛盾约束、语言描述与编译任务结构不匹配）。

### System 1 执行与监控
- 每个子任务选择 STL 引导 MPC 控制器或预定义学习策略。MPC 用于可表达为显式几何/时间/安全约束的子任务；学习策略用于难以解析建模或需要更具表现力感知控制的行为。
- STL 监控器评估活动子任务公式的鲁棒性，提供进度与约束满足的连续度量。鲁棒性低于阈值时触发向 System 2 的召回；公式满足时推进到下一子任务或调用 System 2 重规划。

### 历史日志与 MPC 公式
- 历史日志以固定速率更新，存储最近 L 条记录 H_t = {r_{t−L+1}, …, r_t}，每条记录包含观测、状态、子任务自然语言描述、所选低层执行器、STL 鲁棒值、检测到的完成或失败事件。
- MPC 在有限时域 H 上优化动作序列，仅执行第一个动作并在下一时间步重规划。优化目标为 min Σ_{k=t}^{t+H−1} c(s_{k|t}, a_k) − λρ(z_{t:t+H|t}, φ)，约束为 s_{k+1|t} = f(s_{k|t}, a_k)，z_{k|t} = ψ(s_{k|t}, o_t)。由于动力学模型预测未来状态但不预测未来观测，未来信号用预测状态和当前观测 o_t 计算。

### 感知流程
工作区从单次 RGB-D 捕获转换为类型化场景表示。类无关分割器（Segment-Anything）返回实例掩码；每个掩码区域查询视觉语言模型，产生规范对象标签和估计的像素空间质心。每个质心通过校准的相机内参和共配准深度通道反投影，恢复世界坐标系位姿。聚合输出包含规范实体集合、几何（含圆形符号距离近似）、实时测量位姿与平台元数据。

## 关键创新

1. **STL 作为贯穿全管线的持久表示**：不同于现有工作将 STL 仅用于规范生成或执行前验证，STeP 让 STL 同时驱动任务分解、策略选择、底层控制、运行时监控与重规划。这一设计使语言指令中的精确约束在整个执行过程中可被持续监控与强制，而非一次性检查。

2. **混合执行模型（MPC + 学习策略）**：针对 MPC 在感知复杂或接触丰富场景中表现不佳、而学习策略不暴露优化接口的矛盾，STeP 通过 STL 鲁棒性监控实现动态切换。当学习策略偏离规范时，子任务被重新分配给带避障成本项的 MPC；MPC 到达预抓取区域后学习策略恢复接触丰富抓取。这种切换机制由 STL 鲁棒性阈值驱动，而非人工预设。

3. **基于 STL 违反轨迹的重规划**：与基线 VLM-MPC-Cost 使用标量 MPC 成本不同，STeP 将 STL 违反的约束、鲁棒性裕度与违反时间步作为结构化信息返回 System 2。这使得重规划能针对特定失败参数进行修正，而非过度纠正或重新生成完整计划。

## 实验与结果

实验在 UR3e 机械臂真实世界桌面操作平台上进行，所有 VLM 调用使用 GPT-4o。

### RQ1（精确语言跟随）
比较 STeP 与 VLM-MPC-Cost，共 9 个任务，按主要约束类型分组：逻辑、空间、逻辑+空间、时间。STeP 在所有任务类别中取得更高的安全成功率，时间约束上增益最大。（图 4 为图片，具体数字未提取）

### RQ2（学习策略/运动规划切换）
训练 ResNet-based BC 策略，使用 30 个演示，任务为从箱子中取立方体，测试时在接近路径上引入障碍物。STL 监控器跟踪机械臂是否保持与障碍物的安全距离；鲁棒性低于阈值时子任务从学习策略重新分配给带避障成本项的 MPC。

| 指标 | STeP（30 次试验） | 无切换 BC | 仅 MPC |
|------|------------------|-----------|--------|
| 检测到碰撞 | 29 | 28 次碰撞 | — |
| 通过 MPC 改道 | 25 | — | — |
| 完成抓取 | 22 | — | 24 次避障但抓取失败 |

### RQ3（少样本重规划）
任务为堆叠三个立方体，失败最常发生在第三次放置。STeP 在 20 次试验中 16 次首次尝试撞倒堆叠；STL 监控器记录违反的约束（Safe End-Effector）、鲁棒性裕度、违反时间步，并连同更新场景快照返回 System 2。第二次尝试中 16 次失败有 12 次被纠正，三次尝试内 14 次被纠正。VLM-MPC-Cost 在 20 次试验中 18 次初始失败；因用标量 MPC 成本替代 STL 违反轨迹，18 次失败中仅 7 次在两次尝试内纠正，9 次在三次尝试内纠正。

| 指标 | STeP | VLM-MPC-Cost |
|------|------|--------------|
| 初始失败（20 次试验） | 16 | 18 |
| 两次尝试内纠正 | 12/16 | 7/18 |
| 三次尝试内纠正 | 14/16 | 9/18 |

## 边界与局限

作者明确承认以下局限：仅 MPC 技能直接针对 STL 规范优化动作，学习策略由 STL 鲁棒性监控，但尚未将规范用作推理时控制信号。高层计划表示为子任务序列，限制了与完整自动机相比可表达的分支或循环行为范围。多个系统组件刻意保持简单，包括 MPC 求解器、抓取姿态选择和真实世界执行循环，使系统在杂乱环境中表现不佳。VLM 仍可能产生不完整或不正确的任务规范，尤其是场景描述缺少精细空间细节时。未来工作可探索用世界模型预测未来观测（当前 MPC 用预测状态和当前观测计算未来信号）。

## 工程启示

复现 STeP 时，首先核对感知管线的精度：类无关分割器（Segment-Anything）返回的实例掩码经 VLM 标注后，质心反投影的世界坐标精度直接影响 GoalPosition 谓词与避障约束的有效性。最容易踩坑的是 STL 编译器中秒级时间间隔到控制器时间步的转换——若控制器频率与编译假设不匹配，时间窗口约束会系统性偏移。

对于下游团队，建议优先验证谓词库的覆盖度：预定义谓词库 P = {μ₁, …, μ_M} 虽含灵活的 GoalPosition 谓词，但若任务涉及自定义几何约束（如非圆形障碍物），需扩展谓词库并确保其可微性。混合执行切换的阈值设定是关键超参数——鲁棒性阈值过松会导致碰撞漏检，过紧则频繁触发重规划。RQ2 中 29/30 的碰撞检测率与 22/30 的抓取成功率表明，切换机制有效但仍有改进空间，建议在部署前针对具体任务标定阈值。重规划时，STL 违反轨迹的结构化信息（违反约束、鲁棒性裕度、违反时间步）比标量成本更有助于精准修正，这是与基线 VLM-MPC-Cost 的核心差异。

## Overview
Vision-language-action (VLA) models have shown impressive generalization, but often lack interpretability and can struggle to follow precise natural language instructions that encode spatial, temporal, and logical requirements. We propose a hierarchical framework that uses Signal Temporal Logic (STL) as a shared representation connecting high-level language understanding with low-level robot execution. A high-level policy leverages a VLM to decompose language instructions into high-level subtasks, generate STL specifications for each subtask, and choose a low-level policy for executing each subtask. The STL specifications translate language-derived intent into precise constraints, and the low-level policy selection determines whether those constraints are enforced directly through STL-guided model-predictive control or monitored during execution of a learned policy for perceptually complex, or contact-rich behaviors. By integrating STL into plan validation, low-level policy, subtask monitoring, and replanning, our framework enables language-derived plans to be checked, optimized, and revised at runtime using a common formal structure. We evaluate the approach on a real-world tabletop domain, demonstrating how formal specifications can improve the precision, reliability, and interpretability of language-conditioned robot planning.

## 参考
- https://arxiv.org/abs/2607.18580

## 개요

STeP은 저자 팀이 제안한 하이브리드 언어 조건 로봇 플래닝 프레임워크로, 핵심 기여는 신호 시제 논리(STL)를 고수준 언어 이해와 저수준 동작 실행 사이의 형식적 인터페이스로 사용하여 작업 분해, 정책 선택, 저수준 제어, 런타임 모니터링 및 재플래닝 전 과정에 걸쳐 활용한다는 점입니다. 시스템은 System 2(언어-STL 작업 플래닝)와 System 1(STL 기반 실행 및 모니터링)의 협력을 통해 VLA 모델이 공간, 시간 및 논리적 제약을 포함하는 자연어 명령을 정밀하게 따를 수 있게 합니다.

## 무엇을 바꾸었는가

기존 VLA 모델은 일반화 능력이 뛰어나지만 해석 가능성이 부족하고, 명령에 포함된 정밀한 공간, 시간 및 논리적 요구 사항을 내재적으로 표현하거나 강제로 실행할 수 없습니다. 이중 시스템 아키텍처(System 2 느린 추론 + System 1 빠른 동작)의 분리 자체는 "언어 명령의 정밀한 제약을 어떻게 표현하고 실행할 것인가"라는 핵심 문제를 해결하지 못합니다. 저자의 핵심 판단은 System 2가 단순히 플래닝만 수행하는 것이 아니라, 언어에서 파생된 작업 요구 사항을 System 1이 모니터링하고 가능할 때 강제로 실행할 수 있는 표현으로 형식화해야 한다는 것입니다.

이 작업이 진정으로 바꾼 것은 STL을 "사양 생성 또는 실현 가능성 검사"를 위한 정적 도구에서 제어 파이프라인 전체를 관통하는 지속적 표현으로 전환한 것입니다. 이전 연구는 주로 자연어-STL 번역 품질이나 실행 전 공식 검증에 초점을 맞췄지만, STeP은 STL을 작업 분해, 정책 선택, 저수준 제어, 런타임 모니터링 및 재플래닝의 통합 인터페이스로 만듭니다. 이는 학습 기반 정책이 최적화 인터페이스를 노출하지 않아 STL 제약을 직접 강제하기 어려운 문제를 해결하고, MPC가 인식 복잡성이나 접촉이 많은 시나리오에서 성능이 저하되는 단점을 보완하여 하이브리드 실행 모델을 제안합니다.

## 방법 분해

### 시스템 아키텍처
STeP은 두 개의 모듈로 구성됩니다:
- **System 2**: 작업 해석, 작업 사양 검증, STL 컴파일 및 회상 기반 계획 수정을 담당합니다. 입력은 언어 명령, 현재 관측, 사용 가능한 스킬 및 술어 라이브러리, 회상 컨텍스트이며, 출력은 각 하위 작업에 스킬 이름, 접지 파라미터, 선택적 제약 및 자연어 설명이 포함된 고수준 하위 작업 시퀀스입니다.
- **System 1**: 선택된 저수준 실행기를 사용하여 활성 하위 작업을 실행하고, STL 견고성을 통해 진행 상황을 모니터링하며, 사양에서 벗어날 때 회상을 트리거합니다.

### STL 문법 및 술어 라이브러리
- 공식은 재귀적으로 φ ::= ⊤ | μ_c | ¬φ | φ₁∧φ₂ | φ₁∨φ₂ | φ₁⇒φ₂ | F_[a,b]φ | G_[a,b]φ | φ₁ U_[a,b] φ₂로 정의되며, 여기서 F는 "최종", G는 "항상", U는 "까지"를 의미합니다. 조건부 구조가 언어 명령에서 자연스럽게 나타나므로 함의 술어가 명시적으로 포함됩니다.
- 사전 정의된 술어 라이브러리 P = {μ₁, …, μ_M}, 각 μ_j: Z × Θ_j → ℝ. 원자 술어 μ_{j,c}(z_t) := μ_j(z_t) ≥ c, 견고성은 ρ(z_t, μ_{j,c}) = μ_j(z_t) − c. 언어 모델은 임의의 신호 함수를 생성하는 대신 라이브러리에서 술어를 선택하지만, 정의된 술어가 부족한 경우를 대비해 유연한 GoalPosition 술어가 추가됩니다. 경사 최적화에 사용되는 술어는 미분 가능해야 합니다.

### 견고성 평활화
정량적 의미론을 경사 최적화에 통합하기 위해 softmax로 max/min 연산자를 평활화합니다: max(x) ≈ Σᵢ xᵢ exp(βxᵢ) / Σᵢ exp(βxᵢ), min(x) = −max(−x), β > 0은 근사 예리함을 제어합니다.

### System 2 프로세스
1. 실행 전 정적 작업 사양 검사: JSON 스키마 일치, 스킬이 스킬 라이브러리에 존재하는지, 파라미터 유형이 올바른지, 참조된 객체 또는 영역이 현재 장면에 존재하는지, 제약이 선택된 스킬에서 지원되는지 검증합니다. 실패 시 오류 메시지와 함께 VLM으로 반환됩니다.
2. 결정적 STL 컴파일러는 각 스킬 템플릿과 접지 파라미터를 사전 정의된 술어 라이브러리의 STL 공식으로 매핑하고, 로컬 및 전역 제약(안전 제약 또는 시간 창)을 삽입하며, 초 단위 시간 간격을 컨트롤러 시간 단계로 변환합니다.
3. 선택적 LLM 일관성 검사는 공식에서 명백한 논리적 문제(모순된 제약, 언어 설명과 컴파일된 작업 구조 간 불일치)를 표시합니다.

### System 1 실행 및 모니터링
- 각 하위 작업은 STL 기반 MPC 컨트롤러 또는 사전 정의된 학습 정책을 선택합니다. MPC는 명시적 기하/시간/안전 제약으로 표현할 수 있는 하위 작업에 사용되고, 학습 정책은 해석적으로 모델링하기 어렵거나 더 표현력 있는 인식 제어가 필요한 동작에 사용됩니다.
- STL 모니터는 활성 하위 작업 공식의 견고성을 평가하여 진행 상황과 제약 충족의 연속적 측정을 제공합니다. 견고성이 임계값 아래로 떨어지면 System 2로의 회상이 트리거되고, 공식이 충족되면 다음 하위 작업으로 진행하거나 System 2 재플래닝을 호출합니다.

### 히스토리 로그 및 MPC 공식
- 히스토리 로그는 고정 속도로 업데이트되며 최근 L개의 레코드 H_t = {r_{t−L+1}, …, r_t}를 저장합니다. 각 레코드에는 관측, 상태, 하위 작업 자연어 설명, 선택된 저수준 실행기, STL 견고성 값, 감지된 완료 또는 실패 이벤트가 포함됩니다.
- MPC는 유한 시간 지평 H에서 동작 시퀀스를 최적화하고 첫 번째 동작만 실행한 후 다음 시간 단계에서 재플래닝합니다. 최적화 목표는 min Σ_{k=t}^{t+H−1} c(s_{k|t}, a_k) − λρ(z_{t:t+H|t}, φ)이며, 제약은 s_{k+1|t} = f(s_{k|t}, a_k), z_{k|t} = ψ(s_{k|t}, o_t)입니다. 동역학 모델은 미래 상태를 예측하지만 미래 관측은 예측하지 않으므로, 미래 신호는 예측 상태와 현재 관측 o_t로 계산됩니다.

### 인식 프로세스
작업 공간은 단일 RGB-D 캡처에서 타입화된 장면 표현으로 변환됩니다. 클래스 비의존 분할기(Segment-Anything)는 인스턴스 마스크를 반환하고, 각 마스크 영역은 비전 언어 모델에 쿼리되어 정규 객체 레이블과 추정된 픽셀 공간 중심을 생성합니다. 각 중심은 보정된 카메라 내부 파라미터와 공동 정합 깊이 채널을 통해 역투영되어 세계 좌표계 자세를 복원합니다. 집계 출력에는 정규 엔티티 집합, 기하(원형 부호 거리 근사 포함), 실시간 측정 자세 및 플랫폼 메타데이터가 포함됩니다.

## 핵심 혁신

1. **파이프라인 전체를 관통하는 지속적 표현으로서의 STL**: 기존 연구가 STL을 사양 생성 또는 실행 전 검증에만 사용한 반면, STeP은 STL이 작업 분해, 정책 선택, 저수준 제어, 런타임 모니터링 및 재플래닝을 동시에 구동하게 합니다. 이 설계는 언어 명령의 정밀한 제약이 일회성 검사가 아닌 전체 실행 과정에서 지속적으로 모니터링되고 강제될 수 있게 합니다.

2. **하이브리드 실행 모델(MPC + 학습 정책)**: MPC가 인식 복잡성이나 접촉이 많은 시나리오에서 성능이 저하되고 학습 정책이 최적화 인터페이스를 노출하지 않는 모순에 대해, STeP은 STL 견고성 모니터링을 통한 동적 전환을 구현합니다. 학습 정책이 사양에서 벗어나면 하위 작업은 장애물 회피 비용 항이 있는 MPC로 재할당되고, MPC가 사전 그립 영역에 도달하면 학습 정책이 접촉이 많은 그립을 재개합니다. 이 전환 메커니즘은 수동 사전 설정이 아닌 STL 견고성 임계값에 의해 구동됩니다.

3. **STL 위반 궤적 기반 재플래닝**: 기준 VLM-MPC-Cost가 스칼라 MPC 비용을 사용하는 것과 달리, STeP은 STL 위반 제약, 견고성 여유 및 위반 시간 단계를 구조화된 정보로 System 2에 반환합니다. 이를 통해 재플래닝이 과도한 수정이나 전체 계획 재생성 대신 특정 실패 파라미터를 대상으로 수정할 수 있습니다.

## 실험 및 결과

실험은 UR3e 로봇 팔 실제 세계 데스크톱 조작 플랫폼에서 수행되었으며, 모든 VLM 호출은 GPT-4o를 사용했습니다.

### RQ1(정밀 언어 따르기)
STeP과 VLM-MPC-Cost를 비교했으며, 총 9개 작업을 주요 제약 유형별로 그룹화했습니다: 논리, 공간, 논리+공간, 시간. STeP은 모든 작업 범주에서 더 높은 안전 성공률을 달성했으며, 시간 제약에서 가장 큰 이득을 보였습니다. (그림 4는 이미지이며 구체적인 숫자는 추출되지 않음)

### RQ2(학습 정책/운동 계획 전환)
30개의 데모로 ResNet 기반 BC 정책을 훈련했으며, 작업은 상자에서 큐브를 꺼내는 것이었고, 테스트 시 접근 경로에 장애물을 도입했습니다. STL 모니터는 로봇 팔이 장애물과 안전 거리를 유지하는지 추적하고, 견고성이 임계값 아래로 떨어지면 하위 작업이 학습 정책에서 장애물 회피 비용 항이 있는 MPC로 재할당됩니다.

| 지표 | STeP(30회 시도) | 전환 없는 BC | MPC 전용 |
|------|------------------|-----------|--------|
| 충돌 감지 | 29 | 28회 충돌 | — |
| MPC 경로 변경 | 25 | — | — |
| 그립 완료 | 22 | — | 24회 장애물 회피했지만 그립 실패 |

### RQ3(소수 샷 재플래닝)
작업은 세 개의 큐브를 쌓는 것이었고, 실패는 세 번째 배치에서 가장 자주 발생했습니다. STeP은 20회 시도 중 16회에서 첫 시도에 쌓인 큐브를 넘어뜨렸습니다. STL 모니터는 위반된 제약(Safe End-Effector), 견고성 여유, 위반 시간 단계를 기록하고 업데이트된 장면 스냅샷과 함께 System 2로 반환합니다. 두 번째 시도에서 16회 실패 중 12회가 수정되었고, 세 번의 시도 내에 14회가 수정되었습니다. VLM-MPC-Cost는 20회 시도 중 18회에서 초기 실패가 발생했습니다. 스칼라 MPC 비용으로 STL 위반 궤적을 대체했기 때문에 18회 실패 중 두 번의 시도 내에 7회만 수정되었고, 세 번의 시도 내에 9회가 수정되었습니다.

| 지표 | STeP | VLM-MPC-Cost |
|------|------|--------------|
| 초기 실패(20회 시도) | 16 | 18 |
| 두 번의 시도 내 수정 | 12/16 | 7/18 |
| 세 번의 시도 내 수정 | 14/16 | 9/18 |

## 경계 및 한계

저자는 다음 한계를 명시적으로 인정합니다: MPC 스킬만 STL 사양에 대해 직접 동작을 최적화하고, 학습 정책은 STL 견고성으로 모니터링되지만 사양을 추론 시간 제어 신호로 사용하지는 않습니다. 고수준 계획은 하위 작업 시퀀스로 표현되어 완전한 오토마타와 비교하여 표현 가능한 분기 또는 루프 동작 범위가 제한됩니다. 여러 시스템 구성 요소가 의도적으로 단순하게 유지되었으며, 여기에는 MPC 솔버, 그립 자세 선택 및 실제 세계 실행 루프가 포함되어 혼잡한 환경에서 시스템 성능이 저하됩니다. VLM은 특히 장면 설명에 미세한 공간 세부 정보가 부족할 때 불완전하거나 부정확한 작업 사양을 여전히 생성할 수 있습니다. 향후 작업은 세계 모델을 사용하여 미래 관측을 예측하는 방법(현재 MPC는 예측 상태와 현재 관측으로 미래 신호를 계산)을 탐구할 수 있습니다.

## 공학적 시사점

STeP을 재현할 때 먼저 인식 파이프라인의 정밀도를 확인하십시오: 클래스 비의존 분할기(Segment-Anything)가 반환한 인스턴스 마스크를 VLM으로 주석 처리한 후, 중심 역투영의 세계 좌표 정밀도는 GoalPosition 술어와 장애물 회피 제약의 유효성에 직접적인 영향을 미칩니다. 가장 쉽게 함정에 빠질 수 있는 부분은 STL 컴파일러에서 초 단위 시간 간격을 컨트롤러 시간 단계로 변환하는 것입니다 — 컨트롤러 주파수와 컴파일 가정이 일치하지 않으면 시간 창 제약이 체계적으로 편향됩니다.

다운스트림 팀에게는 술어 라이브러리의 적용 범위를 우선 검증할 것을 권장합니다: 사전 정의된 술어 라이브러리 P = {μ₁, …, μ_M}에는 유연한 GoalPosition 술어가 포함되어 있지만, 작업에 사용자 정의 기하 제약(예: 비원형 장애물)이 포함된 경우 술어 라이브러리를 확장하고 미분 가능성을 보장해야 합니다. 하이브리드 실행 전환의 임계값 설정은 핵심 하이퍼파라미터입니다 — 견고성 임계값이 너무 느슨하면 충돌 누락이 발생하고, 너무 빡빡하면 빈번한 재플래닝이 트리거됩니다. RQ2의 29/30 충돌 감지율과 22/30 그립 성공률은 전환 메커니즘이 효과적이지만 여전히 개선 여지가 있음을 보여주며, 배포 전에 특정 작업에 대해 임계값을 보정할 것을 권장합니다. 재플래닝 시 STL 위반 궤적의 구조화된 정보(위반 제약, 견고성 여유, 위반 시간 단계)는 스칼라 비용보다 정밀한 수정에 더 유용하며, 이는 기준 VLM-MPC-Cost와의 핵심 차이입니다.
