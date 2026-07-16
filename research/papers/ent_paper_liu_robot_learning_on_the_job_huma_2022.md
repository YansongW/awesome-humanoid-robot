---
$id: ent_paper_liu_robot_learning_on_the_job_huma_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment'
  zh: 机器人在岗学习：部署过程中的人机协同自治与学习
  ko: '로봇의 현장 학습: 배포 중 인간 개입 자율성 및 학습'
summary:
  en: This paper introduces Sirius, a human-in-the-loop framework in which a partially autonomous robot handles reliable decisions
    while a human monitors and teleoperates interventions, then improves policies via weighted behavioral cloning on re-weighted
    deployment data.
  zh: With the rapid growth of computing powers and recent advances in deep learning, we have witnessed impressive demonstrations
    of novel robot capabilities in research settings. Nonetheless, these learning systems exhibit brittle generalization and
    require excessive training data for practical tasks. To harness the capabilities of state-of-the-art robot learning models
    while embracing their imperfections, we present Sirius, a principled framework for humans and robots to collaborate through
    a division of work. In this framework, partially autonomous robots are tasked with handling a major portion
  ko: 본 논문은 부분 자율 로봇이 안정적인 의사결정을 수행하고 인간이 모니터링하며 어려운 상황에서 텔레오퍼레이션으로 개입한 후, 재가중된 배포 데이터에 대한 가중 행동 복제를 통해 정책을 지속적으로 개선하는 Sirius
    프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- human_in_the_loop
- robot_learning
- continual_learning
- behavioral_cloning
- shared_autonomy
- teleoperation
- deployment
- contact_rich_manipulation
- sample_reweighting
- real_robot_hardware
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.08416v3.
sources:
- id: src_001
  type: paper
  title: 'Robot Learning on the Job: Human-in-the-Loop Autonomy and Learning During Deployment'
  url: https://arxiv.org/abs/2211.08416
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
With the rapid growth of computing powers and recent advances in deep learning, we have witnessed impressive demonstrations of novel robot capabilities in research settings. Nonetheless, these learning systems exhibit brittle generalization and require excessive training data for practical tasks. To harness the capabilities of state-of-the-art robot learning models while embracing their imperfections, we present Sirius, a principled framework for humans and robots to collaborate through a division of work. In this framework, partially autonomous robots are tasked with handling a major portion of decision-making where they work reliably; meanwhile, human operators monitor the process and intervene in challenging situations. Such a human-robot team ensures safe deployments in complex tasks. Further, we introduce a new learning algorithm to improve the policy's performance on the data collected from the task executions. The core idea is re-weighing training samples with approximated human trust and optimizing the policies with weighted behavioral cloning. We evaluate Sirius in simulation and on real hardware, showing that Sirius consistently outperforms baselines over a collection of contact-rich manipulation tasks, achieving an 8% boost in simulation and 27% on real hardware than the state-of-the-art methods in policy success rate, with twice faster convergence and 85% memory size reduction. Videos and more details are available at https://ut-austin-rpl.github.io/sirius/

## 核心内容
With the rapid growth of computing powers and recent advances in deep learning, we have witnessed impressive demonstrations of novel robot capabilities in research settings. Nonetheless, these learning systems exhibit brittle generalization and require excessive training data for practical tasks. To harness the capabilities of state-of-the-art robot learning models while embracing their imperfections, we present Sirius, a principled framework for humans and robots to collaborate through a division of work. In this framework, partially autonomous robots are tasked with handling a major portion of decision-making where they work reliably; meanwhile, human operators monitor the process and intervene in challenging situations. Such a human-robot team ensures safe deployments in complex tasks. Further, we introduce a new learning algorithm to improve the policy's performance on the data collected from the task executions. The core idea is re-weighing training samples with approximated human trust and optimizing the policies with weighted behavioral cloning. We evaluate Sirius in simulation and on real hardware, showing that Sirius consistently outperforms baselines over a collection of contact-rich manipulation tasks, achieving an 8% boost in simulation and 27% on real hardware than the state-of-the-art methods in policy success rate, with twice faster convergence and 85% memory size reduction. Videos and more details are available at https://ut-austin-rpl.github.io/sirius/

## 参考
- http://arxiv.org/abs/2211.08416v3

## Overview
With the rapid growth of computing powers and recent advances in deep learning, we have witnessed impressive demonstrations of novel robot capabilities in research settings. Nonetheless, these learning systems exhibit brittle generalization and require excessive training data for practical tasks. To harness the capabilities of state-of-the-art robot learning models while embracing their imperfections, we present Sirius, a principled framework for humans and robots to collaborate through a division of work. In this framework, partially autonomous robots are tasked with handling a major portion of decision-making where they work reliably; meanwhile, human operators monitor the process and intervene in challenging situations. Such a human-robot team ensures safe deployments in complex tasks. Further, we introduce a new learning algorithm to improve the policy's performance on the data collected from the task executions. The core idea is re-weighing training samples with approximated human trust and optimizing the policies with weighted behavioral cloning. We evaluate Sirius in simulation and on real hardware, showing that Sirius consistently outperforms baselines over a collection of contact-rich manipulation tasks, achieving an 8% boost in simulation and 27% on real hardware than the state-of-the-art methods in policy success rate, with twice faster convergence and 85% memory size reduction. Videos and more details are available at https://ut-austin-rpl.github.io/sirius/

