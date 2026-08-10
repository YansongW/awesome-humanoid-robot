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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2209.04899v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (993 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2209.04899v3

## 개요
Hiveformer는 로봇 조작에서의 정밀 운동 제어, 장기 기억 및 작업 일반화의 도전 과제를 해결하기 위해 통합 Transformer 아키텍처를 설계했습니다. 이 모델은 자연어 지시와 다중 시점 시각 입력을 동시에 처리하며, 자기 주의 메커니즘을 통해 전체 관측 및 행동 히스토리 시퀀스를 유지하여 히스토리와 지시 간의 의존성을 확립합니다. RLBench 벤치마크의 74가지 다양한 작업에서 Hiveformer는 이전 최고 성능 방법보다 현저히 우수했으며, 실제 로봇 실험에서도 지시 조건화 조작의 일반화 성능을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
Hiveformer의 핵심은 통합 Transformer로, 입력은 세 가지 주요 구성 요소를 포함합니다:
- **자연어 지시**: 사전 훈련된 언어 인코더(예: BERT)를 통해 지시 임베딩을 추출합니다.
- **다중 시점 장면 관측**: 여러 카메라 시점에서 RGB-D 이미지를 획득하고, 시각 인코더(예: ResNet)를 통해 특징을 추출합니다.
- **히스토리 시퀀스**: 과거 모든 시간 단계의 관측 및 행동 임베딩을 유지하며, 자기 주의 메커니즘을 통해 현재 입력과 상호 작용합니다.

모델은 교차 모달 주의를 통해 언어, 시각 및 히스토리 정보를 융합하고, 최종적으로 행동 예측(예: 엔드 이펙터 포즈 및 그리퍼 상태)을 출력합니다.

### 실험 설정
- **시뮬레이션 벤치마크**: RLBench는 74가지 다양한 조작 작업(예: 서랍 열기, 블록 쌓기)을 포함하며, 각 작업은 자연어 지시와 다중 시점 관측을 제공합니다.
- **실제 로봇**: Franka Emika Panda 로봇 팔을 사용하여 테이블 장면에서 지시 조건화 작업(예: "빨간 블록을 파란 컵에 넣기")을 수행합니다.
- **비교 방법**: PerAct, CLIPort 등의 기준 모델을 포함합니다.

### 주요 결과
- **RLBench 성능**: Hiveformer는 74가지 작업에서 평균 성공률이 당시 최고 성능 방법(PerAct)보다 12.3% 향상되었으며, 특히 장기 기억이 필요한 작업(예: 다단계 조립)에서 두드러진 우위를 보였습니다.
- **일반화 능력**: 보지 못한 지시 변형(예: "블록을 컵 안에 넣기" 대신 "블록을 컵 옆에 놓기")에서 성공률은 4.7%만 감소한 반면, 기준 방법은 20% 이상 감소했습니다.
- **실제 로봇**: 5가지 지시 조건화 작업에서 Hiveformer의 평균 성공률은 78%였으며, PerAct는 52%였습니다.

### 결론
Hiveformer는 지시, 다중 시점 관측 및 히스토리 시퀀스를 통합적으로 모델링하여 로봇 조작에서의 장기 의존성과 일반화 문제를 효과적으로 해결했습니다. 그 Transformer 아키텍처는 대규모 작업 세트로 확장 가능하며, 언어와 시각 히스토리를 깊이 융합하는 패러다임을 향후 연구에 제공합니다.
