---
$id: ent_paper_ficht_online_balanced_motion_generat_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Online Balanced Motion Generation for Humanoid Robots
  zh: 人形机器人在线平衡运动生成
  ko: 휴머노이드 로봇을 위한 온라인 균형 모션 생성
summary:
  en: Proposes an analytic whole-body motion generator for low-cost humanoid robots with position-controlled joints and limited
    sensing, approximating the body and limbs with triangle centroid masses and representing the full pose as a five point-mass
    inverted pendulum; validated on the igus Humanoid Open Platform with balanced posing, kicking, and simple PD feedback.
  zh: 提出了一种面向低成本、位置控制关节且传感能力有限的人形机器人的解析全身运动生成方法，该方法用三角形质心质量近似身体和肢体，并将全身姿态表示为五个质点的倒立摆；在 igus 人形开放平台（igus Humanoid Open Platform）上通过平衡姿态、踢球动作和简单
    PD 反馈进行了验证。
  ko: 위치 제어 관절과 제한된 센서를 갖춘 저비용 휴머노이드 로봇을 위한 해석적 전신 모션 생성 기법을 제안하며, 몸통과 사지를 삼각형 중심 질량으로 근사하고 전체 자세를 5개 점질량으로 된 역진자 모델로 표현;
    igus Humanoid Open Platform에서 균형 자세, 킥킹 동작 및 단순 PD 피드백으로 검증되었다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
- 06_design_engineering
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_motion_generation
- inverted_pendulum_model
- triangle_centroid_mass
- static_balance
- position_controlled_joints
- low_cost_humanoid
- com_tracking
- quasi_static_motion
- pd_stabilization
- igus_humanoid_open_platform
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1810.08388v1.
sources:
- id: src_001
  type: paper
  title: Online Balanced Motion Generation for Humanoid Robots
  url: https://arxiv.org/abs/1810.08388
  date: '2018'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Reducing the complexity of higher order problems can enable solving them in analytical ways. In this paper, we propose an analytic whole body motion generator for humanoid robots. Our approach targets inexpensive platforms that possess position controlled joints and have limited feedback capabilities. By analysing the mass distribution in a humanoid-like body, we find relations between limb movement and their respective CoM positions. A full pose of a humanoid robot is then described with five point-masses, with one attached to the trunk and the remaining four assigned to each limb. The weighted sum of these masses in combination with a contact point form an inverted pendulum. We then generate statically stable poses by specifying a desired upright pendulum orientation, and any desired trunk orientation. Limb and trunk placement strategies are utilised to meet the reference CoM position. A set of these poses is interpolated to achieve stable whole body motions. The approach is evaluated by performing several motions with an igus Humanoid Open Platform robot. We demonstrate the extendability of the approach by applying basic feedback mechanisms for disturbance rejection and tracking error minimisation.

## 核心内容
Reducing the complexity of higher order problems can enable solving them in analytical ways. In this paper, we propose an analytic whole body motion generator for humanoid robots. Our approach targets inexpensive platforms that possess position controlled joints and have limited feedback capabilities. By analysing the mass distribution in a humanoid-like body, we find relations between limb movement and their respective CoM positions. A full pose of a humanoid robot is then described with five point-masses, with one attached to the trunk and the remaining four assigned to each limb. The weighted sum of these masses in combination with a contact point form an inverted pendulum. We then generate statically stable poses by specifying a desired upright pendulum orientation, and any desired trunk orientation. Limb and trunk placement strategies are utilised to meet the reference CoM position. A set of these poses is interpolated to achieve stable whole body motions. The approach is evaluated by performing several motions with an igus Humanoid Open Platform robot. We demonstrate the extendability of the approach by applying basic feedback mechanisms for disturbance rejection and tracking error minimisation.

## 参考
- http://arxiv.org/abs/1810.08388v1

