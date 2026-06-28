---
$id: ent_paper_chen_aispo_enhancing_depth_reliabil_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian
    Objects via Affine-Invariant Shape Prior'
  zh: AISPO：基于仿射不变形状先验的非朗伯物体机器人操作深度可靠性增强
  ko: 'AISPO: 아핀 불변 형상 사전을 활용한 비람베르티안 객체 로봇 조작을 위한 깊이 신뢰성 강화'
summary:
  en: AISPO is a depth completion framework that fuses multi-scale RGB-D features
    with an affine-invariant shape prior to improve depth reliability for robotic
    manipulation of transparent and specular objects.
  zh: AISPO是一个深度补全框架，通过融合多尺度RGB-D特征与仿射不变形状先验，提升透明及高反光非朗伯物体机器人操作时的深度可靠性。
  ko: AISPO는 다중 스케일 RGB-D 특징과 아핀 불변 형상 사전을 융합하여 투명하거나 반사성이 강한 비람베르티안 객체의 로봇 조작을 위한
    깊이 신뢰성을 향상시키는 깊이 완성 프레임워크이다.
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
- depth_completion
- rgb_d_fusion
- non_lambertian_objects
- transparent_objects
- specular_objects
- robotic_grasping
- affine_invariant_shape_prior
- vision_transformer
- perception
- synthetic_training
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata (abstract, method summary, and dataset
    lists); requires human review against the full paper before full verification.
sources:
- id: src_001
  type: paper
  title: 'AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian
    Objects via Affine-Invariant Shape Prior'
  url: https://arxiv.org/abs/2606.25503
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Reliable depth perception is fundamental to robotic manipulation, yet conventional depth sensors frequently fail on non-Lambertian surfaces such as transparent containers, glassware, and specular metallic objects. These failures produce corrupted or missing depth measurements that propagate downstream to motion planning, resulting in invalid grasp poses and execution errors during manipulation tasks.

To address this problem, the authors propose AISPO, a depth completion framework that combines multi-scale RGB-D feature fusion with an affine-invariant shape prior. A frozen vision-transformer-based autoencoder extracts the shape prior, which is then integrated through cross-attention hierarchical fusion modules and decoded by a DPT-style decoder. The network is trained in two stages using synthetic data to enforce geometric consistency and reduce catastrophic depth failures.

AISPO is evaluated on multiple benchmarks covering both known and novel object categories, and validated through real-world grasping experiments with a Franka robotic arm. The results show competitive benchmark performance, strong generalization to unseen objects and scenes, and significant improvements in manipulation success rates—especially for transparent objects where many prior methods fail to produce physically usable depth estimates.

## Key Contributions

- A depth completion framework that fuses multi-scale RGB-D features with an affine-invariant shape prior to improve depth reliability for non-Lambertian objects.
- A ViT-based shape-prior autoencoder and a two-stage training strategy designed to enforce structural regularity and mitigate catastrophic depth failures.
- Extensive benchmark evaluations and real-world robotic grasping experiments demonstrating improved manipulation success, particularly on transparent objects.

## Relevance to Humanoid Robotics

Humanoid robots operating in unstructured human environments must handle a wide variety of common household and industrial objects, many of which are transparent, reflective, or otherwise non-Lambertian. AISPO's emphasis on physically plausible and structurally intact depth maps directly supports robust perception-driven grasp planning in these scenarios.

By improving depth reliability for transparent and specular objects, the framework reduces invalid grasp poses and execution errors, enabling more scalable and dependable manipulation behavior for humanoid systems deployed in real-world settings.
