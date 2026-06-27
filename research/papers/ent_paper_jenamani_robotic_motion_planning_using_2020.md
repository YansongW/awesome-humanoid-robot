---
$id: ent_paper_jenamani_robotic_motion_planning_using_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotic Motion Planning using Learned Critical Sources and Local Sampling
  zh: 基于学习临界源与局部采样的机器人运动规划
  ko: 학습된 임계점 소스와 국부 샘플링을 활용한 로봇 동작 계획
summary:
  en: Proposes GenerateCriticalSources, LCS-RRT, and CS-RRT, which preprocess a low-resolution
    occupancy grid with a kernel, train a conditional VAE (LEGO-Global) to emit one
    critical source per bottleneck region, and then use local RRTs to maintain probabilistic
    completeness in R2 and R7 motion-planning problems.
  zh: 提出GenerateCriticalSources、LCS-RRT与CS-RRT方法：以核对低分辨率占用栅格进行预处理，训练条件变分自编码器（LEGO-Global）为每个瓶颈区域生成一个临界源，再通过局部RRT在R2与R7运动规划问题中保持概率完备性。
  ko: 커널로 저해상도 점유 그리드를 전처리하고 조건부 변분 오토인코더(LEGO-Global)를 훈련해 각 병목 영역당 하나의 임계점 소스를 생성한
    뒤, 국부 RRT를 활용해 R2 및 R7 동작 계획 문제에서 확률적 완전성을 유지하는 GenerateCriticalSources, LCS-RRT,
    CS-RRT를 제안한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
- foundations
functional_roles:
- knowledge
- intelligence
tags:
- motion_planning
- sampling_based_planning
- rrt
- learned_sampler
- bottleneck_regions
- critical_sources
- conditional_vae
- occupancy_grid
- manipulation_planning
- high_dof
- probabilistic_completeness
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv PDF; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Robotic Motion Planning using Learned Critical Sources and Local Sampling
  url: https://arxiv.org/abs/2006.04194
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Sampling-based motion planning (SBMP) algorithms build a graph or roadmap to represent a robot's state space, but uniform samplers struggle in constrained environments with narrow passages (bottleneck regions). Recent learning-based methods address this by training a model to predict critical samples inside bottleneck regions, yet they require the learner to capture fine local geometry, which becomes data- and time-intensive as problem complexity grows. This paper argues that the learner only needs to identify the global location of each bottleneck region, after which local planners can explore the local structure.

To implement this insight, the authors preprocess a low-resolution occupancy grid with a kernel to discard local detail and train a conditional variational autoencoder (LEGO-Global) to generate one critical source per bottleneck region. They then present GenerateCriticalSources for producing these sources, Local Critical Source-RRT (LCS-RRT) for bridging disconnected components of a sparse graph via local RRTs rooted at critical sources, and Critical Source-RRT (CS-RRT) for incrementally building RRTs rooted at start, goal, and critical sources without a sparse graph. Both algorithms retain probabilistic completeness and are evaluated on R2 point-object problems and R7 robotic-arm manipulation problems.

## Key Contributions

- GenerateCriticalSources: a fast learner-based method that preprocesses an occupancy grid with a kernel and uses a conditional VAE (LEGO-Global) to generate one critical source per bottleneck region.
- Local Critical Source-RRT (LCS-RRT): an algorithm that combines a sparse graph with RRTs rooted at critical sources to bridge disconnected sub-graphs through bottleneck regions.
- Critical Source-RRT (CS-RRT): an incremental tree-based algorithm that grows RRTs from start, goal, and critical sources without requiring a sparse graph.
- Probabilistic-completeness proofs for LCS-RRT and CS-RRT, together with empirical speedups over RRT-Connect and LEGO on R2 and R7 planning problems.
- Kernel-based occupancy-grid preprocessing that lets the learner focus on global bottleneck locations rather than local structure.

## Relevance to Humanoid Robotics

Efficient sampling-based planning for high-dimensional manipulators in cluttered environments is a core building block for humanoid whole-body motion generation and manipulation. By separating global bottleneck detection from local geometry exploration, the proposed approach can reduce planning latency and improve success rates in tasks such as reaching through narrow gaps or navigating cluttered workspaces, directly affecting the deployment speed and robustness of humanoid robots.

The method is limited to geometric planning without differential constraints or dynamic environments, and it assumes a dataset of similar prior problems for training the learner. Nevertheless, the combination of learned global guidance with probabilistically complete local sampling provides a practical template for scaling motion-planning backends in humanoid systems.
