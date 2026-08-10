---
$id: ent_paper_lens_llm_guided_environment_simplificati_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LENS: LLM-guided Environment Simplification for Planning and Control in Clutter'
  zh: 'LENS: LLM-guided Environment Simplification for Planning and Control in Clutter'
  ko: 'LENS: LLM-guided Environment Simplification for Planning and Control in Clutter'
summary:
  en: Despite recent advances in general-purpose robotic manipulation, real-world multi-object clutter remains challenging
    to handle for today's prevalent approaches. The problem scales in complexity due to more objects and collisions, more
    unpredictable contact physics, distractors, and task ambiguity. Bridging this gap to real-world deployment requires effective
    scene abstractions; yet today,.
  zh: LENS 是一种利用多模态大语言模型（MLLM，具体为 GPT-4o）对机器人操作场景进行任务相关抽象的方法，通过迭代剪枝（pruning）与合并（merging）操作，在规划与控制前抑制任务无关物体。该方法在 TAMP、接触隐式
    MPC（C3+）和视觉-语言-动作模型（VLA，π0.5）三类下游系统上验证了其通用性，显著缓解了杂乱场景带来的组合爆炸与分布偏移问题。
  ko: Despite recent advances in general-purpose robotic manipulation, real-world multi-object clutter remains challenging
    to handle for today's prevalent approaches. The problem scales in complexity due to more objects and collisions, more
    unpredictable contact physics, distractors, and task ambiguity. Bridging this gap to real-world deployment requires effective
    scene abstractions; yet today,.
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
- lens
- llm
- guided
- environment
- simplificati
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
  title: 'arXiv:2607.19633 LENS: LLM-guided Environment Simplification for Planning and Control in Clutter'
  url: https://arxiv.org/abs/2607.19633
  date: '2026-07-22'
  accessed_at: '2026-08-05'
---

## 概述

LENS 是一种利用多模态大语言模型（MLLM，具体为 GPT-4o）对机器人操作场景进行任务相关抽象的方法，通过迭代剪枝（pruning）与合并（merging）操作，在规划与控制前抑制任务无关物体。该方法在 TAMP、接触隐式 MPC（C3+）和视觉-语言-动作模型（VLA，π0.5）三类下游系统上验证了其通用性，显著缓解了杂乱场景带来的组合爆炸与分布偏移问题。

## 它改变了什么

这项工作真正改变的是“杂乱”在机器人操作中的角色定位。以往，无论是基于优化的 TAMP 还是学习型 VLA 策略，都将场景中所有物体视为必须显式推理的变量，导致计算复杂度与失败模式随物体数量线性甚至超线性增长。LENS 的核心贡献在于将“场景简化”从人工设计的启发式（如最近邻选择）或繁琐的任务特定工程中解放出来，转而利用 VLM 的常识推理能力，在任务语义层面动态决定哪些物体可以被忽略、哪些必须保留、哪些可以合并为一个复合实体。

这一转变的意义在于，它把“可处理性”问题从下游算法的负担中剥离出来，变成一个前置的、任务相关的抽象问题。对于 TAMP，这意味着状态空间和决策变量数量的大幅缩减；对于 C3+ 这类接触隐式控制器，它直接降低了线性互补问题（LCP）的维度；对于 VLA，它通过视觉输入过滤缓解了分布偏移。这不仅仅是工程上的加速，而是从方法论上承认：在非结构化场景中，任务相关性本身就是一个需要推理的问题，而非可以预先穷举的几何属性。

## 方法拆解

LENS 的核心是一个迭代的“抽象-执行-反馈”闭环，其流程由 Algorithm 1 定义，关键设计决策如下：

### 场景表示与相关性分类
- 输入为任务描述 τ 和场景描述 𝒪（物体 ID、位姿、质量等，或俯视图像）。
- 定义三种任务相关性：**语义**（与目标上下文相关）、**几何**（阻碍期望运动）、**动态**（会移动或受影响）。VLM 被要求输出结构化抽象 Õ，形式为物体列表的列表，其中子列表表示可合并的物体组。

