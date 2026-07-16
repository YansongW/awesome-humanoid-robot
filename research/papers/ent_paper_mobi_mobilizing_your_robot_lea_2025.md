---
$id: ent_paper_mobi_mobilizing_your_robot_lea_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mobi-π: Mobilizing Your Robot Learning Policy'
  zh: 'Mobi-π: Mobilizing Your Robot Learning Policy'
  ko: 'Mobi-π: Mobilizing Your Robot Learning Policy'
summary:
  en: 'Mobi-π: Mobilizing Your Robot Learning Policy is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  zh: 'Mobi-π: Mobilizing Your Robot Learning Policy is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
  ko: 'Mobi-π: Mobilizing Your Robot Learning Policy is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.'
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
- loco_manipulation
- mobi
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.23692v2.
sources:
- id: src_001
  type: paper
  title: 'Mobi-π: Mobilizing Your Robot Learning Policy (arXiv)'
  url: https://arxiv.org/abs/2505.23692
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Mobi-π: Mobilizing Your Robot Learning Policy project page'
  url: https://mobipi.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learned visuomotor policies are capable of performing increasingly complex manipulation tasks. However, most of these policies are trained on data collected from limited robot positions and camera viewpoints. This leads to poor generalization to novel robot positions, which limits the use of these policies on mobile platforms, especially for precise tasks like pressing buttons or turning faucets. In this work, we formulate the policy mobilization problem: find a mobile robot base pose in a novel environment that is in distribution with respect to a manipulation policy trained on a limited set of camera viewpoints. Compared to retraining the policy itself to be more robust to unseen robot base pose initializations, policy mobilization decouples navigation from manipulation and thus does not require additional demonstrations. Crucially, this problem formulation complements existing efforts to improve manipulation policy robustness to novel viewpoints and remains compatible with them. We propose a novel approach for policy mobilization that bridges navigation and manipulation by optimizing the robot's base pose to align with an in-distribution base pose for a learned policy. Our approach utilizes 3D Gaussian Splatting for novel view synthesis, a score function to evaluate pose suitability, and sampling-based optimization to identify optimal robot poses. To understand policy mobilization in more depth, we also introduce the Mobi-$π$ framework, which includes: (1) metrics that quantify the difficulty of mobilizing a given policy, (2) a suite of simulated mobile manipulation tasks based on RoboCasa to evaluate policy mobilization, and (3) visualization tools for analysis. In both our developed simulation task suite and the real world, we show that our approach outperforms baselines, demonstrating its effectiveness for policy mobilization.

## 核心内容
Learned visuomotor policies are capable of performing increasingly complex manipulation tasks. However, most of these policies are trained on data collected from limited robot positions and camera viewpoints. This leads to poor generalization to novel robot positions, which limits the use of these policies on mobile platforms, especially for precise tasks like pressing buttons or turning faucets. In this work, we formulate the policy mobilization problem: find a mobile robot base pose in a novel environment that is in distribution with respect to a manipulation policy trained on a limited set of camera viewpoints. Compared to retraining the policy itself to be more robust to unseen robot base pose initializations, policy mobilization decouples navigation from manipulation and thus does not require additional demonstrations. Crucially, this problem formulation complements existing efforts to improve manipulation policy robustness to novel viewpoints and remains compatible with them. We propose a novel approach for policy mobilization that bridges navigation and manipulation by optimizing the robot's base pose to align with an in-distribution base pose for a learned policy. Our approach utilizes 3D Gaussian Splatting for novel view synthesis, a score function to evaluate pose suitability, and sampling-based optimization to identify optimal robot poses. To understand policy mobilization in more depth, we also introduce the Mobi-$π$ framework, which includes: (1) metrics that quantify the difficulty of mobilizing a given policy, (2) a suite of simulated mobile manipulation tasks based on RoboCasa to evaluate policy mobilization, and (3) visualization tools for analysis. In both our developed simulation task suite and the real world, we show that our approach outperforms baselines, demonstrating its effectiveness for policy mobilization.

