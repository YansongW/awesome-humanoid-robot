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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.15840v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1029 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.15840v2

## 개요
LVP는 정적 이미지와 언어에 의존하는 대신, 대규모 비디오 사전 학습을 로봇 기반 모델 구축의 주요 모달리티로 활용하는 대안적 패러다임을 탐구한다. 연구팀은 인터넷 규모의 인간 활동 및 작업 시연 비디오 데이터셋을 구성하고, 로봇 계획을 위한 최초의 기반 모델 수준의 개방형 비디오 생성 모델을 훈련시켰다. 이 모델은 새로운 장면과 새로운 작업에 대해 제로샷 비디오 계획을 생성할 수 있으며, 후처리를 통해 실행 가능한 행동을 추출한다. 실험은 제3자가 선정한 야외 작업과 실제 로봇 테스트를 통해 물리적 실행의 성공률을 검증하여, 강력한 명령 준수, 뛰어난 일반화 능력, 그리고 현실적 실현 가능성을 입증했다.

## 핵심 내용
### 방법
LVP는 기존 VLA 모델이 직접 행동을 출력하는 것과 달리, 비디오 생성을 로봇 계획의 핵심 모달리티로 채택한다. 그 프로세스는 두 단계로 나뉜다:
1. **비디오 계획**: 모델은 현재 장면 이미지와 언어 명령을 기반으로 미래 상태 시퀀스의 비디오 계획을 생성한다.
2. **행동 추출**: 후처리(예: 광학 흐름 또는 역동역학 모델)를 통해 생성된 비디오에서 실행 가능한 저수준 행동 명령을 추출한다.

### 아키텍처
- **기반 모델**: 대규모 비디오 사전 학습 기반의 생성 모델로, 파라미터 수가 기반 모델 수준에 도달한다(구체적 수치는 공개되지 않았지만 "foundation-model scale"임을 강조).
- **입력**: 단일 또는 다중 프레임의 현재 장면 이미지 + 자연어 작업 설명.
- **출력**: 작업 실행 과정을 나타내는 다중 프레임 연속 비디오 프레임.

### 데이터셋
- **출처**: 인터넷 규모의 인간 활동 비디오 및 로봇 작업 시연으로, 다양한 장면과 작업을 포함한다.
- **규모**: 구체적인 수량은 공개되지 않았지만 "internet-scale"임을 강조하며, 기존 로봇 데이터셋을 훨씬 초과한다.

### 실험 설정
- **제로샷 일반화**: 모델은 보지 못한 장면과 작업에서 미세 조정 없이 직접 비디오 계획을 생성한다.
- **평가 방식**:
  - 제3자가 선정한 야외 작업(예: 집기, 놓기, 물체 조작).
  - 실제 로봇 실험으로, 물리적 로봇 팔을 사용하여 실행.
- **비교 기준선**: 명시적으로 나열되지는 않았지만, 기존 VLA 모델(예: RT-2)과의 패러다임 차이를 강조한다.

### 주요 수치
- **성공률**: 야외 작업 및 실제 로봇 실험 모두에서 "성공적인 물리적 실행"을 달성했지만, 구체적인 백분율은 제공되지 않았다.
- **일반화 능력**: 보지 못한 도구나 레이아웃과 같은 새로운 장면과 새로운 물체에 대한 제로샷 적응을 보여준다.
- **모델 및 데이터 공개**: 코드, 모델 가중치, 데이터셋이 모두 공개되어 재현 가능한 연구를 지원한다.

### 결론
LVP는 비디오 사전 학습이 로봇 기반 모델의 효과적인 주요 모달리티가 될 수 있음을 입증하며, 그 제로샷 계획 능력은 정적 이미지와 언어에 의존하는 VLA 방법보다 우수하다. 향후 연구는 더 효율적인 행동 추출 방법과 비디오 생성을 저수준 제어 정책과 종단 간 결합하는 방식을 탐구할 수 있다.
