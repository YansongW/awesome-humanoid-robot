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
  zh: 本文提出Sirius框架，部分自主机器人在可靠决策中运行，人工监控并在困难情况下遥操作干预，然后通过对重新加权的部署数据进行加权行为克隆来持续改进策略。
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

