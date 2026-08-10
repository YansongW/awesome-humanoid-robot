---
$id: ent_paper_learning_humanoid_standing_up_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Standing-up Control across Diverse Postures
  zh: Learning Humanoid Standing-up Control across Diverse Postures
  ko: Learning Humanoid Standing-up Control across Diverse Postures
summary:
  en: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: HoST (Humanoid Standing-up Control) 是2025年提出的强化学习框架，由研究团队开发，用于人形机器人从多种姿态中自主站立。其核心贡献在于通过多评论家架构和课程训练实现姿态自适应运动，并成功从仿真迁移到真实Unitree
    G1机器人上。
  ko: Learning Humanoid Standing-up Control across Diverse Postures is a 2025 work on loco-manipulation and whole-body-control
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
- humanoid
- learning_humanoid_standing_up
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.08378v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (831 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Standing-up Control across Diverse Postures (arXiv)
  url: https://arxiv.org/abs/2502.08378
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人站立控制方法要么局限于忽略硬件约束的仿真环境，要么依赖预定义的特定地面运动轨迹，无法在真实场景中实现跨姿态站立。HoST框架通过强化学习从零开始学习站立控制，利用多评论家架构和基于多样化仿真地形的课程训练，有效学习姿态自适应运动。为确保真实部署成功，研究引入了平滑正则化和隐式运动速度约束，分别减轻物理硬件上的振荡和剧烈运动。经过仿真训练后，控制策略直接部署在Unitree G1人形机器人上，在多种实验室和户外环境中实现了平滑、稳定且鲁棒的站立动作。

## 核心内容
### 方法架构
- **多评论家架构 (Multi-critic Architecture)**：用于处理不同姿态下的站立任务，使策略能够自适应学习多种起始姿势的运动模式。
- **课程训练 (Curriculum-based Training)**：在多样化仿真地形上逐步增加难度，从简单姿态过渡到复杂场景，提升泛化能力。

### 关键约束设计
- **平滑正则化 (Smoothness Regularization)**：约束运动平滑性，减少物理硬件上的振荡行为。
- **隐式运动速度约束 (Implicit Motion Speed Bound)**：限制关节运动速度，避免剧烈动作对机器人造成损害。

### 实验设置
- **硬件平台**：Unitree G1 人形机器人。
- **训练环境**：仿真环境包含多种地形（如平地、斜坡、不平整地面），覆盖实验室和户外场景。
- **部署方式**：训练后的控制策略直接迁移至真实机器人，无需额外微调。

### 关键结果
- 在实验室和户外环境中均实现平滑、稳定且鲁棒的站立动作。
- 成功覆盖多种初始姿态（如俯卧、侧卧、坐姿），验证了跨姿态泛化能力。
- 代码与演示视频已开源：https://taohuang13.github.io/humanoid-standingup.github.io/

## Overview
Standing-up control is crucial for humanoid robots, with the potential for integration into current locomotion and loco-manipulation systems, such as fall recovery. Existing approaches are either limited to simulations that overlook hardware constraints or rely on predefined ground-specific motion trajectories, failing to enable standing up across postures in real-world scenes. To bridge this gap, we present HoST (Humanoid Standing-up Control), a reinforcement learning framework that learns standing-up control from scratch, enabling robust sim-to-real transfer across diverse postures. HoST effectively learns posture-adaptive motions by leveraging a multi-critic architecture and curriculum-based training on diverse simulated terrains. To ensure successful real-world deployment, we constrain the motion with smoothness regularization and implicit motion speed bound to alleviate oscillatory and violent motions on physical hardware, respectively. After simulation-based training, the learned control policies are directly deployed on the Unitree G1 humanoid robot. Our experimental results demonstrate that the controllers achieve smooth, stable, and robust standing-up motions across a wide range of laboratory and outdoor environments. Videos and code are available at https://taohuang13.github.io/humanoid-standingup.github.io/.

## 参考
- http://arxiv.org/abs/2502.08378v2

## 개요
기존의 휴머노이드 로봇 기립 제어 방법은 하드웨어 제약을 무시한 시뮬레이션 환경에 국한되거나, 사전에 정의된 특정 지면 운동 궤적에 의존하여 실제 시나리오에서 다양한 자세로의 기립을 구현할 수 없습니다. HoST 프레임워크는 강화 학습을 통해 처음부터 기립 제어를 학습하며, 다중 비평가 아키텍처와 다양한 시뮬레이션 지형 기반의 커리큘럼 학습을 활용하여 자세 적응형 운동을 효과적으로 학습합니다. 실제 배포 성공을 보장하기 위해, 연구에서는 평활화 정규화와 암시적 운동 속도 제약을 도입하여 각각 물리적 하드웨어에서의 진동과 급격한 움직임을 완화합니다. 시뮬레이션 훈련 후, 제어 정책은 Unitree G1 휴머노이드 로봇에 직접 배포되어 다양한 실험실 및 야외 환경에서 부드럽고 안정적이며 견고한 기립 동작을 구현합니다.

## 핵심 내용
### 방법 아키텍처
- **다중 비평가 아키텍처 (Multi-critic Architecture)**: 다양한 자세에서의 기립 작업을 처리하여 정책이 여러 시작 자세의 운동 패턴을 적응형으로 학습할 수 있게 합니다.
- **커리큘럼 학습 (Curriculum-based Training)**: 다양한 시뮬레이션 지형에서 점진적으로 난이도를 높여 단순 자세에서 복잡한 시나리오로 전환하며 일반화 능력을 향상시킵니다.

### 핵심 제약 설계
- **평활화 정규화 (Smoothness Regularization)**: 운동의 평활성을 제약하여 물리적 하드웨어에서의 진동 동작을 줄입니다.
- **암시적 운동 속도 제약 (Implicit Motion Speed Bound)**: 관절 운동 속도를 제한하여 급격한 동작이 로봇에 손상을 입히는 것을 방지합니다.

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇.
- **훈련 환경**: 시뮬레이션 환경은 평지, 경사면, 불규칙한 지면 등 다양한 지형을 포함하며 실험실 및 야외 시나리오를 포괄합니다.
- **배포 방식**: 훈련된 제어 정책은 추가 미세 조정 없이 실제 로봇에 직접 전이됩니다.

### 핵심 결과
- 실험실 및 야외 환경 모두에서 부드럽고 안정적이며 견고한 기립 동작을 구현했습니다.
- 엎드린 자세, 옆으로 누운 자세, 앉은 자세 등 다양한 초기 자세를 성공적으로 포괄하여 자세 간 일반화 능력을 검증했습니다.
- 코드 및 데모 비디오는 오픈소스로 공개되었습니다: https://taohuang13.github.io/humanoid-standingup.github.io/
