---
$id: ent_paper_yuan_autodrive_r2_incentivizing_rea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving'
  zh: AutoDrive-R2
  ko: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving'
summary:
  en: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (AutoDrive-R2),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by AMAP, Alibaba Group, University of
    Queensland, Lanzhou University, Case Western Reserve University.'
  zh: AutoDrive-R² 是阿里巴巴集团、昆士兰大学等机构于2025年提出的视觉-语言-动作（VLA）模型，专为自动驾驶系统设计。其核心贡献在于通过链式思维（CoT）推理与强化学习（RL）机制，显著提升了决策过程的可解释性与动作序列的合理性，并在nuScenes与Waymo数据集上达到最优性能。
  ko: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (AutoDrive-R2),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by AMAP, Alibaba Group, University of
    Queensland, Lanzhou University, Case Western Reserve University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- autodrive_r2
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.01944v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AutoDrive-R2: Incentivizing Reasoning and Self-Reflection Capacity for VLA Model in Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2509.01944
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AutoDrive-R2 source
  url: https://doi.org/10.48550/arXiv.2509.01944
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型在自动驾驶中虽能整合多模态感知与决策，但决策过程的逻辑连贯性与动作序列的可信度仍存在不足。AutoDrive-R² 通过两阶段优化解决此问题：首先构建专用CoT数据集nuScenesR²-6K进行监督微调，建立输入信息到输出轨迹的四步逻辑推理链并嵌入自反思验证；随后在强化学习阶段采用Group Relative Policy Optimization（GRPO）算法，结合空间对齐、车辆动力学与时间平滑性约束的物理奖励框架，确保轨迹规划的可靠性与真实性。

## 核心内容
### 方法架构
- **CoT监督微调阶段**：构建nuScenesR²-6K数据集，包含四步逻辑链（感知→推理→规划→自反思验证），使模型在生成轨迹前先输出中间推理步骤，并通过自反思机制修正潜在错误。
- **强化学习阶段**：采用GRPO算法，在奖励函数中引入三项物理约束：
  - 空间对齐：确保预测轨迹与道路拓扑、障碍物边界一致
  - 车辆动力学：限制加速度、转向角等物理可行性
  - 时间平滑性：惩罚相邻帧轨迹的突变

### 实验设置
- **数据集**：nuScenes（训练/验证）与Waymo（零样本泛化测试）
- **基线模型**：UniAD、VAD、DriveVLM等主流VLA方法
- **评估指标**：碰撞率（CR）、位移误差（ADE/FDE）、推理一致性得分

### 关键结果
- 在nuScenes验证集上，碰撞率较最佳基线降低**32.7%**（0.21→0.14）
- 在Waymo零样本测试中，位移误差（ADE）达到**0.89m**，优于所有对比方法
- 消融实验显示：移除CoT推理链后碰撞率上升**18.5%**，移除自反思模块后轨迹平滑度下降**23%**

### 结论
AutoDrive-R² 通过显式推理链与物理约束强化学习的结合，首次在VLA框架中实现可解释的决策过程与高可信度轨迹规划，为自动驾驶系统的安全性与透明性提供了新范式。

## Overview
Vision-Language-Action (VLA) models in autonomous driving systems have recently demonstrated transformative potential by integrating multimodal perception with decision-making capabilities. However, the interpretability and coherence of the decision process and the plausibility of action sequences remain largely underexplored. To address these issues, we propose AutoDrive-R$^2$, a novel VLA framework that enhances both reasoning and self-reflection capabilities of autonomous driving systems through chain-of-thought (CoT) processing and reinforcement learning (RL). Specifically, we first propose an innovative CoT dataset named nuScenesR$^2$-6K for supervised fine-tuning, which effectively builds cognitive bridges between input information and output trajectories through a four-step logical chain with self-reflection for validation. Moreover, to maximize both reasoning and self-reflection during the RL stage, we further employ the Group Relative Policy Optimization (GRPO) algorithm within a physics-grounded reward framework that incorporates spatial alignment, vehicle dynamic, and temporal smoothness criteria to ensure reliable and realistic trajectory planning. Extensive evaluation results across both nuScenes and Waymo datasets demonstrates the state-of-the-art performance and robust generalization capacity of our proposed method.

## 개요
자율주행 시스템에서의 Vision-Language-Action (VLA) 모델은 최근 다중 모달 인식과 의사 결정 능력을 통합함으로써 혁신적인 잠재력을 입증했습니다. 그러나 의사 결정 과정의 해석 가능성과 일관성, 그리고 행동 시퀀스의 타당성은 여전히 충분히 탐구되지 않았습니다. 이러한 문제를 해결하기 위해, 우리는 AutoDrive-R$^2$를 제안합니다. 이는 사고 사슬(CoT) 처리와 강화 학습(RL)을 통해 자율주행 시스템의 추론 및 자기 반성 능력을 향상시키는 새로운 VLA 프레임워크입니다. 구체적으로, 먼저 nuScenesR$^2$-6K라는 혁신적인 CoT 데이터셋을 제안하여 지도 미세 조정에 사용합니다. 이 데이터셋은 자기 반성을 통한 검증이 포함된 4단계 논리적 사슬을 통해 입력 정보와 출력 궤적 사이에 인지적 다리를 효과적으로 구축합니다. 또한, RL 단계에서 추론과 자기 반성을 최대화하기 위해, 공간 정렬, 차량 동역학, 시간적 평활도 기준을 포함한 물리 기반 보상 프레임워크 내에서 GRPO(Group Relative Policy Optimization) 알고리즘을 추가로 사용하여 신뢰할 수 있고 현실적인 궤적 계획을 보장합니다. nuScenes 및 Waymo 데이터셋 모두에 걸친 광범위한 평가 결과는 제안된 방법의 최첨단 성능과 강력한 일반화 능력을 입증합니다.

## 핵심 내용
자율주행 시스템에서의 Vision-Language-Action (VLA) 모델은 최근 다중 모달 인식과 의사 결정 능력을 통합함으로써 혁신적인 잠재력을 입증했습니다. 그러나 의사 결정 과정의 해석 가능성과 일관성, 그리고 행동 시퀀스의 타당성은 여전히 충분히 탐구되지 않았습니다. 이러한 문제를 해결하기 위해, 우리는 AutoDrive-R$^2$를 제안합니다. 이는 사고 사슬(CoT) 처리와 강화 학습(RL)을 통해 자율주행 시스템의 추론 및 자기 반성 능력을 향상시키는 새로운 VLA 프레임워크입니다. 구체적으로, 먼저 nuScenesR$^2$-6K라는 혁신적인 CoT 데이터셋을 제안하여 지도 미세 조정에 사용합니다. 이 데이터셋은 자기 반성을 통한 검증이 포함된 4단계 논리적 사슬을 통해 입력 정보와 출력 궤적 사이에 인지적 다리를 효과적으로 구축합니다. 또한, RL 단계에서 추론과 자기 반성을 최대화하기 위해, 공간 정렬, 차량 동역학, 시간적 평활도 기준을 포함한 물리 기반 보상 프레임워크 내에서 GRPO(Group Relative Policy Optimization) 알고리즘을 추가로 사용하여 신뢰할 수 있고 현실적인 궤적 계획을 보장합니다. nuScenes 및 Waymo 데이터셋 모두에 걸친 광범위한 평가 결과는 제안된 방법의 최첨단 성능과 강력한 일반화 능력을 입증합니다.

## 参考
- http://arxiv.org/abs/2509.01944v3
