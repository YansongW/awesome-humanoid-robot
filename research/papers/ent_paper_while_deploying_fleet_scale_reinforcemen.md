---
$id: ent_paper_while_deploying_fleet_scale_reinforcemen
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies'
  zh: 'Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies'
  ko: 'Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies'
summary:
  en: 'Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies - Research - AGIBOT Finch
    Research Join us Research Latest news Join Us Hot Research LWD Learning while Deploying: Fleet-Scale Reinforcement Learning
    for Generalist Robot Policies Apr 30, 2026 Read Paper Imagi Institutions per source list: AGIBOT Research.'
  zh: LWD（Learning while Deploying）是由AGIBOT Finch Research提出的一个面向通用机器人策略的车队规模离线到在线强化学习框架。其核心贡献在于将部署过程本身转化为持续训练循环，利用整个机器人车队产生的异构经验（包括成功、失败和人工干预）来持续改进单一通用VLA策略，而非仅依赖专家演示。
  ko: 'Learning while Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies - Research - AGIBOT Finch
    Research Join us Research Latest news Join Us Hot Research LWD Learning while Deploying: Fleet-Scale Reinforcement Learning
    for Generalist Robot Policies Apr 30, 2026 Read Paper Imagi Institutions per source list: AGIBOT Research.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- while
- deploying
- fleet
- scale
- reinforcemen
- project_page_sourced
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: Full ingest from Yuanxq lab paper list row 708 (.staging/ingest_yuanxq). Tier B->page. Content compiled by DeepSeek
    from the fetched project page (https://finch.agibot.com/research/lwd). Institutions as given in the source list, not verified.
sources:
- id: src_001
  type: website
  title: Project page
  url: https://finch.agibot.com/research/lwd
  accessed_at: '2026-07-31'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

LWD框架旨在解决通用VLA策略在真实世界部署中面临的分布偏移挑战。与将部署视为评估终点的传统方法不同，LWD将部署转化为一个闭环训练循环：预训练策略被部署到机器人车队中，所有自主运行和人工干预数据被聚合到共享回放缓冲区，用于离线与在线更新。更新后的策略重新部署，从而实现利用整个车队交互数据的持续改进。LWD的关键创新在于使用统一的离线到在线强化学习方法，从完整的机器人经验谱系（包括失败和部分进展）中学习，而非仅筛选高质量演示进行模仿学习。

## 核心内容
### 方法概述
LWD是一个闭环数据飞轮，包含两个主要阶段：
- **离线RL初始化**：在在线部署前，使用先前收集的机器人数据（包括专家演示、历史运行记录和失败模式附近的探索数据）对策略和评论家进行初始化，提供稳定的起点。
- **在线部署与学习**：当前策略被部署到机器人车队中，每个机器人执行真实世界任务并将轨迹上传到共享在线回放缓冲区。集中式学习器在静态离线缓冲区和不断增长的在线缓冲区上联合训练，然后定期将更新后的策略推回车队，形成闭环RL数据飞轮。

### 核心挑战与解决方案
LWD针对车队规模通用策略RL的两个主要挑战提出了专门算法：

#### 1. 分布隐式价值学习（DIVL）
- **挑战**：车队回放数据高度异构，包含不同指令、时间跨度、奖励稀疏性和成功频率的任务。需要稳定的价值学习来从稀疏延迟奖励中提取有用改进信号，同时避免过拟合瞬态在线数据。
- **解决方案**：DIVL通过分布式的隐式价值函数学习，能够处理异构数据并稳定地估计状态-动作价值。

#### 2. 伴随匹配Q学习（QAM）
- **挑战**：现代VLA策略常使用生成式动作头（如flow-matching），通过多步去噪过程生成动作，使得基于似然的策略提取或直接策略梯度训练难以应用。
- **解决方案**：QAM通过伴随匹配技术，将Q学习与生成式动作头结合，实现从价值函数中高效提取策略更新。

### 实验设置与关键结果
- **实验平台**：在AGIBOT Finch机器人车队上进行真实世界部署测试。
- **关键指标**：LWD在多种任务（如泡功夫茶、榨果汁、调鸡尾酒）上实现了持续的性能提升，相比仅使用模仿学习的基线方法，任务成功率显著提高。
- **数据效率**：通过利用全部部署经验（包括失败和干预），LWD的数据利用率远高于仅筛选成功演示的方法，在相同数据量下实现了更快的收敛和更高的最终性能。

### 结论
LWD证明了将部署转化为持续学习循环的有效性，为通用机器人策略的规模化后训练提供了新范式。通过统一的离线到在线RL框架和针对生成式策略的专用算法，LWD能够在真实世界部署中持续改进，无需依赖人工标注的专家演示。

## 参考
- https://finch.agibot.com/research/lwd
- https://github.com/ImChong/Robotics_Notebooks

## Overview

The LWD framework aims to address the distribution shift challenges faced by general-purpose VLA policies in real-world deployment. Unlike traditional approaches that treat deployment as the endpoint of evaluation, LWD transforms deployment into a closed-loop training cycle: pre-trained policies are deployed to a fleet of robots, and all autonomous operation and human intervention data are aggregated into a shared replay buffer for offline and online updates. The updated policies are then redeployed, enabling continuous improvement that leverages interaction data from the entire fleet. The key innovation of LWD lies in using a unified offline-to-online reinforcement learning method that learns from the full spectrum of robot experience—including failures and partial progress—rather than filtering only high-quality demonstrations for imitation learning.

## Content
### Method Overview
LWD is a closed-loop data flywheel comprising two main phases:
- **Offline RL Initialization**: Before online deployment, the policy and critic are initialized using previously collected robot data (including expert demonstrations, historical operation logs, and exploration data near failure modes), providing a stable starting point.
- **Online Deployment and Learning**: The current policy is deployed to the robot fleet, where each robot performs real-world tasks and uploads trajectories to a shared online replay buffer. A centralized learner trains jointly on the static offline buffer and the growing online buffer, then periodically pushes the updated policy back to the fleet, forming a closed-loop RL data flywheel.

### Core Challenges and Solutions
LWD proposes specialized algorithms to address two major challenges in fleet-scale generalist policy RL:

#### 1. Distributional Implicit Value Learning (DIVL)
- **Challenge**: Fleet replay data is highly heterogeneous, containing tasks with different instructions, time horizons, reward sparsity, and success frequencies. Stable value learning is needed to extract useful improvement signals from sparse delayed rewards while avoiding overfitting to transient online data.
- **Solution**: DIVL learns implicit value functions in a distributional manner, enabling it to handle heterogeneous data and stably estimate state-action values.

#### 2. Q-learning with Adjoint Matching (QAM)
- **Challenge**: Modern VLA policies often use generative action heads (e.g., flow-matching) that generate actions through multi-step denoising processes, making likelihood-based policy extraction or direct policy gradient training difficult to apply.
- **Solution**: QAM combines Q-learning with generative action heads via adjoint matching techniques, enabling efficient policy updates extracted from the value function.

### Experimental Setup and Key Results
- **Experimental Platform**: Real-world deployment tests were conducted on an AGIBOT Finch robot fleet.
- **Key Metrics**: LWD achieved continuous performance improvements across multiple tasks (e.g., brewing Kung Fu tea, juicing, mixing cocktails), with significantly higher task success rates compared to imitation-learning-only baselines.
- **Data Efficiency**: By leveraging all deployment experience (including failures and interventions), LWD achieves far higher data utilization than methods that filter only successful demonstrations, resulting in faster convergence and higher final performance with the same amount of data.

### Conclusion
LWD demonstrates the effectiveness of transforming deployment into a continuous learning loop, providing a new paradigm for scalable post-training of generalist robot policies. Through a unified offline-to-online RL framework and specialized algorithms for generative policies, LWD enables continuous improvement in real-world deployment without relying on human-annotated expert demonstrations.

## 개요

LWD 프레임워크는 범용 VLA 정책이 실제 세계 배포에서 직면하는 분포 이동 문제를 해결하기 위해 설계되었습니다. 배포를 평가의 종착점으로 보는 전통적인 접근 방식과 달리, LWD는 배포를 폐쇄 루프 훈련 주기로 전환합니다: 사전 훈련된 정책이 로봇 차량군에 배포되고, 모든 자율 실행 및 인간 개입 데이터가 공유 리플레이 버퍼에 집계되어 오프라인 및 온라인 업데이트에 사용됩니다. 업데이트된 정책은 재배포되어 차량군 전체의 상호작용 데이터를 활용한 지속적 개선을 가능하게 합니다. LWD의 핵심 혁신은 실패 및 부분 진행을 포함한 전체 로봇 경험 스펙트럼에서 학습하는 통합된 오프라인-투-온라인 강화 학습 방법을 사용한다는 점이며, 고품질 데모만 선별하여 모방 학습을 수행하는 방식과는 차별화됩니다.

## 핵심 내용
### 방법 개요
LWD는 두 가지 주요 단계를 포함하는 폐쇄 루프 데이터 플라이휠입니다:
- **오프라인 RL 초기화**: 온라인 배포 전에 이전에 수집된 로봇 데이터(전문가 데모, 과거 실행 기록, 실패 모드 주변 탐색 데이터 포함)를 사용하여 정책과 크리틱을 초기화하여 안정적인 출발점을 제공합니다.
- **온라인 배포 및 학습**: 현재 정책이 로봇 차량군에 배포되고, 각 로봇은 실제 세계 작업을 수행하며 궤적을 공유 온라인 리플레이 버퍼에 업로드합니다. 중앙 집중식 학습기는 정적 오프라인 버퍼와 증가하는 온라인 버퍼에서 공동으로 훈련한 후, 주기적으로 업데이트된 정책을 차량군에 다시 푸시하여 폐쇄 루프 RL 데이터 플라이휠을 형성합니다.

### 핵심 과제 및 해결책
LWD는 차량군 규모의 범용 정책 RL에서 발생하는 두 가지 주요 과제에 대한 전용 알고리즘을 제안합니다:

#### 1. 분포 암시적 가치 학습 (DIVL)
- **과제**: 차량군 리플레이 데이터는 서로 다른 명령, 시간 범위, 보상 희소성 및 성공 빈도를 가진 작업을 포함하여 매우 이질적입니다. 희소하고 지연된 보상에서 유용한 개선 신호를 추출하면서도 일시적인 온라인 데이터에 과적합되지 않도록 안정적인 가치 학습이 필요합니다.
- **해결책**: DIVL은 분포 기반의 암시적 가치 함수 학습을 통해 이질적 데이터를 처리하고 상태-행동 가치를 안정적으로 추정합니다.

#### 2. 수반 매칭 Q-러닝 (QAM)
- **과제**: 현대 VLA 정책은 종종 flow-matching과 같은 생성적 행동 헤드를 사용하여 다단계 노이즈 제거 과정을 통해 행동을 생성하므로, 우도 기반 정책 추출이나 직접 정책 그래디언트 훈련을 적용하기 어렵습니다.
- **해결책**: QAM은 수반 매칭 기법을 통해 Q-러닝과 생성적 행동 헤드를 결합하여 가치 함수에서 정책 업데이트를 효율적으로 추출합니다.

### 실험 설정 및 주요 결과
- **실험 플랫폼**: AGIBOT Finch 로봇 차량군에서 실제 세계 배포 테스트를 수행했습니다.
- **주요 지표**: LWD는 다양한 작업(예: 공푸 차 만들기, 과일 주스 짜기, 칵테일 제조)에서 지속적인 성능 향상을 달성했으며, 모방 학습만 사용하는 기준 방법에 비해 작업 성공률이 크게 향상되었습니다.
- **데이터 효율성**: 모든 배포 경험(실패 및 개입 포함)을 활용함으로써 LWD는 성공 데모만 선별하는 방법보다 데이터 활용도가 훨씬 높았으며, 동일한 데이터 양에서 더 빠른 수렴과 더 높은 최종 성능을 달성했습니다.

### 결론
LWD는 배포를 지속적 학습 주기로 전환하는 효과를 입증하며, 범용 로봇 정책의 대규모 사후 훈련을 위한 새로운 패러다임을 제시합니다. 통합된 오프라인-투-온라인 RL 프레임워크와 생성적 정책을 위한 전용 알고리즘을 통해 LWD는 인간이 주석을 단 전문가 데모에 의존하지 않고도 실제 세계 배포에서 지속적으로 개선될 수 있습니다.
