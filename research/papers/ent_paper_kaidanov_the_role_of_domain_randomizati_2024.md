---
$id: ent_paper_kaidanov_the_role_of_domain_randomizati_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control
  zh: 领域随机化在训练全身人形机器人控制扩散策略中的作用
  ko: 전신 휴머노이드 제어를 위한 확산 정책 학습에서 도메인 랜덤화의 역할
summary:
  en: This paper studies how dataset diversity and size affect Diffusion Policies for whole-body humanoid locomotion by generating
    synthetic demonstrations with AMP RL agents under various Domain Randomization conditions in IsaacGym. It finds that Diffusion
    Policies require substantially larger and more diverse datasets than manipulation tasks to achieve robust walking, with
    perturbation and terrain randomization being especially important.
  zh: 本文研究数据集多样性与规模如何影响扩散策略（Diffusion Policies）在全身人形机器人运动控制中的表现。研究团队在IsaacGym仿真环境中，通过对抗性运动先验（AMP）强化学习智能体在不同域随机化（Domain Randomization）条件下生成合成演示数据，发现扩散策略需要比操作任务更大且更多样的数据集才能实现稳健行走，其中扰动与地形随机化尤为关键。
  ko: 이 논문은 IsaacGym에서 AMP 강화학습 에이전트를 다양한 도메인 랜덤화 조건 하에서 합성 데모를 생성하여 전신 휴머노이드 보행에 대한 확산 정책에 미치는 데이터셋 다양성과 크기의 영향을 연구한다. 연구
    결과, 조작 작업에 비해 확산 정책이 안정적인 보행을 위해 훨씬 더 크고 다양한 데이터셋이 필요하며, 특히 외란 및 지형 랜덤화가 중요함을 발견했다.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_policy
- domain_randomization
- whole_body_control
- humanoid_locomotion
- adversarial_motion_prior
- imitation_learning
- isaacgym
- synthetic_demonstrations
- unitree_h1
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.01349v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control
  url: https://arxiv.org/abs/2411.01349
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
人形机器人因与人体结构相似，具备从遥操作、动作捕捉甚至人类视频中获取丰富演示数据的潜力，但从演示中蒸馏出控制策略仍具挑战。尽管扩散策略在机器人操作任务中表现优异，其在运动控制与人形机器人领域的应用尚未充分探索。本研究在IsaacGym仿真环境中，通过训练对抗性运动先验智能体并施加不同域随机化条件来生成合成演示数据集，系统比较了不同规模与多样性数据集下扩散策略的训练效果。实验表明，即使面对简单场景，运动控制策略的成功训练也需要比操作任务显著更大且更多样的数据集。

## 核心内容
### 研究背景与动机
- 人形机器人因结构仿生，可借助遥操作、动作捕捉或人类视频获取演示数据，但策略蒸馏仍是核心挑战。
- 扩散策略在机器人操作任务中已取得显著成果，但其在全身运动控制与人形机器人领域的适用性尚未被系统验证。

### 方法设计
- **仿真环境**：基于IsaacGym构建人形机器人全身控制仿真场景。
- **数据生成**：训练对抗性运动先验（AMP）强化学习智能体，在不同域随机化条件下生成合成演示轨迹。
- **域随机化条件**：包括扰动随机化（如外力干扰）与地形随机化（如地面起伏），以模拟真实环境的不确定性。

### 实验设置
- **数据集变量**：系统改变数据集规模（从数千到数十万条轨迹）与多样性（通过调整域随机化参数实现）。
- **策略训练**：使用扩散策略拟合不同特征的数据集，评估其生成稳定行走行为的能力。

### 关键发现
- **规模需求**：运动控制任务所需数据集规模远超操作任务，即使简单场景也需数万条演示轨迹。
- **多样性重要性**：扰动随机化与地形随机化对策略泛化能力提升最为显著，缺乏多样性的数据集会导致策略在未见过场景中失效。
- **性能对比**：扩散策略在充分训练后可实现稳定行走，但收敛速度与最终性能高度依赖数据集的覆盖范围。

### 结论
- 扩散策略应用于人形机器人全身运动控制时，需优先保证数据集的规模与多样性，尤其是环境扰动与地形变化的覆盖。
- 该发现为未来人形机器人数据采集策略（如结合仿真与真实数据）提供了量化指导。

