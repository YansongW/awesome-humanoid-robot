---
$id: ent_paper_maniskill3_gpu_parallelized_ro_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI'
  zh: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI'
  ko: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI'
summary:
  en: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
  zh: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
  ko: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI is a 2024 work on simulation
    benchmark for humanoid robots, with open-source code available.'
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
- maniskill3
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.00425v2.
sources:
- id: src_001
  type: paper
  title: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI (arXiv)'
  url: https://arxiv.org/abs/2410.00425
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI project page'
  url: https://www.maniskill.ai/home
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Simulation has enabled unprecedented compute-scalable approaches to robot learning. However, many existing simulation frameworks typically support a narrow range of scenes/tasks and lack features critical for scaling generalizable robotics and sim2real. We introduce and open source ManiSkill3, the fastest state-visual GPU parallelized robotics simulator with contact-rich physics targeting generalizable manipulation. ManiSkill3 supports GPU parallelization of many aspects including simulation+rendering, heterogeneous simulation, pointclouds/voxels visual input, and more. Simulation with rendering on ManiSkill3 can run 10-1000x faster with 2-3x less GPU memory usage than other platforms, achieving up to 30,000+ FPS in benchmarked environments due to minimal python/pytorch overhead in the system, simulation on the GPU, and the use of the SAPIEN parallel rendering system. Tasks that used to take hours to train can now take minutes. We further provide the most comprehensive range of GPU parallelized environments/tasks spanning 12 distinct domains including but not limited to mobile manipulation for tasks such as drawing, humanoids, and dextrous manipulation in realistic scenes designed by artists or real-world digital twins. In addition, millions of demonstration frames are provided from motion planning, RL, and teleoperation. ManiSkill3 also provides a comprehensive set of baselines that span popular RL and learning-from-demonstrations algorithms.

## 核心内容
Simulation has enabled unprecedented compute-scalable approaches to robot learning. However, many existing simulation frameworks typically support a narrow range of scenes/tasks and lack features critical for scaling generalizable robotics and sim2real. We introduce and open source ManiSkill3, the fastest state-visual GPU parallelized robotics simulator with contact-rich physics targeting generalizable manipulation. ManiSkill3 supports GPU parallelization of many aspects including simulation+rendering, heterogeneous simulation, pointclouds/voxels visual input, and more. Simulation with rendering on ManiSkill3 can run 10-1000x faster with 2-3x less GPU memory usage than other platforms, achieving up to 30,000+ FPS in benchmarked environments due to minimal python/pytorch overhead in the system, simulation on the GPU, and the use of the SAPIEN parallel rendering system. Tasks that used to take hours to train can now take minutes. We further provide the most comprehensive range of GPU parallelized environments/tasks spanning 12 distinct domains including but not limited to mobile manipulation for tasks such as drawing, humanoids, and dextrous manipulation in realistic scenes designed by artists or real-world digital twins. In addition, millions of demonstration frames are provided from motion planning, RL, and teleoperation. ManiSkill3 also provides a comprehensive set of baselines that span popular RL and learning-from-demonstrations algorithms.

## 参考
- http://arxiv.org/abs/2410.00425v2

## Overview
Simulation has enabled unprecedented compute-scalable approaches to robot learning. However, many existing simulation frameworks typically support a narrow range of scenes/tasks and lack features critical for scaling generalizable robotics and sim2real. We introduce and open source ManiSkill3, the fastest state-visual GPU parallelized robotics simulator with contact-rich physics targeting generalizable manipulation. ManiSkill3 supports GPU parallelization of many aspects including simulation+rendering, heterogeneous simulation, pointclouds/voxels visual input, and more. Simulation with rendering on ManiSkill3 can run 10-1000x faster with 2-3x less GPU memory usage than other platforms, achieving up to 30,000+ FPS in benchmarked environments due to minimal python/pytorch overhead in the system, simulation on the GPU, and the use of the SAPIEN parallel rendering system. Tasks that used to take hours to train can now take minutes. We further provide the most comprehensive range of GPU parallelized environments/tasks spanning 12 distinct domains including but not limited to mobile manipulation for tasks such as drawing, humanoids, and dextrous manipulation in realistic scenes designed by artists or real-world digital twins. In addition, millions of demonstration frames are provided from motion planning, RL, and teleoperation. ManiSkill3 also provides a comprehensive set of baselines that span popular RL and learning-from-demonstrations algorithms.

