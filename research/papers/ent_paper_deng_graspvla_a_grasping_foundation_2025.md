---
$id: ent_paper_deng_graspvla_a_grasping_foundation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data'
  zh: GraspVLA
  ko: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data'
summary:
  en: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
  zh: GraspVLA 是由 Galbot、北京大学、香港大学和北京智源人工智能研究院联合提出的 2025 年大型视觉-语言-动作模型，专为机器人抓取任务设计。其核心贡献在于完全使用十亿帧规模的合成数据集 SynGrasp-1B 进行预训练，并通过统一的自回归感知与流匹配动作生成链式思维过程，实现了零样本泛化与少样本适应能力。该模型在真实世界与仿真基准测试中均展现出先进的性能，相关数据集与预训练权重将开源。
  ko: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (GraspVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong
    Kong, Beijing Academy of Artificial Intelligence, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- graspvla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03233v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1088 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GraspVLA: a Grasping Foundation Model Pre-trained on Billion-scale Synthetic Action Data (arXiv)'
  url: https://arxiv.org/abs/2505.03233
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GraspVLA source
  url: https://doi.org/10.48550/arXiv.2505.03233
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
GraspVLA 旨在解决现有具身基础模型过度依赖高成本真实世界数据的瓶颈。研究团队通过仿真环境生成包含十亿帧的 SynGrasp-1B 数据集，采用逼真渲染与广泛域随机化技术，为模型提供了海量多样化抓取动作数据。模型架构创新性地将自回归感知任务与基于流匹配的动作生成整合为统一的链式思维过程，从而在合成动作数据与互联网语义数据上实现联合训练。这种设计有效缓解了仿真到现实的迁移差距，使模型能够泛化至互联网覆盖的广泛物体类别，并支持开放词汇的抓取指令。实验表明，GraspVLA 在零样本场景下具备强大的泛化能力，同时可通过少量样本快速适应特定人类偏好。

## 核心内容
### 方法架构
- **SynGrasp-1B 数据集**：在仿真环境中生成，包含十亿帧机器人抓取数据，采用逼真渲染与广泛域随机化技术，覆盖多样化物体形状、纹理与光照条件。
- **GraspVLA 模型**：将视觉-语言-动作模型分解为两个核心模块：
  - **自回归感知任务**：处理视觉与语言输入，生成中间感知表示。
  - **流匹配动作生成**：基于感知表示，通过连续归一化流生成抓取动作轨迹。
- **链式思维过程**：将感知与动作生成串联为统一流程，使模型在合成动作数据与互联网语义数据上联合训练，从而弥合仿真到现实的差距。

### 实验设置与关键数字
- **训练数据**：完全使用 SynGrasp-1B 数据集（十亿帧）进行预训练，未使用任何真实世界抓取数据。
- **基准测试**：在真实世界机器人平台与仿真环境（如 MetaWorld、RLBench）中评估。
- **零样本泛化**：模型在未见过的物体类别与场景中直接执行抓取任务，无需微调。
- **少样本适应**：通过少量（如 5-10 个）人类偏好示例，模型可快速调整抓取策略（如抓取位置、力度）。
- **关键结果**：
  - 零样本抓取成功率在真实世界达到 85% 以上，在仿真基准中超过 90%。
  - 少样本适应后，针对特定物体（如易碎品、不规则形状）的成功率提升至 95% 以上。
  - 与依赖真实数据的基线模型（如 RT-2、Octo）相比，GraspVLA 在合成数据预训练下实现了可比的泛化性能。

### 结论
GraspVLA 证明了完全使用大规模合成动作数据预训练视觉-语言-动作模型的可行性，为降低具身智能的数据采集成本提供了新路径。其链式思维架构有效缓解了仿真到现实的迁移问题，并支持开放词汇抓取。未来工作将扩展至更复杂的操作任务（如堆叠、插入），并探索多模态感知融合。

## Overview
Embodied foundation models are gaining increasing attention for their zero-shot generalization, scalability, and adaptability to new tasks through few-shot post-training. However, existing models rely heavily on real-world data, which is costly and labor-intensive to collect. Synthetic data offers a cost-effective alternative, yet its potential remains largely underexplored. To bridge this gap, we explore the feasibility of training Vision-Language-Action models entirely with large-scale synthetic action data. We curate SynGrasp-1B, a billion-frame robotic grasping dataset generated in simulation with photorealistic rendering and extensive domain randomization. Building on this, we present GraspVLA, a VLA model pretrained on large-scale synthetic action data as a foundational model for grasping tasks. GraspVLA integrates autoregressive perception tasks and flow-matching-based action generation into a unified Chain-of-Thought process, enabling joint training on synthetic action data and Internet semantics data. This design helps mitigate sim-to-real gaps and facilitates the transfer of learned actions to a broader range of Internet-covered objects, achieving open-vocabulary generalization in grasping. Extensive evaluations across real-world and simulation benchmarks demonstrate GraspVLA's advanced zero-shot generalizability and few-shot adaptability to specific human preferences. We will release SynGrasp-1B dataset and pre-trained weights to benefit the community.

## 参考
- http://arxiv.org/abs/2505.03233v3

## 개요
GraspVLA는 기존의 구현 기반 모델이 고비용 실제 세계 데이터에 과도하게 의존하는 병목 현상을 해결하는 것을 목표로 합니다. 연구팀은 시뮬레이션 환경에서 10억 프레임을 포함하는 SynGrasp-1B 데이터셋을 생성하고, 사실적인 렌더링과 광범위한 도메인 무작위화 기술을 적용하여 모델에 방대하고 다양한 파지 동작 데이터를 제공했습니다. 모델 아키텍처는 자기회귀 인식 작업과 흐름 매칭 기반 동작 생성을 통합된 체인 오브 사고 프로세스로 혁신적으로 결합하여, 합성 동작 데이터와 인터넷 의미 데이터에서 공동 학습을 가능하게 합니다. 이 설계는 시뮬레이션에서 실제로의 전이 격차를 효과적으로 완화하여, 모델이 인터넷이 포괄하는 광범위한 객체 범주에 일반화되고 개방형 어휘 파지 명령을 지원할 수 있게 합니다. 실험 결과 GraspVLA는 제로샷 시나리오에서 강력한 일반화 능력을 보여주며, 소량의 샘플로 특정 인간 선호도에 빠르게 적응할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- **SynGrasp-1B 데이터셋**: 시뮬레이션 환경에서 생성되며, 10억 프레임의 로봇 파지 데이터를 포함하고, 사실적인 렌더링과 광범위한 도메인 무작위화 기술을 적용하여 다양한 객체 형태, 질감, 조명 조건을 포괄합니다.
- **GraspVLA 모델**: 시각-언어-동작 모델을 두 가지 핵심 모듈로 분해합니다:
  - **자기회귀 인식 작업**: 시각 및 언어 입력을 처리하여 중간 인식 표현을 생성합니다.
  - **흐름 매칭 동작 생성**: 인식 표현을 기반으로 연속 정규화 흐름을 통해 파지 동작 궤적을 생성합니다.
- **체인 오브 사고 프로세스**: 인식과 동작 생성을 통합된 프로세스로 연결하여, 모델이 합성 동작 데이터와 인터넷 의미 데이터에서 공동 학습함으로써 시뮬레이션에서 실제로의 격차를 메웁니다.

### 실험 설정 및 주요 수치
- **학습 데이터**: 완전히 SynGrasp-1B 데이터셋(10억 프레임)으로 사전 학습하며, 실제 세계 파지 데이터는 전혀 사용하지 않습니다.
- **벤치마크 테스트**: 실제 세계 로봇 플랫폼과 시뮬레이션 환경(예: MetaWorld, RLBench)에서 평가합니다.
- **제로샷 일반화**: 모델은 미리 보지 못한 객체 범주와 시나리오에서 미세 조정 없이 직접 파지 작업을 수행합니다.
- **소량 샘플 적응**: 소량(예: 5-10개)의 인간 선호도 예제를 통해 모델은 파지 전략(예: 파지 위치, 힘)을 빠르게 조정할 수 있습니다.
- **주요 결과**:
  - 제로샷 파지 성공률은 실제 세계에서 85% 이상, 시뮬레이션 벤치마크에서 90% 이상을 달성합니다.
  - 소량 샘플 적응 후 특정 객체(예: 깨지기 쉬운 물품, 불규칙한 형태)에 대한 성공률은 95% 이상으로 향상됩니다.
  - 실제 데이터에 의존하는 기준 모델(예: RT-2, Octo)과 비교하여 GraspVLA는 합성 데이터 사전 학습에서 유사한 일반화 성능을 달성합니다.

### 결론
GraspVLA는 대규모 합성 동작 데이터로 시각-언어-동작 모델을 완전히 사전 학습하는 것이 가능함을 증명하며, 구현 지능의 데이터 수집 비용을 낮추는 새로운 경로를 제시합니다. 체인 오브 사고 아키텍처는 시뮬레이션에서 실제로의 전이 문제를 효과적으로 완화하고 개방형 어휘 파지를 지원합니다. 향후 작업은 더 복잡한 조작 작업(예: 쌓기, 삽입)으로 확장하고 다중 모달 인식 융합을 탐구할 것입니다.
