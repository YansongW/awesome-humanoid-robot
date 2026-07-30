---
$id: ent_paper_collision_free_humanoid_traver_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
  zh: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
  ko: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes
summary:
  en: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: HumanoidPF 是一种用于人形机器人在杂乱室内场景中无碰撞通行的感知表征方法，由研究者于 2026 年提出。其核心贡献在于将人机障碍物关系编码为无碰撞运动方向，显著简化了基于强化学习的通行技能学习，并展现出极小的 sim-to-real
    差距。该方法结合真实室内场景裁剪与程序化障碍物生成的混合场景训练，成功实现了从仿真到真实世界的策略迁移。
  ko: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- collision_free_humanoid_traver
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.16035v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Collision-Free Humanoid Traversal in Cluttered Indoor Scenes (arXiv)
  url: https://arxiv.org/abs/2601.16035
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人在杂乱室内场景（如跨越地面散落物体、躲避低矮障碍物、穿越狭窄通道）中的无碰撞通行问题，提出 HumanoidPF 感知表征。HumanoidPF 将人机障碍物关系编码为无碰撞运动方向，有效解决了直接学习映射关系的困难，并显著降低了强化学习训练难度。实验发现该表征在仿真与真实环境间具有极小的 sim-to-real 差距。为提升策略泛化能力，研究提出混合场景生成方法，融合真实 3D 室内场景裁剪与程序化合成障碍物。最终策略成功迁移至真实世界，并开发了单点击即可控制人形机器人通行的遥操作系统。

## 核心内容
### 问题定义
研究聚焦人形机器人在杂乱室内场景中的无碰撞通行问题，具体包括：
- 跨越地面散落物体（hurdling）
- 躲避低矮障碍物（crouching）
- 穿越狭窄通道（squeezing through）

### 核心方法：HumanoidPF
- **表征设计**：HumanoidPF 将人机障碍物关系编码为无碰撞运动方向，作为强化学习的状态输入。
- **优势**：相比直接学习感知到动作的映射，HumanoidPF 显著降低了学习难度，并展现出极小的 sim-to-real 差距。

### 场景生成方法
- **混合场景生成**：结合两种数据源：
  - 真实 3D 室内场景的裁剪片段
  - 程序化合成的障碍物布局
- **目的**：提升策略在多样化杂乱场景中的泛化能力。

### 实验设置与结果
- **训练**：基于强化学习框架，以 HumanoidPF 作为感知表征输入。
- **仿真实验**：在多种杂乱室内场景中验证策略的有效性。
- **真实世界迁移**：成功将策略部署至真实人形机器人，并开发单点击遥操作系统。
- **关键发现**：HumanoidPF 的 sim-to-real 差距极小，无需额外域随机化即可实现迁移。

### 结论
HumanoidPF 为人形机器人在杂乱室内场景中的无碰撞通行提供了有效的感知表征方案，结合混合场景生成方法，实现了从仿真到真实世界的策略泛化。代码与演示视频已开源。

## Overview
We study the problem of collision-free humanoid traversal in cluttered indoor scenes, such as hurdling over objects scattered on the floor, crouching under low-hanging obstacles, or squeezing through narrow passages. To achieve this goal, the humanoid needs to map its perception of surrounding obstacles with diverse spatial layouts and geometries to the corresponding traversal skills. However, the lack of an effective representation that captures humanoid-obstacle relationships during collision avoidance makes directly learning such mappings difficult. We therefore propose Humanoid Potential Field (HumanoidPF), which encodes these relationships as collision-free motion directions, significantly facilitating RL-based traversal skill learning. We also find that HumanoidPF exhibits a surprisingly negligible sim-to-real gap as a perceptual representation. To further enable generalizable traversal skills through diverse and challenging cluttered indoor scenes, we further propose a hybrid scene generation method, incorporating crops of realistic 3D indoor scenes and procedurally synthesized obstacles. We successfully transfer our policy to the real world and develop a teleoperation system where users could command the humanoid to traverse in cluttered indoor scenes with just a single click. Extensive experiments are conducted in both simulation and the real world to validate the effectiveness of our method. Demos and code can be found in our website: https://axian12138.github.io/CAT/.

