---
$id: ent_paper_cheng_navila_legged_robot_vision_lan_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation'
  zh: NaVILA
  ko: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation'
summary:
  en: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (NaVILA), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, USC, NVIDIA, and published at RSS25.'
  zh: NaVILA 是由 UC San Diego、USC、NVIDIA 于 2024 年提出的大型视觉-语言-动作模型，发表于 RSS25。其核心贡献在于将视觉-语言导航任务扩展到腿式机器人，通过两级框架将高层语言指令转化为低层腿部关节动作，显著提升了在复杂场景中的导航性能。
  ko: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (NaVILA), is a 2024 large vision-language-action model
    for robotic manipulation, introduced by UC San Diego, USC, NVIDIA, and published at RSS25.'
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
- navila
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.04453v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'NaVILA: Legged Robot Vision-Language-Action Model for Navigation (arXiv)'
  url: https://arxiv.org/abs/2412.04453
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NaVILA source
  url: https://doi.org/10.48550/arXiv.2412.04453
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
NaVILA 解决了腿式机器人在视觉-语言导航中的关键挑战：如何将人类语言指令直接映射到低层腿部关节动作。该模型采用两级框架，首先由 VLA 模型生成包含空间信息的中间层语言动作（如“向前移动 75cm”），再由视觉运动强化学习策略执行该动作。相比现有方法，NaVILA 在多个基准测试中取得显著提升，并在基于 IsaacLab 的新基准和真实机器人实验中验证了其优势。

## 核心内容
### 方法架构
NaVILA 采用两级框架：
- **第一级：VLA 模型**：将视觉输入与语言指令结合，生成中间层语言动作（如“向前移动 75cm”），包含空间信息而非直接输出低层关节动作。
- **第二级：视觉运动 RL 策略**：接收中间层语言动作作为输入，通过强化学习将其转化为低层腿部关节动作，实现实际导航。

### 实验设置
- **基准测试**：在现有导航基准上，NaVILA 显著优于此前方法。
- **新基准**：基于 IsaacLab 开发，包含更逼真的场景、低层控制以及真实机器人实验。
- **真实机器人实验**：验证了模型在真实环境中的有效性。

### 关键结果
- 在现有基准上，NaVILA 大幅提升导航成功率。
- 新基准中，模型在复杂场景下保持稳定性能。
- 真实机器人实验展示了从语言指令到实际导航的完整流程。

### 结论
NaVILA 通过两级框架有效解决了腿式机器人视觉-语言导航的难题，为未来机器人导航提供了灵活且鲁棒的解决方案。更多结果见项目主页：https://navila-bot.github.io/

## Overview
This paper proposes to solve the problem of Vision-and-Language Navigation with legged robots, which not only provides a flexible way for humans to command but also allows the robot to navigate through more challenging and cluttered scenes. However, it is non-trivial to translate human language instructions all the way to low-level leg joint actions. We propose NaVILA, a 2-level framework that unifies a Vision-Language-Action model (VLA) with locomotion skills. Instead of directly predicting low-level actions from VLA, NaVILA first generates mid-level actions with spatial information in the form of language, (e.g., "moving forward 75cm"), which serves as an input for a visual locomotion RL policy for execution. NaVILA substantially improves previous approaches on existing benchmarks. The same advantages are demonstrated in our newly developed benchmarks with IsaacLab, featuring more realistic scenes, low-level controls, and real-world robot experiments. We show more results at https://navila-bot.github.io/

## 개요
본 논문은 보행 로봇을 활용한 시각-언어 내비게이션 문제를 해결하는 방법을 제안합니다. 이는 인간이 명령을 내리는 유연한 방식을 제공할 뿐만 아니라, 로봇이 더 복잡하고 혼잡한 장면을 탐색할 수 있도록 합니다. 그러나 인간의 언어 명령을 저수준의 다리 관절 동작으로 완전히 변환하는 것은 쉽지 않습니다. 우리는 시각-언어-행동 모델(VLA)과 보행 기술을 통합하는 2단계 프레임워크인 NaVILA를 제안합니다. NaVILA는 VLA에서 저수준 동작을 직접 예측하는 대신, 먼저 공간 정보를 포함한 중간 수준의 동작을 언어 형태(예: "75cm 앞으로 이동")로 생성하며, 이는 시각적 보행 강화 학습 정책의 입력으로 사용되어 실행됩니다. NaVILA는 기존 벤치마크에서 이전 접근법을 크게 개선합니다. 이러한 장점은 IsaacLab을 사용하여 새롭게 개발한 벤치마크에서도 입증되었으며, 더 현실적인 장면, 저수준 제어, 실제 로봇 실험을 포함합니다. 더 많은 결과는 https://navila-bot.github.io/에서 확인할 수 있습니다.

## 핵심 내용
본 논문은 보행 로봇을 활용한 시각-언어 내비게이션 문제를 해결하는 방법을 제안합니다. 이는 인간이 명령을 내리는 유연한 방식을 제공할 뿐만 아니라, 로봇이 더 복잡하고 혼잡한 장면을 탐색할 수 있도록 합니다. 그러나 인간의 언어 명령을 저수준의 다리 관절 동작으로 완전히 변환하는 것은 쉽지 않습니다. 우리는 시각-언어-행동 모델(VLA)과 보행 기술을 통합하는 2단계 프레임워크인 NaVILA를 제안합니다. NaVILA는 VLA에서 저수준 동작을 직접 예측하는 대신, 먼저 공간 정보를 포함한 중간 수준의 동작을 언어 형태(예: "75cm 앞으로 이동")로 생성하며, 이는 시각적 보행 강화 학습 정책의 입력으로 사용되어 실행됩니다. NaVILA는 기존 벤치마크에서 이전 접근법을 크게 개선합니다. 이러한 장점은 IsaacLab을 사용하여 새롭게 개발한 벤치마크에서도 입증되었으며, 더 현실적인 장면, 저수준 제어, 실제 로봇 실험을 포함합니다. 더 많은 결과는 https://navila-bot.github.io/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2412.04453v2
