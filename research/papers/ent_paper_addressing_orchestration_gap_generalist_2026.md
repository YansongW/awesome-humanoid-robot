---
$id: ent_paper_addressing_orchestration_gap_generalist_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Addressing the Orchestration Gap in Generalist Robots via Physical Agency
  zh: Addressing the Orchestration Gap in Generalist Robots via Physical Agency
  ko: Addressing the Orchestration Gap in Generalist Robots via Physical Agency
summary:
  en: General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success
    detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities
    into the learned policy via large-scale pre-training. Instead, we show that these capabilities can be decomposed into
    a general language-conditioned policy/control.
  zh: Pigey（Physical Agency）是一个闭环推理时编排器，由前沿VLM作为智能体，调度冻结的TAMP后端与VLA策略后端，解决通用机器人任务中的“编排差距”。核心贡献在于将高层推理（任务分解、验证、恢复）从低层运动控制中分离，使冻结策略在零微调下平均成功率提升超4倍（12.8%
    → 53.3%），真实机器人30任务总体成功率97.3%。
  ko: General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success
    detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities
    into the learned policy via large-scale pre-training. Instead, we show that these capabilities can be decomposed into
    a general language-conditioned policy/control.
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
- addressing
- orchestration
- gap
- generalist
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
  title: arXiv:2607.21725 Addressing the Orchestration Gap in Generalist Robots via Physical Agency
  url: https://arxiv.org/abs/2607.21725
  date: '2026-07-23'
  accessed_at: '2026-08-05'
---

## 概述

Pigey（Physical Agency）是一个闭环推理时编排器，由前沿VLM作为智能体，调度冻结的TAMP后端与VLA策略后端，解决通用机器人任务中的“编排差距”。核心贡献在于将高层推理（任务分解、验证、恢复）从低层运动控制中分离，使冻结策略在零微调下平均成功率提升超4倍（12.8% → 53.3%），真实机器人30任务总体成功率97.3%。

## 它改变了什么

它改变了“单一模型端到端解决一切”的范式假设。现有VLA（如π₀.₅）在接地、推理、恢复上系统性失败，而TAMP在需要世界知识与条件逻辑的任务上同样崩溃——问题不在单个技能，而在“决定做什么、检查是否成功、失败时修复”的闭环缺失。作者用“编排差距”命名这一现象：冻结的运动技能单独实现与在智能体循环内实现之间存在本质差异。

这项工作的真正改变在于：它把编排器当作一等公民，而非附属模块。不是让VLM“辅助”策略，而是让VLM成为决策主体，策略退化为可替换的工具。这颠覆了“越大越好”的预训练思路——与其训练一个全能网络，不如组合现有冻结组件，用推理时计算换取任务级能力。对工业界而言，这意味着昂贵的机器人数据不必用于教授任务逻辑，而可聚焦于运动技能本身。

## 方法拆解

### 系统架构
Pigey = VLM编排器（ϕ）+ 两个冻结后端 + 确定性失败注解。形式化：ϕ: 𝒪 × ℋ × ℐ → 𝒯，后端 π_b: 𝒪 × 𝒮 → 𝒜_motor（b ∈ {tamp, vla}），后端只接收短子目标s，从不接收完整指令I。

### 五个工具（真实机器人）
- **Perceive**：返回相机视图、机器人状态、检测到的物体标签集
- **Pick(ℓ)**：TAMP后端抓取（detect→segment→depth→M2T2 grasp→cuRobo plan→execute）
- **DropAbove(ℓ)**：TAMP后端放置（RELATIVE/ABSOLUTE两种模式）
- **VLARollout(s)**：VLA后端执行子目标（动作块长度15，每H=8步重新推理，K=300控制步/次）
- **Done**：终止（必须紧接Perceive）

### 双重验证机制
确定性信号（is_grasped来自夹爪宽度传感器）+ 视觉信号（腕部图像确认目标在夹爪中且从桌面消失）。保守组合：后端报告成功但传感器显示空夹爪，则覆盖为失败。

