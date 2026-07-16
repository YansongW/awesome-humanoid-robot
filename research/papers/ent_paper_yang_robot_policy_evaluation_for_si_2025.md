---
$id: ent_paper_yang_robot_policy_evaluation_for_si_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective'
  zh: 面向模拟到现实迁移的机器人策略评估：基准测试视角
  ko: '시뮬레이션-현실 전이를 위한 로봇 정책 평가: 벤치마킹 관점'
summary:
  en: This paper identifies challenges and desiderata for benchmarking generalist robot manipulation policies, proposing a
    high-fidelity simulation-based evaluation framework that scales task complexity, applies systematic scene perturbations,
    and quantifies sim-to-real alignment through discrete and continuous metrics.
  zh: 本文识别了通用机器人操作策略基准测试中的挑战与需求，提出了一种基于高保真仿真的评估框架，通过逐步增加任务复杂度、施加系统化场景扰动，并以离散与连续指标量化模拟到现实的对齐程度。
  ko: 본 논문은 범용 로봇 조작 정책 벤치마킹의 과제와 요구사항을 도출하고, 작업 복잡도를 단계적으로 높이고 체계적인 장면 교란을 적용하며 이산/연속 지표로 시뮬레이션-현실 정렬을 정량화하는 고충실도 시뮬레이션 기반
    평가 프레임워크를 제안한다.
domains:
- 10_evaluation_benchmarks
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- sim_to_real
- benchmarking
- visual_fidelity
- policy_evaluation
- manipulation
- isaaclab
- task_taxonomy
- robustness
- simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11117v1.
sources:
- id: src_001
  type: paper
  title: 'Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective'
  url: https://arxiv.org/abs/2508.11117
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_benchmark_libero
  relationship: cites
  description:
    en: Cited as a benchmark with limited testing tasks for lifelong robot learning.
    zh: 作为有限测试任务的终身机器人学习基准被引用。
    ko: 제한된 테스트 작업을 다루는 평생 로봇 학습 벤치마크로 인용됨.
---
## 概述
Current vision-based robotics simulation benchmarks have significantly advanced robotic manipulation research. However, robotics is fundamentally a real-world problem, and evaluation for real-world applications has lagged behind in evaluating generalist policies. In this paper, we discuss challenges and desiderata in designing benchmarks for generalist robotic manipulation policies for the goal of sim-to-real policy transfer. We propose 1) utilizing high visual-fidelity simulation for improved sim-to-real transfer, 2) evaluating policies by systematically increasing task complexity and scenario perturbation to assess robustness, and 3) quantifying performance alignment between real-world performance and its simulation counterparts.

## 核心内容
Current vision-based robotics simulation benchmarks have significantly advanced robotic manipulation research. However, robotics is fundamentally a real-world problem, and evaluation for real-world applications has lagged behind in evaluating generalist policies. In this paper, we discuss challenges and desiderata in designing benchmarks for generalist robotic manipulation policies for the goal of sim-to-real policy transfer. We propose 1) utilizing high visual-fidelity simulation for improved sim-to-real transfer, 2) evaluating policies by systematically increasing task complexity and scenario perturbation to assess robustness, and 3) quantifying performance alignment between real-world performance and its simulation counterparts.

## 参考
- http://arxiv.org/abs/2508.11117v1

## Overview
Current vision-based robotics simulation benchmarks have significantly advanced robotic manipulation research. However, robotics is fundamentally a real-world problem, and evaluation for real-world applications has lagged behind in evaluating generalist policies. In this paper, we discuss challenges and desiderata in designing benchmarks for generalist robotic manipulation policies for the goal of sim-to-real policy transfer. We propose 1) utilizing high visual-fidelity simulation for improved sim-to-real transfer, 2) evaluating policies by systematically increasing task complexity and scenario perturbation to assess robustness, and 3) quantifying performance alignment between real-world performance and its simulation counterparts.

## Content
Current vision-based robotics simulation benchmarks have significantly advanced robotic manipulation research. However, robotics is fundamentally a real-world problem, and evaluation for real-world applications has lagged behind in evaluating generalist policies. In this paper, we discuss challenges and desiderata in designing benchmarks for generalist robotic manipulation policies for the goal of sim-to-real policy transfer. We propose 1) utilizing high visual-fidelity simulation for improved sim-to-real transfer, 2) evaluating policies by systematically increasing task complexity and scenario perturbation to assess robustness, and 3) quantifying performance alignment between real-world performance and its simulation counterparts.

## 개요
현재 비전 기반 로봇공학 시뮬레이션 벤치마크는 로봇 조작 연구를 크게 발전시켰습니다. 그러나 로봇공학은 근본적으로 실제 세계의 문제이며, 실제 응용 분야에서의 평가는 일반화 정책(generalist policies) 평가에 뒤처져 있습니다. 본 논문에서는 시뮬레이션-실제 정책 전이(sim-to-real policy transfer)를 목표로 하는 일반화 로봇 조작 정책을 위한 벤치마크 설계 시 직면하는 과제와 요구사항을 논의합니다. 우리는 1) 시뮬레이션-실제 전이 향상을 위한 높은 시각적 충실도 시뮬레이션 활용, 2) 작업 복잡성과 시나리오 교란을 체계적으로 증가시켜 정책의 강건성을 평가, 3) 실제 성능과 시뮬레이션 성능 간의 일치도 정량화를 제안합니다.

## 핵심 내용
현재 비전 기반 로봇공학 시뮬레이션 벤치마크는 로봇 조작 연구를 크게 발전시켰습니다. 그러나 로봇공학은 근본적으로 실제 세계의 문제이며, 실제 응용 분야에서의 평가는 일반화 정책 평가에 뒤처져 있습니다. 본 논문에서는 시뮬레이션-실제 정책 전이를 목표로 하는 일반화 로봇 조작 정책을 위한 벤치마크 설계 시 직면하는 과제와 요구사항을 논의합니다. 우리는 1) 시뮬레이션-실제 전이 향상을 위한 높은 시각적 충실도 시뮬레이션 활용, 2) 작업 복잡성과 시나리오 교란을 체계적으로 증가시켜 정책의 강건성 평가, 3) 실제 성능과 시뮬레이션 성능 간의 일치도 정량화를 제안합니다.