## 参考
- http://arxiv.org/abs/2505.23692v2

## Overview
Learned visuomotor policies are capable of performing increasingly complex manipulation tasks. However, most of these policies are trained on data collected from limited robot positions and camera viewpoints. This leads to poor generalization to novel robot positions, which limits the use of these policies on mobile platforms, especially for precise tasks like pressing buttons or turning faucets. In this work, we formulate the policy mobilization problem: find a mobile robot base pose in a novel environment that is in distribution with respect to a manipulation policy trained on a limited set of camera viewpoints. Compared to retraining the policy itself to be more robust to unseen robot base pose initializations, policy mobilization decouples navigation from manipulation and thus does not require additional demonstrations. Crucially, this problem formulation complements existing efforts to improve manipulation policy robustness to novel viewpoints and remains compatible with them. We propose a novel approach for policy mobilization that bridges navigation and manipulation by optimizing the robot's base pose to align with an in-distribution base pose for a learned policy. Our approach utilizes 3D Gaussian Splatting for novel view synthesis, a score function to evaluate pose suitability, and sampling-based optimization to identify optimal robot poses. To understand policy mobilization in more depth, we also introduce the Mobi-$π$ framework, which includes: (1) metrics that quantify the difficulty of mobilizing a given policy, (2) a suite of simulated mobile manipulation tasks based on RoboCasa to evaluate policy mobilization, and (3) visualization tools for analysis. In both our developed simulation task suite and the real world, we show that our approach outperforms baselines, demonstrating its effectiveness for policy mobilization.

## Content
Learned visuomotor policies are capable of performing increasingly complex manipulation tasks. However, most of these policies are trained on data collected from limited robot positions and camera viewpoints. This leads to poor generalization to novel robot positions, which limits the use of these policies on mobile platforms, especially for precise tasks like pressing buttons or turning faucets. In this work, we formulate the policy mobilization problem: find a mobile robot base pose in a novel environment that is in distribution with respect to a manipulation policy trained on a limited set of camera viewpoints. Compared to retraining the policy itself to be more robust to unseen robot base pose initializations, policy mobilization decouples navigation from manipulation and thus does not require additional demonstrations. Crucially, this problem formulation complements existing efforts to improve manipulation policy robustness to novel viewpoints and remains compatible with them. We propose a novel approach for policy mobilization that bridges navigation and manipulation by optimizing the robot's base pose to align with an in-distribution base pose for a learned policy. Our approach utilizes 3D Gaussian Splatting for novel view synthesis, a score function to evaluate pose suitability, and sampling-based optimization to identify optimal robot poses. To understand policy mobilization in more depth, we also introduce the Mobi-$π$ framework, which includes: (1) metrics that quantify the difficulty of mobilizing a given policy, (2) a suite of simulated mobile manipulation tasks based on RoboCasa to evaluate policy mobilization, and (3) visualization tools for analysis. In both our developed simulation task suite and the real world, we show that our approach outperforms baselines, demonstrating its effectiveness for policy mobilization.

