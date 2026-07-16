---
$id: ent_paper_ze_3d_diffusion_policy_generaliza_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'
  zh: DP3
  ko: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'
summary:
  en: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
  zh: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
  ko: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dp3
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03954v7.
sources:
- id: src_001
  type: website
  title: DP3 source
  url: https://doi.org/10.15607/RSS.2024.XX.067
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## 核心内容
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## 参考
- http://arxiv.org/abs/2403.03954v7

## Overview
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizably usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## Content
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizably usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## 개요
모방 학습은 로봇에게 정교한 기술을 가르치는 효율적인 방법을 제공하지만, 복잡한 기술을 강건하고 일반화 가능하게 학습하려면 일반적으로 많은 양의 인간 시연이 필요합니다. 이 어려운 문제를 해결하기 위해, 우리는 3D 시각적 표현의 힘을 조건부 행동 생성 모델의 한 종류인 확산 정책에 통합한 새로운 시각적 모방 학습 접근법인 3D Diffusion Policy (DP3)를 제시합니다. DP3의 핵심 설계는 효율적인 포인트 인코더를 사용하여 희소 포인트 클라우드에서 추출된 컴팩트한 3D 시각적 표현을 활용하는 것입니다. 72개의 시뮬레이션 작업을 포함한 실험에서 DP3는 단 10개의 시연만으로 대부분의 작업을 성공적으로 처리했으며, 기준선 대비 24.2%의 상대적 개선을 달성했습니다. 4개의 실제 로봇 작업에서 DP3는 각 작업당 40개의 시연만으로 85%의 높은 성공률로 정밀한 제어를 보여주었으며, 공간, 시점, 외관, 인스턴스 등 다양한 측면에서 뛰어난 일반화 능력을 입증했습니다. 흥미롭게도, 실제 로봇 실험에서 DP3는 안전 요구 사항을 거의 위반하지 않은 반면, 기준선 방법은 자주 위반하여 인간의 개입이 필요했습니다. 우리의 광범위한 평가는 실제 로봇 학습에서 3D 표현의 중요한 중요성을 강조합니다. 비디오, 코드 및 데이터는 https://3d-diffusion-policy.github.io 에서 확인할 수 있습니다.

## 핵심 내용
모방 학습은 로봇에게 정교한 기술을 가르치는 효율적인 방법을 제공하지만, 복잡한 기술을 강건하고 일반화 가능하게 학습하려면 일반적으로 많은 양의 인간 시연이 필요합니다. 이 어려운 문제를 해결하기 위해, 우리는 3D 시각적 표현의 힘을 조건부 행동 생성 모델의 한 종류인 확산 정책에 통합한 새로운 시각적 모방 학습 접근법인 3D Diffusion Policy (DP3)를 제시합니다. DP3의 핵심 설계는 효율적인 포인트 인코더를 사용하여 희소 포인트 클라우드에서 추출된 컴팩트한 3D 시각적 표현을 활용하는 것입니다. 72개의 시뮬레이션 작업을 포함한 실험에서 DP3는 단 10개의 시연만으로 대부분의 작업을 성공적으로 처리했으며, 기준선 대비 24.2%의 상대적 개선을 달성했습니다. 4개의 실제 로봇 작업에서 DP3는 각 작업당 40개의 시연만으로 85%의 높은 성공률로 정밀한 제어를 보여주었으며, 공간, 시점, 외관, 인스턴스 등 다양한 측면에서 뛰어난 일반화 능력을 입증했습니다. 흥미롭게도, 실제 로봇 실험에서 DP3는 안전 요구 사항을 거의 위반하지 않은 반면, 기준선 방법은 자주 위반하여 인간의 개입이 필요했습니다. 우리의 광범위한 평가는 실제 로봇 학습에서 3D 표현의 중요한 중요성을 강조합니다. 비디오, 코드 및 데이터는 https://3d-diffusion-policy.github.io 에서 확인할 수 있습니다.
