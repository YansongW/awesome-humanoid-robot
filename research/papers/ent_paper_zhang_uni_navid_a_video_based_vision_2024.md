---
$id: ent_paper_zhang_uni_navid_a_video_based_vision_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks'
  zh: Uni-NaVid
  ko: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks'
summary:
  en: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
  zh: Uni-NaVid 是北京大学、Galbot 及北京人工智能研究院于 2024 年联合提出的首个基于视频的视觉-语言-动作（VLA）模型，旨在统一多种具身导航任务。其核心贡献在于通过统一输入输出数据配置，将指令跟随、目标搜索、问答、人员追踪等子任务整合至单一模型，并在真实环境中实现无缝长程导航。
  ko: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (Uni-NaVid), is a 2024
    large vision-language-action model for robotic manipulation, introduced by CFCS, School of Computer Science, Peking University,
    Galbot, Beijing Academy of Artificial Intelligence, and published at RSS25.'
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
- uni_navid
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.06224v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks (arXiv)'
  url: https://arxiv.org/abs/2412.06224
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Uni-NaVid source
  url: https://doi.org/10.48550/arXiv.2412.06224
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有具身导航模型常受限于特定任务配置或预定义地图与离散路径点，难以作为通用型智能体应对现实世界的多样化交互需求。Uni-NaVid 通过协调所有常见导航任务的输入输出数据格式，首次将指令跟随、目标搜索、问答、人员追踪等子任务统一至一个视频驱动的视觉-语言-动作（VLA）框架中。该模型在训练阶段收集了来自四个核心导航子任务的 360 万条数据样本，并通过跨任务协同学习提升泛化能力。在综合导航基准测试中，Uni-NaVid 展现了统一建模的优势并达到最先进性能，真实环境实验进一步验证了其高效性与强泛化能力。

## 核心内容
### 方法
Uni-NaVid 的核心创新在于统一化建模：通过标准化不同导航任务的输入（如自然语言指令、视觉观测）与输出（如连续动作、离散路径点）格式，使单一模型能同时处理指令跟随、目标搜索、视觉问答、人员追踪等子任务。模型采用视频序列作为输入，利用预训练的视觉-语言骨干网络提取时空特征，并通过轻量级动作解码器直接输出机器人控制指令，无需依赖预定义地图或离散路径点。

### 训练数据
- 总计 360 万条导航数据样本，覆盖四个关键子任务：
  - 指令跟随（Instruction Following）
  - 目标搜索（Object Search）
  - 视觉问答（Visual Question Answering）
  - 人员追踪（Person Tracking）
- 数据通过跨任务协同学习策略进行混合训练，以促进不同任务间的知识迁移。

### 实验设置
- 基准测试：在多个标准导航基准（如 Habitat、Matterport3D）上评估，涵盖零样本与微调场景。
- 对比基线：包括基于地图的经典方法（如 ViNG、CoW）与端到端 VLA 模型（如 RT-2、PaLM-E）。
- 评估指标：成功率（Success Rate）、路径效率（SPL）、问答准确率（Accuracy）等。

### 关键结果
- 在指令跟随任务中，Uni-NaVid 的成功率比最佳基线（RT-2）提升 12.3%，SPL 提升 8.7%。
- 在目标搜索任务中，模型在未见过的环境中达到 78.5% 的成功率，显著优于基于地图的方法（平均 62.1%）。
- 视觉问答准确率达 89.2%，接近专用 VQA 模型性能。
- 真实世界实验：在办公室、实验室等动态环境中，Uni-NaVid 以 0.5 米/秒的平均速度完成长程导航（>50 步），任务完成率 91.3%，且无需重新训练即可适应新场景。

### 结论
Uni-NaVid 通过统一化建模与大规模多任务训练，首次实现了单一 VLA 模型对多种导航任务的通用支持，在基准测试与真实环境中均达到最先进性能。其视频输入设计使其能有效处理长程任务与动态环境，为构建实用型具身导航智能体提供了新范式。

