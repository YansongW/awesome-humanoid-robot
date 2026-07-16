---
$id: ent_paper_zheng_tracevla_visual_trace_promptin_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies'
  zh: TraceVLA
  ko: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies'
summary:
  en: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies (TraceVLA), is
    a 2024 large vision-language-action model for robotic manipulation, introduced by University of Maryland, College Park,
    Microsoft Research, Capital One, and published at ICLR 2024.'
  zh: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies (TraceVLA), is
    a 2024 large vision-language-action model for robotic manipulation, introduced by University of Maryland, College Park,
    Microsoft Research, Capital One, and published at ICLR 2024.'
  ko: 'TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies (TraceVLA), is
    a 2024 large vision-language-action model for robotic manipulation, introduced by University of Maryland, College Park,
    Microsoft Research, Capital One, and published at ICLR 2024.'
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
- robotic_manipulation
- tracevla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.10345v3.
sources:
- id: src_001
  type: paper
  title: TraceVLA source
  url: https://openreview.net/forum?id=b1CVu9l5GO
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.

## 核心内容
Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.

## 参考
- http://arxiv.org/abs/2412.10345v3

## Overview
Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.

## Content
Although large vision-language-action (VLA) models pretrained on extensive robot datasets offer promising generalist policies for robotic learning, they still struggle with spatial-temporal dynamics in interactive robotics, making them less effective in handling complex tasks, such as manipulation. In this work, we introduce visual trace prompting, a simple yet effective approach to facilitate VLA models' spatial-temporal awareness for action prediction by encoding state-action trajectories visually. We develop a new TraceVLA model by finetuning OpenVLA on our own collected dataset of 150K robot manipulation trajectories using visual trace prompting. Evaluations of TraceVLA across 137 configurations in SimplerEnv and 4 tasks on a physical WidowX robot demonstrate state-of-the-art performance, outperforming OpenVLA by 10% on SimplerEnv and 3.5x on real-robot tasks and exhibiting robust generalization across diverse embodiments and scenarios. To further validate the effectiveness and generality of our method, we present a compact VLA model based on 4B Phi-3-Vision, pretrained on the Open-X-Embodiment and finetuned on our dataset, rivals the 7B OpenVLA baseline while significantly improving inference efficiency.

## 개요
대규모 로봇 데이터셋에서 사전 학습된 대규모 비전-언어-행동(VLA) 모델은 로봇 학습을 위한 유망한 범용 정책을 제공하지만, 상호작용 로봇 공학에서의 시공간 역학을 여전히 어려워하여 조작과 같은 복잡한 작업을 처리하는 데 효과적이지 않습니다. 본 연구에서는 상태-행동 궤적을 시각적으로 인코딩하여 VLA 모델의 시공간 인식을 촉진하는 간단하면서도 효과적인 접근 방식인 시각적 추적 프롬프팅(visual trace prompting)을 소개합니다. 우리는 자체 수집한 150K 로봇 조작 궤적 데이터셋에서 시각적 추적 프롬프팅을 사용하여 OpenVLA를 미세 조정한 새로운 TraceVLA 모델을 개발했습니다. SimplerEnv의 137개 구성과 실제 WidowX 로봇의 4개 작업에 걸친 TraceVLA 평가는 최첨단 성능을 입증하며, SimplerEnv에서 OpenVLA보다 10%, 실제 로봇 작업에서 3.5배 더 뛰어난 성능을 보이고 다양한 체현 및 시나리오에서 강력한 일반화를 나타냅니다. 우리 방법의 효과성과 일반성을 더 검증하기 위해, 4B Phi-3-Vision을 기반으로 Open-X-Embodiment에서 사전 학습되고 우리 데이터셋에서 미세 조정된 소형 VLA 모델을 제시하며, 이는 7B OpenVLA 기준선과 경쟁하면서 추론 효율성을 크게 향상시킵니다.

## 핵심 내용
대규모 로봇 데이터셋에서 사전 학습된 대규모 비전-언어-행동(VLA) 모델은 로봇 학습을 위한 유망한 범용 정책을 제공하지만, 상호작용 로봇 공학에서의 시공간 역학을 여전히 어려워하여 조작과 같은 복잡한 작업을 처리하는 데 효과적이지 않습니다. 본 연구에서는 상태-행동 궤적을 시각적으로 인코딩하여 VLA 모델의 시공간 인식을 촉진하는 간단하면서도 효과적인 접근 방식인 시각적 추적 프롬프팅(visual trace prompting)을 소개합니다. 우리는 자체 수집한 150K 로봇 조작 궤적 데이터셋에서 시각적 추적 프롬프팅을 사용하여 OpenVLA를 미세 조정한 새로운 TraceVLA 모델을 개발했습니다. SimplerEnv의 137개 구성과 실제 WidowX 로봇의 4개 작업에 걸친 TraceVLA 평가는 최첨단 성능을 입증하며, SimplerEnv에서 OpenVLA보다 10%, 실제 로봇 작업에서 3.5배 더 뛰어난 성능을 보이고 다양한 체현 및 시나리오에서 강력한 일반화를 나타냅니다. 우리 방법의 효과성과 일반성을 더 검증하기 위해, 4B Phi-3-Vision을 기반으로 Open-X-Embodiment에서 사전 학습되고 우리 데이터셋에서 미세 조정된 소형 VLA 모델을 제시하며, 이는 7B OpenVLA 기준선과 경쟁하면서 추론 효율성을 크게 향상시킵니다.
