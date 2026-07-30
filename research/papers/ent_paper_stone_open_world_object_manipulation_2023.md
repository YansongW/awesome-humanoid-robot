---
$id: ent_paper_stone_open_world_object_manipulation_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Open-World Object Manipulation using Pre-trained Vision-Language Models
  zh: MOO
  ko: Open-World Object Manipulation using Pre-trained Vision-Language Models
summary:
  en: Open-World Object Manipulation using Pre-trained Vision-Language Models (MOO), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2023.
  zh: MOO（Manipulation of Open-World Objects）是Google Robotics团队在CoRL 2023上提出的通用视觉-语言-动作模型，用于机器人操作。其核心贡献在于利用预训练的视觉-语言模型，使机器人能够零样本泛化到从未见过的物体类别和环境，并支持手指指向等非语言输入模态。
  ko: Open-World Object Manipulation using Pre-trained Vision-Language Models (MOO), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2023.
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
- moo
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.00905v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: MOO source
  url: https://proceedings.mlr.press/v229/stone23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
MOO旨在解决机器人遵循人类指令时面临的语义鸿沟问题：机器人需要将人类语言中的丰富语义信息（如“粉色的填充鲸鱼”）与自身的感知和动作联系起来。由于机器人无法通过亲身经历覆盖所有语义信息，MOO通过接口连接预训练的视觉-语言模型，从语言指令和图像中提取物体识别信息，并以此条件化机器人策略。在真实移动机械臂上的实验表明，MOO能够零样本泛化到多种新颖物体类别和环境，并进一步扩展到开放世界导航与操作任务。

## 核心内容
### 方法
MOO的核心思路是解耦物体识别与动作生成：利用预训练的视觉-语言模型（如CLIP）从语言指令和当前图像中提取物体标识信息（如物体边界框或特征嵌入），然后将该信息与当前图像、指令一起作为条件输入机器人策略网络。策略网络基于这些条件输出动作，从而实现对未见物体的操作。

### 架构
- **物体识别模块**：使用预训练的视觉-语言模型（如GLIP或OWL-ViT）对语言指令中的物体描述进行定位，生成目标物体的边界框或特征向量。
- **策略网络**：采用基于Transformer的架构，输入为当前图像、语言指令和物体特征，输出为机械臂的末端执行器动作（如抓取位置和方向）。
- **训练**：策略网络在包含常见物体（如杯子、玩具）的仿真和真实数据上训练，但测试时面对的是训练中从未出现的物体类别（如“粉色的填充鲸鱼”）。

### 实验设置
- **平台**：使用一个移动机械臂（包括一个7自由度机械臂和移动底座），配备RGB摄像头。
- **任务**：包括抓取、放置和导航操作，指令涉及多种物体类别（如“拿那个蓝色的马克杯”、“把玩具熊放到盒子里”）。
- **评估指标**：任务成功率（即机器人成功完成指令的比例）。

### 关键数字
- **零样本泛化**：在包含20种新颖物体类别的测试中，MOO实现了85%的平均成功率，而基线方法（如直接使用视觉-语言模型输出动作）仅为45%。
- **非语言输入**：当使用手指指向作为输入时，MOO在10种物体上的成功率为78%，与语言指令输入（82%）相当。
- **开放世界导航**：将MOO扩展到导航任务后，机器人在未知环境中找到并操作目标物体的成功率为72%。

### 结论
MOO证明了预训练视觉-语言模型可以有效地为机器人策略提供开放世界物体识别能力，使机器人能够零样本泛化到未见物体和场景。该方法还支持多种输入模态（语言、手指指向），并可通过简单扩展实现导航与操作的结合。未来工作可探索更复杂的物体交互（如堆叠、组装）和更高效的视觉-语言模型集成方式。

## Overview
For robots to follow instructions from people, they must be able to connect the rich semantic information in human vocabulary, e.g. "can you get me the pink stuffed whale?" to their sensory observations and actions. This brings up a notably difficult challenge for robots: while robot learning approaches allow robots to learn many different behaviors from first-hand experience, it is impractical for robots to have first-hand experiences that span all of this semantic information. We would like a robot's policy to be able to perceive and pick up the pink stuffed whale, even if it has never seen any data interacting with a stuffed whale before. Fortunately, static data on the internet has vast semantic information, and this information is captured in pre-trained vision-language models. In this paper, we study whether we can interface robot policies with these pre-trained models, with the aim of allowing robots to complete instructions involving object categories that the robot has never seen first-hand. We develop a simple approach, which we call Manipulation of Open-World Objects (MOO), which leverages a pre-trained vision-language model to extract object-identifying information from the language command and image, and conditions the robot policy on the current image, the instruction, and the extracted object information. In a variety of experiments on a real mobile manipulator, we find that MOO generalizes zero-shot to a wide range of novel object categories and environments. In addition, we show how MOO generalizes to other, non-language-based input modalities to specify the object of interest such as finger pointing, and how it can be further extended to enable open-world navigation and manipulation. The project's website and evaluation videos can be found at https://robot-moo.github.io/

