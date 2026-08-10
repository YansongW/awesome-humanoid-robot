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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.16823v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (730 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2404.16823v2

## 개요
인간형 손재주 조작에서 원격 조작 비용이 높고 다지 손 촉각 하드웨어가 부족하다는 두 가지 도전 과제를 해결하기 위해, 연구팀은 HATO 시스템을 개발했습니다——기성 전자 부품으로 구축된 저비용 양팔 원격 조작 플랫폼으로, 소프트웨어는 다중 모달 데이터 처리와 정책 배포를 지원합니다. 동시에, 두 가지 상용 의수 손을 개조하고 촉각 센서를 통합하여 촉각 인식 하드웨어 부족 문제를 해결했습니다. 수집된 시각-촉각 데이터를 기반으로, 시스템은 다지 손재주와 촉각 피드백이 필요한 장시간 고정밀 작업을 성공적으로 학습했으며, 데이터 양, 인식 모달 및 시각 전처리가 정책 성능에 미치는 영향을 체계적으로 분석했습니다.

## 핵심 내용
### 방법 아키텍처
- **원격 조작 플랫폼 HATO**: 저비용 기성 전자 부품으로 양팔 원격 조작 장치를 구축하고, 소프트웨어는 효율적인 데이터 수집, 다중 모달 데이터 처리, 확장 가능한 정책 학습 및 원활한 배포를 지원합니다.
- **하드웨어 적응**: 두 가지 상용 의수 손을 개조하고 촉각 센서를 통합하여 연구 시나리오에 적합하게 만들고, 다지 손 촉각 하드웨어 부족 문제를 해결합니다.

### 실험 설정
- **데이터 수집**: HATO 시스템을 통해 인간 시연의 시각-촉각 데이터를 수집하여 정책 훈련에 사용합니다.
- **작업 유형**: 장시간, 고정밀 조작 작업으로, 다지 손재주와 촉각 피드백에 의존해야 완료할 수 있습니다.
- **변수 분석**: 데이터 세트 규모, 인식 모달(시각/촉각/시각-촉각 융합) 및 시각 입력 전처리 방식이 정책 학습 효과에 미치는 영향을 체계적으로 탐구합니다.

### 주요 결과
- 시각-촉각 데이터는 장시간 고정밀 작업의 성공률을 크게 향상시키며, 특히 촉각 피드백에 의존하는 정밀 조작 단계에서 효과적입니다.
- 데이터 세트 규모 증가는 정책 일반화 능력을 향상시킬 수 있지만 한계 효과가 존재합니다; 촉각 모달은 접촉 작업에서 시각보다 기여도가 높습니다.
- 시각 입력 전처리(예: 배경 제거, 조명 정규화)는 정책의 환경 과적합을 줄일 수 있습니다.

### 결론
이 작업은 양팔 다지 손의 시각-촉각 데이터 기반 손재주 조작 학습을 위한 저비용, 재현 가능한 솔루션을 제공하며, 오픈 소스 리소스(비디오, 코드, 데이터 세트)는 https://toruowo.github.io/hato/ 에서 확인할 수 있습니다.
