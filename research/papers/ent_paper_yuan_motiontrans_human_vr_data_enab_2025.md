---
$id: ent_paper_yuan_motiontrans_human_vr_data_enab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies'
  zh: MotionTrans
  ko: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies'
summary:
  en: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
  zh: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
  ko: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- motiontrans
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.17759v1.
sources:
- id: src_001
  type: paper
  title: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (arXiv)'
  url: https://arxiv.org/abs/2509.17759
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MotionTrans source
  url: https://doi.org/10.48550/arXiv.2509.17759
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we direcly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## 核心内容
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we direcly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## 参考
- http://arxiv.org/abs/2509.17759v1

## Overview
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we directly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## Content
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we directly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## 개요
실제 로봇 데이터의 확장은 모방 학습의 주요 병목 현상으로, 정책 훈련에 보조 데이터를 사용하게 됩니다. 로봇 조작의 다른 측면(예: 이미지 또는 언어 이해)은 인터넷 기반 데이터셋에서 학습될 수 있지만, 동작 지식을 획득하는 것은 여전히 어려운 과제입니다. 다양한 조작 행동을 포함하는 인간 데이터는 이러한 목적에 귀중한 자원을 제공합니다. 이전 연구들은 인간 데이터를 사용하면 강건성 및 훈련 효율성 향상과 같은 이점을 얻을 수 있음을 보여주었지만, 인간 데이터가 가장 큰 장점인 로봇 정책이 작업 완료를 위해 새로운 동작을 직접 학습할 수 있게 하는 능력을 실현할 수 있는지는 여전히 불분명합니다. 본 논문에서는 다중 작업 인간-로봇 공동 훈련을 통해 이 가능성을 체계적으로 탐구합니다. 우리는 데이터 수집 시스템, 인간 데이터 변환 파이프라인, 가중 공동 훈련 전략을 포함하는 프레임워크인 MotionTrans를 소개합니다. 30개의 인간-로봇 작업을 동시에 공동 훈련함으로써, 13개 작업의 동작을 인간 데이터에서 배포 가능한 엔드투엔드 로봇 정책으로 직접 전송합니다. 특히, 9개 작업은 제로샷 방식에서 유의미한 성공률을 달성합니다. MotionTrans는 또한 사전 훈련-미세 조정 성능을 크게 향상시킵니다(+40% 성공률). 절제 연구를 통해 성공적인 동작 학습의 핵심 요소인 로봇 데이터와의 공동 훈련 및 광범위한 작업 관련 동작 범위를 식별합니다. 이러한 발견은 인간 데이터로부터의 동작 수준 학습 가능성을 열어주며, 로봇 조작 정책 훈련에 효과적으로 활용하기 위한 통찰력을 제공합니다. 모든 데이터, 코드 및 모델 가중치는 https://motiontrans.github.io/에서 오픈소스로 제공됩니다.

## 핵심 내용
실제 로봇 데이터의 확장은 모방 학습의 주요 병목 현상으로, 정책 훈련에 보조 데이터를 사용하게 됩니다. 로봇 조작의 다른 측면(예: 이미지 또는 언어 이해)은 인터넷 기반 데이터셋에서 학습될 수 있지만, 동작 지식을 획득하는 것은 여전히 어려운 과제입니다. 다양한 조작 행동을 포함하는 인간 데이터는 이러한 목적에 귀중한 자원을 제공합니다. 이전 연구들은 인간 데이터를 사용하면 강건성 및 훈련 효율성 향상과 같은 이점을 얻을 수 있음을 보여주었지만, 인간 데이터가 가장 큰 장점인 로봇 정책이 작업 완료를 위해 새로운 동작을 직접 학습할 수 있게 하는 능력을 실현할 수 있는지는 여전히 불분명합니다. 본 논문에서는 다중 작업 인간-로봇 공동 훈련을 통해 이 가능성을 체계적으로 탐구합니다. 우리는 데이터 수집 시스템, 인간 데이터 변환 파이프라인, 가중 공동 훈련 전략을 포함하는 프레임워크인 MotionTrans를 소개합니다. 30개의 인간-로봇 작업을 동시에 공동 훈련함으로써, 13개 작업의 동작을 인간 데이터에서 배포 가능한 엔드투엔드 로봇 정책으로 직접 전송합니다. 특히, 9개 작업은 제로샷 방식에서 유의미한 성공률을 달성합니다. MotionTrans는 또한 사전 훈련-미세 조정 성능을 크게 향상시킵니다(+40% 성공률). 절제 연구를 통해 성공적인 동작 학습의 핵심 요소인 로봇 데이터와의 공동 훈련 및 광범위한 작업 관련 동작 범위를 식별합니다. 이러한 발견은 인간 데이터로부터의 동작 수준 학습 가능성을 열어주며, 로봇 조작 정책 훈련에 효과적으로 활용하기 위한 통찰력을 제공합니다. 모든 데이터, 코드 및 모델 가중치는 https://motiontrans.github.io/에서 오픈소스로 제공됩니다.
