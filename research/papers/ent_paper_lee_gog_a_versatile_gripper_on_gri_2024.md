---
$id: ent_paper_lee_gog_a_versatile_gripper_on_gri_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'G.O.G: A Versatile Gripper-On-Gripper Design for Bimanual Cloth Manipulation
    with a Single Robotic Arm'
  zh: G.O.G：用于单臂双手布料操作的 versatile 夹爪式夹爪设计
  ko: 'G.O.G: 단일 로봇 팔을 이용한 양손 천 조작을 위한 다목적 그리퍼-온-그리퍼 설계'
summary:
  en: Proposes G.O.G., a gripper-on-gripper end effector that enables bimanual cloth
    manipulation with a single robotic arm by combining a width-controlled outer gripper
    with two variable-friction finger grippers.
  zh: 提出 G.O.G. 夹爪式夹爪末端执行器，通过将宽度可控的外层夹爪与两个可变摩擦指尖夹爪相结合，实现单臂双手布料操作。
  ko: 폭 조절 가능한 외부 그리퍼와 두 개의 가변 마찰 손가락 그리퍼를 결합하여 단일 로봇 팔로 양손 천 조작을 가능하게 하는 G.O.G. 엔드
    이펙터를 제안한다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- component
- system
tags:
- gripper_on_gripper
- bimanual_cloth_manipulation
- variable_friction_gripper
- width_control_gripper
- single_arm_manipulation
- cloth_manipulation
- garment_handling
- end_effector
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review required
    to confirm section-level citations and exact component specifications.
sources:
- id: src_001
  type: paper
  title: 'G.O.G: A Versatile Gripper-On-Gripper Design for Bimanual Cloth Manipulation
    with a Single Robotic Arm'
  url: https://arxiv.org/abs/2401.10702
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- system
---

## Overview

Garment manipulation is challenging because cloth is deformable and varies widely in shape and size. Most prior work addresses this with dual-arm robots using off-the-shelf grippers, which raises cost and complicates control due to collision avoidance and arm coordination. This paper proposes an alternative: achieve bimanual cloth manipulation with a single robot arm by adding dexterity at the end effector rather than through a second arm.

The proposed end effector, called G.O.G. (Gripper-On-Gripper), has two nested levels of grasping. A Width Control Gripper (WCG) forms the outer gripper and can adjust the span between its fingertips up to 500 mm. Each fingertip is itself a Variable Friction Gripper (VFG) that can switch between a high-friction firm grasp and a low-friction sliding grasp using a passive friction module. This structure lets one robot arm hold, tension, slide, and reposition cloth in ways normally requiring two arms.

The authors evaluate G.O.G. on household cloth objects and clothing items, testing both the gripper itself and full cloth-manipulation tasks such as folding, flattening, and hanging. The experiments compare performance against commercial grippers and demonstrate that a single arm with the proposed end effector can perform a range of bimanual cloth tasks.

## Key Contributions

- A gripper-on-gripper (G.O.G.) design that enables bimanual cloth manipulation with only one robot arm, sharing dexterity between the manipulator and the end effector.
- A Width Control Gripper (WCG) that adapts fingertip span up to 500 mm to accommodate a wide range of cloth sizes.
- Variable Friction Grippers (VFG) with a passive friction-switching module that supports firm grasp and sliding grasp modes.
- Experimental validation on household and clothing benchmarks showing folding, flattening, hanging, and competitive performance against commercial grippers.

## Relevance to Humanoid Robotics

Humanoid service robots are expected to perform household textile tasks such as folding laundry, hanging garments, and organizing cloth items. These tasks are typically bimanual, which in conventional approaches requires two robot arms and increases hardware cost, control complexity, and collision risk. By concentrating the required dexterity in a single-arm end effector, G.O.G. offers a lower-complexity hardware path for garment-care capabilities in humanoid robots.

The design is also relevant to component-level curation of humanoid end effectors: it combines width adaptation and variable friction in one gripper, two functions that are directly transferable to service robot hands. The limitation that very large cloths exceed the gripper opening is an important trade-off for humanoid applications involving bedsheets or large towels.