### 路由规则（7条）
1. 抽象/多物体任务先Perceive再行动；Pick/DropAbove参数必须是最近Perceive的精确标签
2. 刚性物体用TAMP抓取并验证
3. 未验证的Pick重试一次，第二次失败升级到VLARollout
4. 可变形物体直接走VLA，跳过TAMP
5. 放置用DropAbove，目标位置来自缓存
6. 双向回退：VLARollout无进展可回退到TAMP Pick，反之亦然
7. 停止条件：仅在验证任务谓词后调用Done

### 关键设计决策
- **精确字符串规则**：防止检测器被幻觉目标名污染
- **预Done的Perceive**：硬性系统级不变量
- **确定性注解**：减少VLM从像素推断低层失败的需求
- **提示模板**：不教模型如何操作，只约束何时调用哪个原语以及Done前验证什么

## 关键创新

1. **编排差距的显式化与工具化**：首次将“高层推理与低层控制的分离”形式化为可操作的智能体循环，而非概念讨论。五个工具+两条路由规则覆盖了感知、规划、执行、验证、恢复的完整闭环，这是VLA扩展、代码即策略、推理VLA各自只解决部分问题所缺失的。

2. **双向升级机制**：TAMP失败可升级到VLA，VLA无进展可回退到TAMP。这打破了“单一后端最优”的假设，让编排器根据任务性质动态选择工具。刚性物体走TAMP（精确），可变形物体走VLA（闭环），失败时交叉切换——这是对“工具选择”问题的实用主义回答。

3. **确定性验证与VLM判断的混合**：用夹爪宽度传感器（确定性）与腕部图像（视觉）双重信号验证抓取，而非依赖VLM从像素推断。这避免了VLM在低层状态估计上的不可靠，同时保留了其在高层语义判断上的优势。验证器假成功仅2次（150次试验中），证明该混合策略的有效性。

## 实验与结果

### 真实机器人（30任务，每任务5次试验）
| 类别 | π₀.₅ | TiPToP | Pigey |
|---|---|---|---|
| Pick-and-place | 95% | 80% | 100% |
| World knowledge | 0% | 90% | 100% |
| Conditional logic | 0% | 95% | 100% |
| Multi-step reasoning | 0% | 25% | 100% |
| Spatial reasoning | 20% | 75% | 100% |
| Obstacle reasoning | 0% | 0% | 90% |
| Error recovery | 10% | 0% | 90% |
| Long-horizon memory | 0% | 0% | 100% |
| **Overall** | **16.7%** | **48.7%** | **97.3%** |

### LIBERO-PRO仿真（成功率%）
| 方法 | Obj.swap | Obj.task | Sp.swap | Sp.task | Goal.swap | Goal.task | Mean |
|---|---|---|---|---|---|---|---|
| π₀ | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| π₀.₅ | 17 | 1 | 20 | 1 | 38 | 0 | 12.8 |
| CaP-Agent0 | 22 | 18 | 12 | 14 | 26 | 17 | 18.2 |
| Pigey+Claude Opus 4.7 | 54 | 54 | 66 | 80 | 44 | 22 | 53.3 |

### 首次失败模式分布（150次试验/方法）
| 失败模式 | π₀.₅ | TiPToP | Pigey |
|---|---|---|---|
| 接地 | 86 | 5 | 0 |
| 推理/规划 | 38 | 65 | 0 |
| 抓取执行 | 1 | 7 | 2 |
| 验证器假成功 | 0 | 0 | 2 |
| 总失败 | 125 | 77 | 4 |

### 推理受限探针
原始VLA平均4.6%，Pigey达到96.9%（使用相同VLA）——证明提升来自编排而非策略本身。

关键含义：Pigey将冻结策略成功率从12.8%提升至53.3%（由表内数值12.8→53.3计算，超4×），且无任务特定微调。推理器扫描显示，即使最弱的推理器（GPT-5.5 low，均值44.3%）也远超所有非编排基线，说明编排框架的鲁棒性。

