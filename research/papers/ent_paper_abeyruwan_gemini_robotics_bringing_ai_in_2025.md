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
  zh: Gemini Robotics 和 Gemini Robotics-ER 是 Google DeepMind 基于 Gemini 2.0 构建的视觉-语言-动作（VLA）与具身推理模型系列，旨在实现通用机器人控制。其核心贡献在于支持少样本适应、零样本迁移至新型机器人形态（包括高自由度人形机器人），并具备空间与时间理解能力，为通用机器人发展迈出关键一步。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.20020v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该报告介绍了 Gemini Robotics 系列模型，它们建立在 Gemini 2.0 基础之上，专门为机器人领域设计。Gemini Robotics 作为先进的 VLA 通用模型，能直接控制机器人执行复杂操作任务，对物体类型和位置变化具有鲁棒性，可适应未知环境并遵循多样化开放词汇指令。通过微调，该模型能专精于长时程高灵巧任务，从仅 100 次演示中学习新短期任务，并适应全新机器人形态。其基础是 Gemini Robotics-ER 模型，后者将多模态推理能力扩展到物理世界，增强了空间与时间理解，支持物体检测、指向、轨迹与抓取预测、多视图对应及 3D 边界框预测等功能。该系列模型还讨论了相关安全考量，标志着向通用机器人发展的重要进展。

## 核心内容
### 模型架构与核心能力
- **Gemini Robotics**：基于 Gemini 2.0 的视觉-语言-动作（VLA）通用模型，可直接输出机器人控制指令。它能够执行平滑且反应灵敏的动作，处理复杂操作任务，对物体类型和位置变化具有鲁棒性，适应未知环境，并遵循多样化开放词汇指令。
- **Gemini Robotics-ER（具身推理）**：扩展了 Gemini 的多模态推理能力到物理世界，增强空间与时间理解。支持物体检测、指向、轨迹与抓取预测、多视图对应及 3D 边界框预测等机器人相关能力。

### 实验设置与关键数字
- **少样本适应**：通过微调，Gemini Robotics 可从仅 100 次演示中学习新短期任务，并适应全新机器人形态，包括高自由度（high-DoF）人形机器人。
- **零样本迁移**：模型支持零样本迁移至未见过的机器人形态，无需额外训练数据。
- **长时程任务**：通过额外微调，模型能解决长时程、高灵巧度的复杂任务。

### 结论与安全考量
- Gemini Robotics 系列模型标志着向通用机器人发展的重要一步，实现了 AI 在物理世界中的潜力。
- 报告讨论了与这类新型机器人基础模型相关的重要安全考量，并提出了相应措施。

## Overview
Recent advancements in large multimodal models have led to the emergence of remarkable generalist capabilities in digital domains, yet their translation to physical agents such as robots remains a significant challenge. This report introduces a new family of AI models purposefully designed for robotics and built upon the foundation of Gemini 2.0. We present Gemini Robotics, an advanced Vision-Language-Action (VLA) generalist model capable of directly controlling robots. Gemini Robotics executes smooth and reactive movements to tackle a wide range of complex manipulation tasks while also being robust to variations in object types and positions, handling unseen environments as well as following diverse, open vocabulary instructions. We show that with additional fine-tuning, Gemini Robotics can be specialized to new capabilities including solving long-horizon, highly dexterous tasks, learning new short-horizon tasks from as few as 100 demonstrations and adapting to completely novel robot embodiments. This is made possible because Gemini Robotics builds on top of the Gemini Robotics-ER model, the second model we introduce in this work. Gemini Robotics-ER (Embodied Reasoning) extends Gemini's multimodal reasoning capabilities into the physical world, with enhanced spatial and temporal understanding. This enables capabilities relevant to robotics including object detection, pointing, trajectory and grasp prediction, as well as multi-view correspondence and 3D bounding box predictions. We show how this novel combination can support a variety of robotics applications. We also discuss and address important safety considerations related to this new class of robotics foundation models. The Gemini Robotics family marks a substantial step towards developing general-purpose robots that realizes AI's potential in the physical world.

