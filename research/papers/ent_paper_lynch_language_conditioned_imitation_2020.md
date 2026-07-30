---
$id: ent_paper_lynch_language_conditioned_imitation_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Language Conditioned Imitation Learning over Unstructured Data
  zh: MCIL
  ko: Language Conditioned Imitation Learning over Unstructured Data
summary:
  en: Language Conditioned Imitation Learning over Unstructured Data (MCIL), is a 2020 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at RSS 2021.
  zh: MCIL 是 Google Robotics 于 2020 年提出的通用视觉-语言-动作模型，发表于 RSS 2021。其核心贡献在于将自由形式自然语言条件引入模仿学习，并能在无标签、非结构化的演示数据上训练，将语言标注成本降至总数据的
    1% 以下。该模型通过端到端神经网络同时学习像素感知、语言理解和多任务连续控制，在 3D 环境中仅凭自然语言描述即可执行多种机器人操作技能。
  ko: Language Conditioned Imitation Learning over Unstructured Data (MCIL), is a 2020 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at RSS 2021.
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
- mcil
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2005.07648v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: MCIL source
  url: https://doi.org/10.1109/LRA.2022.3196123
  date: '2020'
  accessed_at: '2026-07-01'
---
## 概述
MCIL 解决了传统模仿学习需要任务 ID 或目标图像、而指令跟随方法又受限于结构化假设的问题。该方法将自由形式自然语言条件融入模仿学习，通过端到端神经网络同时学习像素感知、语言理解和多任务连续控制。其关键创新在于能够利用无标签、非结构化的演示数据（即无任务或语言标签），从而将语言标注成本降至总数据的 1% 以下。在测试时，单个语言条件视觉运动策略仅凭自然语言描述（如“打开抽屉...现在拿起积木...现在按下绿色按钮...”）即可在 3D 环境中执行多种机器人操作技能。此外，通过结合文本条件策略与大型预训练神经语言模型，MCIL 能够对大量分布外的同义指令保持鲁棒性，而无需新的演示数据。

## 核心内容
### 方法概述
MCIL 提出了一种将自由形式自然语言条件融入模仿学习的方法。与以往需要任务 ID 或目标图像的模仿学习不同，MCIL 能够处理非结构化的演示数据，即无需为每个演示提供任务或语言标签。该方法通过端到端训练一个单一的神经网络，同时学习从像素中感知环境、理解自然语言以及执行多任务连续控制。

### 核心创新
- **利用非结构化数据**：MCIL 能够从无标签、非结构化的演示数据中学习，这显著提升了语言条件性能，同时将语言标注成本降低到总数据的 1% 以下。
- **端到端学习**：模型将感知、语言理解和控制整合为一个统一的神经网络，避免了分阶段训练带来的误差累积。
- **语言条件策略**：在测试时，单个语言条件视觉运动策略可以仅通过自然语言描述（例如“打开抽屉...现在拿起积木...现在按下绿色按钮...”）在 3D 环境中执行多种机器人操作技能。

### 扩展能力
为了扩展智能体能够遵循的指令数量，MCIL 提出将文本条件策略与大型预训练神经语言模型相结合。这种方法使得策略能够对大量分布外的同义指令保持鲁棒性，而无需为每个新指令提供新的演示数据。

### 实验设置与结果
- **环境**：在 3D 环境中进行实验，涉及多种机器人操作技能。
- **数据**：使用了非结构化的演示数据，语言标注仅占全部数据的 1%。
- **性能**：实验表明，MCIL 在语言条件模仿学习任务上表现优异，能够泛化到未见过的指令变体。

### 结论
MCIL 通过将自由形式自然语言条件引入模仿学习，并利用非结构化数据，显著降低了语言标注成本，同时提升了策略的泛化能力。结合预训练语言模型进一步增强了其对同义指令的鲁棒性，为机器人操作任务提供了更灵活、更实用的解决方案。

## Overview
Natural language is perhaps the most flexible and intuitive way for humans to communicate tasks to a robot. Prior work in imitation learning typically requires each task be specified with a task id or goal image -- something that is often impractical in open-world environments. On the other hand, previous approaches in instruction following allow agent behavior to be guided by language, but typically assume structure in the observations, actuators, or language that limit their applicability to complex settings like robotics. In this work, we present a method for incorporating free-form natural language conditioning into imitation learning. Our approach learns perception from pixels, natural language understanding, and multitask continuous control end-to-end as a single neural network. Unlike prior work in imitation learning, our method is able to incorporate unlabeled and unstructured demonstration data (i.e. no task or language labels). We show this dramatically improves language conditioned performance, while reducing the cost of language annotation to less than 1% of total data. At test time, a single language conditioned visuomotor policy trained with our method can perform a wide variety of robotic manipulation skills in a 3D environment, specified only with natural language descriptions of each task (e.g. "open the drawer...now pick up the block...now press the green button..."). To scale up the number of instructions an agent can follow, we propose combining text conditioned policies with large pretrained neural language models. We find this allows a policy to be robust to many out-of-distribution synonym instructions, without requiring new demonstrations. See videos of a human typing live text commands to our agent at language-play.github.io

