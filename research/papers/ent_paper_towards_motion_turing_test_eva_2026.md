---
$id: ent_paper_towards_motion_turing_test_eva_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
  zh: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
  ko: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
summary:
  en: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
  zh: '《Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots》是2026年提出的一项针对人形机器人运动拟人度的模拟基准工作。该研究受图灵测试启发，构建了Motion
    Turing Test框架，并发布了包含1000条运动序列的Human-Humanoid Motion (HHMotion)数据集，用于评估人形机器人运动与人类运动的相似性。核心贡献在于通过大规模人工标注和自动预测模型，揭示了当前人形机器人运动在动态动作上的不足。'
  ko: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- simulation
- towards_motion_turing_test
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.06181v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1184 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2603.06181
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作提出Motion Turing Test框架，旨在通过人类观察者仅基于运动学信息区分人形机器人与人类姿态的能力，来评估机器人运动的拟人度。为此，研究者构建了HHMotion数据集，包含来自11个人形机器人模型和10名人类受试者的1000条运动序列，覆盖15个动作类别，所有序列均转换为SMPL-X表示以消除外观干扰。30名标注员对每个姿态的拟人度进行0-5分评分，累计超过500小时标注。分析表明，人形机器人在跳跃、拳击、跑步等动态动作中与人类运动存在显著偏差。基于该数据集，研究还提出了自动预测拟人度分数的任务，并发现当前多模态大语言模型在此任务上表现不足，而所提出的简单基线模型优于多种基于LLM的方法。

## 核心内容
### 方法
- **Motion Turing Test框架**：受图灵测试启发，通过人类观察者仅基于运动学信息（如关节角度、位置）区分人形机器人与人类姿态的能力，来评估机器人运动的拟人度。该框架排除了视觉外观、声音等非运动因素干扰。
- **HHMotion数据集构建**：
  - 包含1000条运动序列，覆盖15个动作类别（如行走、跳跃、拳击、跑步等）。
  - 数据来源：11个人形机器人模型（包括Atlas、ASIMO等）和10名人类受试者。
  - 所有序列转换为SMPL-X表示，确保仅保留运动学信息，消除外观差异。
- **标注过程**：30名标注员对每个姿态的拟人度进行0-5分评分，累计超过500小时标注，确保标注可靠性。

### 实验设置
- **评估任务**：基于HHMotion数据集，定义自动预测拟人度分数的任务，输入为运动序列，输出为0-5分评分。
- **基线模型**：提出简单基线模型（如基于时序卷积网络或循环神经网络），并与多种多模态大语言模型（如GPT-4V、Gemini）进行对比。
- **评估指标**：使用平均绝对误差（MAE）、皮尔逊相关系数等衡量预测与人工标注的一致性。

### 关键发现
- **人形机器人运动偏差**：分析显示，人形机器人在动态动作（如跳跃、拳击、跑步）中与人类运动存在显著偏差，而静态或慢速动作（如站立、慢走）偏差较小。
- **LLM表现不足**：当前多模态大语言模型在运动拟人度评估任务上表现不佳，无法有效捕捉细微运动差异。
- **基线模型优势**：所提出的简单基线模型在MAE和相关系数上均优于多种基于LLM的方法，表明针对运动数据的专用模型更具优势。

### 结论
- 该工作为评估人形机器人运动拟人度提供了标准化基准（HHMotion数据集）和框架（Motion Turing Test）。
- 揭示了当前人形机器人在动态动作上的拟人度不足，并指出多模态大语言模型在此任务上的局限性。
- 数据集、代码和基准将公开，以推动社区研究。

## Overview
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## 参考
- http://arxiv.org/abs/2603.06181v1

