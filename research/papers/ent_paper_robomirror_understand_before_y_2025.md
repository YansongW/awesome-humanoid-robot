---
$id: ent_paper_robomirror_understand_before_y_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
  zh: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
  ko: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion'
summary:
  en: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  zh: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
  ko: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion is a 2025 work on locomotion for humanoid
    robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- robomirror
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23649v3.
sources:
- id: src_001
  type: paper
  title: 'RoboMirror: Understand Before You Imitate for Video to Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2512.23649
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## 核心内容
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## 参考
- http://arxiv.org/abs/2512.23649v3

## Overview
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## Content
Humans learn locomotion through visual observation, interpreting visual content first before imitating actions. However, state-of-the-art humanoid locomotion systems rely on either curated motion capture trajectories or sparse text commands, leaving a critical gap between visual understanding and control. Text-to-motion methods suffer from semantic sparsity and staged pipeline errors, while video-based approaches only perform mechanical pose mimicry without genuine visual understanding. We propose RoboMirror, the first retargeting-free video-to-locomotion framework embodying "understand before you imitate". Leveraging VLMs, it distills raw egocentric/third-person videos into visual motion intents, which directly condition a diffusion-based policy to generate physically plausible, semantically aligned locomotion without explicit pose reconstruction or retargeting. Extensive experiments validate the effectiveness of RoboMirror, it enables telepresence via egocentric videos, drastically reduces third-person control latency by 80%, and achieves a 3.7% higher task success rate than baselines. By reframing humanoid control around video understanding, we bridge the visual understanding and action gap.

## 개요
인간은 시각적 관찰을 통해 보행을 학습하며, 먼저 시각적 내용을 해석한 후 동작을 모방합니다. 그러나 최첨단 휴머노이드 보행 시스템은 정제된 모션 캡처 궤적이나 희소한 텍스트 명령에 의존하여, 시각적 이해와 제어 사이에 중요한 격차가 존재합니다. 텍스트-모션 방법은 의미적 희소성과 단계적 파이프라인 오류로 어려움을 겪는 반면, 비디오 기반 접근법은 진정한 시각적 이해 없이 기계적인 포즈 모방만 수행합니다. 우리는 '모방하기 전에 이해하라'는 원칙을 구현한 최초의 리타겟팅 없는 비디오-보행 프레임워크인 RoboMirror를 제안합니다. VLM을 활용하여, 원시 자기 시점/3인칭 비디오를 시각적 움직임 의도로 추출하며, 이는 확산 기반 정책을 직접 조건화하여 명시적인 포즈 재구성이나 리타겟팅 없이 물리적으로 타당하고 의미적으로 정렬된 보행을 생성합니다. 광범위한 실험을 통해 RoboMirror의 효과성을 검증했으며, 자기 시점 비디오를 통한 원격 현장감을 가능하게 하고, 3인칭 제어 지연 시간을 80% 획기적으로 줄이며, 기준선 대비 작업 성공률을 3.7% 더 높였습니다. 비디오 이해를 중심으로 휴머노이드 제어를 재구성함으로써, 시각적 이해와 행동 간의 격차를 해소합니다.

## 핵심 내용
인간은 시각적 관찰을 통해 보행을 학습하며, 먼저 시각적 내용을 해석한 후 동작을 모방합니다. 그러나 최첨단 휴머노이드 보행 시스템은 정제된 모션 캡처 궤적이나 희소한 텍스트 명령에 의존하여, 시각적 이해와 제어 사이에 중요한 격차가 존재합니다. 텍스트-모션 방법은 의미적 희소성과 단계적 파이프라인 오류로 어려움을 겪는 반면, 비디오 기반 접근법은 진정한 시각적 이해 없이 기계적인 포즈 모방만 수행합니다. 우리는 '모방하기 전에 이해하라'는 원칙을 구현한 최초의 리타겟팅 없는 비디오-보행 프레임워크인 RoboMirror를 제안합니다. VLM을 활용하여, 원시 자기 시점/3인칭 비디오를 시각적 움직임 의도로 추출하며, 이는 확산 기반 정책을 직접 조건화하여 명시적인 포즈 재구성이나 리타겟팅 없이 물리적으로 타당하고 의미적으로 정렬된 보행을 생성합니다. 광범위한 실험을 통해 RoboMirror의 효과성을 검증했으며, 자기 시점 비디오를 통한 원격 현장감을 가능하게 하고, 3인칭 제어 지연 시간을 80% 획기적으로 줄이며, 기준선 대비 작업 성공률을 3.7% 더 높였습니다. 비디오 이해를 중심으로 휴머노이드 제어를 재구성함으로써, 시각적 이해와 행동 간의 격차를 해소합니다.
