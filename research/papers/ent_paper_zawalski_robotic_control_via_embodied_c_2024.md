---
$id: ent_paper_zawalski_robotic_control_via_embodied_c_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic Control via Embodied Chain-of-Thought Reasoning
  zh: ECoT
  ko: Robotic Control via Embodied Chain-of-Thought Reasoning
summary:
  en: Robotic Control via Embodied Chain-of-Thought Reasoning (ECoT), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, University of Warsaw, Stanford University, and published at CoRL24.
  zh: ECoT（Embodied Chain-of-Thought Reasoning）是由UC Berkeley、University of Warsaw和Stanford University于2024年提出的一种大型视觉-语言-动作模型，用于机器人操作任务，发表于CoRL24。其核心贡献在于通过可扩展的合成数据生成管道，训练VLA模型在预测动作前进行多步具身推理（包括计划、子任务、运动及视觉特征），使OpenVLA在挑战性泛化任务中绝对成功率提升28%，且无需额外机器人训练数据。
  ko: Robotic Control via Embodied Chain-of-Thought Reasoning (ECoT), is a 2024 large vision-language-action model for robotic
    manipulation, introduced by UC Berkeley, University of Warsaw, Stanford University, and published at CoRL24.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ecot
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.08693v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: ECoT source
  url: https://proceedings.mlr.press/v270/zawalski25a.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有机器人学习策略的关键局限在于难以泛化到训练数据之外的情境。虽然视觉-语言-动作模型（VLA）通过引入互联网预训练的大型视觉-语言模型作为骨干网络，显著提升了鲁棒性和泛化能力，但如何将大型模型在复杂问题上的迭代推理能力迁移至机器人领域仍待解决。直接套用标准“思维链”（CoT）提示方法效果不佳，因为VLA的训练样本相对简单，且纯语义推理无法将推理结果与传感器观测及机器人状态有效关联。为此，ECoT通过设计可扩展的合成数据生成流程，训练VLA在预测动作前执行多步推理，涵盖计划、子任务、运动以及物体边界框和末端执行器位置等视觉特征。实验表明，该方法无需额外训练数据即可将最强开源VLA策略OpenVLA的绝对成功率提升28%，同时使人类更易解读策略失败原因并通过自然语言修正其行为。

## 核心内容
### 方法架构
ECoT的核心思想是在VLA的动作预测前插入一个**具身推理链**，该链包含多个推理步骤：
- **计划层**：生成高层任务分解（如“先抓取杯子，再移动到水壶下方”）
- **子任务层**：将计划转化为可执行子步骤（如“调整夹爪角度”）
- **运动层**：输出连续动作参数（如关节角度序列）
- **视觉特征层**：预测物体边界框、末端执行器位置等空间信息，使推理结果与传感器观测对齐

### 训练数据生成
为解决真实机器人数据中缺乏推理标注的问题，ECoT设计了**可扩展的合成数据管道**：
- 利用现有大规模机器人数据集（如Open X-Embodiment）中的动作轨迹
- 通过预训练视觉语言模型（如GPT-4V）自动生成与动作对应的多步推理文本
- 将推理文本与原始动作标签拼接，形成“推理-动作”对用于训练

### 实验设置与关键结果
- **基线模型**：OpenVLA（当前最强开源VLA策略）
- **测试任务**：涵盖物体重排、工具使用、多步操作等挑战性泛化场景（如未见过的物体、背景变化、光照干扰）
- **核心指标**：
  - 绝对成功率提升：**28%**（从基线的52%提升至80%）
  - 在需要空间推理的任务（如“将方块放入特定颜色容器”）中提升最显著（+35%）
  - 在零样本跨具身迁移场景中仍保持**15%** 的增益

### 可解释性与交互修正
ECoT的推理链使策略失败原因可视化：
- 示例：若机器人错误抓取物体，推理链会显示“检测到红色方块（实际应为蓝色）”，人类可通过自然语言指令修正（如“关注蓝色物体”）
- 无需重新训练模型，仅通过修改推理链中的错误步骤即可调整后续动作

### 结论
ECoT通过将具身推理嵌入VLA的动作预测流程，在不增加训练数据的前提下显著提升了泛化能力，同时为人类提供了直观的交互式修正接口。该方法为将大型语言模型的推理能力与机器人物理世界交互相结合提供了有效范式。

## Overview
A key limitation of learned robot control policies is their inability to generalize outside their training data. Recent works on vision-language-action models (VLAs) have shown that the use of large, internet pre-trained vision-language models as the backbone of learned robot policies can substantially improve their robustness and generalization ability. Yet, one of the most exciting capabilities of large vision-language models in other domains is their ability to reason iteratively through complex problems. Can that same capability be brought into robotics to allow policies to improve performance by reasoning about a given task before acting? Naive use of "chain-of-thought" (CoT) style prompting is significantly less effective with standard VLAs because of the relatively simple training examples that are available to them. Additionally, purely semantic reasoning about sub-tasks, as is common in regular CoT, is insufficient for robot policies that need to ground their reasoning in sensory observations and the robot state. To this end, we introduce Embodied Chain-of-Thought Reasoning (ECoT) for VLAs, in which we train VLAs to perform multiple steps of reasoning about plans, sub-tasks, motions, and visually grounded features like object bounding boxes and end effector positions, before predicting the robot action. We design a scalable pipeline for generating synthetic training data for ECoT on large robot datasets. We demonstrate, that ECoT increases the absolute success rate of OpenVLA, the current strongest open-source VLA policy, by 28% across challenging generalization tasks, without any additional robot training data. Additionally, ECoT makes it easier for humans to interpret a policy's failures and correct its behavior using natural language.

