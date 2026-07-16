---
$id: ent_paper_gigaworld_1_a_roadmap_to_build_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation'
  zh: 'GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation'
  ko: 'GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation'
summary:
  en: 'arXiv:2607.02642v1 Announce Type: new Abstract: Evaluating embodied robot foundation models remains a critical bottleneck;
    unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world
    rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators,
    yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents
    a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from
    real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons
    across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world
    models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions,
    further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated
    synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights:
    evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism;
    pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability;
    and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine
    alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it
    in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models,
    datasets, and toolkits to advance scalable evaluation research for embodied foundation models.'
  zh: 'arXiv:2607.02642v1 Announce Type: new Abstract: Evaluating embodied robot foundation models remains a critical bottleneck;
    unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world
    rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators,
    yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents
    a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from
    real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons
    across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world
    models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions,
    further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated
    synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights:
    evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism;
    pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability;
    and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine
    alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it
    in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models,
    datasets, and toolkits to advance scalable evaluation research for embodied foundation models.'
  ko: 'arXiv:2607.02642v1 Announce Type: new Abstract: Evaluating embodied robot foundation models remains a critical bottleneck;
    unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world
    rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators,
    yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents
    a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from
    real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons
    across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world
    models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions,
    further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated
    synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights:
    evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism;
    pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability;
    and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine
    alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it
    in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models,
    datasets, and toolkits to advance scalable evaluation research for embodied foundation models.'
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
- gigaworld_1
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02642v1.
sources:
- id: src_001
  type: paper
  title: 'GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation (arXiv)'
  url: https://arxiv.org/abs/2607.02642
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Evaluating embodied robot foundation models remains a critical bottleneck; unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators, yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions, further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights: evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism; pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability; and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models, datasets, and toolkits to advance scalable evaluation research for embodied foundation models.

## 核心内容
Evaluating embodied robot foundation models remains a critical bottleneck; unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators, yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions, further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights: evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism; pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability; and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models, datasets, and toolkits to advance scalable evaluation research for embodied foundation models.

## 参考
- http://arxiv.org/abs/2607.02642v1

## Overview
Evaluating embodied robot foundation models remains a critical bottleneck; unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators, yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions, further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights: evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism; pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability; and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models, datasets, and toolkits to advance scalable evaluation research for embodied foundation models.

## Content
Evaluating embodied robot foundation models remains a critical bottleneck; unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators, yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions, further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights: evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism; pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability; and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models, datasets, and toolkits to advance scalable evaluation research for embodied foundation models.

## 개요
로봇 기반 모델의 평가는 여전히 중요한 병목 현상으로 남아 있습니다. 대규모 언어 모델이 디지털 벤치마크를 통해 효율적으로 평가되는 것과 달리, 로봇 정책은 하드웨어와 인간의 감독에 의해 제한되는 느리고 비용이 많이 드는 실제 환경 롤아웃을 필요로 합니다. 이로 인해 세계 모델을 대리 정책 평가자로 사용하는 데 관심이 집중되었지만, 정책 평가에 신뢰할 수 있는 세계 모델을 만드는 핵심 속성은 아직 잘 이해되지 않고 있습니다. 본 연구는 로봇 정책 평가를 위한 세계 모델에 대한 체계적인 연구를 제시하며, 실제 로봇 원격 조작 데이터와 일치하는 정책 롤아웃으로 구성된 벤치마크인 WMBench를 소개합니다. 이 벤치마크는 다양한 조작 작업을 포괄하여 모델군, 행동 인코딩, 롤아웃 기간 및 평가 지표 간의 통제된 비교를 가능하게 합니다. WMBench를 사용하여 7개의 비디오 세계 모델, 4개의 행동 표현 방식, 324,000개 이상의 시뮬레이션 정책 롤아웃과 실제 로봇 실행을 분석하고, CVPR 2026 GigaBrain Challenge의 대규모 커뮤니티 제출물, 선별된 합성 궤적, 12,000시간 이상의 훈련 비디오로 분석을 더욱 풍부하게 합니다. 실험을 통해 세 가지 핵심 통찰을 얻었습니다: 평가자 품질은 단기 시각적 현실성보다 장기적이고 행동에 충실한 롤아웃 일관성에 의해 지배됩니다. 사전 훈련의 이점은 데이터 규모뿐만 아니라 일반 세계 지식과 로봇 특화 제어 가능성의 균형에서 비롯됩니다. 그리고 행동 인코딩, 메모리 설계, 평가자 중심 사후 훈련을 포함한 아키텍처 선택이 실제 로봇 행동과의 정렬을 강력하게 결정합니다. 이러한 결과를 바탕으로 실용적인 설계 로드맵을 도출하고, 이를 정책 평가에 특화된 세계 모델인 \textit{GigaWorld-1}에서 구현했습니다. 또한 코드, 모델, 데이터셋 및 도구 키트를 완전히 공개하여 임베디드 기반 모델의 확장 가능한 평가 연구를 발전시키고자 합니다.

## 핵심 내용
로봇 기반 모델의 평가는 여전히 중요한 병목 현상으로 남아 있습니다. 대규모 언어 모델이 디지털 벤치마크를 통해 효율적으로 평가되는 것과 달리, 로봇 정책은 하드웨어와 인간의 감독에 의해 제한되는 느리고 비용이 많이 드는 실제 환경 롤아웃을 필요로 합니다. 이로 인해 세계 모델을 대리 정책 평가자로 사용하는 데 관심이 집중되었지만, 정책 평가에 신뢰할 수 있는 세계 모델을 만드는 핵심 속성은 아직 잘 이해되지 않고 있습니다. 본 연구는 로봇 정책 평가를 위한 세계 모델에 대한 체계적인 연구를 제시하며, 실제 로봇 원격 조작 데이터와 일치하는 정책 롤아웃으로 구성된 벤치마크인 WMBench를 소개합니다. 이 벤치마크는 다양한 조작 작업을 포괄하여 모델군, 행동 인코딩, 롤아웃 기간 및 평가 지표 간의 통제된 비교를 가능하게 합니다. WMBench를 사용하여 7개의 비디오 세계 모델, 4개의 행동 표현 방식, 324,000개 이상의 시뮬레이션 정책 롤아웃과 실제 로봇 실행을 분석하고, CVPR 2026 GigaBrain Challenge의 대규모 커뮤니티 제출물, 선별된 합성 궤적, 12,000시간 이상의 훈련 비디오로 분석을 더욱 풍부하게 합니다. 실험을 통해 세 가지 핵심 통찰을 얻었습니다: 평가자 품질은 단기 시각적 현실성보다 장기적이고 행동에 충실한 롤아웃 일관성에 의해 지배됩니다. 사전 훈련의 이점은 데이터 규모뿐만 아니라 일반 세계 지식과 로봇 특화 제어 가능성의 균형에서 비롯됩니다. 그리고 행동 인코딩, 메모리 설계, 평가자 중심 사후 훈련을 포함한 아키텍처 선택이 실제 로봇 행동과의 정렬을 강력하게 결정합니다. 이러한 결과를 바탕으로 실용적인 설계 로드맵을 도출하고, 이를 정책 평가에 특화된 세계 모델인 \textit{GigaWorld-1}에서 구현했습니다. 또한 코드, 모델, 데이터셋 및 도구 키트를 완전히 공개하여 임베디드 기반 모델의 확장 가능한 평가 연구를 발전시키고자 합니다.