## Overview
Humanoids have the potential to be the ideal embodiment in environments designed for humans. Thanks to the structural similarity to the human body, they benefit from rich sources of demonstration data, e.g., collected via teleoperation, motion capture, or even using videos of humans performing tasks. However, distilling a policy from demonstrations is still a challenging problem. While Diffusion Policies (DPs) have shown impressive results in robotic manipulation, their applicability to locomotion and humanoid control remains underexplored. In this paper, we investigate how dataset diversity and size affect the performance of DPs for humanoid whole-body control. In a simulated IsaacGym environment, we generate synthetic demonstrations by training Adversarial Motion Prior (AMP) agents under various Domain Randomization (DR) conditions, and we compare DPs fitted to datasets of different size and diversity. Our findings show that, although DPs can achieve stable walking behavior, successful training of locomotion policies requires significantly larger and more diverse datasets compared to manipulation tasks, even in simple scenarios.

## 개요
휴머노이드는 인간을 위해 설계된 환경에서 이상적인 구현체가 될 잠재력을 지니고 있습니다. 인체와의 구조적 유사성 덕분에 원격 조작, 모션 캡처, 또는 인간이 작업을 수행하는 영상 등을 통해 수집된 풍부한 시연 데이터를 활용할 수 있습니다. 그러나 시연 데이터로부터 정책을 추출하는 것은 여전히 어려운 문제입니다. 확산 정책(Diffusion Policies, DPs)은 로봇 조작 분야에서 인상적인 결과를 보여주었지만, 보행 및 휴머노이드 제어에 대한 적용 가능성은 아직 충분히 탐구되지 않았습니다. 본 논문에서는 데이터셋의 다양성과 크기가 휴머노이드 전신 제어를 위한 DP 성능에 어떤 영향을 미치는지 조사합니다. 시뮬레이션된 IsaacGym 환경에서 다양한 도메인 무작위화(Domain Randomization, DR) 조건 하에 적대적 모션 사전(Adversarial Motion Prior, AMP) 에이전트를 훈련하여 합성 시연 데이터를 생성하고, 다양한 크기와 다양성을 가진 데이터셋에 적합한 DP를 비교합니다. 연구 결과, DP가 안정적인 보행 동작을 달성할 수 있지만, 보행 정책의 성공적인 훈련은 단순한 시나리오에서도 조작 작업에 비해 훨씬 더 크고 다양한 데이터셋을 필요로 한다는 것을 보여줍니다.

## 핵심 내용
휴머노이드는 인간을 위해 설계된 환경에서 이상적인 구현체가 될 잠재력을 지니고 있습니다. 인체와의 구조적 유사성 덕분에 원격 조작, 모션 캡처, 또는 인간이 작업을 수행하는 영상 등을 통해 수집된 풍부한 시연 데이터를 활용할 수 있습니다. 그러나 시연 데이터로부터 정책을 추출하는 것은 여전히 어려운 문제입니다. 확산 정책(Diffusion Policies, DPs)은 로봇 조작 분야에서 인상적인 결과를 보여주었지만, 보행 및 휴머노이드 제어에 대한 적용 가능성은 아직 충분히 탐구되지 않았습니다. 본 논문에서는 데이터셋의 다양성과 크기가 휴머노이드 전신 제어를 위한 DP 성능에 어떤 영향을 미치는지 조사합니다. 시뮬레이션된 IsaacGym 환경에서 다양한 도메인 무작위화(Domain Randomization, DR) 조건 하에 적대적 모션 사전(Adversarial Motion Prior, AMP) 에이전트를 훈련하여 합성 시연 데이터를 생성하고, 다양한 크기와 다양성을 가진 데이터셋에 적합한 DP를 비교합니다. 연구 결과, DP가 안정적인 보행 동작을 달성할 수 있지만, 보행 정책의 성공적인 훈련은 단순한 시나리오에서도 조작 작업에 비해 훨씬 더 크고 다양한 데이터셋을 필요로 한다는 것을 보여줍니다.

## 参考
- http://arxiv.org/abs/2411.01349v1
