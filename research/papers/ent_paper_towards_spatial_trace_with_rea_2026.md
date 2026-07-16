---
$id: ent_paper_towards_spatial_trace_with_rea_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
  zh: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
  ko: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
summary:
  en: 'arXiv:2512.13660v4 Announce Type: replace Abstract: Spatial tracing, as a fundamental embodied interaction ability
    for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial
    referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this
    end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal
    spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover,
    RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process
    rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training,
    we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting
    complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the
    gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding,
    measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench
    by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control
    policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.
    Please see the project page at https://zhoues.github.io/RoboTracer.'
  zh: 'arXiv:2512.13660v4 Announce Type: replace Abstract: Spatial tracing, as a fundamental embodied interaction ability
    for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial
    referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this
    end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal
    spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover,
    RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process
    rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training,
    we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting
    complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the
    gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding,
    measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench
    by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control
    policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.
    Please see the project page at https://zhoues.github.io/RoboTracer.'
  ko: 'arXiv:2512.13660v4 Announce Type: replace Abstract: Spatial tracing, as a fundamental embodied interaction ability
    for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial
    referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this
    end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal
    spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover,
    RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process
    rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training,
    we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting
    complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the
    gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding,
    measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench
    by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control
    policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes.
    Please see the project page at https://zhoues.github.io/RoboTracer.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- towards_spatial_trace_with_rea
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13660v4.
sources:
- id: src_001
  type: paper
  title: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics (arXiv)
  url: https://arxiv.org/abs/2512.13660
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## 核心内容
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## 参考
- http://arxiv.org/abs/2512.13660v4

## Overview
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## Content
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## 개요
공간 추적(Spatial tracing)은 로봇의 기본적인 체화 상호작용 능력으로, 다단계 측정 기반 추론(multi-step metric-grounded reasoning)과 복잡한 공간 지시(spatial referring) 및 실제 세계의 미터법 측정(metric measurement)이 결합되어 본질적으로 어려운 과제입니다. 그러나 기존 방법들은 이러한 구성적 과제에 어려움을 겪고 있습니다. 이를 해결하기 위해, 우리는 RoboTracer를 제안합니다. 이는 3D 인식 VLM으로, 지도 미세 조정(SFT) 중에 범용 공간 인코더와 회귀 감독 디코더를 통해 3D 공간 지시와 측정을 동시에 달성하여 규모 인식을 향상시킵니다. 또한, RoboTracer는 미터법에 민감한 프로세스 보상(metric-sensitive process rewards)을 사용한 강화 미세 조정(RFT)을 통해 다단계 측정 기반 추론을 발전시키며, 주요 중간 지각 단서를 감독하여 공간 추적을 정확하게 생성합니다. SFT 및 RFT 훈련을 지원하기 위해, 우리는 TraceSpatial을 소개합니다. 이는 3000만 QA 쌍으로 구성된 대규모 데이터셋으로, 실외/실내/테이블탑 장면을 포괄하며 최대 9단계의 복잡한 추론 과정을 지원합니다. 또한, 공간 추적 평가의 격차를 메우기 위한 도전적인 벤치마크인 TraceSpatial-Bench를 제시합니다. 실험 결과, RoboTracer는 공간 이해, 측정 및 지시에서 기준선을 능가하며 평균 성공률 79.1%를 달성하고, TraceSpatial-Bench에서도 큰 차이로 SOTA 성능을 기록하여 Gemini-2.5-Pro보다 정확도가 36% 높습니다. 특히, RoboTracer는 다양한 제어 정책과 통합되어 복잡한 실제 세계 장면에서 다양한 로봇(UR5, G1 휴머노이드)으로 장기적이고 동적인 작업을 실행할 수 있습니다. 프로젝트 페이지는 https://zhoues.github.io/RoboTracer에서 확인하세요.

## 핵심 내용
공간 추적(Spatial tracing)은 로봇의 기본적인 체화 상호작용 능력으로, 다단계 측정 기반 추론(multi-step metric-grounded reasoning)과 복잡한 공간 지시(spatial referring) 및 실제 세계의 미터법 측정(metric measurement)이 결합되어 본질적으로 어려운 과제입니다. 그러나 기존 방법들은 이러한 구성적 과제에 어려움을 겪고 있습니다. 이를 해결하기 위해, 우리는 RoboTracer를 제안합니다. 이는 3D 인식 VLM으로, 지도 미세 조정(SFT) 중에 범용 공간 인코더와 회귀 감독 디코더를 통해 3D 공간 지시와 측정을 동시에 달성하여 규모 인식을 향상시킵니다. 또한, RoboTracer는 미터법에 민감한 프로세스 보상(metric-sensitive process rewards)을 사용한 강화 미세 조정(RFT)을 통해 다단계 측정 기반 추론을 발전시키며, 주요 중간 지각 단서를 감독하여 공간 추적을 정확하게 생성합니다. SFT 및 RFT 훈련을 지원하기 위해, 우리는 TraceSpatial을 소개합니다. 이는 3000만 QA 쌍으로 구성된 대규모 데이터셋으로, 실외/실내/테이블탑 장면을 포괄하며 최대 9단계의 복잡한 추론 과정을 지원합니다. 또한, 공간 추적 평가의 격차를 메우기 위한 도전적인 벤치마크인 TraceSpatial-Bench를 제시합니다. 실험 결과, RoboTracer는 공간 이해, 측정 및 지시에서 기준선을 능가하며 평균 성공률 79.1%를 달성하고, TraceSpatial-Bench에서도 큰 차이로 SOTA 성능을 기록하여 Gemini-2.5-Pro보다 정확도가 36% 높습니다. 특히, RoboTracer는 다양한 제어 정책과 통합되어 복잡한 실제 세계 장면에서 다양한 로봇(UR5, G1 휴머노이드)으로 장기적이고 동적인 작업을 실행할 수 있습니다. 프로젝트 페이지는 https://zhoues.github.io/RoboTracer에서 확인하세요.
