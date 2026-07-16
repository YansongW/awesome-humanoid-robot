---
$id: ent_paper_synagent_generalizable_coopera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy'
  zh: SynAgent｜通过单独与合作的智能体协同进行可推广的合作人形操作
  ko: 'SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy'
summary:
  en: Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due
    to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this
    paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation
    by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent
    human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving
    retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial
    relationships among humans and objects. Building upon this refined da
  zh: SynAgent 先从相机图像/多视角观测恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、地形/场景表征。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: SynAgent 先从相机图像/多视角观测恢复场景、目标或运动表征，再用教师-学生知识迁移、PPO/RL 策略训练、扩散策略/流匹配生成全身轨迹/动作序列、地形/场景表征。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- mobile_manipulation
- scene_understanding
- synagent
- vision_guided_control
- visual_perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: SynAgent: Generalizable
    Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy.'
sources:
- id: src_001
  type: website
  title: SynAgent project page
  url: https://yw0208.github.io/synagent/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## 核心内容
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## 参考
- Semantic Scholar search: SynAgent: Generalizable Cooperative Humanoid Manipulation via Solo-to-Cooperative Agent Synergy

## Overview
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## Content
Controllable cooperative humanoid manipulation is a fundamental yet challenging problem for embodied intelligence, due to severe data scarcity, complexities in multi-agent coordination, and limited generalization across objects. In this paper, we present SynAgent, a unified framework that enables scalable and physically plausible cooperative manipulation by leveraging Solo-to-Cooperative Agent Synergy to transfer skills from single-agent human-object interaction to multi-agent human-object-human scenarios. To maintain semantic integrity during motion transfer, we introduce an interaction-preserving retargeting method based on an Interact Mesh constructed via Delaunay tetrahedralization, which faithfully maintains spatial relationships among humans and objects. Building upon this refined data, we propose a single-agent pretraining and adaptation paradigm that bootstraps synergistic collaborative behaviors from abundant single-human data through decentralized training and multi-agent PPO. Finally, we develop a trajectory-conditioned generative policy using a conditional VAE, trained via multi-teacher distillation from motion imitation priors to achieve stable and controllable object-level trajectory execution. Extensive experiments demonstrate that SynAgent significantly outperforms existing baselines in both cooperative imitation and trajectory-conditioned control, while generalizing across diverse object geometries. Codes and data will be available after publication. Project Page: http://yw0208.github.io/synagent

## 개요
제어 가능한 협력적 휴머노이드 조작은 심각한 데이터 부족, 다중 에이전트 협력의 복잡성, 그리고 객체 간 일반화의 한계로 인해 구현 지능(embodied intelligence)의 근본적이면서도 어려운 문제입니다. 본 논문에서는 단일 에이전트-객체 상호작용에서 다중 에이전트 인간-객체-인간 시나리오로 기술을 전이하기 위해 Solo-to-Cooperative Agent Synergy를 활용하여 확장 가능하고 물리적으로 타당한 협력 조작을 가능하게 하는 통합 프레임워크인 SynAgent를 제시합니다. 동작 전이 중 의미적 무결성을 유지하기 위해, Delaunay 사면체화를 통해 구축된 Interact Mesh를 기반으로 하는 상호작용 보존 리타겟팅 방법을 도입하여 인간과 객체 간의 공간적 관계를 충실히 유지합니다. 이 정제된 데이터를 기반으로, 분산 훈련과 다중 에이전트 PPO를 통해 풍부한 단일 인간 데이터로부터 시너지 협력 행동을 부트스트래핑하는 단일 에이전트 사전 훈련 및 적응 패러다임을 제안합니다. 마지막으로, 조건부 VAE를 사용한 궤적 조건 생성 정책을 개발하고, 동작 모방 사전 정보로부터 다중 교사 증류를 통해 훈련하여 안정적이고 제어 가능한 객체 수준 궤적 실행을 달성합니다. 광범위한 실험을 통해 SynAgent가 협력 모방과 궤적 조건 제어 모두에서 기존 기준선을 크게 능가하며, 다양한 객체 형상에 걸쳐 일반화됨을 입증합니다. 코드와 데이터는 출판 후 공개될 예정입니다. 프로젝트 페이지: http://yw0208.github.io/synagent

## 핵심 내용
제어 가능한 협력적 휴머노이드 조작은 심각한 데이터 부족, 다중 에이전트 협력의 복잡성, 그리고 객체 간 일반화의 한계로 인해 구현 지능(embodied intelligence)의 근본적이면서도 어려운 문제입니다. 본 논문에서는 단일 에이전트-객체 상호작용에서 다중 에이전트 인간-객체-인간 시나리오로 기술을 전이하기 위해 Solo-to-Cooperative Agent Synergy를 활용하여 확장 가능하고 물리적으로 타당한 협력 조작을 가능하게 하는 통합 프레임워크인 SynAgent를 제시합니다. 동작 전이 중 의미적 무결성을 유지하기 위해, Delaunay 사면체화를 통해 구축된 Interact Mesh를 기반으로 하는 상호작용 보존 리타겟팅 방법을 도입하여 인간과 객체 간의 공간적 관계를 충실히 유지합니다. 이 정제된 데이터를 기반으로, 분산 훈련과 다중 에이전트 PPO를 통해 풍부한 단일 인간 데이터로부터 시너지 협력 행동을 부트스트래핑하는 단일 에이전트 사전 훈련 및 적응 패러다임을 제안합니다. 마지막으로, 조건부 VAE를 사용한 궤적 조건 생성 정책을 개발하고, 동작 모방 사전 정보로부터 다중 교사 증류를 통해 훈련하여 안정적이고 제어 가능한 객체 수준 궤적 실행을 달성합니다. 광범위한 실험을 통해 SynAgent가 협력 모방과 궤적 조건 제어 모두에서 기존 기준선을 크게 능가하며, 다양한 객체 형상에 걸쳐 일반화됨을 입증합니다. 코드와 데이터는 출판 후 공개될 예정입니다. 프로젝트 페이지: http://yw0208.github.io/synagent
