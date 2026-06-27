---
$id: ent_paper_li_from_w1_towards_general_humano_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
  zh: FRoM-W1：面向自然语言指令的通用人形机器人全身控制
  ko: 'FRoM-W1: 자연어 명령을 통한 범용 휴머노이드 전신 제어를 향하여'
summary:
  en: FRoM-W1 is an open-source two-stage framework that generates whole-body human
    motions from natural-language instructions using a 9B LLaMA-based model (H-GPT)
    and then retargets and executes them on real humanoid robots (Unitree H1 and G1)
    via a reinforcement-learning motion controller (H-ACT) with a modular sim2real
    deployment module (RoboJudo).
  zh: FRoM-W1 是一个开源两阶段框架，首先利用基于 9B LLaMA 的 H-GPT 模型从自然语言指令生成全身人体动作，然后通过强化学习运动控制器 H-ACT
    将动作重定向并在宇树 H1 与 G1 等人形机器人上执行，并借助模块化 sim2real 部署模块 RoboJudo 迁移到真实机器人。
  ko: FRoM-W1은 9B LLaMA 기반 H-GPT 모델로 자연어 명령에서 전신 인체 동작을 생성하고, 강화학습 기반 동작 컨트롤러 H-ACT를
    통해 이를 Unitree H1 및 G1 등의 실제 휴머노이드 로봇으로 리타기팅 및 실행하며, 모듈형 sim2real 배포 모듈인 RoboJudo로
    실제 로봇에 적용하는 오픈소스 2단계 프레임워크이다.
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
- natural_language_control
- whole_body_control
- humanoid_robot
- motion_generation
- sim2real
- reinforcement_learning
- human_to_humanoid_retargeting
- llama
- chain_of_thought
- unitree_h1
- unitree_g1
- open_source
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full-text verification required
    for exact claim support and section-level citations.
sources:
- id: src_001
  type: paper
  title: 'FRoM-W1: Towards General Humanoid Whole-Body Control with Language Instructions'
  url: https://arxiv.org/abs/2601.12799
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---

## Overview

FRoM-W1 addresses the limitation that humanoid robot motions are often hard-coded or task-specific by proposing a general, open-source framework for language-driven whole-body control. The framework consists of two stages. First, H-GPT is a 9B-parameter LLaMA-based language-to-human-motion generation model trained on large-scale human motion data; it generates diverse natural whole-body behaviors and uses Chain-of-Thought reasoning to improve generalization on complex language instructions. Second, H-ACT retargets the generated human SMPL-X motions into robot-specific actions and tracks them with a controller that is pretrained and then fine-tuned through reinforcement learning in physical simulation before being transferred to real hardware via a modular sim2real pipeline called RoboJudo.

The authors evaluate the framework on Unitree H1 and G1 humanoid robots. On the HumanML3D-X benchmark for human whole-body motion generation with hands, FRoM-W1 achieves superior performance, and the reinforcement-learning fine-tuning stage consistently improves motion-tracking accuracy and task success rates. The project is released as a fully open-source package including code, model checkpoints, benchmarks, and deployment tools.

## Key Contributions

- H-GPT: a 9B-parameter LLaMA-based language-to-human-whole-body-motion generator enhanced with Chain-of-Thought reasoning for versatile instruction understanding.
- H-ACT: a human-to-humanoid retargeting and reinforcement-learning-based tracking controller, pretrained and inference-time fine-tuned in simulation for stable motion execution.
- RoboJudo: a modular sim2real deployment framework that supports heterogeneous policies and robot embodiments.
- HumanML3D-X and δHumanML3D-X benchmarks extending HumanML3D to whole-body motion generation with hand motion.
- A fully open-sourced framework including code, model checkpoints, datasets, benchmarks, and deployment tools.

## Relevance to Humanoid Robotics

FRoM-W1 is highly relevant to humanoid robotics because it provides an integrated, open-source pipeline connecting high-level natural-language intent to low-level stable whole-body execution on commercial humanoid platforms. By demonstrating deployment on Unitree H1 and G1 and supporting multiple robot morphologies and end-effector configurations, the work lowers the barrier to general-purpose humanoid behavior programming and supports broader industrial and research adoption of language-controlled humanoids.