### 剪枝与合并操作
- **剪枝**：从下游系统的推理空间中移除物体。在 TAMP 中表现为状态空间缩减（物体姿态固定、不可操作但参与碰撞检查）；在 C3+ 中表现为减少刚体数、接触对和 LCP 维度；在 VLA 中表现为视觉干扰物移除（通过图像修复 inpainting）。
- **合并**：将功能或动态耦合的物体（如堆叠物）分组为单一复合实体。合并体的碰撞模型通过聚合成员几何构建，运行时从成员姿态重新计算，保留物理范围的保守包络。TAMP 中合并组必须能稳定共移（父体为最低支撑物体）；C3+ 中不要求物理稳定，只要接触采样可集体推理即可聚类。

### 反馈驱动的迭代细化
- 执行失败（超时或错误代码）触发反馈。TAMP 的触发阈值为 120 秒，C3+ 为 250 次控制迭代或错误代码。
- 反馈格式为框架特定的提示文本（如 "The last run failed. You chose [previous representation]. Choose a larger set of objects..."），与先前 Õ 一起追加到原始提示中，重新查询 VLM，最多 N 次重试（TAMP 允许 2 次，C3+ 硬件实验限制 3 次）。
- VLA 场景因任务视界短，过滤后无需反馈重新查询。

### 关键参数
- VLM 查询平均耗时 1.76 秒，相对于执行时间可忽略。
- C3+ 提示词约束：最多选择 4 个物体，最多 4 个子列表总数，目标物体保持单例。
- VLA 硬件提示词要求保护机器人末端执行器、目标容器等关键元素，输出仅 JSON 格式的 relevant_objects 和 distractors 列表。

## 关键创新

1. **任务相关性的显式推理替代几何启发式**：LENS 用 VLM 的语义理解替代了距离最近邻或半径阈值等空间启发式。图 9 展示了关键案例：距离目标最近的物体集合遗漏了一个远距离阻塞物，而 LENS 能识别该阻塞物为任务相关。这是对“相关性即空间邻近”假设的根本性挑战。

2. **合并操作作为抽象原语**：不同于仅做减法（剪枝），LENS 引入合并操作将动态耦合的物体（如堆叠物）视为单一复合体。这保留了物理交互的保守包络，同时大幅减少接触对数量。C3+ 中合并体无需物理稳定，只要接触采样可集体推理即可聚类，这扩展了合并的适用范围。

3. **跨范式通用性**：LENS 在符号规划（TAMP）、数值优化（C3+）和端到端学习（VLA）三类截然不同的下游系统中均有效，且抽象操作的定义随系统语义自然映射（状态空间缩减 vs. 视觉干扰物移除）。这种通用性表明任务相关抽象是一个独立于具体算法范式的中间层问题。

## 实验与结果

实验覆盖三类系统，关键结果如下：

| 实验设置 | 条件 | 成功率/性能 | 备注 |
|---------|------|------------|------|
| TAMP（50 情节） | 轻杂乱 | LENS ≈ 基线 | 两者相当 |
| TAMP（50 情节） | 重杂乱 | LENS 优于基线 | 基线频繁超时枚举干扰物 |
| TAMP（50 情节） | 杂乱+堆叠 | LENS 优于基线 | 合并堆叠为单一复合体 |
| C3+ 仿真（每物体 5 次试验） | 小场景（2–4 物体） | 两者相当 | — |
| C3+ 仿真 | 6 物体 | 基线耗时约 1000 秒 | LENS 保持稳定 |
| C3+ 仿真 | 7 物体 | 基线耗时超 4000 秒 | LENS 平均执行时间约 40–135 秒 |
| C3+ 仿真（45 vs 30 次试验） | 全杂乱水平 | LENS 39/45 vs 基线 17/30 | — |
| C3+ 硬件（3 次反馈循环） | 剪枝与剪枝+合并 | 累积成功率均 80% | 失败含超时与工作空间限制 |
| VLA 仿真（100 情节、10 任务） | 无杂乱 | 成功率 0.85 | — |
| VLA 仿真 | 杂乱基线 | 成功率 0.5 | 杂乱显著降低性能 |
| VLA 仿真 | 杂乱+LENS | 成功率 0.69 | 部分恢复性能 |
| VLA 硬件（n=10 每水果） | 杂乱基线 | 菠萝 0.2、梨 0.0、香蕉 0.0、苹果 0.0 | — |
| VLA 硬件（n=10 每水果） | 杂乱+LENS | 菠萝 0.5、梨 0.3、香蕉 0.3、苹果 0.7 | — |

