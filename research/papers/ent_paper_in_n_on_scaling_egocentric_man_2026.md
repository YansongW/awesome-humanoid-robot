---
$id: ent_paper_in_n_on_scaling_egocentric_man_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA'
  zh: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA'
  ko: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA'
summary:
  en: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA is a 2026 work on manipulation for humanoid
    robots.'
  zh: IN-N-ON 是 2026 年面向人形机器人操作的研究，由团队提出。其核心贡献在于将人类第一人称视频数据系统分为 in-the-wild 与 on-task 两类，并基于此构建了包含 1000 小时野外数据与 20 小时任务数据的
    PHSD 数据集，训练出语言条件流匹配策略 Human0。通过域适应技术，Human0 实现了从人类数据到人形机器人的有效迁移，展现出指令跟随、少样本学习与鲁棒性提升等特性。
  ko: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA is a 2026 work on manipulation for humanoid
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15704v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (861 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA project page'
  url: https://openreview.net/attachment?id=JoK1hJg0Td&name=pdf
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该工作首先提出了一种可扩展的第一人称数据收集与使用方案，将人类操作视频明确划分为 in-the-wild（野外）与 on-task（任务）两类，并系统分析了如何利用这些数据。基于此分类，团队构建了 PHSD 数据集，包含超过 1000 小时的多样化野外数据与 20 小时直接对齐目标操作任务的任务数据。利用该数据集，他们训练了一个大规模的语言条件流匹配策略 Human0，并通过域适应技术缩小人类与人形机器人之间的差距。实验表明，Human0 仅从人类数据中学习即可实现语言指令跟随、少样本学习，并借助任务数据提升了鲁棒性。

## 核心内容
### 方法
- 将人类第一人称视频数据分为两类：**in-the-wild**（多样化、非结构化场景）与 **on-task**（直接对齐目标操作任务）。
- 基于此分类，提出可扩展的数据收集与使用方案，并系统分析两类数据在策略学习中的不同作用。

### 数据集
- 构建 **PHSD** 数据集，包含：
  - 超过 **1000 小时** 的 in-the-wild 第一人称数据。
  - 超过 **20 小时** 的 on-task 数据，直接对齐目标操作任务。

### 模型
- 训练 **Human0**，一个大规模的语言条件流匹配策略（language-conditioned flow matching policy）。
- 采用 **域适应技术**，最小化人类数据与人形机器人数据之间的分布差异，实现从人类到人形机器人的知识迁移。

### 实验设置与关键结果
- 实验验证 Human0 具备以下特性：
  - **语言指令跟随**：仅从人类数据中学习即可理解并执行自然语言指令。
  - **少样本学习**：在少量新任务数据上快速适应。
  - **鲁棒性提升**：利用 on-task 数据显著增强了策略在真实场景中的稳定性。
- 项目网站提供更多细节与演示：https://xiongyicai.github.io/In-N-On/

## Overview
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 参考
- http://arxiv.org/abs/2511.15704v1

## 개요
이 연구는 먼저 확장 가능한 일인칭 데이터 수집 및 활용 방안을 제안하며, 인간 조작 비디오를 명시적으로 in-the-wild(야외)와 on-task(과업) 두 가지 유형으로 구분하고, 이러한 데이터를 활용하는 방법을 체계적으로 분석합니다. 이 분류를 기반으로 팀은 1000시간 이상의 다양한 야외 데이터와 20시간의 목표 조작 과업에 직접 정렬된 과업 데이터를 포함하는 PHSD 데이터셋을 구축했습니다. 이 데이터셋을 활용하여 대규모 언어 조건 흐름 매칭 정책 Human0을 훈련시키고, 도메인 적응 기술을 통해 인간과 휴머노이드 로봇 간의 격차를 줄였습니다. 실험 결과, Human0은 인간 데이터만으로 학습하여 언어 명령 따르기, 소수 샷 학습을 구현할 수 있으며, 과업 데이터를 통해 견고성을 향상시킬 수 있음을 보여줍니다.

## 핵심 내용
### 방법
- 인간 일인칭 비디오 데이터를 두 가지 유형으로 구분: **in-the-wild**(다양하고 비구조화된 장면) 및 **on-task**(목표 조작 과업에 직접 정렬).
- 이 분류를 기반으로 확장 가능한 데이터 수집 및 활용 방안을 제안하고, 정책 학습에서 두 데이터 유형의 서로 다른 역할을 체계적으로 분석.

### 데이터셋
- **PHSD** 데이터셋 구축, 포함 내용:
  - **1000시간 이상**의 in-the-wild 일인칭 데이터.
  - **20시간 이상**의 on-task 데이터, 목표 조작 과업에 직접 정렬.

### 모델
- **Human0** 훈련, 대규모 언어 조건 흐름 매칭 정책(language-conditioned flow matching policy).
- **도메인 적응 기술** 채택, 인간 데이터와 휴머노이드 로봇 데이터 간의 분포 차이를 최소화하여 인간에서 휴머노이드 로봇으로의 지식 전이 구현.

### 실험 설정 및 주요 결과
- 실험을 통해 Human0의 다음 특성 검증:
  - **언어 명령 따르기**: 인간 데이터만으로 학습하여 자연어 명령을 이해하고 실행 가능.
  - **소수 샷 학습**: 소량의 새로운 과업 데이터에 빠르게 적응.
  - **견고성 향상**: on-task 데이터를 활용하여 실제 장면에서 정책의 안정성을 크게 강화.
- 프로젝트 웹사이트에서 더 많은 세부 정보 및 데모 제공: https://xiongyicai.github.io/In-N-On/
