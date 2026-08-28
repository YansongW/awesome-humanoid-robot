---
$id: ent_paper_robobench_a_comprehensive_eval_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain'
  zh: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain'
  ko: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain'
summary:
  en: 'arXiv:2510.17801v2 Announce Type: replace Abstract: Building robots that can perceive, reason, and act in dynamic,
    unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where
    System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain,
    the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks
    mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce
    RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five
    dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure
    Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic
    data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven
    navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans
    can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of
    long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations
    in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding,
    and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench
    offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust
    robotic intelligence.'
  zh: RoboBench 是一个用于评估多模态大语言模型作为具身大脑的综合基准，由研究团队提出。它覆盖指令理解、感知推理、广义规划、功能预测和故障分析五个维度，包含 14 种能力、25 个任务和 6,092 个问答对。该基准通过引入 MLLM-as-world-simulator
    框架，在物理和视觉约束下评估长期规划，揭示了现有 MLLM 在隐式指令理解、时空推理等方面的持续局限。
  ko: 'arXiv:2510.17801v2 Announce Type: replace Abstract: Building robots that can perceive, reason, and act in dynamic,
    unstructured environments remains a central challenge. Recent embodied systems often follow a dual-system paradigm, where
    System 2 performs high-level reasoning and System 1 handles low-level control. We refer to System 2 as the embodied brain,
    the cognitive core for decision-making in manipulation. Although evaluating this embodied brain is crucial, existing benchmarks
    mainly measure execution success or cover only limited aspects of high-level cognition and task realism. We introduce
    RoboBench, a benchmark for evaluating multimodal large language models (MLLMs) as embodied brains. RoboBench covers five
    dimensions: Instruction Comprehension, Perception Reasoning, Generalized Planning, Affordance Prediction, and Failure
    Analysis. It spans 14 capabilities, 25 tasks, and 6,092 QA pairs. To improve realism, it draws from large-scale real robotic
    data and in-house collection across diverse embodiments, attribute-rich objects, multi-view scenes, and memory-driven
    navigation. For planning, RoboBench introduces an MLLM-as-world-simulator framework that assesses whether predicted plans
    can achieve critical object-state changes under physical and visual constraints, enabling more faithful evaluation of
    long-horizon reasoning than symbolic matching. Experiments on 18 state-of-the-art MLLMs reveal persistent limitations
    in implicit instruction understanding, spatiotemporal reasoning, cross-scenario planning, fine-grained affordance understanding,
    and failure diagnosis. We further analyze how embodied cognitive abilities relate to downstream robotic control. RoboBench
    offers a comprehensive scaffold for quantifying high-level cognition and guiding next-generation MLLMs toward more robust
    robotic intelligence.'
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
- robobench
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17801v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (980 chars, DeepSeek). [2026-08-28] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'Robobench: A Comprehensive Evaluation Benchmark for Multimodal Large Language Models as Embodied Brain (arXiv)'
  url: https://arxiv.org/abs/2510.17801
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述

RoboBench 是一个面向多模态大语言模型（MLLMs）作为机器人“具身大脑”的系统性评估基准，覆盖指令理解、感知推理、广义规划、可供性预测与失败分析五个维度，共 25 个任务、6092 个 QA 对。其核心贡献在于引入“MLLM-as-world-simulator”评估框架，基于状态依赖 DAG 对技能-对象节点进行结构化评分，而非自由文本打分，从而更可靠地衡量长时程规划的具身可行性，并揭示感知推理与下游 VLA 性能之间的强相关性。

## 它改变了什么

现有基准（如 BEAR、ECBench）主要评估符号计划保真度，未覆盖从隐式指令到物理执行失败的完整流水线，也缺乏对“计划能否在真实世界中完成”的具身可行性判断。RoboBench 改变了这一局面：它将评估重心从“模型说了什么”转向“模型做的计划能否执行”，通过世界模拟器对计划进行物理与逻辑层面的推演。这一转变使得基准分数与下游 VLA 策略的真实表现（如 CALVIN 上的成功率）产生了可量化的关联，从而让 MLLM 的认知评估不再是与执行脱节的孤立指标。

## 方法拆解

### 评估分类法
按操作执行流程组织：隐式指令理解 → 感知推理 → 广义规划 → 可供性接地 → 失败分析。每个维度下细分任务，例如感知推理包含机器人视角理解、时间接地、功能属性推理等。

