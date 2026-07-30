---
$id: ent_paper_in_n_on_scaling_egocentric_man_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data'
  zh: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data'
  ko: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data'
summary:
  en: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data is a 2025 work on manipulation for humanoid
    robots.'
  zh: In-N-On 是 2025 年面向人形机器人的操作工作，由研究团队提出，核心贡献在于将人类第一人称视频数据分为“in-the-wild”与“on-task”两类，并据此构建了包含 1,000 多小时野外数据与 20 多小时任务数据的
    PHSD 数据集，训练出大规模语言条件流匹配策略 Human0，实现了指令跟随、少样本学习与鲁棒性提升。
  ko: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data is a 2025 work on manipulation for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- in_n_on
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15704v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data (arXiv)'
  url: https://arxiv.org/abs/2511.15704
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作首先系统分析了人类第一人称视频数据的异质性，将其划分为两类：in-the-wild（野外数据）与 on-task（任务数据），并给出了可扩展的数据收集与使用方案。基于此，团队构建了 PHSD 数据集，其中包含超过 1,000 小时的多样化野外第一人称数据以及超过 20 小时与目标操作任务直接对齐的任务数据。利用该数据集，他们训练了一个大规模语言条件流匹配策略 Human0，并通过领域自适应技术缩小人类与人形机器人之间的差距。实验表明，Human0 从人类数据中实现了指令跟随、少样本学习以及利用任务数据提升鲁棒性等新颖特性。

## 核心内容
### 方法
- 将人类第一人称视频数据分为两类：**in-the-wild**（野外数据，涵盖日常多样化场景）与 **on-task**（任务数据，直接对齐目标操作任务）。
- 提出可扩展的数据收集与使用方案，系统分析两类数据在训练中的不同作用。

### 数据集
- 构建 **PHSD** 数据集，包含：
  - 超过 **1,000 小时** 的多样化 in-the-wild 第一人称数据。
  - 超过 **20 小时** 的 on-task 数据，直接与目标操作任务对齐。

### 模型架构
- 训练 **Human0**，一个大规模语言条件流匹配策略（language-conditioned flow matching policy）。
- 采用**领域自适应**技术，最小化人类与人形机器人之间的数据分布差异。

### 实验设置与关键结果
- **指令跟随**：仅从人类数据中学习，Human0 能理解并执行语言指令。
- **少样本学习**：利用少量 on-task 数据即可快速适应新任务。
- **鲁棒性提升**：on-task 数据显著增强了策略在真实环境中的稳定性。
- 项目网站提供更多细节与演示：https://xiongyicai.github.io/In-N-On/

## Overview
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 개요
자기중심적 비디오는 조작 정책을 학습하기 위한 가치 있고 확장 가능한 데이터 소스입니다. 그러나 상당한 데이터 이질성으로 인해 대부분의 기존 접근 방식은 인간 데이터를 단순한 사전 학습에 사용하여 그 잠재력을 완전히 활용하지 못합니다. 본 논문은 먼저 인간 데이터를 인더와일드(in-the-wild)와 온태스크(on-task)의 두 범주로 분류하고 데이터 사용 방법에 대한 체계적 분석을 제공함으로써 자기중심적 데이터를 수집하고 사용하기 위한 확장 가능한 레시피를 제시합니다. 우리는 먼저 PHSD 데이터셋을 구축했으며, 이 데이터셋은 1,000시간 이상의 다양한 인더와일드 자기중심적 데이터와 대상 조작 작업에 직접 정렬된 20시간 이상의 온태스크 데이터를 포함합니다. 이를 통해 대규모 자기중심적 언어 조건부 흐름 매칭 정책인 Human0을 학습할 수 있습니다. 도메인 적응 기술을 통해 Human0은 인간과 휴머노이드 간의 격차를 최소화합니다. 실험적으로, 우리는 Human0이 인간 데이터 확장을 통해 여러 새로운 특성을 달성함을 보여줍니다. 여기에는 인간 데이터만으로 지시를 따르는 언어 이해, 퓨샷 학습, 온태스크 데이터를 사용한 향상된 견고성이 포함됩니다. 프로젝트 웹사이트: https://xiongyicai.github.io/In-N-On/

## 핵심 내용
자기중심적 비디오는 조작 정책을 학습하기 위한 가치 있고 확장 가능한 데이터 소스입니다. 그러나 상당한 데이터 이질성으로 인해 대부분의 기존 접근 방식은 인간 데이터를 단순한 사전 학습에 사용하여 그 잠재력을 완전히 활용하지 못합니다. 본 논문은 먼저 인간 데이터를 인더와일드(in-the-wild)와 온태스크(on-task)의 두 범주로 분류하고 데이터 사용 방법에 대한 체계적 분석을 제공함으로써 자기중심적 데이터를 수집하고 사용하기 위한 확장 가능한 레시피를 제시합니다. 우리는 먼저 PHSD 데이터셋을 구축했으며, 이 데이터셋은 1,000시간 이상의 다양한 인더와일드 자기중심적 데이터와 대상 조작 작업에 직접 정렬된 20시간 이상의 온태스크 데이터를 포함합니다. 이를 통해 대규모 자기중심적 언어 조건부 흐름 매칭 정책인 Human0을 학습할 수 있습니다. 도메인 적응 기술을 통해 Human0은 인간과 휴머노이드 간의 격차를 최소화합니다. 실험적으로, 우리는 Human0이 인간 데이터 확장을 통해 여러 새로운 특성을 달성함을 보여줍니다. 여기에는 인간 데이터만으로 지시를 따르는 언어 이해, 퓨샷 학습, 온태스크 데이터를 사용한 향상된 견고성이 포함됩니다. 프로젝트 웹사이트: https://xiongyicai.github.io/In-N-On/

## 参考
- http://arxiv.org/abs/2511.15704v1
