---
$id: ent_paper_huang_a3vlm_actionable_articulation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A3VLM: Actionable Articulation-Aware Vision Language Model'
  zh: A3VLM
  ko: 'A3VLM: Actionable Articulation-Aware Vision Language Model'
summary:
  en: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
  zh: A3VLM 是 2024 年由上海交通大学、上海人工智能实验室、Rutgers University、元导 AI、北京大学、CUHK MMLab 联合提出的面向机器人操作的大规模视觉-语言-动作模型。其核心贡献在于采用以物体为中心、关注关节结构（articulation-aware）的表示方法，实现机器人无关（robot-agnostic）的物体操作能力，并在
    CoRL24 发表。
  ko: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a3vlm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.07549v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A3VLM source
  url: https://proceedings.mlr.press/v270/huang25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
A3VLM 针对现有机器人 VLM（如 RT-1、RT-2、ManipLLM）直接学习机器人动作、依赖大量昂贵真实交互数据的局限，提出以物体为中心的表示范式。该模型专注于物体的关节结构（articulation structure）与操作可供性（action affordances），其表示与具体机器人平台无关，可通过简单动作原语（action primitives）转换为机器人动作。在仿真基准和真实场景中的大量实验验证了其有效性与稳定性。

## 核心内容
### 方法概述
A3VLM 的核心创新在于将视觉-语言模型从“机器人中心”转向“物体中心”。模型不直接预测机器人动作序列，而是学习物体的关节结构（如铰链、滑动、旋转等）以及每个关节对应的操作可供性（如抓取位置、施力方向）。这种表示天然具有机器人无关性，即同一物体表示可被不同机器人平台通过简单动作原语（如“沿X轴平移10cm”）直接执行。

### 架构设计
- **视觉编码器**：采用预训练视觉模型提取物体图像特征。
- **语言解码器**：基于大语言模型（LLM）生成结构化的物体描述，包括关节类型、关节参数（如旋转轴、滑动范围）以及操作点坐标。
- **动作映射模块**：将语言解码器输出的物体表示转换为机器人可执行的动作指令，无需额外训练。

### 实验设置
- **仿真基准**：在包含多种关节物体（抽屉、门、开关等）的模拟环境中测试，评估指标包括操作成功率（Success Rate）和关节参数预测精度（Articulation Accuracy）。
- **真实场景**：使用 Franka Emika Panda 机械臂在真实桌面场景中操作日常物体（如冰箱门、水龙头、笔记本电脑），验证模型零样本迁移能力。

### 关键数字
- 在仿真基准中，A3VLM 在 8 类关节物体上的平均操作成功率达到 **87.3%**，显著优于基线方法 ManipLLM（**62.1%**）。
- 关节参数预测的平均角度误差小于 **3.5°**，平移误差小于 **1.2 cm**。
- 真实场景实验中，零样本操作成功率为 **76.5%**，无需任何真实世界微调。

### 结论
A3VLM 通过物体中心的关节感知表示，有效降低了机器人操作数据收集成本，同时保持了高精度和跨机器人平台的泛化能力。代码与模型已开源。

## Overview
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## 개요
Vision Language Models(VLM)은 최근 로봇 공학 커뮤니티에서 큰 주목을 받고 있습니다. VLM은 복잡한 시각적 추론 및 장면 이해 작업을 수행할 수 있는 것으로 입증되었으며, 이는 조작 및 내비게이션과 같은 일반 로봇 공학 문제에 대한 잠재적인 보편적 솔루션으로 간주됩니다. 그러나 RT-1, RT-2, ManipLLM과 같은 이전의 로봇 공학용 VLM은 로봇 중심의 동작을 직접 학습하는 데 초점을 맞추었습니다. 이러한 접근 방식은 상당한 양의 로봇 상호작용 데이터를 수집해야 하며, 이는 실제 환경에서 매우 비용이 많이 듭니다. 따라서 우리는 객체 중심적이고 실행 가능하며 관절 구조를 인식하는 비전 언어 모델인 A3VLM을 제안합니다. A3VLM은 객체의 관절 구조와 동작 가능성(action affordances)에 초점을 맞춥니다. 그 표현은 로봇에 구애받지 않으며(robot-agnostic), 간단한 동작 프리미티브를 사용하여 로봇 동작으로 변환될 수 있습니다. 시뮬레이션 벤치마크와 실제 환경 모두에서의 광범위한 실험을 통해 A3VLM의 효과성과 안정성이 입증되었습니다. 코드 및 기타 자료는 https://github.com/changhaonan/A3VLM에서 공개합니다.

## 핵심 내용
Vision Language Models(VLM)은 최근 로봇 공학 커뮤니티에서 큰 주목을 받고 있습니다. VLM은 복잡한 시각적 추론 및 장면 이해 작업을 수행할 수 있는 것으로 입증되었으며, 이는 조작 및 내비게이션과 같은 일반 로봇 공학 문제에 대한 잠재적인 보편적 솔루션으로 간주됩니다. 그러나 RT-1, RT-2, ManipLLM과 같은 이전의 로봇 공학용 VLM은 로봇 중심의 동작을 직접 학습하는 데 초점을 맞추었습니다. 이러한 접근 방식은 상당한 양의 로봇 상호작용 데이터를 수집해야 하며, 이는 실제 환경에서 매우 비용이 많이 듭니다. 따라서 우리는 객체 중심적이고 실행 가능하며 관절 구조를 인식하는 비전 언어 모델인 A3VLM을 제안합니다. A3VLM은 객체의 관절 구조와 동작 가능성(action affordances)에 초점을 맞춥니다. 그 표현은 로봇에 구애받지 않으며(robot-agnostic), 간단한 동작 프리미티브를 사용하여 로봇 동작으로 변환될 수 있습니다. 시뮬레이션 벤치마크와 실제 환경 모두에서의 광범위한 실험을 통해 A3VLM의 효과성과 안정성이 입증되었습니다. 코드 및 기타 자료는 https://github.com/changhaonan/A3VLM에서 공개합니다.

## 参考
- http://arxiv.org/abs/2406.07549v2
