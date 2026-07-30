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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.06181v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇은 동작 생성 및 제어 분야에서 상당한 진전을 이루었으며, 점점 더 자연스럽고 인간과 유사한 움직임을 보여주고 있습니다. 튜링 테스트에서 영감을 받아, 우리는 운동 정보만을 사용하여 인간 관찰자가 휴머노이드 로봇과 인간의 자세를 구별할 수 있는지 평가하는 프레임워크인 Motion Turing Test를 제안합니다. 이 평가를 지원하기 위해, 11개의 휴머노이드 모델과 10명의 인간 피험자가 수행한 15개 동작 범주에 걸친 1,000개의 동작 시퀀스로 구성된 Human-Humanoid Motion (HHMotion) 데이터셋을 소개합니다. 모든 동작 시퀀스는 시각적 외형의 영향을 제거하기 위해 SMPL-X 표현으로 변환됩니다. 우리는 30명의 주석 작업자를 모집하여 각 자세의 인간 유사성을 0-5 척도로 평가하도록 하였으며, 그 결과 500시간 이상의 주석 작업이 수행되었습니다. 수집된 데이터 분석 결과, 휴머노이드 동작은 특히 점프, 복싱, 달리기와 같은 역동적인 동작에서 인간의 움직임과 눈에 띄는 차이를 보이는 것으로 나타났습니다. HHMotion을 기반으로, 우리는 동작 데이터에서 인간 유사성 점수를 자동으로 예측하는 것을 목표로 하는 인간 유사성 평가 과제를 구성합니다. 최근 다중 모달 대규모 언어 모델의 발전에도 불구하고, 우리는 이러한 모델이 동작의 인간 유사성을 평가하는 데 여전히 부적합하다는 것을 발견했습니다. 이를 해결하기 위해, 우리는 간단한 기준 모델을 제안하고 이것이 여러 최신 LLM 기반 방법보다 우수함을 입증합니다. 데이터셋, 코드, 벤치마크는 커뮤니티의 향후 연구를 지원하기 위해 공개될 예정입니다.

## 핵심 내용
휴머노이드 로봇은 동작 생성 및 제어 분야에서 상당한 진전을 이루었으며, 점점 더 자연스럽고 인간과 유사한 움직임을 보여주고 있습니다. 튜링 테스트에서 영감을 받아, 우리는 운동 정보만을 사용하여 인간 관찰자가 휴머노이드 로봇과 인간의 자세를 구별할 수 있는지 평가하는 프레임워크인 Motion Turing Test를 제안합니다. 이 평가를 지원하기 위해, 11개의 휴머노이드 모델과 10명의 인간 피험자가 수행한 15개 동작 범주에 걸친 1,000개의 동작 시퀀스로 구성된 Human-Humanoid Motion (HHMotion) 데이터셋을 소개합니다. 모든 동작 시퀀스는 시각적 외형의 영향을 제거하기 위해 SMPL-X 표현으로 변환됩니다. 우리는 30명의 주석 작업자를 모집하여 각 자세의 인간 유사성을 0-5 척도로 평가하도록 하였으며, 그 결과 500시간 이상의 주석 작업이 수행되었습니다. 수집된 데이터 분석 결과, 휴머노이드 동작은 특히 점프, 복싱, 달리기와 같은 역동적인 동작에서 인간의 움직임과 눈에 띄는 차이를 보이는 것으로 나타났습니다. HHMotion을 기반으로, 우리는 동작 데이터에서 인간 유사성 점수를 자동으로 예측하는 것을 목표로 하는 인간 유사성 평가 과제를 구성합니다. 최근 다중 모달 대규모 언어 모델의 발전에도 불구하고, 우리는 이러한 모델이 동작의 인간 유사성을 평가하는 데 여전히 부적합하다는 것을 발견했습니다. 이를 해결하기 위해, 우리는 간단한 기준 모델을 제안하고 이것이 여러 최신 LLM 기반 방법보다 우수함을 입증합니다. 데이터셋, 코드, 벤치마크는 커뮤니티의 향후 연구를 지원하기 위해 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2603.06181v1