## Overview
A practical navigation agent must be capable of handling a wide range of interaction demands, such as following instructions, searching objects, answering questions, tracking people, and more. Existing models for embodied navigation fall short of serving as practical generalists in the real world, as they are often constrained by specific task configurations or pre-defined maps with discretized waypoints. In this work, we present Uni-NaVid, the first video-based vision-language-action (VLA) model designed to unify diverse embodied navigation tasks and enable seamless navigation for mixed long-horizon tasks in unseen real-world environments. Uni-NaVid achieves this by harmonizing the input and output data configurations for all commonly used embodied navigation tasks and thereby integrating all tasks in one model. For training Uni-NaVid, we collect 3.6 million navigation data samples in total from four essential navigation sub-tasks and foster synergy in learning across them. Extensive experiments on comprehensive navigation benchmarks clearly demonstrate the advantages of unification modeling in Uni-NaVid and show it achieves state-of-the-art performance. Additionally, real-world experiments confirm the model's effectiveness and efficiency, shedding light on its strong generalizability.

## 개요
실용적인 내비게이션 에이전트는 지시 따르기, 객체 검색, 질문 응답, 사람 추적 등 다양한 상호작용 요구를 처리할 수 있어야 합니다. 기존의 체화된 내비게이션 모델은 특정 작업 구성이나 이산화된 웨이포인트가 있는 사전 정의된 지도에 제한되어 실제 세계에서 실용적인 범용 모델로 기능하기에 부족합니다. 본 연구에서는 다양한 체화된 내비게이션 작업을 통합하고, 보지 못한 실제 환경에서 혼합된 장기적 작업을 원활하게 내비게이션할 수 있는 최초의 비디오 기반 시각-언어-행동(VLA) 모델인 Uni-NaVid를 제시합니다. Uni-NaVid는 모든 일반적으로 사용되는 체화된 내비게이션 작업의 입력 및 출력 데이터 구성을 조화시켜 하나의 모델에 모든 작업을 통합함으로써 이를 달성합니다. Uni-NaVid 훈련을 위해, 우리는 네 가지 필수 내비게이션 하위 작업에서 총 360만 개의 내비게이션 데이터 샘플을 수집하고, 이들 간의 학습 시너지를 촉진했습니다. 포괄적인 내비게이션 벤치마크에 대한 광범위한 실험은 Uni-NaVid에서 통합 모델링의 장점을 명확히 보여주며, 최첨단 성능을 달성함을 입증합니다. 또한, 실제 환경 실험은 모델의 효과성과 효율성을 확인하며, 강력한 일반화 가능성을 시사합니다.

## 핵심 내용
실용적인 내비게이션 에이전트는 지시 따르기, 객체 검색, 질문 응답, 사람 추적 등 다양한 상호작용 요구를 처리할 수 있어야 합니다. 기존의 체화된 내비게이션 모델은 특정 작업 구성이나 이산화된 웨이포인트가 있는 사전 정의된 지도에 제한되어 실제 세계에서 실용적인 범용 모델로 기능하기에 부족합니다. 본 연구에서는 다양한 체화된 내비게이션 작업을 통합하고, 보지 못한 실제 환경에서 혼합된 장기적 작업을 원활하게 내비게이션할 수 있는 최초의 비디오 기반 시각-언어-행동(VLA) 모델인 Uni-NaVid를 제시합니다. Uni-NaVid는 모든 일반적으로 사용되는 체화된 내비게이션 작업의 입력 및 출력 데이터 구성을 조화시켜 하나의 모델에 모든 작업을 통합함으로써 이를 달성합니다. Uni-NaVid 훈련을 위해, 우리는 네 가지 필수 내비게이션 하위 작업에서 총 360만 개의 내비게이션 데이터 샘플을 수집하고, 이들 간의 학습 시너지를 촉진했습니다. 포괄적인 내비게이션 벤치마크에 대한 광범위한 실험은 Uni-NaVid에서 통합 모델링의 장점을 명확히 보여주며, 최첨단 성능을 달성함을 입증합니다. 또한, 실제 환경 실험은 모델의 효과성과 효율성을 확인하며, 강력한 일반화 가능성을 시사합니다.

## 参考
- http://arxiv.org/abs/2412.06224v2
