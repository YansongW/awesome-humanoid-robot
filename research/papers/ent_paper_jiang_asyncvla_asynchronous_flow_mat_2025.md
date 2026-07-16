---
$id: ent_paper_jiang_asyncvla_asynchronous_flow_mat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models'
  zh: AsyncVLA
  ko: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models'
summary:
  en: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
  zh: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
  ko: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- asyncvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14148v2.
sources:
- id: src_001
  type: paper
  title: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.14148
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AsyncVLA source
  url: https://doi.org/10.48550/arXiv.2511.14148
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## 核心内容
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## 参考
- http://arxiv.org/abs/2511.14148v2

## Overview
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## Content
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## 개요
Vision-language-action (VLA) 모델은 최근 범용 로봇을 구축하기 위한 강력한 패러다임으로 부상했습니다. 그러나 flow matching (FM)을 통해 행동을 생성하는 기존 VLA 모델은 일반적으로 엄격하고 균일한 시간 스케줄, 즉 동기식 FM (SFM)에 의존합니다. 행동 컨텍스트 인식과 비동기식 자기 교정이 없으면 SFM은 장기 과제에서 불안정해져 단일 행동 오류가 연쇄적으로 실패로 이어질 수 있습니다. 본 연구에서는 비동기식 FM (AFM)에 시간적 유연성을 도입하고 행동 생성에서 자기 교정을 가능하게 하는 새로운 프레임워크인 비동기식 flow matching VLA (AsyncVLA)를 제안합니다. AsyncVLA는 행동 컨텍스트 인식을 통해 비균일 시간 스케줄로 행동 토큰을 생성함으로써 VLA 모델의 기본 SFM에서 벗어납니다. 또한, 본 방법은 신뢰도 평가기를 도입하여 초기 생성된 행동의 신뢰도를 추출함으로써 모델이 실행 전에 부정확한 행동 토큰을 선택적으로 개선할 수 있게 합니다. 더 나아가, SFM과 AFM을 위한 통합 훈련 절차를 제안하여 단일 모델이 두 모드를 모두 갖추도록 하여 KV-캐시 활용도를 향상시킵니다. 로봇 조작 벤치마크에 대한 광범위한 실험은 AsyncVLA가 데이터 효율적이며 자기 교정 능력을 보여줍니다. AsyncVLA는 시뮬레이션 및 실제 평가 모두에서 기존 방법보다 뛰어난 성능을 보입니다. 코드는 https://github.com/YuhuaJiang2002/AsyncVLA에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 최근 범용 로봇을 구축하기 위한 강력한 패러다임으로 부상했습니다. 그러나 flow matching (FM)을 통해 행동을 생성하는 기존 VLA 모델은 일반적으로 엄격하고 균일한 시간 스케줄, 즉 동기식 FM (SFM)에 의존합니다. 행동 컨텍스트 인식과 비동기식 자기 교정이 없으면 SFM은 장기 과제에서 불안정해져 단일 행동 오류가 연쇄적으로 실패로 이어질 수 있습니다. 본 연구에서는 비동기식 FM (AFM)에 시간적 유연성을 도입하고 행동 생성에서 자기 교정을 가능하게 하는 새로운 프레임워크인 비동기식 flow matching VLA (AsyncVLA)를 제안합니다. AsyncVLA는 행동 컨텍스트 인식을 통해 비균일 시간 스케줄로 행동 토큰을 생성함으로써 VLA 모델의 기본 SFM에서 벗어납니다. 또한, 본 방법은 신뢰도 평가기를 도입하여 초기 생성된 행동의 신뢰도를 추출함으로써 모델이 실행 전에 부정확한 행동 토큰을 선택적으로 개선할 수 있게 합니다. 더 나아가, SFM과 AFM을 위한 통합 훈련 절차를 제안하여 단일 모델이 두 모드를 모두 갖추도록 하여 KV-캐시 활용도를 향상시킵니다. 로봇 조작 벤치마크에 대한 광범위한 실험은 AsyncVLA가 데이터 효율적이며 자기 교정 능력을 보여줍니다. AsyncVLA는 시뮬레이션 및 실제 평가 모두에서 기존 방법보다 뛰어난 성능을 보입니다. 코드는 https://github.com/YuhuaJiang2002/AsyncVLA에서 확인할 수 있습니다.
