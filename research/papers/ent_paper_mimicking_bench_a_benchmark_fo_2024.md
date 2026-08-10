---
$id: ent_paper_mimicking_bench_a_benchmark_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking'
  zh: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking'
  ko: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking'
summary:
  en: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking is a 2024 work
    on simulation benchmark for humanoid robots.'
  zh: Mimicking-Bench 是 2024 年提出的首个面向人形机器人的通用化场景交互学习基准，通过模仿大规模人类动画数据来训练技能。该基准包含六类家庭全身交互任务，覆盖 11K 种物体形状，并提供 20K 合成与 3K 真实人类交互参考。其核心贡献在于构建了完整的技能学习流水线，并系统评估了运动重定向、跟踪、模仿学习及其组合方法。
  ko: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking is a 2024 work
    on simulation benchmark for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- mimicking_bench
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.17730v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (643 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking (arXiv)'
  url: https://arxiv.org/abs/2412.17730
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking project page'
  url: https://mimicking-bench.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Mimicking-Bench 旨在解决现有方法因依赖小规模人工采集演示数据而缺乏场景几何泛化能力的问题。该基准包含六类家庭全身人形机器人-场景交互任务，涵盖 11K 种不同物体形状，并提供了 20K 合成与 3K 真实世界的人类交互技能参考。研究团队构建了完整的人形技能学习流水线，对运动重定向、运动跟踪、模仿学习及其组合方法进行了基准测试。大量实验揭示了人类模仿在技能学习中的价值，并指出了关键挑战与研究方向。

## 核心内容
### 方法
- 核心思路：通过模仿大规模人类动画参考数据，使人形机器人学习与 3D 场景交互的通用技能，从而克服传统小规模人工演示数据在场景几何泛化上的局限。
- 流水线：构建了完整的人形技能学习流水线，涵盖从人类数据到机器人执行的多个环节。

### 架构与实验设置
- 任务：包含六类家庭全身人形机器人-场景交互任务，覆盖 11K 种不同物体形状。
- 数据：提供 20K 合成人类交互技能参考与 3K 真实世界人类交互技能参考。
- 基准方法：对运动重定向、运动跟踪、模仿学习及其各种组合方法进行系统评估。

### 关键数字与结论
- 规模：任务覆盖 11K 种物体形状，数据包含 20K 合成 + 3K 真实参考。
- 实验发现：人类模仿对技能学习具有显著价值，同时揭示了场景几何泛化、运动重定向精度等关键挑战。
- 结论：Mimicking-Bench 为通用化人形机器人-场景交互学习提供了首个全面基准，明确了未来研究方向。

## Overview
Learning generic skills for humanoid robots interacting with 3D scenes by mimicking human data is a key research challenge with significant implications for robotics and real-world applications. However, existing methodologies and benchmarks are constrained by the use of small-scale, manually collected demonstrations, lacking the general dataset and benchmark support necessary to explore scene geometry generalization effectively. To address this gap, we introduce Mimicking-Bench, the first comprehensive benchmark designed for generalizable humanoid-scene interaction learning through mimicking large-scale human animation references. Mimicking-Bench includes six household full-body humanoid-scene interaction tasks, covering 11K diverse object shapes, along with 20K synthetic and 3K real-world human interaction skill references. We construct a complete humanoid skill learning pipeline and benchmark approaches for motion retargeting, motion tracking, imitation learning, and their various combinations. Extensive experiments highlight the value of human mimicking for skill learning, revealing key challenges and research directions.

## 参考
- http://arxiv.org/abs/2412.17730v1

## 개요
Mimicking-Bench는 기존 방법들이 소규모 수동 수집 시연 데이터에 의존하여 장면 기하 일반화 능력이 부족한 문제를 해결하는 것을 목표로 합니다. 이 벤치마크는 6가지 유형의 가정용 전신 휴머노이드 로봇-장면 상호작용 작업을 포함하며, 11K개의 다양한 물체 형태를 다루고 20K개의 합성 및 3K개의 실제 세계 인간 상호작용 기술 참조를 제공합니다. 연구팀은 모션 리타게팅, 모션 추적, 모방 학습 및 이들의 조합 방법을 벤치마킹하는 완전한 휴머노이드 기술 학습 파이프라인을 구축했습니다. 광범위한 실험은 기술 학습에서 인간 모방의 가치를 드러내고, 핵심 과제와 연구 방향을 제시합니다.

## 핵심 내용
### 방법
- 핵심 아이디어: 대규모 인간 애니메이션 참조 데이터를 모방함으로써 휴머노이드 로봇이 3D 장면과 상호작용하는 일반 기술을 학습하게 하여, 전통적인 소규모 수동 시연 데이터의 장면 기하 일반화 한계를 극복합니다.
- 파이프라인: 인간 데이터에서 로봇 실행까지의 여러 단계를涵盖하는 완전한 휴머노이드 기술 학습 파이프라인을 구축했습니다.

### 아키텍처 및 실험 설정
- 작업: 6가지 유형의 가정용 전신 휴머노이드 로봇-장면 상호작용 작업을 포함하며, 11K개의 다양한 물체 형태를 다룹니다.
- 데이터: 20K개의 합성 인간 상호작용 기술 참조와 3K개의 실제 세계 인간 상호작용 기술 참조를 제공합니다.
- 벤치마크 방법: 모션 리타게팅, 모션 추적, 모방 학습 및 이들의 다양한 조합 방법을 체계적으로 평가합니다.

### 핵심 수치 및 결론
- 규모: 작업은 11K개의 물체 형태를 다루며, 데이터는 20K 합성 + 3K 실제 참조를 포함합니다.
- 실험 발견: 인간 모방은 기술 학습에 상당한 가치가 있으며, 장면 기하 일반화, 모션 리타게팅 정밀도 등의 핵심 과제를 드러냅니다.
- 결론: Mimicking-Bench는 일반화된 휴머노이드 로봇-장면 상호작용 학습을 위한 최초의 포괄적 벤치마크를 제공하며, 향후 연구 방향을 명확히 합니다.