C3+ 距离基线对比（n=30，半径 0.05、0.1、0.15、0.2、0.25）显示 LENS 优于所有启发式变体。VLA 仿真中 LENS 将成功率从 0.5 提升至 0.69，但未完全恢复至无杂乱水平（0.85），表明抽象不完美与底层 VLA 鲁棒性仍有差距。

## 边界与局限

- **反馈机制依赖高层失败信号**：LENS 的迭代细化仅由超时或错误代码触发，不利用失败的具体原因（如碰撞位置、接触力异常），这可能遗漏需要精细调整的失败模式。
- **无跨运行学习**：LENS 不积累经验，每次任务从零开始推理，无法利用历史任务的相关性模式。
- **合并体的动态建模缺失**：C3+ 中将堆视为单个物体时，不建模或预测其形状随时间的变化，这可能在堆在推动过程中发生显著形变时导致控制误差。
- **VLA 仿真依赖特权信息**：仿真中使用地面真值分割而非学习检测器，因为开放词汇检测器（如 GroundingDINO）在模拟场景中因域不匹配不可靠。硬件实验虽使用检测+修复管道，但性能仍受限于检测质量。
- **剩余性能差距**：VLA 中 0.69 对 0.85 的差距表明不完美抽象和底层策略对分布偏移的鲁棒性仍是瓶颈。论文未明确 LENS 在更长视界、多阶段任务中的表现，也未涉及相关性随时间演化的场景。

## 工程启示

- **先核对 VLM 提示词与下游系统的接口契约**：LENS 的抽象质量高度依赖提示词约束。C3+ 中“最多 4 个物体、最多 4 个子列表”的硬约束是保证 LCP 可解性的关键；VLA 硬件提示词要求列出所有干扰物（遗漏一个即失败）。复现时务必逐条核对输出格式（如 JSON 结构、子列表语义）。
- **最容易踩坑的是合并体的几何更新**：C3+ 中合并体形状实时从成员姿态重算，但控制器不建模内部形变。若你的下游系统对接触几何敏感，需评估合并导致的包络误差是否可接受。TAMP 中合并组要求物理稳定，否则规划可能产生不可行解。
- **反馈触发阈值需按系统调参**：TAMP 的 120 秒超时和 C3+ 的 250 次迭代是经验值。若你的规划器更慢或控制器更快，需重新标定，否则反馈要么过于频繁（增加 VLM 查询开销）要么过晚（浪费执行时间）。
- **VLA 场景优先考虑无反馈的单次过滤**：由于任务视界短，LENS 在 VLA 中无需迭代。但需注意，过滤后的图像通过 inpainting 生成，若修复质量差会引入新的伪影。硬件实验中检测管道的可靠性是主要瓶颈，建议先验证 GroundingDINO + SAM + LaMa 在你的场景域中的表现。
- **性能评估需区分“剪枝”与“合并”的独立贡献**：C3+ 硬件实验中剪枝和剪枝+合并的累积成功率均为 80%，但失败模式不同。建议分别报告两种变体的成功率与失败原因，以判断合并是否在你的场景中带来额外收益。

