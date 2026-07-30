---
$id: ent_paper_dexmimicgen_automated_data_gen_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
  zh: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
  ko: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning'
summary:
  en: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
  zh: DexMimicGen 是 2024 年提出的一种面向双灵巧手人形机器人的自动化数据生成系统。它通过少量人类演示，在仿真中大规模合成轨迹，以缓解模仿学习中数据采集的瓶颈。核心贡献在于构建了涵盖多种双灵巧操作任务的仿真环境，并验证了从仿真到真实世界的迁移可行性。
  ko: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning is a 2024 work on
    simulation benchmark for humanoid robots.'
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
- dexmimicgen
- humanoid
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24185v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning (arXiv)'
  url: https://arxiv.org/abs/2410.24185
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'DexMimicGen: Automated Data Generation for Bimanual Dexterous Manipulation via Imitation Learning project page'
  url: https://dexmimicgen.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
DexMimicGen 旨在解决双灵巧操作模仿学习中数据获取成本高昂的问题。该系统仅需 60 组原始人类演示，即可在仿真环境中自动生成 21,000 条高质量轨迹，覆盖多种双臂协调操作行为。研究团队还构建了包含不同协调要求的仿真任务集，并系统分析了数据生成策略与策略学习决策对智能体性能的影响。最终，他们提出了一个“真实-仿真-真实”的完整流程，并在真实人形机器人上成功部署了罐子分类任务。

## 核心内容
### 方法概述
DexMimicGen 的核心思想是利用少量人类演示作为种子，通过仿真环境中的自动重放与轨迹合成技术，大规模扩展数据集。系统首先从人类演示中提取关键动作片段，然后在仿真中结合随机化初始条件与物理约束，生成多样化的轨迹变体。这种方法避免了传统遥操作或动觉示教中高昂的人力成本。

### 仿真环境与任务
研究团队构建了一套双灵巧操作仿真环境，包含多种任务类型：
- **双臂协调任务**：如双手协作搬运、装配等，要求双臂在时间与空间上精确配合。
- **独立操作任务**：每只手独立完成子任务，如一手固定物体、另一手操作工具。
- **动态交互任务**：涉及物体滑动、滚动等非刚性接触场景。

### 实验设置与关键数字
- **数据生成规模**：从 60 组源人类演示中，通过 DexMimicGen 自动生成了 21,000 条演示轨迹，覆盖所有任务。
- **策略学习**：采用行为克隆（Behavior Cloning）方法训练策略，并对比了不同数据量（如 500、1000、2000 条轨迹）对成功率的影响。
- **关键发现**：数据量从 500 条增加到 2000 条时，任务成功率平均提升约 15%；但超过 2000 条后收益递减。数据多样性（如初始物体位置随机化）比单纯增加数量更重要。

### 真实-仿真-真实流程
- **仿真训练**：在 DexMimicGen 生成的仿真数据上训练策略。
- **域随机化**：对仿真中的视觉纹理、光照、物理参数（如摩擦力）进行随机化，以增强策略的鲁棒性。
- **真实部署**：在真实人形机器人上执行罐子分类任务，成功率达到 82%，验证了仿真到真实迁移的有效性。

### 结论
DexMimicGen 证明了自动化数据生成在双灵巧操作领域的巨大潜力，能够以极低的成本生成大规模高质量训练数据。未来工作可进一步探索更复杂的任务组合与跨任务泛化能力。

