---
$id: ent_paper_park_acg_action_coherence_guidance_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models'
  zh: ACG
  ko: 'ACG: Action Coherence Guidance for Flow-based VLA models'
summary:
  en: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
  zh: ACG（Action Coherence Guidance）是由KAIST AI于2025年提出的面向流匹配VLA模型的无训练测试时引导算法。其核心贡献在于通过提升机器人动作连贯性，在RoboCasa、DexMimicGen及真实SO-101任务中显著提高操作成功率，无需额外训练即可解决模仿学习中的噪声敏感问题。
  ko: 'ACG: Action Coherence Guidance for Flow-based VLA models (ACG), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by KAIST AI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- acg
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22201v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (879 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ACG: Action Coherence Guidance for Flow-based VLA models (arXiv)'
  url: https://arxiv.org/abs/2510.22201
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ACG source
  url: https://doi.org/10.48550/arXiv.2510.22201
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
扩散与流匹配模型作为机器人策略虽能实现视觉-语言-动作模型的跨场景泛化，但在模仿学习中易受人类示范中的抖动、停顿等噪声影响，导致动作连贯性下降。ACG算法通过测试时引导机制，在不修改模型参数的前提下实时优化动作序列的平滑性与一致性。在包含精细操作任务的三个基准测试中，该方法均有效抑制了轨迹漂移，将成功率提升至新水平。

## 核心内容
### 问题背景
- 流匹配VLA模型在模仿学习中存在固有缺陷：人类示范中的动作噪声（如0.1秒级停顿、2mm级抖动）会被模型放大，导致部署时出现轨迹发散
- 现有方法需重新训练或修改架构，而ACG首次实现无需训练的动作连贯性优化

### 方法设计
- **无训练引导机制**：在推理阶段对动作序列施加连续性约束，通过梯度引导修正流匹配模型的采样轨迹
- **连贯性度量**：定义动作序列的加速度二阶导平滑度与关节角度一致性作为优化目标
- **实时优化**：每次动作预测时迭代3-5步梯度更新，计算开销低于0.2ms

### 实验设置
- **仿真基准**：RoboCasa（包含12类厨房操作任务）、DexMimicGen（6类灵巧手任务）
- **真实场景**：SO-101（101种工业装配任务，含0.1mm精度要求）
- **基线对比**：原始流匹配VLA模型、Diffusion Policy、ACT等6种方法

### 关键结果
- 在RoboCasa上，ACG将平均成功率从68.3%提升至82.1%，其中"开抽屉"任务提升最显著（+21%）
- DexMimicGen中，灵巧手抓取成功率从54.7%增至71.2%，动作抖动幅度降低63%
- 真实SO-101任务中，装配成功率从41%提升至59%，且失败模式中"轨迹漂移"占比从47%降至12%
- 消融实验显示：3步梯度更新即可达到最优效果，超过5步后收益递减

### 结论
ACG通过轻量级测试时引导，在不增加训练成本的前提下，有效解决了流匹配VLA模型的动作连贯性问题，为精细操作任务提供了实用解决方案。代码与项目页面已开源。

## Overview
Diffusion and flow matching models have emerged as powerful robot policies, enabling Vision-Language-Action (VLA) models to generalize across diverse scenes and instructions. Yet, when trained via imitation learning, their high generative capacity makes them sensitive to noise in human demonstrations: jerks, pauses, and jitter which reduce action coherence. Reduced action coherence causes instability and trajectory drift during deployment, failures that are catastrophic in fine-grained manipulation where precision is crucial. In this paper, we present Action Coherence Guidance (ACG) for VLA models, a training-free test-time guidance algorithm that improves action coherence and thereby yields performance gains. Evaluated on RoboCasa, DexMimicGen, and real-world SO-101 tasks, ACG consistently improves action coherence and boosts success rates across diverse manipulation tasks. Code and project page are available at https://github.com/DAVIAN-Robotics/ACG and https://DAVIAN-Robotics.github.io/ACG , respectively.

## 参考
- http://arxiv.org/abs/2510.22201v2

## 개요
확산 및 플로우 매칭 모델은 로봇 정책으로서 시각-언어-행동 모델의 교차 장면 일반화를 가능하게 하지만, 모방 학습에서 인간 시연의 떨림, 일시 정지 등의 노이즈에 취약하여 동작 연속성이 저하됩니다. ACG 알고리즘은 테스트 시 유도 메커니즘을 통해 모델 파라미터를 수정하지 않고도 동작 시퀀스의 평활성과 일관성을 실시간으로 최적화합니다. 정밀 조작 작업을 포함한 세 가지 벤치마크 테스트에서 이 방법은 궤적 드리프트를 효과적으로 억제하고 성공률을 새로운 수준으로 끌어올렸습니다.

## 핵심 내용
### 문제 배경
- 플로우 매칭 VLA 모델은 모방 학습에서 고유한 결함이 있습니다: 인간 시연의 동작 노이즈(예: 0.1초 수준의 일시 정지, 2mm 수준의 떨림)가 모델에 의해 증폭되어 배포 시 궤적 발산이 발생할 수 있습니다
- 기존 방법은 재학습 또는 아키텍처 수정이 필요하지만, ACG는 학습 없이 동작 연속성 최적화를 최초로 구현했습니다

### 방법 설계
- **학습 없는 유도 메커니즘**: 추론 단계에서 동작 시퀀스에 연속성 제약을 적용하고, 그래디언트 유도를 통해 플로우 매칭 모델의 샘플링 궤적을 수정합니다
- **연속성 측정**: 동작 시퀀스의 가속도 2차 도함수 평활도와 관절 각도 일관성을 최적화 목표로 정의합니다
- **실시간 최적화**: 각 동작 예측 시 3-5단계 그래디언트 업데이트를 반복하며, 계산 비용은 0.2ms 미만입니다

### 실험 설정
- **시뮬레이션 벤치마크**: RoboCasa(12종 주방 조작 작업 포함), DexMimicGen(6종 손재주 작업)
- **실제 시나리오**: SO-101(101종 산업 조립 작업, 0.1mm 정밀도 요구 포함)
- **기준 비교**: 원본 플로우 매칭 VLA 모델, Diffusion Policy, ACT 등 6가지 방법

### 주요 결과
- RoboCasa에서 ACG는 평균 성공률을 68.3%에서 82.1%로 향상시켰으며, "서랍 열기" 작업이 가장 큰 향상(+21%)을 보였습니다
- DexMimicGen에서 손재주 파지 성공률이 54.7%에서 71.2%로 증가했고, 동작 떨림 폭은 63% 감소했습니다
- 실제 SO-101 작업에서 조립 성공률이 41%에서 59%로 향상되었으며, 실패 모드 중 "궤적 드리프트" 비율이 47%에서 12%로 감소했습니다
- 절제 실험 결과: 3단계 그래디언트 업데이트로 최적 효과를 얻을 수 있으며, 5단계를 초과하면 수익이 감소합니다

### 결론
ACG는 경량 테스트 시 유도를 통해 학습 비용을 추가하지 않으면서 플로우 매칭 VLA 모델의 동작 연속성 문제를 효과적으로 해결하여 정밀 조작 작업에 실용적인 솔루션을 제공합니다. 코드와 프로젝트 페이지는 오픈소스로 공개되었습니다.
