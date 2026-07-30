---
$id: ent_paper_scaling_large_motion_models_wi_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scaling Large Motion Models with Million-Level Human Motions
  zh: Scaling Large Motion Models with Million-Level Human Motions
  ko: Scaling Large Motion Models with Million-Level Human Motions
summary:
  en: Scaling Large Motion Models with Million-Level Human Motions is a 2024 work on human motion analysis and synthesis for
    humanoid robots.
  zh: MotionLib 是首个百万级人类运动数据集，规模至少是现有数据集的 15 倍，并配有分层文本描述。基于此数据集训练的 Being-M0 大运动模型在多种人类活动（包括未见过的活动）上展现出稳健性能。该工作首次系统揭示了数据与模型规模缩放对运动生成的重要性，并提出了
    Motionbook 运动编码方法以增强运动模态的表示能力。
  ko: Scaling Large Motion Models with Million-Level Human Motions is a 2024 work on human motion analysis and synthesis for
    humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- scaling_large_motion_models_wi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.03311v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Scaling Large Motion Models with Million-Level Human Motions (arXiv)
  url: https://arxiv.org/abs/2410.03311
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
受大语言模型成功启发，人类运动理解领域正转向开发大运动模型，但高质量数据匮乏是主要瓶颈。为此，研究者构建了 MotionLib 数据集，其规模远超现有同类数据集，并采用分层文本描述增强语义丰富度。基于该数据集训练的 Being-M0 模型在广泛的人类活动上表现优异，包括未见过的活动。通过系统研究，该工作首次强调了数据与模型规模缩放对运动生成的关键作用，并提出了 Motionbook 运动编码方法，包含紧凑无损的运动特征表示和新型 2D 无查找运动分词器，在扩展码本容量的同时保留细粒度运动细节。

## 核心内容
### 核心贡献
- **MotionLib 数据集**：首个百万级运动生成数据集，规模至少是现有数据集的 15 倍，并配有分层文本描述。
- **Being-M0 模型**：基于 MotionLib 训练的大运动模型，在广泛人类活动（包括未见过的活动）上展现稳健性能。
- **规模缩放研究**：首次系统揭示数据与模型规模缩放对运动生成的重要性，并提供关键见解。
- **Motionbook 运动编码**：包含两个创新组件：
  - 紧凑无损的运动特征表示
  - 新型 2D 无查找运动分词器，在扩展码本容量的同时保留细粒度运动细节，显著增强运动令牌的表示能力。

### 实验设置与关键数字
- 数据集规模：MotionLib 包含百万级运动序列，是现有数据集的 15 倍以上。
- 模型性能：Being-M0 在多种人类活动上表现稳健，包括未见过的活动。
- 运动编码：Motionbook 的 2D 无查找运动分词器在保留细粒度运动细节的同时扩展了码本容量。

### 结论
该工作为开发更通用、更强大的运动生成模型奠定了基础。更多细节请访问 https://beingbeyond.github.io/Being-M0/。

## Overview
Inspired by the recent success of LLMs, the field of human motion understanding has increasingly shifted toward developing large motion models. Despite some progress, current efforts remain far from achieving truly generalist models, primarily due to the lack of massive high-quality data. To address this gap, we present MotionLib, the first million-level dataset for motion generation, which is at least 15$\times$ larger than existing counterparts and enriched with hierarchical text descriptions. Using MotionLib, we train a large motion model named \projname, demonstrating robust performance across a wide range of human activities, including unseen ones. Through systematic investigation, for the first time, we highlight the importance of scaling both data and model size for advancing motion generation, along with key insights to achieve this goal. To better integrate the motion modality, we propose Motionbook, an innovative motion encoding approach including (1) a compact yet lossless feature to represent motions; (2) a novel 2D lookup-free motion tokenizer that preserves fine-grained motion details while expanding codebook capacity, significantly enhancing the representational power of motion tokens. We believe this work lays the groundwork for developing more versatile and powerful motion generation models in the future. For further details, visit https://beingbeyond.github.io/Being-M0/.

## 개요
최근 LLM의 성공에 영감을 받아, 인간 동작 이해 분야는 점차 대규모 동작 모델 개발로 방향을 전환하고 있습니다. 일부 진전이 있었지만, 현재의 노력은 주로 대규모 고품질 데이터의 부족으로 인해 진정한 범용 모델을 달성하는 데는 아직 멀었습니다. 이러한 격차를 해소하기 위해, 우리는 MotionLib을 제시합니다. 이는 동작 생성을 위한 최초의 백만 단위 데이터셋으로, 기존 데이터셋보다 최소 15배 이상 크며 계층적 텍스트 설명으로 풍부하게 구성되어 있습니다. MotionLib을 사용하여 \projname이라는 대규모 동작 모델을 훈련시켰으며, 보지 못한 활동을 포함한 다양한 인간 활동에서 강력한 성능을 입증했습니다. 체계적인 조사를 통해, 우리는 처음으로 동작 생성 발전을 위한 데이터와 모델 크기 확장의 중요성과 이를 달성하기 위한 핵심 통찰력을 강조합니다. 동작 모달리티를 더 잘 통합하기 위해, 우리는 Motionbook을 제안합니다. 이는 혁신적인 동작 인코딩 접근 방식으로, (1) 동작을 표현하는 간결하면서도 무손실 특징, (2) 미세한 동작 세부 정보를 보존하면서 코드북 용량을 확장하고 동작 토큰의 표현력을 크게 향상시키는 새로운 2D 조회 없는 동작 토크나이저를 포함합니다. 우리는 이 작업이 미래에 더 다재다능하고 강력한 동작 생성 모델을 개발하기 위한 기초를 마련한다고 믿습니다. 자세한 내용은 https://beingbeyond.github.io/Being-M0/를 방문하십시오.

## 핵심 내용
최근 LLM의 성공에 영감을 받아, 인간 동작 이해 분야는 점차 대규모 동작 모델 개발로 방향을 전환하고 있습니다. 일부 진전이 있었지만, 현재의 노력은 주로 대규모 고품질 데이터의 부족으로 인해 진정한 범용 모델을 달성하는 데는 아직 멀었습니다. 이러한 격차를 해소하기 위해, 우리는 MotionLib을 제시합니다. 이는 동작 생성을 위한 최초의 백만 단위 데이터셋으로, 기존 데이터셋보다 최소 15배 이상 크며 계층적 텍스트 설명으로 풍부하게 구성되어 있습니다. MotionLib을 사용하여 \projname이라는 대규모 동작 모델을 훈련시켰으며, 보지 못한 활동을 포함한 다양한 인간 활동에서 강력한 성능을 입증했습니다. 체계적인 조사를 통해, 우리는 처음으로 동작 생성 발전을 위한 데이터와 모델 크기 확장의 중요성과 이를 달성하기 위한 핵심 통찰력을 강조합니다. 동작 모달리티를 더 잘 통합하기 위해, 우리는 Motionbook을 제안합니다. 이는 혁신적인 동작 인코딩 접근 방식으로, (1) 동작을 표현하는 간결하면서도 무손실 특징, (2) 미세한 동작 세부 정보를 보존하면서 코드북 용량을 확장하고 동작 토큰의 표현력을 크게 향상시키는 새로운 2D 조회 없는 동작 토크나이저를 포함합니다. 우리는 이 작업이 미래에 더 다재다능하고 강력한 동작 생성 모델을 개발하기 위한 기초를 마련한다고 믿습니다. 자세한 내용은 https://beingbeyond.github.io/Being-M0/를 방문하십시오.

## 参考
- http://arxiv.org/abs/2410.03311v3