## Content
Simulation has enabled unprecedented compute-scalable approaches to robot learning. However, many existing simulation frameworks typically support a narrow range of scenes/tasks and lack features critical for scaling generalizable robotics and sim2real. We introduce and open source ManiSkill3, the fastest state-visual GPU parallelized robotics simulator with contact-rich physics targeting generalizable manipulation. ManiSkill3 supports GPU parallelization of many aspects including simulation+rendering, heterogeneous simulation, pointclouds/voxels visual input, and more. Simulation with rendering on ManiSkill3 can run 10-1000x faster with 2-3x less GPU memory usage than other platforms, achieving up to 30,000+ FPS in benchmarked environments due to minimal python/pytorch overhead in the system, simulation on the GPU, and the use of the SAPIEN parallel rendering system. Tasks that used to take hours to train can now take minutes. We further provide the most comprehensive range of GPU parallelized environments/tasks spanning 12 distinct domains including but not limited to mobile manipulation for tasks such as drawing, humanoids, and dextrous manipulation in realistic scenes designed by artists or real-world digital twins. In addition, millions of demonstration frames are provided from motion planning, RL, and teleoperation. ManiSkill3 also provides a comprehensive set of baselines that span popular RL and learning-from-demonstrations algorithms.

## 개요
시뮬레이션은 로봇 학습에 전례 없는 계산 확장 가능 접근 방식을 가능하게 했습니다. 그러나 기존의 많은 시뮬레이션 프레임워크는 일반적으로 제한된 범위의 장면/작업만 지원하며, 일반화 가능한 로봇공학과 sim2real 확장에 중요한 기능이 부족합니다. 우리는 일반화 가능한 조작을 목표로 하는 접촉이 풍부한 물리 엔진을 갖춘 가장 빠른 상태-시각 GPU 병렬 로봇공학 시뮬레이터인 ManiSkill3를 소개하고 오픈소스로 공개합니다. ManiSkill3는 시뮬레이션+렌더링, 이기종 시뮬레이션, 포인트클라우드/복셀 시각 입력 등 다양한 측면의 GPU 병렬화를 지원합니다. ManiSkill3에서 렌더링을 포함한 시뮬레이션은 다른 플랫폼보다 10-1000배 빠르게 실행되며 GPU 메모리 사용량은 2-3배 적습니다. 이는 시스템 내 최소한의 python/pytorch 오버헤드, GPU 상의 시뮬레이션, SAPIEN 병렬 렌더링 시스템 사용 덕분에 벤치마크 환경에서 최대 30,000+ FPS를 달성합니다. 훈련에 몇 시간이 걸리던 작업이 이제는 몇 분 만에 가능해졌습니다. 또한 우리는 드로잉, 휴머노이드, 아티스트가 디자인한 현실적인 장면이나 실제 세계 디지털 트윈에서의 정밀 조작 등 모바일 조작을 포함한 12개의 다양한 도메인에 걸쳐 가장 포괄적인 GPU 병렬 환경/작업 범위를 제공합니다. 추가로 모션 플래닝, 강화학습, 원격 조작에서 얻은 수백만 개의 데모 프레임이 제공됩니다. ManiSkill3는 또한 인기 있는 강화학습 및 데모 학습 알고리즘을 포괄하는 포괄적인 베이스라인 세트를 제공합니다.

## 핵심 내용
시뮬레이션은 로봇 학습에 전례 없는 계산 확장 가능 접근 방식을 가능하게 했습니다. 그러나 기존의 많은 시뮬레이션 프레임워크는 일반적으로 제한된 범위의 장면/작업만 지원하며, 일반화 가능한 로봇공학과 sim2real 확장에 중요한 기능이 부족합니다. 우리는 일반화 가능한 조작을 목표로 하는 접촉이 풍부한 물리 엔진을 갖춘 가장 빠른 상태-시각 GPU 병렬 로봇공학 시뮬레이터인 ManiSkill3를 소개하고 오픈소스로 공개합니다. ManiSkill3는 시뮬레이션+렌더링, 이기종 시뮬레이션, 포인트클라우드/복셀 시각 입력 등 다양한 측면의 GPU 병렬화를 지원합니다. ManiSkill3에서 렌더링을 포함한 시뮬레이션은 다른 플랫폼보다 10-1000배 빠르게 실행되며 GPU 메모리 사용량은 2-3배 적습니다. 이는 시스템 내 최소한의 python/pytorch 오버헤드, GPU 상의 시뮬레이션, SAPIEN 병렬 렌더링 시스템 사용 덕분에 벤치마크 환경에서 최대 30,000+ FPS를 달성합니다. 훈련에 몇 시간이 걸리던 작업이 이제는 몇 분 만에 가능해졌습니다. 또한 우리는 드로잉, 휴머노이드, 아티스트가 디자인한 현실적인 장면이나 실제 세계 디지털 트윈에서의 정밀 조작 등 모바일 조작을 포함한 12개의 다양한 도메인에 걸쳐 가장 포괄적인 GPU 병렬 환경/작업 범위를 제공합니다. 추가로 모션 플래닝, 강화학습, 원격 조작에서 얻은 수백만 개의 데모 프레임이 제공됩니다. ManiSkill3는 또한 인기 있는 강화학습 및 데모 학습 알고리즘을 포괄하는 포괄적인 베이스라인 세트를 제공합니다.