## 개요
최근 대규모 멀티모달 모델의 발전으로 디지털 영역에서 놀라운 범용 능력이 등장했지만, 이를 로봇과 같은 물리적 에이전트로 전환하는 것은 여전히 중요한 과제로 남아 있습니다. 본 보고서는 Gemini 2.0을 기반으로 로봇 공학을 위해 특별히 설계된 새로운 AI 모델 제품군을 소개합니다. 우리는 로봇을 직접 제어할 수 있는 고급 Vision-Language-Action(VLA) 범용 모델인 Gemini Robotics를 제시합니다. Gemini Robotics는 부드럽고 반응적인 움직임을 실행하여 다양한 복잡한 조작 작업을 처리할 뿐만 아니라 객체 유형과 위치의 변화에 강건하며, 보지 못한 환경을 처리하고 다양한 개방형 어휘 명령을 따릅니다. 추가 미세 조정을 통해 Gemini Robotics는 장기적이고 고도로 정밀한 작업 해결, 최소 100개의 시연으로 새로운 단기 작업 학습, 완전히 새로운 로봇 형태에 적응하는 등 새로운 능력에 특화될 수 있음을 보여줍니다. 이는 Gemini Robotics가 본 연구에서 소개하는 두 번째 모델인 Gemini Robotics-ER 모델 위에 구축되었기 때문에 가능합니다. Gemini Robotics-ER(Embodied Reasoning)은 향상된 공간 및 시간 이해를 통해 Gemini의 멀티모달 추론 능력을 물리적 세계로 확장합니다. 이를 통해 객체 감지, 포인팅, 궤적 및 파지 예측, 다중 뷰 대응 및 3D 경계 상자 예측 등 로봇 공학과 관련된 능력이 가능해집니다. 우리는 이 새로운 조합이 다양한 로봇 공학 응용을 어떻게 지원할 수 있는지 보여줍니다. 또한 이 새로운 종류의 로봇 기초 모델과 관련된 중요한 안전 고려 사항을 논의하고 해결합니다. Gemini Robotics 제품군은 AI의 잠재력을 물리적 세계에서 실현하는 범용 로봇 개발을 향한 중요한 진전을 의미합니다.

## 핵심 내용
최근 대규모 멀티모달 모델의 발전으로 디지털 영역에서 놀라운 범용 능력이 등장했지만, 이를 로봇과 같은 물리적 에이전트로 전환하는 것은 여전히 중요한 과제로 남아 있습니다. 본 보고서는 Gemini 2.0을 기반으로 로봇 공학을 위해 특별히 설계된 새로운 AI 모델 제품군을 소개합니다. 우리는 로봇을 직접 제어할 수 있는 고급 Vision-Language-Action(VLA) 범용 모델인 Gemini Robotics를 제시합니다. Gemini Robotics는 부드럽고 반응적인 움직임을 실행하여 다양한 복잡한 조작 작업을 처리할 뿐만 아니라 객체 유형과 위치의 변화에 강건하며, 보지 못한 환경을 처리하고 다양한 개방형 어휘 명령을 따릅니다. 추가 미세 조정을 통해 Gemini Robotics는 장기적이고 고도로 정밀한 작업 해결, 최소 100개의 시연으로 새로운 단기 작업 학습, 완전히 새로운 로봇 형태에 적응하는 등 새로운 능력에 특화될 수 있음을 보여줍니다. 이는 Gemini Robotics가 본 연구에서 소개하는 두 번째 모델인 Gemini Robotics-ER 모델 위에 구축되었기 때문에 가능합니다. Gemini Robotics-ER(Embodied Reasoning)은 향상된 공간 및 시간 이해를 통해 Gemini의 멀티모달 추론 능력을 물리적 세계로 확장합니다. 이를 통해 객체 감지, 포인팅, 궤적 및 파지 예측, 다중 뷰 대응 및 3D 경계 상자 예측 등 로봇 공학과 관련된 능력이 가능해집니다. 우리는 이 새로운 조합이 다양한 로봇 공학 응용을 어떻게 지원할 수 있는지 보여줍니다. 또한 이 새로운 종류의 로봇 기초 모델과 관련된 중요한 안전 고려 사항을 논의하고 해결합니다. Gemini Robotics 제품군은 AI의 잠재력을 물리적 세계에서 실현하는 범용 로봇 개발을 향한 중요한 진전을 의미합니다.

## 参考
- http://arxiv.org/abs/2503.20020v1
