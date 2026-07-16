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

## Overview
The manipulation of garments poses research challenges due to their deformable nature and the extensive variability in shapes and sizes. Despite numerous attempts by researchers to address these via approaches involving robot perception and control, there has been a relatively limited interest in resolving it through the co-development of robot hardware. Consequently, the majority of studies employ off-the-shelf grippers in conjunction with dual robot arms to enable bimanual manipulation and high dexterity. However, this dual-arm system increases the overall cost of the robotic system as well as its control complexity in order to tackle robot collisions and other robot coordination issues. As an alternative approach, we propose to enable bimanual cloth manipulation using a single robot arm via novel end effector design -- sharing dexterity skills between manipulator and gripper rather than relying entirely on robot arm coordination. To this end, we introduce a new gripper, called G.O.G., based on a gripper-on-gripper structure where the first gripper independently regulates the span, up to 500mm, between its fingers which are in turn also grippers. These finger grippers consist of a variable friction module that enables two grasping modes: firm and sliding grasps. Household item and cloth object benchmarks are employed to evaluate the performance of the proposed design, encompassing both experiments on the gripper design itself and on cloth manipulation. Experimental results demonstrate the potential of the introduced ideas to undertake a range of bimanual cloth manipulation tasks with a single robot arm. Supplementary material is available at https://sites.google.com/view/gripperongripper.

## Content
The manipulation of garments poses research challenges due to their deformable nature and the extensive variability in shapes and sizes. Despite numerous attempts by researchers to address these via approaches involving robot perception and control, there has been a relatively limited interest in resolving it through the co-development of robot hardware. Consequently, the majority of studies employ off-the-shelf grippers in conjunction with dual robot arms to enable bimanual manipulation and high dexterity. However, this dual-arm system increases the overall cost of the robotic system as well as its control complexity in order to tackle robot collisions and other robot coordination issues. As an alternative approach, we propose to enable bimanual cloth manipulation using a single robot arm via novel end effector design -- sharing dexterity skills between manipulator and gripper rather than relying entirely on robot arm coordination. To this end, we introduce a new gripper, called G.O.G., based on a gripper-on-gripper structure where the first gripper independently regulates the span, up to 500mm, between its fingers which are in turn also grippers. These finger grippers consist of a variable friction module that enables two grasping modes: firm and sliding grasps. Household item and cloth object benchmarks are employed to evaluate the performance of the proposed design, encompassing both experiments on the gripper design itself and on cloth manipulation. Experimental results demonstrate the potential of the introduced ideas to undertake a range of bimanual cloth manipulation tasks with a single robot arm. Supplementary material is available at https://sites.google.com/view/gripperongripper.

## 개요
의류 조작은 변형 가능한 특성과 다양한 형태 및 크기로 인해 연구 과제를 제기합니다. 연구자들이 로봇 인식 및 제어 접근법을 통해 이를 해결하려는 많은 시도가 있었지만, 로봇 하드웨어의 공동 개발을 통해 해결하려는 관심은 상대적으로 제한적이었습니다. 결과적으로 대부분의 연구는 기성 그리퍼를 이중 로봇 팔과 함께 사용하여 양손 조작과 높은 손재주를 가능하게 합니다. 그러나 이 이중 팔 시스템은 로봇 충돌 및 기타 로봇 조정 문제를 해결하기 위해 로봇 시스템의 전체 비용과 제어 복잡성을 증가시킵니다. 대안적인 접근법으로, 우리는 새로운 엔드 이펙터 설계를 통해 단일 로봇 팔을 사용한 양손 천 조작을 제안합니다. 이는 로봇 팔 조정에 전적으로 의존하지 않고 조작기와 그리퍼 간에 손재주 기술을 공유하는 방식입니다. 이를 위해 우리는 G.O.G.라는 새로운 그리퍼를 소개합니다. 이는 그리퍼-온-그리퍼 구조를 기반으로 하며, 첫 번째 그리퍼가 자체적으로 손가락(이 역시 그리퍼임) 사이의 간격을 최대 500mm까지 독립적으로 조절합니다. 이러한 손가락 그리퍼는 가변 마찰 모듈로 구성되어 두 가지 파지 모드(단단한 파지와 미끄러짐 파지)를 가능하게 합니다. 가정용 물체 및 천 객체 벤치마크를 사용하여 제안된 설계의 성능을 평가하며, 그리퍼 설계 자체와 천 조작에 대한 실험을 모두 포함합니다. 실험 결과는 단일 로봇 팔로 다양한 양손 천 조작 작업을 수행할 수 있는 도입된 아이디어의 잠재력을 보여줍니다. 추가 자료는 https://sites.google.com/view/gripperongripper에서 확인할 수 있습니다.

## 핵심 내용
의류 조작은 변형 가능한 특성과 다양한 형태 및 크기로 인해 연구 과제를 제기합니다. 연구자들이 로봇 인식 및 제어 접근법을 통해 이를 해결하려는 많은 시도가 있었지만, 로봇 하드웨어의 공동 개발을 통해 해결하려는 관심은 상대적으로 제한적이었습니다. 결과적으로 대부분의 연구는 기성 그리퍼를 이중 로봇 팔과 함께 사용하여 양손 조작과 높은 손재주를 가능하게 합니다. 그러나 이 이중 팔 시스템은 로봇 충돌 및 기타 로봇 조정 문제를 해결하기 위해 로봇 시스템의 전체 비용과 제어 복잡성을 증가시킵니다. 대안적인 접근법으로, 우리는 새로운 엔드 이펙터 설계를 통해 단일 로봇 팔을 사용한 양손 천 조작을 제안합니다. 이는 로봇 팔 조정에 전적으로 의존하지 않고 조작기와 그리퍼 간에 손재주 기술을 공유하는 방식입니다. 이를 위해 우리는 G.O.G.라는 새로운 그리퍼를 소개합니다. 이는 그리퍼-온-그리퍼 구조를 기반으로 하며, 첫 번째 그리퍼가 자체적으로 손가락(이 역시 그리퍼임) 사이의 간격을 최대 500mm까지 독립적으로 조절합니다. 이러한 손가락 그리퍼는 가변 마찰 모듈로 구성되어 두 가지 파지 모드(단단한 파지와 미끄러짐 파지)를 가능하게 합니다. 가정용 물체 및 천 객체 벤치마크를 사용하여 제안된 설계의 성능을 평가하며, 그리퍼 설계 자체와 천 조작에 대한 실험을 모두 포함합니다. 실험 결과는 단일 로봇 팔로 다양한 양손 천 조작 작업을 수행할 수 있는 도입된 아이디어의 잠재력을 보여줍니다. 추가 자료는 https://sites.google.com/view/gripperongripper에서 확인할 수 있습니다.
