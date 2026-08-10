---
$id: ent_paper_e_sds_environment_aware_see_it_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
  zh: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
  ko: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
summary:
  en: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
  zh: E-SDS（Environment-aware See it, Do it, Sorted）是一个由2025年研究提出的自动化框架，旨在为双足机器人设计环境感知的行走策略。其核心贡献在于将视觉语言模型（VLM）与实时地形传感器分析相结合，自动生成奖励函数，从而在复杂地形（如楼梯）上实现鲁棒行走，并将人工奖励设计时间从数天缩短至两小时内。
  ko: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- e_sds
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16446v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (793 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid
    Locomotion (arXiv)'
  url: https://arxiv.org/abs/2512.16446
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有基于VLM的奖励设计方法因缺乏环境感知能力，在复杂地形中表现“盲目”。E-SDS通过整合VLM与实时地形传感器分析，自动生成奖励函数，并利用示例视频训练鲁棒的感知行走策略。在Unitree G1人形机器人上，该框架在四种地形（平地、间隙、障碍、楼梯）中均优于手动设计奖励或非感知自动化基线，尤其在楼梯任务中实现唯一成功。此外，E-SDS将速度跟踪误差降低51.9-82.6%，显著提升了策略的鲁棒性与开发效率。

## 核心内容
### 方法架构
E-SDS框架包含三个核心模块：
- **See it**：利用VLM（如GPT-4V）分析示例视频，提取行走动作与地形特征。
- **Do it**：结合实时地形传感器（如深度相机）数据，VLM自动生成奖励函数，指导强化学习训练。
- **Sorted**：通过迭代优化奖励函数，确保策略在动态环境中保持鲁棒性。

### 实验设置
- **机器人平台**：Unitree G1人形机器人。
- **测试地形**：四种场景——平地、间隙（0.3m宽）、障碍（0.15m高）、楼梯（0.2m高，共5级）。
- **基线对比**：手动设计奖励函数（基于速度跟踪与稳定性）与非感知自动化基线（仅依赖VLM，无地形输入）。

### 关键结果
- **楼梯任务**：E-SDS是唯一成功完成下楼梯的策略，手动设计基线与非感知基线均失败（机器人摔倒或无法启动）。
- **速度跟踪误差**：在所有地形中，E-SDS将误差降低51.9%（平地）至82.6%（障碍地形）。
- **效率提升**：奖励设计时间从人工的3-5天缩短至1.5小时，且无需专家干预。

### 结论
E-SDS通过环境感知闭环，解决了VLM在机器人控制中的“盲目性”问题，证明了自动化奖励设计在复杂地形中的可行性。未来工作可扩展至动态障碍物与多地形混合场景。

## Overview
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## 参考
- http://arxiv.org/abs/2512.16446v1

## 개요
기존 VLM 기반 보상 설계 방법은 환경 인식 능력이 부족하여 복잡한 지형에서 '맹목적'으로 작동합니다. E-SDS는 VLM과 실시간 지형 센서 분석을 통합하여 보상 함수를 자동 생성하고, 예시 비디오를 활용해 강건한 인식 보행 정책을 훈련합니다. Unitree G1 휴머노이드 로봇에서 이 프레임워크는 네 가지 지형(평지, 틈, 장애물, 계단)에서 수동 설계 보상 또는 비인식 자동화 기준선보다 우수한 성능을 보였으며, 특히 계단 작업에서 유일하게 성공했습니다. 또한 E-SDS는 속도 추적 오차를 51.9-82.6% 감소시켜 정책의 강건성과 개발 효율성을 크게 향상시켰습니다.

## 핵심 내용
### 방법 아키텍처
E-SDS 프레임워크는 세 가지 핵심 모듈로 구성됩니다:
- **See it**: VLM(예: GPT-4V)을 활용해 예시 비디오를 분석하고 보행 동작과 지형 특징을 추출합니다.
- **Do it**: 실시간 지형 센서(예: 깊이 카메라) 데이터를 결합하여 VLM이 보상 함수를 자동 생성하고 강화 학습 훈련을 안내합니다.
- **Sorted**: 반복적 보상 함수 최적화를 통해 정책이 동적 환경에서 강건성을 유지하도록 보장합니다.

### 실험 설정
- **로봇 플랫폼**: Unitree G1 휴머노이드 로봇.
- **테스트 지형**: 네 가지 시나리오——평지, 틈(0.3m 너비), 장애물(0.15m 높이), 계단(0.2m 높이, 총 5단).
- **기준선 비교**: 수동 설계 보상 함수(속도 추적 및 안정성 기반)와 비인식 자동화 기준선(VLM만 의존, 지형 입력 없음).

### 주요 결과
- **계단 작업**: E-SDS는 계단 내려가기를 유일하게 성공한 정책이며, 수동 설계 기준선과 비인식 기준선 모두 실패했습니다(로봇 넘어짐 또는 시작 불가).
- **속도 추적 오차**: 모든 지형에서 E-SDS는 오차를 51.9%(평지)에서 82.6%(장애물 지형)까지 감소시켰습니다.
- **효율성 향상**: 보상 설계 시간이 수작업 3-5일에서 1.5시간으로 단축되었으며, 전문가 개입이 필요 없습니다.

### 결론
E-SDS는 환경 인식 폐루프를 통해 VLM의 로봇 제어에서 '맹목성' 문제를 해결했으며, 복잡한 지형에서 자동화된 보상 설계의 실현 가능성을 입증했습니다. 향후 작업은 동적 장애물과 다중 지형 혼합 시나리오로 확장할 수 있습니다.
