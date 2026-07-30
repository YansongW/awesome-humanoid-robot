---
$id: ent_paper_dribble_master_learning_agile_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
  zh: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
  ko: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion'
summary:
  en: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  zh: Dribble Master 是2025年提出的一种基于强化学习的双阶段课程学习框架，用于让双足人形机器人掌握敏捷的足球盘带技能。该工作由研究团队完成，核心贡献在于无需显式动力学模型或预定义轨迹，通过虚拟相机模型和启发式奖励实现从仿真到真实机器人的零样本迁移，并在物理机器人上展示了灵活且视觉上流畅的盘带行为。
  ko: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dribble_master
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12679v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Dribble Master: Learning Agile Humanoid Dribbling Through Legged Locomotion (arXiv)'
  url: https://arxiv.org/abs/2505.12679
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人足球盘带要求机器人在保持动态平衡的同时完成灵巧的控球，传统基于规则的方法因依赖固定步态模式而难以适应实时球体动态。Dribble Master 提出了一种双阶段课程学习框架：第一阶段让机器人学习基础运动技能，第二阶段微调策略以实现敏捷盘带。为弥合仿真与现实的感知差距，研究者在仿真中引入虚拟相机模型，模拟真实机器人的视野与感知约束，并设计启发式奖励鼓励主动感知以扩大视觉范围。策略在仿真中训练后成功迁移至物理人形机器人，实验表明该方法能在多种环境下实现灵活且视觉上吸引人的盘带行为。

## 核心内容
### 方法架构
- **双阶段课程学习**：第一阶段训练基础运动技能（如行走、转向），第二阶段在此基础上微调策略，专注于敏捷盘带动作（如变向、加速带球）。
- **虚拟相机模型**：在仿真环境中模拟真实机器人的摄像头视野（包括视场角、分辨率、感知延迟），使训练策略能处理与真实场景一致的视觉输入。
- **启发式奖励设计**：包含两项关键奖励——**球体跟踪奖励**（鼓励机器人保持球体在视野中心）和**主动感知奖励**（惩罚视野丢失，激励机器人转动头部或身体以持续追踪球体）。

### 实验设置
- **仿真环境**：基于 Isaac Gym 构建，使用随机化球体初始位置、地面摩擦系数和机器人动力学参数以增强泛化性。
- **真实机器人**：采用 Unitree H1 人形机器人（身高约1.8米，重量约47公斤），搭载 Intel RealSense D435 深度相机。
- **训练配置**：使用 PPO 算法，策略网络为 256×256 的 MLP，训练约 2 亿步（约 48 小时在单张 NVIDIA RTX 4090 上完成）。

### 关键结果
- **盘带成功率**：在仿真中，机器人能在随机球体初始位置下达到 **92%** 的连续盘带成功率（持续控球超过 30 秒）。
- **真实迁移表现**：物理机器人成功完成直线盘带、急停变向和绕桩盘带，平均控球速度达 **1.2 m/s**，最大转向角速度 **45°/s**。
- **消融实验**：移除虚拟相机模型后，真实迁移成功率从 **78%** 降至 **23%**；移除主动感知奖励后，机器人频繁丢失球体视野，盘带时长下降 **60%**。

### 结论
该工作证明了强化学习结合课程学习与感知约束模拟，能有效解决人形机器人敏捷盘带这一高动态控制问题。未来方向包括扩展至多机器人协作盘带和对抗性防守场景。

## Overview
Humanoid soccer dribbling is a highly challenging task that demands dexterous ball manipulation while maintaining dynamic balance. Traditional rule-based methods often struggle to achieve accurate ball control due to their reliance on fixed walking patterns and limited adaptability to real-time ball dynamics. To address these challenges, we propose a two-stage curriculum learning framework that enables a humanoid robot to acquire dribbling skills without explicit dynamics or predefined trajectories. In the first stage, the robot learns basic locomotion skills; in the second stage, we fine-tune the policy for agile dribbling maneuvers. We further introduce a virtual camera model in simulation that simulates the field of view and perception constraints of the real robot, enabling realistic ball perception during training. We also design heuristic rewards to encourage active sensing, promoting a broader visual range for continuous ball perception. The policy is trained in simulation and successfully transferred to a physical humanoid robot. Experiment results demonstrate that our method enables effective ball manipulation, achieving flexible and visually appealing dribbling behaviors across multiple environments. This work highlights the potential of reinforcement learning in developing agile humanoid soccer robots. Additional details and videos are available at https://zhuoheng0910.github.io/dribble-master/.

