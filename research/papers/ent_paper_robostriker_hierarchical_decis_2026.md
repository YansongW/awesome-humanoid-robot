---
$id: ent_paper_robostriker_hierarchical_decis_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing'
  zh: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing'
  ko: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing'
summary:
  en: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing is a 2026 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing is a 2026 work on loco-manipulation and whole-body-control
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
- loco_manipulation
- robostriker
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.22517v1.
sources:
- id: src_001
  type: paper
  title: 'RoboStriker: Hierarchical Decision-Making for Autonomous Humanoid Boxing (arXiv)'
  url: https://arxiv.org/abs/2601.22517
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Achieving human-level competitive intelligence and physical agility in humanoid robots remains a major challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning (MARL) offers a principled framework for strategic interaction, its direct application to humanoid control is hindered by high-dimensional contact dynamics and the absence of strong physical motion priors. We propose RoboStriker, a hierarchical three-stage framework that enables fully autonomous humanoid boxing by decoupling high-level strategic reasoning from low-level physical execution. The framework first learns a comprehensive repertoire of boxing skills by training a single-agent motion tracker on human motion capture data. These skills are subsequently distilled into a structured latent manifold, regularized by projecting the Gaussian-parameterized distribution onto a unit hypersphere. This topological constraint effectively confines exploration to the subspace of physically plausible motions. In the final stage, we introduce Latent-Space Neural Fictitious Self-Play (LS-NFSP), where competing agents learn competitive tactics by interacting within the latent action space rather than the raw motor space, significantly stabilizing multi-agent training. Experimental results demonstrate that RoboStriker achieves superior competitive performance in simulation and exhibits sim-to-real transfer. Our website is available at RoboStriker.

## 核心内容
Achieving human-level competitive intelligence and physical agility in humanoid robots remains a major challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning (MARL) offers a principled framework for strategic interaction, its direct application to humanoid control is hindered by high-dimensional contact dynamics and the absence of strong physical motion priors. We propose RoboStriker, a hierarchical three-stage framework that enables fully autonomous humanoid boxing by decoupling high-level strategic reasoning from low-level physical execution. The framework first learns a comprehensive repertoire of boxing skills by training a single-agent motion tracker on human motion capture data. These skills are subsequently distilled into a structured latent manifold, regularized by projecting the Gaussian-parameterized distribution onto a unit hypersphere. This topological constraint effectively confines exploration to the subspace of physically plausible motions. In the final stage, we introduce Latent-Space Neural Fictitious Self-Play (LS-NFSP), where competing agents learn competitive tactics by interacting within the latent action space rather than the raw motor space, significantly stabilizing multi-agent training. Experimental results demonstrate that RoboStriker achieves superior competitive performance in simulation and exhibits sim-to-real transfer. Our website is available at RoboStriker.

## 参考
- http://arxiv.org/abs/2601.22517v1

## Overview
Achieving human-level competitive intelligence and physical agility in humanoid robots remains a major challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning (MARL) offers a principled framework for strategic interaction, its direct application to humanoid control is hindered by high-dimensional contact dynamics and the absence of strong physical motion priors. We propose RoboStriker, a hierarchical three-stage framework that enables fully autonomous humanoid boxing by decoupling high-level strategic reasoning from low-level physical execution. The framework first learns a comprehensive repertoire of boxing skills by training a single-agent motion tracker on human motion capture data. These skills are subsequently distilled into a structured latent manifold, regularized by projecting the Gaussian-parameterized distribution onto a unit hypersphere. This topological constraint effectively confines exploration to the subspace of physically plausible motions. In the final stage, we introduce Latent-Space Neural Fictitious Self-Play (LS-NFSP), where competing agents learn competitive tactics by interacting within the latent action space rather than the raw motor space, significantly stabilizing multi-agent training. Experimental results demonstrate that RoboStriker achieves superior competitive performance in simulation and exhibits sim-to-real transfer. Our website is available at RoboStriker.

