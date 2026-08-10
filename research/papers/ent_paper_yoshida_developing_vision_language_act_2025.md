---
$id: ent_paper_yoshida_developing_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing Vision-Language-Action Model from Egocentric Videos
  zh: Developing Vision-Language-Action Model from Egocentric Videos
  ko: Developing Vision-Language-Action Model from Egocentric Videos
summary:
  en: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
  zh: 本文由Institute of Science Tokyo、NII LLMC与Sony Interactive Entertainment联合提出，介绍了一种从第一人称视频中训练视觉-语言-动作模型（VLA）的方法。核心贡献在于提出EgoScaler框架，无需辅助标注即可从原始第一人称视频中提取6DoF物体操作轨迹，并构建大规模预训练数据集。实验表明，该预训练方法在模拟与真实机器人环境中将任务成功率提升超过20%，性能可与真实机器人数据集媲美。
  ko: Developing Vision-Language-Action Model from Egocentric Videos (Developing Vision-Language-Action Model from Egocentric
    Videos), is a 2025 large vision-language-action model for robotic manipulation, introduced by Institute of Science Tokyo,
    NII LLMC, Sony Interactive Entertainment.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- developing_vision_language_act
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21986v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (704 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Developing Vision-Language-Action Model from Egocentric Videos (arXiv)
  url: https://arxiv.org/abs/2509.21986
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Developing Vision-Language-Action Model from Egocentric Videos source
  url: https://doi.org/10.48550/arXiv.2509.21986
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
第一人称视频记录了人类操作物体与工具的过程，提供了丰富的运动线索，但以往研究依赖手部姿态等辅助标注。本文提出的EgoScaler框架可直接从原始第一人称视频中提取六自由度物体操作轨迹，无需额外记录。研究团队将EgoScaler应用于四个大规模第一人称视频数据集，自动修正噪声与不完整轨迹，构建了新的VLA预训练数据集。基于$π_0$架构的实验显示，该预训练方法在模拟与真实机器人环境中均显著提升任务成功率，且与真实机器人数据集结合使用效果更佳。

## 核心内容
### 方法
- **EgoScaler框架**：从原始第一人称视频中提取6DoF物体操作轨迹，无需手部姿态等辅助标注。
- **数据集构建**：应用于四个大规模第一人称视频数据集（具体名称未在正文中列出），自动修正噪声与不完整轨迹，形成VLA预训练数据集。

### 实验设置
- **基础模型**：采用$π_0$架构，该架构为当前最先进的VLA模型之一。
- **评估环境**：同时包含模拟环境与真实机器人环境。
- **对比条件**：训练从零开始（scratch）、仅使用本文数据集预训练、仅使用真实机器人数据集预训练、两者结合预训练。

### 关键结果
- **成功率提升**：预训练后任务成功率相比从零开始训练提升超过20%。
- **性能对比**：本文数据集预训练的性能与使用真实机器人数据集预训练相当。
- **协同效应**：将本文数据集与真实机器人数据结合使用，可进一步改善性能。

### 结论
第一人称视频是推动VLA研究的有前景且可扩展的资源，EgoScaler框架有效解决了从原始视频中提取操作轨迹的难题。

## Overview
Egocentric videos capture how humans manipulate objects and tools, providing diverse motion cues for learning object manipulation. Unlike the costly, expert-driven manual teleoperation commonly used in training Vision-Language-Action models (VLAs), egocentric videos offer a scalable alternative. However, prior studies that leverage such videos for training robot policies typically rely on auxiliary annotations, such as detailed hand-pose recordings. Consequently, it remains unclear whether VLAs can be trained directly from raw egocentric videos. In this work, we address this challenge by leveraging EgoScaler, a framework that extracts 6DoF object manipulation trajectories from egocentric videos without requiring auxiliary recordings. We apply EgoScaler to four large-scale egocentric video datasets and automatically refine noisy or incomplete trajectories, thereby constructing a new large-scale dataset for VLA pre-training. Our experiments with a state-of-the-art $π_0$ architecture in both simulated and real-robot environments yield three key findings: (i) pre-training on our dataset improves task success rates by over 20\% compared to training from scratch, (ii) the performance is competitive with that achieved using real-robot datasets, and (iii) combining our dataset with real-robot data yields further improvements. These results demonstrate that egocentric videos constitute a promising and scalable resource for advancing VLA research.

## 参考
- http://arxiv.org/abs/2509.21986v1

## 개요
1인칭 비디오는 인간이 물체와 도구를 조작하는 과정을 기록하며 풍부한 운동 단서를 제공하지만, 기존 연구는 손 자세와 같은 보조 주석에 의존해 왔습니다. 본 논문에서 제안하는 EgoScaler 프레임워크는 추가 기록 없이 원시 1인칭 비디오에서 직접 6자유도 물체 조작 궤적을 추출할 수 있습니다. 연구팀은 EgoScaler를 네 개의 대규모 1인칭 비디오 데이터셋에 적용하여 노이즈와 불완전한 궤적을 자동으로 수정하고, 새로운 VLA 사전 학습 데이터셋을 구축했습니다. $π_0$ 아키텍처를 기반으로 한 실험에서 이 사전 학습 방법은 시뮬레이션 및 실제 로봇 환경 모두에서 작업 성공률을 크게 향상시켰으며, 실제 로봇 데이터셋과 결합할 때 더욱 효과적임을 보여주었습니다.

## 핵심 내용
### 방법
- **EgoScaler 프레임워크**: 손 자세와 같은 보조 주석 없이 원시 1인칭 비디오에서 6DoF 물체 조작 궤적을 추출합니다.
- **데이터셋 구축**: 네 개의 대규모 1인칭 비디오 데이터셋(구체적인 이름은 본문에 나열되지 않음)에 적용하여 노이즈와 불완전한 궤적을 자동으로 수정하고, VLA 사전 학습 데이터셋을 형성합니다.

### 실험 설정
- **기본 모델**: 현재 최첨단 VLA 모델 중 하나인 $π_0$ 아키텍처를 채택합니다.
- **평가 환경**: 시뮬레이션 환경과 실제 로봇 환경을 모두 포함합니다.
- **비교 조건**: 처음부터 학습(scratch), 본 논문의 데이터셋만 사전 학습, 실제 로봇 데이터셋만 사전 학습, 두 가지를 결합한 사전 학습.

### 주요 결과
- **성공률 향상**: 사전 학습 후 작업 성공률이 처음부터 학습한 경우보다 20% 이상 향상되었습니다.
- **성능 비교**: 본 논문의 데이터셋 사전 학습 성능은 실제 로봇 데이터셋 사전 학습과 동등했습니다.
- **시너지 효과**: 본 논문의 데이터셋과 실제 로봇 데이터를 결합하면 성능이 더욱 개선되었습니다.

### 결론
1인칭 비디오는 VLA 연구를 추진하는 유망하고 확장 가능한 자원이며, EgoScaler 프레임워크는 원시 비디오에서 조작 궤적을 추출하는 어려움을 효과적으로 해결합니다.
