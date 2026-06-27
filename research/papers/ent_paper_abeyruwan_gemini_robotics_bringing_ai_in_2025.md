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
  en: This report introduces Gemini Robotics and Gemini Robotics-ER, a family of Vision-Language-Action
    and embodied-reasoning models built on Gemini 2.0 that enable generalist robot
    control, few-shot adaptation, and zero-shot transfer to novel robot embodiments
    including high-DoF humanoids.
  zh: 本报告介绍了 Gemini Robotics 与 Gemini Robotics-ER，这是一系列基于 Gemini 2.0 的 vision-language-action
    与具身推理模型，能够实现通用机器人控制、小样本适应以及对包括高自由度人形机器人在内的新型机器人本体进行零样本迁移。
  ko: 본 보고서는 Gemini 2.0을 기반으로 한 Vision-Language-Action 및 구체화된 추론 모델 패밀리인 Gemini Robotics와
    Gemini Robotics-ER을 소개하며, 이는 범용 로봇 제어, 소수 샘플 적응, 고자유도 휴머노이드를 포함한 새로운 로봇 형태로의 제로샷
    전이를 가능하게 한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review is needed
    before marking verified.
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

## Overview

Gemini Robotics is presented as a generalist Vision-Language-Action (VLA) model that directly controls robots. It is built on top of Gemini 2.0 and leverages a cloud backbone together with a local action decoder to generate smooth, reactive, high-frequency robot actions. The model handles open-vocabulary instructions, variations in object types and positions, and previously unseen environments.

A companion model, Gemini Robotics-ER (Embodied Reasoning), extends Gemini's multimodal reasoning into the physical world with stronger spatial, temporal, and 3D understanding. It supports robotics-relevant capabilities such as object detection, pointing, trajectory and grasp prediction, multi-view correspondence, and 3D bounding-box prediction. Together, the two models enable zero-shot robot-code generation, few-shot in-context learning, and specialization to long-horizon dexterous tasks.

The report also introduces ERQA, an open-source benchmark for evaluating embodied reasoning in multimodal models, and discusses safety and responsible-development considerations for robotics foundation models.

## Key Contributions

- Introduces Gemini Robotics-ER, a VLM with enhanced spatial, temporal, and 3D embodied reasoning for robotics.
- Introduces Gemini Robotics, a generalist Vision-Language-Action model that directly controls robots with high-frequency dexterous actions.
- Proposes ERQA, an open-source benchmark for evaluating embodied reasoning in multimodal models.
- Demonstrates specialization to long-horizon dexterous tasks, few-shot adaptation from around 100 demonstrations, and zero-shot transfer to new robot embodiments.
- Discusses responsible development and safety considerations for robotics foundation models.

## Relevance to Humanoid Robotics

Gemini Robotics is highly relevant to humanoid robotics because it is explicitly evaluated on adaptation to a high-degrees-of-freedom humanoid, in addition to bimanual and bi-arm platforms. Its ability to follow open-vocabulary instructions, generalize across objects and scenes, and perform dexterous manipulation addresses core requirements for scalable humanoid deployment.

The paper's emphasis on embodiment transfer—adapting a single trained model to novel robot hardware—directly supports the long-term goal of general-purpose humanoid systems that can be deployed with minimal task-specific engineering. Safety considerations for foundation-model-based robot control are also pertinent as humanoids enter unstructured human environments.
