---
$id: ent_paper_lynch_interactive_language_talking_t_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Interactive Language: Talking to Robots in Real Time'
  zh: Interactive Language
  ko: 'Interactive Language: Talking to Robots in Real Time'
summary:
  en: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
  zh: Interactive Language 是 Google Robotics 于 2022 年提出的通用视觉-语言-动作模型，用于机器人实时操控。其核心贡献在于通过行为克隆训练，使机器人能理解并执行 87,000 条独特自然语言指令，在真实世界任务中达到
    93.5% 的成功率。该工作还开源了包含近 60 万条语言标注轨迹的数据集、环境、基准和策略。
  ko: 'Interactive Language: Talking to Robots in Real Time (Interactive Language), is a 2022 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google.'
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
- interactive_language
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.06407v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (717 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Interactive Language: Talking to Robots in Real Time (arXiv)'
  url: https://arxiv.org/abs/2210.06407
  date: '2022'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Interactive Language source
  url: https://doi.org/10.48550/arXiv.2210.06407
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
该研究构建了一个在真实世界中通过自然语言实时交互的机器人框架。模型采用行为克隆方法，在数十万条语言标注轨迹上训练，最终能执行比以往工作多一个数量级的指令。实验表明，同一策略可被人类通过实时语言引导完成精确的长时序重排任务，例如“用积木拼出笑脸”。发布的公开数据集包含近 60 万条语言标注轨迹，规模是此前最大数据集的十倍。

## 核心内容
### 方法架构
- 提出端到端的视觉-语言-动作模型，直接处理原始视觉输入、自然语言指令并输出机器人动作。
- 采用行为克隆（Behavioral Cloning）作为训练范式，无需强化学习或人工奖励设计。

### 数据集与实验设置
- 数据集包含 **近 600,000 条** 语言标注的机器人操作轨迹，覆盖多种桌面操控场景。
- 测试集包含 **87,000 条** 独特的自然语言字符串，涵盖从简单抓取到复杂组合操作（如“将红色方块放在蓝色方块左侧”）的指令。
- 在真实物理机器人上评估，不依赖仿真环境。

### 关键结果
- 在 87,000 条独特语言指令上，模型达到 **93.5%** 的成功率，性能比此前最佳方法提升一个数量级。
- 同一策略支持实时人类语言引导，可完成长时序重排目标，例如“用积木拼出笑脸”这类需要多步推理的任务。
- 开源内容包括：数据集、仿真环境、标准化基准测试以及训练好的策略模型。

### 结论
该工作证明，通过大规模行为克隆训练，单一模型即可掌握广泛的语言引导操控技能，并支持实时交互。开源资源旨在推动自然语言交互机器人的进一步发展。演示视频见 https://interactive-language.github.io。

## Overview
We present a framework for building interactive, real-time, natural language-instructable robots in the real world, and we open source related assets (dataset, environment, benchmark, and policies). Trained with behavioral cloning on a dataset of hundreds of thousands of language-annotated trajectories, a produced policy can proficiently execute an order of magnitude more commands than previous works: specifically we estimate a 93.5% success rate on a set of 87,000 unique natural language strings specifying raw end-to-end visuo-linguo-motor skills in the real world. We find that the same policy is capable of being guided by a human via real-time language to address a wide range of precise long-horizon rearrangement goals, e.g. "make a smiley face out of blocks". The dataset we release comprises nearly 600,000 language-labeled trajectories, an order of magnitude larger than prior available datasets. We hope the demonstrated results and associated assets enable further advancement of helpful, capable, natural-language-interactable robots. See videos at https://interactive-language.github.io.

## 参考
- http://arxiv.org/abs/2210.06407v1

## 개요
이 연구는 실제 세계에서 자연어를 통해 실시간으로 상호작용하는 로봇 프레임워크를 구축했습니다. 모델은 행동 복제(Behavioral Cloning) 방식을 채택하여 수십만 개의 언어 주석 궤적에서 훈련되었으며, 기존 연구보다 한 자릿수 더 많은 명령을 실행할 수 있습니다. 실험 결과, 동일한 정책이 인간의 실시간 언어 안내를 통해 "블록으로 웃는 얼굴 만들기"와 같은 정밀한 장기 순차 재배치 작업을 완료할 수 있음을 보여줍니다. 공개된 데이터셋에는 약 60만 개의 언어 주석 궤적이 포함되어 있으며, 이는 이전 최대 데이터셋의 10배 규모입니다.

## 핵심 내용
### 방법 아키텍처
- 원시 시각 입력, 자연어 명령을 직접 처리하고 로봇 동작을 출력하는 엔드투엔드 비전-언어-행동 모델을 제안합니다.
- 강화 학습이나 수동 보상 설계 없이 행동 복제(Behavioral Cloning)를 훈련 패러다임으로 채택합니다.

### 데이터셋 및 실험 설정
- 데이터셋에는 **약 600,000개**의 언어 주석이 달린 로봇 조작 궤적이 포함되어 있으며, 다양한 데스크톱 조작 시나리오를 다룹니다.
- 테스트 세트에는 **87,000개의 고유한** 자연어 문자열이 포함되어 있으며, 단순 집기부터 "빨간 블록을 파란 블록 왼쪽에 놓기"와 같은 복잡한 조합 작업까지의 명령을 다룹니다.
- 시뮬레이션 환경에 의존하지 않고 실제 물리 로봇에서 평가합니다.

### 주요 결과
- 87,000개의 고유한 언어 명령에서 모델은 **93.5%**의 성공률을 달성했으며, 이전 최고 방법보다 성능이 한 자릿수 향상되었습니다.
- 동일한 정책은 실시간 인간 언어 안내를 지원하며, "블록으로 웃는 얼굴 만들기"와 같은 다단계 추론이 필요한 장기 순차 재배치 목표를 완료할 수 있습니다.
- 오픈소스 콘텐츠에는 데이터셋, 시뮬레이션 환경, 표준화된 벤치마크 테스트 및 훈련된 정책 모델이 포함됩니다.

### 결론
이 연구는 대규모 행동 복제 훈련을 통해 단일 모델이 광범위한 언어 안내 조작 기술을 습득하고 실시간 상호작용을 지원할 수 있음을 입증합니다. 오픈소스 리소스는 자연어 상호작용 로봇의 추가 발전을 촉진하기 위해 제공됩니다. 데모 비디오는 https://interactive-language.github.io에서 확인할 수 있습니다.