## Overview
Despite recent advances in general-purpose robotic manipulation, real-world multi-object clutter remains challenging to handle for today's prevalent approaches. The problem scales in complexity due to more objects and collisions, more unpredictable contact physics, distractors, and task ambiguity. Bridging this gap to real-world deployment requires effective scene abstractions; yet today, producing such abstractions requires extensive task-specific manual engineering, which does not scale. These abstractions are costly to generate and difficult to adjust or fine-tune. We instead propose a plug-and-play fix to automatically generate scene-specific, task-specific, adaptively updating abstractions on top of existing planning and control stacks. LLM-guided Environment Simplification (LENS) produces a de-cluttered abstracted scene representation by merging (e.g., stacked objects) or pruning (e.g., distant objects) scene entities in a closed loop in response to task progress. These dynamic, task-relevant abstractions are versatile and easy to use. In our experiments, we show that LENS improves classical planning, model-based control, and a vision-language-action model, across a diverse set of highly cluttered manipulation scenes. Project website: https://lens-2026.github.io/.

## 参考
- https://arxiv.org/abs/2607.19633

## 개요

LENS는 다중 모달 대규모 언어 모델(MLLM, 구체적으로 GPT-4o)을 활용하여 로봇 조작场景에서 작업 관련 추상화를 수행하는 방법으로, 반복적 가지치기(pruning)와 병합(merging) 연산을 통해 계획 및 제어 전에 작업과 무관한 객체를 억제합니다. 이 방법은 TAMP, 접촉 암시적 MPC(C3+) 및 시각-언어-행동 모델(VLA, π0.5)의 세 가지 하위 시스템에서 그 범용성을 검증했으며, 복잡한 장면으로 인한 조합 폭발과 분포 이동 문제를 크게 완화했습니다.

## 그것이 바꾼 것

이 작업이 진정으로 바꾼 것은 로봇 조작에서 '복잡함'의 역할定位입니다. 과거에는 최적화 기반 TAMP든 학습 기반 VLA 정책이든 장면의 모든 객체를 명시적으로 추론해야 하는 변수로 간주하여 계산 복잡도와 실패 모드가 객체 수에 따라 선형 또는 초선형으로 증가했습니다. LENS의 핵심 기여는 '장면 단순화'를 수작업으로 설계된 휴리스틱(예: 최근접 이웃 선택)이나 번거로운 작업별 엔지니어링에서 해방시키고, VLM의 상식 추론 능력을 활용하여 작업 의미론 수준에서 어떤 객체를 무시할 수 있는지, 어떤 객체를 반드시 유지해야 하는지, 어떤 객체를 하나의 복합 엔티티로 병합할 수 있는지를 동적으로 결정하는 것입니다.

이 전환의 의미는 '처리 가능성' 문제를 하위 알고리즘의 부담에서 분리하여 사전 단계의 작업 관련 추상화 문제로 만든다는 점입니다. TAMP의 경우 상태 공간과 결정 변수 수의 대폭 축소를 의미하고, C3+와 같은 접촉 암시적 제어기의 경우 선형 상보 문제(LCP)의 차원을 직접 낮추며, VLA의 경우 시각 입력 필터링을 통해 분포 이동을 완화합니다. 이는 단순한 엔지니어링 가속이 아니라 방법론적으로 비구조화된 장면에서 작업 관련성 자체가 추론이 필요한 문제이며, 사전에 완전히 열거할 수 있는 기하학적 속성이 아님을 인정하는 것입니다.

## 방법 분해

LENS의 핵심은 반복적인 '추상화-실행-피드백' 폐루프이며, 그 흐름은 Algorithm 1에 정의되어 있습니다. 주요 설계 결정은 다음과 같습니다:

