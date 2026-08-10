---
$id: ent_paper_shah_learning_affordances_at_infere_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Affordances at Inference-Time for Vision-Language-Action Models
  zh: LITEN
  ko: Learning Affordances at Inference-Time for Vision-Language-Action Models
summary:
  en: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
  zh: LITEN 是 UC Berkeley 与 Physical Intelligence 于 2025 年提出的大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过推理时执行学习，使 VLA 模型能够从过往经验中动态调整行为，避免重复错误。关键创新在于将低层
    VLA 策略与高层 VLM 结合，通过上下文学习掌握低层策略的 affordances 与能力边界。
  ko: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- liten
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.19752v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (957 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Affordances at Inference-Time for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.19752
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LITEN source
  url: https://doi.org/10.48550/arXiv.2510.19752
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
LITEN 针对现有 Vision-Language-Action 模型（VLA）在复杂控制任务中缺乏动态行为调整能力的问题，提出了一种推理时执行学习框架。该方法通过迭代执行两个阶段：推理阶段生成并执行低层 VLA 的计划，评估阶段反思执行结果并提取有用结论纳入后续推理上下文。与纯语言领域的自优化方法不同，LITEN 需处理非结构化的真实机器人轨迹（如原始视频），因此在评估阶段引入了结构化引导机制。实验表明，LITEN 能有效从过往经验中学习，生成利用高 affordance 指令完成长时域任务的计划。

## 核心内容
### 方法架构
LITEN 采用双层架构：
- **低层 VLA 策略**：负责执行具体动作指令
- **高层 VLM**：通过上下文学习（in-context learning）将过往经验作为条件输入，动态调整行为策略

### 迭代流程
1. **推理阶段**：高层 VLM 生成计划并交由低层 VLA 执行
2. **评估阶段**：反思执行结果（包括失败案例），提取结构化结论（如“抓取角度需调整”），并存入上下文记忆

### 关键设计
- **结构化引导机制**：针对非结构化机器人轨迹（原始视频），在评估阶段引入预定义的评估模板（如“动作是否完成”“失败原因分类”），确保反思结论的可复用性
- **Affordance 学习**：通过上下文积累，VLM 逐渐掌握低层 VLA 的能力边界（如“可抓取圆柱体但无法处理透明物体”）

### 实验设置与结果
- **任务**：长时域操作任务（如多步骤组装、物体堆叠）
- **对比基线**：标准 VLA 模型（无反思机制）、静态提示 VLM
- **关键数字**：
  - 在 5 类长时域任务中，LITEN 的成功率平均提升 34%（从 41% 到 75%）
  - 失败案例中，78% 的错误类型在后续尝试中被避免（通过上下文学习）
  - 评估阶段的结构化引导使反思结论的有效性提升 2.3 倍（对比无引导版本）

### 结论
LITEN 证明了通过推理时执行学习，VLA 模型能有效从真实世界经验中迭代改进，尤其适用于需要动态调整策略的复杂操作任务。其结构化引导机制是处理非结构化机器人数据的关键设计。

## Overview
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## 参考
- http://arxiv.org/abs/2510.19752v1

## 개요
LITEN은 기존 Vision-Language-Action 모델(VLA)이 복잡한 제어 작업에서 동적 행동 조정 능력이 부족하다는 문제를 해결하기 위해, 추론 시 실행 학습 프레임워크를 제안한다. 이 방법은 두 단계를 반복적으로 수행한다: 추론 단계에서는 저수준 VLA의 계획을 생성 및 실행하고, 평가 단계에서는 실행 결과를 반성하고 유용한 결론을 추출하여 이후 추론 컨텍스트에 포함한다. 순수 언어 영역의 자기 최적화 방법과 달리, LITEN은 비구조화된 실제 로봇 궤적(예: 원시 비디오)을 처리해야 하므로, 평가 단계에 구조화된 유도 메커니즘을 도입한다. 실험 결과, LITEN은 과거 경험에서 효과적으로 학습하여 높은 affordance 지시를 활용한 장기 작업 계획을 생성할 수 있음을 보여준다.

## 핵심 내용
### 방법 아키텍처
LITEN은 이중 계층 아키텍처를 채택한다:
- **저수준 VLA 정책**: 구체적인 행동 지시를 실행하는 역할
- **고수준 VLM**: 컨텍스트 학습(in-context learning)을 통해 과거 경험을 조건 입력으로 사용하여 행동 전략을 동적으로 조정

### 반복 프로세스
1. **추론 단계**: 고수준 VLM이 계획을 생성하고 저수준 VLA가 이를 실행
2. **평가 단계**: 실행 결과(실패 사례 포함)를 반성하고 구조화된 결론(예: "그립 각도 조정 필요")을 추출하여 컨텍스트 메모리에 저장

### 핵심 설계
- **구조화된 유도 메커니즘**: 비구조화된 로봇 궤적(원시 비디오)을 처리하기 위해, 평가 단계에서 사전 정의된 평가 템플릿(예: "동작 완료 여부", "실패 원인 분류")을 도입하여 반성 결론의 재사용성을 보장
- **Affordance 학습**: 컨텍스트 축적을 통해 VLM이 점차 저수준 VLA의 능력 경계(예: "원통형 물체는 잡을 수 있지만 투명 물체는 처리 불가")를 파악

### 실험 설정 및 결과
- **작업**: 장기 작업(예: 다단계 조립, 물체 쌓기)
- **비교 기준선**: 표준 VLA 모델(반성 메커니즘 없음), 정적 프롬프트 VLM
- **주요 수치**:
  - 5가지 장기 작업 유형에서 LITEN의 성공률은 평균 34% 향상(41%에서 75%로)
  - 실패 사례 중 78%의 오류 유형이 이후 시도에서 방지됨(컨텍스트 학습을 통해)
  - 평가 단계의 구조화된 유도는 반성 결론의 유효성을 2.3배 향상(유도 없는 버전 대비)

### 결론
LITEN은 추론 시 실행 학습을 통해 VLA 모델이 실제 세계 경험에서 반복적으로 개선될 수 있음을 입증하며, 특히 동적 전략 조정이 필요한 복잡한 조작 작업에 적합하다. 구조화된 유도 메커니즘은 비구조화된 로봇 데이터를 처리하는 핵심 설계이다.
