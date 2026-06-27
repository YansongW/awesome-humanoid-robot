---
$id: ent_paper_saund_clasp_constrained_latent_shape_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLASP: Constrained Latent Shape Projection for Refining Object Shape from Robot
    Contact'
  zh: CLASP：基于机器人接触的约束潜在形状投影以细化物体形状
  ko: 'CLASP: 로봇 접촉을 이용한 물체 형상 정제를 위한 제약 잠재 형상 투영'
summary:
  en: CLASP fuses RGB-D shape-completion priors with binary robot contact observations
    by maintaining a particle filter in the latent space of a variational shape network
    and projecting particles onto the contact manifold, consistently reducing Chamfer
    distance to ground-truth scenes.
  zh: CLASP 通过在变分形状网络的潜在空间中维护粒子滤波器，并将粒子投影到接触流形上，融合 RGB-D 形状补全先验与二值机器人接触观测，持续降低预测场景与真实场景之间的
    Chamfer 距离。
  ko: CLASP는 변분 형상 네트워크의 잠재 공간에서 입자 필터를 유지하고 입자를 접촉 다양체로 투영함으로써 RGB-D 형상 완성 사전 정보와
    이진 로봇 접촉 관측을 융합하여 예측 장면과 실제 장면 간 Chamfer 거리를 지속적으로 줄인다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- shape_completion
- contact_sensing
- rgbd_contact_fusion
- latent_shape_projection
- particle_filter
- object_state_estimation
- manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; requires human review
    against the full arXiv PDF before full verification.
sources:
- id: src_001
  type: paper
  title: 'CLASP: Constrained Latent Shape Projection for Refining Object Shape from
    Robot Contact'
  url: https://arxiv.org/abs/2110.08719
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Robots that manipulate objects in cluttered, unstructured environments must estimate object geometry from partial and noisy RGB-D data. While shape-completion networks can provide strong shape priors that fill occlusions and reduce sensor noise, they do not naturally explain unexpected contact events. CLASP addresses this gap by combining a variational shape-completion network, PSSNet, with a constrained optimization procedure in latent space.

The core idea is to represent the belief over object shapes as a particle filter in the latent space of the shape-completion network. Each particle is a latent vector that can be decoded into a full 3D shape. When the robot detects contact or free-space observations, CLASP projects each latent particle via iterative gradient descent so that the decoded shape satisfies contact and free-space constraints while remaining likely under the RGB-D prior. This projection effectively moves shape hypotheses onto the contact manifold.

The system was evaluated both in simulation and on a physical Kuka iiwa arm equipped with a Robotiq 3-finger gripper and a Kinect depth camera, using Axis-Aligned Boxes (AAB), YCB objects, and ShapeNet mugs. Results show that CLASP consistently reduces Chamfer distance between predicted and ground-truth scenes, whereas baseline approaches do not benefit from contact information.

## Key Contributions

- Latent-space projection of shape samples onto the contact manifold using gradient descent with free-space, contact, and prior loss terms.
- Particle-filter belief representation that combines RGB-D shape-completion priors with robot contact and free-space observations.
- Multi-object contact assignment strategy that resolves ambiguous contacts without assigning a single contact to multiple objects.
- Simulation and live-robot experiments demonstrating consistent Chamfer-distance reduction compared to ablations and baselines.

## Relevance to Humanoid Robotics

Accurate, real-time object shape estimation from vision and contact is a fundamental capability for humanoid robots that must navigate and manipulate in unstructured environments. CLASP's framework for fusing visual shape priors with physical contact directly supports safer, more robust manipulation on humanoid platforms.

The paper itself demonstrates the approach on a fixed dual-arm manipulator rather than a bipedal humanoid, so its humanoid relevance is indirect. However, the underlying method is platform-agnostic: it assumes only an RGB-D sensor, a robot arm, and binary contact detection, all of which are available on typical humanoid systems. Consequently, CLASP can be adopted as a perception component for humanoid manipulation pipelines.
