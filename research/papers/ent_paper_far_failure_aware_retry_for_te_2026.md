---
$id: ent_paper_far_failure_aware_retry_for_te_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement'
  zh: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement'
  ko: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement'
summary:
  en: 'arXiv:2607.01111v1 Announce Type: new Abstract: Robot policies inevitably encounter failures when deployed in real
    environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention.
    In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at
    test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive
    Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously
    unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further
    incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both
    simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average
    gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly
    improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative
    failure cases.'
  zh: 'arXiv:2607.01111v1 Announce Type: new Abstract: Robot policies inevitably encounter failures when deployed in real
    environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention.
    In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at
    test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive
    Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously
    unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further
    incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both
    simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average
    gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly
    improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative
    failure cases.'
  ko: 'arXiv:2607.01111v1 Announce Type: new Abstract: Robot policies inevitably encounter failures when deployed in real
    environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention.
    In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at
    test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive
    Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously
    unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further
    incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both
    simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average
    gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly
    improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative
    failure cases.'
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
- robotics
- far
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.01111v1.
sources:
- id: src_001
  type: paper
  title: 'FAR: Failure-Aware Retry for Test-Time Recovery and Continual Policy Improvement (arXiv)'
  url: https://arxiv.org/abs/2607.01111
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative failure cases.

## 核心内容
Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative failure cases.

## 参考
- http://arxiv.org/abs/2607.01111v1

## Overview
Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative failure cases.

## Content
Robot policies inevitably encounter failures when deployed in real environments. Naive retries often repeat the same mistakes, while many existing recovery methods rely on human intervention. In this paper, we propose Failure-Aware Retry (FAR), a framework that enables robots to learn from previous failures at test time, adapt their behavior accordingly, and eventually complete the task autonomously. FAR combines Failure-Contrastive Preference Adaptation, which constructs preference learning data from failures to steer the policy away from previously unsuccessful behaviors, with lightweight action perturbations during retries to encourage local exploration. We further incorporate successful recovery trajectories into a training loop for continual policy improvement. Experiments in both simulation and real-world manipulation tasks show that FAR substantially improves success rates and robustness, with average gains of 17.6% over the standard diffusion policy in simulation and 11.7% in the real world. In addition, FAR significantly improves data efficiency under both reset and timestep budgets during continual policy improvement by exploiting informative failure cases.

## 개요
로봇 정책은 실제 환경에 배치될 때 필연적으로 실패에 직면합니다. 단순한 재시도는 종종 동일한 실수를 반복하는 반면, 기존의 많은 복구 방법은 인간의 개입에 의존합니다. 본 논문에서는 테스트 시점에서 이전 실패로부터 학습하고, 이에 따라 행동을 조정하며, 궁극적으로 자율적으로 작업을 완료할 수 있는 프레임워크인 Failure-Aware Retry (FAR)를 제안합니다. FAR은 실패로부터 선호 학습 데이터를 구성하여 정책이 이전의 실패한 행동에서 벗어나도록 유도하는 Failure-Contrastive Preference Adaptation과 재시도 중 경량의 행동 섭동을 결합하여 국소적 탐색을 장려합니다. 또한 성공적인 복구 궤적을 훈련 루프에 통합하여 지속적인 정책 개선을 수행합니다. 시뮬레이션 및 실제 조작 작업 모두에서의 실험 결과, FAR은 표준 확산 정책 대비 시뮬레이션에서 평균 17.6%, 실제 환경에서 11.7%의 성공률 및 견고성 향상을 보여줍니다. 또한 FAR은 정보를 제공하는 실패 사례를 활용하여 지속적인 정책 개선 중 리셋 및 타임스텝 예산 하에서 데이터 효율성을 크게 향상시킵니다.

## 핵심 내용
로봇 정책은 실제 환경에 배치될 때 필연적으로 실패에 직면합니다. 단순한 재시도는 종종 동일한 실수를 반복하는 반면, 기존의 많은 복구 방법은 인간의 개입에 의존합니다. 본 논문에서는 테스트 시점에서 이전 실패로부터 학습하고, 이에 따라 행동을 조정하며, 궁극적으로 자율적으로 작업을 완료할 수 있는 프레임워크인 Failure-Aware Retry (FAR)를 제안합니다. FAR은 실패로부터 선호 학습 데이터를 구성하여 정책이 이전의 실패한 행동에서 벗어나도록 유도하는 Failure-Contrastive Preference Adaptation과 재시도 중 경량의 행동 섭동을 결합하여 국소적 탐색을 장려합니다. 또한 성공적인 복구 궤적을 훈련 루프에 통합하여 지속적인 정책 개선을 수행합니다. 시뮬레이션 및 실제 조작 작업 모두에서의 실험 결과, FAR은 표준 확산 정책 대비 시뮬레이션에서 평균 17.6%, 실제 환경에서 11.7%의 성공률 및 견고성 향상을 보여줍니다. 또한 FAR은 정보를 제공하는 실패 사례를 활용하여 지속적인 정책 개선 중 리셋 및 타임스텝 예산 하에서 데이터 효율성을 크게 향상시킵니다.
