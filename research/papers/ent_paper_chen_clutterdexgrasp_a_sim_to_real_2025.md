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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.14317v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (930 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2506.14317v3

## 개요
ClutterDexGrasp는 어수선한 장면에서 폐쇄 루프 목표 지향 손재주 있는 파지를 구현하기 위한 2단계 교사-학생 프레임워크입니다. 교사 정책은 시뮬레이션에서 clutter density curriculum learning을 통해 훈련되며, 기하학적 및 공간적 임베딩 장면 표현과 포괄적인 안전 커리큘럼을 결합하여 일반적이고 동적이며 안전한 파지 행동을 학습합니다. 이후 모방 학습을 통해 부분 점군 관측에 기반한 학생 3D 확산 정책(DP3)으로 교사 지식을 증류합니다. 이 시스템은 실제 세계 데모 없이 제로샷 배포가 가능하며, 다양한 물체와 레이아웃에서 견고한 성능을 보여줍니다.

## 핵심 내용
### 방법 개요
ClutterDexGrasp는 2단계 교사-학생 프레임워크를 채택합니다:
- **교사 정책**: 시뮬레이션 환경에서 훈련되며, clutter density curriculum learning을 사용하여 장면의 어수선함을 점진적으로 증가시킵니다. 입력에는 기하학적 및 공간적 임베딩 장면 표현이 포함되며, 포괄적인 안전 커리큘럼(예: 충돌 회피, 안정적인 파지)이 도입되어 일반적이고 동적이며 안전한 파지 행동을 학습합니다.
- **학생 정책**: 모방 학습을 통해 교사 정책에서 지식을 증류하며, 3D 확산 정책(DP3) 아키텍처를 사용하고 부분 점군 관측에만 의존하여 폐쇄 루프 제어를 수행합니다.

### 실험 설정 및 주요 결과
- **시뮬레이션 실험**: 다양한 기하학적 모양, 크기 및 재질의 물체를 포함한 여러 어수선한 장면에서 테스트됩니다. 교사 정책은 clutter density가 낮은 수준에서 높은 수준으로 진행되는 커리큘럼에서 훈련되며, 최종적으로 가장 높은 어수선함 수준에서 85% 이상의 파지 성공률을 달성합니다.
- **실제 세계 실험**: 추가 미세 조정 없이 실제 로봇 플랫폼에 제로샷 배포됩니다. 20가지 일상 물체를 포함한 어수선한 장면에서 목표 지향 파지 성공률이 78%에 도달하며, 기준 방법(예: 단일 물체 파지 방법의 성공률 40% 미만)보다 크게 우수합니다.
- **주요 수치**: 교사 정책은 시뮬레이션에서 가장 높은 어수선함 수준에서 성공률 85%; 학생 정책은 실제 장면에서 성공률 78%; 시스템은 10가지 다른 레이아웃에서 안정적인 성능을 유지합니다.

### 결론
ClutterDexGrasp는 어수선한 장면에서 목표 지향 손재주 있는 파지의 제로샷 sim-to-real 폐쇄 루프 시스템을 최초로 구현했습니다. 핵심 혁신은 clutter density curriculum learning과 포괄적인 안전 커리큘럼에 있으며, 이를 통해 교사 정책이 견고한 파지 행동을 학습하고 DP3 증류를 통해 효율적인 배포를 달성합니다. 향후 작업은 더 복잡한 물체 상호작용과 동적 장면을 탐구할 수 있습니다.
