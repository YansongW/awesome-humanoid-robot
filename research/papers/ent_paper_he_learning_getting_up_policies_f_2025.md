---
$id: ent_paper_he_learning_getting_up_policies_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Getting-Up Policies for Real-World Humanoid Robots
  zh: 面向现实世界人形机器人的起身策略学习
  ko: 실제 세계 휴머노이드 로봇을 위한 일어서기 정책 학습
summary:
  en: Introduces HUMANUP, a two-stage reinforcement-learning framework that learns
    getting-up controllers for humanoid robots, enabling a Unitree G1 to recover from
    supine and prone lying poses on flat, deformable, slippery, and sloped terrains.
  zh: 提出 HUMANUP，一个两阶段强化学习框架，用于学习人形机器人的起身控制器，使 Unitree G1 能够在平地、可变形地面、湿滑地面和斜坡上从仰卧和俯卧姿势恢复站立。
  ko: 휴머노이드 로봇을 위한 일어서기 컨트롤러를 학습하는 두 단계 강화학습 프레임워크인 HUMANUP을 소개하며, Unitree G1이 평지,
    가변형 지면, 미끄러운 지면 및 경사면에서 엎드린 자세와 누운 자세에서 복귀할 수 있도록 함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- sim_to_real
- fall_recovery
- whole_body_control
- unitree_g1
- isaac_gym
- domain_randomization
- contact_rich_motion
- humanoid_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; requires human review
    against the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Learning Getting-Up Policies for Real-World Humanoid Robots
  url: https://arxiv.org/abs/2502.12152
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: Real-world experiments are conducted on a Unitree G1 humanoid robot.
    zh: 在 Unitree G1 人形机器人上进行真实世界实验。
    ko: Unitree G1 휴머노이드 로봇에서 실제 세계 실험을 수행함.
- id: ent_oem_unitree_robotics
  relationship: uses
  description:
    en: Uses the Unitree G1 robot platform developed by Unitree Robotics.
    zh: 使用宇树科技开发的 Unitree G1 机器人平台。
    ko: Unitree Robotics가 개발한 Unitree G1 로봇 플랫폼을 사용함.
---

## Overview

Automatic fall recovery is a critical prerequisite for deploying humanoid robots in unstructured environments. This paper presents HUMANUP, a learning framework that trains controllers to get a humanoid robot up from diverse fallen configurations on varied terrains. Unlike learned locomotion policies, the getting-up task involves complex contact patterns with the environment, requiring accurate collision modeling and dealing with sparser rewards.

HUMANUP addresses these challenges through a two-phase curriculum. In Stage I, a policy discovers getting-up or rolling-over motions under weak regularization, allowing the optimizer to explore aggressive contact-rich behaviors without early constraints on smoothness, speed, or torque limits. In Stage II, the discovered motions are slowed down and tracked by a refined policy with strong control regularization and domain randomization, producing smooth, deployable controllers that are robust to variations in initial posture and terrain. The framework is trained in Isaac Gym at 1 kHz and transferred to a real Unitree G1 robot.

The real-world evaluation covers six terrains, including flat ground, deformable surfaces, slippery surfaces, and slopes such as sloppy grass and snowfield. The robot is tested from two initial situations: lying face up (supine) and lying face down (prone). The authors report that the learned policies achieve higher success rates and lower motor heating than the manufacturer-provided controller.

## Key Contributions

- Two-stage RL curriculum that separates motion discovery from deployable policy learning for contact-rich getting-up tasks.
- Whole-body policies that handle both supine and prone lying poses without hand-designed trajectories.
- Real-world sim-to-real transfer on a Unitree G1 robot across six terrains including slopes, grass, and snow.
- Demonstration of higher success rates and lower motor heating than the manufacturer-provided controller.

## Relevance to Humanoid Robotics

Reliable automatic fall recovery directly improves the operational robustness of humanoid robots in real-world deployments. By learning to get up from arbitrary fallen configurations on challenging terrains, the work reduces dependence on human intervention after falls and moves humanoid systems closer to autonomous long-duration operation.

The paper is also practically relevant because it validates the approach on a commercially available, human-sized humanoid platform (Unitree G1) rather than only in simulation, demonstrating sim-to-real transfer for a highly dynamic, contact-rich whole-body skill.
