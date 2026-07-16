---
$id: ent_paper_tang_vlash_real_time_vlas_via_futur_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference'
  zh: VLASH
  ko: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference'
summary:
  en: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
  zh: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
  ko: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (VLASH), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MIT.'
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
- vision_language_action
- vla
- vlash
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01031v1.
sources:
- id: src_001
  type: paper
  title: 'VLASH: Real-Time VLAs via Future-State-Aware Asynchronous Inference (arXiv)'
  url: https://arxiv.org/abs/2512.01031
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLASH source
  url: https://doi.org/10.48550/arXiv.2512.01031
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## 核心内容
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## 参考
- http://arxiv.org/abs/2512.01031v1

## Overview
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## Content
Vision-Language-Action models (VLAs) are becoming increasingly capable across diverse robotic tasks. However, their real-world deployment remains slow and inefficient: demonstration videos are often sped up by 5-10x to appear smooth, with noticeable action stalls and delayed reactions to environmental changes. Asynchronous inference offers a promising solution to achieve continuous and low-latency control by enabling robots to execute actions and perform inference simultaneously. However, because the robot and environment continue to evolve during inference, a temporal misalignment arises between the prediction and execution intervals. This leads to significant action instability, while existing methods either degrade accuracy or introduce runtime overhead to mitigate it. We propose VLASH, a general asynchronous inference framework for VLAs that delivers smooth, accurate, and fast reaction control without additional overhead or architectural changes. VLASH estimates the future execution-time state by rolling the robot state forward with the previously generated action chunk, thereby bridging the gap between prediction and execution. Experiments show that VLASH achieves up to 2.03x speedup and reduces reaction latency by up to 17.4x compared to synchronous inference while fully preserving the original accuracy. Moreover, it empowers VLAs to handle fast-reaction, high-precision tasks such as playing ping-pong and playing whack-a-mole, where traditional synchronous inference fails. Code is available at https://github.com/mit-han-lab/vlash

## 개요
Vision-Language-Action 모델(VLA)은 다양한 로봇 작업에서 점점 더 강력해지고 있습니다. 그러나 실제 환경에서의 배포는 여전히 느리고 비효율적입니다. 데모 영상은 종종 5~10배 속도를 높여 부드럽게 보이지만, 눈에 띄는 동작 지연과 환경 변화에 대한 늦은 반응이 나타납니다. 비동기 추론은 로봇이 동작을 실행하는 동시에 추론을 수행할 수 있게 하여 지속적이고 지연 시간이 짧은 제어를 달성할 수 있는 유망한 솔루션을 제공합니다. 그러나 추론 중에 로봇과 환경이 계속 변화하기 때문에 예측 구간과 실행 구간 사이에 시간적 불일치가 발생합니다. 이는 심각한 동작 불안정성을 초래하며, 기존 방법은 이를 완화하기 위해 정확도를 저하시키거나 런타임 오버헤드를 발생시킵니다. 우리는 추가 오버헤드나 아키텍처 변경 없이 부드럽고 정확하며 빠른 반응 제어를 제공하는 VLA를 위한 일반 비동기 추론 프레임워크인 VLASH를 제안합니다. VLASH는 이전에 생성된 동작 청크를 사용하여 로봇 상태를 전진시킴으로써 미래 실행 시점의 상태를 추정하여 예측과 실행 사이의 간극을 메웁니다. 실험 결과, VLASH는 동기 추론 대비 최대 2.03배 속도 향상과 최대 17.4배 반응 지연 시간 감소를 달성하면서 원래 정확도를 완전히 유지합니다. 또한, 전통적인 동기 추론이 실패하는 탁구 치기나 두더지 잡기와 같은 빠른 반응과 높은 정밀도가 필요한 작업을 VLA가 처리할 수 있게 합니다. 코드는 https://github.com/mit-han-lab/vlash 에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action 모델(VLA)은 다양한 로봇 작업에서 점점 더 강력해지고 있습니다. 그러나 실제 환경에서의 배포는 여전히 느리고 비효율적입니다. 데모 영상은 종종 5~10배 속도를 높여 부드럽게 보이지만, 눈에 띄는 동작 지연과 환경 변화에 대한 늦은 반응이 나타납니다. 비동기 추론은 로봇이 동작을 실행하는 동시에 추론을 수행할 수 있게 하여 지속적이고 지연 시간이 짧은 제어를 달성할 수 있는 유망한 솔루션을 제공합니다. 그러나 추론 중에 로봇과 환경이 계속 변화하기 때문에 예측 구간과 실행 구간 사이에 시간적 불일치가 발생합니다. 이는 심각한 동작 불안정성을 초래하며, 기존 방법은 이를 완화하기 위해 정확도를 저하시키거나 런타임 오버헤드를 발생시킵니다. 우리는 추가 오버헤드나 아키텍처 변경 없이 부드럽고 정확하며 빠른 반응 제어를 제공하는 VLA를 위한 일반 비동기 추론 프레임워크인 VLASH를 제안합니다. VLASH는 이전에 생성된 동작 청크를 사용하여 로봇 상태를 전진시킴으로써 미래 실행 시점의 상태를 추정하여 예측과 실행 사이의 간극을 메웁니다. 실험 결과, VLASH는 동기 추론 대비 최대 2.03배 속도 향상과 최대 17.4배 반응 지연 시간 감소를 달성하면서 원래 정확도를 완전히 유지합니다. 또한, 전통적인 동기 추론이 실패하는 탁구 치기나 두더지 잡기와 같은 빠른 반응과 높은 정밀도가 필요한 작업을 VLA가 처리할 수 있게 합니다. 코드는 https://github.com/mit-han-lab/vlash 에서 확인할 수 있습니다.