## 개요
자연어는 인간이 로봇에게 작업을 전달하는 가장 유연하고 직관적인 방법일 것입니다. 모방 학습(imitation learning)의 기존 연구는 일반적으로 각 작업을 작업 ID나 목표 이미지로 지정해야 하는데, 이는 개방형 환경에서 종종 비실용적입니다. 반면, 명령 수행(instruction following)의 이전 접근법은 언어로 에이전트의 행동을 안내할 수 있지만, 일반적으로 관찰, 액추에이터 또는 언어의 구조를 가정하여 로봇 공학과 같은 복잡한 환경에 적용하기 어렵습니다. 본 연구에서는 자유 형식의 자연어 조건을 모방 학습에 통합하는 방법을 제시합니다. 우리의 접근법은 픽셀에서의 지각, 자연어 이해, 그리고 다중 작업 연속 제어를 단일 신경망으로 종단간(end-to-end) 학습합니다. 모방 학습의 기존 연구와 달리, 우리의 방법은 레이블이 없고 구조화되지 않은 시연 데이터(즉, 작업 또는 언어 레이블이 없는 데이터)를 통합할 수 있습니다. 이를 통해 언어 조건 성능이 극적으로 향상되며, 언어 주석 비용을 전체 데이터의 1% 미만으로 줄일 수 있음을 보여줍니다. 테스트 시, 우리의 방법으로 훈련된 단일 언어 조건 시각운동 정책(visuomotor policy)은 각 작업의 자연어 설명(예: "서랍을 열어... 이제 블록을 집어... 이제 초록색 버튼을 눌러...")만으로 3D 환경에서 다양한 로봇 조작 기술을 수행할 수 있습니다. 에이전트가 따를 수 있는 명령의 수를 확장하기 위해, 텍스트 조건 정책을 대규모 사전 훈련된 신경 언어 모델과 결합하는 것을 제안합니다. 이를 통해 새로운 시연 없이도 많은 분포 외 동의어 명령에 대해 정책이 강건해짐을 발견했습니다. 인간이 우리 에이전트에게 실시간 텍스트 명령을 입력하는 비디오는 language-play.github.io에서 확인할 수 있습니다.

## 핵심 내용
자연어는 인간이 로봇에게 작업을 전달하는 가장 유연하고 직관적인 방법일 것입니다. 모방 학습의 기존 연구는 일반적으로 각 작업을 작업 ID나 목표 이미지로 지정해야 하는데, 이는 개방형 환경에서 종종 비실용적입니다. 반면, 명령 수행의 이전 접근법은 언어로 에이전트의 행동을 안내할 수 있지만, 일반적으로 관찰, 액추에이터 또는 언어의 구조를 가정하여 로봇 공학과 같은 복잡한 환경에 적용하기 어렵습니다. 본 연구에서는 자유 형식의 자연어 조건을 모방 학습에 통합하는 방법을 제시합니다. 우리의 접근법은 픽셀에서의 지각, 자연어 이해, 그리고 다중 작업 연속 제어를 단일 신경망으로 종단간 학습합니다. 모방 학습의 기존 연구와 달리, 우리의 방법은 레이블이 없고 구조화되지 않은 시연 데이터(즉, 작업 또는 언어 레이블이 없는 데이터)를 통합할 수 있습니다. 이를 통해 언어 조건 성능이 극적으로 향상되며, 언어 주석 비용을 전체 데이터의 1% 미만으로 줄일 수 있음을 보여줍니다. 테스트 시, 우리의 방법으로 훈련된 단일 언어 조건 시각운동 정책은 각 작업의 자연어 설명(예: "서랍을 열어... 이제 블록을 집어... 이제 초록색 버튼을 눌러...")만으로 3D 환경에서 다양한 로봇 조작 기술을 수행할 수 있습니다. 에이전트가 따를 수 있는 명령의 수를 확장하기 위해, 텍스트 조건 정책을 대규모 사전 훈련된 신경 언어 모델과 결합하는 것을 제안합니다. 이를 통해 새로운 시연 없이도 많은 분포 외 동의어 명령에 대해 정책이 강건해짐을 발견했습니다. 인간이 우리 에이전트에게 실시간 텍스트 명령을 입력하는 비디오는 language-play.github.io에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2005.07648v2
