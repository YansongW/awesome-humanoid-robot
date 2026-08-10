---
$id: ent_paper_go_to_zero_towards_zero_shot_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  zh: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  ko: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
summary:
  en: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data is a paper on Human Motion for humanoid robotics.'
  zh: 本文提出MotionMillion，目前最大的人体运动数据集，包含超过2000小时和200万条高质量运动序列。研究团队基于该数据集训练了一个7B参数的可扩展模型，在零样本运动生成任务上展现出强大的泛化能力，并配套发布了MotionMillion-Eval基准用于评估。
  ko: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data is a paper on Human Motion for humanoid robotics.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- go_to_zero
- human_motion
- humanoid
- motion_synthesis
theoretical_depth:
- system
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.07095v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (690 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
针对现有文本到运动生成方法在零样本泛化能力上的不足，以及缺乏全面评估框架的问题，本研究开发了高效标注流程并构建了MotionMillion数据集。该数据集规模达到200万条运动序列，总时长超过2000小时。基于可扩展架构训练的7B参数模型在MotionMillion-Eval基准测试中，对域外和复杂组合运动展现出优异泛化性能，标志着零样本人体运动生成领域的重要进展。

## 核心内容
### 核心贡献
- **数据集构建**：开发高效标注流程，创建MotionMillion数据集，包含200万条高质量运动序列（总时长超2000小时），为当前最大规模人体运动数据集
- **评估基准**：提出MotionMillion-Eval，首个专门针对零样本运动生成的综合评估框架
- **模型架构**：采用可扩展架构，将模型参数规模扩展至7B，在MotionMillion-Eval上验证性能

### 实验设置与结果
- **训练数据**：全部使用MotionMillion数据集进行训练
- **评估指标**：在MotionMillion-Eval基准上测试零样本生成能力
- **关键发现**：
  - 对域外运动（out-of-domain motions）展现出强泛化能力
  - 能有效处理复杂组合运动（complex compositional motions）
  - 验证了大规模数据对零样本泛化能力的提升作用

### 开源资源
代码已公开在GitHub仓库：https://github.com/VankouF/MotionMillion-Codes

## Overview
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion-the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## Overview
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion—the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## Content
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion—the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## 参考
- http://arxiv.org/abs/2507.07095v1

## 개요
기존 텍스트-모션 생성 방법의 제로샷 일반화 능력 부족과 포괄적인 평가 프레임워크의 부재 문제를 해결하기 위해, 본 연구는 효율적인 주석 파이프라인을 개발하고 MotionMillion 데이터셋을 구축했습니다. 이 데이터셋은 총 200만 개의 모션 시퀀스와 2000시간 이상의 총 길이를 자랑합니다. 확장 가능한 아키텍처를 기반으로 훈련된 7B 파라미터 모델은 MotionMillion-Eval 벤치마크에서 도메인 외 및 복잡한 조합 모션에 대해 우수한 일반화 성능을 보여주며, 제로샷 인간 모션 생성 분야의 중요한 진전을 나타냅니다.

## 핵심 내용
### 핵심 기여
- **데이터셋 구축**: 효율적인 주석 파이프라인을 개발하여 MotionMillion 데이터셋을 생성, 200만 개의 고품질 모션 시퀀스(총 2000시간 이상)를 포함하며, 현재 최대 규모의 인간 모션 데이터셋입니다.
- **평가 벤치마크**: 제로샷 모션 생성을 위한 최초의 포괄적인 평가 프레임워크인 MotionMillion-Eval을 제안합니다.
- **모델 아키텍처**: 확장 가능한 아키텍처를 채택하여 모델 파라미터 규모를 7B로 확장하고, MotionMillion-Eval에서 성능을 검증했습니다.

### 실험 설정 및 결과
- **훈련 데이터**: 전체 MotionMillion 데이터셋을 사용하여 훈련을 진행했습니다.
- **평가 지표**: MotionMillion-Eval 벤치마크에서 제로샷 생성 능력을 테스트했습니다.
- **주요 발견**:
  - 도메인 외 모션(out-of-domain motions)에 대해 강력한 일반화 능력을 보여줍니다.
  - 복잡한 조합 모션(complex compositional motions)을 효과적으로 처리할 수 있습니다.
  - 대규모 데이터가 제로샷 일반화 능력 향상에 기여함을 검증했습니다.

### 오픈소스 리소스
코드는 GitHub 저장소에 공개되어 있습니다: https://github.com/VankouF/MotionMillion-Codes
