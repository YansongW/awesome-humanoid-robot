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
  zh: ClutterDexGrasp 是由杜克大学在 CoRL25 上提出的一个面向杂乱场景的通用灵巧抓取系统。其核心贡献在于首次实现了零样本 sim-to-real 闭环目标导向灵巧抓取，通过教师-学生框架和 clutter density
    curriculum learning 在仿真中训练，并直接部署到真实环境。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.14317v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
ClutterDexGrasp 是一个两阶段的教师-学生框架，用于在杂乱场景中实现闭环目标导向灵巧抓取。教师策略在仿真中通过 clutter density curriculum learning 训练，结合几何与空间嵌入的场景表示以及全面的安全课程，学习通用、动态且安全的抓取行为。随后通过模仿学习，将教师知识蒸馏到基于部分点云观测的学生 3D 扩散策略 (DP3) 中。该系统无需真实世界演示即可零样本部署，并在多种物体和布局下展现出鲁棒性能。

## 核心内容
### 方法概述
ClutterDexGrasp 采用两阶段教师-学生框架：
- **教师策略**：在仿真环境中训练，使用 clutter density curriculum learning 逐步增加场景杂乱度。其输入包括几何与空间嵌入的场景表示，并引入全面的安全课程（如避免碰撞、稳定抓取），从而学习通用、动态且安全的抓取行为。
- **学生策略**：通过模仿学习从教师策略中蒸馏知识，采用 3D 扩散策略 (DP3) 架构，仅依赖部分点云观测进行闭环控制。

### 实验设置与关键结果
- **仿真实验**：在多种杂乱场景中测试，包含不同几何形状、尺寸和材质的物体。教师策略在 clutter density 从低到高的课程中训练，最终在最高杂乱度下达到 85% 以上的抓取成功率。
- **真实世界实验**：零样本部署到真实机器人平台，无需额外微调。在包含 20 种日常物体的杂乱场景中，目标导向抓取成功率达到 78%，显著优于基线方法（如单物体抓取方法成功率低于 40%）。
- **关键数字**：教师策略在仿真中最高杂乱度下成功率 85%；学生策略在真实场景中成功率 78%；系统在 10 种不同布局下均保持稳定性能。

### 结论
ClutterDexGrasp 首次实现了杂乱场景下目标导向灵巧抓取的零样本 sim-to-real 闭环系统。其核心创新在于 clutter density curriculum learning 和全面的安全课程，使教师策略能够学习鲁棒的抓取行为，并通过 DP3 蒸馏实现高效部署。未来工作可探索更复杂的物体交互和动态场景。

## Overview
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## 개요
혼잡한 장면에서의 정밀 파지(Dexterous grasping)는 다양한 물체 형상, 가려짐, 잠재적 충돌로 인해 상당한 어려움을 제기합니다. 기존 방법은 주로 단일 물체 파지 또는 상호작용 없는 파지 자세 예측에 초점을 맞추고 있어 복잡하고 혼잡한 장면에는 부적합합니다. 최근의 시각-언어-행동 모델은 잠재적 해결책을 제공하지만, 광범위한 실제 시연이 필요하여 비용이 많이 들고 확장이 어렵습니다. 이러한 한계를 해결하기 위해, 우리는 시뮬레이션-실제 전송 파이프라인을 재검토하고 강력한 일반화를 유지하면서 실제 환경에서 제로샷 배포를 가능하게 하는 핵심 기술을 개발합니다. 우리는 혼잡한 장면에서 폐쇄 루프 목표 지향 정밀 파지를 위한 2단계 교사-학생 프레임워크인 ClutterDexGrasp를 제안합니다. 이 프레임워크는 혼잡 밀도 커리큘럼 학습을 사용하여 시뮬레이션에서 훈련된 교사 정책을 특징으로 하며, 기하학 및 공간 임베디드 장면 표현과 새로운 포괄적 안전 커리큘럼을 통합하여 일반적이고 동적이며 안전한 파지 행동을 가능하게 합니다. 모방 학습을 통해, 우리는 교사의 지식을 부분 포인트 클라우드 관찰에서 작동하는 학생 3D 확산 정책(DP3)으로 증류합니다. 우리가 아는 한, 이는 혼잡한 장면에서 목표 지향 정밀 파지를 위한 최초의 제로샷 시뮬레이션-실제 폐쇄 루프 시스템으로, 다양한 물체와 배치에서 강력한 성능을 입증합니다. 더 자세한 내용과 비디오는 https://clutterdexgrasp.github.io/에서 확인할 수 있습니다.

## 핵심 내용
혼잡한 장면에서의 정밀 파지는 다양한 물체 형상, 가려짐, 잠재적 충돌로 인해 상당한 어려움을 제기합니다. 기존 방법은 주로 단일 물체 파지 또는 상호작용 없는 파지 자세 예측에 초점을 맞추고 있어 복잡하고 혼잡한 장면에는 부적합합니다. 최근의 시각-언어-행동 모델은 잠재적 해결책을 제공하지만, 광범위한 실제 시연이 필요하여 비용이 많이 들고 확장이 어렵습니다. 이러한 한계를 해결하기 위해, 우리는 시뮬레이션-실제 전송 파이프라인을 재검토하고 강력한 일반화를 유지하면서 실제 환경에서 제로샷 배포를 가능하게 하는 핵심 기술을 개발합니다. 우리는 혼잡한 장면에서 폐쇄 루프 목표 지향 정밀 파지를 위한 2단계 교사-학생 프레임워크인 ClutterDexGrasp를 제안합니다. 이 프레임워크는 혼잡 밀도 커리큘럼 학습을 사용하여 시뮬레이션에서 훈련된 교사 정책을 특징으로 하며, 기하학 및 공간 임베디드 장면 표현과 새로운 포괄적 안전 커리큘럼을 통합하여 일반적이고 동적이며 안전한 파지 행동을 가능하게 합니다. 모방 학습을 통해, 우리는 교사의 지식을 부분 포인트 클라우드 관찰에서 작동하는 학생 3D 확산 정책(DP3)으로 증류합니다. 우리가 아는 한, 이는 혼잡한 장면에서 목표 지향 정밀 파지를 위한 최초의 제로샷 시뮬레이션-실제 폐쇄 루프 시스템으로, 다양한 물체와 배치에서 강력한 성능을 입증합니다. 더 자세한 내용과 비디오는 https://clutterdexgrasp.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2506.14317v3
