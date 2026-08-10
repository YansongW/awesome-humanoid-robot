---
$id: ent_paper_seo_learning_sim_to_real_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  zh: 在15分钟内学习从仿真到现实的人形机器人运动
  ko: 15분 만에 학습하는 시뮬레이션-현실 간 휴머노이드 보행
summary:
  en: This paper presents a practical recipe using FastSAC and FastTD3 with massively parallel simulation to train robust
    full-body humanoid locomotion policies on a single RTX 4090 GPU in 15 minutes, and demonstrates sim-to-real deployment
    on Unitree G1 and Booster T1 robots.
  zh: 本文提出一种基于FastSAC和FastTD3的实用方案，利用大规模并行仿真在单张RTX 4090 GPU上仅需15分钟即可训练出鲁棒的全身体人形运动策略，并在Unitree G1和Booster T1机器人上实现了仿真到现实的部署。
  ko: 본 논문은 대규모 병렬 시뮬레이션과 FastSAC 및 FastTD3를 활용한 실용적인 방법론을 제안하여 단일 RTX 4090 GPU에서 15분 만에 강건한 전신 휴머노이드 보행 정책을 학습하고, Unitree
    G1과 Booster T1 로봇에서 sim-to-real 전개를 입증한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- intelligence
- knowledge
tags:
- sim_to_real
- reinforcement_learning
- off_policy_rl
- fastsac
- fasttd3
- humanoid_locomotion
- whole_body_motion_tracking
- domain_randomization
- unitree_g1
- booster_t1
- rtx_4090
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01996v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (690 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Sim-to-Real Humanoid Locomotion in 15 Minutes
  url: https://arxiv.org/abs/2512.01996
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
该工作针对人形机器人强化学习训练中高维度和域随机化带来的挑战，通过精心调整的设计选择和极简奖励函数，在数千个并行环境中稳定了离策略RL算法的大规模训练。实验证明，该方法能在强域随机化条件下（如随机动力学、崎岖地形和推挤扰动）快速学习端到端的人形运动控制器，并支持全身人体运动跟踪策略的快速训练。

## 核心内容
### 方法核心
- **算法基础**：采用离策略RL算法FastSAC和FastTD3，通过大规模并行仿真（数千个环境）实现高效训练。
- **关键设计**：通过精心调优的超参数和极简奖励函数，解决了离策略算法在大规模并行场景下的稳定性问题。
- **训练效率**：单张RTX 4090 GPU上15分钟完成训练，相比传统方法（数天）大幅缩短。

### 实验设置
- **机器人平台**：Unitree G1和Booster T1两款人形机器人。
- **域随机化**：包括随机动力学参数、崎岖地形、推挤扰动等强干扰条件。
- **任务类型**：端到端人形运动控制（行走、奔跑）和全身人体运动跟踪。

### 关键结果
- **训练速度**：15分钟完成策略训练，达到可部署的鲁棒性。
- **仿真到现实迁移**：在两种不同硬件上成功部署，验证了方法的泛化能力。
- **开源资源**：提供视频演示和开源代码（https://younggyo.me/fastsac-humanoid）。

### 结论
该工作证明，通过合理的算法选择和工程优化，离策略RL方法可在极短时间内训练出适用于真实人形机器人的运动策略，为快速迭代和低成本部署提供了实用方案。

## Overview
Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization. In this work, we introduce a simple and practical recipe based on off-policy RL algorithms, i.e., FastSAC and FastTD3, that enables rapid training of humanoid locomotion policies in just 15 minutes with a single RTX 4090 GPU. Our simple recipe stabilizes off-policy RL algorithms at massive scale with thousands of parallel environments through carefully tuned design choices and minimalist reward functions. We demonstrate rapid end-to-end learning of humanoid locomotion controllers on Unitree G1 and Booster T1 robots under strong domain randomization, e.g., randomized dynamics, rough terrain, and push perturbations, as well as fast training of whole-body human-motion tracking policies. We provide videos and open-source implementation at: https://younggyo.me/fastsac-humanoid.

## 参考
- http://arxiv.org/abs/2512.01996v1

## 개요
이 연구는 휴머노이드 로봇 강화학습 훈련에서 고차원성과 도메인 무작위화가 가져오는 도전 과제를 해결하기 위해, 세심하게 조정된 설계 선택과 극도로 단순화된 보상 함수를 통해 수천 개의 병렬 환경에서 off-policy RL 알고리즘의 대규모 훈련을 안정화했습니다. 실험 결과, 이 방법은 강한 도메인 무작위화 조건(예: 무작위 동역학, 험준한 지형, 밀기 교란)에서 엔드투엔드 휴머노이드 운동 컨트롤러를 빠르게 학습할 수 있으며, 전신 인간 동작 추적 정책의 빠른 훈련도 지원합니다.

## 핵심 내용
### 방법 핵심
- **알고리즘 기반**: off-policy RL 알고리즘인 FastSAC와 FastTD3를 사용하며, 대규모 병렬 시뮬레이션(수천 개 환경)을 통해 효율적인 훈련을 구현합니다.
- **핵심 설계**: 세심하게 튜닝된 하이퍼파라미터와 극도로 단순화된 보상 함수를 통해 대규모 병렬 시나리오에서 off-policy 알고리즘의 안정성 문제를 해결합니다.
- **훈련 효율성**: 단일 RTX 4090 GPU에서 15분 만에 훈련을 완료하며, 기존 방법(수일 소요)에 비해 크게 단축됩니다.

### 실험 설정
- **로봇 플랫폼**: Unitree G1 및 Booster T1 두 종류의 휴머노이드 로봇.
- **도메인 무작위화**: 무작위 동역학 파라미터, 험준한 지형, 밀기 교란 등 강한 교란 조건 포함.
- **작업 유형**: 엔드투엔드 휴머노이드 운동 제어(보행, 달리기) 및 전신 인간 동작 추적.

### 핵심 결과
- **훈련 속도**: 15분 만에 정책 훈련을 완료하여 배포 가능한 견고성을 달성.
- **시뮬레이션-실제 전이**: 두 가지 서로 다른 하드웨어에서 성공적으로 배포되어 방법의 일반화 능력을 검증.
- **오픈소스 자료**: 비디오 데모 및 오픈소스 코드 제공 (https://younggyo.me/fastsac-humanoid).

### 결론
이 연구는 합리적인 알고리즘 선택과 엔지니어링 최적화를 통해 off-policy RL 방법이 극도로 짧은 시간 내에 실제 휴머노이드 로봇에 적용 가능한 운동 정책을 훈련할 수 있음을 증명하며, 빠른 반복과 저비용 배포를 위한 실용적인 솔루션을 제공합니다.
