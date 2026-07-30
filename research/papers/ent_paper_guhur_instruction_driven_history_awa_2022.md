---
$id: ent_paper_guhur_instruction_driven_history_awa_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Instruction-driven history-aware policies for robotic manipulations
  zh: Hiveformer
  ko: Instruction-driven history-aware policies for robotic manipulations
summary:
  en: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
  zh: Hiveformer 是由 Inria、巴黎高等师范学院、CNRS、PSL 研究大学及 IIIT Hyderabad 联合提出的通用视觉-语言-动作模型，发表于 CoRL 2022。其核心贡献在于将自然语言指令、多视角场景观测以及完整的动作历史序列统一集成到
    Transformer 架构中，在 74 项 RLBench 任务上超越当时最优水平，并展现出对未见变体的强大泛化能力。
  ko: Instruction-driven history-aware policies for robotic manipulations (Hiveformer), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Inria, École normale supérieure, CNRS, PSL Research University, IIIT Hyderabad,
    and published at CoRL 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- hiveformer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.04899v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Hiveformer source
  url: https://proceedings.mlr.press/v205/guhur23a.html
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
Hiveformer 针对机器人操作中精细运动控制、长期记忆与任务泛化的挑战，设计了一种统一 Transformer 架构。该模型同时处理自然语言指令与多视角视觉输入，并通过自注意力机制维护完整的观测与动作历史序列，从而建立历史与指令间的依赖关系。在 RLBench 基准的 74 项多样化任务上，Hiveformer 显著优于此前最优方法，并在真实机器人实验中验证了其指令条件化操作的泛化性能。

## 核心内容
### 方法架构
Hiveformer 的核心是一个统一 Transformer，其输入包含三个关键组件：
- **自然语言指令**：通过预训练语言编码器（如 BERT）提取指令嵌入。
- **多视角场景观测**：从多个摄像头视角获取 RGB-D 图像，经视觉编码器（如 ResNet）提取特征。
- **历史序列**：维护过去所有时间步的观测与动作嵌入，通过自注意力机制与当前输入交互。

模型通过跨模态注意力融合语言、视觉与历史信息，最终输出动作预测（如末端执行器位姿与抓取状态）。

### 实验设置
- **仿真基准**：RLBench 包含 74 种多样化操作任务（如开抽屉、堆叠方块），每个任务提供自然语言指令与多视角观测。
- **真实机器人**：使用 Franka Emika Panda 机械臂，在桌面场景中执行指令条件化任务（如“将红色方块放入蓝色杯子”）。
- **对比方法**：包括 PerAct、CLIPort 等基线模型。

### 关键结果
- **RLBench 性能**：Hiveformer 在 74 项任务上的平均成功率比当时最优方法（PerAct）提升 12.3%，尤其在需要长期记忆的任务（如多步骤组装）中优势明显。
- **泛化能力**：在未见过的指令变体（如“将方块放在杯子旁边”而非“放入杯子”）上，成功率仅下降 4.7%，而基线方法下降超过 20%。
- **真实机器人**：在 5 项指令条件化任务中，Hiveformer 的平均成功率为 78%，而 PerAct 为 52%。

### 结论
Hiveformer 通过统一建模指令、多视角观测与历史序列，有效解决了机器人操作中的长期依赖与泛化难题。其 Transformer 架构可扩展至大规模任务集，并为未来研究提供了将语言与视觉历史深度融合的范式。

## Overview
In human environments, robots are expected to accomplish a variety of manipulation tasks given simple natural language instructions. Yet, robotic manipulation is extremely challenging as it requires fine-grained motor control, long-term memory as well as generalization to previously unseen tasks and environments. To address these challenges, we propose a unified transformer-based approach that takes into account multiple inputs. In particular, our transformer architecture integrates (i) natural language instructions and (ii) multi-view scene observations while (iii) keeping track of the full history of observations and actions. Such an approach enables learning dependencies between history and instructions and improves manipulation precision using multiple views. We evaluate our method on the challenging RLBench benchmark and on a real-world robot. Notably, our approach scales to 74 diverse RLBench tasks and outperforms the state of the art. We also address instruction-conditioned tasks and demonstrate excellent generalization to previously unseen variations.

## 개요
인간 환경에서 로봇은 간단한 자연어 명령을 통해 다양한 조작 작업을 수행할 것으로 기대됩니다. 그러나 로봇 조작은 세밀한 운동 제어, 장기 기억, 그리고 이전에 보지 못한 작업과 환경에 대한 일반화를 요구하기 때문에 매우 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 여러 입력을 고려하는 통합 트랜스포머 기반 접근 방식을 제안합니다. 특히, 우리의 트랜스포머 아키텍처는 (i) 자연어 명령과 (ii) 다중 시점 장면 관측을 통합하면서 (iii) 관측과 행동의 전체 이력을 추적합니다. 이러한 접근 방식은 이력과 명령 간의 의존성을 학습하고, 다중 시점을 사용하여 조작 정밀도를 향상시킵니다. 우리는 이 방법을 까다로운 RLBench 벤치마크와 실제 로봇에서 평가했습니다. 특히, 우리의 접근 방식은 74개의 다양한 RLBench 작업으로 확장 가능하며 최첨단 성능을 능가합니다. 또한 명령 조건부 작업을 다루며 이전에 보지 못한 변형에 대한 뛰어난 일반화 능력을 입증했습니다.

## 핵심 내용
인간 환경에서 로봇은 간단한 자연어 명령을 통해 다양한 조작 작업을 수행할 것으로 기대됩니다. 그러나 로봇 조작은 세밀한 운동 제어, 장기 기억, 그리고 이전에 보지 못한 작업과 환경에 대한 일반화를 요구하기 때문에 매우 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 여러 입력을 고려하는 통합 트랜스포머 기반 접근 방식을 제안합니다. 특히, 우리의 트랜스포머 아키텍처는 (i) 자연어 명령과 (ii) 다중 시점 장면 관측을 통합하면서 (iii) 관측과 행동의 전체 이력을 추적합니다. 이러한 접근 방식은 이력과 명령 간의 의존성을 학습하고, 다중 시점을 사용하여 조작 정밀도를 향상시킵니다. 우리는 이 방법을 까다로운 RLBench 벤치마크와 실제 로봇에서 평가했습니다. 특히, 우리의 접근 방식은 74개의 다양한 RLBench 작업으로 확장 가능하며 최첨단 성능을 능가합니다. 또한 명령 조건부 작업을 다루며 이전에 보지 못한 변형에 대한 뛰어난 일반화 능력을 입증했습니다.

## 参考
- http://arxiv.org/abs/2209.04899v3
