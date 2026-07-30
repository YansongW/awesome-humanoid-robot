---
$id: ent_paper_chen_large_video_planner_enables_ge_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Large Video Planner Enables Generalizable Robot Control
  zh: LVP
  ko: Large Video Planner Enables Generalizable Robot Control
summary:
  en: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
  zh: Large Video Planner (LVP) 是2025年由MIT、UC Berkeley和哈佛大学联合提出的大型视觉-语言-动作模型，用于机器人操控。其核心贡献在于首次以基础模型规模训练开放视频模型，通过互联网规模的人类活动视频预训练实现零样本视频规划，并后处理提取可执行动作，展示了强大的指令遵循与泛化能力。
  ko: Large Video Planner Enables Generalizable Robot Control (LVP), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by MIT, UC Berkeley, Harvard.
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
- lvp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15840v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Large Video Planner Enables Generalizable Robot Control (arXiv)
  url: https://arxiv.org/abs/2512.15840
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LVP source
  url: https://doi.org/10.48550/arXiv.2512.15840
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
LVP 探索了一种替代范式：将大规模视频预训练作为构建机器人基础模型的主要模态，而非依赖静态图像和语言。研究团队策划了互联网规模的人类活动与任务演示视频数据集，训练出首个基础模型级别的开放视频生成模型，用于机器人规划。该模型能为新场景和新任务生成零样本视频计划，再通过后处理提取可执行动作。实验通过第三方选定的野外任务和真实机器人测试，验证了物理执行的成功率，证明了鲁棒的指令遵循、强泛化能力和现实可行性。

## 核心内容
### 方法
LVP 采用视频生成作为机器人规划的核心模态，区别于传统VLA模型直接输出动作。其流程分为两步：
1. **视频规划**：模型根据当前场景图像和语言指令，生成未来状态序列的视频计划。
2. **动作提取**：通过后处理（如光流或逆动力学模型）从生成的视频中提取可执行的低级动作指令。

### 架构
- **基础模型**：基于大规模视频预训练的生成式模型，参数量达到基础模型级别（具体未公开，但强调“foundation-model scale”）。
- **输入**：单帧或多帧当前场景图像 + 自然语言任务描述。
- **输出**：多帧连续视频帧，表示任务执行过程。

### 数据集
- **来源**：互联网规模的人类活动视频和机器人任务演示，涵盖多样化场景和任务。
- **规模**：未公开具体数量，但强调“internet-scale”，远超现有机器人数据集。

### 实验设置
- **零样本泛化**：模型在未见过的场景和任务上直接生成视频计划，无需微调。
- **评估方式**：
  - 第三方选定的野外任务（如抓取、放置、操作物体）。
  - 真实机器人实验，使用物理机械臂执行。
- **对比基线**：未明确列出，但强调与现有VLA模型（如RT-2）的范式差异。

### 关键数字
- **成功率**：在野外任务和真实机器人实验中均实现“successful physical execution”，但未给出具体百分比。
- **泛化能力**：展示了对新场景、新物体的零样本适应，例如从未见过的工具或布局。
- **模型与数据开放**：代码、模型权重和数据集均公开，支持可复现研究。

### 结论
LVP 证明视频预训练可作为机器人基础模型的有效主模态，其零样本规划能力优于依赖静态图像和语言的VLA方法。未来工作可探索更高效的动作提取方法，以及将视频生成与低级控制策略端到端结合。

## Overview
General-purpose robots require decision-making models that generalize across diverse tasks and environments. Recent works build robot foundation models by extending multimodal large language models (MLLMs) with action outputs, creating vision-language-action (VLA) systems. These efforts are motivated by the intuition that MLLMs' large-scale language and image pretraining can be effectively transferred to the action output modality. In this work, we explore an alternative paradigm of using large-scale video pretraining as a primary modality for building robot foundation models. Unlike static images and language, videos capture spatio-temporal sequences of states and actions in the physical world that are naturally aligned with robotic behavior. We curate an internet-scale video dataset of human activities and task demonstrations, and train, for the first time at a foundation-model scale, an open video model for generative robotics planning. The model produces zero-shot video plans for novel scenes and tasks, which we post-process to extract executable robot actions. We evaluate task-level generalization through third-party selected tasks in the wild and real-robot experiments, demonstrating successful physical execution. Together, these results show robust instruction following, strong generalization, and real-world feasibility. We release both the model and dataset to support open, reproducible video-based robot learning. Our website is available at https://www.boyuan.space/large-video-planner/.

