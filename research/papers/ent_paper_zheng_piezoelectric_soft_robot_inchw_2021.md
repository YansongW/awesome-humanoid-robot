---
$id: ent_paper_zheng_piezoelectric_soft_robot_inchw_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through Robot Shape: Quasi-Static Modeling and Experimental
    Validation'
  zh: 通过机器人形状调节地面摩擦的压电软体机器人尺蠖运动：准静态建模与实验验证
  ko: '로봇 형상을 통한 지면 마찰 튜닝을 이용한 압전 소프트 로봇 인치웜 운동: 준정적 모델링 및 실험적 검증'
summary:
  en: Zheng et al. present a sub-millimeter-thick soft robot driven by five coordinated piezoelectric actuators on a steel
    foil substrate, using shape-controlled ground friction to achieve bidirectional inchworm crawling, and validate a gravity-inclusive
    Euler-Bernoulli quasi-static model against experiments.
  zh: Zheng 等人提出了一种厚度小于 0.5 毫米的软体机器人，通过协调五个压电致动器在钢箔基底上的驱动，利用形状控制地面摩擦实现双向尺蠖式爬行。研究还开发了包含重力的 Euler-Bernoulli 准静态模型，并通过实验验证了其有效性。
  ko: Zheng 등은 강박 기판 위에 5개의 압전 액추에이터를 조화롭게 구동하는 수백 마이크로미터 두께의 소프트 로봇을 제안하고, 형상에 의한 지면 마찰 제어로 양방향 인치웜 이동을 구현하며 중력을 포함한 Euler-Bernoulli
    준정적 모델을 실험으로 검증하였다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- piezoelectric_actuator
- pzt
- soft_robot
- inchworm_locomotion
- friction_tuning
- thin_film
- quasi_static_modeling
- ground_contact_modeling
- steel_foil
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2111.00944v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (603 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through Robot Shape: Quasi-Static Modeling and
    Experimental Validation'
  url: https://arxiv.org/abs/2111.00944
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究聚焦于基于压电致动器的电驱动软体机器人，旨在实现紧凑外形与复杂环境中的机动性。不同于以往单自由度控制，该工作通过协调五个独立压电致动器在金属箔上的协同作用，使机器人厚度不足 0.5 毫米。运动机制依赖于通过机器人形状控制地面摩擦：一端因形状变化被静摩擦锚定，其余部分则进行伸缩。研究建立了包含重力的完整解析模型，用于量化形状、摩擦与位移，并通过实验验证模型后，实现了机器人的双向尺蠖式前进与后退。

## 核心内容
### 方法与架构
- 机器人由五个独立压电致动器附着于钢箔基底构成，总厚度小于 0.5 毫米。
- 致动器协调激活，通过改变机器人整体形状来调节与地面的摩擦分布：特定形状下，一端因静摩擦锚定，另一端则实现伸缩，从而模拟尺蠖运动。

### 模型与实验
- 开发了基于 Euler-Bernoulli 梁理论的准静态模型，并首次将重力纳入分析，以精确计算机器人形状、摩擦力和位移。
- 实验验证了模型的有效性，确认了形状与摩擦控制的对应关系。

### 关键结果
- 通过序列化激活五个致动器，机器人成功实现了双向（前进与后退）尺蠖式爬行。
- 机器人厚度小于 0.5 毫米，展示了超薄软体机器人在受限空间中的运动潜力。

### 结论
该工作证明了通过多压电致动器协调控制形状来调节地面摩擦，是实现超薄软体机器人双向运动的有效策略，且准静态模型为后续设计提供了理论工具。

## Overview
Electrically-driven soft robots based on piezoelectric actuators may enable compact form factors and maneuverability in complex environments. In most prior work, piezoelectric actuators are used to control a single degree of freedom. In this work, the coordinated activation of five independent piezoelectric actuators, attached to a common metal foil, is used to implement inchworm-inspired crawling motion in a robot that is less than 0.5 mm thick. The motion is based on the control of its friction to the ground through the robot's shape, in which one end of the robot (depending on its shape) is anchored to the ground by static friction, while the rest of its body expands or contracts. A complete analytical model of the robot shape, which includes gravity, is developed to quantify the robot shape, friction, and displacement. After validation of the model by experiments, the robot's five actuators are collectively sequenced for inchworm-like forward and backward motion.

## 参考
- http://arxiv.org/abs/2111.00944v2

## 개요
이 연구는 압전 액추에이터 기반 전기 구동 소프트 로봇에 초점을 맞추며, 컴팩트한 외형과 복잡한 환경에서의 기동성을 목표로 한다. 기존의 단일 자유도 제어와 달리, 이 작업은 금속 호일 위에서 다섯 개의 독립적인 압전 액추에이터의 협력 작용을 조정하여 로봇의 두께를 0.5밀리미터 미만으로 만든다. 운동 메커니즘은 로봇의 형상을 통해 지면 마찰을 제어하는 데 의존한다: 한쪽 끝은 형상 변화로 인해 정지 마찰에 의해 고정되고, 나머지 부분은 신축을 수행한다. 연구는 중력을 포함한 완전한 해석 모델을 수립하여 형상, 마찰 및 변위를 정량화하고, 실험을 통해 모델을 검증한 후 로봇의 양방향 자벌레식 전진 및 후진을 구현했다.

## 핵심 내용
### 방법 및 아키텍처
- 로봇은 강철 호일 기판에 부착된 다섯 개의 독립적인 압전 액추에이터로 구성되며, 총 두께는 0.5밀리미터 미만이다.
- 액추에이터는 협력적으로 활성화되어 로봇의 전체 형상을 변경함으로써 지면과의 마찰 분포를 조절한다: 특정 형상에서 한쪽 끝은 정지 마찰로 고정되고, 다른 쪽 끝은 신축을 수행하여 자벌레 운동을 모사한다.

### 모델 및 실험
- Euler-Bernoulli 보 이론에 기반한 준정적 모델을 개발했으며, 중력을 처음으로 분석에 포함하여 로봇의 형상, 마찰력 및 변위를 정밀하게 계산했다.
- 실험을 통해 모델의 유효성을 검증하고, 형상과 마찰 제어 간의 대응 관계를 확인했다.

### 주요 결과
- 다섯 개의 액추에이터를 순차적으로 활성화함으로써 로봇은 양방향(전진 및 후진) 자벌레식 기어가기를 성공적으로 구현했다.
- 로봇의 두께는 0.5밀리미터 미만으로, 제한된 공간에서 초박형 소프트 로봇의 운동 가능성을 보여준다.

### 결론
이 작업은 다중 압전 액추에이터의 협력적 형상 제어를 통해 지면 마찰을 조절하는 것이 초박형 소프트 로봇의 양방향 운동을 구현하는 효과적인 전략임을 입증했으며, 준정적 모델은 향후 설계를 위한 이론적 도구를 제공한다.
