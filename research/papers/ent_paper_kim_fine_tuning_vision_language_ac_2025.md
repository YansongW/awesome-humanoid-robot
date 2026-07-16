---
$id: ent_paper_kim_fine_tuning_vision_language_ac_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
  zh: OpenVLA-OFT
  ko: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success'
summary:
  en: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
  zh: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
  ko: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University, and published at RSS 2025.'
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
- openvla_oft
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.19645v2.
sources:
- id: src_001
  type: paper
  title: 'Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (arXiv)'
  url: https://arxiv.org/abs/2502.19645
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenVLA-OFT source
  url: https://doi.org/10.48550/arXiv.2502.19645
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 核心内容
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 参考
- http://arxiv.org/abs/2502.19645v2

## Overview
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## Content
Recent vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets to demonstrate strong task execution, language following ability, and semantic generalization. Despite these successes, VLAs struggle with novel robot setups and require fine-tuning to achieve good performance, yet how to most effectively fine-tune them is unclear given many possible strategies. In this work, we study key VLA adaptation design choices such as different action decoding schemes, action representations, and learning objectives for fine-tuning, using OpenVLA as our representative base model. Our empirical analysis informs an Optimized Fine-Tuning (OFT) recipe that integrates parallel decoding, action chunking, a continuous action representation, and a simple L1 regression-based learning objective to altogether improve inference efficiency, policy performance, and flexibility in the model's input-output specifications. We propose OpenVLA-OFT, an instantiation of this recipe, which sets a new state of the art on the LIBERO simulation benchmark, significantly boosting OpenVLA's average success rate across four task suites from 76.5% to 97.1% while increasing action generation throughput by 26$\times$. In real-world evaluations, our fine-tuning recipe enables OpenVLA to successfully execute dexterous, high-frequency control tasks on a bimanual ALOHA robot and outperform other VLAs ($π_0$ and RDT-1B) fine-tuned using their default recipes, as well as strong imitation learning policies trained from scratch (Diffusion Policy and ACT) by up to 15% (absolute) in average success rate. We release code for OFT and pretrained model checkpoints at https://openvla-oft.github.io/.

## 개요
최근 비전-언어-행동 모델(VLA)은 사전 훈련된 비전-언어 모델을 기반으로 다양한 로봇 데이터셋을 활용하여 강력한 작업 실행, 언어 명령 수행 능력 및 의미적 일반화를 입증했습니다. 이러한 성공에도 불구하고 VLA는 새로운 로봇 설정에 어려움을 겪으며 좋은 성능을 달성하기 위해 미세 조정이 필요하지만, 다양한 가능한 전략이 존재하는 가운데 가장 효과적인 미세 조정 방법은 불분명합니다. 본 연구에서는 OpenVLA를 대표적인 기본 모델로 사용하여 다양한 행동 디코딩 방식, 행동 표현 및 미세 조정을 위한 학습 목표와 같은 주요 VLA 적응 설계 선택지를 연구합니다. 실증 분석을 통해 병렬 디코딩, 행동 청킹, 연속 행동 표현 및 간단한 L1 회귀 기반 학습 목표를 통합하여 추론 효율성, 정책 성능 및 모델의 입출력 사양 유연성을 모두 개선하는 최적화된 미세 조정(OFT) 레시피를 도출했습니다. 이 레시피의 구현체인 OpenVLA-OFT를 제안하며, 이는 LIBERO 시뮬레이션 벤치마크에서 새로운 최첨단 성능을 달성하여 네 가지 작업 제품군에서 OpenVLA의 평균 성공률을 76.5%에서 97.1%로 크게 향상시키고 행동 생성 처리량을 26배 증가시킵니다. 실제 환경 평가에서, 당사의 미세 조정 레시피는 OpenVLA가 양팔 ALOHA 로봇에서 정밀하고 고주파 제어 작업을 성공적으로 실행할 수 있게 하며, 기본 레시피로 미세 조정된 다른 VLA($π_0$ 및 RDT-1B)와 처음부터 훈련된 강력한 모방 학습 정책(Diffusion Policy 및 ACT)을 평균 성공률에서 최대 15%(절대값)까지 능가합니다. OFT 코드와 사전 훈련된 모델 체크포인트를 https://openvla-oft.github.io/에서 공개합니다.

## 핵심 내용
최근 비전-언어-행동 모델(VLA)은 사전 훈련된 비전-언어 모델을 기반으로 다양한 로봇 데이터셋을 활용하여 강력한 작업 실행, 언어 명령 수행 능력 및 의미적 일반화를 입증했습니다. 이러한 성공에도 불구하고 VLA는 새로운 로봇 설정에 어려움을 겪으며 좋은 성능을 달성하기 위해 미세 조정이 필요하지만, 다양한 가능한 전략이 존재하는 가운데 가장 효과적인 미세 조정 방법은 불분명합니다. 본 연구에서는 OpenVLA를 대표적인 기본 모델로 사용하여 다양한 행동 디코딩 방식, 행동 표현 및 미세 조정을 위한 학습 목표와 같은 주요 VLA 적응 설계 선택지를 연구합니다. 실증 분석을 통해 병렬 디코딩, 행동 청킹, 연속 행동 표현 및 간단한 L1 회귀 기반 학습 목표를 통합하여 추론 효율성, 정책 성능 및 모델의 입출력 사양 유연성을 모두 개선하는 최적화된 미세 조정(OFT) 레시피를 도출했습니다. 이 레시피의 구현체인 OpenVLA-OFT를 제안하며, 이는 LIBERO 시뮬레이션 벤치마크에서 새로운 최첨단 성능을 달성하여 네 가지 작업 제품군에서 OpenVLA의 평균 성공률을 76.5%에서 97.1%로 크게 향상시키고 행동 생성 처리량을 26배 증가시킵니다. 실제 환경 평가에서, 당사의 미세 조정 레시피는 OpenVLA가 양팔 ALOHA 로봇에서 정밀하고 고주파 제어 작업을 성공적으로 실행할 수 있게 하며, 기본 레시피로 미세 조정된 다른 VLA($π_0$ 및 RDT-1B)와 처음부터 훈련된 강력한 모방 학습 정책(Diffusion Policy 및 ACT)을 평균 성공률에서 최대 15%(절대값)까지 능가합니다. OFT 코드와 사전 훈련된 모델 체크포인트를 https://openvla-oft.github.io/에서 공개합니다.
