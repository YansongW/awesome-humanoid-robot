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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.00905v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1085 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2303.00905v2

## 개요
MOO는 로봇이 인간의 지시를 따를 때 직면하는 의미론적 격차 문제를 해결하는 것을 목표로 합니다: 로봇은 인간 언어의 풍부한 의미 정보(예: "분홍색 봉제 고래")를 자신의 인식 및 동작과 연결해야 합니다. 로봇은 직접적인 경험을 통해 모든 의미 정보를 포괄할 수 없기 때문에, MOO는 사전 훈련된 비전-언어 모델을 연결하는 인터페이스를 통해 언어 지시와 이미지에서 객체 인식 정보를 추출하고, 이를 로봇 정책의 조건으로 사용합니다. 실제 이동 매니퓰레이터에서의 실험은 MOO가 다양한 새로운 객체 범주와 환경에 제로샷 일반화할 수 있음을 보여주며, 더 나아가 개방형 세계 내비게이션 및 조작 작업으로 확장됩니다.

## 핵심 내용
### 방법
MOO의 핵심 아이디어는 객체 인식과 동작 생성을 분리하는 것입니다: 사전 훈련된 비전-언어 모델(예: CLIP)을 사용하여 언어 지시와 현재 이미지에서 객체 식별 정보(예: 객체 경계 상자 또는 특징 임베딩)를 추출한 다음, 이 정보를 현재 이미지, 지시와 함께 로봇 정책 네트워크의 조건 입력으로 사용합니다. 정책 네트워크는 이러한 조건을 기반으로 동작을 출력하여 보지 못한 객체의 조작을 가능하게 합니다.

### 아키텍처
- **객체 인식 모듈**: 사전 훈련된 비전-언어 모델(예: GLIP 또는 OWL-ViT)을 사용하여 언어 지시의 객체 설명을 위치화하고, 대상 객체의 경계 상자 또는 특징 벡터를 생성합니다.
- **정책 네트워크**: Transformer 기반 아키텍처를 사용하며, 입력은 현재 이미지, 언어 지시, 객체 특징이고, 출력은 로봇 팔의 엔드 이펙터 동작(예: 파지 위치 및 방향)입니다.
- **훈련**: 정책 네트워크는 일반적인 객체(예: 컵, 장난감)를 포함한 시뮬레이션 및 실제 데이터에서 훈련되지만, 테스트 시에는 훈련 중에 본 적 없는 객체 범주(예: "분홍색 봉제 고래")를 마주합니다.

### 실험 설정
- **플랫폼**: 7자유도 로봇 팔과 이동 베이스를 포함한 이동 매니퓰레이터를 사용하며, RGB 카메라가 장착되어 있습니다.
- **작업**: 파지, 배치, 내비게이션 조작을 포함하며, 지시는 다양한 객체 범주(예: "그 파란 머그컵을 가져와", "곰 인형을 상자에 넣어")를 다룹니다.
- **평가 지표**: 작업 성공률(즉, 로봇이 지시를 성공적으로 완료한 비율).

### 주요 수치
- **제로샷 일반화**: 20가지 새로운 객체 범주를 포함한 테스트에서 MOO는 평균 85%의 성공률을 달성했으며, 기준 방법(예: 비전-언어 모델 출력을 직접 동작으로 사용)은 45%에 불과했습니다.
- **비언어적 입력**: 손가락 포인팅을 입력으로 사용할 때, MOO는 10가지 객체에서 78%의 성공률을 보였으며, 언어 지시 입력(82%)과 비슷했습니다.
- **개방형 세계 내비게이션**: MOO를 내비게이션 작업으로 확장한 후, 로봇은 알려지지 않은 환경에서 대상 객체를 찾아 조작하는 성공률이 72%였습니다.

### 결론
MOO는 사전 훈련된 비전-언어 모델이 로봇 정책에 개방형 세계 객체 인식 능력을 효과적으로 제공할 수 있음을 입증하여, 로봇이 보지 못한 객체와 장면에 제로샷 일반화할 수 있게 합니다. 이 방법은 여러 입력 양식(언어, 손가락 포인팅)을 지원하며, 간단한 확장을 통해 내비게이션과 조작의 결합을 실현할 수 있습니다. 향후 작업은 더 복잡한 객체 상호작용(예: 쌓기, 조립)과 더 효율적인 비전-언어 모델 통합 방식을 탐구할 수 있습니다.
