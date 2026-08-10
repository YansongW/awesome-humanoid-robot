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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.08416v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (852 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2211.08416v3

## 개요
Sirius 프레임워크는 로봇 학습 모델이 실제 작업에서 일반화 능력이 약하고 훈련 데이터 요구량이 큰 문제를 해결하는 데 목적을 둡니다. 이는 분업 협력을 통해 로봇이 대부분의 신뢰할 수 있는 결정을 자율적으로 처리하고, 인간 운영자는 복잡한 상황을 모니터링하고 개입하여 안전한 배포를 보장합니다. 이 프레임워크는 또한 근사 인간 신뢰도를 활용하여 훈련 샘플을 재가중하고, 가중 행동 클로닝을 통해 정책을 최적화하는 새로운 학습 알고리즘을 도입합니다. 시뮬레이션 및 실제 하드웨어에서의 접촉이 많은 조작 작업 평가에서 Sirius는 정책 성공률, 수렴 속도 및 메모리 사용량 측면에서 기존 방법보다 현저히 우수합니다.

## 핵심 내용
### 방법
Sirius 프레임워크의 핵심은 **인간-로봇 분업 협력**입니다: 로봇은 신뢰할 수 있는 결정 부분을 처리하고, 인간 운영자는 전체 과정을 모니터링하며 로봇이 어려움에 직면했을 때 원격 조작을 통해 개입합니다. 이러한 협력은 복잡한 작업에서 안전한 배포를 보장합니다.

### 학습 알고리즘
프레임워크는 새로운 학습 알고리즘을 도입하며, 핵심 아이디어는 다음과 같습니다:
- **데이터 재가중**: 근사 인간 신뢰도를 활용하여 작업 실행 중 수집된 훈련 샘플을 재가중합니다.
- **정책 최적화**: **가중 행동 클로닝**(Weighted Behavioral Cloning)을 통해 정책을 최적화하여 로봇이 인간 개입에서 더 효과적으로 학습하도록 합니다.

### 실험 설정
- **작업**: 일련의 접촉이 많은 조작 작업(contact-rich manipulation tasks).
- **평가 환경**: 시뮬레이션 환경 및 실제 하드웨어 플랫폼.
- **기준 방법**: 현재 최첨단 방법과 비교.

### 주요 결과
- **정책 성공률**: Sirius는 시뮬레이션 환경에서 최첨단 방법보다 **8%** 향상, 실제 하드웨어에서 **27%** 향상.
- **수렴 속도**: 수렴 속도는 기존 방법의 **두 배**(twice faster convergence).
- **메모리 사용량**: 메모리 사용량 **85%** 감소(85% memory size reduction).

### 결론
Sirius는 인간-로봇 협력과 데이터 재가중 학습을 통해 접촉이 많은 조작 작업에서 정책 성능, 수렴 효율성을 현저히 향상시키고 메모리 요구량을 줄여 실제 배포에서의 효과를 검증했습니다. 더 많은 세부 사항과 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다.
