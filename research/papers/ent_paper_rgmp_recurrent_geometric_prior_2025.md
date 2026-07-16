---
$id: ent_paper_rgmp_recurrent_geometric_prior_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation'
  zh: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation'
  ko: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation'
summary:
  en: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  zh: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation is a 2025 work on manipulation
    for humanoid robots.'
  ko: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation is a 2025 work on manipulation
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
- manipulation
- rgmp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.09141v2.
sources:
- id: src_001
  type: paper
  title: 'RGMP: Recurrent Geometric-prior Multimodal Policy for Generalizable Humanoid Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2511.09141
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussion adaptation.

## 核心内容
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussion adaptation.

## 参考
- http://arxiv.org/abs/2511.09141v2

## Overview
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussian adaptation.

## Content
Humanoid robots exhibit significant potential in executing diverse human-level skills. However, current research predominantly relies on data-driven approaches that necessitate extensive training datasets to achieve robust multimodal decision-making capabilities and generalizable visuomotor control. These methods raise concerns due to the neglect of geometric reasoning in unseen scenarios and the inefficient modeling of robot-target relationships within the training data, resulting in significant waste of training resources. To address these limitations, we present the Recurrent Geometric-prior Multimodal Policy (RGMP), an end-to-end framework that unifies geometric-semantic skill reasoning with data-efficient visuomotor control. For perception capabilities, we propose the Geometric-prior Skill Selector, which infuses geometric inductive biases into a vision language model, producing adaptive skill sequences for unseen scenes with minimal spatial common sense tuning. To achieve data-efficient robotic motion synthesis, we introduce the Adaptive Recursive Gaussian Network, which parameterizes robot-object interactions as a compact hierarchy of Gaussian processes that recursively encode multi-scale spatial relationships, yielding dexterous, data-efficient motion synthesis even from sparse demonstrations. Evaluated on both our humanoid robot and desktop dual-arm robot, the RGMP framework achieves 87% task success in generalization tests and exhibits 5x greater data efficiency than the state-of-the-art model. This performance underscores its superior cross-domain generalization, enabled by geometric-semantic reasoning and recursive-Gaussian adaptation.

## 개요
휴머노이드 로봇은 다양한 인간 수준의 기술을 실행하는 데 상당한 잠재력을 보여줍니다. 그러나 현재 연구는 주로 데이터 기반 접근 방식에 의존하며, 강력한 다중 모달 의사 결정 능력과 일반화 가능한 시각 운동 제어를 달성하기 위해 광범위한 훈련 데이터셋이 필요합니다. 이러한 방법은 보지 못한 시나리오에서 기하학적 추론을 무시하고 훈련 데이터 내 로봇-대상 관계의 비효율적인 모델링으로 인해 훈련 자원의 상당한 낭비를 초래하여 우려를 제기합니다. 이러한 한계를 해결하기 위해, 우리는 기하학-의미론적 기술 추론과 데이터 효율적인 시각 운동 제어를 통합하는 종단 간 프레임워크인 Recurrent Geometric-prior Multimodal Policy (RGMP)를 제시합니다. 인식 능력을 위해, 우리는 기하학적 귀납적 편향을 시각 언어 모델에 주입하여 최소한의 공간 상식 조정으로 보지 못한 장면에 대한 적응형 기술 시퀀스를 생성하는 Geometric-prior Skill Selector를 제안합니다. 데이터 효율적인 로봇 동작 합성을 달성하기 위해, 우리는 로봇-객체 상호 작용을 다중 스케일 공간 관계를 재귀적으로 인코딩하는 컴팩트한 가우시안 프로세스 계층 구조로 매개변수화하여 희소 시연에서도 능숙하고 데이터 효율적인 동작 합성을 제공하는 Adaptive Recursive Gaussian Network를 도입합니다. 우리의 휴머노이드 로봇과 데스크탑 이중 팔 로봇 모두에서 평가된 RGMP 프레임워크는 일반화 테스트에서 87%의 작업 성공률을 달성하고 최첨단 모델보다 5배 더 큰 데이터 효율성을 보여줍니다. 이 성능은 기하학-의미론적 추론과 재귀적 가우시안 적응에 의해 가능해진 뛰어난 교차 도메인 일반화를 강조합니다.

## 핵심 내용
휴머노이드 로봇은 다양한 인간 수준의 기술을 실행하는 데 상당한 잠재력을 보여줍니다. 그러나 현재 연구는 주로 데이터 기반 접근 방식에 의존하며, 강력한 다중 모달 의사 결정 능력과 일반화 가능한 시각 운동 제어를 달성하기 위해 광범위한 훈련 데이터셋이 필요합니다. 이러한 방법은 보지 못한 시나리오에서 기하학적 추론을 무시하고 훈련 데이터 내 로봇-대상 관계의 비효율적인 모델링으로 인해 훈련 자원의 상당한 낭비를 초래하여 우려를 제기합니다. 이러한 한계를 해결하기 위해, 우리는 기하학-의미론적 기술 추론과 데이터 효율적인 시각 운동 제어를 통합하는 종단 간 프레임워크인 Recurrent Geometric-prior Multimodal Policy (RGMP)를 제시합니다. 인식 능력을 위해, 우리는 기하학적 귀납적 편향을 시각 언어 모델에 주입하여 최소한의 공간 상식 조정으로 보지 못한 장면에 대한 적응형 기술 시퀀스를 생성하는 Geometric-prior Skill Selector를 제안합니다. 데이터 효율적인 로봇 동작 합성을 달성하기 위해, 우리는 로봇-객체 상호 작용을 다중 스케일 공간 관계를 재귀적으로 인코딩하는 컴팩트한 가우시안 프로세스 계층 구조로 매개변수화하여 희소 시연에서도 능숙하고 데이터 효율적인 동작 합성을 제공하는 Adaptive Recursive Gaussian Network를 도입합니다. 우리의 휴머노이드 로봇과 데스크탑 이중 팔 로봇 모두에서 평가된 RGMP 프레임워크는 일반화 테스트에서 87%의 작업 성공률을 달성하고 최첨단 모델보다 5배 더 큰 데이터 효율성을 보여줍니다. 이 성능은 기하학-의미론적 추론과 재귀적 가우시안 적응에 의해 가능해진 뛰어난 교차 도메인 일반화를 강조합니다.
