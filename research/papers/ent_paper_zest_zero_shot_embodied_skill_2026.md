---
$id: ent_paper_zest_zero_shot_embodied_skill_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control'
  zh: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control'
  ko: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control'
summary:
  en: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: ZEST（Zero-shot Embodied Skill Transfer）是2026年提出的一种运动模仿框架，用于人形机器人的全身控制与灵巧操作。该工作由研究团队开发，核心贡献在于：无需接触标签、参考窗口、状态估计器或大量奖励塑形，即可从多种数据源（高保真动作捕捉、噪声单目视频、非物理约束动画）零样本迁移技能到真实机器人上，并在Boston
    Dynamics Atlas、Unitree G1和Spot四足机器人上验证了动态、多接触行为的泛化能力。
  ko: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
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
- loco_manipulation
- whole_body_control
- zest
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.00401v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP1 dedup merge 2026-08-06: merged
    ent_paper_zest_zero_shot_embodied_skill_2026 into this card (rules: same_arxiv). Backup+manifest: .staging/cleanup_wp12/.
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (1008 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ZEST: Zero-shot Embodied Skill Transfer for Athletic Robot Control (arXiv)'
  url: https://arxiv.org/abs/2602.00401
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
ZEST通过强化学习训练策略，结合自适应采样（聚焦困难运动片段）和基于模型辅助力矩的自动课程学习，实现了动态长时程动作的零样本部署。其训练流程完全在仿真环境中进行，采用中等域随机化，并提供了从近似解析臂值选择关节级增益的流程，以及改进的致动器模型。实验表明，ZEST能从动作捕捉学习多接触技能（如匍匐前进、霹雳舞），从视频直接迁移舞蹈和场景交互技能（如爬箱），甚至跨形态到Spot四足机器人实现连续后空翻等杂技动作，展示了异构数据源和实体间的鲁棒零样本迁移能力。

## 核心内容
### 方法概述
ZEST的核心是运动模仿框架，通过强化学习从多样化数据源训练策略，无需接触标签、参考窗口、状态估计器或大量奖励塑形。其训练流程包含两个关键组件：
- **自适应采样**：在训练过程中动态聚焦于困难运动片段，提升学习效率。
- **自动课程学习**：基于模型辅助力矩（model-based assistive wrench）自动调整任务难度，使策略能掌握动态、长时程动作。

### 架构与实验设置
- **训练环境**：完全在仿真中完成，采用中等域随机化（moderate domain randomization）增强鲁棒性。
- **硬件部署**：零样本迁移到真实机器人，无需额外微调。
- **关节增益选择**：提供从近似解析臂值（approximate analytical armature values）选择关节级增益的流程，并改进了致动器模型（actuator model）。

### 关键实验结果
- **Boston Dynamics Atlas**：从动作捕捉数据学习动态多接触技能，如匍匐前进（army crawl）和霹雳舞（breakdancing）。
- **Atlas与Unitree G1**：直接从单目视频迁移表达性舞蹈和场景交互技能，如爬箱（box-climbing）。
- **Spot四足机器人**：跨形态迁移，通过动画数据实现连续后空翻（continuous backflip）等杂技动作。

### 结论
ZEST在异构数据源（动作捕捉、视频、动画）和不同机器人形态（Atlas、G1、Spot）上均实现了零样本部署，无需接触标签或状态估计器，显著降低了工程调参成本。该框架为生物运动与机器人控制之间提供了可扩展的接口，验证了从仿真到真实世界的鲁棒迁移能力。

## Overview
Achieving robust, human-like whole-body control on humanoid robots for agile, contact-rich behaviors remains a central challenge, demanding heavy per-skill engineering and a brittle process of tuning controllers. We introduce ZEST (Zero-shot Embodied Skill Transfer), a streamlined motion-imitation framework that trains policies via reinforcement learning from diverse sources -- high-fidelity motion capture, noisy monocular video, and non-physics-constrained animation -- and deploys them to hardware zero-shot. ZEST generalizes across behaviors and platforms while avoiding contact labels, reference or observation windows, state estimators, and extensive reward shaping. Its training pipeline combines adaptive sampling, which focuses training on difficult motion segments, and an automatic curriculum using a model-based assistive wrench, together enabling dynamic, long-horizon maneuvers. We further provide a procedure for selecting joint-level gains from approximate analytical armature values for closed-chain actuators, along with a refined model of actuators. Trained entirely in simulation with moderate domain randomization, ZEST demonstrates remarkable generality. On Boston Dynamics' Atlas humanoid, ZEST learns dynamic, multi-contact skills (e.g., army crawl, breakdancing) from motion capture. It transfers expressive dance and scene-interaction skills, such as box-climbing, directly from videos to Atlas and the Unitree G1. Furthermore, it extends across morphologies to the Spot quadruped, enabling acrobatics, such as a continuous backflip, through animation. Together, these results demonstrate robust zero-shot deployment across heterogeneous data sources and embodiments, establishing ZEST as a scalable interface between biological movements and their robotic counterparts.

## 参考
- http://arxiv.org/abs/2602.00401v1

## 개요
ZEST는 강화 학습을 통해 정책을 훈련하고, 적응형 샘플링(어려운 동작 구간에 집중)과 모델 기반 보조 토크를 활용한 자동 커리큘럼 학습을 결합하여 동적 장시간 동작의 제로샷 배포를 구현합니다. 훈련 과정은 전적으로 시뮬레이션 환경에서 이루어지며, 중간 수준의 도메인 무작위화를 채택하고, 근사 해석적 아마추어 값에서 관절 수준 이득을 선택하는 절차와 개선된 액추에이터 모델을 제공합니다. 실험 결과, ZEST는 모션 캡처에서 다중 접촉 기술(예: 기어가기, 브레이크댄스)을 학습하고, 비디오에서 직접 춤과 장면 상호작용 기술(예: 상자 오르기)을 전이하며, 심지어 Spot 네 발 달린 로봇으로 형태를 넘어 연속 백플립과 같은 곡예 동작을 구현하여 이질적 데이터 소스와 개체 간의 강건한 제로샷 전이 능력을 보여줍니다.

## 핵심 내용
### 방법 개요
ZEST의 핵심은 운동 모방 프레임워크로, 강화 학습을 통해 다양한 데이터 소스에서 정책을 훈련하며 접촉 라벨, 참조 창, 상태 추정기 또는 과도한 보상 형성 없이 수행됩니다. 훈련 과정은 두 가지 핵심 구성 요소를 포함합니다:
- **적응형 샘플링**: 훈련 중 어려운 동작 구간에 동적으로 집중하여 학습 효율을 향상시킵니다.
- **자동 커리큘럼 학습**: 모델 기반 보조 토크(model-based assistive wrench)를 활용하여 작업 난이도를 자동으로 조정하며, 정책이 동적이고 장시간 동작을 숙달할 수 있게 합니다.

### 아키텍처 및 실험 설정
- **훈련 환경**: 전적으로 시뮬레이션에서 완료되며, 중간 수준의 도메인 무작위화(moderate domain randomization)를 채택하여 강건성을 강화합니다.
- **하드웨어 배포**: 추가 미세 조정 없이 실제 로봇으로 제로샷 전이됩니다.
- **관절 이득 선택**: 근사 해석적 아마추어 값(approximate analytical armature values)에서 관절 수준 이득을 선택하는 절차를 제공하고, 액추에이터 모델(actuator model)을 개선합니다.

### 주요 실험 결과
- **Boston Dynamics Atlas**: 모션 캡처 데이터에서 기어가기(army crawl)와 브레이크댄스(breakdancing)와 같은 동적 다중 접촉 기술을 학습합니다.
- **Atlas 및 Unitree G1**: 단일 비디오에서 표현적 춤과 장면 상호작용 기술(예: 상자 오르기, box-climbing)을 직접 전이합니다.
- **Spot 네 발 달린 로봇**: 형태를 넘어 애니메이션 데이터를 통해 연속 백플립(continuous backflip)과 같은 곡예 동작을 구현합니다.

### 결론
ZEST는 이질적 데이터 소스(모션 캡처, 비디오, 애니메이션)와 다양한 로봇 형태(Atlas, G1, Spot)에서 접촉 라벨이나 상태 추정기 없이 제로샷 배포를 구현하며, 엔지니어링 파라미터 튜닝 비용을 크게 줄입니다. 이 프레임워크는 생물학적 운동과 로봇 제어 사이에 확장 가능한 인터페이스를 제공하며, 시뮬레이션에서 실제 세계로의 강건한 전이 능력을 검증합니다.
