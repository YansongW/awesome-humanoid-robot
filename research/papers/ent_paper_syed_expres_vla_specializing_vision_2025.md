---
$id: ent_paper_syed_expres_vla_specializing_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval'
  zh: ExpReS-VLA
  ko: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval'
summary:
  en: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
  zh: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
  ko: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- expres_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06202v2.
sources:
- id: src_001
  type: paper
  title: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (arXiv)'
  url: https://arxiv.org/abs/2511.06202
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ExpReS-VLA source
  url: https://doi.org/10.48550/arXiv.2511.06202
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the $k$ most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including $π_0$ (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## 核心内容
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the $k$ most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including $π_0$ (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## 参考
- http://arxiv.org/abs/2511.06202v2

## Overview
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the \(k\) most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including \(\pi_0\) (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## Content
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the \(k\) most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including \(\pi_0\) (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## 개요
OpenVLA와 같은 Vision-Language-Action (VLA) 모델은 로봇 조작 작업에서 인상적인 제로샷 일반화 성능을 보여주지만, 광범위한 일반화보다 제한된 작업 집합에서 일관된 고성능이 더 중요한 특정 배포 환경에 적응하는 데 어려움을 겪습니다. 본 논문에서는 압축된 경험 재생과 검색 증강 생성을 통해 치명적 망각을 방지하면서 사전 훈련된 VLA를 대상 도메인에 신속하게 온디바이스 적응시키는 방법인 ExpReS-VLA (EXPierence replayed, REtrieval augmented, Specialized VLA)를 제시합니다. 우리의 접근 방식은 OpenVLA의 고정된 비전 백본에서 추출된 임베딩을 저장하여 메모리 효율적인 버퍼를 유지하며, 원시 이미지-행동 쌍에 비해 저장 요구 사항을 97% 줄입니다. 배포 중에 ExpReS-VLA는 코사인 유사도를 사용하여 가장 유사한 $k$개의 과거 경험을 검색하여 훈련 배치를 보강하고, 우선순위 경험 재생 버퍼는 최근 성공한 궤적을 보존합니다. 실패한 시도를 활용하기 위해 임계값 하이브리드 대조 손실(THCL)을 도입하여 모델이 성공 및 실패 시연 모두에서 학습할 수 있도록 합니다. LIBERO 벤치마크 실험에서는 기본 OpenVLA 대비 공간 추론에서 82.6%에서 93.1%로, 장기 과제에서 61%에서 72.3%로 향상되었으며, $π_0$(+3.2포인트) 및 OpenVLA-OFT(+1.7포인트)를 포함한 다양한 아키텍처에서 성능 향상을 보였습니다. 다섯 가지 작업에 걸친 실제 로봇 실험에서는 분포 내 및 분포 외 조건 모두에서 98%의 성공률을 보였으며, 이는 순수 미세 조정의 각각 84.7% 및 32%에서 향상된 것입니다. 적응은 단일 RTX 5090에서 12개의 시연을 사용하여 31초 만에 완료됩니다.

## 핵심 내용
OpenVLA와 같은 Vision-Language-Action (VLA) 모델은 로봇 조작 작업에서 인상적인 제로샷 일반화 성능을 보여주지만, 광범위한 일반화보다 제한된 작업 집합에서 일관된 고성능이 더 중요한 특정 배포 환경에 적응하는 데 어려움을 겪습니다. 본 논문에서는 압축된 경험 재생과 검색 증강 생성을 통해 치명적 망각을 방지하면서 사전 훈련된 VLA를 대상 도메인에 신속하게 온디바이스 적응시키는 방법인 ExpReS-VLA (EXPierence replayed, REtrieval augmented, Specialized VLA)를 제시합니다. 우리의 접근 방식은 OpenVLA의 고정된 비전 백본에서 추출된 임베딩을 저장하여 메모리 효율적인 버퍼를 유지하며, 원시 이미지-행동 쌍에 비해 저장 요구 사항을 97% 줄입니다. 배포 중에 ExpReS-VLA는 코사인 유사도를 사용하여 가장 유사한 $k$개의 과거 경험을 검색하여 훈련 배치를 보강하고, 우선순위 경험 재생 버퍼는 최근 성공한 궤적을 보존합니다. 실패한 시도를 활용하기 위해 임계값 하이브리드 대조 손실(THCL)을 도입하여 모델이 성공 및 실패 시연 모두에서 학습할 수 있도록 합니다. LIBERO 벤치마크 실험에서는 기본 OpenVLA 대비 공간 추론에서 82.6%에서 93.1%로, 장기 과제에서 61%에서 72.3%로 향상되었으며, $π_0$(+3.2포인트) 및 OpenVLA-OFT(+1.7포인트)를 포함한 다양한 아키텍처에서 성능 향상을 보였습니다. 다섯 가지 작업에 걸친 실제 로봇 실험에서는 분포 내 및 분포 외 조건 모두에서 98%의 성공률을 보였으며, 이는 순수 미세 조정의 각각 84.7% 및 32%에서 향상된 것입니다. 적응은 단일 RTX 5090에서 12개의 시연을 사용하여 31초 만에 완료됩니다.