### 장면 표현 및 관련성 분류
- 입력은 작업 설명 τ와 장면 설명 𝒪(객체 ID, 자세, 질량 등 또는 탑뷰 이미지)입니다.
- 세 가지 작업 관련성을 정의합니다: **의미론적**(목표 맥락과 관련), **기하학적**(원하는 운동을 방해), **동적**(이동하거나 영향을 받을 수 있음). VLM은 객체 목록의 목록 형태인 구조화된 추상화 Õ를 출력하도록 요청받으며, 하위 목록은 병합 가능한 객체 그룹을 나타냅니다.

### 가지치기 및 병합 연산
- **가지치기**: 하위 시스템의 추론 공간에서 객체를 제거합니다. TAMP에서는 상태 공간 축소(객체 자세 고정, 조작 불가하지만 충돌 검사에는 참여)로 나타나고, C3+에서는 강체 수, 접촉 쌍 및 LCP 차원 감소로 나타나며, VLA에서는 시각적 방해물 제거(이미지 인페인팅을 통해)로 나타납니다.
- **병합**: 기능적 또는 동적으로 결합된 객체(예: 적층물)를 단일 복합 엔티티로 그룹화합니다. 병합체의 충돌 모델은 구성원 기하의 집계로 구축되며, 런타임 시 구성원 자세에서 재계산되어 물리적 범위의 보수적 포락선을 유지합니다. TAMP에서 병합 그룹은 안정적으로 함께 이동할 수 있어야 하며(부모는 최하위 지지 객체), C3+에서는 물리적 안정성이 요구되지 않고 접촉 샘플링이 집합적으로 추론 가능하기만 하면 클러스터링할 수 있습니다.

### 피드백 기반 반복 세분화
- 실행 실패(시간 초과 또는 오류 코드)가 피드백을 트리거합니다. TAMP의 트리거 임계값은 120초, C3+는 250회 제어 반복 또는 오류 코드입니다.
- 피드백 형식은 프레임워크별 프롬프트 텍스트(예: "The last run failed. You chose [previous representation]. Choose a larger set of objects...")이며, 이전 Õ와 함께 원래 프롬프트에 추가되어 VLM을 다시 쿼리하며, 최대 N회 재시도(TAMP는 2회 허용, C3+ 하드웨어 실험은 3회 제한)합니다.
- VLA 장면은 작업 시야가 짧아 필터링 후 피드백 재쿼리가 필요 없습니다.

### 주요 매개변수
- VLM 쿼리 평균 소요 시간은 1.76초로 실행 시간에 비해 무시할 수 있습니다.
- C3+ 프롬프트 제약: 최대 4개 객체 선택, 최대 4개 하위 목록 총수, 목표 객체는 단일 항목 유지.
- VLA 하드웨어 프롬프트는 로봇 엔드 이펙터, 목표 용기 등 핵심 요소 보호를 요구하며, 출력은 JSON 형식의 relevant_objects 및 distractors 목록만 허용합니다.

## 핵심 혁신

1. **작업 관련성의 명시적 추론이 기하학적 휴리스틱을 대체**: LENS는 VLM의 의미론적 이해를 사용하여 거리 최근접 이웃이나 반경 임계값과 같은 공간적 휴리스틱을 대체합니다. 그림 9는 핵심 사례를 보여줍니다: 목표에 가장 가까운 객체 집합은 원거리 차단물을 놓치지만, LENS는 해당 차단물을 작업 관련으로 식별할 수 있습니다. 이는 '관련성 = 공간적 근접성'이라는 가정에 대한 근본적인 도전입니다.

2. **병합 연산을 추상화 원시 연산으로 사용**: 단순히 감산(가지치기)만 하는 것이 아니라, LENS는 병합 연산을 도입하여 동적으로 결합된 객체(예: 적층물)를 단일 복합체로 간주합니다. 이는 물리적 상호작용의 보수적 포락선을 보존하면서 접촉 쌍 수를 크게 줄입니다. C3+에서 병합체는 물리적 안정성이 필요 없고 접촉 샘플링이 집합적으로 추론 가능하기만 하면 클러스터링할 수 있어 병합의 적용 범위를 확장합니다.

