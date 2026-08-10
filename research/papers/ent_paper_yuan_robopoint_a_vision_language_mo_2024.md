---
$id: ent_paper_yuan_robopoint_a_vision_language_mo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics'
  zh: RoboPoint
  ko: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics'
summary:
  en: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
  zh: RoboPoint 是由华盛顿大学、NVIDIA、艾伦人工智能研究所、圣巴勃罗天主教大学联合提出的 2024 年通用视觉-语言-动作模型，发表于 CoRL 2024。其核心贡献在于通过自动合成数据管道对 VLM 进行指令微调，使其能根据语言指令预测图像关键点空间可供性，无需真实数据或人类演示，在空间可供性预测准确率和下游任务成功率上分别超越
    GPT-4o 和 PIVOT 达 21.8% 和 30.5%。
  ko: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
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
- robopoint
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10721v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (917 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: RoboPoint source
  url: https://proceedings.mlr.press/v270/yuan25c.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
RoboPoint 针对现有视觉语言模型难以精确表达机器人动作语言的问题，设计了一套自动合成数据生成管道，将 VLM 微调至机器人领域。该模型仅需语言指令即可预测图像中的关键点空间可供性，无需任何真实世界数据采集或人类示范，因此能高效扩展至不同环境和视角。作为通用模型，RoboPoint 支持机器人导航、操作及增强现实辅助等多种下游应用，实验表明其在空间可供性预测和下游任务成功率上均显著优于 GPT-4o 和 PIVOT 等现有方法。

## 核心内容
### 方法
- **问题背景**：机器人执行如桌面物体重排或货架放置等任务时，需精确规划动作点。现有 VLM 虽能控制机器人行为，但难以用语言精确描述动作。
- **核心方案**：RoboPoint 采用自动合成数据生成管道，对 VLM 进行指令微调，使其学会根据语言指令预测图像中的关键点空间可供性（即动作可行位置）。
- **关键优势**：无需真实数据或人类演示，仅依赖合成数据，大幅提升对不同环境和视角的扩展性。

### 架构
- **模型类型**：通用视觉-语言-动作模型，输入为图像和语言指令，输出为图像关键点坐标。
- **训练数据**：通过自动管道生成合成数据，涵盖多种机器人操作场景，确保模型泛化能力。

### 实验设置
- **对比方法**：与 GPT-4o（当前最强 VLM）和 PIVOT（视觉提示技术）进行对比。
- **评估指标**：空间可供性预测准确率、下游任务（导航、操作、AR 辅助）成功率。

### 关键结果
- **空间可供性预测**：RoboPoint 准确率比 GPT-4o 和 PIVOT 高 21.8%。
- **下游任务成功率**：RoboPoint 成功率比对比方法高 30.5%。
- **扩展性**：无需真实数据，合成数据管道使其能轻松适应新环境和新视角。

### 结论
RoboPoint 通过合成数据驱动的 VLM 微调，有效解决了机器人动作语言精确表达问题，在多项任务中显著超越现有方法，为机器人通用操作提供了可扩展的解决方案。项目网站：https://robo-point.github.io。

## Overview
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## 参考
- http://arxiv.org/abs/2406.10721v1

## 개요
RoboPoint는 기존 비전-언어 모델이 로봇 동작 언어를 정밀하게 표현하기 어려운 문제를 해결하기 위해, 자동 합성 데이터 생성 파이프라인을 설계하여 VLM을 로봇 도메인에 미세 조정한 모델입니다. 이 모델은 언어 명령만으로 이미지 내 키포인트 공간 가용성을 예측할 수 있으며, 실제 세계 데이터 수집이나 인간 시연 없이도 작동하므로 다양한 환경과 시점으로 효율적으로 확장할 수 있습니다. 범용 모델로서 RoboPoint는 로봇 내비게이션, 조작, 증강 현실 보조 등 다양한 하위 작업을 지원하며, 실험 결과 공간 가용성 예측과 하위 작업 성공률 모두에서 GPT-4o 및 PIVOT과 같은 기존 방법보다 크게 우수함을 보여줍니다.

## 핵심 내용
### 방법
- **문제 배경**: 로봇이 테이블 위 물체 재배치나 선반 배치와 같은 작업을 수행할 때 정밀한 동작 지점 계획이 필요합니다. 기존 VLM은 로봇 동작을 제어할 수 있지만, 언어로 동작을 정밀하게 설명하는 데 어려움이 있습니다.
- **핵심 솔루션**: RoboPoint는 자동 합성 데이터 생성 파이프라인을 채택하여 VLM을 명령 미세 조정하고, 언어 명령에 따라 이미지 내 키포인트 공간 가용성(즉, 동작 가능 위치)을 예측하도록 학습시킵니다.
- **주요 장점**: 실제 데이터나 인간 시연이 필요 없고 합성 데이터에만 의존하므로, 다양한 환경과 시점에 대한 확장성이 크게 향상됩니다.

### 아키텍처
- **모델 유형**: 범용 비전-언어-동작 모델로, 입력은 이미지와 언어 명령, 출력은 이미지 내 키포인트 좌표입니다.
- **학습 데이터**: 자동 파이프라인을 통해 합성 데이터를 생성하며, 다양한 로봇 조작 시나리오를 포함하여 모델의 일반화 능력을 보장합니다.

### 실험 설정
- **비교 방법**: GPT-4o(현재 최강 VLM) 및 PIVOT(시각 프롬프트 기술)과 비교합니다.
- **평가 지표**: 공간 가용성 예측 정확도, 하위 작업(내비게이션, 조작, AR 보조) 성공률.

### 주요 결과
- **공간 가용성 예측**: RoboPoint의 정확도는 GPT-4o 및 PIVOT보다 21.8% 높습니다.
- **하위 작업 성공률**: RoboPoint의 성공률은 비교 방법보다 30.5% 높습니다.
- **확장성**: 실제 데이터가 필요 없으며, 합성 데이터 파이프라인 덕분에 새로운 환경과 시점에 쉽게 적응할 수 있습니다.

### 결론
RoboPoint는 합성 데이터 기반 VLM 미세 조정을 통해 로봇 동작 언어의 정밀한 표현 문제를 효과적으로 해결하며, 여러 작업에서 기존 방법을 크게 능가하여 로봇 범용 조작을 위한 확장 가능한 솔루션을 제공합니다. 프로젝트 웹사이트: https://robo-point.github.io.
