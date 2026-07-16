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
  zh: Open-World Object Manipulation using Pre-trained Vision-Language Models (MOO), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2023.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.00905v2.
sources:
- id: src_001
  type: paper
  title: MOO source
  url: https://proceedings.mlr.press/v229/stone23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
For robots to follow instructions from people, they must be able to connect the rich semantic information in human vocabulary, e.g. "can you get me the pink stuffed whale?" to their sensory observations and actions. This brings up a notably difficult challenge for robots: while robot learning approaches allow robots to learn many different behaviors from first-hand experience, it is impractical for robots to have first-hand experiences that span all of this semantic information. We would like a robot's policy to be able to perceive and pick up the pink stuffed whale, even if it has never seen any data interacting with a stuffed whale before. Fortunately, static data on the internet has vast semantic information, and this information is captured in pre-trained vision-language models. In this paper, we study whether we can interface robot policies with these pre-trained models, with the aim of allowing robots to complete instructions involving object categories that the robot has never seen first-hand. We develop a simple approach, which we call Manipulation of Open-World Objects (MOO), which leverages a pre-trained vision-language model to extract object-identifying information from the language command and image, and conditions the robot policy on the current image, the instruction, and the extracted object information. In a variety of experiments on a real mobile manipulator, we find that MOO generalizes zero-shot to a wide range of novel object categories and environments. In addition, we show how MOO generalizes to other, non-language-based input modalities to specify the object of interest such as finger pointing, and how it can be further extended to enable open-world navigation and manipulation. The project's website and evaluation videos can be found at https://robot-moo.github.io/

## 核心内容
For robots to follow instructions from people, they must be able to connect the rich semantic information in human vocabulary, e.g. "can you get me the pink stuffed whale?" to their sensory observations and actions. This brings up a notably difficult challenge for robots: while robot learning approaches allow robots to learn many different behaviors from first-hand experience, it is impractical for robots to have first-hand experiences that span all of this semantic information. We would like a robot's policy to be able to perceive and pick up the pink stuffed whale, even if it has never seen any data interacting with a stuffed whale before. Fortunately, static data on the internet has vast semantic information, and this information is captured in pre-trained vision-language models. In this paper, we study whether we can interface robot policies with these pre-trained models, with the aim of allowing robots to complete instructions involving object categories that the robot has never seen first-hand. We develop a simple approach, which we call Manipulation of Open-World Objects (MOO), which leverages a pre-trained vision-language model to extract object-identifying information from the language command and image, and conditions the robot policy on the current image, the instruction, and the extracted object information. In a variety of experiments on a real mobile manipulator, we find that MOO generalizes zero-shot to a wide range of novel object categories and environments. In addition, we show how MOO generalizes to other, non-language-based input modalities to specify the object of interest such as finger pointing, and how it can be further extended to enable open-world navigation and manipulation. The project's website and evaluation videos can be found at https://robot-moo.github.io/

## 参考
- http://arxiv.org/abs/2303.00905v2

## Overview
For robots to follow instructions from people, they must be able to connect the rich semantic information in human vocabulary, e.g. "can you get me the pink stuffed whale?" to their sensory observations and actions. This brings up a notably difficult challenge for robots: while robot learning approaches allow robots to learn many different behaviors from first-hand experience, it is impractical for robots to have first-hand experiences that span all of this semantic information. We would like a robot's policy to be able to perceive and pick up the pink stuffed whale, even if it has never seen any data interacting with a stuffed whale before. Fortunately, static data on the internet has vast semantic information, and this information is captured in pre-trained vision-language models. In this paper, we study whether we can interface robot policies with these pre-trained models, with the aim of allowing robots to complete instructions involving object categories that the robot has never seen first-hand. We develop a simple approach, which we call Manipulation of Open-World Objects (MOO), which leverages a pre-trained vision-language model to extract object-identifying information from the language command and image, and conditions the robot policy on the current image, the instruction, and the extracted object information. In a variety of experiments on a real mobile manipulator, we find that MOO generalizes zero-shot to a wide range of novel object categories and environments. In addition, we show how MOO generalizes to other, non-language-based input modalities to specify the object of interest such as finger pointing, and how it can be further extended to enable open-world navigation and manipulation. The project's website and evaluation videos can be found at https://robot-moo.github.io/

