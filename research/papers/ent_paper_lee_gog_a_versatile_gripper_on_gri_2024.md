---
$id: ent_paper_lee_gog_a_versatile_gripper_on_gri_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'G.O.G: A Versatile Gripper-On-Gripper Design for Bimanual Cloth Manipulation with a Single Robotic Arm'
  zh: G.O.G：用于单臂双手布料操作的 versatile 夹爪式夹爪设计
  ko: 'G.O.G: 단일 로봇 팔을 이용한 양손 천 조작을 위한 다목적 그리퍼-온-그리퍼 설계'
summary:
  en: Proposes G.O.G., a gripper-on-gripper end effector that enables bimanual cloth manipulation with a single robotic arm
    by combining a width-controlled outer gripper with two variable-friction finger grippers.
  zh: The manipulation of garments poses research challenges due to their deformable nature and the extensive variability
    in shapes and sizes. Despite numerous attempts by researchers to address these via approaches involving robot perception
    and control, there has been a relatively limited interest in resolving it through the co-development of robot hardware.
    Consequently, the majority of studies employ off-the-shelf grippers in conjunction with dual robot arms to enable bimanual
    manipulation and high dexterity. However, this dual-arm system increases the overall cost of the robotic system as well
  ko: 폭 조절 가능한 외부 그리퍼와 두 개의 가변 마찰 손가락 그리퍼를 결합하여 단일 로봇 팔로 양손 천 조작을 가능하게 하는 G.O.G. 엔드 이펙터를 제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.10702v1.
sources:
- id: src_001
  type: paper
  title: 'G.O.G: A Versatile Gripper-On-Gripper Design for Bimanual Cloth Manipulation with a Single Robotic Arm'
  url: https://arxiv.org/abs/2401.10702
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- system
---

## 概述
The manipulation of garments poses research challenges due to their deformable nature and the extensive variability in shapes and sizes. Despite numerous attempts by researchers to address these via approaches involving robot perception and control, there has been a relatively limited interest in resolving it through the co-development of robot hardware. Consequently, the majority of studies employ off-the-shelf grippers in conjunction with dual robot arms to enable bimanual manipulation and high dexterity. However, this dual-arm system increases the overall cost of the robotic system as well as its control complexity in order to tackle robot collisions and other robot coordination issues. As an alternative approach, we propose to enable bimanual cloth manipulation using a single robot arm via novel end effector design -- sharing dexterity skills between manipulator and gripper rather than relying entirely on robot arm coordination. To this end, we introduce a new gripper, called G.O.G., based on a gripper-on-gripper structure where the first gripper independently regulates the span, up to 500mm, between its fingers which are in turn also grippers. These finger grippers consist of a variable friction module that enables two grasping modes: firm and sliding grasps. Household item and cloth object benchmarks are employed to evaluate the performance of the proposed design, encompassing both experiments on the gripper design itself and on cloth manipulation. Experimental results demonstrate the potential of the introduced ideas to undertake a range of bimanual cloth manipulation tasks with a single robot arm. Supplementary material is available at https://sites.google.com/view/gripperongripper.

## 核心内容
The manipulation of garments poses research challenges due to their deformable nature and the extensive variability in shapes and sizes. Despite numerous attempts by researchers to address these via approaches involving robot perception and control, there has been a relatively limited interest in resolving it through the co-development of robot hardware. Consequently, the majority of studies employ off-the-shelf grippers in conjunction with dual robot arms to enable bimanual manipulation and high dexterity. However, this dual-arm system increases the overall cost of the robotic system as well as its control complexity in order to tackle robot collisions and other robot coordination issues. As an alternative approach, we propose to enable bimanual cloth manipulation using a single robot arm via novel end effector design -- sharing dexterity skills between manipulator and gripper rather than relying entirely on robot arm coordination. To this end, we introduce a new gripper, called G.O.G., based on a gripper-on-gripper structure where the first gripper independently regulates the span, up to 500mm, between its fingers which are in turn also grippers. These finger grippers consist of a variable friction module that enables two grasping modes: firm and sliding grasps. Household item and cloth object benchmarks are employed to evaluate the performance of the proposed design, encompassing both experiments on the gripper design itself and on cloth manipulation. Experimental results demonstrate the potential of the introduced ideas to undertake a range of bimanual cloth manipulation tasks with a single robot arm. Supplementary material is available at https://sites.google.com/view/gripperongripper.

## 参考
- http://arxiv.org/abs/2401.10702v1


