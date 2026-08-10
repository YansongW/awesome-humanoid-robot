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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.06039v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (750 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2405.06039v2

## 개요
Bi-VLA 시스템은 시각 모듈을 통해 환경을 인식하고, 언어 모듈이 인간의 지시를 실행 가능한 코드로 변환하며, 동작 모듈이 양팔 로봇을 구동하여 정밀한 조작을 완수합니다. 연구진은 여러 가정 환경 실험에서 시스템 성능을 평가했으며, 그 결과 언어 모듈의 코드 생성 정확도는 100%, 시각 모듈의 특정 식재료 감지 성공률은 96.06%, 전체 작업 실행 성공률은 83.4%로 나타났습니다. 이 시스템은 복잡한 지시 이해, 시각적 맥락 인식, 양팔 협동 조작에서의 종합적인 능력을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
Bi-VLA는 세 가지 모듈로 구성된 협력 아키텍처를 채택합니다:
- **Vision Module**: 장면 이해와 식재료 인식을 담당하며, 시각적 인식을 통해 조작 대상의 공간적 위치와 상태를 획득합니다.
- **Language Module**: 자연어 지시(예: "샐러드 준비해 줘")를 로봇이 실행 가능한 코드 시퀀스로 변환합니다.
- **Action Module**: 시각 및 언어 정보를 기반으로 양팔의 정교한 조작을 위한 동작 명령을 생성합니다.

### 실험 설정
- **작업 시나리오**: 가정 주방 환경에서의 샐러드 준비 작업으로, 여러 식재료(예: 채소, 소스)의 인식, 파지, 조합을 포함합니다.
- **평가 지표**: 언어 모듈의 코드 생성 정확도, 시각 모듈의 식재료 감지 성공률, 전체 작업 실행 성공률.
- **실험 변수**: 다양한 샐러드 레시피와 사용자 선호도(예: 식재료 대체, 분량 조절).

### 주요 결과
- **언어 모듈**: 모든 테스트 지시에서 코드 생성 정확도 **100%** 달성.
- **시각 모듈**: 지정된 식재료 감지 성공률 **96.06%**.
- **전체 시스템**: 사용자 요청 작업의 완전 실행 성공률 **83.4%**.

### 결론
Bi-VLA는 시각-언어-동작 모델이 양팔 정밀 조작에서의 실현 가능성을 검증했으며, 특히 의미적 이해와 정밀 제어가 필요한 복합 작업에서 뛰어난 성능을 보였습니다. 향후 연구는 폐색(occlusion) 상황에서 시각 모듈의 견고성을 향상시키고, 더 복잡한 다단계 조작 프로세스로 확장하는 데 초점을 맞출 수 있습니다.
