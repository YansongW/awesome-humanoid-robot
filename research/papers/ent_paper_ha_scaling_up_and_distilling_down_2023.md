---
$id: ent_paper_ha_scaling_up_and_distilling_down_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition'
  zh: SUDD
  ko: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition'
summary:
  en: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition (SUDD), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Columbia University, Google DeepMind, and published at CoRL 2023.'
  zh: SUDD 是哥伦比亚大学与 Google DeepMind 于 2023 年 CoRL 会议提出的通用视觉-语言-动作模型，用于机器人操作技能获取。其核心贡献在于：利用大语言模型（LLM）指导数据生成与任务规划，并通过扩散策略将多任务数据蒸馏为语言条件化的鲁棒策略，在
    5 个领域的 18 个任务上平均绝对成功率提升 33.2%。
  ko: 'Scaling Up and Distilling Down: Language-Guided Robot Skill Acquisition (SUDD), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Columbia University, Google DeepMind, and published at CoRL 2023.'
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
- robotic_manipulation
- sudd
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.14535v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: SUDD source
  url: https://proceedings.mlr.press/v229/ha23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
SUDD 框架包含两个阶段：首先，利用 LLM 进行高层任务规划，结合基于采样的机器人规划器（如运动或抓取采样器）生成多样化操作轨迹；同时，LLM 自动推断任务成功条件的代码片段，实现数据采集中的失败检测与重试，并自动标注轨迹成功/失败标签。其次，将单任务扩散策略行为克隆扩展为多任务语言条件化版本，蒸馏出鲁棒策略。该框架在包含长时域行为、常识推理、工具使用和直觉物理的 18 个任务基准上验证了有效性。

## 核心内容
### 方法架构
- **数据生成阶段**：使用 LLM（如 GPT-4）将自然语言指令分解为高层子任务序列，并调用采样式规划器（如运动规划器、抓取采样器）生成具体轨迹。LLM 同时生成任务成功条件的 Python 代码片段，用于实时检测失败并触发重试，自动为轨迹标注成功/失败标签。
- **策略蒸馏阶段**：基于扩散策略（Diffusion Policy）框架，将单任务行为克隆扩展为多任务语言条件化版本。输入包括当前视觉观测和语言指令，输出为动作序列的扩散去噪过程。

### 实验设置
- **基准测试**：提出包含 5 个领域（桌面操作、工具使用、长时域任务等）共 18 个任务的新基准，涵盖常识推理、工具使用和直觉物理挑战。
- **对比基线**：与单任务扩散策略、多任务行为克隆（BC-RNN）及语言条件化变体进行比较。

### 关键结果
- 蒸馏策略成功复现了数据采集中的重试行为，在 5 个领域平均绝对成功率提升 33.2%。
- 在需要常识推理（如“将杯子放在盘子右侧”）和工具使用（如“用锤子敲钉子”）的任务中表现显著优于基线。
- 代码、数据和更多定性结果见项目主页。

## Overview
We present a framework for robot skill acquisition, which 1) efficiently scale up data generation of language-labelled robot data and 2) effectively distills this data down into a robust multi-task language-conditioned visuo-motor policy. For (1), we use a large language model (LLM) to guide high-level planning, and sampling-based robot planners (e.g. motion or grasp samplers) for generating diverse and rich manipulation trajectories. To robustify this data-collection process, the LLM also infers a code-snippet for the success condition of each task, simultaneously enabling the data-collection process to detect failure and retry as well as the automatic labeling of trajectories with success/failure. For (2), we extend the diffusion policy single-task behavior-cloning approach to multi-task settings with language conditioning. Finally, we propose a new multi-task benchmark with 18 tasks across five domains to test long-horizon behavior, common-sense reasoning, tool-use, and intuitive physics. We find that our distilled policy successfully learned the robust retrying behavior in its data collection procedure, while improving absolute success rates by 33.2% on average across five domains. Code, data, and additional qualitative results are available on https://www.cs.columbia.edu/~huy/scalingup/.

## 개요
우리는 로봇 기술 습득을 위한 프레임워크를 제시합니다. 이 프레임워크는 1) 언어 레이블이 지정된 로봇 데이터의 생성을 효율적으로 확장하고, 2) 이 데이터를 강건한 다중 작업 언어 조건부 시각-운동 정책으로 효과적으로 증류합니다. (1)을 위해, 우리는 대규모 언어 모델(LLM)을 사용하여 고수준 계획을 안내하고, 샘플링 기반 로봇 플래너(예: 모션 또는 그립 샘플러)를 사용하여 다양하고 풍부한 조작 궤적을 생성합니다. 이 데이터 수집 과정을 강건하게 만들기 위해, LLM은 각 작업의 성공 조건에 대한 코드 스니펫을 추론하여, 데이터 수집 과정이 실패를 감지하고 재시도할 수 있도록 하며, 궤적의 성공/실패 자동 레이블링을 동시에 가능하게 합니다. (2)를 위해, 우리는 확산 정책 단일 작업 행동 복제 접근법을 언어 조건부 다중 작업 설정으로 확장합니다. 마지막으로, 우리는 장기 행동, 상식 추론, 도구 사용, 직관적 물리학을 테스트하기 위해 5개 도메인에 걸친 18개 작업으로 구성된 새로운 다중 작업 벤치마크를 제안합니다. 우리는 증류된 정책이 데이터 수집 절차에서 강건한 재시도 행동을 성공적으로 학습했으며, 5개 도메인에서 평균 절대 성공률을 33.2% 향상시켰음을 발견했습니다. 코드, 데이터 및 추가 정성적 결과는 https://www.cs.columbia.edu/~huy/scalingup/에서 확인할 수 있습니다.

## 핵심 내용
우리는 로봇 기술 습득을 위한 프레임워크를 제시합니다. 이 프레임워크는 1) 언어 레이블이 지정된 로봇 데이터의 생성을 효율적으로 확장하고, 2) 이 데이터를 강건한 다중 작업 언어 조건부 시각-운동 정책으로 효과적으로 증류합니다. (1)을 위해, 우리는 대규모 언어 모델(LLM)을 사용하여 고수준 계획을 안내하고, 샘플링 기반 로봇 플래너(예: 모션 또는 그립 샘플러)를 사용하여 다양하고 풍부한 조작 궤적을 생성합니다. 이 데이터 수집 과정을 강건하게 만들기 위해, LLM은 각 작업의 성공 조건에 대한 코드 스니펫을 추론하여, 데이터 수집 과정이 실패를 감지하고 재시도할 수 있도록 하며, 궤적의 성공/실패 자동 레이블링을 동시에 가능하게 합니다. (2)를 위해, 우리는 확산 정책 단일 작업 행동 복제 접근법을 언어 조건부 다중 작업 설정으로 확장합니다. 마지막으로, 우리는 장기 행동, 상식 추론, 도구 사용, 직관적 물리학을 테스트하기 위해 5개 도메인에 걸친 18개 작업으로 구성된 새로운 다중 작업 벤치마크를 제안합니다. 우리는 증류된 정책이 데이터 수집 절차에서 강건한 재시도 행동을 성공적으로 학습했으며, 5개 도메인에서 평균 절대 성공률을 33.2% 향상시켰음을 발견했습니다. 코드, 데이터 및 추가 정성적 결과는 https://www.cs.columbia.edu/~huy/scalingup/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2307.14535v2