## 边界与局限

- **受后端能力上限约束**：Pigey可以补偿弱策略，但存在由低层工具“支撑”设定的上限。若TAMP与VLA都无法执行某类动作（如高精度装配），编排器无能为力。
- **验证不完美**：遮挡造成的部分可观测性可能隐藏糟糕的抓取，允许虚假成功向下游传播（150次试验中出现2次验证器假成功）。
- **延迟与成本**：依赖API调用编排，每次试验3-15次VLM调用，成本$0.02至$0.50，墙钟时间2-6分钟。对低延迟或高速应用具有挑战性。
- **未做之事**：未收集额外数据或后训练；未训练专用模块（记忆、验证器、奖励模型、高层规划器）。OB3（doll surrounded）仅3/5成功，是唯一低于5/5的任务。
- **论文未明确**：对可变形物体操作的扩展验证、多机器人平台泛化、以及推理器在更复杂长时程任务（>10分钟）中的稳定性。

## 工程启示

- **先核对后端能力边界**：Pigey的成功依赖TAMP与VLA的互补性。复现前务必确认你的TAMP能处理刚性物体精确拾放、VLA能处理可变形物体闭环控制——若两者能力重叠或都有盲区，编排收益会大幅缩水。
- **最容易踩坑的是验证机制**：双重信号（夹爪宽度+腕部图像）是防止假成功的关键。若你的平台没有夹爪宽度传感器，需设计等效的确定性信号（如力传感器阈值），否则验证器假成功会污染下游决策。
- **提示模板的纪律性比模型能力更重要**：精确字符串规则、预Done的Perceive、工具调用结尾——这些硬性约束比VLM本身的选择更影响成功率。复现时先严格照搬模板结构，再考虑针对你的任务调整路由规则。
- **推理器选择有边际收益**：从GPT-5.5 low（44.3%）到Claude Opus 4.7（53.3%），推理器能力提升带来约9个百分点增益。若预算有限，先用中等推理器验证框架，再升级到最强模型。
- **仿真与真实的差距主要在感知**：LIBERO-PRO中Pigey均值53.3%，真实机器人97.3%——仿真中检测器噪声和物体多样性更低，但任务谓词更严格。复现时先在仿真调试路由逻辑，再迁移到真实平台处理感知噪声。

## Overview
General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities into the learned policy via large-scale pre-training. Instead, we show that these capabilities can be decomposed into a general language-conditioned policy/control agent and a high-level agent manager/orchestrator. Rather than training policies to reason via pre-training, we build a closed-loop physical agent orchestrator that can do high-level planning, decompose the goal into achievable subgoals, command low-level motor commands, track and verify the outcome from low-level observations, and recover from failures. Our Physical Agency orchestrator (Pigey) can control existing vision-language-action (VLA) policies as well as parametrized skills to solve complex reasoning tasks in the real world, without any additional data collection or post-training. We evaluate Pigey extensively across simulation benchmarks and challenging real-world robotic manipulation tasks, and demonstrate significant performance improvements over existing generalist policies. On LIBERO-PRO, Pigey advances the state-of-the-art by over 4x (12.8% -> 53.3%) with no task-specific fine-tuning. On a real robot, Pigey lifts the frozen policy from near-zero to over 90% on reasoning-limited tasks. We call the difference between what frozen motor skills achieve alone and inside the agentic loop the orchestration gap.

## 参考
- https://arxiv.org/abs/2607.21725

## 개요

Pigey(Physical Agency)는 최첨단 VLM을 에이전트로 사용하여 동결된 TAMP 백엔드와 VLA 정책 백엔드를 조율하는 폐루프 추론 시 오케스트레이터로, 일반 로봇 작업에서의 "오케스트레이션 격차"를 해결합니다. 핵심 기여는 고수준 추론(작업 분해, 검증, 복구)을 저수준 운동 제어에서 분리하여, 동결 정책이 제로 미세 조정으로 평균 성공률을 4배 이상 향상(12.8% → 53.3%)시키고, 실제 로봇 30개 작업에서 전체 성공률 97.3%를 달성한 것입니다.

