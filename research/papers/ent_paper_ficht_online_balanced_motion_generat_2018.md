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
  en: Proposes an analytic whole-body motion generator for low-cost humanoid robots
    with position-controlled joints and limited sensing, approximating the body and
    limbs with triangle centroid masses and representing the full pose as a five point-mass
    inverted pendulum; validated on the igus Humanoid Open Platform with balanced
    posing, kicking, and simple PD feedback.
  zh: 提出了一种面向低成本、位置控制关节且传感能力有限的人形机器人的解析全身运动生成方法，该方法用三角形质心质量近似身体和肢体，并将全身姿态表示为五个质点的倒立摆；在
    igus 人形开放平台（igus Humanoid Open Platform）上通过平衡姿态、踢球动作和简单 PD 反馈进行了验证。
  ko: 위치 제어 관절과 제한된 센서를 갖춘 저비용 휴머노이드 로봇을 위한 해석적 전신 모션 생성 기법을 제안하며, 몸통과 사지를 삼각형 중심
    질량으로 근사하고 전체 자세를 5개 점질량으로 된 역진자 모델로 표현; igus Humanoid Open Platform에서 균형 자세, 킥킹
    동작 및 단순 PD 피드백으로 검증되었다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the full arXiv source (v1, 2018-10-19); requires human
    review before final verification. DOI is not provided in the source.
sources:
- id: src_001
  type: paper
  title: Online Balanced Motion Generation for Humanoid Robots
  url: https://arxiv.org/abs/1810.08388
  date: '2018'
  accessed_at: '2026-06-26'
---


## Overview

The paper addresses whole-body motion generation for humanoid robots that cannot afford expensive torque-controlled hardware and rich sensing. It proposes an analytic, geometric method that reduces the robot's kinematic and mass model to a set of triangles—one for the trunk and one for each limb—whose centroids encode the center of mass (CoM) of the corresponding body part. A full static pose is then represented by five point masses (trunk plus four limbs), whose weighted sum together with a single ground contact point forms an inverted pendulum. By constraining the pendulum to an upright orientation, the generated poses are inherently statically stable.

The method introduces projected pitch and roll angles to decompose the 3D pendulum orientation into independent 2D problems. Given a desired upright pendulum orientation, a desired trunk orientation, and desired foot positions, analytical limb and trunk placement strategies compute the joint configurations needed to place the whole-body CoM at the reference position. Arm placement also compensates for residual CoM errors within the arms' reachable ranges. Statically stable keyframes are linearly interpolated (with spherical interpolation for the nonlinear projected angles) to produce whole-body motions at runtime, assuming dynamic effects are negligible for slow movements.

The approach is calibrated once from a CAD model of the igus Humanoid Open Platform to obtain body lengths, masses, and the mass distribution parameters for each triangle. Validation compares the triangle-based CoM estimate against the robot's URDF model and demonstrates balanced standing, trunk-tilt, single-leg support, and kicking motions on the real robot. A simple PD feedback loop on the pendulum roll, pitch, and length is added to reject disturbances and reduce CoM tracking errors.

## Key Contributions

- An analytic whole-body motion generation method that avoids numerical optimization by using triangle centroid mass models.
- A five point-mass inverted pendulum representation of a humanoid pose (one trunk mass plus one mass per limb) that links limb motion to whole-body CoM position.
- Analytical limb, trunk, foot, and arm placement strategies for placing the whole-body CoM at a desired reference location.
- Runtime interpolation of statically stable keyframes into whole-body motions using projected angles.
- Experimental validation on the igus Humanoid Open Platform, including balanced posing and a dynamic kicking motion, with simple PD stabilisation for disturbance rejection and tracking-error reduction.

## Relevance to Humanoid Robotics

The work is directly relevant to the cost-effective mass production and deployment of humanoid robots. Most state-of-the-art whole-body control methods assume torque-controlled actuators, high-rate control loops, and rich force/torque feedback, which are incompatible with inexpensive, position-controlled platforms. By providing an analytic, low-complexity balance and motion generation method that needs only a 6-axis IMU and joint positions, the paper lowers the hardware and sensing barriers for stable humanoid locomotion and manipulation. This makes it especially pertinent to affordable, large-scale humanoid systems intended for research, education, and light-service applications.