3. **교차 패러다임 범용성**: LENS는 기호 계획(TAMP), 수치 최적화(C3+), 종단 간 학습(VLA)의 세 가지 상이한 하위 시스템에서 모두 유효하며, 추상화 연산의 정의는 시스템 의미론에 따라 자연스럽게 매핑됩니다(상태 공간 축소 vs. 시각적 방해물 제거). 이러한 범용성은 작업 관련 추상화가 특정 알고리즘 패러다임과 독립적인 중간 계층 문제임을 시사합니다.

## 실험 및 결과

실험은 세 가지 시스템을 포괄하며, 주요 결과는 다음과 같습니다:

| 실험 설정 | 조건 | 성공률/성능 | 비고 |
|---------|------|------------|------|
| TAMP(50 에피소드) | 경량 복잡 | LENS ≈ 기준선 | 둘 다 유사 |
| TAMP(50 에피소드) | 중량 복잡 | LENS 우수 | 기준선이 방해물 열거로 빈번한 시간 초과 |
| TAMP(50 에피소드) | 복잡+적층 | LENS 우수 | 적층을 단일 복합체로 병합 |
| C3+ 시뮬레이션(객체당 5회 시험) | 소형 장면(2–4 객체) | 둘 다 유사 | — |
| C3+ 시뮬레이션 | 6 객체 | 기준선 약 1000초 소요 | LENS 안정 유지 |
| C3+ 시뮬레이션 | 7 객체 | 기준선 4000초 초과 | LENS 평균 실행 시간 약 40–135초 |
| C3+ 시뮬레이션(45 vs 30회 시험) | 전체 복잡 수준 | LENS 39/45 vs 기준선 17/30 | — |
| C3+ 하드웨어(3회 피드백 루프) | 가지치기 및 가지치기+병합 | 누적 성공률 모두 80% | 실패는 시간 초과 및 작업 공간 제한 포함 |
| VLA 시뮬레이션(100 에피소드, 10 작업) | 복잡 없음 | 성공률 0.85 | — |
| VLA 시뮬레이션 | 복잡 기준선 | 성공률 0.5 | 복잡이 성능을 크게 저하 |
| VLA 시뮬레이션 | 복잡+LENS | 성공률 0.69 | 성능 부분 회복 |
| VLA 하드웨어(n=10 과일별) | 복잡 기준선 | 파인애플 0.2, 배 0.0, 바나나 0.0, 사과 0.0 | — |
| VLA 하드웨어(n=10 과일별) | 복잡+LENS | 파인애플 0.5, 배 0.3, 바나나 0.3, 사과 0.7 | — |

C3+ 거리 기준선 비교(n=30, 반경 0.05, 0.1, 0.15, 0.2, 0.25)는 LENS가 모든 휴리스틱 변형보다 우수함을 보여줍니다. VLA 시뮬레이션에서 LENS는 성공률을 0.5에서 0.69로 향상시켰지만, 복잡 없는 수준(0.85)까지 완전히 회복하지는 못했으며, 이는 불완전한 추상화와 하위 VLA의 견고성 사이에 여전히 격차가 있음을 나타냅니다.

## 경계 및 한계

