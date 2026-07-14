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
  en: Introduces HUMANUP, a two-stage reinforcement-learning framework that learns getting-up controllers for humanoid robots,
    enabling a Unitree G1 to recover from supine and prone lying poses on flat, deformable, slippery, and sloped terrains.
  zh: 提出 HUMANUP，一个两阶段强化学习框架，用于学习人形机器人的起身控制器，使 Unitree G1 能够在平地、可变形地面、湿滑地面和斜坡上从仰卧和俯卧姿势恢复站立。
  ko: 휴머노이드 로봇을 위한 일어서기 컨트롤러를 학습하는 두 단계 강화학습 프레임워크인 HUMANUP을 소개하며, Unitree G1이 평지, 가변형 지면, 미끄러운 지면 및 경사면에서 엎드린 자세와 누운 자세에서
    복귀할 수 있도록 함.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.12152v2.
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
## 概述
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## 核心内容
Automatic fall recovery is a crucial prerequisite before humanoid robots can be reliably deployed. Hand-designing controllers for getting up is difficult because of the varied configurations a humanoid can end up in after a fall and the challenging terrains humanoid robots are expected to operate on. This paper develops a learning framework to produce controllers that enable humanoid robots to get up from varying configurations on varying terrains. Unlike previous successful applications of learning to humanoid locomotion, the getting-up task involves complex contact patterns (which necessitates accurately modeling of the collision geometry) and sparser rewards. We address these challenges through a two-phase approach that induces a curriculum. The first stage focuses on discovering a good getting-up trajectory under minimal constraints on smoothness or speed / torque limits. The second stage then refines the discovered motions into deployable (i.e. smooth and slow) motions that are robust to variations in initial configuration and terrains. We find these innovations enable a real-world G1 humanoid robot to get up from two main situations that we considered: a) lying face up and b) lying face down, both tested on flat, deformable, slippery surfaces and slopes (e.g., sloppy grass and snowfield). This is one of the first successful demonstrations of learned getting-up policies for human-sized humanoid robots in the real world.

## 参考
- http://arxiv.org/abs/2502.12152v2

