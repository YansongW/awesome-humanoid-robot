---
$id: ent_paper_olaf_bringing_an_animated_char_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Olaf: Bringing an Animated Character to Life in the Physical World'
  zh: 'Olaf: Bringing an Animated Character to Life in the Physical World'
  ko: 'Olaf: Bringing an Animated Character to Life in the Physical World'
summary:
  en: 'Olaf: Bringing an Animated Character to Life in the Physical World is a 2025 work on hardware design for humanoid robots.'
  zh: Olaf 是一项 2025 年的人形机器人硬件设计工作，旨在将动画角色带入物理世界。其核心贡献在于通过强化学习与动画参考控制，结合非对称腿部隐藏、球形/平面连杆机构及温度感知策略，实现了高可信度的角色运动。关键参数包括软泡沫裙下的隐藏双腿、小型执行器驱动的头部与颈部，以及针对接触噪声和过热问题的奖励机制。
  ko: 'Olaf: Bringing an Animated Character to Life in the Physical World is a 2025 work on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- olaf
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16705v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Olaf: Bringing an Animated Character to Life in the Physical World (arXiv)'
  url: https://arxiv.org/abs/2512.16705
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究将动画角色 Olaf 实体化，利用强化学习结合动画参考进行控制，以解决非物理运动与异常比例带来的挑战。为营造角色双脚沿身体移动的视觉效果，团队在软泡沫裙下隐藏了两条非对称腿；同时采用球形与平面连杆机构驱动手臂、嘴巴和眼睛，以适应紧凑的机身空间。针对行走循环产生的刺耳接触声，研究引入了额外奖励以显著降低冲击噪声。此外，由于大头部由细颈内的小型执行器驱动，且服装加剧了过热风险，团队将温度值作为策略输入，并设计新奖励来约束执行器温度。仿真与硬件实验验证了该方法的有效性，展示了角色机器人前所未有的可信度。

## 核心内容
### 方法
- **控制框架**：基于强化学习，以动画参考作为引导，使机器人模仿动画角色的非物理运动风格。
- **机械设计**：
  - 在软泡沫裙下隐藏两条非对称腿，营造角色双脚沿身体移动的视觉错觉。
  - 手臂、嘴巴和眼睛采用球形与平面连杆机构，以适配角色内部的紧凑空间。
- **噪声抑制**：针对行走循环产生的硬接触声，引入额外奖励函数，显著降低冲击噪声。
- **热管理**：
  - 将执行器温度值作为策略的额外输入。
  - 设计新奖励项，确保执行器温度保持在安全范围内，避免因大头部与细颈结构导致的过热问题。

### 实验设置
- **仿真与硬件验证**：在仿真环境和真实硬件上分别测试模型的有效性。
- **评估指标**：以角色运动的可信度为主要衡量标准，对比传统方法。

### 关键数字与结论
- 通过隐藏双腿与连杆机构，实现了动画角色特有的非物理运动比例。
- 温度感知策略成功防止了执行器过热，尤其在服装加剧散热困难的场景下。
- 噪声奖励机制将接触声降低至可接受水平，提升了整体表现的真实感。
- 实验证明，该方法在成本角色机器人上达到了前所未有的可信度水平。

## Overview
Animated characters often move in non-physical ways and have proportions that are far from a typical walking robot. This provides an ideal platform for innovation in both mechanical design and stylized motion control. In this paper, we bring Olaf to life in the physical world, relying on reinforcement learning guided by animation references for control. To create the illusion of Olaf's feet moving along his body, we hide two asymmetric legs under a soft foam skirt. To fit actuators inside the character, we use spherical and planar linkages in the arms, mouth, and eyes. Because the walk cycle results in harsh contact sounds, we introduce additional rewards that noticeably reduce impact noise. The large head, driven by small actuators in the character's slim neck, creates a risk of overheating, amplified by the costume. To keep actuators from overheating, we feed temperature values as additional inputs to policies, introducing new rewards to keep them within bounds. We validate the efficacy of our modeling in simulation and on hardware, demonstrating an unmatched level of believability for a costumed robotic character.

## 개요
애니메이션 캐릭터는 종종 물리적이지 않은 방식으로 움직이며, 일반적인 보행 로봇과는 거리가 먼 비율을 가지고 있습니다. 이는 기계 설계와 양식화된 동작 제어 모두에서 혁신을 위한 이상적인 플랫폼을 제공합니다. 본 논문에서는 애니메이션 참조에 의해 안내되는 강화 학습을 제어에 활용하여 올라프를 물리적 세계에서 구현합니다. 올라프의 발이 몸을 따라 움직이는 듯한 착각을 만들기 위해, 두 개의 비대칭 다리를 부드러운 폼 스커트 아래에 숨깁니다. 캐릭터 내부에 액추에이터를 장착하기 위해, 팔, 입, 눈에 구형 및 평면 링키지를 사용합니다. 보행 주기가 거친 접촉음을 발생시키기 때문에, 충격 소음을 현저히 줄이는 추가 보상을 도입합니다. 캐릭터의 가느다란 목에 있는 작은 액추에이터에 의해 구동되는 큰 머리는 의상에 의해 증폭된 과열 위험을 초래합니다. 액추에이터의 과열을 방지하기 위해, 온도 값을 정책에 추가 입력으로 제공하고, 이를 허용 범위 내로 유지하기 위한 새로운 보상을 도입합니다. 우리는 시뮬레이션과 하드웨어에서 모델링의 효용성을 검증하여, 의상을 입은 로봇 캐릭터로서 비교할 수 없는 수준의 신뢰성을 입증합니다.

## 핵심 내용
애니메이션 캐릭터는 종종 물리적이지 않은 방식으로 움직이며, 일반적인 보행 로봇과는 거리가 먼 비율을 가지고 있습니다. 이는 기계 설계와 양식화된 동작 제어 모두에서 혁신을 위한 이상적인 플랫폼을 제공합니다. 본 논문에서는 애니메이션 참조에 의해 안내되는 강화 학습을 제어에 활용하여 올라프를 물리적 세계에서 구현합니다. 올라프의 발이 몸을 따라 움직이는 듯한 착각을 만들기 위해, 두 개의 비대칭 다리를 부드러운 폼 스커트 아래에 숨깁니다. 캐릭터 내부에 액추에이터를 장착하기 위해, 팔, 입, 눈에 구형 및 평면 링키지를 사용합니다. 보행 주기가 거친 접촉음을 발생시키기 때문에, 충격 소음을 현저히 줄이는 추가 보상을 도입합니다. 캐릭터의 가느다란 목에 있는 작은 액추에이터에 의해 구동되는 큰 머리는 의상에 의해 증폭된 과열 위험을 초래합니다. 액추에이터의 과열을 방지하기 위해, 온도 값을 정책에 추가 입력으로 제공하고, 이를 허용 범위 내로 유지하기 위한 새로운 보상을 도입합니다. 우리는 시뮬레이션과 하드웨어에서 모델링의 효용성을 검증하여, 의상을 입은 로봇 캐릭터로서 비교할 수 없는 수준의 신뢰성을 입증합니다.

## 参考
- http://arxiv.org/abs/2512.16705v2
