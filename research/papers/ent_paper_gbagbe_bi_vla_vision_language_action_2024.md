---
$id: ent_paper_gbagbe_bi_vla_vision_language_action_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bi-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Dexterous Manipulations'
  zh: Bi-VLA
  ko: 'Bi-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Dexterous Manipulations'
summary:
  en: 'Bi-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Dexterous Manipulations (Bi-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Skolkovo Institute of Science and Technology,
    and published at SMC 2024.'
  zh: Bi-VLA 是 Skolkovo Institute of Science and Technology 于 2024 年提出的大型视觉-语言-动作模型，专为双臂机器人灵巧操作设计。其核心贡献在于将场景理解、指令翻译与物理动作生成无缝集成，在沙拉制备等家务任务中实现了
    83.4% 的整体任务成功率。
  ko: 'Bi-VLA: Vision-Language-Action Model-Based System for Bimanual Robotic Dexterous Manipulations (Bi-VLA), is a 2024
    large vision-language-action model for robotic manipulation, introduced by Skolkovo Institute of Science and Technology,
    and published at SMC 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bi_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.06039v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: Bi-VLA source
  url: https://doi.org/10.1109/SMC54092.2024.10831380
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Bi-VLA 系统通过视觉模块感知环境、语言模块将人类指令转化为可执行代码，再由动作模块驱动双臂机器人完成精细操作。研究者在多组家庭场景实验中评估了系统性能，结果显示语言模块生成代码的正确率达 100%，视觉模块对特定食材的检测成功率为 96.06%，整体任务执行成功率为 83.4%。该系统展示了在复杂指令理解、视觉上下文感知及双臂协同操作方面的综合能力。

## 核心内容
### 方法架构
Bi-VLA 采用三模块协同架构：
- **Vision Module**：负责场景理解与食材识别，通过视觉感知获取操作对象的空间位置与状态。
- **Language Module**：将自然语言指令（如“准备一份沙拉”）翻译为机器人可执行的代码序列。
- **Action Module**：基于视觉与语言信息生成双臂灵巧操作的动作指令。

### 实验设置
- **任务场景**：家庭厨房环境中的沙拉制备任务，包含多种食材（如蔬菜、酱料）的识别、抓取与组合。
- **评估指标**：语言模块代码生成正确率、视觉模块食材检测成功率、整体任务执行成功率。
- **实验变量**：不同沙拉食谱与用户偏好（如食材替换、份量调整）。

### 关键结果
- **语言模块**：在全部测试指令中，代码生成正确率达 **100%**。
- **视觉模块**：对指定食材的检测成功率为 **96.06%**。
- **整体系统**：用户请求任务的完整执行成功率为 **83.4%**。

### 结论
Bi-VLA 验证了视觉-语言-动作模型在双臂灵巧操作中的可行性，尤其在需要语义理解与精细控制的复合任务中表现突出。未来工作可聚焦于提升视觉模块在遮挡场景下的鲁棒性，以及扩展至更复杂的多步骤操作流程。

## Overview
This research introduces the Bi-VLA (Vision-Language-Action) model, a novel system designed for bimanual robotic dexterous manipulation that seamlessly integrates vision for scene understanding, language comprehension for translating human instructions into executable code, and physical action generation. We evaluated the system's functionality through a series of household tasks, including the preparation of a desired salad upon human request. Bi-VLA demonstrates the ability to interpret complex human instructions, perceive and understand the visual context of ingredients, and execute precise bimanual actions to prepare the requested salad. We assessed the system's performance in terms of accuracy, efficiency, and adaptability to different salad recipes and human preferences through a series of experiments. Our results show a 100% success rate in generating the correct executable code by the Language Module, a 96.06% success rate in detecting specific ingredients by the Vision Module, and an overall success rate of 83.4% in correctly executing user-requested tasks.

## 개요
본 연구는 Bi-VLA(Vision-Language-Action) 모델을 소개합니다. 이는 양손 로봇의 정밀 조작을 위해 설계된 새로운 시스템으로, 장면 이해를 위한 시각, 인간 명령을 실행 가능한 코드로 변환하는 언어 이해, 그리고 물리적 동작 생성을 원활하게 통합합니다. 우리는 일련의 가사 작업(예: 인간 요청에 따른 원하는 샐러드 준비)을 통해 시스템의 기능을 평가했습니다. Bi-VLA는 복잡한 인간 명령을 해석하고, 재료의 시각적 맥락을 인지 및 이해하며, 요청된 샐러드를 준비하기 위해 정밀한 양손 동작을 실행하는 능력을 보여줍니다. 일련의 실험을 통해 정확성, 효율성, 그리고 다양한 샐러드 레시피 및 인간 선호도에 대한 적응성 측면에서 시스템 성능을 평가했습니다. 그 결과, 언어 모듈이 올바른 실행 코드를 생성하는 성공률은 100%, 시각 모듈이 특정 재료를 감지하는 성공률은 96.06%, 사용자 요청 작업을 올바르게 실행하는 전체 성공률은 83.4%를 기록했습니다.

## 핵심 내용
본 연구는 Bi-VLA(Vision-Language-Action) 모델을 소개합니다. 이는 양손 로봇의 정밀 조작을 위해 설계된 새로운 시스템으로, 장면 이해를 위한 시각, 인간 명령을 실행 가능한 코드로 변환하는 언어 이해, 그리고 물리적 동작 생성을 원활하게 통합합니다. 우리는 일련의 가사 작업(예: 인간 요청에 따른 원하는 샐러드 준비)을 통해 시스템의 기능을 평가했습니다. Bi-VLA는 복잡한 인간 명령을 해석하고, 재료의 시각적 맥락을 인지 및 이해하며, 요청된 샐러드를 준비하기 위해 정밀한 양손 동작을 실행하는 능력을 보여줍니다. 일련의 실험을 통해 정확성, 효율성, 그리고 다양한 샐러드 레시피 및 인간 선호도에 대한 적응성 측면에서 시스템 성능을 평가했습니다. 그 결과, 언어 모듈이 올바른 실행 코드를 생성하는 성공률은 100%, 시각 모듈이 특정 재료를 감지하는 성공률은 96.06%, 사용자 요청 작업을 올바르게 실행하는 전체 성공률은 83.4%를 기록했습니다.

## 参考
- http://arxiv.org/abs/2405.06039v2