## Content
With the rapid growth of computing powers and recent advances in deep learning, we have witnessed impressive demonstrations of novel robot capabilities in research settings. Nonetheless, these learning systems exhibit brittle generalization and require excessive training data for practical tasks. To harness the capabilities of state-of-the-art robot learning models while embracing their imperfections, we present Sirius, a principled framework for humans and robots to collaborate through a division of work. In this framework, partially autonomous robots are tasked with handling a major portion of decision-making where they work reliably; meanwhile, human operators monitor the process and intervene in challenging situations. Such a human-robot team ensures safe deployments in complex tasks. Further, we introduce a new learning algorithm to improve the policy's performance on the data collected from the task executions. The core idea is re-weighing training samples with approximated human trust and optimizing the policies with weighted behavioral cloning. We evaluate Sirius in simulation and on real hardware, showing that Sirius consistently outperforms baselines over a collection of contact-rich manipulation tasks, achieving an 8% boost in simulation and 27% on real hardware than the state-of-the-art methods in policy success rate, with twice faster convergence and 85% memory size reduction. Videos and more details are available at https://ut-austin-rpl.github.io/sirius/

## 개요
컴퓨팅 성능의 급속한 성장과 딥러닝의 최근 발전에 힘입어, 연구 환경에서 인상적인 새로운 로봇 능력 시연을 목격했습니다. 그럼에도 불구하고 이러한 학습 시스템은 취약한 일반화 능력을 보이며, 실용적인 작업을 위해 과도한 학습 데이터를 필요로 합니다. 최첨단 로봇 학습 모델의 능력을 활용하면서도 그 불완전성을 수용하기 위해, 우리는 작업 분할을 통해 인간과 로봇이 협력할 수 있는 원칙적인 프레임워크인 Sirius를 제시합니다. 이 프레임워크에서 부분 자율 로봇은 신뢰할 수 있는 의사 결정의 주요 부분을 처리하는 임무를 맡고, 인간 운영자는 프로세스를 모니터링하며 어려운 상황에 개입합니다. 이러한 인간-로봇 팀은 복잡한 작업에서 안전한 배치를 보장합니다. 또한, 작업 실행에서 수집된 데이터를 기반으로 정책의 성능을 향상시키는 새로운 학습 알고리즘을 소개합니다. 핵심 아이디어는 근사화된 인간 신뢰도로 학습 샘플에 가중치를 재부여하고, 가중 행동 복제를 통해 정책을 최적화하는 것입니다. 우리는 시뮬레이션과 실제 하드웨어에서 Sirius를 평가했으며, Sirius가 접촉이 많은 조작 작업 집합에서 기준선을 일관되게 능가하여, 최첨단 방법 대비 정책 성공률에서 시뮬레이션 8%, 실제 하드웨어 27% 향상, 두 배 빠른 수렴 속도, 85% 메모리 크기 감소를 달성함을 보여줍니다. 비디오 및 자세한 내용은 https://ut-austin-rpl.github.io/sirius/ 에서 확인할 수 있습니다.

## 핵심 내용
컴퓨팅 성능의 급속한 성장과 딥러닝의 최근 발전에 힘입어, 연구 환경에서 인상적인 새로운 로봇 능력 시연을 목격했습니다. 그럼에도 불구하고 이러한 학습 시스템은 취약한 일반화 능력을 보이며, 실용적인 작업을 위해 과도한 학습 데이터를 필요로 합니다. 최첨단 로봇 학습 모델의 능력을 활용하면서도 그 불완전성을 수용하기 위해, 우리는 작업 분할을 통해 인간과 로봇이 협력할 수 있는 원칙적인 프레임워크인 Sirius를 제시합니다. 이 프레임워크에서 부분 자율 로봇은 신뢰할 수 있는 의사 결정의 주요 부분을 처리하는 임무를 맡고, 인간 운영자는 프로세스를 모니터링하며 어려운 상황에 개입합니다. 이러한 인간-로봇 팀은 복잡한 작업에서 안전한 배치를 보장합니다. 또한, 작업 실행에서 수집된 데이터를 기반으로 정책의 성능을 향상시키는 새로운 학습 알고리즘을 소개합니다. 핵심 아이디어는 근사화된 인간 신뢰도로 학습 샘플에 가중치를 재부여하고, 가중 행동 복제를 통해 정책을 최적화하는 것입니다. 우리는 시뮬레이션과 실제 하드웨어에서 Sirius를 평가했으며, Sirius가 접촉이 많은 조작 작업 집합에서 기준선을 일관되게 능가하여, 최첨단 방법 대비 정책 성공률에서 시뮬레이션 8%, 실제 하드웨어 27% 향상, 두 배 빠른 수렴 속도, 85% 메모리 크기 감소를 달성함을 보여줍니다. 비디오 및 자세한 내용은 https://ut-austin-rpl.github.io/sirius/ 에서 확인할 수 있습니다.
