---
$id: ent_paper_scaling_data_generation_vision_language_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scaling Data Generation in Vision-and-Language Navigation
  zh: Scaling Data Generation in Vision-and-Language Navigation
  ko: Scaling Data Generation in Vision-and-Language Navigation
summary:
  en: 'Recent research in language-guided visual navigation has demonstrated a significant demand for the diversity of traversable
    environments and the quantity of supervision for training generalizable agents. Institutions per source list: 澳大利亚国立大学、上海
    AI Lab.'
  zh: 本研究提出了一种大规模数据生成范式，用于解决视觉与语言导航（VLN）中的数据稀缺问题。该工作基于HM3D和Gibson数据集中的1200多个逼真环境，合成了490万条指令-轨迹对，并通过模仿学习将R2R基准测试的单次成功率提升至80%，较之前最佳方法绝对提升11%。同时，该方法将已知与未知环境间的泛化差距从8%缩小至不足1%。
  ko: 'Recent research in language-guided visual navigation has demonstrated a significant demand for the diversity of traversable
    environments and the quantity of supervision for training generalizable agents. Institutions per source list: 澳大利亚国立大学、上海
    AI Lab.'
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
- scaling
- data
- generation
- vision
- language
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 823 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2307.15644v2); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: arXiv:2307.15644 Scaling Data Generation in Vision-and-Language Navigation
  url: https://arxiv.org/abs/2307.15644
  accessed_at: '2026-07-31'
  date: '2023-07-28'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

该研究针对语言引导的视觉导航任务中训练数据不足的挑战，提出了一种高效的数据生成范式。通过利用HM3D和Gibson数据集的1200多个照片级真实环境，并整合网络上的完全可访问资源，合成了490万条指令-轨迹对。研究者系统分析了该范式中各组件对智能体性能的影响，并探索了如何将增强数据有效用于预训练和微调。实验表明，仅通过简单的模仿学习，该方法就在R2R测试集上实现了80%的单次成功率，将泛化差距从8%降至1%以下。此外，该范式还帮助不同模型在CVDN、REVERIE和连续环境下的R2R任务中取得了新的最佳导航结果。

## 核心内容
### 方法概述
- 数据生成范式基于HM3D和Gibson数据集中的1200多个照片级真实环境，利用网络上的完全可访问资源合成490万条指令-轨迹对。
- 研究者系统分析了该范式中各组件（如环境多样性、指令生成策略、轨迹采样方式）对智能体性能的影响，并研究了如何将增强数据有效用于预训练和微调。

### 实验设置与关键结果
- 在R2R测试集上，通过简单的模仿学习，智能体实现了80%的单次成功率，较之前最佳方法（SoTA）绝对提升11%。
- 已知与未知环境间的泛化差距从之前最佳方法的8%缩小至不足1%，显著提升了模型的泛化能力。
- 该范式还帮助不同模型在CVDN、REVERIE和连续环境下的R2R任务中取得了新的最佳导航结果。

### 结论
- 本研究提出的数据生成范式有效解决了VLN任务中的数据稀缺问题，通过大规模合成数据显著提升了智能体的导航性能和泛化能力。
- 该范式具有通用性，可应用于多种VLN模型和任务，为未来研究提供了可扩展的数据生成框架。

## Overview
Recent research in language-guided visual navigation has demonstrated a significant demand for the diversity of traversable environments and the quantity of supervision for training generalizable agents. To tackle the common data scarcity issue in existing vision-and-language navigation datasets, we propose an effective paradigm for generating large-scale data for learning, which applies 1200+ photo-realistic environments from HM3D and Gibson datasets and synthesizes 4.9 million instruction trajectory pairs using fully-accessible resources on the web. Importantly, we investigate the influence of each component in this paradigm on the agent's performance and study how to adequately apply the augmented data to pre-train and fine-tune an agent. Thanks to our large-scale dataset, the performance of an existing agent can be pushed up (+11% absolute with regard to previous SoTA) to a significantly new best of 80% single-run success rate on the R2R test split by simple imitation learning. The long-lasting generalization gap between navigating in seen and unseen environments is also reduced to less than 1% (versus 8% in the previous best method). Moreover, our paradigm also facilitates different models to achieve new state-of-the-art navigation results on CVDN, REVERIE, and R2R in continuous environments.

## 参考
- https://arxiv.org/abs/2307.15644
- https://github.com/ImChong/Robotics_Notebooks

## 개요

본 연구는 언어 기반 시각 내비게이션 작업에서 훈련 데이터 부족이라는 도전 과제를 해결하기 위해 효율적인 데이터 생성 패러다임을 제안합니다. HM3D 및 Gibson 데이터셋의 1200개 이상의 사실적인 환경을 활용하고, 웹상의 완전히 접근 가능한 리소스를 통합하여 490만 개의 명령-궤적 쌍을 합성했습니다. 연구자들은 이 패러다임의 각 구성 요소가 에이전트 성능에 미치는 영향을 체계적으로 분석하고, 증강 데이터를 사전 훈련 및 미세 조정에 효과적으로 활용하는 방법을 탐구했습니다. 실험 결과, 단순한 모방 학습만으로도 R2R 테스트 세트에서 80%의 단일 시도 성공률을 달성했으며, 일반화 격차를 8%에서 1% 미만으로 줄였습니다. 또한, 이 패러다임은 CVDN, REVERIE 및 연속 환경에서의 R2R 작업에서 다양한 모델이 새로운 최고 내비게이션 결과를 달성하도록 도왔습니다.

## 핵심 내용
### 방법 개요
- 데이터 생성 패러다임은 HM3D 및 Gibson 데이터셋의 1200개 이상의 사실적인 환경을 기반으로, 웹상의 완전히 접근 가능한 리소스를 활용하여 490만 개의 명령-궤적 쌍을 합성합니다.
- 연구자들은 이 패러다임의 각 구성 요소(예: 환경 다양성, 명령 생성 전략, 궤적 샘플링 방식)가 에이전트 성능에 미치는 영향을 체계적으로 분석하고, 증강 데이터를 사전 훈련 및 미세 조정에 효과적으로 활용하는 방법을 연구했습니다.

### 실험 설정 및 주요 결과
- R2R 테스트 세트에서 단순한 모방 학습을 통해 에이전트가 80%의 단일 시도 성공률을 달성했으며, 이는 이전 최고 방법(SoTA) 대비 절대적으로 11% 향상된 수치입니다.
- 알려진 환경과 알려지지 않은 환경 간의 일반화 격차가 이전 최고 방법의 8%에서 1% 미만으로 줄어들어, 모델의 일반화 능력이 크게 향상되었습니다.
- 이 패러다임은 CVDN, REVERIE 및 연속 환경에서의 R2R 작업에서 다양한 모델이 새로운 최고 내비게이션 결과를 달성하도록 도왔습니다.

### 결론
- 본 연구에서 제안한 데이터 생성 패러다임은 VLN 작업의 데이터 부족 문제를 효과적으로 해결하며, 대규모 합성 데이터를 통해 에이전트의 내비게이션 성능과 일반화 능력을 크게 향상시킵니다.
- 이 패러다임은 다양한 VLN 모델 및 작업에 적용 가능한 범용성을 가지며, 향후 연구를 위한 확장 가능한 데이터 생성 프레임워크를 제공합니다.
