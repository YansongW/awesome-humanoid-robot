---
$id: ent_paper_pyroki_a_modular_toolkit_for_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
  zh: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
  ko: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization'
summary:
  en: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization is a 2025 work on loco-manipulation and whole-body-control
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
- pyroki
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03728v1.
sources:
- id: src_001
  type: paper
  title: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization (arXiv)'
  url: https://arxiv.org/abs/2505.03728
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'PyRoki: A Modular Toolkit for Robot Kinematic Optimization project page'
  url: https://pyroki-toolkit.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## 核心内容
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## 参考
- http://arxiv.org/abs/2505.03728v1

## Overview
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## Content
Robot motion can have many goals. Depending on the task, we might optimize for pose error, speed, collision, or similarity to a human demonstration. Motivated by this, we present PyRoki: a modular, extensible, and cross-platform toolkit for solving kinematic optimization problems. PyRoki couples an interface for specifying kinematic variables and costs with an efficient nonlinear least squares optimizer. Unlike existing tools, it is also cross-platform: optimization runs natively on CPU, GPU, and TPU. In this paper, we present (i) the design and implementation of PyRoki, (ii) motion retargeting and planning case studies that highlight the advantages of PyRoki's modularity, and (iii) optimization benchmarking, where PyRoki can be 1.4-1.7x faster and converges to lower errors than cuRobo, an existing GPU-accelerated inverse kinematics library.

## 개요
로봇 동작은 다양한 목표를 가질 수 있습니다. 작업에 따라 자세 오차, 속도, 충돌 또는 인간 시연과의 유사성을 최적화할 수 있습니다. 이러한 동기에서 우리는 PyRoki를 소개합니다: 모듈식이며 확장 가능하고 크로스 플랫폼을 지원하는 운동학 최적화 문제 해결 도구입니다. PyRoki는 운동학 변수와 비용을 지정하는 인터페이스와 효율적인 비선형 최소제곱 최적화기를 결합합니다. 기존 도구와 달리 크로스 플랫폼을 지원하여 CPU, GPU 및 TPU에서 최적화가 기본적으로 실행됩니다. 본 논문에서는 (i) PyRoki의 설계 및 구현, (ii) PyRoki의 모듈성 장점을 강조하는 동작 리타겟팅 및 계획 사례 연구, (iii) 기존 GPU 가속 역운동학 라이브러리인 cuRobo보다 1.4-1.7배 빠르고 더 낮은 오차로 수렴하는 최적화 벤치마킹을 제시합니다.

## 핵심 내용
로봇 동작은 다양한 목표를 가질 수 있습니다. 작업에 따라 자세 오차, 속도, 충돌 또는 인간 시연과의 유사성을 최적화할 수 있습니다. 이러한 동기에서 우리는 PyRoki를 소개합니다: 모듈식이며 확장 가능하고 크로스 플랫폼을 지원하는 운동학 최적화 문제 해결 도구입니다. PyRoki는 운동학 변수와 비용을 지정하는 인터페이스와 효율적인 비선형 최소제곱 최적화기를 결합합니다. 기존 도구와 달리 크로스 플랫폼을 지원하여 CPU, GPU 및 TPU에서 최적화가 기본적으로 실행됩니다. 본 논문에서는 (i) PyRoki의 설계 및 구현, (ii) PyRoki의 모듈성 장점을 강조하는 동작 리타겟팅 및 계획 사례 연구, (iii) 기존 GPU 가속 역운동학 라이브러리인 cuRobo보다 1.4-1.7배 빠르고 더 낮은 오차로 수렴하는 최적화 벤치마킹을 제시합니다.
