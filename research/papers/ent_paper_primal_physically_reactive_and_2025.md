---
$id: ent_paper_primal_physically_reactive_and_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning
  zh: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning
  ko: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning
summary:
  en: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning is a 2025 work on human motion analysis and
    synthesis for humanoid robots.
  zh: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning is a 2025 work on human motion analysis and
    synthesis for humanoid robots.
  ko: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning is a 2025 work on human motion analysis and
    synthesis for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- primal_physically_reactive_and
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.17544v2.
sources:
- id: src_001
  type: paper
  title: PRIMAL Physically Reactive and Interactive Motor Model for Avatar Learning (arXiv)
  url: https://arxiv.org/abs/2503.17544
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We formulate the motor system of an interactive avatar as a generative motion model that can drive the body to move through 3D space in a perpetual, realistic, controllable, and responsive manner. Although human motion generation has been extensively studied, many existing methods lack the responsiveness and realism of real human movements. Inspired by recent advances in foundation models, we propose PRIMAL, which is learned with a two-stage paradigm. In the pretraining stage, the model learns body movements from a large number of sub-second motion segments, providing a generative foundation from which more complex motions are built. This training is fully unsupervised without annotations. Given a single-frame initial state during inference, the pretrained model not only generates unbounded, realistic, and controllable motion, but also enables the avatar to be responsive to induced impulses in real time. In the adaptation phase, we employ a novel ControlNet-like adaptor to fine-tune the base model efficiently, adapting it to new tasks such as few-shot personalized action generation and spatial target reaching. Evaluations show that our proposed method outperforms state-of-the-art baselines. We leverage the model to create a real-time character animation system in Unreal Engine that feels highly responsive and natural. Code, models, and more results are available at: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## 核心内容
We formulate the motor system of an interactive avatar as a generative motion model that can drive the body to move through 3D space in a perpetual, realistic, controllable, and responsive manner. Although human motion generation has been extensively studied, many existing methods lack the responsiveness and realism of real human movements. Inspired by recent advances in foundation models, we propose PRIMAL, which is learned with a two-stage paradigm. In the pretraining stage, the model learns body movements from a large number of sub-second motion segments, providing a generative foundation from which more complex motions are built. This training is fully unsupervised without annotations. Given a single-frame initial state during inference, the pretrained model not only generates unbounded, realistic, and controllable motion, but also enables the avatar to be responsive to induced impulses in real time. In the adaptation phase, we employ a novel ControlNet-like adaptor to fine-tune the base model efficiently, adapting it to new tasks such as few-shot personalized action generation and spatial target reaching. Evaluations show that our proposed method outperforms state-of-the-art baselines. We leverage the model to create a real-time character animation system in Unreal Engine that feels highly responsive and natural. Code, models, and more results are available at: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## 参考
- http://arxiv.org/abs/2503.17544v2

