---
$id: ent_paper_liu_occvla_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision'
  zh: OccVLA
  ko: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision'
summary:
  en: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
  zh: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
  ko: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (OccVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Xi’an Jiaotong University, Fudan University,
    Shanghai Jiao Tong University, Tsinghua University.'
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
- occvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05578v1.
sources:
- id: src_001
  type: paper
  title: 'OccVLA: Vision-Language-Action Model with Implicit 3D Occupancy Supervision (arXiv)'
  url: https://arxiv.org/abs/2509.05578
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OccVLA source
  url: https://doi.org/10.48550/arXiv.2509.05578
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## 核心内容
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## 参考
- http://arxiv.org/abs/2509.05578v1

## Overview
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## Content
Multimodal large language models (MLLMs) have shown strong vision-language reasoning abilities but still lack robust 3D spatial understanding, which is critical for autonomous driving. This limitation stems from two key challenges: (1) the difficulty of constructing accessible yet effective 3D representations without expensive manual annotations, and (2) the loss of fine-grained spatial details in VLMs due to the absence of large-scale 3D vision-language pretraining. To address these challenges, we propose OccVLA, a novel framework that integrates 3D occupancy representations into a unified multimodal reasoning process. Unlike prior approaches that rely on explicit 3D inputs, OccVLA treats dense 3D occupancy as both a predictive output and a supervisory signal, enabling the model to learn fine-grained spatial structures directly from 2D visual inputs. The occupancy predictions are regarded as implicit reasoning processes and can be skipped during inference without performance degradation, thereby adding no extra computational overhead. OccVLA achieves state-of-the-art results on the nuScenes benchmark for trajectory planning and demonstrates superior performance on 3D visual question-answering tasks, offering a scalable, interpretable, and fully vision-based solution for autonomous driving.

## 개요
멀티모달 대규모 언어 모델(MLLM)은 강력한 시각-언어 추론 능력을 보여주었지만, 자율주행에 중요한 3D 공간 이해 능력은 여전히 부족합니다. 이러한 한계는 두 가지 주요 과제에서 비롯됩니다: (1) 고가의 수동 주석 없이 접근 가능하면서도 효과적인 3D 표현을 구축하는 어려움, (2) 대규모 3D 시각-언어 사전 학습 부재로 인한 VLM의 세부 공간 정보 손실입니다. 이러한 과제를 해결하기 위해, 우리는 3D 점유 표현을 통합된 멀티모달 추론 과정에 통합하는 새로운 프레임워크인 OccVLA를 제안합니다. 명시적 3D 입력에 의존하는 이전 접근 방식과 달리, OccVLA는 밀집 3D 점유를 예측 출력이자 감독 신호로 처리하여, 모델이 2D 시각 입력에서 직접 세부 공간 구조를 학습할 수 있도록 합니다. 점유 예측은 암시적 추론 과정으로 간주되며, 추론 중 성능 저하 없이 생략할 수 있어 추가 계산 오버헤드가 발생하지 않습니다. OccVLA는 궤적 계획을 위한 nuScenes 벤치마크에서 최첨단 결과를 달성하고, 3D 시각 질의응답 작업에서 뛰어난 성능을 보여주며, 자율주행을 위한 확장 가능하고 해석 가능하며 완전히 시각 기반의 솔루션을 제공합니다.

## 핵심 내용
멀티모달 대규모 언어 모델(MLLM)은 강력한 시각-언어 추론 능력을 보여주었지만, 자율주행에 중요한 3D 공간 이해 능력은 여전히 부족합니다. 이러한 한계는 두 가지 주요 과제에서 비롯됩니다: (1) 고가의 수동 주석 없이 접근 가능하면서도 효과적인 3D 표현을 구축하는 어려움, (2) 대규모 3D 시각-언어 사전 학습 부재로 인한 VLM의 세부 공간 정보 손실입니다. 이러한 과제를 해결하기 위해, 우리는 3D 점유 표현을 통합된 멀티모달 추론 과정에 통합하는 새로운 프레임워크인 OccVLA를 제안합니다. 명시적 3D 입력에 의존하는 이전 접근 방식과 달리, OccVLA는 밀집 3D 점유를 예측 출력이자 감독 신호로 처리하여, 모델이 2D 시각 입력에서 직접 세부 공간 구조를 학습할 수 있도록 합니다. 점유 예측은 암시적 추론 과정으로 간주되며, 추론 중 성능 저하 없이 생략할 수 있어 추가 계산 오버헤드가 발생하지 않습니다. OccVLA는 궤적 계획을 위한 nuScenes 벤치마크에서 최첨단 결과를 달성하고, 3D 시각 질의응답 작업에서 뛰어난 성능을 보여주며, 자율주행을 위한 확장 가능하고 해석 가능하며 완전히 시각 기반의 솔루션을 제공합니다.
