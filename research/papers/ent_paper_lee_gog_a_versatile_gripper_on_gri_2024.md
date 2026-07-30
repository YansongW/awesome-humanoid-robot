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
  zh: G.O.G. 是一种创新的“夹爪上夹爪”末端执行器，由单个机械臂即可实现双手布料操作。该设计通过一个宽度可控的外夹爪与两个可变摩擦手指夹爪组合而成，旨在降低传统双臂系统的成本与控制复杂度。实验表明，G.O.G. 能有效完成多种双手布料操作任务。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.10702v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
布料操作因材料易变形且尺寸形状多变而极具挑战性。现有研究多依赖双臂机器人系统，但这带来了高成本与复杂的碰撞协调问题。G.O.G. 提出了一种替代方案：通过新型末端执行器设计，将灵巧性从机械臂协调转移到夹爪本身。其核心是一个可独立调节跨度（最大500mm）的外夹爪，而外夹爪的两个手指本身也是夹爪，并集成了可变摩擦模块，支持牢固抓取和滑动抓取两种模式。实验采用家居物品和布料基准进行评估，验证了该设计在单臂条件下完成多种双手布料操作任务的潜力。

## 核心内容
### 方法
- **G.O.G. 结构**：采用“夹爪上夹爪”架构，外夹爪可独立控制其两个手指之间的跨度（最大500mm），而这两个手指本身即为可变摩擦手指夹爪。
- **可变摩擦模块**：每个手指夹爪集成了可变摩擦模块，支持两种抓取模式：
  - **牢固抓取**：用于需要稳定夹持的操作。
  - **滑动抓取**：允许布料在手指间滑动，便于调整姿态。

### 实验设置
- **基准测试**：使用家居物品和布料操作两类基准进行评估。
- **评估内容**：包括对夹爪设计本身的实验，以及对布料操作任务的实验。

### 关键结果
- 实验证明了 G.O.G. 在单臂条件下执行多种双手布料操作任务的潜力。
- 具体任务包括但不限于：布料展开、折叠等需要双手协调的动作。
- 补充材料与演示视频可在项目网站获取：https://sites.google.com/view/gripperongripper

### 结论
G.O.G. 通过创新的硬件设计，成功将双臂系统的灵巧性需求转移到单臂末端执行器上，为低成本、低复杂度的布料操作提供了可行方案。

## Overview
The manipulation of garments poses research challenges due to their deformable nature and the extensive variability in shapes and sizes. Despite numerous attempts by researchers to address these via approaches involving robot perception and control, there has been a relatively limited interest in resolving it through the co-development of robot hardware. Consequently, the majority of studies employ off-the-shelf grippers in conjunction with dual robot arms to enable bimanual manipulation and high dexterity. However, this dual-arm system increases the overall cost of the robotic system as well as its control complexity in order to tackle robot collisions and other robot coordination issues. As an alternative approach, we propose to enable bimanual cloth manipulation using a single robot arm via novel end effector design -- sharing dexterity skills between manipulator and gripper rather than relying entirely on robot arm coordination. To this end, we introduce a new gripper, called G.O.G., based on a gripper-on-gripper structure where the first gripper independently regulates the span, up to 500mm, between its fingers which are in turn also grippers. These finger grippers consist of a variable friction module that enables two grasping modes: firm and sliding grasps. Household item and cloth object benchmarks are employed to evaluate the performance of the proposed design, encompassing both experiments on the gripper design itself and on cloth manipulation. Experimental results demonstrate the potential of the introduced ideas to undertake a range of bimanual cloth manipulation tasks with a single robot arm. Supplementary material is available at https://sites.google.com/view/gripperongripper.

