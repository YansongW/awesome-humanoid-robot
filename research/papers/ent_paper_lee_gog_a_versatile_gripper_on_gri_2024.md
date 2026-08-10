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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2401.10702v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (716 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2401.10702v1

## 개요
직물 조작은 재료가 쉽게 변형되고 크기와 형태가 다양하여 매우 도전적입니다. 기존 연구는 주로 이중 팔 로봇 시스템에 의존하지만, 이는 높은 비용과 복잡한 충돌 조정 문제를 초래합니다. G.O.G.는 새로운 엔드 이펙터 설계를 통해 기민성을 로봇 팔 조정에서 그리퍼 자체로 전환하는 대안을 제안합니다. 핵심은 최대 500mm까지 독립적으로 간격을 조절할 수 있는 외부 그리퍼이며, 외부 그리퍼의 두 손가락 자체도 그리퍼로, 가변 마찰 모듈이 통합되어 견고한 파지와 슬라이딩 파지의 두 가지 모드를 지원합니다. 실험은 가정용 물품과 직물 벤치마크를 사용하여 단일 팔 조건에서 다양한 양손 직물 조작 작업을 수행할 수 있는 이 설계의 잠재력을 검증했습니다.

## 핵심 내용
### 방법
- **G.O.G. 구조**: "그리퍼 위 그리퍼" 아키텍처를 채택하며, 외부 그리퍼는 두 손가락 사이의 간격(최대 500mm)을 독립적으로 제어할 수 있고, 이 두 손가락 자체가 가변 마찰 손가락 그리퍼입니다.
- **가변 마찰 모듈**: 각 손가락 그리퍼에는 가변 마찰 모듈이 통합되어 두 가지 파지 모드를 지원합니다:
  - **견고한 파지**: 안정적인 고정이 필요한 조작에 사용.
  - **슬라이딩 파지**: 직물이 손가락 사이에서 미끄러지도록 허용하여 자세 조정을 용이하게 함.

### 실험 설정
- **벤치마크 테스트**: 가정용 물품과 직물 조작의 두 가지 벤치마크를 사용하여 평가.
- **평가 내용**: 그리퍼 설계 자체에 대한 실험과 직물 조작 작업에 대한 실험을 포함.

### 주요 결과
- 실험은 G.O.G.가 단일 팔 조건에서 다양한 양손 직물 조작 작업을 수행할 수 있는 잠재력을 입증했습니다.
- 구체적인 작업에는 직물 펼치기, 접기 등 양손 협응이 필요한 동작이 포함되며 이에 국한되지 않습니다.
- 추가 자료와 데모 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다: https://sites.google.com/view/gripperongripper

### 결론
G.O.G.는 혁신적인 하드웨어 설계를 통해 이중 팔 시스템의 기민성 요구를 단일 팔 엔드 이펙터로 성공적으로 전환하여 저비용, 저복잡성 직물 조작을 위한 실현 가능한 솔루션을 제공합니다.
