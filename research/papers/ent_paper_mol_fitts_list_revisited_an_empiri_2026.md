---
$id: ent_paper_mol_fitts_list_revisited_an_empiri_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fitts'' List Revisited: An Empirical Study on Function Allocation in a Two-Agent Physical Human-Robot Collaborative
    Position/Force Task'
  zh: 重新审视菲茨列表：双主体物理人机协作位置/力任务中功能分配的实证研究
  ko: '피츠 목록 재검토: 이중 주체 물리적 인간-로봇 협업 위치/력 작업에서 기능 할당에 대한 실증 연구'
summary:
  en: Empirically evaluates Fitts' List by allocating position and force control between a human and a robot in an abstract
    blending task, showing that assigning position control to the human and force control to the robot improves performance
    and user acceptance.
  zh: 本研究通过抽象混合任务中的人机位置/力控制分配实验，实证检验了Fitts' List在物理人机协作中的适用性。结果表明，将位置控制分配给人类、力控制分配给机器人可显著提升任务表现与用户接受度，同时揭示了监督角色与自主性感知的微妙权衡。
  ko: 추상적 블렌딩 작업에서 인간과 로봇 간 위치 및 힘 제어 할당을 통해 피츠 목록을 실증적으로 평가하였으며, 위치 제어를 인간에게, 힘 제어를 로봇에게 할당할 때 성능과 사용자 수용도가 향상됨을 보임.