- **피드백 메커니즘은 상위 수준 실패 신호에 의존**: LENS의 반복 세분화는 시간 초과나 오류 코드에 의해서만 트리거되며, 실패의 구체적인 원인(충돌 위치, 접촉력 이상 등)을 활용하지 않아 세밀한 조정이 필요한 실패 모드를 놓칠 수 있습니다.
- **실행 간 학습 없음**: LENS는 경험을 축적하지 않으며, 각 작업은 처음부터 추론을 시작하여 과거 작업의 관련성 패턴을 활용할 수 없습니다.
- **병합체의 동적 모델링 부재**: C3+에서 적층물을 단일 객체로 간주할 때 시간에 따른 형태 변화를 모델링하거나 예측하지 않으며, 이는 적층물이 밀기 과정에서 상당한 변형을 겪을 때 제어 오차를 유발할 수 있습니다.
- **VLA 시뮬레이션은 특권 정보에 의존**: 시뮬레이션에서는 학습 기반 검출기 대신 지상 진실 분할을 사용하는데, 이는 개방 어휘 검출기(예: GroundingDINO)가 시뮬레이션 장면에서 도메인 불일치로 인해 신뢰할 수 없기 때문입니다. 하드웨어 실험은 검출+인페인팅 파이프라인을 사용하지만 성능은 여전히 검출 품질에 제한됩니다.
- **잔여 성능 격차**: VLA에서 0.69 대 0.85의 격차는 불완전한 추상화와 하위 정책의 분포 이동에 대한 견고성이 여전히 병목임을 시사합니다. 논문은 더 긴 시야, 다단계 작업에서의 LENS 성능을 명시하지 않았으며, 관련성이 시간에 따라 진화하는 장면도 다루지 않습니다.

## 공학적 시사점

- **먼저 VLM 프롬프트와 하위 시스템의 인터페이스 계약을 확인하세요**: LENS의 추상화 품질은 프롬프트 제약에 크게 의존합니다. C3+에서 '최대 4개 객체, 최대 4개 하위 목록'의 하드 제약은 LCP 해결 가능성을 보장하는 핵심이며, VLA 하드웨어 프롬프트는 모든 방해물을 나열하도록 요구합니다(하나 누락 시 실패). 재현 시 출력 형식(JSON 구조, 하위 목록 의미론)을 항목별로 반드시 확인하세요.
- **가장 함정에 빠지기 쉬운 것은 병합체의 기하학 업데이트입니다**: C3+에서 병합체 형태는 구성원 자세에서 실시간으로 재계산되지만, 제어기는 내부 변형을 모델링하지 않습니다. 하위 시스템이 접촉 기하학에 민감하다면 병합으로 인한 포락선 오차가 허용 가능한지 평가해야 합니다. TAMP에서 병합 그룹은 물리적 안정성이 요구되며, 그렇지 않으면 계획이 실행 불가능한 해를 생성할 수 있습니다.
- **피드백 트리거 임계값은 시스템별로 튜닝해야 합니다**: TAMP의 120초 시간 초과와 C3+의 250회 반복은 경험적 값입니다. 계획기가 더 느리거나 제어기가 더 빠르다면 재보정해야 하며, 그렇지 않으면 피드백이 너무 빈번(VLM 쿼리 오버헤드 증가)하거나 너무 늦게(실행 시간 낭비) 발생할 수 있습니다.
- **VLA 장면에서는 피드백 없는 단일 필터링을 우선 고려하세요**: 작업 시야가 짧기 때문에 LENS는 VLA에서 반복이 필요 없습니다. 그러나 필터링된 이미지는 인페인팅으로 생성되므로 복원 품질이 낮으면 새로운 아티팩트가 도입될 수 있습니다. 하드웨어 실험에서 검출 파이프라인의 신뢰성이 주요 병목이므로, GroundingDINO + SAM + LaMa가 해당 장면 도메인에서의 성능을 먼저 검증하는 것이 좋습니다.
- **성능 평가는 '가지치기'와 '병합'의 독립적 기여를 구분해야 합니다**: C3+ 하드웨어 실험에서 가지치기와 가지치기+병합의 누적 성공률은 모두 80%이지만 실패 모드는 다릅니다. 두 변형의 성공률과 실패 원인을 각각 보고하여 병합이 해당 장면에서 추가 이점을 제공하는지 판단하는 것이 좋습니다.
