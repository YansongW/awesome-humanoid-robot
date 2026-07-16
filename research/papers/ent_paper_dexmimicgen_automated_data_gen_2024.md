---
$id: ent_paper_dexmimicgen_automated_data_gen_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
  zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
  ko: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
summary:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
  zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
  ko: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- dexmimicgen
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24185v2.
sources:
- id: src_001
  type: paper
  title: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (arXiv)'
  url: https://arxiv.org/abs/2410.24185
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning project page'
  url: https://dexmimicgen.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## 核心内容
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## 参考
- http://arxiv.org/abs/2410.24185v2

## Overview
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## Content
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## 개요
인간 시연으로부터의 모방 학습은 로봇에게 조작 기술을 가르치는 효과적인 방법입니다. 그러나 데이터 수집은 비용과 인간의 노력이 많이 들기 때문에 이 패러다임을 더 널리 적용하는 데 주요 장애물입니다. 휴머노이드와 같은 양손 정밀 로봇을 위한 모방 학습에 대한 상당한 관심이 있었습니다. 불행히도, 여러 팔과 다지 손을 동시에 제어해야 하는 어려움으로 인해 데이터 수집은 여기서 더욱 까다롭습니다. 시뮬레이션에서의 자동 데이터 생성은 이러한 데이터 수요를 충족시키는 매력적이고 확장 가능한 대안입니다. 이를 위해 우리는 정밀 손을 가진 휴머노이드 로봇을 위해 소수의 인간 시연으로부터 궤적을 합성하는 대규모 자동 데이터 생성 시스템인 DexMimicGen을 소개합니다. 우리는 다양한 조작 행동과 두 팔 간의 조정 요구 사항을 포괄하는 양손 정밀 조작 환경에서의 시뮬레이션 환경 모음을 제시합니다. 단 60개의 소스 인간 시연으로부터 이러한 작업 전반에 걸쳐 21K개의 시연을 생성하고, 여러 데이터 생성 및 정책 학습 결정이 에이전트 성능에 미치는 영향을 연구합니다. 마지막으로, 실제-시뮬레이션-실제 파이프라인을 제시하고 실제 휴머노이드 캔 분류 작업에 배포합니다. 생성된 데이터셋, 시뮬레이션 환경 및 추가 결과는 https://dexmimicgen.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
인간 시연으로부터의 모방 학습은 로봇에게 조작 기술을 가르치는 효과적인 방법입니다. 그러나 데이터 수집은 비용과 인간의 노력이 많이 들기 때문에 이 패러다임을 더 널리 적용하는 데 주요 장애물입니다. 휴머노이드와 같은 양손 정밀 로봇을 위한 모방 학습에 대한 상당한 관심이 있었습니다. 불행히도, 여러 팔과 다지 손을 동시에 제어해야 하는 어려움으로 인해 데이터 수집은 여기서 더욱 까다롭습니다. 시뮬레이션에서의 자동 데이터 생성은 이러한 데이터 수요를 충족시키는 매력적이고 확장 가능한 대안입니다. 이를 위해 우리는 정밀 손을 가진 휴머노이드 로봇을 위해 소수의 인간 시연으로부터 궤적을 합성하는 대규모 자동 데이터 생성 시스템인 DexMimicGen을 소개합니다. 우리는 다양한 조작 행동과 두 팔 간의 조정 요구 사항을 포괄하는 양손 정밀 조작 환경에서의 시뮬레이션 환경 모음을 제시합니다. 단 60개의 소스 인간 시연으로부터 이러한 작업 전반에 걸쳐 21K개의 시연을 생성하고, 여러 데이터 생성 및 정책 학습 결정이 에이전트 성능에 미치는 영향을 연구합니다. 마지막으로, 실제-시뮬레이션-실제 파이프라인을 제시하고 실제 휴머노이드 캔 분류 작업에 배포합니다. 생성된 데이터셋, 시뮬레이션 환경 및 추가 결과는 https://dexmimicgen.github.io/ 에서 확인할 수 있습니다.
