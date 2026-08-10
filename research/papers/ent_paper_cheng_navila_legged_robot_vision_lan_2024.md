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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.04453v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (681 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2412.04453v2

## 개요
NaVILA는 보행 로봇의 시각-언어 내비게이션에서 핵심 과제를 해결합니다: 인간의 언어 명령을 저수준 다리 관절 동작으로 직접 매핑하는 방법입니다. 이 모델은 2단계 프레임워크를 채택하며, 먼저 VLA 모델이 공간 정보를 포함한 중간 수준 언어 동작(예: "앞으로 75cm 이동")을 생성하고, 그 다음 시각 운동 강화 학습 정책이 해당 동작을 실행합니다. 기존 방법과 비교하여 NaVILA는 여러 벤치마크에서 현저한 향상을 보였으며, IsaacLab 기반의 새로운 벤치마크와 실제 로봇 실험에서 그 우수성을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
NaVILA는 2단계 프레임워크를 채택합니다:
- **1단계: VLA 모델**: 시각 입력과 언어 명령을 결합하여 중간 수준 언어 동작(예: "앞으로 75cm 이동")을 생성하며, 저수준 관절 동작을 직접 출력하는 대신 공간 정보를 포함합니다.
- **2단계: 시각 운동 RL 정책**: 중간 수준 언어 동작을 입력으로 받아 강화 학습을 통해 저수준 다리 관절 동작으로 변환하여 실제 내비게이션을 구현합니다.

### 실험 설정
- **벤치마크 테스트**: 기존 내비게이션 벤치마크에서 NaVILA는 이전 방법보다 현저히 우수했습니다.
- **새로운 벤치마크**: IsaacLab 기반으로 개발되었으며, 더 현실적인 장면, 저수준 제어 및 실제 로봇 실험을 포함합니다.
- **실제 로봇 실험**: 실제 환경에서 모델의 효과성을 검증했습니다.

### 주요 결과
- 기존 벤치마크에서 NaVILA는 내비게이션 성공률을 크게 향상시켰습니다.
- 새로운 벤치마크에서 모델은 복잡한 장면에서도 안정적인 성능을 유지했습니다.
- 실제 로봇 실험은 언어 명령에서 실제 내비게이션까지의 완전한 흐름을 보여주었습니다.

### 결론
NaVILA는 2단계 프레임워크를 통해 보행 로봇의 시각-언어 내비게이션 문제를 효과적으로 해결하며, 미래 로봇 내비게이션에 유연하고 견고한 솔루션을 제공합니다. 더 많은 결과는 프로젝트 홈페이지에서 확인하세요: https://navila-bot.github.io/
