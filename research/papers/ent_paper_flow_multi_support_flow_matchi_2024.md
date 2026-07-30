---
$id: ent_paper_flow_multi_support_flow_matchi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation'
  zh: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation'
  ko: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation'
summary:
  en: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: Flow Multi-Support 是 2024 年提出的一种结合优化多接触全身控制器与 Flow Matching 的模仿学习方法，用于人形机器人的全身操作与支撑接触任务。该方法在仿真中证明 Flow Matching 比 Diffusion
    和传统行为克隆更适合机器人，并在真实 Talos 人形机器人上成功实现了非抓取推箱和用自由手辅助平衡关闭洗碗机抽屉的任务。此外，还引入了共享自主模式，为演示未覆盖的任务提供自动接触放置。
  ko: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- flow_multi_support
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.12381v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation (arXiv)'
  url: https://arxiv.org/abs/2407.12381
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Flow Multi-Support: Flow Matching Imitation Learning for Multi-Support Manipulation project page'
  url: https://www.youtube.com/watch?v=OyXojqRasHU
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人利用上半身进行支撑接触以增强工作空间、稳定性和接触丰富任务能力的需求，提出了一种统一框架。它结合了基于优化的多接触全身控制器与 Flow Matching 生成多模态轨迹分布的能力，用于模仿学习。在仿真中，Flow Matching 展现出比 Diffusion 和传统行为克隆更优的适用性。在真实 Talos 人形机器人上，该方法成功学会了全身非抓取推箱任务，并能通过自由手添加接触来平衡，从而关闭洗碗机抽屉。此外，还设计了共享自主模式，通过自动接触放置辅助遥操作，处理演示未覆盖的任务。

## 核心内容
### 方法架构
- 核心是将 **Flow Matching** 与 **优化多接触全身控制器** 结合。Flow Matching 是一种生成多模态轨迹分布的新方法，用于模仿学习；优化控制器则处理多接触条件下的全身平衡与运动。
- 共享自主模式：为演示未覆盖的任务提供自动接触放置，辅助遥操作。

### 实验设置
- 仿真环境：对比 Flow Matching、Diffusion 和传统行为克隆在机器人任务中的表现。
- 真实机器人：使用 **Talos** 全尺寸人形机器人，执行两项任务：
  - 全身非抓取推箱任务（non-prehensile box-pushing）。
  - 用自由手添加接触以平衡，关闭洗碗机抽屉（close dishwasher drawers）。

### 关键结果
- 仿真中，Flow Matching 比 Diffusion 和传统行为克隆更适合机器人任务，能生成多模态轨迹分布。
- 真实机器人成功完成推箱和抽屉关闭任务，验证了方法的有效性。
- 共享自主模式扩展了任务覆盖范围，无需额外演示。

### 结论
- 该方法为人形机器人利用上半身支撑接触提供了统一框架，提升了工作空间和稳定性。
- 实验视频见：https://hucebot.github.io/flow_multisupport_website/

## Overview
Humanoid robots could benefit from using their upper bodies for support contacts, enhancing their workspace, stability, and ability to perform contact-rich and pushing tasks. In this paper, we propose a unified approach that combines an optimization-based multi-contact whole-body controller with Flow Matching, a recently introduced method capable of generating multi-modal trajectory distributions for imitation learning. In simulation, we show that Flow Matching is more appropriate for robotics than Diffusion and traditional behavior cloning. On a real full-size humanoid robot (Talos), we demonstrate that our approach can learn a whole-body non-prehensile box-pushing task and that the robot can close dishwasher drawers by adding contacts with its free hand when needed for balance. We also introduce a shared autonomy mode for assisted teleoperation, providing automatic contact placement for tasks not covered in the demonstrations. Full experimental videos are available at: https://hucebot.github.io/flow_multisupport_website/

## 개요
휴머노이드 로봇은 상체를 지지 접촉에 활용함으로써 작업 공간, 안정성, 그리고 접촉이 많고 밀어내는 작업을 수행하는 능력을 향상시킬 수 있습니다. 본 논문에서는 최적화 기반의 다중 접촉 전신 제어기와 최근 도입된 방법인 Flow Matching을 결합한 통합 접근법을 제안합니다. Flow Matching은 모방 학습을 위한 다중 모드 궤적 분포를 생성할 수 있습니다. 시뮬레이션을 통해 Flow Matching이 Diffusion 및 전통적인 행동 복제보다 로봇 공학에 더 적합함을 보여줍니다. 실제 전신 휴머노이드 로봇(Talos)에서 우리의 접근법이 전신 비파지적 상자 밀기 작업을 학습할 수 있으며, 로봇이 균형을 위해 필요할 때 자유로운 손으로 접촉을 추가하여 식기 세척기 서랍을 닫을 수 있음을 입증합니다. 또한, 시연에 포함되지 않은 작업에 대해 자동 접촉 배치를 제공하는 보조 원격 조작을 위한 공유 자율 모드를 소개합니다. 전체 실험 비디오는 다음에서 확인할 수 있습니다: https://hucebot.github.io/flow_multisupport_website/

## 핵심 내용
휴머노이드 로봇은 상체를 지지 접촉에 활용함으로써 작업 공간, 안정성, 그리고 접촉이 많고 밀어내는 작업을 수행하는 능력을 향상시킬 수 있습니다. 본 논문에서는 최적화 기반의 다중 접촉 전신 제어기와 최근 도입된 방법인 Flow Matching을 결합한 통합 접근법을 제안합니다. Flow Matching은 모방 학습을 위한 다중 모드 궤적 분포를 생성할 수 있습니다. 시뮬레이션을 통해 Flow Matching이 Diffusion 및 전통적인 행동 복제보다 로봇 공학에 더 적합함을 보여줍니다. 실제 전신 휴머노이드 로봇(Talos)에서 우리의 접근법이 전신 비파지적 상자 밀기 작업을 학습할 수 있으며, 로봇이 균형을 위해 필요할 때 자유로운 손으로 접촉을 추가하여 식기 세척기 서랍을 닫을 수 있음을 입증합니다. 또한, 시연에 포함되지 않은 작업에 대해 자동 접촉 배치를 제공하는 보조 원격 조작을 위한 공유 자율 모드를 소개합니다. 전체 실험 비디오는 다음에서 확인할 수 있습니다: https://hucebot.github.io/flow_multisupport_website/

## 参考
- http://arxiv.org/abs/2407.12381v2
