---
$id: ent_paper_teleopbench_a_simulator_centri_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation'
  zh: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation'
  ko: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation'
summary:
  en: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation is a 2025 work on teleoperation for
    humanoid robots.'
  zh: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation is a 2025 work on teleoperation for
    humanoid robots.'
  ko: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation is a 2025 work on teleoperation for
    humanoid robots.'
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
- teleopbench
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.12748v2.
sources:
- id: src_001
  type: paper
  title: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2505.12748
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'TeleOpBench: A Simulator-Centric Benchmark for Dual-Arm Dexterous Teleoperation project page'
  url: https://gorgeous2002.github.io/TeleOpBench/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

## 核心内容
Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

## 参考
- http://arxiv.org/abs/2505.12748v2

## Overview
Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

## Content
Teleoperation is a cornerstone of embodied-robot learning, and bimanual dexterous teleoperation in particular provides rich demonstrations that are difficult to obtain with fully autonomous systems. While recent studies have proposed diverse hardware pipelines-ranging from inertial motion-capture gloves to exoskeletons and vision-based interfaces-there is still no unified benchmark that enables fair, reproducible comparison of these systems. In this paper, we introduce TeleOpBench, a simulator-centric benchmark tailored to bimanual dexterous teleoperation. TeleOpBench contains 30 high-fidelity task environments that span pick-and-place, tool use, and collaborative manipulation, covering a broad spectrum of kinematic and force-interaction difficulty. Within this benchmark we implement four representative teleoperation modalities-(i) MoCap, (ii) VR device, (iii) arm-hand exoskeletons, and (iv) monocular vision tracking-and evaluate them with a common protocol and metric suite. To validate that performance in simulation is predictive of real-world behavior, we conduct mirrored experiments on a physical dual-arm platform equipped with two 6-DoF dexterous hands. Across 10 held-out tasks we observe a strong correlation between simulator and hardware performance, confirming the external validity of TeleOpBench. TeleOpBench establishes a common yardstick for teleoperation research and provides an extensible platform for future algorithmic and hardware innovation. Codes is now available at https://github.com/cyjdlhy/TeleOpBench .

## 개요
원격 조작은 임베디드 로봇 학습의 초석이며, 특히 양손 정밀 원격 조작은 완전 자율 시스템으로는 얻기 어려운 풍부한 시연 데이터를 제공합니다. 최근 연구에서는 관성 모션 캡처 장갑부터 외골격 및 비전 기반 인터페이스에 이르기까지 다양한 하드웨어 파이프라인이 제안되었지만, 이러한 시스템들을 공정하고 재현 가능하게 비교할 수 있는 통합 벤치마크는 아직 없습니다. 본 논문에서는 양손 정밀 원격 조작에 특화된 시뮬레이터 중심 벤치마크인 TeleOpBench를 소개합니다. TeleOpBench는 집어 옮기기, 도구 사용, 협력 조작을 아우르는 30개의 고충실도 작업 환경을 포함하며, 다양한 운동학적 및 힘 상호작용 난이도를 포괄합니다. 이 벤치마크 내에서 (i) MoCap, (ii) VR 기기, (iii) 팔-손 외골격, (iv) 단안 비전 추적의 네 가지 대표적인 원격 조작 방식을 구현하고, 공통 프로토콜과 메트릭 세트로 평가합니다. 시뮬레이션 성능이 실제 세계 동작을 예측할 수 있는지 검증하기 위해, 두 개의 6자유도 정밀 손을 장착한 물리적 이중 팔 플랫폼에서 대칭 실험을 수행했습니다. 10개의 보류 작업에서 시뮬레이터와 하드웨어 성능 간 강한 상관관계를 관찰하여 TeleOpBench의 외적 타당성을 확인했습니다. TeleOpBench는 원격 조작 연구를 위한 공통 척도를 제공하며, 향후 알고리즘 및 하드웨어 혁신을 위한 확장 가능한 플랫폼을 제공합니다. 코드는 https://github.com/cyjdlhy/TeleOpBench 에서 확인할 수 있습니다.

## 핵심 내용
원격 조작은 임베디드 로봇 학습의 초석이며, 특히 양손 정밀 원격 조작은 완전 자율 시스템으로는 얻기 어려운 풍부한 시연 데이터를 제공합니다. 최근 연구에서는 관성 모션 캡처 장갑부터 외골격 및 비전 기반 인터페이스에 이르기까지 다양한 하드웨어 파이프라인이 제안되었지만, 이러한 시스템들을 공정하고 재현 가능하게 비교할 수 있는 통합 벤치마크는 아직 없습니다. 본 논문에서는 양손 정밀 원격 조작에 특화된 시뮬레이터 중심 벤치마크인 TeleOpBench를 소개합니다. TeleOpBench는 집어 옮기기, 도구 사용, 협력 조작을 아우르는 30개의 고충실도 작업 환경을 포함하며, 다양한 운동학적 및 힘 상호작용 난이도를 포괄합니다. 이 벤치마크 내에서 (i) MoCap, (ii) VR 기기, (iii) 팔-손 외골격, (iv) 단안 비전 추적의 네 가지 대표적인 원격 조작 방식을 구현하고, 공통 프로토콜과 메트릭 세트로 평가합니다. 시뮬레이션 성능이 실제 세계 동작을 예측할 수 있는지 검증하기 위해, 두 개의 6자유도 정밀 손을 장착한 물리적 이중 팔 플랫폼에서 대칭 실험을 수행했습니다. 10개의 보류 작업에서 시뮬레이터와 하드웨어 성능 간 강한 상관관계를 관찰하여 TeleOpBench의 외적 타당성을 확인했습니다. TeleOpBench는 원격 조작 연구를 위한 공통 척도를 제공하며, 향후 알고리즘 및 하드웨어 혁신을 위한 확장 가능한 플랫폼을 제공합니다. 코드는 https://github.com/cyjdlhy/TeleOpBench 에서 확인할 수 있습니다.