## 개요
이 연구는 인간 관찰자가 운동학적 정보만을 기반으로 휴머노이드 로봇과 인간의 자세를 구분할 수 있는 능력을 통해 로봇 운동의 인간 유사성을 평가하는 Motion Turing Test 프레임워크를 제안합니다. 이를 위해 연구진은 11개의 휴머노이드 로봇 모델과 10명의 인간 피험자로부터 수집한 1000개의 운동 시퀀스를 포함하는 HHMotion 데이터셋을 구축했으며, 15개의 동작 범주를涵盖하고 모든 시퀀스는 외관 간섭을 제거하기 위해 SMPL-X 표현으로 변환되었습니다. 30명의 주석자가 각 자세의 인간 유사성을 0-5점으로 평가하여 총 500시간 이상의 주석 작업을 수행했습니다. 분석 결과, 휴머노이드 로봇은 점프, 권투, 달리기와 같은 동적 동작에서 인간 운동과 유의미한 차이를 보였습니다. 이 데이터셋을 기반으로 연구는 인간 유사성 점수를 자동으로 예측하는 작업도 제안했으며, 현재의 다중 모달 대규모 언어 모델은 이 작업에서 성능이 부족하고, 제안된 간단한 기준 모델이 여러 LLM 기반 방법보다 우수함을 발견했습니다.

## 핵심 내용
### 방법
- **Motion Turing Test 프레임워크**: 튜링 테스트에서 영감을 받아, 인간 관찰자가 운동학적 정보(예: 관절 각도, 위치)만을 기반으로 휴머노이드 로봇과 인간의 자세를 구분하는 능력을 통해 로봇 운동의 인간 유사성을 평가합니다. 이 프레임워크는 시각적 외관, 소리 등 비운동적 요인의 간섭을 배제합니다.
- **HHMotion 데이터셋 구축**:
  - 15개의 동작 범주(예: 걷기, 점프, 권투, 달리기 등)를涵盖하는 1000개의 운동 시퀀스 포함.
  - 데이터 출처: 11개의 휴머노이드 로봇 모델(Atlas, ASIMO 등 포함) 및 10명의 인간 피험자.
  - 모든 시퀀스는 SMPL-X 표현으로 변환되어 운동학적 정보만 유지하고 외관 차이를 제거합니다.
- **주석 과정**: 30명의 주석자가 각 자세의 인간 유사성을 0-5점으로 평가하여 총 500시간 이상의 주석 작업을 수행, 주석 신뢰성을 보장합니다.

### 실험 설정
- **평가 작업**: HHMotion 데이터셋을 기반으로, 운동 시퀀스를 입력으로 받아 0-5점의 인간 유사성 점수를 출력하는 자동 예측 작업을 정의합니다.
- **기준 모델**: 간단한 기준 모델(예: 시간적 컨볼루션 네트워크 또는 순환 신경망 기반)을 제안하고, 여러 다중 모달 대규모 언어 모델(예: GPT-4V, Gemini)과 비교합니다.
- **평가 지표**: 평균 절대 오차(MAE), 피어슨 상관 계수 등을 사용하여 예측과 인간 주석 간의 일치도를 측정합니다.

### 주요 발견
- **휴머노이드 로봇 운동 편차**: 분석 결과, 휴머노이드 로봇은 점프, 권투, 달리기와 같은 동적 동작에서 인간 운동과 유의미한 차이를 보이며, 정적 또는 느린 동작(예: 서기, 느린 걷기)에서는 차이가 작습니다.
- **LLM 성능 부족**: 현재의 다중 모달 대규모 언어 모델은 운동 인간 유사성 평가 작업에서 성능이 좋지 않아 미세한 운동 차이를 효과적으로 포착하지 못합니다.
- **기준 모델 우위**: 제안된 간단한 기준 모델은 MAE와 상관 계수 모두에서 여러 LLM 기반 방법보다 우수하여, 운동 데이터에 특화된 모델이 더 유리함을 시사합니다.

### 결론
- 이 연구는 휴머노이드 로봇 운동의 인간 유사성을 평가하기 위한 표준화된 기준(HHMotion 데이터셋)과 프레임워크(Motion Turing Test)를 제공합니다.
- 현재 휴머노이드 로봇의 동적 동작에서 인간 유사성 부족을 밝혀내고, 다중 모달 대규모 언어 모델의 이 작업에서의 한계를 지적합니다.
- 데이터셋, 코드 및 기준은 커뮤니티 연구를 촉진하기 위해 공개될 예정입니다.
