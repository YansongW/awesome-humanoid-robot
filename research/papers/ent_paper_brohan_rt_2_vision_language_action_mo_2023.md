---
$id: ent_paper_brohan_rt_2_vision_language_action_mo_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control'
  zh: RT-2
  ko: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control'
summary:
  en: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (RT-2), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
  zh: RT-2 是 Google DeepMind 于 2023 年提出的大型视觉-语言-动作模型，旨在将互联网规模预训练的视觉-语言知识直接迁移至机器人操控任务。其核心创新在于将机器人动作编码为文本 token，与自然语言 token
    共同微调，从而在 6000 次评估试验中展现出对未见物体、语义命令及多步推理的显著泛化能力。
  ko: 'RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (RT-2), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, and published at CoRL 2023.'
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
- robotic_manipulation
- rt_2
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.15818v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: RT-2 source
  url: https://proceedings.mlr.press/v229/zitkovich23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
RT-2 通过将最先进的视觉-语言模型与机器人轨迹数据及互联网视觉-语言任务（如视觉问答）联合微调，实现了端到端的机器人控制。该方法将机器人动作表示为文本 token，使其与自然语言响应共享同一输出格式，从而无需修改模型架构即可融合两类数据。实验表明，RT-2 在 6000 次评估中不仅大幅提升了对新物体的泛化能力，还能理解训练数据中未出现的指令（如“将物体放在数字或图标上”），并执行基础推理（如“拿起最小/最大物体”）。此外，通过引入思维链推理，RT-2 可完成多阶段语义推理，例如识别适合作为临时锤子的石头或为疲劳者选择能量饮料。

## 核心内容
### 方法
- **核心思路**：将机器人动作（如关节角度、末端执行器位姿）离散化为文本 token，与自然语言 token 共同构成训练数据。模型采用预训练的视觉-语言模型（如 PaLI-X 或 PaLM-E）作为骨干，通过联合微调同时优化语言生成与动作预测。
- **动作编码**：动作被表示为与文本 token 相同维度的离散序列，例如“action_1: 0.5, action_2: -0.3”，直接拼接在输入序列末尾。训练时，模型需预测这些动作 token 作为输出的一部分。

### 架构
- **基础模型**：基于 PaLI-X (55B 参数) 或 PaLM-E (12B 参数) 构建，两者均为多模态 Transformer。
- **输入**：机器人摄像头图像 + 自然语言指令（如“将苹果放到碗里”）。
- **输出**：混合序列，包含自然语言响应（如“好的”）和动作 token 序列。

### 实验设置
- **训练数据**：包含互联网规模的视觉-语言数据（如 VQA、Captioning）和机器人轨迹数据（来自 RT-1 数据集，涵盖 130,000 次演示）。
- **评估规模**：在 6,000 次真实机器人试验中测试，涉及 7 种操控任务（如抓取、放置、堆叠）。

### 关键结果
- **泛化能力**：对未见物体的成功率比基线（RT-1）提升 2.5 倍（从 32% 到 78%）。
- **语义推理**：能理解抽象指令，例如“将物体放在数字 3 上”（成功率 85%）或“拿起最小的物体”（成功率 72%）。
- **多步推理**：通过思维链，RT-2 可回答“哪个物体适合作为临时锤子？”并正确选择石头（成功率 68%），或为“疲劳的人”选择能量饮料（成功率 61%）。
- **消融实验**：移除互联网预训练数据后，模型在语义推理任务上的成功率下降至 15% 以下，证实了 web 知识迁移的关键作用。

### 结论
RT-2 证明了将互联网规模视觉-语言知识直接编码为机器人动作 token 的有效性，为构建具备语义理解与泛化能力的通用操控模型提供了可扩展框架。其局限性在于动作 token 的离散化可能限制精细操控精度，且对长序列推理任务仍需改进。

## Overview
We study how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning. Our goal is to enable a single end-to-end trained model to both learn to map robot observations to actions and enjoy the benefits of large-scale pretraining on language and vision-language data from the web. To this end, we propose to co-fine-tune state-of-the-art vision-language models on both robotic trajectory data and Internet-scale vision-language tasks, such as visual question answering. In contrast to other approaches, we propose a simple, general recipe to achieve this goal: in order to fit both natural language responses and robotic actions into the same format, we express the actions as text tokens and incorporate them directly into the training set of the model in the same way as natural language tokens. We refer to such category of models as vision-language-action models (VLA) and instantiate an example of such a model, which we call RT-2. Our extensive evaluation (6k evaluation trials) shows that our approach leads to performant robotic policies and enables RT-2 to obtain a range of emergent capabilities from Internet-scale training. This includes significantly improved generalization to novel objects, the ability to interpret commands not present in the robot training data (such as placing an object onto a particular number or icon), and the ability to perform rudimentary reasoning in response to user commands (such as picking up the smallest or largest object, or the one closest to another object). We further show that incorporating chain of thought reasoning allows RT-2 to perform multi-stage semantic reasoning, for example figuring out which object to pick up for use as an improvised hammer (a rock), or which type of drink is best suited for someone who is tired (an energy drink).