## Content
For robots to follow instructions from people, they must be able to connect the rich semantic information in human vocabulary, e.g. "can you get me the pink stuffed whale?" to their sensory observations and actions. This brings up a notably difficult challenge for robots: while robot learning approaches allow robots to learn many different behaviors from first-hand experience, it is impractical for robots to have first-hand experiences that span all of this semantic information. We would like a robot's policy to be able to perceive and pick up the pink stuffed whale, even if it has never seen any data interacting with a stuffed whale before. Fortunately, static data on the internet has vast semantic information, and this information is captured in pre-trained vision-language models. In this paper, we study whether we can interface robot policies with these pre-trained models, with the aim of allowing robots to complete instructions involving object categories that the robot has never seen first-hand. We develop a simple approach, which we call Manipulation of Open-World Objects (MOO), which leverages a pre-trained vision-language model to extract object-identifying information from the language command and image, and conditions the robot policy on the current image, the instruction, and the extracted object information. In a variety of experiments on a real mobile manipulator, we find that MOO generalizes zero-shot to a wide range of novel object categories and environments. In addition, we show how MOO generalizes to other, non-language-based input modalities to specify the object of interest such as finger pointing, and how it can be further extended to enable open-world navigation and manipulation. The project's website and evaluation videos can be found at https://robot-moo.github.io/

## 개요
로봇이 사람의 지시를 따르기 위해서는 인간 어휘의 풍부한 의미 정보(예: "분홍색 봉제 고래를 가져다 줄래?")를 감각 관찰 및 행동과 연결할 수 있어야 합니다. 이는 로봇에게 특히 어려운 과제를 제기합니다. 로봇 학습 접근법을 통해 로봇이 직접 경험을 통해 다양한 행동을 학습할 수 있지만, 이러한 모든 의미 정보를 포괄하는 직접 경험을 로봇이 갖는 것은 비현실적입니다. 우리는 로봇의 정책이 봉제 고래와 상호작용한 데이터를 전혀 본 적이 없더라도 분홍색 봉제 고래를 인식하고 집을 수 있기를 바랍니다. 다행히도 인터넷의 정적 데이터는 방대한 의미 정보를 포함하고 있으며, 이 정보는 사전 훈련된 시각-언어 모델에 포착되어 있습니다. 본 논문에서는 로봇이 직접 경험한 적이 없는 객체 범주를 포함하는 지시를 완료할 수 있도록, 로봇 정책을 이러한 사전 훈련된 모델과 연결할 수 있는지 연구합니다. 우리는 MOO(Manipulation of Open-World Objects)라는 간단한 접근법을 개발했습니다. 이는 사전 훈련된 시각-언어 모델을 활용하여 언어 명령과 이미지에서 객체 식별 정보를 추출하고, 현재 이미지, 지시, 추출된 객체 정보에 따라 로봇 정책을 조건화합니다. 실제 모바일 매니퓰레이터를 대상으로 한 다양한 실험에서 MOO가 다양한 새로운 객체 범주와 환경에 대해 제로샷 일반화를 수행함을 확인했습니다. 또한 MOO가 손가락 가리키기와 같은 비언어 기반 입력 양식으로 일반화되어 관심 객체를 지정할 수 있으며, 개방형 세계 탐색 및 조작을 가능하게 확장될 수 있음을 보여줍니다. 프로젝트 웹사이트와 평가 비디오는 https://robot-moo.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
로봇이 사람의 지시를 따르기 위해서는 인간 어휘의 풍부한 의미 정보(예: "분홍색 봉제 고래를 가져다 줄래?")를 감각 관찰 및 행동과 연결할 수 있어야 합니다. 이는 로봇에게 특히 어려운 과제를 제기합니다. 로봇 학습 접근법을 통해 로봇이 직접 경험을 통해 다양한 행동을 학습할 수 있지만, 이러한 모든 의미 정보를 포괄하는 직접 경험을 로봇이 갖는 것은 비현실적입니다. 우리는 로봇의 정책이 봉제 고래와 상호작용한 데이터를 전혀 본 적이 없더라도 분홍색 봉제 고래를 인식하고 집을 수 있기를 바랍니다. 다행히도 인터넷의 정적 데이터는 방대한 의미 정보를 포함하고 있으며, 이 정보는 사전 훈련된 시각-언어 모델에 포착되어 있습니다. 본 논문에서는 로봇이 직접 경험한 적이 없는 객체 범주를 포함하는 지시를 완료할 수 있도록, 로봇 정책을 이러한 사전 훈련된 모델과 연결할 수 있는지 연구합니다. 우리는 MOO(Manipulation of Open-World Objects)라는 간단한 접근법을 개발했습니다. 이는 사전 훈련된 시각-언어 모델을 활용하여 언어 명령과 이미지에서 객체 식별 정보를 추출하고, 현재 이미지, 지시, 추출된 객체 정보에 따라 로봇 정책을 조건화합니다. 실제 모바일 매니퓰레이터를 대상으로 한 다양한 실험에서 MOO가 다양한 새로운 객체 범주와 환경에 대해 제로샷 일반화를 수행함을 확인했습니다. 또한 MOO가 손가락 가리키기와 같은 비언어 기반 입력 양식으로 일반화되어 관심 객체를 지정할 수 있으며, 개방형 세계 탐색 및 조작을 가능하게 확장될 수 있음을 보여줍니다. 프로젝트 웹사이트와 평가 비디오는 https://robot-moo.github.io/ 에서 확인할 수 있습니다.
