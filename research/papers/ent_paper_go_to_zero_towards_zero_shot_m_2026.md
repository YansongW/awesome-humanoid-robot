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
  zh: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data is a paper on Human Motion for humanoid robotics.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.07095v1.
sources:
- id: src_001
  type: website
  title: 'Go to Zero: Towards Zero-shot Motion Generation with Million-scale Data'
  url: ''
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion-the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## 核心内容
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion-the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## 参考
- http://arxiv.org/abs/2507.07095v1

## Overview
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion—the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## Content
Generating diverse and natural human motion sequences based on textual descriptions constitutes a fundamental and challenging research area within the domains of computer vision, graphics, and robotics. Despite significant advancements in this field, current methodologies often face challenges regarding zero-shot generalization capabilities, largely attributable to the limited size of training datasets. Moreover, the lack of a comprehensive evaluation framework impedes the advancement of this task by failing to identify directions for improvement. In this work, we aim to push text-to-motion into a new era, that is, to achieve the generalization ability of zero-shot. To this end, firstly, we develop an efficient annotation pipeline and introduce MotionMillion—the largest human motion dataset to date, featuring over 2,000 hours and 2 million high-quality motion sequences. Additionally, we propose MotionMillion-Eval, the most comprehensive benchmark for evaluating zero-shot motion generation. Leveraging a scalable architecture, we scale our model to 7B parameters and validate its performance on MotionMillion-Eval. Our results demonstrate strong generalization to out-of-domain and complex compositional motions, marking a significant step toward zero-shot human motion generation. The code is available at https://github.com/VankouF/MotionMillion-Codes.

## 개요
텍스트 설명을 기반으로 다양하고 자연스러운 인간 동작 시퀀스를 생성하는 것은 컴퓨터 비전, 그래픽스 및 로보틱스 분야에서 기본적이면서도 도전적인 연구 영역입니다. 이 분야에서 상당한 진전이 있었음에도 불구하고, 현재의 방법론은 훈련 데이터셋의 제한된 크기로 인해 제로샷 일반화 능력에 있어 어려움을 겪는 경우가 많습니다. 또한, 포괄적인 평가 프레임워크의 부재는 개선 방향을 식별하지 못함으로써 이 작업의 발전을 저해합니다. 본 연구에서는 텍스트-투-모션을 새로운 시대로 이끌고자 합니다. 즉, 제로샷의 일반화 능력을 달성하는 것입니다. 이를 위해 먼저 효율적인 주석 파이프라인을 개발하고, 현재까지 가장 큰 인간 동작 데이터셋인 MotionMillion을 소개합니다. 이 데이터셋은 2,000시간 이상, 200만 개의 고품질 동작 시퀀스를 포함합니다. 또한, 제로샷 동작 생성을 평가하기 위한 가장 포괄적인 벤치마크인 MotionMillion-Eval을 제안합니다. 확장 가능한 아키텍처를 활용하여 모델을 7B 파라미터로 확장하고, MotionMillion-Eval에서 성능을 검증합니다. 우리의 결과는 도메인 외부 및 복잡한 구성 동작에 대한 강력한 일반화를 입증하며, 제로샷 인간 동작 생성으로의 중요한 진전을 나타냅니다. 코드는 https://github.com/VankouF/MotionMillion-Codes에서 확인할 수 있습니다.

## 핵심 내용
텍스트 설명을 기반으로 다양하고 자연스러운 인간 동작 시퀀스를 생성하는 것은 컴퓨터 비전, 그래픽스 및 로보틱스 분야에서 기본적이면서도 도전적인 연구 영역입니다. 이 분야에서 상당한 진전이 있었음에도 불구하고, 현재의 방법론은 훈련 데이터셋의 제한된 크기로 인해 제로샷 일반화 능력에 있어 어려움을 겪는 경우가 많습니다. 또한, 포괄적인 평가 프레임워크의 부재는 개선 방향을 식별하지 못함으로써 이 작업의 발전을 저해합니다. 본 연구에서는 텍스트-투-모션을 새로운 시대로 이끌고자 합니다. 즉, 제로샷의 일반화 능력을 달성하는 것입니다. 이를 위해 먼저 효율적인 주석 파이프라인을 개발하고, 현재까지 가장 큰 인간 동작 데이터셋인 MotionMillion을 소개합니다. 이 데이터셋은 2,000시간 이상, 200만 개의 고품질 동작 시퀀스를 포함합니다. 또한, 제로샷 동작 생성을 평가하기 위한 가장 포괄적인 벤치마크인 MotionMillion-Eval을 제안합니다. 확장 가능한 아키텍처를 활용하여 모델을 7B 파라미터로 확장하고, MotionMillion-Eval에서 성능을 검증합니다. 우리의 결과는 도메인 외부 및 복잡한 구성 동작에 대한 강력한 일반화를 입증하며, 제로샷 인간 동작 생성으로의 중요한 진전을 나타냅니다. 코드는 https://github.com/VankouF/MotionMillion-Codes에서 확인할 수 있습니다.
