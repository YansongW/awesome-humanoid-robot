---
$id: ent_paper_lisondra_embodied_ai_with_foundation_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embodied AI with Foundation Models for Mobile Service Robots: A Systematic
    Review'
  zh: 面向移动服务机器人的基础模型具身智能：系统综述
  ko: '이동 서비스 로봇을 위한 파운데이션 모델 기반 구체화된 AI: 체계적 리뷰'
summary:
  en: A 2025 systematic review analyzing how large language, vision-language, multimodal,
    and vision-language-action models address language-to-action mapping, multimodal
    perception, uncertainty estimation, and onboard deployment challenges in mobile
    service robotics.
  zh: 2025年系统综述，分析大语言模型、视觉-语言模型、多模态大语言模型和视觉-语言-动作模型如何解决移动服务机器人中的语言到动作映射、多模态感知、不确定性估计和机载部署挑战。
  ko: 2025년 체계적 리뷰로, 대형 언어 모델, 비전-언어 모델, 멀티모달 대형 언어 모델, 비전-언어-행동 모델이 이동 서비스 로봇의 언어-행동
    매핑, 다중감각 인식, 불확실성 추정, 온보드 배포 과제를 어떻게 해결하는지 분석함.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 12_policy_regulation_ethics
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- foundation_models
- mobile_service_robots
- vision_language_action_models
- multimodal_perception
- language_conditioned_control
- uncertainty_aware_reasoning
- human_robot_interaction
- domestic_assistance
- healthcare_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; full-text verification
    needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'Embodied AI with Foundation Models for Mobile Service Robots: A Systematic
    Review'
  url: https://arxiv.org/abs/2505.20503
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This systematic review examines the integration of foundation models—Large Language Models (LLMs), Vision-Language Models (VLMs), Multimodal Large Language Models (MLLMs), and Vision-Language-Action Models (VLAs)—into mobile service robotics. The authors frame embodied AI as the intersection of perception, reasoning, and physical action, and focus on four persistent challenges: translating natural-language instructions into executable robot actions, fusing multimodal perception in human-centered environments, estimating uncertainty for safe decision-making, and scaling models for resource-constrained onboard deployment. The review is supported by an OpenAlex-based bibliometric analysis of 7,506 relevant works.

The paper organizes recent advances around a unified architecture that maps foundation models to mobile service robot perception, planning, and control. For each of the four core challenges, the authors survey how LLMs, VLMs, MLLMs, and VLAs have been applied, and connect these technical advances to real-world use cases such as domestic assistance, healthcare support, and service automation. The review also addresses ethical, societal, privacy, and human-robot interaction implications.

Finally, the authors outline future research directions emphasizing reliability and lifelong adaptation, privacy-aware and resource-constrained deployment, and governance and human-in-the-loop frameworks. They argue that safe, scalable, and trustworthy mobile service robotics will require progress across all of these dimensions rather than isolated model improvements.

## Key Contributions

- Identifies and ranks four core challenges for embodied AI in mobile service robots: language-to-action mapping, multimodal perception, uncertainty estimation, and computational capabilities.
- Proposes a unified architecture showing how foundation models integrate perception, planning, and control in mobile service robots.
- Surveys how LLMs, VLMs, MLLMs, and VLAs address each challenge and maps them to real-world domestic, healthcare, and service-automation applications.
- Discusses ethical, societal, privacy, and human-robot interaction implications of deploying foundation model-enabled service robots.
- Outlines future research directions for reliable, resource-constrained, privacy-aware, and human-in-the-loop mobile service robotics.

## Relevance to Humanoid Robotics

The review directly maps the same foundation-model building blocks—language-to-action grounding, multimodal perception, uncertainty-aware reasoning, and onboard-efficient inference—to the perception-planning-control stack needed for humanoid robot deployment in homes, hospitals, and public service settings. Humanoid robots operating in these unstructured, human-centered environments must solve the identical set of challenges: understanding natural-language instructions, integrating visual, linguistic, and proprioceptive signals, reasoning under uncertainty, and running capable models on limited onboard compute.

By surveying how foundation models are integrated into mobile service robots and mobile manipulators such as Stretch RE-1, Fetch, LoCoBot, Mobile ALOHA, and Boston Dynamics Spot, the paper provides a transferable blueprint for humanoid systems. Its discussion of ethical, privacy, and governance considerations is also directly applicable to humanoid robots deployed in close proximity to people.