### MLLM-as-world-simulator 评分框架
- 输入：场景图像、GT 动作序列、GT DAG 依赖图、模型预测计划。
- 节点正确性（NodeCorrectness）：将预测计划中的技能-对象节点与 GT 节点进行贪心一对一匹配，要求技能令牌相同、对象物理指代相同（别名仅限同一实体）、参数方向/功能等价。完全正确得 1，否则 0，无部分学分。最终分数 = ⌊matched/N_GT×10⌋。
- 任务完成度（TaskCompletion）：从 GT 动作与目标中提取关键状态集 S*，通过 DAG 排序，逐步模拟模型计划，检查前提、更新世界状态。隐式继承（如 pick_up 隐含 grasp+move_to）不阻止目标达成；错误方向动作无效果；替代技能若物理上达到相同最终状态则计数。分数 = ⌊|Ŝ|/|S*|×10⌋。
- 排除的机器人运动（move_to、grasp、hold、observation 等）不参与关键状态评估。

### 隐式指令与诊断
- 通过链式思维（CoT）脚手架（推断意图 → 识别相关对象 → 推断目标状态）进行诊断性消融，但默认设置不采用此脚手架。
- 跨评估器鲁棒性测试：使用四个异构评判模型、三种评分提示变体（v1 基础、v2 结构规则、v3 生产 DAG 接地回滚）评估 200 个分层样本。

### 下游 VLA 相关性分析
将 8 个 VLM 的具身认知分数与 VLM4VLA 协议下的下游微调结果结合，在 CALVIN（ABC-D 分割，30k 步训练，1000 个任务序列）和 LIBERO-10（50k 步，每任务 50 次试验）上计算皮尔逊相关。

## 关键创新

1. **世界模拟器评分替代文本评分**：这是对长时程规划评估的根本性革新。通过状态依赖 DAG 和物理模拟，将计划评估从表面语言一致性转向执行可行性，与人类判断的 Pearson 相关系数达 r=0.83（vs 基线 LLM 评分的 r=0.73），且跨评判器节点级 ICC(2,k)=0.948，证明其稳定可靠。
2. **隐式指令的严格诊断**：通过 CoT 消融揭示，即使提供显式意图推理脚手架，前沿模型（GPT-5、Claude、Gemini）在隐式指令上的提升也极为有限（计划项 Δ 分别为 +1.6、0.0、-3.1），且多数集为精确平局。这证明意图接地是真正的认知瓶颈，而非提示工程可解决的表面问题。
3. **认知分数与下游 VLA 的量化关联**：发现感知推理（对象中心 r=0.884、场景中心 r=0.833）与 CALVIN 强相关，可供性预测（静态+动态 r=0.677）与 LIBERO-10 相关，而低层执行错误与两者均弱相关（r=-0.057、-0.259）。这首次为“哪些认知能力真正决定执行表现”提供了数据支撑。

## 实验与结果

### 模型与基线
评估 18 个闭源与开源模型（GPT 系列、Claude 系列、Gemini 系列、Qwen 系列、LLaVA-OneVision、RoboBrain、MiMo-Embodied 等），外加 GPT-5.4 纯文本消融。

### 关键结果
| 维度 | 最佳模型 | 分数 | 对比基线 |
|---|---|---|---|
| 感知-机器人视角 | Claude-Opus-4.7 | 53.62 | 文本-only 平均 27.12 |
| 感知-时间接地 | Gemini-2.5-Pro | 50.38 | 文本-only 平均 27.12 |
| 功能属性推理 | Gemini-2.5-Pro | 82.28 | 文本-only 平均 27.12 |
| 可供性-静态 | Gemini-3.1-Pro | 82.31 | 人类 82.63 |
| 可供性-动态 | Gemini-3.1-Pro | 77.85 | 人类 82.63 |
| 可供性-导航 | Gemini-3.1-Pro | 96.94 | 人类 82.63 |
| 失败分析-执行 | RoboBrain-2.5-4B | 43.71 | 多数模型 15-27 |
| 失败分析-规划 | Gemini-3.1-Pro | 80.74 | 人类 80.67 |

### 隐式 vs 显式指令
最强显式目标模型（Claude-Sonnet-4.6）从 79.94 降至 61.38（隐式），降幅达 18.56（由表内数值 0.634→0.514 计算） 点，表明隐式指令是显著的难度来源。

### 相关性分析
CALVIN 上对象中心感知 r=0.884（p=0.0035）、场景中心 r=0.833（p=0.0103）；LIBERO-10 上静态+动态可供性 r=0.677（p=0.0652）。低层执行错误与两者均弱相关。

## 边界与局限

- CoT 消融仅覆盖前沿模型；较弱的 MLLM 在隐式设置中差距更大，可能仍受益于显式意图脚手架，论文未验证。
- 低层执行错误在当前 VLM4VLA 设置下与 CALVIN 和 LIBERO 的相关性均较弱，表明下游策略性能差异不由低层执行错误意识主要解释。
- 未发现单一通用认知预测器；不同下游环境强调具身智能的不同方面。
- 论文未明确提供完整模型名单、人类评估协议细节、跨评估者鲁棒性研究的完整数据、隐式指令消融的完整数据、注释噪声鲁棒性的完整数据、下游 VLA 实现细节（均声明在附录中，但事实要点未提供）。

## 工程启示

