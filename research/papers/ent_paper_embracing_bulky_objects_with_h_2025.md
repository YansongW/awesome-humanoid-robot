---
$id: ent_paper_embracing_bulky_objects_with_h_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
  zh: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
  ko: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning'
summary:
  en: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
  zh: 本文提出一种面向人形机器人的强化学习框架，通过整合预训练人体运动先验与神经符号距离场（NSDF）表示，实现针对大体积物体的全身拥抱操作。该方法采用教师-学生架构蒸馏大规模人体运动数据，生成自然且物理可行的全身运动模式，并通过多接触交互提升操作鲁棒性与负载能力。仿真与实物实验验证了该方法对不同形状尺寸物体的适应性及sim-to-real迁移效果。
  ko: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning is a 2025 work on
    loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- embracing_bulky_objects_with_h
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13534v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Embracing Bulky Objects with Humanoid Robots: Whole-Body Manipulation with Reinforcement Learning (arXiv)'
  url: https://arxiv.org/abs/2509.13534
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对传统末端执行器抓取在稳定性和负载能力上的局限，该研究提出一种结合人体运动先验与NSDF的强化学习框架，用于人形机器人对大体积物体的全身拥抱操作。通过教师-学生架构，系统从大规模人体运动数据中学习自然协调的全身运动模式，实现手臂与躯干的协同控制。NSDF提供连续精确的几何感知，增强长时程任务中的接触意识。实验表明，该方法能适应多种物体形状尺寸，并成功实现从仿真到真实环境的迁移。

## 核心内容
### 方法架构
- **核心框架**：基于强化学习的全身操作（WBM）框架，整合预训练人体运动先验与神经符号距离场（NSDF）表示。
- **教师-学生架构**：通过蒸馏大规模人体运动数据，生成运动学自然且物理可行的全身运动模式，实现手臂与躯干的协调控制。
- **NSDF感知**：提供连续精确的几何感知，增强长时程任务中的接触意识，提升多接触交互的鲁棒性。

### 实验设置
- **仿真环境**：在多种大体积物体（如箱子、圆柱体）上进行全身拥抱任务测试。
- **实物实验**：在真实人形机器人平台上验证sim-to-real迁移效果，评估对不同形状尺寸物体的适应性。

### 关键结果
- **适应性**：方法成功适应多种物体形状与尺寸，包括非规则几何体。
- **鲁棒性**：多接触交互显著提升操作稳定性与负载能力。
- **迁移效果**：仿真训练策略成功迁移至真实机器人，实现稳定拥抱操作。

### 结论
该框架为面向大体积物体的全身操作任务提供了有效且实用的解决方案，尤其适用于需要多接触与长时程控制的场景。

## Overview
Whole-body manipulation (WBM) for humanoid robots presents a promising approach for executing embracing tasks involving bulky objects, where traditional grasping relying on end-effectors only remains limited in such scenarios due to inherent stability and payload constraints. This paper introduces a reinforcement learning framework that integrates a pre-trained human motion prior with a neural signed distance field (NSDF) representation to achieve robust whole-body embracing. Our method leverages a teacher-student architecture to distill large-scale human motion data, generating kinematically natural and physically feasible whole-body motion patterns. This facilitates coordinated control across the arms and torso, enabling stable multi-contact interactions that enhance the robustness in manipulation and also the load capacity. The embedded NSDF further provides accurate and continuous geometric perception, improving contact awareness throughout long-horizon tasks. We thoroughly evaluate the approach through comprehensive simulations and real-world experiments. The results demonstrate improved adaptability to diverse shapes and sizes of objects and also successful sim-to-real transfer. These indicate that the proposed framework offers an effective and practical solution for multi-contact and long-horizon WBM tasks of humanoid robots.

## 개요
휴머노이드 로봇의 전신 조작(WBM)은 대형 물체를 포함한 포옹 작업을 실행하는 유망한 접근 방식을 제시합니다. 기존의 엔드 이펙터에만 의존하는 파지 방식은 안정성과 페이로드 제약으로 인해 이러한 시나리오에서 여전히 한계가 있습니다. 본 논문은 사전 훈련된 인간 동작 사전과 신경 부호 거리장(NSDF) 표현을 통합한 강화 학습 프레임워크를 소개하여 강건한 전신 포옹을 달성합니다. 우리의 방법은 교사-학생 아키텍처를 활용하여 대규모 인간 동작 데이터를 증류하고, 운동학적으로 자연스럽고 물리적으로 실현 가능한 전신 동작 패턴을 생성합니다. 이는 팔과 몸통 간의 협조 제어를 촉진하여 안정적인 다중 접촉 상호작용을 가능하게 하고, 조작의 강건성과 하중 용량을 향상시킵니다. 내장된 NSDF는 추가로 정확하고 연속적인 기하학적 인식을 제공하여 장기 작업에서 접촉 인식을 개선합니다. 우리는 포괄적인 시뮬레이션과 실제 실험을 통해 접근 방식을 철저히 평가합니다. 결과는 다양한 모양과 크기의 물체에 대한 적응성 향상과 성공적인 시뮬레이션-실제 전환을 보여줍니다. 이는 제안된 프레임워크가 휴머노이드 로봇의 다중 접촉 및 장기 WBM 작업에 효과적이고 실용적인 솔루션을 제공함을 나타냅니다.

## 핵심 내용
휴머노이드 로봇의 전신 조작(WBM)은 대형 물체를 포함한 포옹 작업을 실행하는 유망한 접근 방식을 제시합니다. 기존의 엔드 이펙터에만 의존하는 파지 방식은 안정성과 페이로드 제약으로 인해 이러한 시나리오에서 여전히 한계가 있습니다. 본 논문은 사전 훈련된 인간 동작 사전과 신경 부호 거리장(NSDF) 표현을 통합한 강화 학습 프레임워크를 소개하여 강건한 전신 포옹을 달성합니다. 우리의 방법은 교사-학생 아키텍처를 활용하여 대규모 인간 동작 데이터를 증류하고, 운동학적으로 자연스럽고 물리적으로 실현 가능한 전신 동작 패턴을 생성합니다. 이는 팔과 몸통 간의 협조 제어를 촉진하여 안정적인 다중 접촉 상호작용을 가능하게 하고, 조작의 강건성과 하중 용량을 향상시킵니다. 내장된 NSDF는 추가로 정확하고 연속적인 기하학적 인식을 제공하여 장기 작업에서 접촉 인식을 개선합니다. 우리는 포괄적인 시뮬레이션과 실제 실험을 통해 접근 방식을 철저히 평가합니다. 결과는 다양한 모양과 크기의 물체에 대한 적응성 향상과 성공적인 시뮬레이션-실제 전환을 보여줍니다. 이는 제안된 프레임워크가 휴머노이드 로봇의 다중 접촉 및 장기 WBM 작업에 효과적이고 실용적인 솔루션을 제공함을 나타냅니다.

## 参考
- http://arxiv.org/abs/2509.13534v1