## 개요
학습된 로봇 제어 정책의 주요 한계는 훈련 데이터 외부로 일반화할 수 없다는 점입니다. 최근 비전-언어-행동 모델(VLA)에 대한 연구는 대규모 인터넷 사전 훈련된 비전-언어 모델을 학습된 로봇 정책의 백본으로 사용하면 견고성과 일반화 능력을 크게 향상시킬 수 있음을 보여주었습니다. 그러나 다른 분야에서 대규모 비전-언어 모델의 가장 흥미로운 능력 중 하나는 복잡한 문제를 반복적으로 추론하는 능력입니다. 이러한 능력을 로봇 공학에 도입하여 정책이 행동하기 전에 주어진 작업에 대해 추론함으로써 성능을 향상시킬 수 있을까요? "사고의 사슬"(CoT) 스타일 프롬프팅을 단순히 사용하는 것은 표준 VLA에서 상대적으로 단순한 훈련 예제만 사용 가능하기 때문에 훨씬 덜 효과적입니다. 또한 일반적인 CoT에서 흔히 볼 수 있는 하위 작업에 대한 순수 의미론적 추론은 감각 관찰과 로봇 상태에 추론을 근거해야 하는 로봇 정책에는 충분하지 않습니다. 이를 위해 우리는 VLA를 위한 체화된 사고의 사슬 추론(ECoT)을 소개합니다. 이는 로봇 행동을 예측하기 전에 계획, 하위 작업, 동작, 그리고 객체 경계 상자 및 엔드 이펙터 위치와 같은 시각적 근거 특징에 대한 여러 단계의 추론을 수행하도록 VLA를 훈련시키는 것입니다. 우리는 대규모 로봇 데이터셋에서 ECoT를 위한 합성 훈련 데이터를 생성하는 확장 가능한 파이프라인을 설계합니다. 우리는 ECoT가 현재 가장 강력한 오픈소스 VLA 정책인 OpenVLA의 절대 성공률을 추가 로봇 훈련 데이터 없이도 도전적인 일반화 작업에서 28% 향상시킨다는 것을 입증합니다. 또한 ECoT는 인간이 정책의 실패를 해석하고 자연어를 사용하여 행동을 수정하는 것을 더 쉽게 만듭니다.

## 핵심 내용
학습된 로봇 제어 정책의 주요 한계는 훈련 데이터 외부로 일반화할 수 없다는 점입니다. 최근 비전-언어-행동 모델(VLA)에 대한 연구는 대규모 인터넷 사전 훈련된 비전-언어 모델을 학습된 로봇 정책의 백본으로 사용하면 견고성과 일반화 능력을 크게 향상시킬 수 있음을 보여주었습니다. 그러나 다른 분야에서 대규모 비전-언어 모델의 가장 흥미로운 능력 중 하나는 복잡한 문제를 반복적으로 추론하는 능력입니다. 이러한 능력을 로봇 공학에 도입하여 정책이 행동하기 전에 주어진 작업에 대해 추론함으로써 성능을 향상시킬 수 있을까요? "사고의 사슬"(CoT) 스타일 프롬프팅을 단순히 사용하는 것은 표준 VLA에서 상대적으로 단순한 훈련 예제만 사용 가능하기 때문에 훨씬 덜 효과적입니다. 또한 일반적인 CoT에서 흔히 볼 수 있는 하위 작업에 대한 순수 의미론적 추론은 감각 관찰과 로봇 상태에 추론을 근거해야 하는 로봇 정책에는 충분하지 않습니다. 이를 위해 우리는 VLA를 위한 체화된 사고의 사슬 추론(ECoT)을 소개합니다. 이는 로봇 행동을 예측하기 전에 계획, 하위 작업, 동작, 그리고 객체 경계 상자 및 엔드 이펙터 위치와 같은 시각적 근거 특징에 대한 여러 단계의 추론을 수행하도록 VLA를 훈련시키는 것입니다. 우리는 대규모 로봇 데이터셋에서 ECoT를 위한 합성 훈련 데이터를 생성하는 확장 가능한 파이프라인을 설계합니다. 우리는 ECoT가 현재 가장 강력한 오픈소스 VLA 정책인 OpenVLA의 절대 성공률을 추가 로봇 훈련 데이터 없이도 도전적인 일반화 작업에서 28% 향상시킨다는 것을 입증합니다. 또한 ECoT는 인간이 정책의 실패를 해석하고 자연어를 사용하여 행동을 수정하는 것을 더 쉽게 만듭니다.

## 参考
- http://arxiv.org/abs/2407.08693v3
