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
  zh: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction is a 2025
    work on physics-based character animation for humanoid robots.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.02566v1.
sources:
- id: src_001
  type: paper
  title: 'PhysHMR: Learning Humanoid Control Policies from Vision for Physically Plausible Human Motion Reconstruction (arXiv)'
  url: https://arxiv.org/abs/2510.02566
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## 核心内容
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## 参考
- http://arxiv.org/abs/2510.02566v1

## Overview
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## Content
Reconstructing physically plausible human motion from monocular videos remains a challenging problem in computer vision and graphics. Existing methods primarily focus on kinematics-based pose estimation, often leading to unrealistic results due to the lack of physical constraints. To address such artifacts, prior methods have typically relied on physics-based post-processing following the initial kinematics-based motion estimation. However, this two-stage design introduces error accumulation, ultimately limiting the overall reconstruction quality. In this paper, we present PhysHMR, a unified framework that directly learns a visual-to-action policy for humanoid control in a physics-based simulator, enabling motion reconstruction that is both physically grounded and visually aligned with the input video. A key component of our approach is the pixel-as-ray strategy, which lifts 2D keypoints into 3D spatial rays and transforms them into global space. These rays are incorporated as policy inputs, providing robust global pose guidance without depending on noisy 3D root predictions. This soft global grounding, combined with local visual features from a pretrained encoder, allows the policy to reason over both detailed pose and global positioning. To overcome the sample inefficiency of reinforcement learning, we further introduce a distillation scheme that transfers motion knowledge from a mocap-trained expert to the vision-conditioned policy, which is then refined using physically motivated reinforcement learning rewards. Extensive experiments demonstrate that PhysHMR produces high-fidelity, physically plausible motion across diverse scenarios, outperforming prior approaches in both visual accuracy and physical realism.

## 개요
단일 시점 비디오에서 물리적으로 타당한 인간 동작을 재구성하는 것은 컴퓨터 비전 및 그래픽스 분야에서 여전히 어려운 문제로 남아 있습니다. 기존 방법들은 주로 운동학 기반의 자세 추정에 초점을 맞추며, 물리적 제약이 부족하여 비현실적인 결과를 초래하는 경우가 많습니다. 이러한 문제를 해결하기 위해, 이전 방법들은 초기 운동학 기반 동작 추정 후 물리 기반 후처리에 의존해 왔습니다. 그러나 이러한 2단계 설계는 오류 누적을 유발하여 궁극적으로 전체 재구성 품질을 제한합니다. 본 논문에서는 물리 기반 시뮬레이터에서 휴머노이드 제어를 위한 시각-행동 정책을 직접 학습하는 통합 프레임워크인 PhysHMR을 제안합니다. 이를 통해 입력 비디오와 시각적으로 정렬되면서도 물리적으로 타당한 동작 재구성이 가능합니다. 우리 접근법의 핵심 구성 요소는 픽셀-광선 전략으로, 2D 키포인트를 3D 공간 광선으로 변환하고 이를 전역 공간으로 변환합니다. 이러한 광선은 정책 입력으로 통합되어, 노이즈가 많은 3D 루트 예측에 의존하지 않고 강건한 전역 자세 지침을 제공합니다. 사전 학습된 인코더의 로컬 시각적 특징과 결합된 이 부드러운 전역 기반은 정책이 세부 자세와 전역 위치 모두를 추론할 수 있게 합니다. 강화 학습의 샘플 비효율성을 극복하기 위해, 우리는 모션 캡처로 학습된 전문가로부터 시각 조건화 정책으로 동작 지식을 전이하는 증류 기법을 추가로 도입하며, 이후 물리 기반 강화 학습 보상을 사용하여 정제합니다. 광범위한 실험을 통해 PhysHMR이 다양한 시나리오에서 높은 충실도와 물리적 타당성을 가진 동작을 생성하며, 시각적 정확성과 물리적 현실성 모두에서 이전 방법들을 능가함을 입증합니다.

## 핵심 내용
단일 시점 비디오에서 물리적으로 타당한 인간 동작을 재구성하는 것은 컴퓨터 비전 및 그래픽스 분야에서 여전히 어려운 문제로 남아 있습니다. 기존 방법들은 주로 운동학 기반의 자세 추정에 초점을 맞추며, 물리적 제약이 부족하여 비현실적인 결과를 초래하는 경우가 많습니다. 이러한 문제를 해결하기 위해, 이전 방법들은 초기 운동학 기반 동작 추정 후 물리 기반 후처리에 의존해 왔습니다. 그러나 이러한 2단계 설계는 오류 누적을 유발하여 궁극적으로 전체 재구성 품질을 제한합니다. 본 논문에서는 물리 기반 시뮬레이터에서 휴머노이드 제어를 위한 시각-행동 정책을 직접 학습하는 통합 프레임워크인 PhysHMR을 제안합니다. 이를 통해 입력 비디오와 시각적으로 정렬되면서도 물리적으로 타당한 동작 재구성이 가능합니다. 우리 접근법의 핵심 구성 요소는 픽셀-광선 전략으로, 2D 키포인트를 3D 공간 광선으로 변환하고 이를 전역 공간으로 변환합니다. 이러한 광선은 정책 입력으로 통합되어, 노이즈가 많은 3D 루트 예측에 의존하지 않고 강건한 전역 자세 지침을 제공합니다. 사전 학습된 인코더의 로컬 시각적 특징과 결합된 이 부드러운 전역 기반은 정책이 세부 자세와 전역 위치 모두를 추론할 수 있게 합니다. 강화 학습의 샘플 비효율성을 극복하기 위해, 우리는 모션 캡처로 학습된 전문가로부터 시각 조건화 정책으로 동작 지식을 전이하는 증류 기법을 추가로 도입하며, 이후 물리 기반 강화 학습 보상을 사용하여 정제합니다. 광범위한 실험을 통해 PhysHMR이 다양한 시나리오에서 높은 충실도와 물리적 타당성을 가진 동작을 생성하며, 시각적 정확성과 물리적 현실성 모두에서 이전 방법들을 능가함을 입증합니다.