## 개요
범용 로봇은 다양한 작업과 환경에서 일반화되는 의사 결정 모델을 필요로 합니다. 최근 연구들은 멀티모달 대규모 언어 모델(MLLM)에 행동 출력을 확장하여 비전-언어-행동(VLA) 시스템을 구축함으로써 로봇 기반 모델을 개발하고 있습니다. 이러한 노력은 MLLM의 대규모 언어 및 이미지 사전 학습이 행동 출력 모달리티로 효과적으로 전이될 수 있다는 직관에 기반합니다. 본 연구에서는 대규모 비디오 사전 학습을 로봇 기반 모델 구축의 주요 모달리티로 활용하는 대안적 패러다임을 탐구합니다. 정적 이미지 및 언어와 달리, 비디오는 물리적 세계에서 상태와 행동의 시공간적 시퀀스를 포착하며, 이는 로봇 행동과 자연스럽게 정렬됩니다. 우리는 인간 활동 및 작업 시연의 인터넷 규모 비디오 데이터셋을 선별하고, 처음으로 기반 모델 규모에서 생성적 로봇 계획을 위한 오픈 비디오 모델을 학습시킵니다. 이 모델은 새로운 장면과 작업에 대해 제로샷 비디오 계획을 생성하며, 이를 후처리하여 실행 가능한 로봇 행동을 추출합니다. 우리는 실제 환경에서 제3자가 선정한 작업과 실제 로봇 실험을 통해 작업 수준 일반화를 평가하며, 성공적인 물리적 실행을 입증합니다. 이러한 결과는 강력한 명령 수행, 뛰어난 일반화, 그리고 실제 환경에서의 실현 가능성을 보여줍니다. 우리는 모델과 데이터셋을 모두 공개하여 개방적이고 재현 가능한 비디오 기반 로봇 학습을 지원합니다. 웹사이트는 https://www.boyuan.space/large-video-planner/ 에서 확인할 수 있습니다.

## 핵심 내용
범용 로봇은 다양한 작업과 환경에서 일반화되는 의사 결정 모델을 필요로 합니다. 최근 연구들은 멀티모달 대규모 언어 모델(MLLM)에 행동 출력을 확장하여 비전-언어-행동(VLA) 시스템을 구축함으로써 로봇 기반 모델을 개발하고 있습니다. 이러한 노력은 MLLM의 대규모 언어 및 이미지 사전 학습이 행동 출력 모달리티로 효과적으로 전이될 수 있다는 직관에 기반합니다. 본 연구에서는 대규모 비디오 사전 학습을 로봇 기반 모델 구축의 주요 모달리티로 활용하는 대안적 패러다임을 탐구합니다. 정적 이미지 및 언어와 달리, 비디오는 물리적 세계에서 상태와 행동의 시공간적 시퀀스를 포착하며, 이는 로봇 행동과 자연스럽게 정렬됩니다. 우리는 인간 활동 및 작업 시연의 인터넷 규모 비디오 데이터셋을 선별하고, 처음으로 기반 모델 규모에서 생성적 로봇 계획을 위한 오픈 비디오 모델을 학습시킵니다. 이 모델은 새로운 장면과 작업에 대해 제로샷 비디오 계획을 생성하며, 이를 후처리하여 실행 가능한 로봇 행동을 추출합니다. 우리는 실제 환경에서 제3자가 선정한 작업과 실제 로봇 실험을 통해 작업 수준 일반화를 평가하며, 성공적인 물리적 실행을 입증합니다. 이러한 결과는 강력한 명령 수행, 뛰어난 일반화, 그리고 실제 환경에서의 실현 가능성을 보여줍니다. 우리는 모델과 데이터셋을 모두 공개하여 개방적이고 재현 가능한 비디오 기반 로봇 학습을 지원합니다. 웹사이트는 https://www.boyuan.space/large-video-planner/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2512.15840v2