## Overview
We formulate the motor system of an interactive avatar as a generative motion model that can drive the body to move through 3D space in a perpetual, realistic, controllable, and responsive manner. Although human motion generation has been extensively studied, many existing methods lack the responsiveness and realism of real human movements. Inspired by recent advances in foundation models, we propose PRIMAL, which is learned with a two-stage paradigm. In the pretraining stage, the model learns body movements from a large number of sub-second motion segments, providing a generative foundation from which more complex motions are built. This training is fully unsupervised without annotations. Given a single-frame initial state during inference, the pretrained model not only generates unbounded, realistic, and controllable motion, but also enables the avatar to be responsive to induced impulses in real time. In the adaptation phase, we employ a novel ControlNet-like adaptor to fine-tune the base model efficiently, adapting it to new tasks such as few-shot personalized action generation and spatial target reaching. Evaluations show that our proposed method outperforms state-of-the-art baselines. We leverage the model to create a real-time character animation system in Unreal Engine that feels highly responsive and natural. Code, models, and more results are available at: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## Content
We formulate the motor system of an interactive avatar as a generative motion model that can drive the body to move through 3D space in a perpetual, realistic, controllable, and responsive manner. Although human motion generation has been extensively studied, many existing methods lack the responsiveness and realism of real human movements. Inspired by recent advances in foundation models, we propose PRIMAL, which is learned with a two-stage paradigm. In the pretraining stage, the model learns body movements from a large number of sub-second motion segments, providing a generative foundation from which more complex motions are built. This training is fully unsupervised without annotations. Given a single-frame initial state during inference, the pretrained model not only generates unbounded, realistic, and controllable motion, but also enables the avatar to be responsive to induced impulses in real time. In the adaptation phase, we employ a novel ControlNet-like adaptor to fine-tune the base model efficiently, adapting it to new tasks such as few-shot personalized action generation and spatial target reaching. Evaluations show that our proposed method outperforms state-of-the-art baselines. We leverage the model to create a real-time character animation system in Unreal Engine that feels highly responsive and natural. Code, models, and more results are available at: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## 개요
우리는 인터랙티브 아바타의 운동 시스템을 생성적 동작 모델로 정식화하여, 신체가 3D 공간에서 영구적이고 현실적이며 제어 가능하고 반응적으로 움직이도록 구동합니다. 인간 동작 생성은 광범위하게 연구되어 왔지만, 많은 기존 방법들은 실제 인간 움직임의 반응성과 현실성을 결여하고 있습니다. 최근 기초 모델의 발전에서 영감을 받아, 우리는 PRIMAL을 제안하며, 이는 2단계 패러다임으로 학습됩니다. 사전 학습 단계에서 모델은 대량의 1초 미만 동작 세그먼트로부터 신체 움직임을 학습하여, 더 복잡한 동작이 구축되는 생성적 기반을 제공합니다. 이 학습은 주석 없이 완전히 비지도 방식으로 이루어집니다. 추론 중 단일 프레임 초기 상태가 주어지면, 사전 학습된 모델은 무한하고 현실적이며 제어 가능한 동작을 생성할 뿐만 아니라, 아바타가 유도된 충격에 실시간으로 반응할 수 있게 합니다. 적응 단계에서는 새로운 ControlNet 유사 어댑터를 사용하여 기본 모델을 효율적으로 미세 조정하며, 소수 샷 개인화 동작 생성 및 공간 목표 도달과 같은 새로운 작업에 적응시킵니다. 평가 결과, 우리의 제안 방법이 최신 기준선을 능가함을 보여줍니다. 우리는 이 모델을 활용하여 Unreal Engine에서 매우 반응적이고 자연스러운 실시간 캐릭터 애니메이션 시스템을 구축합니다. 코드, 모델 및 추가 결과는 다음에서 확인할 수 있습니다: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL

## 핵심 내용
우리는 인터랙티브 아바타의 운동 시스템을 생성적 동작 모델로 정식화하여, 신체가 3D 공간에서 영구적이고 현실적이며 제어 가능하고 반응적으로 움직이도록 구동합니다. 인간 동작 생성은 광범위하게 연구되어 왔지만, 많은 기존 방법들은 실제 인간 움직임의 반응성과 현실성을 결여하고 있습니다. 최근 기초 모델의 발전에서 영감을 받아, 우리는 PRIMAL을 제안하며, 이는 2단계 패러다임으로 학습됩니다. 사전 학습 단계에서 모델은 대량의 1초 미만 동작 세그먼트로부터 신체 움직임을 학습하여, 더 복잡한 동작이 구축되는 생성적 기반을 제공합니다. 이 학습은 주석 없이 완전히 비지도 방식으로 이루어집니다. 추론 중 단일 프레임 초기 상태가 주어지면, 사전 학습된 모델은 무한하고 현실적이며 제어 가능한 동작을 생성할 뿐만 아니라, 아바타가 유도된 충격에 실시간으로 반응할 수 있게 합니다. 적응 단계에서는 새로운 ControlNet 유사 어댑터를 사용하여 기본 모델을 효율적으로 미세 조정하며, 소수 샷 개인화 동작 생성 및 공간 목표 도달과 같은 새로운 작업에 적응시킵니다. 평가 결과, 우리의 제안 방법이 최신 기준선을 능가함을 보여줍니다. 우리는 이 모델을 활용하여 Unreal Engine에서 매우 반응적이고 자연스러운 실시간 캐릭터 애니메이션 시스템을 구축합니다. 코드, 모델 및 추가 결과는 다음에서 확인할 수 있습니다: https://yz-cnsdqz.github.io/eigenmotion/PRIMAL
