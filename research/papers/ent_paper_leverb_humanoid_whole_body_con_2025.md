---
$id: ent_paper_leverb_humanoid_whole_body_con_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
  zh: LeVERB｜具有潜在视觉语言指令的人形全身控制
  ko: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
summary:
  en: 'Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet
    most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector
    pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors
    required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the
    first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories.
    We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework
    for humanoid vision-language WBC, the first of its kind. At the'
  zh: LeVERB 是一个面向人形机器人全身控制（WBC）的层级式潜在指令跟随框架，由研究团队首次提出。其核心贡献包括：构建了首个包含150余项任务的视觉-语言闭环基准测试，并实现了零样本条件下80%的简单导航任务成功率与58.5%的整体成功率，性能较传统层级式VLA方案提升7.8倍。
  ko: LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- contact_planning
- leverb
- mobile_manipulation
- task_planning
- visual_closed_loop
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: LeVERB: Humanoid Whole-Body
    Control with Latent Vision-Language Instruction. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (732 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: LeVERB project page
  url: https://github.com/ember-lab-berkeley/LeVERB-Website
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
现有视觉-语言-动作（VLA）模型依赖手工设计的动作词汇（如末端执行器位姿或根部速度），仅适用于准静态任务，无法满足人形机器人全身控制所需的敏捷行为。为填补这一空白，研究团队首先推出了首个面向人形WBC的视觉-语言闭环基准测试，涵盖10大类150余项任务。在此基础上提出LeVERB框架，其顶层通过合成运动学演示学习潜在动作词汇，底层则利用强化学习策略生成动力学级指令，实现层级式潜在指令跟随。

## 核心内容
### 方法架构
- **顶层**：视觉-语言策略从合成渲染的运动学演示中学习潜在动作词汇（latent action vocabulary），将自然语言指令映射为抽象行为编码。
- **底层**：强化学习训练的WBC策略接收这些潜在动词（latent verbs），生成关节力矩等动力学级控制指令，实现全身协调运动。

### 基准测试
- 首个sim-to-real就绪的视觉-语言闭环基准，包含10个任务类别（如导航、操作、平衡等），总计超过150项子任务。
- 任务设计覆盖动态场景（如避障、抓取移动物体），要求全身关节协同响应。

### 实验设置
- 训练数据：合成渲染的运动学演示，无需真实机器人数据。
- 评估指标：零样本任务成功率，对比基线为传统层级式VLA（直接输出末端位姿指令）。

### 关键结果
- 简单视觉导航任务零样本成功率：80%
- 整体任务零样本成功率：58.5%
- 性能对比：较传统层级式VLA方案提升7.8倍（后者成功率仅约7.5%）

### 结论
LeVERB通过潜在动作词汇解耦语义理解与动力学控制，首次实现人形机器人全身VLA闭环控制，验证了层级式潜在指令框架在复杂动态任务中的有效性。

## Overview
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain a 80% success rate on simple visual navigation tasks, and 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## Overview
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action "vocabulary" such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain an 80% success rate on simple visual navigation tasks, and a 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## Content
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action "vocabulary" such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain an 80% success rate on simple visual navigation tasks, and a 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## 参考
- Semantic Scholar search: LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction

## 개요
기존의 비전-언어-행동(VLA) 모델은 수작업으로 설계된 행동 어휘(예: 말단 실행기 자세 또는 루트 속도)에 의존하며, 준정적 작업에만 적용 가능하여 휴머노이드 로봇의 전신 제어에 필요한 민첩한 행동을 충족할 수 없습니다. 이러한 공백을 메우기 위해 연구팀은 먼저 휴머노이드 WBC를 위한 최초의 비전-언어 폐루프 벤치마크를 출시했으며, 10개 대분류 150여 개 작업을 포함합니다. 이를 바탕으로 LeVERB 프레임워크를 제안하며, 상위 계층은 합성 운동학 데모를 통해 잠재 행동 어휘를 학습하고, 하위 계층은 강화 학습 정책을 활용하여 동역학 수준의 명령을 생성하여 계층적 잠재 명령 추종을 구현합니다.

## 핵심 내용
### 방법 아키텍처
- **상위 계층**: 비전-언어 정책이 합성 렌더링된 운동학 데모에서 잠재 행동 어휘(latent action vocabulary)를 학습하여 자연어 명령을 추상 행동 인코딩으로 매핑합니다.
- **하위 계층**: 강화 학습으로 훈련된 WBC 정책이 이러한 잠재 동사(latent verbs)를 수신하여 관절 토크와 같은 동역학 수준의 제어 명령을 생성하고 전신 협조 운동을 구현합니다.

### 벤치마크
- 시뮬레이션-실제(sim-to-real) 준비가 완료된 최초의 비전-언어 폐루프 벤치마크로, 10개 작업 범주(예: 내비게이션, 조작, 균형 등)를 포함하며 총 150개 이상의 하위 작업으로 구성됩니다.
- 작업 설계는 동적 시나리오(예: 장애물 회피, 이동 물체 잡기)를 포함하며, 전신 관절의 협조적 응답을 요구합니다.

### 실험 설정
- 훈련 데이터: 합성 렌더링된 운동학 데모로, 실제 로봇 데이터가 필요 없습니다.
- 평가 지표: 제로샷 작업 성공률, 기준선은 전통적인 계층형 VLA(말단 자세 명령 직접 출력)와 비교합니다.

### 주요 결과
- 단순 시각 내비게이션 작업 제로샷 성공률: 80%
- 전체 작업 제로샷 성공률: 58.5%
- 성능 비교: 전통적인 계층형 VLA 방식 대비 7.8배 향상(후자의 성공률은 약 7.5%에 불과)

### 결론
LeVERB는 잠재 행동 어휘를 통해 의미 이해와 동역학 제어를 분리하여, 휴머노이드 로봇의 전신 VLA 폐루프 제어를 최초로 구현했으며, 복잡한 동적 작업에서 계층적 잠재 명령 프레임워크의 효율성을 검증했습니다.