## 개요
학습된 시각-운동 정책(Learned visuomotor policies)은 점점 더 복잡한 조작 작업을 수행할 수 있습니다. 그러나 이러한 정책의 대부분은 제한된 로봇 위치와 카메라 시점에서 수집된 데이터로 훈련됩니다. 이는 새로운 로봇 위치에 대한 일반화 성능이 낮아져, 특히 버튼 누르기나 수도꼭지 돌리기와 같은 정밀 작업에서 모바일 플랫폼에서의 사용을 제한합니다. 본 연구에서는 정책 모빌리제이션(policy mobilization) 문제를 정식화합니다: 제한된 카메라 시점에서 훈련된 조작 정책과 분포 내(in-distribution)에 있는 새로운 환경에서 모바일 로봇의 베이스 포즈(base pose)를 찾는 것입니다. 보이지 않는 로봇 베이스 포즈 초기화에 더 강건하도록 정책 자체를 재훈련하는 것과 비교하여, 정책 모빌리제이션은 내비게이션과 조작을 분리하므로 추가적인 시연이 필요하지 않습니다. 결정적으로, 이 문제 정식화는 새로운 시점에 대한 조작 정책 강건성을 개선하려는 기존 노력을 보완하며, 이들과 호환됩니다. 우리는 학습된 정책에 대한 분포 내 베이스 포즈와 일치하도록 로봇의 베이스 포즈를 최적화함으로써 내비게이션과 조작을 연결하는 새로운 정책 모빌리제이션 접근법을 제안합니다. 우리의 접근법은 새로운 시점 합성을 위한 3D Gaussian Splatting, 포즈 적합성을 평가하는 점수 함수, 그리고 최적의 로봇 포즈를 식별하기 위한 샘플링 기반 최적화를 활용합니다. 정책 모빌리제이션을 더 깊이 이해하기 위해, 우리는 Mobi-$π$ 프레임워크도 소개합니다. 이 프레임워크는 (1) 주어진 정책을 모빌리제이션하는 난이도를 정량화하는 메트릭, (2) 정책 모빌리제이션을 평가하기 위한 RoboCasa 기반의 시뮬레이션 모바일 조작 작업 모음, (3) 분석을 위한 시각화 도구를 포함합니다. 우리가 개발한 시뮬레이션 작업 모음과 실제 환경 모두에서, 우리의 접근법이 기준선보다 우수함을 보여주며, 정책 모빌리제이션에 대한 효과성을 입증합니다.

## 핵심 내용
학습된 시각-운동 정책은 점점 더 복잡한 조작 작업을 수행할 수 있습니다. 그러나 이러한 정책의 대부분은 제한된 로봇 위치와 카메라 시점에서 수집된 데이터로 훈련됩니다. 이는 새로운 로봇 위치에 대한 일반화 성능이 낮아져, 특히 버튼 누르기나 수도꼭지 돌리기와 같은 정밀 작업에서 모바일 플랫폼에서의 사용을 제한합니다. 본 연구에서는 정책 모빌리제이션 문제를 정식화합니다: 제한된 카메라 시점에서 훈련된 조작 정책과 분포 내에 있는 새로운 환경에서 모바일 로봇의 베이스 포즈를 찾는 것입니다. 보이지 않는 로봇 베이스 포즈 초기화에 더 강건하도록 정책 자체를 재훈련하는 것과 비교하여, 정책 모빌리제이션은 내비게이션과 조작을 분리하므로 추가적인 시연이 필요하지 않습니다. 결정적으로, 이 문제 정식화는 새로운 시점에 대한 조작 정책 강건성을 개선하려는 기존 노력을 보완하며, 이들과 호환됩니다. 우리는 학습된 정책에 대한 분포 내 베이스 포즈와 일치하도록 로봇의 베이스 포즈를 최적화함으로써 내비게이션과 조작을 연결하는 새로운 정책 모빌리제이션 접근법을 제안합니다. 우리의 접근법은 새로운 시점 합성을 위한 3D Gaussian Splatting, 포즈 적합성을 평가하는 점수 함수, 그리고 최적의 로봇 포즈를 식별하기 위한 샘플링 기반 최적화를 활용합니다. 정책 모빌리제이션을 더 깊이 이해하기 위해, 우리는 Mobi-$π$ 프레임워크도 소개합니다. 이 프레임워크는 (1) 주어진 정책을 모빌리제이션하는 난이도를 정량화하는 메트릭, (2) 정책 모빌리제이션을 평가하기 위한 RoboCasa 기반의 시뮬레이션 모바일 조작 작업 모음, (3) 분석을 위한 시각화 도구를 포함합니다. 우리가 개발한 시뮬레이션 작업 모음과 실제 환경 모두에서, 우리의 접근법이 기준선보다 우수함을 보여주며, 정책 모빌리제이션에 대한 효과성을 입증합니다.