## 개요
의류 조작은 변형 가능한 특성과 다양한 형태 및 크기로 인해 연구 과제를 제기합니다. 연구자들이 로봇 인식 및 제어 접근법을 통해 이를 해결하려는 많은 시도가 있었지만, 로봇 하드웨어의 공동 개발을 통해 해결하려는 관심은 상대적으로 제한적이었습니다. 결과적으로 대부분의 연구는 기성 그리퍼를 이중 로봇 팔과 함께 사용하여 양손 조작과 높은 손재주를 가능하게 합니다. 그러나 이 이중 팔 시스템은 로봇 충돌 및 기타 로봇 조정 문제를 해결하기 위해 로봇 시스템의 전체 비용과 제어 복잡성을 증가시킵니다. 대안적인 접근법으로, 우리는 새로운 엔드 이펙터 설계를 통해 단일 로봇 팔을 사용한 양손 천 조작을 제안합니다. 이는 로봇 팔 조정에 전적으로 의존하지 않고 조작기와 그리퍼 간에 손재주 기술을 공유하는 방식입니다. 이를 위해 우리는 G.O.G.라는 새로운 그리퍼를 소개합니다. 이는 그리퍼-온-그리퍼 구조를 기반으로 하며, 첫 번째 그리퍼가 자체적으로 손가락(이 역시 그리퍼임) 사이의 간격을 최대 500mm까지 독립적으로 조절합니다. 이러한 손가락 그리퍼는 가변 마찰 모듈로 구성되어 두 가지 파지 모드(단단한 파지와 미끄러짐 파지)를 가능하게 합니다. 가정용 물체 및 천 객체 벤치마크를 사용하여 제안된 설계의 성능을 평가하며, 그리퍼 설계 자체와 천 조작에 대한 실험을 모두 포함합니다. 실험 결과는 단일 로봇 팔로 다양한 양손 천 조작 작업을 수행할 수 있는 도입된 아이디어의 잠재력을 보여줍니다. 추가 자료는 https://sites.google.com/view/gripperongripper에서 확인할 수 있습니다.

## 핵심 내용
의류 조작은 변형 가능한 특성과 다양한 형태 및 크기로 인해 연구 과제를 제기합니다. 연구자들이 로봇 인식 및 제어 접근법을 통해 이를 해결하려는 많은 시도가 있었지만, 로봇 하드웨어의 공동 개발을 통해 해결하려는 관심은 상대적으로 제한적이었습니다. 결과적으로 대부분의 연구는 기성 그리퍼를 이중 로봇 팔과 함께 사용하여 양손 조작과 높은 손재주를 가능하게 합니다. 그러나 이 이중 팔 시스템은 로봇 충돌 및 기타 로봇 조정 문제를 해결하기 위해 로봇 시스템의 전체 비용과 제어 복잡성을 증가시킵니다. 대안적인 접근법으로, 우리는 새로운 엔드 이펙터 설계를 통해 단일 로봇 팔을 사용한 양손 천 조작을 제안합니다. 이는 로봇 팔 조정에 전적으로 의존하지 않고 조작기와 그리퍼 간에 손재주 기술을 공유하는 방식입니다. 이를 위해 우리는 G.O.G.라는 새로운 그리퍼를 소개합니다. 이는 그리퍼-온-그리퍼 구조를 기반으로 하며, 첫 번째 그리퍼가 자체적으로 손가락(이 역시 그리퍼임) 사이의 간격을 최대 500mm까지 독립적으로 조절합니다. 이러한 손가락 그리퍼는 가변 마찰 모듈로 구성되어 두 가지 파지 모드(단단한 파지와 미끄러짐 파지)를 가능하게 합니다. 가정용 물체 및 천 객체 벤치마크를 사용하여 제안된 설계의 성능을 평가하며, 그리퍼 설계 자체와 천 조작에 대한 실험을 모두 포함합니다. 실험 결과는 단일 로봇 팔로 다양한 양손 천 조작 작업을 수행할 수 있는 도입된 아이디어의 잠재력을 보여줍니다. 추가 자료는 https://sites.google.com/view/gripperongripper에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2401.10702v1
