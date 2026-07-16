---
$id: ent_paper_humanoidgen_data_generation_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
  zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
  ko: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning'
summary:
  en: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
    for humanoid robots.'
  zh: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
    for humanoid robots.'
  ko: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning is a 2025 work on simulation benchmark
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
- humanoidgen
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.00833v2.
sources:
- id: src_001
  type: paper
  title: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning (arXiv)'
  url: https://arxiv.org/abs/2507.00833
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'HumanoidGen: Data Generation for Bimanual Dexterous Manipulation via LLM Reasoning project page'
  url: https://openhumanoidgen.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## 核心内容
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## 参考
- http://arxiv.org/abs/2507.00833v2

## Overview
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## Content
For robotic manipulation, existing robotics datasets and simulation benchmarks predominantly cater to robot-arm platforms. However, for humanoid robots equipped with dual arms and dexterous hands, simulation tasks and high-quality demonstrations are notably lacking. Bimanual dexterous manipulation is inherently more complex, as it requires coordinated arm movements and hand operations, making autonomous data collection challenging. This paper presents HumanoidGen, an automated task creation and demonstration collection framework that leverages atomic dexterous operations and LLM reasoning to generate relational constraints. Specifically, we provide spatial annotations for both assets and dexterous hands based on the atomic operations, and perform an LLM planner to generate a chain of actionable spatial constraints for arm movements based on object affordances and scenes. To further improve planning ability, we employ a variant of Monte Carlo tree search to enhance LLM reasoning for long-horizon tasks and insufficient annotation. In experiments, we create a novel benchmark with augmented scenarios to evaluate the quality of the collected data. The results show that the performance of the 2D and 3D diffusion policies can scale with the generated dataset. Project page is https://openhumanoidgen.github.io.

## 개요
로봇 조작 분야에서 기존의 로봇공학 데이터셋과 시뮬레이션 벤치마크는 주로 로봇 암 플랫폼에 초점을 맞추고 있습니다. 그러나 이중 암과 정교한 손을 갖춘 휴머노이드 로봇의 경우, 시뮬레이션 작업과 고품질 시연 데이터가 현저히 부족합니다. 양손 정밀 조작은 본질적으로 더 복잡하며, 팔 움직임과 손 조작의 협응이 필요하여 자율 데이터 수집이 어렵습니다. 본 논문에서는 원자적 정밀 조작과 LLM 추론을 활용하여 관계적 제약 조건을 생성하는 자동화된 작업 생성 및 시연 수집 프레임워크인 HumanoidGen을 제시합니다. 구체적으로, 원자적 조작을 기반으로 자산과 정밀 손 모두에 대한 공간 주석을 제공하고, LLM 플래너를 실행하여 객체의 기능성과 장면에 기반한 팔 움직임을 위한 실행 가능한 공간 제약 조건 체인을 생성합니다. 계획 능력을 더욱 향상시키기 위해, 몬테카를로 트리 탐색의 변형을 사용하여 장기적 작업과 불충분한 주석에 대한 LLM 추론을 강화합니다. 실험에서는 증강된 시나리오를 포함한 새로운 벤치마크를 생성하여 수집된 데이터의 품질을 평가합니다. 결과는 2D 및 3D 확산 정책의 성능이 생성된 데이터셋에 따라 확장될 수 있음을 보여줍니다. 프로젝트 페이지는 https://openhumanoidgen.github.io 입니다.

## 핵심 내용
로봇 조작 분야에서 기존의 로봇공학 데이터셋과 시뮬레이션 벤치마크는 주로 로봇 암 플랫폼에 초점을 맞추고 있습니다. 그러나 이중 암과 정교한 손을 갖춘 휴머노이드 로봇의 경우, 시뮬레이션 작업과 고품질 시연 데이터가 현저히 부족합니다. 양손 정밀 조작은 본질적으로 더 복잡하며, 팔 움직임과 손 조작의 협응이 필요하여 자율 데이터 수집이 어렵습니다. 본 논문에서는 원자적 정밀 조작과 LLM 추론을 활용하여 관계적 제약 조건을 생성하는 자동화된 작업 생성 및 시연 수집 프레임워크인 HumanoidGen을 제시합니다. 구체적으로, 원자적 조작을 기반으로 자산과 정밀 손 모두에 대한 공간 주석을 제공하고, LLM 플래너를 실행하여 객체의 기능성과 장면에 기반한 팔 움직임을 위한 실행 가능한 공간 제약 조건 체인을 생성합니다. 계획 능력을 더욱 향상시키기 위해, 몬테카를로 트리 탐색의 변형을 사용하여 장기적 작업과 불충분한 주석에 대한 LLM 추론을 강화합니다. 실험에서는 증강된 시나리오를 포함한 새로운 벤치마크를 생성하여 수집된 데이터의 품질을 평가합니다. 결과는 2D 및 3D 확산 정책의 성능이 생성된 데이터셋에 따라 확장될 수 있음을 보여줍니다. 프로젝트 페이지는 https://openhumanoidgen.github.io 입니다.
