---
$id: ent_paper_example_based_motion_synthesis_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Example-based Motion Synthesis via Generative Motion Matching
  zh: Example-based Motion Synthesis via Generative Motion Matching
  ko: Example-based Motion Synthesis via Generative Motion Matching
summary:
  en: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  zh: GenMM 是一个基于生成式运动匹配的模型，由研究团队于2023年提出，用于人形机器人的运动分析与合成。其核心贡献在于无需训练即可从少量示例序列中挖掘多样运动，并在复杂骨骼结构上实现亚秒级高质量合成，同时支持运动补全、关键帧引导生成等扩展功能。
  ko: Example-based Motion Synthesis via Generative Motion Matching is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- example_based_motion_synthesis
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.00378v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Example-based Motion Synthesis via Generative Motion Matching (arXiv)
  url: https://arxiv.org/abs/2306.00378
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
GenMM 继承了 Motion Matching 方法无需训练且质量优越的特性，解决了现有数据驱动方法训练时间长、易出现视觉伪影、难以处理大型复杂骨骼的问题。该模型通过生成式运动匹配模块，利用双向视觉相似性作为生成成本函数，在多阶段框架中逐步优化随机初始猜测，从而高效合成高质量运动。除了多样运动生成，GenMM 还展示了在运动补全、关键帧引导生成、无限循环和运动重组等场景中的通用性，这些是传统 Motion Matching 无法实现的。

## 核心内容
### 方法架构
- **核心模块**：生成式运动匹配模块，使用双向视觉相似性作为生成成本函数，替代传统 Motion Matching 的匹配准则。
- **多阶段框架**：从随机初始猜测开始，通过多阶段迭代逐步优化，每个阶段利用示例运动匹配来细化结果。
- **无需训练**：继承 Motion Matching 的无需训练特性，避免长时间离线训练。

### 实验设置与关键数字
- **性能**：在高度复杂和大型骨骼结构上，GenMM 能在亚秒级（fraction of a second）内合成高质量运动。
- **对比优势**：相比现有数据驱动方法，GenMM 无需训练、无视觉伪影，且能处理大型复杂骨骼。
- **扩展场景**：支持运动补全、关键帧引导生成、无限循环和运动重组，这些是传统 Motion Matching 无法实现的。

### 结论
GenMM 通过生成式运动匹配实现了高效、高质量的运动合成，尤其适用于复杂骨骼结构，并展示了在多种运动相关任务中的通用性。代码和数据已开源。

## Overview
We present GenMM, a generative model that "mines" as many diverse motions as possible from a single or few example sequences. In stark contrast to existing data-driven methods, which typically require long offline training time, are prone to visual artifacts, and tend to fail on large and complex skeletons, GenMM inherits the training-free nature and the superior quality of the well-known Motion Matching method. GenMM can synthesize a high-quality motion within a fraction of a second, even with highly complex and large skeletal structures. At the heart of our generative framework lies the generative motion matching module, which utilizes the bidirectional visual similarity as a generative cost function to motion matching, and operates in a multi-stage framework to progressively refine a random guess using exemplar motion matches. In addition to diverse motion generation, we show the versatility of our generative framework by extending it to a number of scenarios that are not possible with motion matching alone, including motion completion, key frame-guided generation, infinite looping, and motion reassembly. Code and data for this paper are at https://wyysf-98.github.io/GenMM/

## 개요
우리는 GenMM을 제시합니다. 이는 하나 또는 소수의 예제 시퀀스에서 가능한 한 다양한 모션을 "채굴"하는 생성 모델입니다. 일반적으로 긴 오프라인 학습 시간이 필요하고, 시각적 아티팩트가 발생하기 쉬우며, 크고 복잡한 골격에서 실패하는 경향이 있는 기존의 데이터 기반 방법들과는 대조적으로, GenMM은 잘 알려진 Motion Matching 방법의 학습 불필요성과 우수한 품질을 계승합니다. GenMM은 매우 복잡하고 큰 골격 구조에서도 1초 미만의 시간 내에 고품질 모션을 합성할 수 있습니다. 우리 생성 프레임워크의 핵심에는 생성적 모션 매칭 모듈이 있으며, 이는 양방향 시각적 유사성을 모션 매칭의 생성 비용 함수로 활용하고, 다단계 프레임워크에서 작동하여 예제 모션 매칭을 사용해 무작위 추측을 점진적으로 개선합니다. 다양한 모션 생성 외에도, 우리는 모션 완성, 키 프레임 기반 생성, 무한 루핑, 모션 재조립 등 모션 매칭만으로는 불가능한 여러 시나리오로 생성 프레임워크를 확장하여 그 다재다능함을 보여줍니다. 이 논문의 코드와 데이터는 https://wyysf-98.github.io/GenMM/ 에 있습니다.

## 핵심 내용
우리는 GenMM을 제시합니다. 이는 하나 또는 소수의 예제 시퀀스에서 가능한 한 다양한 모션을 "채굴"하는 생성 모델입니다. 일반적으로 긴 오프라인 학습 시간이 필요하고, 시각적 아티팩트가 발생하기 쉬우며, 크고 복잡한 골격에서 실패하는 경향이 있는 기존의 데이터 기반 방법들과는 대조적으로, GenMM은 잘 알려진 Motion Matching 방법의 학습 불필요성과 우수한 품질을 계승합니다. GenMM은 매우 복잡하고 큰 골격 구조에서도 1초 미만의 시간 내에 고품질 모션을 합성할 수 있습니다. 우리 생성 프레임워크의 핵심에는 생성적 모션 매칭 모듈이 있으며, 이는 양방향 시각적 유사성을 모션 매칭의 생성 비용 함수로 활용하고, 다단계 프레임워크에서 작동하여 예제 모션 매칭을 사용해 무작위 추측을 점진적으로 개선합니다. 다양한 모션 생성 외에도, 우리는 모션 완성, 키 프레임 기반 생성, 무한 루핑, 모션 재조립 등 모션 매칭만으로는 불가능한 여러 시나리오로 생성 프레임워크를 확장하여 그 다재다능함을 보여줍니다. 이 논문의 코드와 데이터는 https://wyysf-98.github.io/GenMM/ 에 있습니다.

## 参考
- http://arxiv.org/abs/2306.00378v1
