---
$id: ent_paper_nasiriany_pivot_iterative_visual_prompti_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs'
  zh: PIVOT
  ko: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs'
summary:
  en: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs (PIVOT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Stanford University, The University of Texas at Austin,
    and published at ICML 2024.'
  zh: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs (PIVOT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Stanford University, The University of Texas at Austin,
    and published at ICML 2024.'
  ko: 'PIVOT: Iterative Visual Prompting Elicits Actionable Knowledge for VLMs (PIVOT), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Google DeepMind, Stanford University, The University of Texas at Austin,
    and published at ICML 2024.'
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
- pivot
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.07872v1.
sources:
- id: src_001
  type: paper
  title: PIVOT source
  url: https://openreview.net/forum?id=051jaf8MQy
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data?   In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains. Website: pivot-prompt.github.io and HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## 核心内容
Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data?   In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains. Website: pivot-prompt.github.io and HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## 参考
- http://arxiv.org/abs/2402.07872v1

## Overview
Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data? In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains. Website: pivot-prompt.github.io and HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## Content
Vision language models (VLMs) have shown impressive capabilities across a variety of tasks, from logical reasoning to visual understanding. This opens the door to richer interaction with the world, for example robotic control. However, VLMs produce only textual outputs, while robotic control and other spatial tasks require outputting continuous coordinates, actions, or trajectories. How can we enable VLMs to handle such settings without fine-tuning on task-specific data? In this paper, we propose a novel visual prompting approach for VLMs that we call Prompting with Iterative Visual Optimization (PIVOT), which casts tasks as iterative visual question answering. In each iteration, the image is annotated with a visual representation of proposals that the VLM can refer to (e.g., candidate robot actions, localizations, or trajectories). The VLM then selects the best ones for the task. These proposals are iteratively refined, allowing the VLM to eventually zero in on the best available answer. We investigate PIVOT on real-world robotic navigation, real-world manipulation from images, instruction following in simulation, and additional spatial inference tasks such as localization. We find, perhaps surprisingly, that our approach enables zero-shot control of robotic systems without any robot training data, navigation in a variety of environments, and other capabilities. Although current performance is far from perfect, our work highlights potentials and limitations of this new regime and shows a promising approach for Internet-Scale VLMs in robotic and spatial reasoning domains. Website: pivot-prompt.github.io and HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## 개요
비전 언어 모델(VLM)은 논리적 추론부터 시각적 이해에 이르기까지 다양한 작업에서 인상적인 능력을 보여주었습니다. 이는 로봇 제어와 같은 세계와의 더 풍부한 상호작용 가능성을 열어줍니다. 그러나 VLM은 텍스트 출력만 생성하는 반면, 로봇 제어 및 기타 공간 작업은 연속적인 좌표, 동작 또는 궤적을 출력해야 합니다. 작업별 데이터에 미세 조정 없이 VLM이 이러한 설정을 처리할 수 있도록 하려면 어떻게 해야 할까요? 본 논문에서는 작업을 반복적인 시각적 질문 응답으로 변환하는 PIVOT(Prompting with Iterative Visual Optimization)이라는 VLM을 위한 새로운 시각적 프롬프트 접근 방식을 제안합니다. 각 반복에서 이미지는 VLM이 참조할 수 있는 제안(예: 후보 로봇 동작, 위치 또는 궤적)의 시각적 표현으로 주석 처리됩니다. 그런 다음 VLM은 작업에 가장 적합한 것을 선택합니다. 이러한 제안은 반복적으로 정제되어 VLM이 궁극적으로 최상의 답변에 도달할 수 있도록 합니다. 우리는 실제 로봇 내비게이션, 이미지 기반 실제 조작, 시뮬레이션에서의 명령 따르기, 위치 파악과 같은 추가 공간 추론 작업에서 PIVOT을 조사했습니다. 놀랍게도, 우리의 접근 방식은 로봇 훈련 데이터 없이도 로봇 시스템의 제로샷 제어, 다양한 환경에서의 내비게이션 및 기타 기능을 가능하게 합니다. 현재 성능이 완벽하지는 않지만, 우리의 연구는 이 새로운 체계의 잠재력과 한계를 강조하며 로봇 및 공간 추론 영역에서 인터넷 규모 VLM을 위한 유망한 접근 방식을 보여줍니다. 웹사이트: pivot-prompt.github.io 및 HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.

## 핵심 내용
비전 언어 모델(VLM)은 논리적 추론부터 시각적 이해에 이르기까지 다양한 작업에서 인상적인 능력을 보여주었습니다. 이는 로봇 제어와 같은 세계와의 더 풍부한 상호작용 가능성을 열어줍니다. 그러나 VLM은 텍스트 출력만 생성하는 반면, 로봇 제어 및 기타 공간 작업은 연속적인 좌표, 동작 또는 궤적을 출력해야 합니다. 작업별 데이터에 미세 조정 없이 VLM이 이러한 설정을 처리할 수 있도록 하려면 어떻게 해야 할까요? 본 논문에서는 작업을 반복적인 시각적 질문 응답으로 변환하는 PIVOT(Prompting with Iterative Visual Optimization)이라는 VLM을 위한 새로운 시각적 프롬프트 접근 방식을 제안합니다. 각 반복에서 이미지는 VLM이 참조할 수 있는 제안(예: 후보 로봇 동작, 위치 또는 궤적)의 시각적 표현으로 주석 처리됩니다. 그런 다음 VLM은 작업에 가장 적합한 것을 선택합니다. 이러한 제안은 반복적으로 정제되어 VLM이 궁극적으로 최상의 답변에 도달할 수 있도록 합니다. 우리는 실제 로봇 내비게이션, 이미지 기반 실제 조작, 시뮬레이션에서의 명령 따르기, 위치 파악과 같은 추가 공간 추론 작업에서 PIVOT을 조사했습니다. 놀랍게도, 우리의 접근 방식은 로봇 훈련 데이터 없이도 로봇 시스템의 제로샷 제어, 다양한 환경에서의 내비게이션 및 기타 기능을 가능하게 합니다. 현재 성능이 완벽하지는 않지만, 우리의 연구는 이 새로운 체계의 잠재력과 한계를 강조하며 로봇 및 공간 추론 영역에서 인터넷 규모 VLM을 위한 유망한 접근 방식을 보여줍니다. 웹사이트: pivot-prompt.github.io 및 HuggingFace: https://huggingface.co/spaces/pivot-prompt/pivot-prompt-demo.
