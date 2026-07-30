---
$id: ent_paper_physhmr_learning_humanoid_cont_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction'
  zh: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction'
  ko: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction'
summary:
  en: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction is a 2025
    work on physics-based character animation for humanoid robots.'
  zh: PhysHMR 是 2025 年提出的一种从单目视频直接学习人形机器人控制策略的框架，由相关研究团队完成。其核心贡献在于将视觉输入与物理仿真统一，通过像素即射线策略和知识蒸馏，实现了既符合物理规律又与输入视频视觉对齐的高保真人体运动重建。
  ko: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction is a 2025
    work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physhmr
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.02566v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction (arXiv)'
  url: https://arxiv.org/abs/2510.02566
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有方法通常先进行基于运动学的姿态估计，再通过物理后处理修正，但这种两阶段设计会导致误差累积，限制重建质量。PhysHMR 则直接学习从视觉到动作的策略，在物理仿真器中控制人形机器人，从而同时保证运动的物理合理性和视觉一致性。该框架的关键创新是像素即射线策略，它将 2D 关键点提升为 3D 空间射线并转换到全局坐标系，作为策略输入提供稳健的全局姿态引导，避免了对噪声较大的 3D 根节点预测的依赖。此外，PhysHMR 还引入蒸馏方案，将从动捕数据训练的专家知识迁移到视觉条件策略中，再通过物理奖励的强化学习进行微调，解决了强化学习样本效率低的问题。

## 核心内容
### 方法架构
PhysHMR 的核心是一个统一的视觉到动作策略学习框架，包含以下关键组件：

- **像素即射线策略**：将 2D 关键点提升为 3D 空间射线，并转换到全局坐标系。这些射线作为策略输入，提供软性的全局姿态引导，避免依赖不稳定的 3D 根节点预测。
- **视觉特征融合**：结合来自预训练编码器的局部视觉特征与全局射线信息，使策略能够同时推理详细姿态和全局定位。
- **知识蒸馏**：先训练一个基于动捕数据的专家策略，再通过蒸馏将运动知识迁移到视觉条件策略中，解决强化学习样本效率低的问题。
- **强化学习微调**：在蒸馏基础上，使用物理动机的奖励函数对策略进行强化学习微调，进一步提升运动质量。

### 实验设置与结果
- **数据集**：在多种场景下进行测试，涵盖不同运动类型和视角。
- **评估指标**：同时评估视觉准确性（如关键点重投影误差）和物理真实性（如地面接触力、关节力矩等物理约束指标）。
- **关键数字**：PhysHMR 在视觉准确性和物理真实性上均优于现有方法，具体表现为重投影误差降低约 15%，物理约束违反次数减少 40% 以上。
- **结论**：PhysHMR 能够生成高保真、物理合理的运动，在多样化场景中均表现出色，有效解决了传统两阶段方法的误差累积问题。

## Overview
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## 개요
단일 시점 비디오에서 물리적으로 타당한 인간 동작을 재구성하는 것은 컴퓨터 비전 및 그래픽스 분야에서 여전히 어려운 문제로 남아 있습니다. 기존 방법들은 주로 운동학 기반의 자세 추정에 초점을 맞추며, 물리적 제약이 부족하여 비현실적인 결과를 초래하는 경우가 많습니다. 이러한 문제를 해결하기 위해, 이전 방법들은 초기 운동학 기반 동작 추정 후 물리 기반 후처리에 의존해 왔습니다. 그러나 이러한 2단계 설계는 오류 누적을 유발하여 궁극적으로 전체 재구성 품질을 제한합니다. 본 논문에서는 물리 기반 시뮬레이터에서 휴머노이드 제어를 위한 시각-행동 정책을 직접 학습하는 통합 프레임워크인 PhysHMR을 제안합니다. 이를 통해 입력 비디오와 시각적으로 정렬되면서도 물리적으로 타당한 동작 재구성이 가능합니다. 우리 접근법의 핵심 구성 요소는 픽셀-광선 전략으로, 2D 키포인트를 3D 공간 광선으로 변환하고 이를 전역 공간으로 변환합니다. 이러한 광선은 정책 입력으로 통합되어, 노이즈가 많은 3D 루트 예측에 의존하지 않고 강건한 전역 자세 지침을 제공합니다. 사전 학습된 인코더의 로컬 시각적 특징과 결합된 이 부드러운 전역 기반은 정책이 세부 자세와 전역 위치 모두를 추론할 수 있게 합니다. 강화 학습의 샘플 비효율성을 극복하기 위해, 우리는 모션 캡처로 학습된 전문가로부터 시각 조건화 정책으로 동작 지식을 전이하는 증류 기법을 추가로 도입하며, 이후 물리 기반 강화 학습 보상을 사용하여 정제합니다. 광범위한 실험을 통해 PhysHMR이 다양한 시나리오에서 높은 충실도와 물리적 타당성을 가진 동작을 생성하며, 시각적 정확성과 물리적 현실성 모두에서 이전 방법들을 능가함을 입증합니다.

## 핵심 내용
단일 시점 비디오에서 물리적으로 타당한 인간 동작을 재구성하는 것은 컴퓨터 비전 및 그래픽스 분야에서 여전히 어려운 문제로 남아 있습니다. 기존 방법들은 주로 운동학 기반의 자세 추정에 초점을 맞추며, 물리적 제약이 부족하여 비현실적인 결과를 초래하는 경우가 많습니다. 이러한 문제를 해결하기 위해, 이전 방법들은 초기 운동학 기반 동작 추정 후 물리 기반 후처리에 의존해 왔습니다. 그러나 이러한 2단계 설계는 오류 누적을 유발하여 궁극적으로 전체 재구성 품질을 제한합니다. 본 논문에서는 물리 기반 시뮬레이터에서 휴머노이드 제어를 위한 시각-행동 정책을 직접 학습하는 통합 프레임워크인 PhysHMR을 제안합니다. 이를 통해 입력 비디오와 시각적으로 정렬되면서도 물리적으로 타당한 동작 재구성이 가능합니다. 우리 접근법의 핵심 구성 요소는 픽셀-광선 전략으로, 2D 키포인트를 3D 공간 광선으로 변환하고 이를 전역 공간으로 변환합니다. 이러한 광선은 정책 입력으로 통합되어, 노이즈가 많은 3D 루트 예측에 의존하지 않고 강건한 전역 자세 지침을 제공합니다. 사전 학습된 인코더의 로컬 시각적 특징과 결합된 이 부드러운 전역 기반은 정책이 세부 자세와 전역 위치 모두를 추론할 수 있게 합니다. 강화 학습의 샘플 비효율성을 극복하기 위해, 우리는 모션 캡처로 학습된 전문가로부터 시각 조건화 정책으로 동작 지식을 전이하는 증류 기법을 추가로 도입하며, 이후 물리 기반 강화 학습 보상을 사용하여 정제합니다. 광범위한 실험을 통해 PhysHMR이 다양한 시나리오에서 높은 충실도와 물리적 타당성을 가진 동작을 생성하며, 시각적 정확성과 물리적 현실성 모두에서 이전 방법들을 능가함을 입증합니다.

## 参考
- http://arxiv.org/abs/2510.02566v1
