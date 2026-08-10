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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24185v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1025 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.24185v2

## 개요
DexMimicGen은 이중 손재주 조작 모방 학습에서 데이터 수집 비용이 높은 문제를 해결하는 것을 목표로 합니다. 이 시스템은 단 60개의 원본 인간 시연만으로 시뮬레이션 환경에서 21,000개의 고품질 궤적을 자동 생성하며, 다양한 양팔 협조 조작 행동을 포괄합니다. 연구팀은 또한 서로 다른 협조 요구 사항을 포함하는 시뮬레이션 작업 세트를 구축하고, 데이터 생성 전략과 정책 학습 결정이 에이전트 성능에 미치는 영향을 체계적으로 분석했습니다. 마지막으로, 그들은 '실제-시뮬레이션-실제'의 완전한 흐름을 제안하고 실제 휴머노이드 로봇에서 캔 분류 작업을 성공적으로 배포했습니다.

## 핵심 내용
### 방법 개요
DexMimicGen의 핵심 아이디어는 소수의 인간 시연을 시드로 사용하여 시뮬레이션 환경에서 자동 재생 및 궤적 합성 기술을 통해 데이터 세트를 대규모로 확장하는 것입니다. 시스템은 먼저 인간 시연에서 핵심 동작 세그먼트를 추출한 다음, 시뮬레이션에서 무작위 초기 조건과 물리적 제약을 결합하여 다양한 궤적 변형을 생성합니다. 이 방법은 전통적인 원격 조작이나 운동 감각 시연에서 발생하는 높은 인건비를 피합니다.

### 시뮬레이션 환경 및 작업
연구팀은 다양한 작업 유형을 포함하는 이중 손재주 조작 시뮬레이션 환경을 구축했습니다:
- **양팔 협조 작업**: 양손 협력 운반, 조립 등과 같은 작업으로, 양팔이 시간과 공간에서 정밀하게 협조해야 합니다.
- **독립 조작 작업**: 각 손이 하위 작업을 독립적으로 완료하는 작업, 예를 들어 한 손은 물체를 고정하고 다른 손은 도구를 조작하는 경우입니다.
- **동적 상호작용 작업**: 물체의 미끄러짐, 굴림 등 비강성 접촉 시나리오를 포함합니다.

### 실험 설정 및 핵심 수치
- **데이터 생성 규모**: 60개의 원본 인간 시연에서 DexMimicGen을 통해 21,000개의 시연 궤적을 자동 생성하여 모든 작업을 포괄했습니다.
- **정책 학습**: 행동 복제(Behavior Cloning) 방법을 사용하여 정책을 훈련하고, 서로 다른 데이터 양(예: 500, 1000, 2000개의 궤적)이 성공률에 미치는 영향을 비교했습니다.
- **핵심 발견**: 데이터 양이 500개에서 2000개로 증가할 때 작업 성공률이 평균 약 15% 향상되었지만, 2000개를 초과하면 수익이 감소했습니다. 데이터 다양성(예: 초기 물체 위치 무작위화)은 단순히 양을 늘리는 것보다 더 중요합니다.

### 실제-시뮬레이션-실제 흐름
- **시뮬레이션 훈련**: DexMimicGen이 생성한 시뮬레이션 데이터에서 정책을 훈련합니다.
- **도메인 무작위화**: 시뮬레이션의 시각적 텍스처, 조명, 물리적 매개변수(예: 마찰력)를 무작위화하여 정책의 견고성을 강화합니다.
- **실제 배포**: 실제 휴머노이드 로봇에서 캔 분류 작업을 실행하여 성공률 82%를 달성했으며, 시뮬레이션에서 실제로의 전이 효과를 검증했습니다.

### 결론
DexMimicGen은 이중 손재주 조작 분야에서 자동화된 데이터 생성의 엄청난 잠재력을 증명하며, 매우 낮은 비용으로 대규모 고품질 훈련 데이터를 생성할 수 있습니다. 향후 작업은 더 복잡한 작업 조합과 교차 작업 일반화 능력을 추가로 탐구할 수 있습니다.
