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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.01944v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (848 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.01944v3

## 개요
기존 VLA 모델은 자율주행에서 다중 모달 인식과 의사 결정을 통합할 수 있지만, 의사 결정 과정의 논리적 일관성과 행동 시퀀스의 신뢰성은 여전히 부족합니다. AutoDrive-R²는 두 단계 최적화를 통해 이 문제를 해결합니다: 먼저 전용 CoT 데이터셋 nuScenesR²-6K를 구축하여 지도 미세 조정을 수행하고, 입력 정보에서 출력 궤적까지의 4단계 논리 추론 체인을 확립하며 자기 반성 검증을 내장합니다. 이후 강화 학습 단계에서는 Group Relative Policy Optimization(GRPO) 알고리즘을 채택하고, 공간 정렬, 차량 역학 및 시간 평활성 제약을 포함한 물리적 보상 프레임워크를 결합하여 궤적 계획의 신뢰성과 현실성을 보장합니다.

## 핵심 내용
### 방법 아키텍처
- **CoT 지도 미세 조정 단계**: nuScenesR²-6K 데이터셋을 구축하며, 4단계 논리 체인(인식→추론→계획→자기 반성 검증)을 포함하여 모델이 궤적을 생성하기 전에 중간 추론 단계를 먼저 출력하고, 자기 반성 메커니즘을 통해 잠재적 오류를 수정합니다.
- **강화 학습 단계**: GRPO 알고리즘을 채택하고, 보상 함수에 세 가지 물리적 제약을 도입합니다:
  - 공간 정렬: 예측 궤적이 도로 토폴로지 및 장애물 경계와 일치하도록 보장
  - 차량 역학: 가속도, 조향각 등의 물리적 실현 가능성 제한
  - 시간 평활성: 인접 프레임 궤적의 급격한 변화에 페널티 부여

### 실험 설정
- **데이터셋**: nuScenes(훈련/검증) 및 Waymo(제로샷 일반화 테스트)
- **기준 모델**: UniAD, VAD, DriveVLM 등 주요 VLA 방법
- **평가 지표**: 충돌률(CR), 변위 오차(ADE/FDE), 추론 일관성 점수

### 주요 결과
- nuScenes 검증 세트에서 충돌률이 최고 기준선 대비 **32.7%** 감소(0.21→0.14)
- Waymo 제로샷 테스트에서 변위 오차(ADE)가 **0.89m**로 모든 비교 방법보다 우수
- 제거 실험 결과: CoT 추론 체인 제거 시 충돌률 **18.5%** 증가, 자기 반성 모듈 제거 시 궤적 평활도 **23%** 감소

### 결론
AutoDrive-R²는 명시적 추론 체인과 물리적 제약 강화 학습의 결합을 통해 VLA 프레임워크에서 처음으로 해석 가능한 의사 결정 과정과 높은 신뢰도의 궤적 계획을 구현하며, 자율주행 시스템의 안전성과 투명성에 새로운 패러다임을 제공합니다.