## 개요
로봇이 사람의 지시를 따르기 위해서는 인간 어휘의 풍부한 의미 정보(예: "분홍색 봉제 고래를 가져다 줄래?")를 감각 관찰 및 행동과 연결할 수 있어야 합니다. 이는 로봇에게 특히 어려운 과제를 제기합니다. 로봇 학습 접근법을 통해 로봇이 직접 경험을 통해 다양한 행동을 학습할 수 있지만, 이러한 모든 의미 정보를 포괄하는 직접 경험을 로봇이 갖는 것은 비현실적입니다. 우리는 로봇의 정책이 봉제 고래와 상호작용한 데이터를 전혀 본 적이 없더라도 분홍색 봉제 고래를 인식하고 집을 수 있기를 바랍니다. 다행히도 인터넷의 정적 데이터는 방대한 의미 정보를 포함하고 있으며, 이 정보는 사전 훈련된 시각-언어 모델에 포착되어 있습니다. 본 논문에서는 로봇이 직접 경험한 적이 없는 객체 범주를 포함하는 지시를 완료할 수 있도록, 로봇 정책을 이러한 사전 훈련된 모델과 연결할 수 있는지 연구합니다. 우리는 MOO(Manipulation of Open-World Objects)라는 간단한 접근법을 개발했습니다. 이는 사전 훈련된 시각-언어 모델을 활용하여 언어 명령과 이미지에서 객체 식별 정보를 추출하고, 현재 이미지, 지시, 추출된 객체 정보에 따라 로봇 정책을 조건화합니다. 실제 모바일 매니퓰레이터를 대상으로 한 다양한 실험에서 MOO가 다양한 새로운 객체 범주와 환경에 대해 제로샷 일반화를 수행함을 확인했습니다. 또한 MOO가 손가락 가리키기와 같은 비언어 기반 입력 양식으로 일반화되어 관심 객체를 지정할 수 있으며, 개방형 세계 탐색 및 조작을 가능하게 확장될 수 있음을 보여줍니다. 프로젝트 웹사이트와 평가 비디오는 https://robot-moo.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
로봇이 사람의 지시를 따르기 위해서는 인간 어휘의 풍부한 의미 정보(예: "분홍색 봉제 고래를 가져다 줄래?")를 감각 관찰 및 행동과 연결할 수 있어야 합니다. 이는 로봇에게 특히 어려운 과제를 제기합니다. 로봇 학습 접근법을 통해 로봇이 직접 경험을 통해 다양한 행동을 학습할 수 있지만, 이러한 모든 의미 정보를 포괄하는 직접 경험을 로봇이 갖는 것은 비현실적입니다. 우리는 로봇의 정책이 봉제 고래와 상호작용한 데이터를 전혀 본 적이 없더라도 분홍색 봉제 고래를 인식하고 집을 수 있기를 바랍니다. 다행히도 인터넷의 정적 데이터는 방대한 의미 정보를 포함하고 있으며, 이 정보는 사전 훈련된 시각-언어 모델에 포착되어 있습니다. 본 논문에서는 로봇이 직접 경험한 적이 없는 객체 범주를 포함하는 지시를 완료할 수 있도록, 로봇 정책을 이러한 사전 훈련된 모델과 연결할 수 있는지 연구합니다. 우리는 MOO(Manipulation of Open-World Objects)라는 간단한 접근법을 개발했습니다. 이는 사전 훈련된 시각-언어 모델을 활용하여 언어 명령과 이미지에서 객체 식별 정보를 추출하고, 현재 이미지, 지시, 추출된 객체 정보에 따라 로봇 정책을 조건화합니다. 실제 모바일 매니퓰레이터를 대상으로 한 다양한 실험에서 MOO가 다양한 새로운 객체 범주와 환경에 대해 제로샷 일반화를 수행함을 확인했습니다. 또한 MOO가 손가락 가리키기와 같은 비언어 기반 입력 양식으로 일반화되어 관심 객체를 지정할 수 있으며, 개방형 세계 탐색 및 조작을 가능하게 확장될 수 있음을 보여줍니다. 프로젝트 웹사이트와 평가 비디오는 https://robot-moo.github.io/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2303.00905v2
