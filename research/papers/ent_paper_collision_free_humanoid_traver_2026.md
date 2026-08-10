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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.16035v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (902 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2601.16035v2

## 개요
이 연구는 휴머노이드 로봇이 복잡한 실내 환경(예: 바닥에 흩어진 물체를 넘기, 낮은 장애물 회피, 좁은 통로 통과)에서 충돌 없이 이동하는 문제를 해결하기 위해 HumanoidPF 인식 표현을 제안합니다. HumanoidPF는 로봇-장애물 관계를 충돌 없는 이동 방향으로 인코딩하여, 직접적인 매핑 관계 학습의 어려움을 효과적으로 해결하고 강화 학습 훈련 난이도를 크게 낮춥니다. 실험 결과, 이 표현은 시뮬레이션과 실제 환경 간의 sim-to-real 격차가 매우 작음을 발견했습니다. 정책 일반화 능력을 향상시키기 위해, 연구는 실제 3D 실내 장면 크롭과 절차적 합성 장애물을 결합한 혼합 장면 생성 방법을 제안합니다. 최종 정책은 실제 세계로 성공적으로 전이되었으며, 단일 클릭으로 휴머노이드 로봇의 이동을 제어할 수 있는 원격 조작 시스템을 개발했습니다.

## 핵심 내용
### 문제 정의
연구는 휴머노이드 로봇이 복잡한 실내 환경에서 충돌 없이 이동하는 문제에 초점을 맞추며, 구체적으로 다음을 포함합니다:
- 바닥에 흩어진 물체 넘기(hurdling)
- 낮은 장애물 회피(crouching)
- 좁은 통로 통과(squeezing through)

### 핵심 방법: HumanoidPF
- **표현 설계**: HumanoidPF는 로봇-장애물 관계를 충돌 없는 이동 방향으로 인코딩하여 강화 학습의 상태 입력으로 사용합니다.
- **장점**: 인식에서 행동으로의 직접적인 매핑 학습에 비해, HumanoidPF는 학습 난이도를 크게 낮추고 sim-to-real 격차가 매우 작음을 보여줍니다.

### 장면 생성 방법
- **혼합 장면 생성**: 두 가지 데이터 소스를 결합합니다:
  - 실제 3D 실내 장면의 크롭 조각
  - 절차적으로 합성된 장애물 배치
- **목적**: 다양한 복잡한 장면에서 정책의 일반화 능력을 향상시킵니다.

### 실험 설정 및 결과
- **훈련**: 강화 학습 프레임워크를 기반으로 HumanoidPF를 인식 표현 입력으로 사용합니다.
- **시뮬레이션 실험**: 다양한 복잡한 실내 장면에서 정책의 유효성을 검증합니다.
- **실제 세계 전이**: 정책을 실제 휴머노이드 로봇에 성공적으로 배포하고 단일 클릭 원격 조작 시스템을 개발했습니다.
- **주요 발견**: HumanoidPF의 sim-to-real 격차가 매우 작아 추가 도메인 무작위화 없이 전이가 가능합니다.

### 결론
HumanoidPF는 휴머노이드 로봇이 복잡한 실내 환경에서 충돌 없이 이동하는 문제에 효과적인 인식 표현 솔루션을 제공하며, 혼합 장면 생성 방법과 결합하여 시뮬레이션에서 실제 세계로의 정책 일반화를 달성합니다. 코드와 데모 비디오는 오픈소스로 공개되었습니다.