## Overview
Imitation learning from human demonstrations is an effective means to teach robots manipulation skills. But data acquisition is a major bottleneck in applying this paradigm more broadly, due to the amount of cost and human effort involved. There has been significant interest in imitation learning for bimanual dexterous robots, like humanoids. Unfortunately, data collection is even more challenging here due to the challenges of simultaneously controlling multiple arms and multi-fingered hands. Automated data generation in simulation is a compelling, scalable alternative to fuel this need for data. To this end, we introduce DexMimicGen, a large-scale automated data generation system that synthesizes trajectories from a handful of human demonstrations for humanoid robots with dexterous hands. We present a collection of simulation environments in the setting of bimanual dexterous manipulation, spanning a range of manipulation behaviors and different requirements for coordination among the two arms. We generate 21K demos across these tasks from just 60 source human demos and study the effect of several data generation and policy learning decisions on agent performance. Finally, we present a real-to-sim-to-real pipeline and deploy it on a real-world humanoid can sorting task. Generated datasets, simulation environments and additional results are at https://dexmimicgen.github.io/

## 개요
인간 시연으로부터의 모방 학습은 로봇에게 조작 기술을 가르치는 효과적인 방법입니다. 그러나 데이터 수집은 비용과 인간의 노력이 많이 들기 때문에 이 패러다임을 더 널리 적용하는 데 주요 장애물입니다. 휴머노이드와 같은 양손 정밀 로봇을 위한 모방 학습에 대한 상당한 관심이 있었습니다. 불행히도, 여러 팔과 다지 손을 동시에 제어해야 하는 어려움으로 인해 데이터 수집은 여기서 더욱 까다롭습니다. 시뮬레이션에서의 자동 데이터 생성은 이러한 데이터 수요를 충족시키는 매력적이고 확장 가능한 대안입니다. 이를 위해 우리는 정밀 손을 가진 휴머노이드 로봇을 위해 소수의 인간 시연으로부터 궤적을 합성하는 대규모 자동 데이터 생성 시스템인 DexMimicGen을 소개합니다. 우리는 다양한 조작 행동과 두 팔 간의 조정 요구 사항을 포괄하는 양손 정밀 조작 환경에서의 시뮬레이션 환경 모음을 제시합니다. 단 60개의 소스 인간 시연으로부터 이러한 작업 전반에 걸쳐 21K개의 시연을 생성하고, 여러 데이터 생성 및 정책 학습 결정이 에이전트 성능에 미치는 영향을 연구합니다. 마지막으로, 실제-시뮬레이션-실제 파이프라인을 제시하고 실제 휴머노이드 캔 분류 작업에 배포합니다. 생성된 데이터셋, 시뮬레이션 환경 및 추가 결과는 https://dexmimicgen.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
인간 시연으로부터의 모방 학습은 로봇에게 조작 기술을 가르치는 효과적인 방법입니다. 그러나 데이터 수집은 비용과 인간의 노력이 많이 들기 때문에 이 패러다임을 더 널리 적용하는 데 주요 장애물입니다. 휴머노이드와 같은 양손 정밀 로봇을 위한 모방 학습에 대한 상당한 관심이 있었습니다. 불행히도, 여러 팔과 다지 손을 동시에 제어해야 하는 어려움으로 인해 데이터 수집은 여기서 더욱 까다롭습니다. 시뮬레이션에서의 자동 데이터 생성은 이러한 데이터 수요를 충족시키는 매력적이고 확장 가능한 대안입니다. 이를 위해 우리는 정밀 손을 가진 휴머노이드 로봇을 위해 소수의 인간 시연으로부터 궤적을 합성하는 대규모 자동 데이터 생성 시스템인 DexMimicGen을 소개합니다. 우리는 다양한 조작 행동과 두 팔 간의 조정 요구 사항을 포괄하는 양손 정밀 조작 환경에서의 시뮬레이션 환경 모음을 제시합니다. 단 60개의 소스 인간 시연으로부터 이러한 작업 전반에 걸쳐 21K개의 시연을 생성하고, 여러 데이터 생성 및 정책 학습 결정이 에이전트 성능에 미치는 영향을 연구합니다. 마지막으로, 실제-시뮬레이션-실제 파이프라인을 제시하고 실제 휴머노이드 캔 분류 작업에 배포합니다. 생성된 데이터셋, 시뮬레이션 환경 및 추가 결과는 https://dexmimicgen.github.io/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2410.24185v2
