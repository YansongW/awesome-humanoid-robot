---
$id: ent_paper_hu_robot_trains_robot_automatic_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids'
  zh: 机器人训练机器人：人形机器人的自动现实世界策略适应与学习
  ko: '로봇이 로봇을 훈련시킨다: 휴머노이드를 위한 자동 실제 세계 정책 적응 및 학습'
summary:
  en: This paper proposes Robot-Trains-Robot (RTR), a framework in which a robot-arm teacher supports and guides a humanoid
    student through compliant contact, curriculum scheduling, perturbations, failure detection, and automatic resets, enabling
    efficient real-world reinforcement learning with minimal human intervention. The authors also introduce a dynamics-aware
    latent-optimization pipeline using FiLM layers and domain randomization to stabilize sim-to-real transfer, and demonstrate
    it on a ToddlerBot humanoid for walking-speed tracking fine-tuning and swing-up learning from scratch.
  zh: 本文提出了机器人训练机器人（RTR）框架，其中一个机器臂教师通过柔顺接触、课程调度、扰动、故障检测和自动重置来支持和引导人形学生，从而实现最少人工干预的高效现实世界强化学习。作者还介绍了使用 FiLM 层和域随机化的动态感知潜变量优化流程以稳定仿真到现实的迁移，并在
    ToddlerBot 人形机器人上展示了行走速度跟踪微调和从零开始的起身摆动学习。
  ko: 본 논문은 로봇 팔 교사가 순응적 접촉, 커리큘럼 스케줄링, 섭동, 실패 감지 및 자동 리셋을 통해 휴머노이드 학생을 지지하고 안내하여 최소한의 인간 개입으로 효율적인 실제 세계 강화 학습을 가능하게 하는 Robot-Trains-Robot(RTR)
    프레임워크를 제안한다. 저자들은 또한 FiLM 레이어와 도메인 랜덤화를 사용하여 시뮬레이션에서 실제로의 전이를 안정화하는 동역학 인식 잠재 변수 최적화 파이프라인을 소개하고, ToddlerBot 휴머노이드에서 보행
    속도 추적 미세 조정 및 처음부터의 스윙업 학습을 입증한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- reinforcement_learning
- sim_to_real
- humanoid_locomotion
- real_world_rl
- robot_teacher
- curriculum_learning
- automatic_reset
- ppo
- film_layer
- domain_randomization
- toddlerbot
- ur5
- force_torque_sensor
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.12252v2.
sources:
- id: src_001
  type: paper
  title: 'Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids'
  url: https://arxiv.org/abs/2508.12252
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Simulation-based reinforcement learning (RL) has significantly advanced humanoid locomotion tasks, yet direct real-world RL from scratch or adapting from pretrained policies remains rare, limiting the full potential of humanoid robots. Real-world learning, despite being crucial for overcoming the sim-to-real gap, faces substantial challenges related to safety, reward design, and learning efficiency. To address these limitations, we propose Robot-Trains-Robot (RTR), a novel framework where a robotic arm teacher actively supports and guides a humanoid robot student. The RTR system provides protection, learning schedule, reward, perturbation, failure detection, and automatic resets. It enables efficient long-term real-world humanoid training with minimal human intervention. Furthermore, we propose a novel RL pipeline that facilitates and stabilizes sim-to-real transfer by optimizing a single dynamics-encoded latent variable in the real world. We validate our method through two challenging real-world humanoid tasks: fine-tuning a walking policy for precise speed tracking and learning a humanoid swing-up task from scratch, illustrating the promising capabilities of real-world humanoid learning realized by RTR-style systems. See https://robot-trains-robot.github.io/ for more info.

## 核心内容
Simulation-based reinforcement learning (RL) has significantly advanced humanoid locomotion tasks, yet direct real-world RL from scratch or adapting from pretrained policies remains rare, limiting the full potential of humanoid robots. Real-world learning, despite being crucial for overcoming the sim-to-real gap, faces substantial challenges related to safety, reward design, and learning efficiency. To address these limitations, we propose Robot-Trains-Robot (RTR), a novel framework where a robotic arm teacher actively supports and guides a humanoid robot student. The RTR system provides protection, learning schedule, reward, perturbation, failure detection, and automatic resets. It enables efficient long-term real-world humanoid training with minimal human intervention. Furthermore, we propose a novel RL pipeline that facilitates and stabilizes sim-to-real transfer by optimizing a single dynamics-encoded latent variable in the real world. We validate our method through two challenging real-world humanoid tasks: fine-tuning a walking policy for precise speed tracking and learning a humanoid swing-up task from scratch, illustrating the promising capabilities of real-world humanoid learning realized by RTR-style systems. See https://robot-trains-robot.github.io/ for more info.

## 参考
- http://arxiv.org/abs/2508.12252v2