- **复现优先核对**：世界模拟器评分是核心，需严格实现 DAG 依赖图、排除运动列表（move_to、grasp、hold 等）和隐式继承规则（pick_up 隐含 grasp+move_to）。任何偏差都会导致节点匹配和任务完成度分数失真。
- **最容易踩坑**：节点匹配要求“对象物理指代相同”，别名仅限同一实体。若下游团队使用不同对象命名或未做实体消歧，NodeCorrectness 会系统性偏低。建议先在小样本上人工核对匹配逻辑。
- **选型指导**：若目标是提升 CALVIN 类操作性能，优先优化感知推理（对象中心、场景中心）；若目标是 LIBERO-10 类长时程任务，优先优化可供性预测。低层执行错误诊断能力对下游性能影响有限，可降低优先级。
- **隐式指令处理**：不要期望 CoT 脚手架能解决意图接地问题——前沿模型在消融中提升几乎为零。若需提升隐式指令表现，应从训练数据中增加隐式-显式配对样本入手，而非依赖推理时提示。
- **评估器选择**：生产评估器（v3 变体）跨评判器节点级 ICC(2,k)=0.948，建议直接采用该提示变体，避免使用 v1 基础提示（ICC=0.935）导致分数波动。

## 参考
- http://arxiv.org/abs/2510.17801v2

## 개요
RoboBench는 기존 벤치마크가 실행 성공률만 측정하거나 제한된 고급 인지 및 작업 현실성만 다루는 문제를 해결하기 위해 설계되었습니다. 대규모 실제 로봇 데이터와 내부 수집을 통해 얻은 다형태(multi-modal), 속성 풍부 객체, 다중 시점 장면, 메모리 기반 내비게이션 데이터에서 콘텐츠를 추출하여 현실성을 높입니다. 계획 평가에서 RoboBench는 MLLM-as-world-simulator 프레임워크를 채택하여 예측된 계획이 물리적 및 시각적 제약 하에서 핵심 객체 상태 변화를 달성할 수 있는지 검사함으로써, 기호 매칭보다 장기 추론을 더 충실하게 평가합니다. 18개의 최첨단 MLLM에 대한 실험은 암시적 명령 이해, 시공간 추론, 교차 장면 계획, 세분화된 기능 이해, 오류 진단에서 지속적인 부족을 드러냅니다. 이 벤치마크는 또한 구현 인지 능력과 하위 로봇 제어 간의 관계를 분석하여 고급 인지 정량화와 차세대 MLLM 지침을 위한 포괄적인 프레임워크를 제공합니다.

## 핵심 내용
### 배경 및 동기
동적 비구조화 환경에서 인지, 추론, 행동할 수 있는 로봇 구축은 여전히 핵심 과제입니다. 현재 구현 시스템은 종종 이중 시스템 패러다임을 채택합니다: System 2는 고급 추론을 담당하고 System 1은 저수준 제어를 처리합니다. 본 논문은 System 2를 구현 뇌(embodied brain), 즉 조작 결정의 인지 핵심으로 부릅니다. 기존 벤치마크는 주로 실행 성공률을 측정하거나 고급 인지 및 작업 현실성의 제한된 측면만 다룹니다.

### RoboBench 벤치마크 설계
- **평가 차원**: 명령 이해, 지각 추론, 일반화 계획, 기능 예측, 오류 분석의 다섯 가지 차원을 다룹니다.
- **규모**: 14가지 능력, 25개 작업, 6,092개의 질문-답변 쌍을 포함합니다.
- **데이터 출처**: 현실성을 높이기 위해 대규모 실제 로봇 데이터와 내부 수집 데이터를 사용하며, 다양한 형태, 속성 풍부 객체, 다중 시점 장면, 메모리 기반 내비게이션을 포함합니다.

### 계획 평가 혁신: MLLM-as-world-simulator
- 전통적인 방법은 기호 매칭으로 계획을 평가하지만, RoboBench는 MLLM-as-world-simulator 프레임워크를 도입합니다.
- 이 프레임워크는 예측된 계획이 물리적 및 시각적 제약 하에서 핵심 객체 상태 변화를 달성할 수 있는지 검사하여 장기 추론을 더 충실하게 평가합니다.

### 실험 및 발견
- 18개의 최첨단 MLLM에 대한 실험은 다음과 같은 지속적인 한계를 드러냅니다:
  - 암시적 명령 이해 부족
  - 시공간 추론 능력 약화
  - 교차 장면 계획의 어려움
  - 세분화된 기능 이해 제한
  - 오류 진단 능력 부족
- 구현 인지 능력과 하위 로봇 제어 간의 관계를 추가로 분석합니다.

### 결론
RoboBench는 고급 인지 정량화를 위한 포괄적인 프레임워크를 제공하여 차세대 MLLM이 더 견고한 로봇 지능으로 발전하도록 안내합니다.
