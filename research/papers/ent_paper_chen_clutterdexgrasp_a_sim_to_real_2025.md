---
$id: ent_paper_chen_clutterdexgrasp_a_sim_to_real_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes'
  zh: ClutterDexGrasp
  ko: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes'
summary:
  en: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (ClutterDexGrasp), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Duke University, and published at CoRL25.'
  zh: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (ClutterDexGrasp), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Duke University, and published at CoRL25.'
  ko: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (ClutterDexGrasp), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Duke University, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clutterdexgrasp
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.14317v3.
sources:
- id: src_001
  type: paper
  title: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (arXiv)'
  url: https://arxiv.org/abs/2506.14317
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ClutterDexGrasp source
  url: https://doi.org/10.48550/arXiv.2506.14317
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## 核心内容
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## 参考
- http://arxiv.org/abs/2506.14317v3

## Overview
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## Content
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## 개요
혼잡한 장면에서의 정밀 파지(Dexterous grasping)는 다양한 물체 형상, 가려짐, 잠재적 충돌로 인해 상당한 어려움을 제기합니다. 기존 방법은 주로 단일 물체 파지 또는 상호작용 없는 파지 자세 예측에 초점을 맞추고 있어 복잡하고 혼잡한 장면에는 부적합합니다. 최근의 시각-언어-행동 모델은 잠재적 해결책을 제공하지만, 광범위한 실제 시연이 필요하여 비용이 많이 들고 확장이 어렵습니다. 이러한 한계를 해결하기 위해, 우리는 시뮬레이션-실제 전송 파이프라인을 재검토하고 강력한 일반화를 유지하면서 실제 환경에서 제로샷 배포를 가능하게 하는 핵심 기술을 개발합니다. 우리는 혼잡한 장면에서 폐쇄 루프 목표 지향 정밀 파지를 위한 2단계 교사-학생 프레임워크인 ClutterDexGrasp를 제안합니다. 이 프레임워크는 혼잡 밀도 커리큘럼 학습을 사용하여 시뮬레이션에서 훈련된 교사 정책을 특징으로 하며, 기하학 및 공간 임베디드 장면 표현과 새로운 포괄적 안전 커리큘럼을 통합하여 일반적이고 동적이며 안전한 파지 행동을 가능하게 합니다. 모방 학습을 통해, 우리는 교사의 지식을 부분 포인트 클라우드 관찰에서 작동하는 학생 3D 확산 정책(DP3)으로 증류합니다. 우리가 아는 한, 이는 혼잡한 장면에서 목표 지향 정밀 파지를 위한 최초의 제로샷 시뮬레이션-실제 폐쇄 루프 시스템으로, 다양한 물체와 배치에서 강력한 성능을 입증합니다. 더 자세한 내용과 비디오는 https://clutterdexgrasp.github.io/에서 확인할 수 있습니다.

## 핵심 내용
혼잡한 장면에서의 정밀 파지는 다양한 물체 형상, 가려짐, 잠재적 충돌로 인해 상당한 어려움을 제기합니다. 기존 방법은 주로 단일 물체 파지 또는 상호작용 없는 파지 자세 예측에 초점을 맞추고 있어 복잡하고 혼잡한 장면에는 부적합합니다. 최근의 시각-언어-행동 모델은 잠재적 해결책을 제공하지만, 광범위한 실제 시연이 필요하여 비용이 많이 들고 확장이 어렵습니다. 이러한 한계를 해결하기 위해, 우리는 시뮬레이션-실제 전송 파이프라인을 재검토하고 강력한 일반화를 유지하면서 실제 환경에서 제로샷 배포를 가능하게 하는 핵심 기술을 개발합니다. 우리는 혼잡한 장면에서 폐쇄 루프 목표 지향 정밀 파지를 위한 2단계 교사-학생 프레임워크인 ClutterDexGrasp를 제안합니다. 이 프레임워크는 혼잡 밀도 커리큘럼 학습을 사용하여 시뮬레이션에서 훈련된 교사 정책을 특징으로 하며, 기하학 및 공간 임베디드 장면 표현과 새로운 포괄적 안전 커리큘럼을 통합하여 일반적이고 동적이며 안전한 파지 행동을 가능하게 합니다. 모방 학습을 통해, 우리는 교사의 지식을 부분 포인트 클라우드 관찰에서 작동하는 학생 3D 확산 정책(DP3)으로 증류합니다. 우리가 아는 한, 이는 혼잡한 장면에서 목표 지향 정밀 파지를 위한 최초의 제로샷 시뮬레이션-실제 폐쇄 루프 시스템으로, 다양한 물체와 배치에서 강력한 성능을 입증합니다. 더 자세한 내용과 비디오는 https://clutterdexgrasp.github.io/에서 확인할 수 있습니다.
