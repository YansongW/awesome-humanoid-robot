---
$id: ent_paper_from_grasps_to_dexterity_large_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
  zh: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
  ko: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
summary:
  en: 'arXiv:2606.30749v1 Announce Type: new Abstract: Large-scale dexterous grasp datasets encode rich priors over hand-object
    interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether
    such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain
    contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level
    hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining
    dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is
    then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark
    with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments,
    our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the
    real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can
    serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation.
    Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .'
  zh: 'arXiv:2606.30749v1 Announce Type: new Abstract: Large-scale dexterous grasp datasets encode rich priors over hand-object
    interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether
    such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain
    contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level
    hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining
    dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is
    then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark
    with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments,
    our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the
    real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can
    serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation.
    Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .'
  ko: 'arXiv:2606.30749v1 Announce Type: new Abstract: Large-scale dexterous grasp datasets encode rich priors over hand-object
    interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether
    such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain
    contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level
    hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining
    dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is
    then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark
    with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments,
    our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the
    real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can
    serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation.
    Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- from_grasps_to_dexterity
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.30749v1.
sources:
- id: src_001
  type: paper
  title: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
  url: https://arxiv.org/abs/2606.30749
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

## 核心内容
Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

## 参考
- http://arxiv.org/abs/2606.30749v1

## Overview
Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

## Content
Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

## 개요
대규모 정밀 파지 데이터셋은 손-물체 상호작용에 대한 풍부한 사전 지식을 인코딩하지만, 그 활용은 주로 파지 생성과 집어 옮기기 조작에 국한되어 왔습니다. 본 연구에서는 이러한 데이터가 오히려 관절 도구 사용에서의 기능적 정밀성을 지원할 수 있는지 조사합니다. 여기서 로봇은 도구를 획득하고, 접촉을 유지하며, 기능적 움직임 부품을 작동해야 합니다. 우리는 고수준의 손 하위 목표 예측과 저수준의 목표 조건 제어기를 결합한 계층적 모방 학습 프레임워크를 적용합니다. 대규모 정밀 파지 주석에서 355k 궤적의 파지 사전 학습 데이터셋을 구축하고, 이를 저수준 제어기 사전 학습에 사용합니다. 그런 다음 제어기는 하위 작업 시연에 대해 미세 조정됩니다. 이 설정을 평가하기 위해, 우리는 조정된 손가락 움직임이 필요한 여섯 가지 관절 도구 사용 작업을 포함하는 시뮬레이션 벤치마크인 DexCraft를 소개합니다. 시뮬레이션 및 실제 실험 전반에 걸쳐, 우리의 접근 방식은 종단간 확산 정책 기준선과 처음부터 학습된 계층적 정책보다 우수한 성능을 보입니다. 실제 환경에서는 DP3 대비 전체 작업 성공률을 33.3% 포인트 향상시킵니다. 이러한 결과는 파지 데이터셋이 파지 합성을 위한 자원뿐만 아니라 접촉이 풍부한 정밀 조작을 위한 확장 가능한 사전 학습 데이터로도 사용될 수 있음을 보여줍니다. 비디오는 https://yingyuan0414.github.io/grasp2dexterity/ 에서 확인할 수 있습니다.

## 핵심 내용
대규모 정밀 파지 데이터셋은 손-물체 상호작용에 대한 풍부한 사전 지식을 인코딩하지만, 그 활용은 주로 파지 생성과 집어 옮기기 조작에 국한되어 왔습니다. 본 연구에서는 이러한 데이터가 오히려 관절 도구 사용에서의 기능적 정밀성을 지원할 수 있는지 조사합니다. 여기서 로봇은 도구를 획득하고, 접촉을 유지하며, 기능적 움직임 부품을 작동해야 합니다. 우리는 고수준의 손 하위 목표 예측과 저수준의 목표 조건 제어기를 결합한 계층적 모방 학습 프레임워크를 적용합니다. 대규모 정밀 파지 주석에서 355k 궤적의 파지 사전 학습 데이터셋을 구축하고, 이를 저수준 제어기 사전 학습에 사용합니다. 그런 다음 제어기는 하위 작업 시연에 대해 미세 조정됩니다. 이 설정을 평가하기 위해, 우리는 조정된 손가락 움직임이 필요한 여섯 가지 관절 도구 사용 작업을 포함하는 시뮬레이션 벤치마크인 DexCraft를 소개합니다. 시뮬레이션 및 실제 실험 전반에 걸쳐, 우리의 접근 방식은 종단간 확산 정책 기준선과 처음부터 학습된 계층적 정책보다 우수한 성능을 보입니다. 실제 환경에서는 DP3 대비 전체 작업 성공률을 33.3% 포인트 향상시킵니다. 이러한 결과는 파지 데이터셋이 파지 합성을 위한 자원뿐만 아니라 접촉이 풍부한 정밀 조작을 위한 확장 가능한 사전 학습 데이터로도 사용될 수 있음을 보여줍니다. 비디오는 https://yingyuan0414.github.io/grasp2dexterity/ 에서 확인할 수 있습니다.
