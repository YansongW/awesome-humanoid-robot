---
$id: ent_paper_chae_multi_robot_motion_planning_fr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Multi-Robot Motion Planning from Vision and Language using Heat-inspired Diffusion
  zh: 基于热启发扩散的视觉语言多机器人运动规划
  ko: 열 확산에 영감을 받은 비전 및 언어 기반 다중 로봇 동작 계획
summary:
  en: Language-conditioned Heat-inspired Diffusion (LHD) is an end-to-end vision-language
    planner that generates collision-free multi-robot trajectories from a raw RGB
    image and natural-language instructions, using a heat-equation diffusion kernel
    to amortize static obstacle avoidance into training and a lightweight inter-robot
    guidance term for safe coordination.
  zh: 语言条件热启发扩散（LHD）是一种端到端视觉语言规划器，仅利用原始RGB图像和自然语言指令生成无碰撞的多机器人轨迹；它通过热方程扩散核将静态避障成本摊入训练阶段，并采用轻量级机器人间引导项实现安全协调。
  ko: 언어 조건 열 영감 확산(LHD)은 원시 RGB 이미지와 자연어 명령만으로 충돌 없는 다중 로봇 궤적을 생성하는 종단형 비전-언어 플래너로,
    열 방정식 확산 커널로 정적 장애물 회피 비용을 학습 단계에 분산시키고 가벼운 로봇 간 안내 항으로 안전한 협응을 실현한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_motion_planning
- vision_language_planning
- diffusion_policy
- collision_avoidance
- clip
- heat_equation
- language_conditioned
- trajectory_generation
- motion_planning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the published IEEE RA-L preprint (arXiv:2512.13090); hardware
    details and quantitative claims require human review before full verification.
sources:
- id: src_001
  type: paper
  title: Multi-Robot Motion Planning from Vision and Language using Heat-inspired
    Diffusion
  url: https://arxiv.org/abs/2512.13090
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Multi-robot motion planning (MRMP) traditionally requires explicit goal coordinates and environment representations, making it cumbersome for human-centric settings such as warehouses. Chae et al. address this by proposing Language-conditioned Heat-inspired Diffusion (LHD), an end-to-end framework that consumes a raw RGB top-down view of the workspace together with a natural-language instruction for each robot and outputs collision-free trajectories. The key insight is to replace the Gaussian diffusion kernel with a collision-avoiding heat-equation kernel that treats obstacles as perfect thermal insulators; this bakes geometric reachability into the forward diffusion process so that unreachable regions are excluded from the learned distribution. At inference, Langevin dynamics generate intermediate trajectory waypoints that progressively approach the goal while a lightweight distance-based guidance term enforces inter-robot safety margins.

## Key Contributions

- Introduction of LHD, an end-to-end vision-language diffusion planner for multi-robot trajectory generation.
- A collision-avoiding diffusion kernel that grounds language instructions to reachable regions by amortizing static obstacle avoidance into the training phase.
- A lightweight inter-robot guidance term that augments the reverse diffusion sampling process with inter-robot collision costs.
- Empirical demonstration on four real-world-inspired maps and on real TurtleBot3 hardware, showing higher success rates, OOD reachability generalization, and orders-of-magnitude lower planning latency than prior diffusion-based planners.

## Relevance to Humanoid Robotics

The current experiments use wheeled TurtleBot3 robots in a 2D workspace, but the authors explicitly identify extension to 3D heat transfer for high-DoF systems such as multiple mobile manipulators or humanoids as future work. If realized, the same vision-language conditioning and heat-inspired reachability prior could support coordinated fleet motion planning for humanoid robots from natural language and RGB observations, reducing reliance on explicit environment maps. Until that extension is demonstrated, the relevance to humanoids remains prospective rather than proven.
