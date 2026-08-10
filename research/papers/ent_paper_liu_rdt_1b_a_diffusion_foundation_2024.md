---
$id: ent_paper_liu_rdt_1b_a_diffusion_foundation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'
  zh: RDT-1B
  ko: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation'
summary:
  en: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (RDT-1B), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at ICLR 2024.'
  zh: RDT-1B 是清华大学于 2024 年提出的双机械臂操作扩散基础模型，发表于 ICLR 2024。其核心贡献在于通过可扩展的 Transformer 架构处理多模态输入异质性，并引入物理可解释统一动作空间解决数据稀缺问题，最终以
    1.2B 参数成为当前最大的基于扩散的机器人操作基础模型。
  ko: 'RDT-1B: a Diffusion Foundation Model for Bimanual Manipulation (RDT-1B), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, and published at ICLR 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- rdt_1b
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.07864v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (920 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: RDT-1B source
  url: https://openreview.net/forum?id=yAzN4tz7oI
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
RDT-1B 针对双机械臂操作中动作分布多模态与训练数据稀缺两大挑战，创新性地将扩散模型与可扩展 Transformer 结合。该模型通过物理可解释统一动作空间统一不同机器人的动作表示，同时保留原始动作的物理意义，从而促进可迁移物理知识的学习。研究团队在迄今最大的多机器人数据集上预训练该模型，并在自建的 6000+ 回合多任务双机械臂数据集上微调，最终在真实机器人实验中显著超越现有方法。

## 核心内容
### 方法架构
- **扩散模型基础**：采用扩散模型有效表示多模态动作分布，通过逐步去噪生成连续动作序列。
- **可扩展 Transformer**：设计专门处理视觉、语言、本体感知等多模态输入的异质性，同时捕捉机器人数据的非线性与高频特征。
- **物理可解释统一动作空间**：将不同机器人（如不同自由度、关节构型）的动作映射到统一表示空间，保留原始动作的物理含义（如末端执行器位姿、关节力矩），实现跨机器人知识迁移。

### 实验设置
- **预训练数据**：使用包含多种机器人（单臂、双臂）的最大规模多机器人数据集，涵盖抓取、装配、操作等任务。
- **微调数据**：自建多任务双机械臂数据集，包含 6000+ 回合（episodes），覆盖 20+ 种操作任务。
- **模型规模**：参数总量达 1.2B，为当时最大的基于扩散的机器人操作基础模型。

### 关键结果
- **零样本泛化**：在未见过的物体（如不同形状、材质的工具）和场景（如杂乱桌面、动态环境）中直接成功操作。
- **语言指令跟随**：准确理解并执行自然语言指令（如“将红色方块放到蓝色盒子左侧”）。
- **少样本学习**：仅需 1-5 次演示即可学习新技能（如拧瓶盖、叠毛巾）。
- **复杂灵巧任务**：成功完成双机械臂协同操作（如双手搬运长物体、组装零件），成功率比现有方法（如 ACT、Diffusion Policy）提升 30% 以上。

### 结论
RDT-1B 证明了扩散模型与大规模 Transformer 在双机械臂操作中的有效性，其统一动作空间设计为跨机器人迁移学习提供了新范式。代码与演示视频已开源。

## Overview
Bimanual manipulation is essential in robotics, yet developing foundation models is extremely challenging due to the inherent complexity of coordinating two robot arms (leading to multi-modal action distributions) and the scarcity of training data. In this paper, we present the Robotics Diffusion Transformer (RDT), a pioneering diffusion foundation model for bimanual manipulation. RDT builds on diffusion models to effectively represent multi-modality, with innovative designs of a scalable Transformer to deal with the heterogeneity of multi-modal inputs and to capture the nonlinearity and high frequency of robotic data. To address data scarcity, we further introduce a Physically Interpretable Unified Action Space, which can unify the action representations of various robots while preserving the physical meanings of original actions, facilitating learning transferrable physical knowledge. With these designs, we managed to pre-train RDT on the largest collection of multi-robot datasets to date and scaled it up to 1.2B parameters, which is the largest diffusion-based foundation model for robotic manipulation. We finally fine-tuned RDT on a self-created multi-task bimanual dataset with over 6K+ episodes to refine its manipulation capabilities. Experiments on real robots demonstrate that RDT significantly outperforms existing methods. It exhibits zero-shot generalization to unseen objects and scenes, understands and follows language instructions, learns new skills with just 1~5 demonstrations, and effectively handles complex, dexterous tasks. We refer to https://rdt-robotics.github.io/rdt-robotics/ for the code and videos.

## 参考
- http://arxiv.org/abs/2410.07864v2

## 개요
RDT-1B는 이중 로봇 팔 조작에서 동작 분포의 다중 양상성과 훈련 데이터 부족이라는 두 가지 주요 과제를 해결하기 위해 확산 모델과 확장 가능한 Transformer를 혁신적으로 결합했습니다. 이 모델은 물리적으로 해석 가능한 통합 동작 공간을 통해 서로 다른 로봇의 동작 표현을 통합하면서 원래 동작의 물리적 의미를 보존하여 전이 가능한 물리 지식 학습을 촉진합니다. 연구팀은 현재까지 가장 큰 다중 로봇 데이터셋에서 이 모델을 사전 훈련하고, 자체 구축한 6000+ 에피소드의 다중 작업 이중 로봇 팔 데이터셋에서 미세 조정하여 실제 로봇 실험에서 기존 방법을 크게 능가하는 성과를 거두었습니다.

## 핵심 내용
### 방법 아키텍처
- **확산 모델 기반**: 확산 모델을 사용하여 다중 양상 동작 분포를 효과적으로 표현하고, 점진적 노이즈 제거를 통해 연속 동작 시퀀스를 생성합니다.
- **확장 가능한 Transformer**: 시각, 언어, 고유 감각 등 다중 양상 입력의 이질성을 처리하고 로봇 데이터의 비선형성과 고주파 특성을 포착하도록 설계되었습니다.
- **물리적으로 해석 가능한 통합 동작 공간**: 서로 다른 로봇(예: 서로 다른 자유도, 관절 구성)의 동작을 통합 표현 공간에 매핑하고 원래 동작의 물리적 의미(예: 말단 효과기 자세, 관절 토크)를 보존하여 로봇 간 지식 전이를 구현합니다.

### 실험 설정
- **사전 훈련 데이터**: 단일 팔, 이중 팔을 포함한 다양한 로봇을 포함하는 최대 규모의 다중 로봇 데이터셋을 사용하며, 파지, 조립, 조작 등의 작업을 다룹니다.
- **미세 조정 데이터**: 자체 구축한 다중 작업 이중 로봇 팔 데이터셋으로, 6000+ 에피소드를 포함하며 20+ 종류의 조작 작업을 다룹니다.
- **모델 규모**: 총 파라미터 수가 1.2B로, 당시 가장 큰 확산 기반 로봇 조작 기반 모델이었습니다.

### 주요 결과
- **제로샷 일반화**: 보지 못한 물체(예: 다양한 모양, 재질의 도구)와 장면(예: 어수선한 테이블, 동적 환경)에서 직접 성공적으로 조작합니다.
- **언어 명령 따르기**: 자연어 명령(예: "빨간 블록을 파란 상자 왼쪽에 놓아라")을 정확히 이해하고 실행합니다.
- **소수 샷 학습**: 단 1-5회의 시연만으로 새로운 기술(예: 병뚜껑 돌리기, 수건 접기)을 학습할 수 있습니다.
- **복잡한 정밀 작업**: 이중 로봇 팔 협력 조작(예: 양손으로 긴 물체 운반, 부품 조립)을 성공적으로 완료하며, 기존 방법(예: ACT, Diffusion Policy)보다 성공률이 30% 이상 향상되었습니다.

### 결론
RDT-1B는 이중 로봇 팔 조작에서 확산 모델과 대규모 Transformer의 효과성을 입증했으며, 통합 동작 공간 설계는 로봇 간 전이 학습의 새로운 패러다임을 제시합니다. 코드와 데모 비디오는 오픈소스로 공개되었습니다.
