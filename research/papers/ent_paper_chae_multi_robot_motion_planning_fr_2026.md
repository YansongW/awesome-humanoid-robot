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

## Overview
Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-conditioned Heat-inspired Diffusion (LHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LHD integrates semantic priors from CLIP, a vision-language model (VLM), with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution (OOD) scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency. Project page is available at: https://jebeom.github.io/lhd_project_page/

## Content
Diffusion models have recently emerged as powerful tools for robot motion planning by capturing the multi-modal distribution of feasible trajectories. However, their extension to multi-robot settings with flexible, language-conditioned task specifications remains limited. Furthermore, current diffusion-based approaches incur high computational cost during inference and struggle with generalization because they require explicit construction of environment representations and lack mechanisms for reasoning about geometric reachability. To address these limitations, we present Language-conditioned Heat-inspired Diffusion (LHD), an end-to-end vision-based framework that generates language-conditioned, collision-free trajectories. LHD integrates semantic priors from CLIP, a vision-language model (VLM), with a collision-avoiding diffusion kernel serving as a physical inductive bias that enables the planner to interpret language commands strictly within the reachable workspace. This naturally handles out-of-distribution (OOD) scenarios -- in terms of reachability -- by guiding robots toward accessible alternatives that match the semantic intent, while eliminating the need for explicit obstacle information at inference time. Extensive evaluations on diverse real-world-inspired maps, along with real-robot experiments, show that LHD consistently outperforms prior diffusion-based planners in success rate, while reducing planning latency. Project page is available at: https://jebeom.github.io/lhd_project_page/

## 개요
확산 모델은 최근 실행 가능한 궤적의 다중 모드 분포를 포착하여 로봇 동작 계획을 위한 강력한 도구로 부상했습니다. 그러나 유연하고 언어로 조건화된 작업 사양을 갖춘 다중 로봇 환경으로의 확장은 여전히 제한적입니다. 또한, 현재의 확산 기반 접근 방식은 환경 표현의 명시적 구성을 필요로 하고 기하학적 도달 가능성에 대한 추론 메커니즘이 부족하여 추론 시 높은 계산 비용이 발생하고 일반화에 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 언어 조건화된 열 기반 확산(LHD)을 제시합니다. 이는 언어로 조건화되고 충돌 없는 궤적을 생성하는 엔드투엔드 비전 기반 프레임워크입니다. LHD는 CLIP(시각-언어 모델, VLM)의 의미론적 사전 지식을 충돌 회피 확산 커널과 통합합니다. 이 커널은 물리적 귀납적 편향으로 작용하여 계획자가 도달 가능한 작업 공간 내에서만 언어 명령을 해석할 수 있게 합니다. 이는 의미론적 의도와 일치하는 접근 가능한 대안으로 로봇을 안내함으로써 도달 가능성 측면에서 분포 외(OOD) 시나리오를 자연스럽게 처리하며, 추론 시 명시적 장애물 정보의 필요성을 제거합니다. 다양한 실제 세계에서 영감을 받은 지도와 실제 로봇 실험에 대한 광범위한 평가는 LHD가 계획 지연 시간을 줄이면서 성공률에서 이전 확산 기반 계획자를 일관되게 능가함을 보여줍니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://jebeom.github.io/lhd_project_page/

## 핵심 내용
확산 모델은 최근 실행 가능한 궤적의 다중 모드 분포를 포착하여 로봇 동작 계획을 위한 강력한 도구로 부상했습니다. 그러나 유연하고 언어로 조건화된 작업 사양을 갖춘 다중 로봇 환경으로의 확장은 여전히 제한적입니다. 또한, 현재의 확산 기반 접근 방식은 환경 표현의 명시적 구성을 필요로 하고 기하학적 도달 가능성에 대한 추론 메커니즘이 부족하여 추론 시 높은 계산 비용이 발생하고 일반화에 어려움을 겪습니다. 이러한 한계를 해결하기 위해, 우리는 언어 조건화된 열 기반 확산(LHD)을 제시합니다. 이는 언어로 조건화되고 충돌 없는 궤적을 생성하는 엔드투엔드 비전 기반 프레임워크입니다. LHD는 CLIP(시각-언어 모델, VLM)의 의미론적 사전 지식을 충돌 회피 확산 커널과 통합합니다. 이 커널은 물리적 귀납적 편향으로 작용하여 계획자가 도달 가능한 작업 공간 내에서만 언어 명령을 해석할 수 있게 합니다. 이는 의미론적 의도와 일치하는 접근 가능한 대안으로 로봇을 안내함으로써 도달 가능성 측면에서 분포 외(OOD) 시나리오를 자연스럽게 처리하며, 추론 시 명시적 장애물 정보의 필요성을 제거합니다. 다양한 실제 세계에서 영감을 받은 지도와 실제 로봇 실험에 대한 광범위한 평가는 LHD가 계획 지연 시간을 줄이면서 성공률에서 이전 확산 기반 계획자를 일관되게 능가함을 보여줍니다. 프로젝트 페이지는 다음에서 확인할 수 있습니다: https://jebeom.github.io/lhd_project_page/
