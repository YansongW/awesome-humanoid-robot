---
$id: ent_paper_abeyruwan_gemini_robotics_bringing_ai_in_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Gemini Robotics: Bringing AI into the Physical World'
  zh: Gemini Robotics：将 AI 引入物理世界
  ko: 'Gemini Robotics: AI를 물리 세계로 가져오기'
summary:
  en: This report introduces Gemini Robotics and Gemini Robotics-ER, a family of Vision-Language-Action and embodied-reasoning
    models built on Gemini 2.0 that enable generalist robot control, few-shot adaptation, and zero-shot transfer to novel
    robot embodiments including high-DoF humanoids.
  zh: 本报告介绍了 Gemini Robotics 与 Gemini Robotics-ER，这是一系列基于 Gemini 2.0 的 vision-language-action 与具身推理模型，能够实现通用机器人控制、小样本适应以及对包括高自由度人形机器人在内的新型机器人本体进行零样本迁移。
  ko: 본 보고서는 Gemini 2.0을 기반으로 한 Vision-Language-Action 및 구체화된 추론 모델 패밀리인 Gemini Robotics와 Gemini Robotics-ER을 소개하며, 이는 범용
    로봇 제어, 소수 샘플 적응, 고자유도 휴머노이드를 포함한 새로운 로봇 형태로의 제로샷 전이를 가능하게 한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
- system
tags:
- gemini_robotics
- gemini_robotics_er
- vla
- vision_language_action
- embodied_reasoning
- multimodal_foundation_model
- generalist_robotics
- humanoid_adaptation
- google_deepmind
- gemini_2_0
- robotics_safety
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.20020v1.
sources:
- id: src_001
  type: paper
  title: 'Gemini Robotics: Bringing AI into the Physical World'
  url: https://arxiv.org/abs/2503.20020
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding. This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

## 核心内容
Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding. This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

## 参考
- http://arxiv.org/abs/2503.20020v1

