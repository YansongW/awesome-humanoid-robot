---
$id: ent_paper_molmospaces_a_large_scale_open_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation'
  zh: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation'
  ko: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation'
summary:
  en: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation is a 2026 work on simulation benchmark
    for humanoid robots.'
  zh: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation is a 2026 work on simulation benchmark
    for humanoid robots.'
  ko: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation is a 2026 work on simulation benchmark
    for humanoid robots.'
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
- humanoid
- molmospaces
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11337v2.
sources:
- id: src_001
  type: paper
  title: 'MolmoSpaces: A Large-Scale Open Ecosystem for Robot Navigation and Manipulation (arXiv)'
  url: https://arxiv.org/abs/2602.11337
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Deploying robots at scale demands robustness to the long tail of everyday situations. The countless variations in scene layout, object geometry, and task specifications that characterize real environments are vast and underrepresented in existing robot benchmarks. Measuring this level of generalization requires infrastructure at a scale and diversity that physical evaluation alone cannot provide. We introduce MolmoSpaces, a fully open ecosystem to support large-scale benchmarking of robot policies. MolmoSpaces consists of over 230k diverse indoor environments, ranging from handcrafted household scenes to procedurally generated multiroom houses, populated with 130k richly annotated object assets, including 48k manipulable objects with 42M stable grasps. Crucially, these environments are simulator-agnostic, supporting popular options such as MuJoCo, Isaac, and ManiSkill. The ecosystem supports the full spectrum of embodied tasks: static and mobile manipulation, navigation, and multiroom long-horizon tasks requiring coordinated perception, planning, and interaction across entire indoor environments. We also design MolmoSpaces-Bench, a benchmark suite of 8 tasks in which robots interact with our diverse scenes and richly annotated objects. Our experiments show MolmoSpaces-Bench exhibits strong sim-to-real correlation (R = 0.96, \r{ho} = 0.98), confirm newer and stronger zero-shot policies outperform earlier versions in our benchmarks, and identify key sensitivities to prompt phrasing, initial joint positions, and camera occlusion. Through MolmoSpaces and its open-source assets and tooling, we provide a foundation for scalable data generation, policy training, and benchmark creation for robot learning research.

## 核心内容
Deploying robots at scale demands robustness to the long tail of everyday situations. The countless variations in scene layout, object geometry, and task specifications that characterize real environments are vast and underrepresented in existing robot benchmarks. Measuring this level of generalization requires infrastructure at a scale and diversity that physical evaluation alone cannot provide. We introduce MolmoSpaces, a fully open ecosystem to support large-scale benchmarking of robot policies. MolmoSpaces consists of over 230k diverse indoor environments, ranging from handcrafted household scenes to procedurally generated multiroom houses, populated with 130k richly annotated object assets, including 48k manipulable objects with 42M stable grasps. Crucially, these environments are simulator-agnostic, supporting popular options such as MuJoCo, Isaac, and ManiSkill. The ecosystem supports the full spectrum of embodied tasks: static and mobile manipulation, navigation, and multiroom long-horizon tasks requiring coordinated perception, planning, and interaction across entire indoor environments. We also design MolmoSpaces-Bench, a benchmark suite of 8 tasks in which robots interact with our diverse scenes and richly annotated objects. Our experiments show MolmoSpaces-Bench exhibits strong sim-to-real correlation (R = 0.96, \r{ho} = 0.98), confirm newer and stronger zero-shot policies outperform earlier versions in our benchmarks, and identify key sensitivities to prompt phrasing, initial joint positions, and camera occlusion. Through MolmoSpaces and its open-source assets and tooling, we provide a foundation for scalable data generation, policy training, and benchmark creation for robot learning research.

## 参考
- http://arxiv.org/abs/2602.11337v2

## Overview
Deploying robots at scale demands robustness to the long tail of everyday situations. The countless variations in scene layout, object geometry, and task specifications that characterize real environments are vast and underrepresented in existing robot benchmarks. Measuring this level of generalization requires infrastructure at a scale and diversity that physical evaluation alone cannot provide. We introduce MolmoSpaces, a fully open ecosystem to support large-scale benchmarking of robot policies. MolmoSpaces consists of over 230k diverse indoor environments, ranging from handcrafted household scenes to procedurally generated multiroom houses, populated with 130k richly annotated object assets, including 48k manipulable objects with 42M stable grasps. Crucially, these environments are simulator-agnostic, supporting popular options such as MuJoCo, Isaac, and ManiSkill. The ecosystem supports the full spectrum of embodied tasks: static and mobile manipulation, navigation, and multiroom long-horizon tasks requiring coordinated perception, planning, and interaction across entire indoor environments. We also design MolmoSpaces-Bench, a benchmark suite of 8 tasks in which robots interact with our diverse scenes and richly annotated objects. Our experiments show MolmoSpaces-Bench exhibits strong sim-to-real correlation (R = 0.96, \r{ho} = 0.98), confirm newer and stronger zero-shot policies outperform earlier versions in our benchmarks, and identify key sensitivities to prompt phrasing, initial joint positions, and camera occlusion. Through MolmoSpaces and its open-source assets and tooling, we provide a foundation for scalable data generation, policy training, and benchmark creation for robot learning research.

