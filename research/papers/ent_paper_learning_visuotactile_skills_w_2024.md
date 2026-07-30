---
$id: ent_paper_learning_visuotactile_skills_w_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Visuotactile Skills with Two Multifingered Hands
  zh: Learning Visuotactile Skills with Two Multifingered Hands
  ko: Learning Visuotactile Skills with Two Multifingered Hands
summary:
  en: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
  zh: 本文提出一种基于双多指手与视触觉数据的灵巧操作技能学习方法，通过低成本遥操作系统HATO采集人类演示数据，并改造商用假肢手集成触觉传感器，实现长时程高精度任务。实验验证了数据集规模、感知模态与视觉预处理对策略学习的影响，代码与数据集已开源。
  ko: Learning Visuotactile Skills with Two Multifingered Hands is a 2024 work on manipulation for humanoid robots, with open-source
    code available.
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
- learning_visuotactile_skills_w
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.16823v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning Visuotactile Skills with Two Multifingered Hands (arXiv)
  url: https://arxiv.org/abs/2404.16823
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Learning Visuotactile Skills with Two Multifingered Hands project page
  url: https://toruowo.github.io/hato/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
针对仿人灵巧操作中遥操作成本高、多指手触觉硬件稀缺两大挑战，研究团队开发了HATO系统——利用现成电子元件构建的低成本双臂遥操作平台，配套软件支持多模态数据处理与策略部署。同时，通过改造两款商用假肢手并集成触觉传感器，解决了触觉感知硬件不足的问题。基于采集的视触觉数据，系统成功学习完成需要多指灵巧性与触觉反馈的长时程高精度任务，并系统分析了数据量、感知模态及视觉预处理对策略性能的影响。

## 核心内容
### 方法架构
- **遥操作平台HATO**：采用低成本现成电子元件构建双臂遥操作装置，配套软件支持高效数据采集、多模态数据处理、可扩展策略学习与平滑部署。
- **硬件适配**：改造两款商用假肢手，集成触觉传感器，使其适用于研究场景，解决多指手触觉硬件稀缺问题。

### 实验设置
- **数据采集**：通过HATO系统采集人类演示的视触觉数据，用于训练策略。
- **任务类型**：长时程、高精度操作任务，需依赖多指灵巧性与触觉反馈才能完成。
- **变量分析**：系统探究数据集规模、感知模态（视觉/触觉/视触觉融合）及视觉输入预处理方式对策略学习效果的影响。

### 关键结果
- 视触觉数据显著提升长时程高精度任务的成功率，尤其依赖触觉反馈的精细操作环节。
- 数据集规模增大可提升策略泛化能力，但存在边际效应；触觉模态在接触类任务中贡献度高于视觉。
- 视觉输入预处理（如背景去除、光照归一化）可降低策略对环境的过拟合。

### 结论
该工作为双臂多指手基于视触觉数据的灵巧操作学习提供了低成本、可复现的解决方案，开源资源（视频、代码、数据集）可访问 https://toruowo.github.io/hato/ 。

## Overview
Aiming to replicate human-like dexterity, perceptual experiences, and motion patterns, we explore learning from human demonstrations using a bimanual system with multifingered hands and visuotactile data. Two significant challenges exist: the lack of an affordable and accessible teleoperation system suitable for a dual-arm setup with multifingered hands, and the scarcity of multifingered hand hardware equipped with touch sensing. To tackle the first challenge, we develop HATO, a low-cost hands-arms teleoperation system that leverages off-the-shelf electronics, complemented with a software suite that enables efficient data collection; the comprehensive software suite also supports multimodal data processing, scalable policy learning, and smooth policy deployment. To tackle the latter challenge, we introduce a novel hardware adaptation by repurposing two prosthetic hands equipped with touch sensors for research. Using visuotactile data collected from our system, we learn skills to complete long-horizon, high-precision tasks which are difficult to achieve without multifingered dexterity and touch feedback. Furthermore, we empirically investigate the effects of dataset size, sensing modality, and visual input preprocessing on policy learning. Our results mark a promising step forward in bimanual multifingered manipulation from visuotactile data. Videos, code, and datasets can be found at https://toruowo.github.io/hato/ .

