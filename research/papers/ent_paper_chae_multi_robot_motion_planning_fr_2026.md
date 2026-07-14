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
  en: Language-conditioned Heat-inspired Diffusion (LHD) is an end-to-end vision-language planner that generates collision-free
    multi-robot trajectories from a raw RGB image and natural-language instructions, using a heat-equation diffusion kernel
    to amortize static obstacle avoidance into training and a lightweight inter-robot guidance term for safe coordination.
  zh: 语言条件热启发扩散（LHD）是一种端到端视觉语言规划器，仅利用原始RGB图像和自然语言指令生成无碰撞的多机器人轨迹；它通过热方程扩散核将静态避障成本摊入训练阶段，并采用轻量级机器人间引导项实现安全协调。
  ko: 언어 조건 열 영감 확산(LHD)은 원시 RGB 이미지와 자연어 명령만으로 충돌 없는 다중 로봇 궤적을 생성하는 종단형 비전-언어 플래너로, 열 방정식 확산 커널로 정적 장애물 회피 비용을 학습 단계에 분산시키고
    가벼운 로봇 간 안내 항으로 안전한 협응을 실현한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13090v2.
sources:
- id: src_001
  type: paper
  title: Multi-Robot Motion Planning from Vision and Language using Heat-inspired Diffusion
  url: https://arxiv.org/abs/2512.13090
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-conditioned Heat-inspired Diffusion (LHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LHD integrates semantic priors from CLIP, a vision-language model (VLM), with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution (OOD) scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency. Project page is available at: https://jebeom.github.io/lhd_project_page/

## 核心内容
Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-conditioned Heat-inspired Diffusion (LHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LHD integrates semantic priors from CLIP, a vision-language model (VLM), with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution (OOD) scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency. Project page is available at: https://jebeom.github.io/lhd_project_page/

## 参考
- http://arxiv.org/abs/2512.13090v2

