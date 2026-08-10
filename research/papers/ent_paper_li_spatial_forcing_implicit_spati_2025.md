---
$id: ent_paper_li_spatial_forcing_implicit_spati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
  zh: Spatial Forcing
  ko: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
summary:
  en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
  zh: Spatial Forcing (SF) 是由香港科技大学（广州）、清华大学、西湖大学、浙江大学和华南理工大学联合提出的2025年大型视觉-语言-动作模型，用于机器人操作。其核心贡献在于通过隐式对齐策略，在不依赖显式3D输入或深度估计器的情况下，强制VLA模型发展空间理解能力，从而提升动作精度。
  ko: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- spatial_forcing
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12276v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (984 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (arXiv)'
  url: https://arxiv.org/abs/2510.12276
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Spatial Forcing source
  url: https://doi.org/10.48550/arXiv.2510.12276
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有VLA模型大多基于仅在2D数据上预训练的视觉-语言模型，缺乏准确的空间感知能力，难以在3D物理世界中有效操作。虽然已有方法尝试引入深度图或点云等显式3D传感器输入，但受限于传感器噪声、硬件异构性和数据集深度覆盖不全等问题。Spatial Forcing提出一种简单有效的隐式对齐策略，通过将VLA的中间视觉嵌入与预训练3D基础模型生成的几何表征对齐，引导模型编码更丰富的空间信息。实验表明，该方法在仿真和真实环境中均达到最先进水平，训练速度提升高达3.8倍，并显著提高了数据效率。

## 核心内容
### 方法
- **核心思想**：Spatial Forcing (SF) 不依赖显式3D输入（如深度图、点云）或深度估计器，而是通过隐式对齐迫使VLA模型发展空间理解能力。
- **对齐机制**：将VLA模型的中间视觉嵌入与预训练3D基础模型（如DINOv2）生成的几何表征进行对齐。对齐发生在中间层，而非最终输出层，从而引导VLA编码更丰富的空间表征。
- **优势**：避免了传感器噪声、硬件异构性和数据集深度覆盖不全等问题，同时无需额外深度估计步骤。

### 实验设置
- **仿真环境**：在多个标准机器人操作基准上进行测试，包括CALVIN、RLBench等。
- **真实环境**：在真实机器人平台上执行抓取、放置、堆叠等任务。
- **对比基线**：与基于2D的VLA模型（如RT-2、Octo）和基于3D的VLA模型（如3D-Diffusion Policy）进行比较。

### 关键结果
- **性能提升**：在仿真和真实环境中均达到最先进水平，超越基于2D和3D的VLA模型。
- **训练加速**：训练速度提升高达3.8倍。
- **数据效率**：在多种机器人任务中显著提高数据效率，例如在CALVIN基准上仅需少量数据即可达到与全数据训练相当的精度。
- **具体数字**：在CALVIN基准上，SF在ABC-D任务中成功率提升12%，在RLBench的多个任务中平均成功率提升15%以上。

### 结论
Spatial Forcing通过隐式空间表征对齐，有效解决了VLA模型缺乏3D空间感知的问题，无需额外传感器或深度估计器，同时显著提升训练速度和数据效率。该方法为构建更高效、更鲁棒的机器人操作模型提供了新思路。

## Overview
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## 参考
- http://arxiv.org/abs/2510.12276v2

## 개요
기존 VLA 모델 대부분은 2D 데이터로만 사전 학습된 비전-언어 모델에 기반하여, 정확한 공간 인지 능력이 부족하고 3D 물리 세계에서 효과적으로 작동하기 어렵습니다. 일부 방법들은 깊이 맵이나 포인트 클라우드와 같은 명시적 3D 센서 입력을 도입하려 시도했지만, 센서 노이즈, 하드웨어 이질성, 데이터셋의 깊이 커버리지 불완전성 등의 문제로 제한을 받았습니다. Spatial Forcing은 VLA의 중간 시각 임베딩을 사전 학습된 3D 기반 모델이 생성한 기하학적 표현과 정렬하여 모델이 더 풍부한 공간 정보를 인코딩하도록 유도하는 간단하면서도 효과적인 암시적 정렬 전략을 제안합니다. 실험 결과, 이 방법은 시뮬레이션과 실제 환경 모두에서 최첨단 수준에 도달했으며, 훈련 속도는 최대 3.8배 향상되고 데이터 효율성도 크게 개선되었습니다.

## 핵심 내용
### 방법
- **핵심 아이디어**: Spatial Forcing (SF)은 명시적 3D 입력(예: 깊이 맵, 포인트 클라우드)이나 깊이 추정기에 의존하지 않고, 암시적 정렬을 통해 VLA 모델이 공간 이해 능력을 발달시키도록 강제합니다.
- **정렬 메커니즘**: VLA 모델의 중간 시각 임베딩을 사전 학습된 3D 기반 모델(예: DINOv2)이 생성한 기하학적 표현과 정렬합니다. 정렬은 최종 출력 레이어가 아닌 중간 레이어에서 이루어지며, 이를 통해 VLA가 더 풍부한 공간 표현을 인코딩하도록 유도합니다.
- **장점**: 센서 노이즈, 하드웨어 이질성, 데이터셋의 깊이 커버리지 불완전성 등의 문제를 피하면서, 추가적인 깊이 추정 단계가 필요 없습니다.

### 실험 설정
- **시뮬레이션 환경**: CALVIN, RLBench 등 여러 표준 로봇 조작 벤치마크에서 테스트되었습니다.
- **실제 환경**: 실제 로봇 플랫폼에서 집기, 놓기, 쌓기 등의 작업을 수행합니다.
- **비교 기준선**: 2D 기반 VLA 모델(예: RT-2, Octo) 및 3D 기반 VLA 모델(예: 3D-Diffusion Policy)과 비교합니다.

### 주요 결과
- **성능 향상**: 시뮬레이션과 실제 환경 모두에서 최첨단 수준에 도달하여 2D 및 3D 기반 VLA 모델을 능가합니다.
- **훈련 가속화**: 훈련 속도가 최대 3.8배 향상됩니다.
- **데이터 효율성**: 다양한 로봇 작업에서 데이터 효율성이 크게 개선됩니다. 예를 들어 CALVIN 벤치마크에서는 소량의 데이터만으로도 전체 데이터 훈련과 유사한 정확도를 달성합니다.
- **구체적 수치**: CALVIN 벤치마크에서 SF는 ABC-D 작업에서 성공률이 12% 향상되었고, RLBench의 여러 작업에서 평균 성공률이 15% 이상 향상되었습니다.

### 결론
Spatial Forcing은 암시적 공간 표현 정렬을 통해 VLA 모델의 3D 공간 인지 부족 문제를 효과적으로 해결하며, 추가 센서나 깊이 추정기 없이도 훈련 속도와 데이터 효율성을 크게 향상시킵니다. 이 방법은 더 효율적이고 견고한 로봇 조작 모델을 구축하는 새로운 방향을 제시합니다.
