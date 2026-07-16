---
$id: ent_paper_mishra_artitwinsplat_interactable_dig_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting
    from RGB-D videos'
  zh: ArtiTwinSplat：基于RGB-D视频的高斯溅射可交互数字孪生重建
  ko: 'ArtiTwinSplat: RGB-D 비디오에서 가우시안 스플래팅을 통한 상호작용 가능한 디지털 트윈 재구성'
summary:
  en: ArtiTwinSplat reconstructs articulated, photo-realistic digital twins from RGB-D
    videos without CAD models or manual annotations, using 3D Gaussian Splatting and
    unsupervised articulation discovery to produce URDF models for robot simulation.
  zh: ArtiTwinSplat 无需 CAD 模型或人工标注，直接从 RGB-D 视频重建可关节运动、照片级真实的数字孪生，利用 3D 高斯溅射与无监督关节发现生成可用于机器人仿真的
    URDF 模型。
  ko: ArtiTwinSplat은 CAD 모델이나 수동 주석 없이 RGB-D 비디오로부터 관절형 사실적 디지털 트윈을 재구성하며, 3D 가우시안
    스플래팅과 비지도식 관절 발견을 통해 로봇 시뮬레이션용 URDF 모델을 생성한다.
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
- gaussian_splatting
- digital_twin
- articulated_object_reconstruction
- rgb_d_reconstruction
- articulation_discovery
- sim_to_real
- urdf_export
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from arXiv abstract and provided metadata; full-text review
    needed before verification.
sources:
- id: src_001
  type: paper
  title: 'ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting
    from RGB-D videos'
  url: https://arxiv.org/abs/2606.24628
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

ArtiTwinSplat is a fully automatic pipeline that constructs articulated, photo-realistic digital twins of objects directly from RGB-D videos. It requires no CAD models, simulation assets, or manual annotations, and instead relies on 3D Gaussian Splatting for geometric and photometric fidelity, paired with an unsupervised articulation-discovery stage that recovers part structure and joint kinematics from observed motion alone.

The reconstruction process couples tracking and optimization stages. Articulation is discovered by analyzing appearance changes and using reverse-time SAM2 tracking. Joint parameters are estimated from TAPIP3D correspondences through 4D RANSAC, and the final model is optimized as a joint-conditioned articulated 3D Gaussian Splatting representation. The resulting digital twin supports real-time rendering, viewpoint control, and interactive manipulation at arbitrary joint configurations.

The paper emphasizes operation on real-world observations rather than synthetic scenes. Reconstructed models can be exported directly as URDFs and used in NVIDIA Isaac Sim, providing a practical bridge from casual RGB-D capture to downstream robot planning and learning systems.

## Key Contributions

- Annotation-free automatic articulation discovery that detects parts and recovers joint type, axis, pivot, and range of motion from RGB-D video.
- Joint-conditioned two-phase Gaussian optimization that enforces physically consistent part motion while maintaining global scene appearance.
- Direct export of reconstructed articulated models as URDFs compatible with NVIDIA Isaac Sim for sim-to-real robotic workflows.
- Real-time rendering and interactive manipulation of articulated digital twins at arbitrary joint configurations.

## Relevance to Humanoid Robotics

The work is explicitly motivated by robot deployment in unstructured real-world environments and targets downstream robot planning, learning, and human-robot collaboration. By lowering the barrier between real-world capture and simulation-ready articulated object models, it is directly relevant to humanoid manipulation pipelines that need interactive object models.

The URDF export to NVIDIA Isaac Sim supports sim-to-real transfer, a common need in humanoid control and learning. The use of commodity RGB-D capture (Apple iPhone Pro with Record3D) further suggests a scalable pathway for building object-level digital twins for embodied AI systems, including humanoid robots operating in everyday environments.