## 개요
본 연구는 복잡한 실내 환경에서 인간형 로봇의 충돌 없는 이동 문제를 다룹니다. 예를 들어 바닥에 흩어진 장애물을 뛰어넘거나, 낮게 걸린 장애물 아래로 웅크려 지나가거나, 좁은 통로를 비집고 지나가는 등의 상황을 포함합니다. 이러한 목표를 달성하기 위해 인간형 로봇은 다양한 공간 배치와 기하학적 형태를 가진 주변 장애물에 대한 인식을 해당 이동 기술에 매핑해야 합니다. 그러나 충돌 회피 과정에서 인간형 로봇과 장애물 간의 관계를 포착하는 효과적인 표현이 부족하여 이러한 매핑을 직접 학습하기 어렵습니다. 따라서 우리는 **Humanoid Potential Field (HumanoidPF)**를 제안합니다. 이는 이러한 관계를 충돌 없는 이동 방향으로 인코딩하여 강화 학습 기반 이동 기술 학습을 크게 촉진합니다. 또한 HumanoidPF는 지각 표현으로서 시뮬레이션과 실제 환경 간의 격차가 놀라울 정도로 미미함을 발견했습니다. 다양하고 도전적인 복잡한 실내 환경에서 일반화 가능한 이동 기술을 더욱 가능하게 하기 위해, 현실적인 3D 실내 장면의 일부와 절차적으로 합성된 장애물을 결합한 하이브리드 장면 생성 방법을 추가로 제안합니다. 우리는 정책을 실제 세계로 성공적으로 전이하고, 사용자가 단 한 번의 클릭으로 인간형 로봇을 복잡한 실내 환경에서 이동하도록 명령할 수 있는 원격 조작 시스템을 개발했습니다. 시뮬레이션과 실제 환경 모두에서 광범위한 실험을 수행하여 방법의 효과를 검증했습니다. 데모와 코드는 웹사이트(https://axian12138.github.io/CAT/)에서 확인할 수 있습니다.

## 핵심 내용
본 연구는 복잡한 실내 환경에서 인간형 로봇의 충돌 없는 이동 문제를 다룹니다. 예를 들어 바닥에 흩어진 장애물을 뛰어넘거나, 낮게 걸린 장애물 아래로 웅크려 지나가거나, 좁은 통로를 비집고 지나가는 등의 상황을 포함합니다. 이러한 목표를 달성하기 위해 인간형 로봇은 다양한 공간 배치와 기하학적 형태를 가진 주변 장애물에 대한 인식을 해당 이동 기술에 매핑해야 합니다. 그러나 충돌 회피 과정에서 인간형 로봇과 장애물 간의 관계를 포착하는 효과적인 표현이 부족하여 이러한 매핑을 직접 학습하기 어렵습니다. 따라서 우리는 **Humanoid Potential Field (HumanoidPF)**를 제안합니다. 이는 이러한 관계를 충돌 없는 이동 방향으로 인코딩하여 강화 학습 기반 이동 기술 학습을 크게 촉진합니다. 또한 HumanoidPF는 지각 표현으로서 시뮬레이션과 실제 환경 간의 격차가 놀라울 정도로 미미함을 발견했습니다. 다양하고 도전적인 복잡한 실내 환경에서 일반화 가능한 이동 기술을 더욱 가능하게 하기 위해, 현실적인 3D 실내 장면의 일부와 절차적으로 합성된 장애물을 결합한 하이브리드 장면 생성 방법을 추가로 제안합니다. 우리는 정책을 실제 세계로 성공적으로 전이하고, 사용자가 단 한 번의 클릭으로 인간형 로봇을 복잡한 실내 환경에서 이동하도록 명령할 수 있는 원격 조작 시스템을 개발했습니다. 시뮬레이션과 실제 환경 모두에서 광범위한 실험을 수행하여 방법의 효과를 검증했습니다. 데모와 코드는 웹사이트(https://axian12138.github.io/CAT/)에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2601.16035v2