## 그것이 바꾼 것

이것은 "단일 모델의 엔드투엔드가 모든 것을 해결한다"는 패러다임 가정을 바꿉니다. 기존 VLA(예: π₀.₅)는 접지, 추론, 복구에서 체계적으로 실패하는 반면, TAMP는 세계 지식과 조건부 논리가 필요한 작업에서도 붕괴합니다. 문제는 개별 스킬이 아니라 "무엇을 할지 결정하고, 성공 여부를 확인하고, 실패 시 수정하는" 폐루프의 부재입니다. 저자들은 이 현상을 "오케스트레이션 격차"라고 명명했습니다: 동결된 운동 스킬이 단독으로 구현될 때와 에이전트 루프 내에서 구현될 때의 본질적 차이입니다.

이 작업의 진정한 변화는 오케스트레이터를 부속 모듈이 아닌 일등 시민으로 취급한다는 점입니다. VLM이 정책을 "보조"하는 것이 아니라 VLM이 의사 결정 주체가 되고, 정책은 교체 가능한 도구로 격하됩니다. 이는 "클수록 좋다"는 사전 학습 접근 방식을 뒤집습니다—전능한 네트워크를 훈련하는 대신 기존 동결 구성 요소를 조합하고, 추론 시 계산으로 작업 수준 능력을 얻는 것입니다. 산업계 관점에서 이는 값비싼 로봇 데이터가 작업 논리를 가르치는 데 사용될 필요 없이 운동 스킬 자체에 집중할 수 있음을 의미합니다.

## 방법 분해

### 시스템 아키텍처
Pigey = VLM 오케스트레이터(ϕ) + 두 개의 동결 백엔드 + 결정적 실패 주석. 형식화: ϕ: 𝒪 × ℋ × ℐ → 𝒯, 백엔드 π_b: 𝒪 × 𝒮 → 𝒜_motor (b ∈ {tamp, vla}), 백엔드는 짧은 하위 목표 s만 수신하며 전체 명령 I는 절대 수신하지 않습니다.

### 다섯 가지 도구(실제 로봇)
- **Perceive**: 카메라 뷰, 로봇 상태, 감지된 객체 레이블 집합 반환
- **Pick(ℓ)**: TAMP 백엔드 그리퍼(detect→segment→depth→M2T2 grasp→cuRobo plan→execute)
- **DropAbove(ℓ)**: TAMP 백엔드 배치(RELATIVE/ABSOLUTE 두 가지 모드)
- **VLARollout(s)**: VLA 백엔드 하위 목표 실행(액션 블록 길이 15, H=8단계마다 재추론, K=300 제어 단계/회)
- **Done**: 종료(반드시 Perceive 직후)

### 이중 검증 메커니즘
결정적 신호(그리퍼 폭 센서의 is_grasped) + 시각적 신호(손목 이미지로 대상이 그리퍼에 있고 테이블에서 사라졌는지 확인). 보수적 조합: 백엔드가 성공을 보고하지만 센서가 빈 그리퍼를 표시하면 실패로 덮어씁니다.

### 라우팅 규칙(7가지)
1. 추상/다중 객체 작업은 행동 전에 먼저 Perceive; Pick/DropAbove 매개변수는 가장 최근 Perceive의 정확한 레이블이어야 함
2. 강체는 TAMP로 그리핑하고 검증
3. 검증되지 않은 Pick은 한 번 재시도, 두 번째 실패 시 VLARollout으로 업그레이드
4. 변형 가능 객체는 직접 VLA로, TAMP 건너뜀
5. 배치는 DropAbove 사용, 목표 위치는 캐시에서
6. 양방향 폴백: VLARollout이 진전이 없으면 TAMP Pick으로 폴백 가능, 그 반대도 가능
7. 중지 조건: 작업 술어 검증 후에만 Done 호출