domains:
- 05_mass_production
- 04_assembly_integration_testing
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- physical_human_robot_collaboration
- function_allocation
- fitts_list
- maba_maba
- shared_control
- position_force_control
- human_robot_interaction
- industry_5_0
- blending_task
- user_study
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.04722v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (700 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Fitts'' List Revisited: An Empirical Study on Function Allocation in a Two-Agent Physical Human-Robot Collaborative
    Position/Force Task'
  url: https://arxiv.org/abs/2505.04722
  date: '2026'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2025.3632607
theoretical_depth:
- method
---
## 概述
该研究以26名被试的组内设计实验，在抽象混合任务中测试了四种人机位置/力控制分配方案。核心发现是：当人类控制位置、机器人控制力时，过度混合现象显著减少，且用户在体力需求、系统接受度、自主性、参与度和挫败感等主观指标上表现更优。值得注意的是，机器人同时控制位置与力的监督角色在主观接受度中排名第二，而将位置控制交给机器人会显著降低用户的自主性感知。

## 核心内容
### 研究背景与目标
- 验证Fitts' List在物理人机协作中的适用性，为工业5.0中“增强而非替代工人”提供指导
- 假设人类控制位置时任务表现与用户评分更优

### 实验设计
- **被试**：26人，采用组内设计（within-subject design）
- **任务**：抽象混合任务，需同时控制位置与力
- **四种分配方案**：
  1. 人类控制位置+机器人控制力
  2. 机器人控制位置+人类控制力
  3. 人类同时控制位置与力
  4. 机器人同时控制位置与力（监督角色）

### 关键发现
- **性能指标**：人类控制位置+机器人控制力时，过度混合现象显著减少（p<0.05）
- **主观评价**：
  - 该方案在体力需求、系统接受度、自主性、参与度上评分最高，挫败感最低
  - 监督角色（机器人全控）在主观接受度中排名第二
  - 当机器人控制位置时，用户自主性感知显著低于机器人控制力时

### 结论
- 实证支持Fitts' List在静态功能分配中的有效性
- 揭示了关键的用户体验权衡：位置控制权下放会显著影响自主性感知，这对工业5.0的人机协作设计具有重要启示

## Overview
In this letter, we investigate whether classical function allocation-the principle of assigning tasks to either a human or a machine-holds for physical Human-Robot Collaboration, which is important for providing insights for Industry 5.0 to guide how to best augment rather than replace workers. This study empirically tests the applicability of Fitts' List within physical Human-Robot Collaboration, by conducting a user study (N=26, within-subject design) to evaluate four distinct allocations of position/force control between human and robot in an abstract blending task. We hypothesize that the function in which humans control the position achieves better performance and receives higher user ratings. When allocating position control to the human and force control to the robot, compared to the opposite case, we observed a significant improvement in preventing overblending. This was also perceived better in terms of physical demand and overall system acceptance, while participants experienced greater autonomy, more engagement and less frustration. An interesting insight was that the supervisory role (when the robot controls both position and force) was rated second best in terms of subjective acceptance. Another surprising insight was that if position control was delegated to the robot, the participants perceived much lower autonomy than when the force control was delegated to the robot. These findings empirically support applying Fitts' principles to static function allocation for physical collaboration, while also revealing important nuanced user experience trade-offs, particularly regarding perceived autonomy when delegating position control.

## Overview
In this letter, we investigate whether classical function allocation—the principle of assigning tasks to either a human or a machine—holds for physical Human-Robot Collaboration, which is important for providing insights for Industry 5.0 to guide how to best augment rather than replace workers. This study empirically tests the applicability of Fitts' List within physical Human-Robot Collaboration, by conducting a user study (N=26, within-subject design) to evaluate four distinct allocations of position/force control between human and robot in an abstract blending task. We hypothesize that the function in which humans control the position achieves better performance and receives higher user ratings. When allocating position control to the human and force control to the robot, compared to the opposite case, we observed a significant improvement in preventing overblending. This was also perceived better in terms of physical demand and overall system acceptance, while participants experienced greater autonomy, more engagement and less frustration. An interesting insight was that the supervisory role (when the robot controls both position and force) was rated second best in terms of subjective acceptance. Another surprising insight was that if position control was delegated to the robot, the participants perceived much lower autonomy than when the force control was delegated to the robot. These findings empirically support applying Fitts' principles to static function allocation for physical collaboration, while also revealing important nuanced user experience trade-offs, particularly regarding perceived autonomy when delegating position control.

## Content
In this letter, we investigate whether classical function allocation—the principle of assigning tasks to either a human or a machine—holds for physical Human-Robot Collaboration, which is important for providing insights for Industry 5.0 to guide how to best augment rather than replace workers. This study empirically tests the applicability of Fitts' List within physical Human-Robot Collaboration, by conducting a user study (N=26, within-subject design) to evaluate four distinct allocations of position/force control between human and robot in an abstract blending task. We hypothesize that the function in which humans control the position achieves better performance and receives higher user ratings. When allocating position control to the human and force control to the robot, compared to the opposite case, we observed a significant improvement in preventing overblending. This was also perceived better in terms of physical demand and overall system acceptance, while participants experienced greater autonomy, more engagement and less frustration. An interesting insight was that the supervisory role (when the robot controls both position and force) was rated second best in terms of subjective acceptance. Another surprising insight was that if position control was delegated to the robot, the participants perceived much lower autonomy than when the force control was delegated to the robot. These findings empirically support applying Fitts' principles to static function allocation for physical collaboration, while also revealing important nuanced user experience trade-offs, particularly regarding perceived autonomy when delegating position control.

## 参考
- http://arxiv.org/abs/2505.04722v2

## 개요
이 연구는 26명의 피험자를 대상으로 한 피험자 내 설계 실험에서 추상 혼합 과제를 통해 네 가지 인간-로봇 위치/힘 제어 할당 방안을 테스트했습니다. 핵심 발견은 인간이 위치를 제어하고 로봇이 힘을 제어할 때 과도한 혼합 현상이 유의미하게 감소했으며, 사용자의 신체적 요구, 시스템 수용도, 자율성, 참여도 및 좌절감과 같은 주관적 지표에서 더 우수한 성과를 보였다는 점입니다. 주목할 점은 로봇이 위치와 힘을 동시에 제어하는 감독 역할이 주관적 수용도에서 두 번째로 높았으며, 위치 제어를 로봇에 맡기는 경우 사용자의 자율성 인식이 유의미하게 감소한다는 것입니다.

## 핵심 내용
### 연구 배경 및 목표
- 물리적 인간-로봇 협업에서 Fitts' List의 적용 가능성을 검증하여 산업 5.0의 '근로자 대체가 아닌 강화'에 대한 지침 제공
- 인간이 위치를 제어할 때 과제 성과와 사용자 평가가 더 우수할 것이라는 가설

### 실험 설계
- **피험자**: 26명, 피험자 내 설계(within-subject design) 사용
- **과제**: 위치와 힘을 동시에 제어해야 하는 추상 혼합 과제
- **네 가지 할당 방안**:
  1. 인간이 위치 제어 + 로봇이 힘 제어
  2. 로봇이 위치 제어 + 인간이 힘 제어
  3. 인간이 위치와 힘을 동시에 제어
  4. 로봇이 위치와 힘을 동시에 제어(감독 역할)

### 핵심 발견
- **성능 지표**: 인간이 위치 제어 + 로봇이 힘 제어 시 과도한 혼합 현상이 유의미하게 감소(p<0.05)
- **주관적 평가**:
  - 해당 방안은 신체적 요구, 시스템 수용도, 자율성, 참여도에서 가장 높은 점수를 받았고 좌절감은 가장 낮음
  - 감독 역할(로봇 전면 제어)은 주관적 수용도에서 두 번째로 높음
  - 로봇이 위치를 제어할 때 사용자의 자율성 인식은 로봇이 힘을 제어할 때보다 유의미하게 낮음

### 결론
- 정적 기능 할당에서 Fitts' List의 유효성을 실증적으로 지지
- 핵심적인 사용자 경험 트레이드오프를 밝힘: 위치 제어 권한의 하양은 자율성 인식에 유의미한 영향을 미치며, 이는 산업 5.0의 인간-로봇 협업 설계에 중요한 시사점을 제공
