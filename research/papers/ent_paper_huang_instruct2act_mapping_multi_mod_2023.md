---
$id: ent_paper_huang_instruct2act_mapping_multi_mod_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model'
  zh: Instruct2Act
  ko: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model'
summary:
  en: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (Instruct2Act), is a
    2023 generalized vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Shanghai
    AI Laboratory, PKU, University of Chinese Academy of Sciences, The Chinese University of Hong Kong.'
  zh: Instruct2Act 是上海交通大学、上海人工智能实验室、北京大学、中国科学院大学及香港中文大学于 2023 年提出的通用视觉-语言-动作模型，用于机器人操作任务。其核心贡献在于利用大型语言模型将多模态指令映射为顺序动作，通过生成
    Python 程序实现感知、规划与动作的完整循环，并在零样本场景下超越多项现有学习策略。
  ko: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (Instruct2Act), is a
    2023 generalized vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Shanghai
    AI Laboratory, PKU, University of Chinese Academy of Sciences, The Chinese University of Hong Kong.'
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
- instruct2act
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.11176v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (716 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Instruct2Act: Mapping Multi-modality Instructions to Robotic Actions with Large Language Model (arXiv)'
  url: https://arxiv.org/abs/2305.11176
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Instruct2Act source
  url: https://doi.org/10.48550/arXiv.2305.11176
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Instruct2Act 框架通过大型语言模型将多模态指令转化为机器人可执行的序列动作。在感知模块中，它预定义 API 调用 Segment Anything Model (SAM) 精确定位候选物体，并利用 CLIP 进行分类，从而整合基础模型的专长与机器人能力。该框架支持灵活调整指令模态与输入类型，在桌面操作领域的多场景任务中验证了实用性与效率。其零样本方法在多项任务中优于当前最先进的基于学习的策略。

## 核心内容
### 方法架构
Instruct2Act 的核心是使用大型语言模型生成 Python 程序，构成机器人任务的感知、规划与动作循环。感知部分通过预定义 API 调用多个基础模型：Segment Anything Model (SAM) 负责精确分割候选物体，CLIP 则对分割结果进行分类。这种设计将复杂的高层指令转化为精确的策略代码，同时保持对不同指令模态（如文本、图像）和输入类型的适应性。

### 实验设置与关键结果
- 在桌面操作领域的多场景任务中评估，包括抓取、放置等典型操作。
- 零样本测试中，Instruct2Act 在多项任务上超越 state-of-the-art 学习策略，例如在物体分类与定位任务中表现突出。
- 代码开源于 https://github.com/OpenGVLab/Instruct2Act，可作为多模态高维机器人指令任务的基准。

### 结论
Instruct2Act 通过整合大型语言模型与基础模型（SAM、CLIP），实现了从多模态指令到机器人动作的高效映射，其零样本能力验证了框架的泛化性与实用性，为机器人操作任务提供了可扩展的解决方案。

## Overview
Foundation models have made significant strides in various applications, including text-to-image generation, panoptic segmentation, and natural language processing. This paper presents Instruct2Act, a framework that utilizes Large Language Models to map multi-modal instructions to sequential actions for robotic manipulation tasks. Specifically, Instruct2Act employs the LLM model to generate Python programs that constitute a comprehensive perception, planning, and action loop for robotic tasks. In the perception section, pre-defined APIs are used to access multiple foundation models where the Segment Anything Model (SAM) accurately locates candidate objects, and CLIP classifies them. In this way, the framework leverages the expertise of foundation models and robotic abilities to convert complex high-level instructions into precise policy codes. Our approach is adjustable and flexible in accommodating various instruction modalities and input types and catering to specific task demands. We validated the practicality and efficiency of our approach by assessing it on robotic tasks in different scenarios within tabletop manipulation domains. Furthermore, our zero-shot method outperformed many state-of-the-art learning-based policies in several tasks. The code for our proposed approach is available at https://github.com/OpenGVLab/Instruct2Act, serving as a robust benchmark for high-level robotic instruction tasks with assorted modality inputs.

## 参考
- http://arxiv.org/abs/2305.11176v3

## 개요
Instruct2Act 프레임워크는 대규모 언어 모델을 통해 다중 모달 지침을 로봇이 실행 가능한 순차적 동작으로 변환합니다. 인식 모듈에서는 사전 정의된 API를 호출하여 Segment Anything Model(SAM)이 후보 객체를 정밀하게 위치시키고, CLIP을 활용하여 분류함으로써 기초 모델의 전문성과 로봇 능력을 통합합니다. 이 프레임워크는 지침의 모달리티와 입력 유형을 유연하게 조정할 수 있으며, 데스크톱 조작 영역의 다중 시나리오 작업에서 실용성과 효율성을 검증했습니다. 제로샷 방식은 여러 작업에서 현재 최첨단 학습 기반 정책보다 우수한 성능을 보입니다.

## 핵심 내용
### 방법 아키텍처
Instruct2Act의 핵심은 대규모 언어 모델을 사용하여 Python 프로그램을 생성하고, 이를 통해 로봇 작업의 인식, 계획 및 동작 루프를 구성하는 것입니다. 인식 부분은 사전 정의된 API를 통해 여러 기초 모델을 호출합니다: Segment Anything Model(SAM)은 후보 객체의 정밀한 분할을 담당하고, CLIP은 분할 결과를 분류합니다. 이러한 설계는 복잡한 고수준 지침을 정밀한 정책 코드로 변환하면서도 다양한 지침 모달리티(예: 텍스트, 이미지)와 입력 유형에 대한 적응성을 유지합니다.

### 실험 설정 및 주요 결과
- 데스크톱 조작 영역의 다중 시나리오 작업에서 평가되었으며, 집기, 놓기 등의 전형적인 조작을 포함합니다.
- 제로샷 테스트에서 Instruct2Act는 여러 작업에서 최첨단 학습 정책을 능가했으며, 예를 들어 객체 분류 및 위치 파악 작업에서 두드러진 성능을 보였습니다.
- 코드는 https://github.com/OpenGVLab/Instruct2Act 에서 오픈소스로 제공되며, 다중 모달 고차원 로봇 지침 작업의 벤치마크로 활용될 수 있습니다.

### 결론
Instruct2Act는 대규모 언어 모델과 기초 모델(SAM, CLIP)을 통합하여 다중 모달 지침에서 로봇 동작으로의 효율적인 매핑을 구현했으며, 제로샷 능력은 프레임워크의 일반화 가능성과 실용성을 검증하여 로봇 조작 작업에 확장 가능한 솔루션을 제공합니다.