### 핵심 설계 결정
- **정확한 문자열 규칙**: 감지기가 환각 목표 이름에 오염되는 것 방지
- **Done 전 Perceive**: 하드 시스템 수준 불변식
- **결정적 주석**: VLM이 픽셀에서 저수준 실패를 추론할 필요성 감소
- **프롬프트 템플릿**: 모델에게 조작 방법을 가르치지 않고, 언제 어떤 프리미티브를 호출하고 Done 전에 무엇을 검증할지만 제약

## 핵심 혁신

1. **오케스트레이션 격차의 명시화와 도구화**: "고수준 추론과 저수준 제어의 분리"를 개념적 논의가 아닌 작동 가능한 에이전트 루프로 처음 형식화. 다섯 가지 도구와 두 가지 라우팅 규칙이 지각, 계획, 실행, 검증, 복구의 완전한 폐루프를 포괄하며, 이는 VLA 확장, 코드로서의 정책, 추론 VLA가 각각 부분 문제만 해결하는 데서 누락된 부분입니다.

2. **양방향 업그레이드 메커니즘**: TAMP 실패는 VLA로 업그레이드 가능, VLA의 진전 없음은 TAMP로 폴백 가능. 이는 "단일 백엔드 최적" 가정을 깨고, 오케스트레이터가 작업 특성에 따라 도구를 동적으로 선택하게 합니다. 강체는 TAMP(정밀), 변형 가능 객체는 VLA(폐루프), 실패 시 교차 전환—이는 "도구 선택" 문제에 대한 실용주의적 답변입니다.

3. **결정적 검증과 VLM 판단의 혼합**: 그리퍼 폭 센서(결정적)와 손목 이미지(시각적)의 이중 신호로 그리핑을 검증하며, VLM이 픽셀에서 추론하는 것을 의존하지 않습니다. 이는 저수준 상태 추정에서 VLM의 불신뢰성을 피하면서 고수준 의미론적 판단에서의 장점을 유지합니다. 검증기 거짓 성공은 150회 시행 중 2회뿐으로, 이 혼합 전략의 효과를 증명합니다.

## 실험과 결과

### 실제 로봇(30개 작업, 작업당 5회 시행)
| 범주 | π₀.₅ | TiPToP | Pigey |
|---|---|---|---|
| Pick-and-place | 95% | 80% | 100% |
| 세계 지식 | 0% | 90% | 100% |
| 조건부 논리 | 0% | 95% | 100% |
| 다단계 추론 | 0% | 25% | 100% |
| 공간 추론 | 20% | 75% | 100% |
| 장애물 추론 | 0% | 0% | 90% |
| 오류 복구 | 10% | 0% | 90% |
| 장기 메모리 | 0% | 0% | 100% |
| **전체** | **16.7%** | **48.7%** | **97.3%** |

### LIBERO-PRO 시뮬레이션(성공률 %)
| 방법 | Obj.swap | Obj.task | Sp.swap | Sp.task | Goal.swap | Goal.task | 평균 |
|---|---|---|---|---|---|---|---|
| π₀ | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| π₀.₅ | 17 | 1 | 20 | 1 | 38 | 0 | 12.8 |
| CaP-Agent0 | 22 | 18 | 12 | 14 | 26 | 17 | 18.2 |
| Pigey+Claude Opus 4.7 | 54 | 54 | 66 | 80 | 44 | 22 | 53.3 |

### 최초 실패 모드 분포(방법당 150회 시행)
| 실패 모드 | π₀.₅ | TiPToP | Pigey |
|---|---|---|---|
| 접지 | 86 | 5 | 0 |
| 추론/계획 | 38 | 65 | 0 |
| 그리핑 실행 | 1 | 7 | 2 |
| 검증기 거짓 성공 | 0 | 0 | 2 |
| 총 실패 | 125 | 77 | 4 |

### 추론 제한 프로브
원본 VLA 평균 4.6%, Pigey는 96.9% 달성(동일 VLA 사용)—향상이 정책 자체가 아닌 오케스트레이션에서 비롯됨을 증명.

