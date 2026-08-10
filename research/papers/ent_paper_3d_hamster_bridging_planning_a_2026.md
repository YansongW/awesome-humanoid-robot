---
$id: ent_paper_3d_hamster_bridging_planning_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
  zh: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
  ko: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
summary:
  en: 'arXiv:2606.31329v1 Announce Type: new Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level
    planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D
    end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However,
    state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks
    depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically
    distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly
    output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction
    objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across
    3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs
    and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual
    conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.'
  zh: 3D HAMSTER 是一个分层视觉-语言-动作（VLA）框架，由 Davian Robotics 团队提出，核心贡献在于让高层规划器直接输出度量可靠的 3D 轨迹，以替代现有方法中因缺乏深度信息而产生几何失真的 2D 轨迹引导。该框架通过为
    VLM 增加专用深度编码器和密集深度重建目标，将预测的 3D 路点序列直接集成到基于点云的低层策略中，在仿真和真实操作中均优于专有 VLM 和 2D 引导基线。
  ko: 'arXiv:2606.31329v1 Announce Type: new Abstract: Hierarchical Vision-Language-Action (VLA) models decouple high-level
    planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D
    end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However,
    state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks
    depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically
    distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly
    output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction
    objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across
    3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs
    and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual
    conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3d_hamster
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31329v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (810 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: '3D HAMSTER: Bridging Planning and Control in Hierarchical Vision Language Action Models through 3D Trajectory Guidance'
  url: https://arxiv.org/abs/2606.31329
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
现有分层 VLA 模型通常使用 VLM 预测的 2D 末端执行器轨迹作为下游策略的显式引导，但低层策略在点云的三维度量空间中运行，2D 引导因缺乏深度信息会导致路点被赋予场景表面深度，产生几何畸变。3D HAMSTER 通过让规划器直接输出度量可靠的 3D 轨迹来弥合这一差距，它用专用深度编码器和密集深度重建目标增强 VLM，使其能预测 3D 路点序列，并直接集成到基于点云的低层策略中。在 3D 轨迹预测、仿真和真实操作中，该方法持续优于专有 VLM 和 2D 引导基线，尤其在表观变化、未见语言、空间和视觉条件下提升最大。

## 核心内容
### 方法架构
3D HAMSTER 采用分层框架，将高层规划与低层控制解耦。高层规划器基于 VLM，通过新增的专用深度编码器（depth encoder）和密集深度重建目标（dense depth reconstruction objective），直接预测度量可靠的 3D 路点序列。这些 3D 轨迹被直接输入到基于点云的低层策略中，避免了 2D 引导因深度缺失导致的几何失真问题。

### 实验设置
- **评估维度**：包括 3D 轨迹预测精度、仿真环境中的操作成功率以及真实世界操作任务。
- **基线对比**：与专有 VLM（如 GPT-4V 等）和 2D 轨迹引导的基线方法进行比较。
- **测试条件**：涵盖标准条件、表观变化（appearance-altering shifts）、未见语言指令、未见空间布局和未见视觉条件。

### 关键结果
- 在所有评估场景中，3D HAMSTER 均优于专有 VLM 和 2D 引导基线。
- 最大性能提升出现在表观变化、未见语言、空间和视觉条件下，表明其泛化能力显著增强。
- 项目页面提供更多细节：https://davian-robotics.github.io/3D_HAMSTER/。

## Overview
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloudbased low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## Overview
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloud-based low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## Content
Hierarchical Vision-Language-Action (VLA) models decouple high-level planning from low-level control to improve generalization in robot manipulation. Recent work in this paradigm uses 2D end-effector trajectories predicted by a Vision-Language Model (VLM) as explicit guidance for a downstream policy. However, state-of-the-art low-level policies operate in 3D metric space on point clouds, and feeding them 2D guidance that lacks depth forces each waypoint to be assigned the depth of whatever scene surface lies beneath it, producing geometrically distorted trajectories. We propose 3D HAMSTER, a hierarchical framework that closes this gap by having the planner directly output metrically reliable 3D trajectories. We augment a VLM with a dedicated depth encoder and a dense depth reconstruction objective to predict 3D waypoint sequences, which are directly integrated into a pointcloud-based low-level policy. Across 3D trajectory prediction, simulation, and real-world manipulation, 3D HAMSTER consistently outperforms proprietary VLMs and 2D-guided baselines, with the largest gains under appearance-altering shifts and unseen language, spatial, and visual conditions. The project page is available at https://davian-robotics.github.io/3D_HAMSTER/.

## 参考
- http://arxiv.org/abs/2606.31329v2

## 개요
기존의 계층적 VLA 모델은 일반적으로 VLM이 예측한 2D 엔드 이펙터 궤적을 하위 정책의 명시적 가이드로 사용하지만, 하위 정책은 포인트 클라우드의 3차원 미터법 공간에서 작동하므로 2D 가이드는 깊이 정보 부족으로 인해 웨이포인트가 장면 표면 깊이로 할당되어 기하학적 왜곡이 발생합니다. 3D HAMSTER는 플래너가 직접 미터법으로 신뢰할 수 있는 3D 궤적을 출력하도록 하여 이러한 격차를 해소하며, 전용 깊이 인코더와 조밀한 깊이 재구성 목표로 VLM을 강화하여 3D 웨이포인트 시퀀스를 예측하고 이를 포인트 클라우드 기반 하위 정책에 직접 통합합니다. 3D 궤적 예측, 시뮬레이션 및 실제 조작에서 이 방법은 독점 VLM 및 2D 가이드 기준선을 지속적으로 능가하며, 특히 외관 변화, 미지의 언어, 공간 및 시각적 조건에서 가장 큰 향상을 보입니다.

## 핵심 내용
### 방법 아키텍처
3D HAMSTER는 계층적 프레임워크를 채택하여 고수준 계획과 저수준 제어를 분리합니다. 고수준 플래너는 VLM을 기반으로 하며, 새로 추가된 전용 깊이 인코더와 조밀한 깊이 재구성 목표를 통해 미터법으로 신뢰할 수 있는 3D 웨이포인트 시퀀스를 직접 예측합니다. 이러한 3D 궤적은 포인트 클라우드 기반 하위 정책에 직접 입력되어, 2D 가이드가 깊이 부족으로 인해 발생하는 기하학적 왜곡 문제를 피합니다.

### 실험 설정
- **평가 차원**: 3D 궤적 예측 정확도, 시뮬레이션 환경에서의 조작 성공률, 실제 세계 조작 작업을 포함합니다.
- **기준선 비교**: 독점 VLM(예: GPT-4V 등) 및 2D 궤적 가이드 기준선 방법과 비교합니다.
- **테스트 조건**: 표준 조건, 외관 변화, 미지의 언어 명령, 미지의 공간 배치 및 미지의 시각적 조건을 포함합니다.

### 주요 결과
- 모든 평가 시나리오에서 3D HAMSTER는 독점 VLM 및 2D 가이드 기준선보다 우수합니다.
- 가장 큰 성능 향상은 외관 변화, 미지의 언어, 공간 및 시각적 조건에서 나타나며, 일반화 능력이 크게 향상되었음을 나타냅니다.
- 프로젝트 페이지에서 더 많은 세부 정보를 확인할 수 있습니다: https://davian-robotics.github.io/3D_HAMSTER/.
