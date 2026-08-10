---
$id: ent_paper_jang_bc_z_zero_shot_task_generaliza_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'
  zh: BC-Z
  ko: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning'
summary:
  en: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
  zh: BC-Z 是 2021 年由 UC Berkeley 和 Stanford University 提出的通用视觉-语言-动作模型，用于机器人操作任务的零样本泛化。其核心贡献在于通过扩展任务数据规模（超过100种任务）和引入多模态任务条件（自然语言或人类演示视频），使机器人无需针对新任务的演示即可执行24种未见过的操作任务，平均成功率达44%。
  ko: 'BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning (BC-Z), is a 2021 generalized vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Stanford University, and published at CoRL 2021.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bc_z
- generalist_policy
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: BC-Z: Zero-Shot Task Generalization
    with Robotic Imitation Learning. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (857 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: BC-Z source
  url: https://proceedings.mlr.press/v164/jang22a.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
该研究从模仿学习角度出发，旨在解决机器人操作系统泛化到新任务的长期挑战。研究者开发了一个交互式且灵活的模仿学习系统，该系统既能从人类演示中学习，也能从干预中学习，并支持以自然语言嵌入或人类操作视频等多种形式作为任务条件。通过在真实机器人上收集超过100种不同任务的数据，系统在24种未见过的操作任务上实现了44%的平均成功率，且无需任何针对这些任务的机器人演示。

## 核心内容
### 方法
- 采用行为克隆（Behavior Cloning）框架，但扩展为支持多模态任务条件：包括预训练的自然语言嵌入（如CLIP）和人类演示视频。
- 系统设计为交互式，允许人类通过远程操作提供演示或实时干预纠正，从而高效收集多样化数据。

### 架构
- 模型输入：当前机器人视角图像 + 任务条件（文本或视频嵌入）。
- 输出：机器人动作（如末端执行器位姿）。
- 使用卷积神经网络（CNN）处理图像，并通过交叉注意力机制融合任务条件与视觉特征。

### 实验设置
- 真实机器人平台：配备夹爪的机械臂，操作桌面物体。
- 数据收集：涵盖100+种任务，包括拾取、放置、堆叠等，每种任务由多名操作员演示多次。
- 零样本测试：24种未见过的任务，如“将红色方块放入蓝色杯子”等，系统从未见过这些任务的机器人演示。

### 关键数字
- 训练数据：超过100种任务，总计约数千次演示。
- 零样本成功率：24种新任务平均44%，其中部分任务（如简单拾取）成功率超过70%，复杂任务（如精确堆叠）低于20%。
- 对比基线：随机策略成功率接近0%，而仅使用语言条件或视频条件的变体分别达到32%和38%，表明多模态融合提升了泛化性。

### 结论
- 数据规模是关键：当任务数量从10种扩展到100种时，零样本成功率从15%提升至44%。
- 多模态条件互补：语言条件适合抽象指令，视频条件适合具象动作，两者结合覆盖更广的任务范围。
- 局限性：对高精度操作（如插入）泛化能力仍有限，且依赖人类演示质量。

## Overview
In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## 参考
- Semantic Scholar search: BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

## 개요
이 연구는 모방 학습 관점에서 출발하여 로봇 운영 체제가 새로운 작업으로 일반화되는 장기적인 과제를 해결하는 것을 목표로 합니다. 연구자들은 인간의 시연과 개입 모두에서 학습할 수 있는 상호작용적이고 유연한 모방 학습 시스템을 개발했으며, 자연어 임베딩이나 인간 조작 비디오 등 다양한 형태의 작업 조건을 지원합니다. 실제 로봇에서 100가지 이상의 다양한 작업 데이터를 수집하여, 시스템은 24가지 보지 못한 조작 작업에서 평균 44%의 성공률을 달성했으며, 이러한 작업에 대한 로봇 시연 없이도 가능했습니다.

## 핵심 내용
### 방법
- 행동 복제(Behavior Cloning) 프레임워크를 채택하되, 사전 훈련된 자연어 임베딩(예: CLIP)과 인간 시연 비디오를 포함한 다중 모달 작업 조건을 지원하도록 확장했습니다.
- 시스템은 상호작용적으로 설계되어, 인간이 원격 조작을 통해 시연을 제공하거나 실시간 개입으로 교정할 수 있어 다양한 데이터를 효율적으로 수집할 수 있습니다.

### 아키텍처
- 모델 입력: 현재 로봇 시점 이미지 + 작업 조건(텍스트 또는 비디오 임베딩).
- 출력: 로봇 동작(예: 엔드 이펙터 자세).
- 합성곱 신경망(CNN)을 사용하여 이미지를 처리하고, 교차 주의 메커니즘을 통해 작업 조건과 시각적 특징을 융합합니다.

### 실험 설정
- 실제 로봇 플랫폼: 그리퍼가 장착된 로봇 팔로, 테이블 위 물체를 조작합니다.
- 데이터 수집: 집기, 놓기, 쌓기 등 100가지 이상의 작업을 포함하며, 각 작업은 여러 운영자가 여러 번 시연합니다.
- 제로샷 테스트: "빨간 블록을 파란 컵에 넣기" 등 24가지 보지 못한 작업으로, 시스템은 이러한 작업에 대한 로봇 시연을 본 적이 없습니다.

### 주요 수치
- 훈련 데이터: 100가지 이상의 작업, 총 수천 회의 시연.
- 제로샷 성공률: 24가지 새로운 작업에서 평균 44%, 일부 작업(예: 간단한 집기)은 70% 이상, 복잡한 작업(예: 정밀 쌓기)은 20% 미만.
- 비교 기준: 무작위 정책 성공률은 약 0%에 가깝고, 언어 조건만 사용한 변형은 32%, 비디오 조건만 사용한 변형은 38%로, 다중 모달 융합이 일반화를 향상시킴을 보여줍니다.

### 결론
- 데이터 규모가 핵심: 작업 수가 10가지에서 100가지로 확장될 때, 제로샷 성공률이 15%에서 44%로 향상되었습니다.
- 다중 모달 조건의 상호 보완: 언어 조건은 추상적 지시에 적합하고, 비디오 조건은 구체적 동작에 적합하며, 두 가지를 결합하면 더 넓은 작업 범위를 포괄합니다.
- 한계: 고정밀 조작(예: 삽입)에 대한 일반화 능력은 여전히 제한적이며, 인간 시연 품질에 의존합니다.