핵심 의미: Pigey는 동결 정책 성공률을 12.8%에서 53.3%로 향상(표 내 수치 12.8→53.3에서 계산, 4배 이상)시키며 작업별 미세 조정이 없습니다. 추론기 스캔은 가장 약한 추론기(GPT-5.5 low, 평균 44.3%)조차 모든 비오케스트레이션 기준선을 크게 능가함을 보여, 오케스트레이션 프레임워크의 견고성을 입증합니다.

## 경계와 한계

- **백엔드 능력 상한에 제약**: Pigey는 약한 정책을 보상할 수 있지만, 저수준 도구 "지원"이 설정한 상한이 존재합니다. TAMP와 VLA 모두 특정 유형의 동작(예: 고정밀 조립)을 실행할 수 없다면 오케스트레이터도 할 수 없습니다.
- **불완전한 검증**: 폐색으로 인한 부분 관측 가능성은 나쁜 그리핑을 숨겨 거짓 성공이 하류로 전파될 수 있습니다(150회 시행 중 2회 검증기 거짓 성공).
- **지연과 비용**: API 호출 오케스트레이션에 의존, 시행당 3-15회 VLM 호출, 비용 $0.02~$0.50, 벽시계 시간 2-6분. 저지연 또는 고속 애플리케이션에 도전적.
- **하지 않은 것**: 추가 데이터 수집이나 사후 훈련 없음; 전용 모듈(메모리, 검증기, 보상 모델, 고수준 플래너) 훈련 없음. OB3(인형이 둘러싸인)은 3/5 성공에 그쳐 유일하게 5/5 미만인 작업.
- **논문에서 명시하지 않은 것**: 변형 가능 객체 조작에 대한 확장 검증, 다중 로봇 플랫폼 일반화, 더 복잡한 장기 작업(>10분)에서 추론기의 안정성.

## 공학적 시사점

- **먼저 백엔드 능력 경계 확인**: Pigey의 성공은 TAMP와 VLA의 상보성에 의존합니다. 재현 전에 TAMP가 강체 정밀 픽앤플레이스를 처리하고 VLA가 변형 가능 객체 폐루프 제어를 처리할 수 있는지 확인하세요—두 능력이 중복되거나 모두 사각지대가 있으면 오케스트레이션 이점이 크게 줄어듭니다.
- **가장 함정에 빠지기 쉬운 것은 검증 메커니즘**: 이중 신호(그리퍼 폭 + 손목 이미지)는 거짓 성공 방지의 핵심입니다. 플랫폼에 그리퍼 폭 센서가 없으면 동등한 결정적 신호(예: 힘 센서 임계값)를 설계해야 하며, 그렇지 않으면 검증기 거짓 성공이 하류 의사 결정을 오염시킵니다.
- **프롬프트 템플릿의 규율이 모델 능력보다 중요**: 정확한 문자열 규칙, Done 전 Perceive, 도구 호출 종료—이러한 하드 제약이 VLM 자체의 선택보다 성공률에 더 큰 영향을 미칩니다. 재현 시 먼저 템플릿 구조를 엄격히 따르고, 그 다음 작업에 맞춰 라우팅 규칙을 조정하세요.
- **추론기 선택은 한계적 이익**: GPT-5.5 low(44.3%)에서 Claude Opus 4.7(53.3%)까지, 추론기 능력 향상은 약 9퍼센트포인트 이득을 가져옵니다. 예산이 제한적이면 먼저 중간 추론기로 프레임워크를 검증한 후 최강 모델로 업그레이드하세요.
- **시뮬레이션과 실제의 격차는 주로 지각**: LIBERO-PRO에서 Pigey 평균 53.3%, 실제 로봇 97.3%—시뮬레이션은 감지기 노이즈와 객체 다양성이 낮지만 작업 술어는 더 엄격합니다. 재현 시 먼저 시뮬레이션에서 라우팅 로직을 디버깅한 후 실제 플랫폼으로 옮겨 지각 노이즈를 처리하세요.
