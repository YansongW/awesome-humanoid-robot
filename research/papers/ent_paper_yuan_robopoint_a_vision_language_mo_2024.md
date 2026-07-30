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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10721v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
테이블 위의 물체를 재배열하는 것부터 식료품을 선반에 올리는 것까지, 로봇은 작업을 정확하고 신뢰성 있게 수행하기 위해 정밀한 동작 지점을 계획해야 합니다. 최근 로봇 행동 제어를 위해 시각-언어 모델(VLM)이 도입되었지만, VLM은 언어를 사용하여 로봇 동작을 정밀하게 표현하는 데 어려움을 겪습니다. 우리는 VLM을 로봇 도메인과 요구 사항에 맞게 명령어 튜닝하는 자동 합성 데이터 생성 파이프라인을 소개합니다. 이 파이프라인을 사용하여 언어 명령어가 주어졌을 때 이미지의 키포인트 어포던스를 예측하는 VLM인 RoboPoint를 훈련합니다. 대안 접근법과 비교하여, 우리의 방법은 실제 세계 데이터 수집이나 인간 시연이 필요하지 않아 다양한 환경과 시점으로 확장성이 훨씬 뛰어납니다. 또한 RoboPoint는 로봇 내비게이션, 조작, 증강 현실(AR) 지원과 같은 여러 하위 응용 프로그램을 가능하게 하는 일반 모델입니다. 실험 결과, RoboPoint는 공간 어포던스 예측 정확도에서 최신 VLM(GPT-4o) 및 시각적 프롬프트 기술(PIVOT)보다 21.8%, 하위 작업 성공률에서 30.5% 더 우수한 성능을 보였습니다. 프로젝트 웹사이트: https://robo-point.github.io.

## 핵심 내용
테이블 위의 물체를 재배열하는 것부터 식료품을 선반에 올리는 것까지, 로봇은 작업을 정확하고 신뢰성 있게 수행하기 위해 정밀한 동작 지점을 계획해야 합니다. 최근 로봇 행동 제어를 위해 시각-언어 모델(VLM)이 도입되었지만, VLM은 언어를 사용하여 로봇 동작을 정밀하게 표현하는 데 어려움을 겪습니다. 우리는 VLM을 로봇 도메인과 요구 사항에 맞게 명령어 튜닝하는 자동 합성 데이터 생성 파이프라인을 소개합니다. 이 파이프라인을 사용하여 언어 명령어가 주어졌을 때 이미지의 키포인트 어포던스를 예측하는 VLM인 RoboPoint를 훈련합니다. 대안 접근법과 비교하여, 우리의 방법은 실제 세계 데이터 수집이나 인간 시연이 필요하지 않아 다양한 환경과 시점으로 확장성이 훨씬 뛰어납니다. 또한 RoboPoint는 로봇 내비게이션, 조작, 증강 현실(AR) 지원과 같은 여러 하위 응용 프로그램을 가능하게 하는 일반 모델입니다. 실험 결과, RoboPoint는 공간 어포던스 예측 정확도에서 최신 VLM(GPT-4o) 및 시각적 프롬프트 기술(PIVOT)보다 21.8%, 하위 작업 성공률에서 30.5% 더 우수한 성능을 보였습니다. 프로젝트 웹사이트: https://robo-point.github.io.

## 参考
- http://arxiv.org/abs/2406.10721v1
