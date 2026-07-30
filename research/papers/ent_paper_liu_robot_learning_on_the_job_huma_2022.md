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
  zh: Sirius 是一个人机协作框架，由德克萨斯大学奥斯汀分校提出。其核心贡献在于：让部分自主的机器人处理可靠决策，人类监控并远程干预，再通过加权行为克隆优化策略。实验表明，Sirius 在接触丰富的操作任务中，策略成功率比最先进方法提升
    8%（仿真）和 27%（真实硬件），收敛速度翻倍，内存占用减少 85%。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.08416v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
Sirius 框架旨在解决机器人学习模型在现实任务中泛化能力弱、训练数据需求大的问题。它通过分工协作，让机器人自主处理大部分可靠决策，人类操作员则监控并干预复杂情况，确保安全部署。该框架还引入了一种新学习算法，利用近似人类信任度对训练样本重新加权，并通过加权行为克隆优化策略。在仿真和真实硬件上的接触丰富操作任务评估中，Sirius 在策略成功率、收敛速度和内存占用方面均显著优于现有方法。

## 核心内容
### 方法
Sirius 框架的核心是**人机分工协作**：机器人负责处理其可靠决策的部分，人类操作员则监控整个过程，并在机器人遇到困难时通过远程操作进行干预。这种协作确保了复杂任务中的安全部署。

### 学习算法
框架引入了一种新的学习算法，其核心思想是：
- **数据重加权**：利用近似的人类信任度对任务执行过程中收集的训练样本进行重新加权。
- **策略优化**：通过**加权行为克隆**（Weighted Behavioral Cloning）优化策略，使机器人从人类干预中更有效地学习。

### 实验设置
- **任务**：一系列接触丰富的操作任务（contact-rich manipulation tasks）。
- **评估环境**：仿真环境与真实硬件平台。
- **基线方法**：与当前最先进的方法进行对比。

### 关键结果
- **策略成功率**：Sirius 在仿真环境中比最先进方法提升 **8%**，在真实硬件上提升 **27%**。
- **收敛速度**：收敛速度是现有方法的 **两倍**（twice faster convergence）。
- **内存占用**：内存占用减少 **85%**（85% memory size reduction）。

### 结论
Sirius 通过人机协作与数据重加权学习，在接触丰富的操作任务中显著提升了策略性能、收敛效率并降低了内存需求，验证了其在实际部署中的有效性。更多细节和视频可访问项目网站。

## Overview
With the rapid growth of computing powers and recent advances in deep learning, we have witnessed impressive demonstrations of novel robot capabilities in research settings. Nonetheless, these learning systems exhibit brittle generalization and require excessive training data for practical tasks. To harness the capabilities of state-of-the-art robot learning models while embracing their imperfections, we present Sirius, a principled framework for humans and robots to collaborate through a division of work. In this framework, partially autonomous robots are tasked with handling a major portion of decision-making where they work reliably; meanwhile, human operators monitor the process and intervene in challenging situations. Such a human-robot team ensures safe deployments in complex tasks. Further, we introduce a new learning algorithm to improve the policy's performance on the data collected from the task executions. The core idea is re-weighing training samples with approximated human trust and optimizing the policies with weighted behavioral cloning. We evaluate Sirius in simulation and on real hardware, showing that Sirius consistently outperforms baselines over a collection of contact-rich manipulation tasks, achieving an 8% boost in simulation and 27% on real hardware than the state-of-the-art methods in policy success rate, with twice faster convergence and 85% memory size reduction. Videos and more details are available at https://ut-austin-rpl.github.io/sirius/

## 개요
컴퓨팅 성능의 급속한 성장과 딥러닝의 최근 발전에 힘입어, 연구 환경에서 인상적인 새로운 로봇 능력 시연을 목격했습니다. 그럼에도 불구하고 이러한 학습 시스템은 취약한 일반화 능력을 보이며, 실용적인 작업을 위해 과도한 학습 데이터를 필요로 합니다. 최첨단 로봇 학습 모델의 능력을 활용하면서도 그 불완전성을 수용하기 위해, 우리는 작업 분할을 통해 인간과 로봇이 협력할 수 있는 원칙적인 프레임워크인 Sirius를 제시합니다. 이 프레임워크에서 부분 자율 로봇은 신뢰할 수 있는 의사 결정의 주요 부분을 처리하는 임무를 맡고, 인간 운영자는 프로세스를 모니터링하며 어려운 상황에 개입합니다. 이러한 인간-로봇 팀은 복잡한 작업에서 안전한 배치를 보장합니다. 또한, 작업 실행에서 수집된 데이터를 기반으로 정책의 성능을 향상시키는 새로운 학습 알고리즘을 소개합니다. 핵심 아이디어는 근사화된 인간 신뢰도로 학습 샘플에 가중치를 재부여하고, 가중 행동 복제를 통해 정책을 최적화하는 것입니다. 우리는 시뮬레이션과 실제 하드웨어에서 Sirius를 평가했으며, Sirius가 접촉이 많은 조작 작업 집합에서 기준선을 일관되게 능가하여, 최첨단 방법 대비 정책 성공률에서 시뮬레이션 8%, 실제 하드웨어 27% 향상, 두 배 빠른 수렴 속도, 85% 메모리 크기 감소를 달성함을 보여줍니다. 비디오 및 자세한 내용은 https://ut-austin-rpl.github.io/sirius/ 에서 확인할 수 있습니다.

## 핵심 내용
컴퓨팅 성능의 급속한 성장과 딥러닝의 최근 발전에 힘입어, 연구 환경에서 인상적인 새로운 로봇 능력 시연을 목격했습니다. 그럼에도 불구하고 이러한 학습 시스템은 취약한 일반화 능력을 보이며, 실용적인 작업을 위해 과도한 학습 데이터를 필요로 합니다. 최첨단 로봇 학습 모델의 능력을 활용하면서도 그 불완전성을 수용하기 위해, 우리는 작업 분할을 통해 인간과 로봇이 협력할 수 있는 원칙적인 프레임워크인 Sirius를 제시합니다. 이 프레임워크에서 부분 자율 로봇은 신뢰할 수 있는 의사 결정의 주요 부분을 처리하는 임무를 맡고, 인간 운영자는 프로세스를 모니터링하며 어려운 상황에 개입합니다. 이러한 인간-로봇 팀은 복잡한 작업에서 안전한 배치를 보장합니다. 또한, 작업 실행에서 수집된 데이터를 기반으로 정책의 성능을 향상시키는 새로운 학습 알고리즘을 소개합니다. 핵심 아이디어는 근사화된 인간 신뢰도로 학습 샘플에 가중치를 재부여하고, 가중 행동 복제를 통해 정책을 최적화하는 것입니다. 우리는 시뮬레이션과 실제 하드웨어에서 Sirius를 평가했으며, Sirius가 접촉이 많은 조작 작업 집합에서 기준선을 일관되게 능가하여, 최첨단 방법 대비 정책 성공률에서 시뮬레이션 8%, 실제 하드웨어 27% 향상, 두 배 빠른 수렴 속도, 85% 메모리 크기 감소를 달성함을 보여줍니다. 비디오 및 자세한 내용은 https://ut-austin-rpl.github.io/sirius/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2211.08416v3
