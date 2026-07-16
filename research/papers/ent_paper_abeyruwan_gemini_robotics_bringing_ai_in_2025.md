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

## Overview
Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding. This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

## Content
Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding. This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

## 개요
최근 대규모 멀티모달 모델의 발전으로 디지털 영역에서 놀라운 범용 능력이 등장했지만, 이를 로봇과 같은 물리적 에이전트로 전환하는 것은 여전히 중요한 과제로 남아 있습니다. 본 보고서는 Gemini 2.0을 기반으로 로봇 공학을 위해 특별히 설계된 새로운 AI 모델 제품군을 소개합니다. 우리는 로봇을 직접 제어할 수 있는 고급 Vision-Language-Action(VLA) 범용 모델인 Gemini Robotics를 제시합니다. Gemini Robotics는 부드럽고 반응적인 움직임을 실행하여 다양한 복잡한 조작 작업을 처리할 뿐만 아니라 객체 유형과 위치의 변화에 강건하며, 보지 못한 환경을 처리하고 다양한 개방형 어휘 명령을 따릅니다. 추가 미세 조정을 통해 Gemini Robotics는 장기적이고 고도로 정밀한 작업 해결, 최소 100개의 시연으로 새로운 단기 작업 학습, 완전히 새로운 로봇 형태에 적응하는 등 새로운 능력에 특화될 수 있음을 보여줍니다. 이는 Gemini Robotics가 본 연구에서 소개하는 두 번째 모델인 Gemini Robotics-ER 모델 위에 구축되었기 때문에 가능합니다. Gemini Robotics-ER(Embodied Reasoning)은 향상된 공간 및 시간 이해를 통해 Gemini의 멀티모달 추론 능력을 물리적 세계로 확장합니다. 이를 통해 객체 감지, 포인팅, 궤적 및 파지 예측, 다중 뷰 대응 및 3D 경계 상자 예측 등 로봇 공학과 관련된 능력이 가능해집니다. 우리는 이 새로운 조합이 다양한 로봇 공학 응용을 어떻게 지원할 수 있는지 보여줍니다. 또한 이 새로운 종류의 로봇 기초 모델과 관련된 중요한 안전 고려 사항을 논의하고 해결합니다. Gemini Robotics 제품군은 AI의 잠재력을 물리적 세계에서 실현하는 범용 로봇 개발을 향한 중요한 진전을 의미합니다.

## 핵심 내용
최근 대규모 멀티모달 모델의 발전으로 디지털 영역에서 놀라운 범용 능력이 등장했지만, 이를 로봇과 같은 물리적 에이전트로 전환하는 것은 여전히 중요한 과제로 남아 있습니다. 본 보고서는 Gemini 2.0을 기반으로 로봇 공학을 위해 특별히 설계된 새로운 AI 모델 제품군을 소개합니다. 우리는 로봇을 직접 제어할 수 있는 고급 Vision-Language-Action(VLA) 범용 모델인 Gemini Robotics를 제시합니다. Gemini Robotics는 부드럽고 반응적인 움직임을 실행하여 다양한 복잡한 조작 작업을 처리할 뿐만 아니라 객체 유형과 위치의 변화에 강건하며, 보지 못한 환경을 처리하고 다양한 개방형 어휘 명령을 따릅니다. 추가 미세 조정을 통해 Gemini Robotics는 장기적이고 고도로 정밀한 작업 해결, 최소 100개의 시연으로 새로운 단기 작업 학습, 완전히 새로운 로봇 형태에 적응하는 등 새로운 능력에 특화될 수 있음을 보여줍니다. 이는 Gemini Robotics가 본 연구에서 소개하는 두 번째 모델인 Gemini Robotics-ER 모델 위에 구축되었기 때문에 가능합니다. Gemini Robotics-ER(Embodied Reasoning)은 향상된 공간 및 시간 이해를 통해 Gemini의 멀티모달 추론 능력을 물리적 세계로 확장합니다. 이를 통해 객체 감지, 포인팅, 궤적 및 파지 예측, 다중 뷰 대응 및 3D 경계 상자 예측 등 로봇 공학과 관련된 능력이 가능해집니다. 우리는 이 새로운 조합이 다양한 로봇 공학 응용을 어떻게 지원할 수 있는지 보여줍니다. 또한 이 새로운 종류의 로봇 기초 모델과 관련된 중요한 안전 고려 사항을 논의하고 해결합니다. Gemini Robotics 제품군은 AI의 잠재력을 물리적 세계에서 실현하는 범용 로봇 개발을 향한 중요한 진전을 의미합니다.
