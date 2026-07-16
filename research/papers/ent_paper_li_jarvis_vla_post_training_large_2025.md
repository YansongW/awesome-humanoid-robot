---
$id: ent_paper_li_jarvis_vla_post_training_large_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse'
  zh: JARVIS-VLA
  ko: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse'
summary:
  en: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse (JARVIS-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, and published
    at ACL 2025.'
  zh: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse (JARVIS-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, and published
    at ACL 2025.'
  ko: 'JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse (JARVIS-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University, and published
    at ACL 2025.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- jarvis_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.16365v2.
sources:
- id: src_001
  type: website
  title: JARVIS-VLA source
  url: https://aclanthology.org/2025.findings-acl.920/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recently, action-based decision-making in open-world environments has gained significant attention. Visual Language Action (VLA) models, pretrained on large-scale web datasets, have shown promise in decision-making tasks. However, previous work has primarily focused on action post-training, often neglecting enhancements to the foundational model itself. In response, we introduce a novel approach, Act from Visual Language Post-Training, which refines Visual Language Models (VLMs) through visual and linguistic guidance in a self-supervised manner. This enhancement improves the models' capabilities in world knowledge, visual recognition, and spatial grounding in open-world environments. Following the above post-training paradigms, we obtain the first VLA models in Minecraft that can follow human instructions on over 1k different atomic tasks, including crafting, smelting, cooking, mining, and killing. Our experiments demonstrate that post-training on non-trajectory tasks leads to a significant 40% improvement over the best agent baseline on a diverse set of atomic tasks. Furthermore, we demonstrate that our approach surpasses traditional imitation learning-based policies in Minecraft, achieving state-of-the-art performance. We have open-sourced the code, models, and datasets to foster further research. The project page can be found in https://craftjarvis.github.io/JarvisVLA.

## 核心内容
Recently, action-based decision-making in open-world environments has gained significant attention. Visual Language Action (VLA) models, pretrained on large-scale web datasets, have shown promise in decision-making tasks. However, previous work has primarily focused on action post-training, often neglecting enhancements to the foundational model itself. In response, we introduce a novel approach, Act from Visual Language Post-Training, which refines Visual Language Models (VLMs) through visual and linguistic guidance in a self-supervised manner. This enhancement improves the models' capabilities in world knowledge, visual recognition, and spatial grounding in open-world environments. Following the above post-training paradigms, we obtain the first VLA models in Minecraft that can follow human instructions on over 1k different atomic tasks, including crafting, smelting, cooking, mining, and killing. Our experiments demonstrate that post-training on non-trajectory tasks leads to a significant 40% improvement over the best agent baseline on a diverse set of atomic tasks. Furthermore, we demonstrate that our approach surpasses traditional imitation learning-based policies in Minecraft, achieving state-of-the-art performance. We have open-sourced the code, models, and datasets to foster further research. The project page can be found in https://craftjarvis.github.io/JarvisVLA.

## 参考
- http://arxiv.org/abs/2503.16365v2

## Overview
Recently, action-based decision-making in open-world environments has gained significant attention. Visual Language Action (VLA) models, pretrained on large-scale web datasets, have shown promise in decision-making tasks. However, previous work has primarily focused on action post-training, often neglecting enhancements to the foundational model itself. In response, we introduce a novel approach, Act from Visual Language Post-Training, which refines Visual Language Models (VLMs) through visual and linguistic guidance in a self-supervised manner. This enhancement improves the models' capabilities in world knowledge, visual recognition, and spatial grounding in open-world environments. Following the above post-training paradigms, we obtain the first VLA models in Minecraft that can follow human instructions on over 1k different atomic tasks, including crafting, smelting, cooking, mining, and killing. Our experiments demonstrate that post-training on non-trajectory tasks leads to a significant 40% improvement over the best agent baseline on a diverse set of atomic tasks. Furthermore, we demonstrate that our approach surpasses traditional imitation learning-based policies in Minecraft, achieving state-of-the-art performance. We have open-sourced the code, models, and datasets to foster further research. The project page can be found in https://craftjarvis.github.io/JarvisVLA.

## Content
Recently, action-based decision-making in open-world environments has gained significant attention. Visual Language Action (VLA) models, pretrained on large-scale web datasets, have shown promise in decision-making tasks. However, previous work has primarily focused on action post-training, often neglecting enhancements to the foundational model itself. In response, we introduce a novel approach, Act from Visual Language Post-Training, which refines Visual Language Models (VLMs) through visual and linguistic guidance in a self-supervised manner. This enhancement improves the models' capabilities in world knowledge, visual recognition, and spatial grounding in open-world environments. Following the above post-training paradigms, we obtain the first VLA models in Minecraft that can follow human instructions on over 1k different atomic tasks, including crafting, smelting, cooking, mining, and killing. Our experiments demonstrate that post-training on non-trajectory tasks leads to a significant 40% improvement over the best agent baseline on a diverse set of atomic tasks. Furthermore, we demonstrate that our approach surpasses traditional imitation learning-based policies in Minecraft, achieving state-of-the-art performance. We have open-sourced the code, models, and datasets to foster further research. The project page can be found in https://craftjarvis.github.io/JarvisVLA.

## 개요
최근 오픈 월드 환경에서의 행동 기반 의사 결정이 큰 주목을 받고 있습니다. 대규모 웹 데이터셋으로 사전 학습된 VLA(Visual Language Action) 모델은 의사 결정 작업에서 가능성을 보여주었습니다. 그러나 기존 연구는 주로 행동 사후 학습에 초점을 맞추어 기반 모델 자체의 개선을 간과하는 경우가 많았습니다. 이에 대응하여, 우리는 시각 및 언어 지침을 자기 지도 방식으로 활용하여 VLM(Visual Language Models)을 정제하는 새로운 접근법인 Act from Visual Language Post-Training을 도입합니다. 이 개선은 오픈 월드 환경에서 세계 지식, 시각 인식 및 공간 기반 능력을 향상시킵니다. 위의 사후 학습 패러다임을 따라, 우리는 Minecraft에서 제작, 제련, 요리, 채굴 및 처치를 포함한 1,000개 이상의 다양한 원자 작업에 대해 인간의 지시를 따를 수 있는 최초의 VLA 모델을 얻었습니다. 실험 결과, 비궤적 작업에 대한 사후 학습이 다양한 원자 작업에서 최고의 에이전트 기준선 대비 40%의 유의미한 성능 향상을 가져옴을 입증했습니다. 또한, 우리의 접근 방식이 Minecraft에서 전통적인 모방 학습 기반 정책을 능가하여 최첨단 성능을 달성함을 보여줍니다. 추가 연구를 촉진하기 위해 코드, 모델 및 데이터셋을 오픈소스로 공개했습니다. 프로젝트 페이지는 https://craftjarvis.github.io/JarvisVLA에서 확인할 수 있습니다.

## 핵심 내용
최근 오픈 월드 환경에서의 행동 기반 의사 결정이 큰 주목을 받고 있습니다. 대규모 웹 데이터셋으로 사전 학습된 VLA(Visual Language Action) 모델은 의사 결정 작업에서 가능성을 보여주었습니다. 그러나 기존 연구는 주로 행동 사후 학습에 초점을 맞추어 기반 모델 자체의 개선을 간과하는 경우가 많았습니다. 이에 대응하여, 우리는 시각 및 언어 지침을 자기 지도 방식으로 활용하여 VLM(Visual Language Models)을 정제하는 새로운 접근법인 Act from Visual Language Post-Training을 도입합니다. 이 개선은 오픈 월드 환경에서 세계 지식, 시각 인식 및 공간 기반 능력을 향상시킵니다. 위의 사후 학습 패러다임을 따라, 우리는 Minecraft에서 제작, 제련, 요리, 채굴 및 처치를 포함한 1,000개 이상의 다양한 원자 작업에 대해 인간의 지시를 따를 수 있는 최초의 VLA 모델을 얻었습니다. 실험 결과, 비궤적 작업에 대한 사후 학습이 다양한 원자 작업에서 최고의 에이전트 기준선 대비 40%의 유의미한 성능 향상을 가져옴을 입증했습니다. 또한, 우리의 접근 방식이 Minecraft에서 전통적인 모방 학습 기반 정책을 능가하여 최첨단 성능을 달성함을 보여줍니다. 추가 연구를 촉진하기 위해 코드, 모델 및 데이터셋을 오픈소스로 공개했습니다. 프로젝트 페이지는 https://craftjarvis.github.io/JarvisVLA에서 확인할 수 있습니다.
