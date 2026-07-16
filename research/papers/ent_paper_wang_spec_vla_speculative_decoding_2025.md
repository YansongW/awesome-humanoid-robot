---
$id: ent_paper_wang_spec_vla_speculative_decoding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance'
  zh: Spec-VLA
  ko: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance'
summary:
  en: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
  zh: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
  ko: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
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
- spec_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.22424v2.
sources:
- id: src_001
  type: paper
  title: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (arXiv)'
  url: https://arxiv.org/abs/2507.22424
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Spec-VLA source
  url: https://doi.org/10.48550/arXiv.2507.22424
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## 核心内容
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## 参考
- http://arxiv.org/abs/2507.22424v2

## Overview
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## Content
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## 개요
Vision-Language-Action (VLA) 모델은 Visual Language Models (VLM)의 강력한 기능을 활용하여 상당한 진전을 이루었습니다. 그러나 VLM의 큰 파라미터 크기와 자기회귀(AR) 디코딩 특성은 VLA 모델에 상당한 계산 요구를 부과합니다. Speculative Decoding (SD)은 효율적인 드래프팅과 병렬 검증을 통해 Large Language Models (LLM)을 가속화하는 데 효과적임이 입증되었으며, 한 번의 순방향 패스에서 여러 토큰을 생성할 수 있지만, VLA 모델에 대한 적용은 아직 탐구되지 않았습니다. 본 연구는 VLA 모델을 가속화하기 위해 설계된 SD 프레임워크인 Spec-VLA를 소개합니다. 행동 예측 작업의 어려움과 VLA 모델의 탐욕적 디코딩 메커니즘으로 인해, 고급 SD 프레임워크를 VLA 예측 작업에 직접 적용하면 속도 향상이 미미합니다. 생성 속도를 높이기 위해, 우리는 VLA 모델의 행동 토큰이 나타내는 상대적 거리를 활용하여 수용을 완화하는 효과적인 메커니즘을 제안합니다. 다양한 테스트 시나리오에 걸친 실증적 결과는 Spec-VLA 프레임워크의 효과성을 확인하며, 추가 분석은 제안된 전략의 영향을 입증하여 수용 길이를 44% 향상시키고, 성공률을 저하시키지 않으면서 OpenVLA 기준선 대비 1.42배의 속도 향상을 달성합니다. Spec-VLA 프레임워크의 성공은 VLA 예측 시나리오에서 추측 실행의 더 넓은 적용 가능성을 강조합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 Visual Language Models (VLM)의 강력한 기능을 활용하여 상당한 진전을 이루었습니다. 그러나 VLM의 큰 파라미터 크기와 자기회귀(AR) 디코딩 특성은 VLA 모델에 상당한 계산 요구를 부과합니다. Speculative Decoding (SD)은 효율적인 드래프팅과 병렬 검증을 통해 Large Language Models (LLM)을 가속화하는 데 효과적임이 입증되었으며, 한 번의 순방향 패스에서 여러 토큰을 생성할 수 있지만, VLA 모델에 대한 적용은 아직 탐구되지 않았습니다. 본 연구는 VLA 모델을 가속화하기 위해 설계된 SD 프레임워크인 Spec-VLA를 소개합니다. 행동 예측 작업의 어려움과 VLA 모델의 탐욕적 디코딩 메커니즘으로 인해, 고급 SD 프레임워크를 VLA 예측 작업에 직접 적용하면 속도 향상이 미미합니다. 생성 속도를 높이기 위해, 우리는 VLA 모델의 행동 토큰이 나타내는 상대적 거리를 활용하여 수용을 완화하는 효과적인 메커니즘을 제안합니다. 다양한 테스트 시나리오에 걸친 실증적 결과는 Spec-VLA 프레임워크의 효과성을 확인하며, 추가 분석은 제안된 전략의 영향을 입증하여 수용 길이를 44% 향상시키고, 성공률을 저하시키지 않으면서 OpenVLA 기준선 대비 1.42배의 속도 향상을 달성합니다. Spec-VLA 프레임워크의 성공은 VLA 예측 시나리오에서 추측 실행의 더 넓은 적용 가능성을 강조합니다.