## Content
Achieving human-level competitive intelligence and physical agility in humanoid robots remains a major challenge, particularly in contact-rich and highly dynamic tasks such as boxing. While Multi-Agent Reinforcement Learning (MARL) offers a principled framework for strategic interaction, its direct application to humanoid control is hindered by high-dimensional contact dynamics and the absence of strong physical motion priors. We propose RoboStriker, a hierarchical three-stage framework that enables fully autonomous humanoid boxing by decoupling high-level strategic reasoning from low-level physical execution. The framework first learns a comprehensive repertoire of boxing skills by training a single-agent motion tracker on human motion capture data. These skills are subsequently distilled into a structured latent manifold, regularized by projecting the Gaussian-parameterized distribution onto a unit hypersphere. This topological constraint effectively confines exploration to the subspace of physically plausible motions. In the final stage, we introduce Latent-Space Neural Fictitious Self-Play (LS-NFSP), where competing agents learn competitive tactics by interacting within the latent action space rather than the raw motor space, significantly stabilizing multi-agent training. Experimental results demonstrate that RoboStriker achieves superior competitive performance in simulation and exhibits sim-to-real transfer. Our website is available at RoboStriker.

## 개요
휴머노이드 로봇에서 인간 수준의 경쟁 지능과 신체적 민첩성을 달성하는 것은 특히 복싱과 같은 접촉이 많고 역동성이 높은 작업에서 여전히 주요 과제로 남아 있습니다. 다중 에이전트 강화 학습(MARL)은 전략적 상호작용을 위한 원칙적인 프레임워크를 제공하지만, 이를 휴머노이드 제어에 직접 적용하는 것은 고차원 접촉 역학과 강력한 물리적 운동 사전 지식의 부재로 인해 어려움을 겪습니다. 우리는 고수준의 전략적 추론을 저수준의 물리적 실행에서 분리하여 완전 자율적인 휴머노이드 복싱을 가능하게 하는 계층적 3단계 프레임워크인 RoboStriker를 제안합니다. 이 프레임워크는 먼저 인간 모션 캡처 데이터에서 단일 에이전트 모션 트래커를 훈련하여 포괄적인 복싱 기술 레퍼토리를 학습합니다. 이러한 기술은 이후 가우시안 매개변수화된 분포를 단위 초구에 투영하여 정규화된 구조화된 잠재 매니폴드로 증류됩니다. 이 위상적 제약은 탐색을 물리적으로 타당한 움직임의 부분 공간으로 효과적으로 제한합니다. 마지막 단계에서는 잠재 공간 신경 가상 자기 대결(LS-NFSP)을 도입하여 경쟁 에이전트가 원시 모터 공간이 아닌 잠재 행동 공간 내에서 상호작용하며 경쟁 전술을 학습하도록 하여 다중 에이전트 훈련을 크게 안정화합니다. 실험 결과는 RoboStriker가 시뮬레이션에서 우수한 경쟁 성능을 달성하고 시뮬레이션-실제 전이를 보여줍니다. 저희 웹사이트는 RoboStriker에서 확인할 수 있습니다.

## 핵심 내용
휴머노이드 로봇에서 인간 수준의 경쟁 지능과 신체적 민첩성을 달성하는 것은 특히 복싱과 같은 접촉이 많고 역동성이 높은 작업에서 여전히 주요 과제로 남아 있습니다. 다중 에이전트 강화 학습(MARL)은 전략적 상호작용을 위한 원칙적인 프레임워크를 제공하지만, 이를 휴머노이드 제어에 직접 적용하는 것은 고차원 접촉 역학과 강력한 물리적 운동 사전 지식의 부재로 인해 어려움을 겪습니다. 우리는 고수준의 전략적 추론을 저수준의 물리적 실행에서 분리하여 완전 자율적인 휴머노이드 복싱을 가능하게 하는 계층적 3단계 프레임워크인 RoboStriker를 제안합니다. 이 프레임워크는 먼저 인간 모션 캡처 데이터에서 단일 에이전트 모션 트래커를 훈련하여 포괄적인 복싱 기술 레퍼토리를 학습합니다. 이러한 기술은 이후 가우시안 매개변수화된 분포를 단위 초구에 투영하여 정규화된 구조화된 잠재 매니폴드로 증류됩니다. 이 위상적 제약은 탐색을 물리적으로 타당한 움직임의 부분 공간으로 효과적으로 제한합니다. 마지막 단계에서는 잠재 공간 신경 가상 자기 대결(LS-NFSP)을 도입하여 경쟁 에이전트가 원시 모터 공간이 아닌 잠재 행동 공간 내에서 상호작용하며 경쟁 전술을 학습하도록 하여 다중 에이전트 훈련을 크게 안정화합니다. 실험 결과는 RoboStriker가 시뮬레이션에서 우수한 경쟁 성능을 달성하고 시뮬레이션-실제 전이를 보여줍니다. 저희 웹사이트는 RoboStriker에서 확인할 수 있습니다.
