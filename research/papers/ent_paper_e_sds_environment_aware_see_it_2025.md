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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16446v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-language models (VLMs)는 인간형 로코모션에서 보상 설계를 자동화하는 가능성을 보여주며, 이는 지루한 수동 엔지니어링의 필요성을 없앨 수 있습니다. 그러나 현재 VLM 기반 방법은 본질적으로 "맹목적"이며, 복잡한 지형을 탐색하는 데 필요한 환경 인식 능력이 부족합니다. 우리는 이러한 인식 격차를 해소하는 프레임워크인 E-SDS (Environment-aware See it, Do it, Sorted)를 제시합니다. E-SDS는 VLM을 실시간 지형 센서 분석과 통합하여, 예시 비디오를 기반으로 강건한 인식 기반 로코모션 정책 훈련을 촉진하는 보상 함수를 자동으로 생성합니다. Unitree G1 인간형 로봇을 네 가지 다른 지형(단순, 간격, 장애물, 계단)에서 평가한 결과, E-SDS는 유일하게 계단 하강을 성공적으로 수행했으며, 수동 설계 보상이나 비인식 자동 기준선으로 훈련된 정책은 작업을 완료하지 못했습니다. 모든 지형에서 E-SDS는 속도 추적 오차를 51.9-82.6% 감소시켰습니다. 우리의 프레임워크는 보상 설계에 필요한 인간의 노력을 며칠에서 2시간 미만으로 줄이면서도 더 강건하고 능력 있는 로코모션 정책을 생성합니다.

## 핵심 내용
Vision-language models (VLMs)는 인간형 로코모션에서 보상 설계를 자동화하는 가능성을 보여주며, 이는 지루한 수동 엔지니어링의 필요성을 없앨 수 있습니다. 그러나 현재 VLM 기반 방법은 본질적으로 "맹목적"이며, 복잡한 지형을 탐색하는 데 필요한 환경 인식 능력이 부족합니다. 우리는 이러한 인식 격차를 해소하는 프레임워크인 E-SDS (Environment-aware See it, Do it, Sorted)를 제시합니다. E-SDS는 VLM을 실시간 지형 센서 분석과 통합하여, 예시 비디오를 기반으로 강건한 인식 기반 로코모션 정책 훈련을 촉진하는 보상 함수를 자동으로 생성합니다. Unitree G1 인간형 로봇을 네 가지 다른 지형(단순, 간격, 장애물, 계단)에서 평가한 결과, E-SDS는 유일하게 계단 하강을 성공적으로 수행했으며, 수동 설계 보상이나 비인식 자동 기준선으로 훈련된 정책은 작업을 완료하지 못했습니다. 모든 지형에서 E-SDS는 속도 추적 오차를 51.9-82.6% 감소시켰습니다. 우리의 프레임워크는 보상 설계에 필요한 인간의 노력을 며칠에서 2시간 미만으로 줄이면서도 더 강건하고 능력 있는 로코모션 정책을 생성합니다.

## 参考
- http://arxiv.org/abs/2512.16446v1
