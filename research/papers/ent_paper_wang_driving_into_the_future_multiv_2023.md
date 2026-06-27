---
$id: ent_paper_wang_driving_into_the_future_multiv_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Drive-WM: Driving into the Future: Multiview Visual Forecasting and Planning
    with World Model for Autonomous Driving'
  zh: Drive-WM：面向自动驾驶的多视角视觉预测与世界模型规划
  ko: 'Drive-WM: 자율주행을 위한 다중 시각 예측 및 세계 모델 기반 계획'
summary:
  en: Drive-WM is a latent video diffusion world model for autonomous driving that
    generates high-fidelity multi-view videos through view-factorized spatial-temporal
    modeling, supports unified conditioning from images, text, layouts, and ego actions,
    and is applied to tree-based trajectory planning with image-based rewards.
  zh: Drive-WM是一个用于自动驾驶的隐式视频扩散世界模型，通过视图分解的时空建模生成高保真多视角视频，支持来自图像、文本、布局和自车动作的统一条件输入，并应用于基于图像奖励的树状轨迹规划。
  ko: Drive-WM은 자율주행을 위한 잠재 비디오 확산 세계 모델로, 뷰 분해를 통한 시공간 모델링으로 고화질 다중 뷰 영상을 생성하고 이미지,
    텍스트, 레이아웃, 자차 행동 등의 통합 조건 입력을 지원하며, 이미지 기반 보상을 이용한 트리 기반 궤적 계획에 적용되었다.
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
- world_model
- video_diffusion
- multiview_forecasting
- view_factorization
- trajectory_planning
- safety_planning
- autonomous_driving
- image_based_rewards
- ood_simulation
- latent_diffusion
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text verification
    not performed. Requires human review before final verification.
sources:
- id: src_001
  type: paper
  title: 'Driving into the Future: Multiview Visual Forecasting and Planning with
    World Model for Autonomous Driving'
  url: https://arxiv.org/abs/2311.17918
  date: '2023'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---


## Overview

Drive-WM addresses the challenge that end-to-end autonomous driving planners can fail when encountering out-of-distribution states, such as the ego vehicle being laterally off the lane center. The authors propose a latent video diffusion world model that jointly models spatial-temporal multi-view driving data and generates high-fidelity, controllable multi-view videos. A view factorization mechanism is introduced to improve cross-view consistency, and a unified condition interface integrates heterogeneous inputs including images, text, 3D bounding boxes, bird's-eye-view maps, and ego actions.

The model is designed to be compatible with existing end-to-end planning models. Beyond generation, Drive-WM is applied to safe driving planning by branching into multiple future trajectories corresponding to distinct driving maneuvers and selecting the optimal one using image-based rewards. Evaluation is conducted on the nuScenes and Waymo Open datasets, where the authors report high-quality, consistent, and controllable multi-view video generation.

The work positions the world model as a predictive simulator that can foresee consequences of planned actions, thereby improving planning soundness and robustness to out-of-distribution scenarios.

## Key Contributions

- First driving world model that generates high-fidelity, controllable, and consistent multi-view videos.
- View factorization approach that significantly improves multi-view consistency.
- Unified condition interface integrating images, text, 3D boxes, BEV maps, and ego actions.
- First exploration of applying a world model to end-to-end autonomous driving planning, improving planning soundness and out-of-distribution robustness.
- Proposed keypoint matching (KPM) metric for quantifying multi-view consistency.

## Relevance to Humanoid Robotics

Although Drive-WM is developed and evaluated in the autonomous driving domain, its core methodology—multi-view visual forecasting, generative world modeling, and safety-aware planning—offers transferable value for humanoid robotics. Humanoid robots operating in unstructured human environments must similarly predict future states, evaluate risks, and select safe motions from rich visual input.

The view-factorized diffusion approach and unified conditioning interface could inspire analogous perception and planning systems for humanoids, particularly for out-of-distribution simulation and deployment robustness. However, direct transfer remains speculative and would require substantial adaptation to embodied humanoid sensing and action spaces.