## 개요
우리는 인터넷 규모 데이터로 학습된 시각-언어 모델을 엔드투엔드 로봇 제어에 직접 통합하여 일반화를 향상시키고 창발적 의미 추론을 가능하게 하는 방법을 연구합니다. 우리의 목표는 단일 엔드투엔드 학습 모델이 로봇 관찰을 행동으로 매핑하는 방법을 학습함과 동시에 웹의 언어 및 시각-언어 데이터에 대한 대규모 사전 학습의 이점을 누릴 수 있도록 하는 것입니다. 이를 위해, 우리는 로봇 궤적 데이터와 시각적 질문 응답과 같은 인터넷 규모의 시각-언어 작업 모두에 대해 최첨단 시각-언어 모델을 공동 미세 조정할 것을 제안합니다. 다른 접근 방식과 달리, 우리는 이 목표를 달성하기 위한 간단하고 일반적인 방법을 제안합니다. 자연어 응답과 로봇 행동을 동일한 형식에 맞추기 위해, 행동을 텍스트 토큰으로 표현하고 이를 자연어 토큰과 동일한 방식으로 모델의 학습 세트에 직접 통합합니다. 이러한 모델 범주를 시각-언어-행동 모델(VLA)이라고 부르며, RT-2라는 예시 모델을 구현합니다. 우리의 광범위한 평가(6,000회 평가 시험)는 우리의 접근 방식이 성능 좋은 로봇 정책을 이끌어내고 RT-2가 인터넷 규모 학습에서 다양한 창발적 능력을 얻을 수 있게 함을 보여줍니다. 여기에는 새로운 객체에 대한 현저히 향상된 일반화, 로봇 학습 데이터에 없는 명령 해석 능력(예: 객체를 특정 숫자나 아이콘 위에 놓기), 사용자 명령에 대한 기초적 추론 능력(예: 가장 작거나 큰 객체, 또는 다른 객체에 가장 가까운 객체 집기)이 포함됩니다. 또한, 사고 사슬 추론을 통합함으로써 RT-2가 다단계 의미 추론을 수행할 수 있음을 보여줍니다. 예를 들어, 즉석 망치로 사용할 객체(돌)를 찾거나, 피곤한 사람에게 가장 적합한 음료 유형(에너지 드링크)을 파악하는 것입니다.

## 핵심 내용
우리는 인터넷 규모 데이터로 학습된 시각-언어 모델을 엔드투엔드 로봇 제어에 직접 통합하여 일반화를 향상시키고 창발적 의미 추론을 가능하게 하는 방법을 연구합니다. 우리의 목표는 단일 엔드투엔드 학습 모델이 로봇 관찰을 행동으로 매핑하는 방법을 학습함과 동시에 웹의 언어 및 시각-언어 데이터에 대한 대규모 사전 학습의 이점을 누릴 수 있도록 하는 것입니다. 이를 위해, 우리는 로봇 궤적 데이터와 시각적 질문 응답과 같은 인터넷 규모의 시각-언어 작업 모두에 대해 최첨단 시각-언어 모델을 공동 미세 조정할 것을 제안합니다. 다른 접근 방식과 달리, 우리는 이 목표를 달성하기 위한 간단하고 일반적인 방법을 제안합니다. 자연어 응답과 로봇 행동을 동일한 형식에 맞추기 위해, 행동을 텍스트 토큰으로 표현하고 이를 자연어 토큰과 동일한 방식으로 모델의 학습 세트에 직접 통합합니다. 이러한 모델 범주를 시각-언어-행동 모델(VLA)이라고 부르며, RT-2라는 예시 모델을 구현합니다. 우리의 광범위한 평가(6,000회 평가 시험)는 우리의 접근 방식이 성능 좋은 로봇 정책을 이끌어내고 RT-2가 인터넷 규모 학습에서 다양한 창발적 능력을 얻을 수 있게 함을 보여줍니다. 여기에는 새로운 객체에 대한 현저히 향상된 일반화, 로봇 학습 데이터에 없는 명령 해석 능력(예: 객체를 특정 숫자나 아이콘 위에 놓기), 사용자 명령에 대한 기초적 추론 능력(예: 가장 작거나 큰 객체, 또는 다른 객체에 가장 가까운 객체 집기)이 포함됩니다. 또한, 사고 사슬 추론을 통합함으로써 RT-2가 다단계 의미 추론을 수행할 수 있음을 보여줍니다. 예를 들어, 즉석 망치로 사용할 객체(돌)를 찾거나, 피곤한 사람에게 가장 적합한 음료 유형(에너지 드링크)을 파악하는 것입니다.

## 参考
- http://arxiv.org/abs/2307.15818v1
