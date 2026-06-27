---
$id: ent_paper_liu_enhancing_the_llm_based_robot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
  zh: 通过人机协作增强基于大语言模型的机器人操作
  ko: 인간-로봇 협업을 통한 LLM 기반 로봇 조작 향상
summary:
  en: Proposes a GPT-4-based hierarchical planning framework integrated with YOLOv5
    visual perception and a teleoperation-DMP human-robot collaboration mechanism,
    validated on the Toyota Human Support Robot for complex manipulation tasks.
  zh: 提出了一种基于GPT-4的分层规划框架，结合YOLOv5视觉感知和基于遥操作的DMP人机协作机制，并在丰田人体支持机器人上验证了复杂操作任务。
  ko: YOLOv5 시각 인식 및 텔레오퍼레이션-DMP 인간-로봇 협업 메커니즘을 결합한 GPT-4 기반 계층적 계획 프레임워크를 제안하고 도요타
    휴먼 서포트 로봇에서 복잡한 조작 작업으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- llm_planning
- human_robot_collaboration
- teleoperation
- dynamic_movement_primitives
- yolov5
- visual_grounding
- toyota_hsr
- service_robotics
- one_shot_learning
- ros
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full paper before final verification.
sources:
- id: src_001
  type: paper
  title: Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
  url: https://arxiv.org/abs/2406.14097
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3415931
theoretical_depth:
- method
---

## Overview

Large Language Models (LLMs) are increasingly applied to robotics, yet existing LLM-based robots are mostly confined to simple, repetitive motions because language models, robots, and the environment are poorly integrated. This paper presents a human-robot collaboration (HRC) framework that uses a prompted GPT-4 model to decompose high-level natural-language commands into executable motion sequences. A YOLOv5-based perception module supplies visual cues to the LLM, enabling environment-aware motion planning, while a teleoperation interface combined with Dynamic Movement Primitives (DMP) allows the robot to learn custom trajectories from a single human demonstration.

Real-world experiments were conducted on the Toyota Human Support Robot (HSR), equipped with an Xtion depth camera and an Oculus VR device for teleoperation. The results indicate that tasks requiring complex trajectory planning and reasoning over the environment can be accomplished efficiently once human demonstrations are incorporated. By linking high-level language reasoning, visual perception, and low-level motion learning, the work provides a unified manipulation pipeline for service robots.

## Key Contributions

- GPT-4-based LLM planning framework for complex, long-horizon manipulation tasks, augmented by YOLOv5 visual perception.
- Hierarchical prompting framework that decomposes high-level commands into sub-tasks and executable motion functions.
- Teleoperation-based HRC method combining VR teleoperation and DMP for one-shot skill learning.
- Real-world validation on the Toyota HSR demonstrating that HRC enables previously infeasible complex trajectories.

## Relevance to Humanoid Robotics

For humanoid robots to be deployed at scale in service and domestic environments, they must interpret natural-language instructions, perceive cluttered scenes, and acquire new manipulation skills with minimal programming. This paper addresses all three capabilities by grounding GPT-4 planning in YOLOv5 visual input and using DMP-based learning from teleoperated demonstrations, making the resulting pipeline directly transferable to humanoid platforms that require adaptive, long-horizon manipulation in unstructured settings.

Furthermore, the reliance on widely available hardware such as RGB-D cameras, VR headsets, and commodity LLM APIs means the approach can be replicated across different humanoid robot designs without requiring custom end-effectors or expensive sensing suites, supporting both prototyping and mass-production roadmaps.