## Content
Deploying robots at scale demands robustness to the long tail of everyday situations. The countless variations in scene layout, object geometry, and task specifications that characterize real environments are vast and underrepresented in existing robot benchmarks. Measuring this level of generalization requires infrastructure at a scale and diversity that physical evaluation alone cannot provide. We introduce MolmoSpaces, a fully open ecosystem to support large-scale benchmarking of robot policies. MolmoSpaces consists of over 230k diverse indoor environments, ranging from handcrafted household scenes to procedurally generated multiroom houses, populated with 130k richly annotated object assets, including 48k manipulable objects with 42M stable grasps. Crucially, these environments are simulator-agnostic, supporting popular options such as MuJoCo, Isaac, and ManiSkill. The ecosystem supports the full spectrum of embodied tasks: static and mobile manipulation, navigation, and multiroom long-horizon tasks requiring coordinated perception, planning, and interaction across entire indoor environments. We also design MolmoSpaces-Bench, a benchmark suite of 8 tasks in which robots interact with our diverse scenes and richly annotated objects. Our experiments show MolmoSpaces-Bench exhibits strong sim-to-real correlation (R = 0.96, \r{ho} = 0.98), confirm newer and stronger zero-shot policies outperform earlier versions in our benchmarks, and identify key sensitivities to prompt phrasing, initial joint positions, and camera occlusion. Through MolmoSpaces and its open-source assets and tooling, we provide a foundation for scalable data generation, policy training, and benchmark creation for robot learning research.

## 개요
로봇을 대규모로 배포하려면 일상적인 상황의 긴 꼬리(long tail)에 대한 강건성이 필요합니다. 실제 환경을 특징짓는 장면 배치, 객체 형상, 작업 사양의 무수한 변형은 기존 로봇 벤치마크에서 과소 대표되어 있습니다. 이러한 수준의 일반화를 측정하려면 물리적 평가만으로는 제공할 수 없는 규모와 다양성을 갖춘 인프라가 필요합니다. 우리는 로봇 정책의 대규모 벤치마킹을 지원하는 완전 개방형 생태계인 MolmoSpaces를 소개합니다. MolmoSpaces는 수작업으로 제작된 가정용 장면부터 절차적으로 생성된 다중 방 주택까지 23만 개 이상의 다양한 실내 환경으로 구성되며, 13만 개의 풍부한 주석이 달린 객체 자산(48만 개의 조작 가능한 객체와 4,200만 개의 안정적인 그립 포함)이 배치되어 있습니다. 결정적으로, 이러한 환경은 시뮬레이터에 구애받지 않으며 MuJoCo, Isaac, ManiSkill과 같은 인기 옵션을 지원합니다. 이 생태계는 정적 및 이동 조작, 내비게이션, 전체 실내 환경에 걸친 조정된 인식, 계획 및 상호작용이 필요한 다중 방 장기 과제 등 구현된 작업의 전체 스펙트럼을 지원합니다. 또한 로봇이 다양한 장면과 풍부한 주석이 달린 객체와 상호작용하는 8가지 작업으로 구성된 벤치마크 제품군인 MolmoSpaces-Bench를 설계했습니다. 실험 결과 MolmoSpaces-Bench는 강력한 시뮬레이션-실제 상관관계(R = 0.96, \r{ho} = 0.98)를 보여주며, 더 새롭고 강력한 제로샷 정책이 이전 버전보다 벤치마크에서 우수함을 확인하고, 프롬프트 표현, 초기 관절 위치, 카메라 폐색에 대한 주요 민감도를 식별합니다. MolmoSpaces와 오픈소스 자산 및 도구를 통해 로봇 학습 연구를 위한 확장 가능한 데이터 생성, 정책 훈련, 벤치마크 생성을 위한 기반을 제공합니다.

## 핵심 내용
로봇을 대규모로 배포하려면 일상적인 상황의 긴 꼬리(long tail)에 대한 강건성이 필요합니다. 실제 환경을 특징짓는 장면 배치, 객체 형상, 작업 사양의 무수한 변형은 기존 로봇 벤치마크에서 과소 대표되어 있습니다. 이러한 수준의 일반화를 측정하려면 물리적 평가만으로는 제공할 수 없는 규모와 다양성을 갖춘 인프라가 필요합니다. 우리는 로봇 정책의 대규모 벤치마킹을 지원하는 완전 개방형 생태계인 MolmoSpaces를 소개합니다. MolmoSpaces는 수작업으로 제작된 가정용 장면부터 절차적으로 생성된 다중 방 주택까지 23만 개 이상의 다양한 실내 환경으로 구성되며, 13만 개의 풍부한 주석이 달린 객체 자산(48만 개의 조작 가능한 객체와 4,200만 개의 안정적인 그립 포함)이 배치되어 있습니다. 결정적으로, 이러한 환경은 시뮬레이터에 구애받지 않으며 MuJoCo, Isaac, ManiSkill과 같은 인기 옵션을 지원합니다. 이 생태계는 정적 및 이동 조작, 내비게이션, 전체 실내 환경에 걸친 조정된 인식, 계획 및 상호작용이 필요한 다중 방 장기 과제 등 구현된 작업의 전체 스펙트럼을 지원합니다. 또한 로봇이 다양한 장면과 풍부한 주석이 달린 객체와 상호작용하는 8가지 작업으로 구성된 벤치마크 제품군인 MolmoSpaces-Bench를 설계했습니다. 실험 결과 MolmoSpaces-Bench는 강력한 시뮬레이션-실제 상관관계(R = 0.96, \r{ho} = 0.98)를 보여주며, 더 새롭고 강력한 제로샷 정책이 이전 버전보다 벤치마크에서 우수함을 확인하고, 프롬프트 표현, 초기 관절 위치, 카메라 폐색에 대한 주요 민감도를 식별합니다. MolmoSpaces와 오픈소스 자산 및 도구를 통해 로봇 학습 연구를 위한 확장 가능한 데이터 생성, 정책 훈련, 벤치마크 생성을 위한 기반을 제공합니다.