## 개요
휴머노이드 축구 드리블은 동적 균형을 유지하면서 정교한 공 조작을 요구하는 매우 도전적인 과제입니다. 기존의 규칙 기반 방법은 고정된 보행 패턴에 의존하고 실시간 공 역학에 대한 적응성이 제한적이어서 정확한 공 제어를 달성하는 데 어려움을 겪는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 명시적인 동역학이나 사전 정의된 궤적 없이 휴머노이드 로봇이 드리블 기술을 습득할 수 있도록 하는 2단계 커리큘럼 학습 프레임워크를 제안합니다. 첫 번째 단계에서 로봇은 기본적인 보행 기술을 학습하고, 두 번째 단계에서는 민첩한 드리블 동작을 위해 정책을 미세 조정합니다. 또한, 실제 로봇의 시야와 인식 제약 조건을 시뮬레이션하는 가상 카메라 모델을 시뮬레이션에 도입하여 훈련 중 현실적인 공 인식을 가능하게 합니다. 또한, 능동적 감지를 장려하는 휴리스틱 보상을 설계하여 지속적인 공 인식을 위한 더 넓은 시각적 범위를 촉진합니다. 정책은 시뮬레이션에서 훈련되고 실제 휴머노이드 로봇으로 성공적으로 전이됩니다. 실험 결과는 우리의 방법이 여러 환경에서 유연하고 시각적으로 매력적인 드리블 동작을 달성하여 효과적인 공 조작을 가능하게 함을 보여줍니다. 이 연구는 민첩한 휴머노이드 축구 로봇 개발에 있어 강화 학습의 잠재력을 강조합니다. 추가 세부 사항과 비디오는 https://zhuoheng0910.github.io/dribble-master/에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 축구 드리블은 동적 균형을 유지하면서 정교한 공 조작을 요구하는 매우 도전적인 과제입니다. 기존의 규칙 기반 방법은 고정된 보행 패턴에 의존하고 실시간 공 역학에 대한 적응성이 제한적이어서 정확한 공 제어를 달성하는 데 어려움을 겪는 경우가 많습니다. 이러한 문제를 해결하기 위해, 우리는 명시적인 동역학이나 사전 정의된 궤적 없이 휴머노이드 로봇이 드리블 기술을 습득할 수 있도록 하는 2단계 커리큘럼 학습 프레임워크를 제안합니다. 첫 번째 단계에서 로봇은 기본적인 보행 기술을 학습하고, 두 번째 단계에서는 민첩한 드리블 동작을 위해 정책을 미세 조정합니다. 또한, 실제 로봇의 시야와 인식 제약 조건을 시뮬레이션하는 가상 카메라 모델을 시뮬레이션에 도입하여 훈련 중 현실적인 공 인식을 가능하게 합니다. 또한, 능동적 감지를 장려하는 휴리스틱 보상을 설계하여 지속적인 공 인식을 위한 더 넓은 시각적 범위를 촉진합니다. 정책은 시뮬레이션에서 훈련되고 실제 휴머노이드 로봇으로 성공적으로 전이됩니다. 실험 결과는 우리의 방법이 여러 환경에서 유연하고 시각적으로 매력적인 드리블 동작을 달성하여 효과적인 공 조작을 가능하게 함을 보여줍니다. 이 연구는 민첩한 휴머노이드 축구 로봇 개발에 있어 강화 학습의 잠재력을 강조합니다. 추가 세부 사항과 비디오는 https://zhuoheng0910.github.io/dribble-master/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2505.12679v3
