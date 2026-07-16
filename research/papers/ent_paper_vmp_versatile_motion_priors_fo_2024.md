---
$id: ent_paper_vmp_versatile_motion_priors_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
  zh: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
  ko: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters'
summary:
  en: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters is a 2024 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- vmp
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: Summary backfilled by scripts/backfill_report_summaries.py from https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/.
sources:
- id: src_001
  type: website
  title: 'VMP: Versatile Motion Priors for Robustly Tracking Motion on Physical Characters project page'
  url: https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## 核心内容
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## 参考
- https://la.disneyresearch.com/publication/vmp-versatile-motion-priors-for-robustly-tracking-motion-on-physical-characters/

## Overview
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## Content
Recent progress in physics-based character control has made it possible to learn policies from unstructured motion data. However, it remains challenging to train a single control policy that works with diverse and unseen motions, and can be deployed to real-world physical robots. In this paper, we propose a two-stage technique that enables the control of a character with a full-body kinematic motion reference, with a focus on imitation accuracy. In a first stage, we extract a latent space encoding by training a variational autoencoder, taking short windows of motion from unstructured data as input. We then use the embedding from the time-varying latent code to train a conditional policy in a second stage, providing a mapping from kinematic input to dynamics-aware output. By keeping the two stages separate, we benefit from self-supervised methods to get better latent codes and explicit imitation rewards to avoid mode collapse. We demonstrate the efficiency and robustness of our method in simulation, with unseen user-specified motions, and on a bipedal robot, where we bring dynamic motions to the real world.

## 개요
물리 기반 캐릭터 제어의 최근 발전으로 비정형 동작 데이터로부터 정책을 학습하는 것이 가능해졌습니다. 그러나 다양하고 보지 못한 동작에서 작동하며 실제 물리적 로봇에 배포할 수 있는 단일 제어 정책을 훈련하는 것은 여전히 어려운 과제입니다. 본 논문에서는 전신 운동학적 동작 참조를 통해 캐릭터를 제어할 수 있는 2단계 기법을 제안하며, 모방 정확도에 중점을 둡니다. 첫 번째 단계에서는 비정형 데이터의 짧은 동작 윈도우를 입력으로 받아 변분 오토인코더를 훈련시켜 잠재 공간 인코딩을 추출합니다. 그런 다음 두 번째 단계에서 시간에 따라 변하는 잠재 코드의 임베딩을 사용하여 조건부 정책을 훈련하며, 운동학적 입력에서 동역학 인식 출력으로의 매핑을 제공합니다. 두 단계를 분리함으로써 자기 지도 학습 방법을 활용하여 더 나은 잠재 코드를 얻고 명시적 모방 보상을 통해 모드 붕괴를 방지합니다. 우리는 시뮬레이션, 보지 못한 사용자 지정 동작, 그리고 이족 보행 로봇에서 동적 동작을 실제 세계로 구현하는 실험을 통해 제안 방법의 효율성과 강건성을 입증합니다.

## 핵심 내용
물리 기반 캐릭터 제어의 최근 발전으로 비정형 동작 데이터로부터 정책을 학습하는 것이 가능해졌습니다. 그러나 다양하고 보지 못한 동작에서 작동하며 실제 물리적 로봇에 배포할 수 있는 단일 제어 정책을 훈련하는 것은 여전히 어려운 과제입니다. 본 논문에서는 전신 운동학적 동작 참조를 통해 캐릭터를 제어할 수 있는 2단계 기법을 제안하며, 모방 정확도에 중점을 둡니다. 첫 번째 단계에서는 비정형 데이터의 짧은 동작 윈도우를 입력으로 받아 변분 오토인코더를 훈련시켜 잠재 공간 인코딩을 추출합니다. 그런 다음 두 번째 단계에서 시간에 따라 변하는 잠재 코드의 임베딩을 사용하여 조건부 정책을 훈련하며, 운동학적 입력에서 동역학 인식 출력으로의 매핑을 제공합니다. 두 단계를 분리함으로써 자기 지도 학습 방법을 활용하여 더 나은 잠재 코드를 얻고 명시적 모방 보상을 통해 모드 붕괴를 방지합니다. 우리는 시뮬레이션, 보지 못한 사용자 지정 동작, 그리고 이족 보행 로봇에서 동적 동작을 실제 세계로 구현하는 실험을 통해 제안 방법의 효율성과 강건성을 입증합니다.