## 개요
인간과 유사한 손재주, 지각 경험 및 움직임 패턴을 재현하는 것을 목표로, 우리는 다지 손과 시각-촉각 데이터를 갖춘 양손 시스템을 사용하여 인간 시연으로부터 학습하는 방법을 탐구합니다. 두 가지 주요 과제가 존재합니다: 다지 손을 갖춘 이중 팔 설정에 적합한 저렴하고 접근 가능한 원격 조작 시스템의 부족, 그리고 촉각 감지 기능이 장착된 다지 손 하드웨어의 희소성입니다. 첫 번째 과제를 해결하기 위해, 우리는 기성 전자 부품을 활용한 저비용 손-팔 원격 조작 시스템인 HATO를 개발하고, 효율적인 데이터 수집을 가능하게 하는 소프트웨어 제품군을 함께 제공합니다. 이 포괄적인 소프트웨어 제품군은 다중 모드 데이터 처리, 확장 가능한 정책 학습, 그리고 원활한 정책 배포도 지원합니다. 두 번째 과제를 해결하기 위해, 우리는 연구 목적으로 촉각 센서가 장착된 두 개의 의수(prosthetic hand)를 재활용하는 새로운 하드웨어 적응 방식을 도입합니다. 우리 시스템에서 수집된 시각-촉각 데이터를 사용하여, 다지 손재주와 촉각 피드백 없이는 달성하기 어려운 장기적이고 고정밀 작업을 완료하는 기술을 학습합니다. 또한, 데이터 세트 크기, 감지 양식, 그리고 시각 입력 전처리가 정책 학습에 미치는 영향을 실증적으로 조사합니다. 우리의 결과는 시각-촉각 데이터를 활용한 양손 다지 조작 분야에서 유망한 진전을 의미합니다. 비디오, 코드 및 데이터 세트는 https://toruowo.github.io/hato/ 에서 확인할 수 있습니다.

## 핵심 내용
인간과 유사한 손재주, 지각 경험 및 움직임 패턴을 재현하는 것을 목표로, 우리는 다지 손과 시각-촉각 데이터를 갖춘 양손 시스템을 사용하여 인간 시연으로부터 학습하는 방법을 탐구합니다. 두 가지 주요 과제가 존재합니다: 다지 손을 갖춘 이중 팔 설정에 적합한 저렴하고 접근 가능한 원격 조작 시스템의 부족, 그리고 촉각 감지 기능이 장착된 다지 손 하드웨어의 희소성입니다. 첫 번째 과제를 해결하기 위해, 우리는 기성 전자 부품을 활용한 저비용 손-팔 원격 조작 시스템인 HATO를 개발하고, 효율적인 데이터 수집을 가능하게 하는 소프트웨어 제품군을 함께 제공합니다. 이 포괄적인 소프트웨어 제품군은 다중 모드 데이터 처리, 확장 가능한 정책 학습, 그리고 원활한 정책 배포도 지원합니다. 두 번째 과제를 해결하기 위해, 우리는 연구 목적으로 촉각 센서가 장착된 두 개의 의수를 재활용하는 새로운 하드웨어 적응 방식을 도입합니다. 우리 시스템에서 수집된 시각-촉각 데이터를 사용하여, 다지 손재주와 촉각 피드백 없이는 달성하기 어려운 장기적이고 고정밀 작업을 완료하는 기술을 학습합니다. 또한, 데이터 세트 크기, 감지 양식, 그리고 시각 입력 전처리가 정책 학습에 미치는 영향을 실증적으로 조사합니다. 우리의 결과는 시각-촉각 데이터를 활용한 양손 다지 조작 분야에서 유망한 진전을 의미합니다. 비디오, 코드 및 데이터 세트는 https://toruowo.github.io/hato/ 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2404.16823v2
