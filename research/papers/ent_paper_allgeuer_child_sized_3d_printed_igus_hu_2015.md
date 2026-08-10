---
$id: ent_paper_allgeuer_child_sized_3d_printed_igus_hu_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Child-sized 3D Printed igus Humanoid Open Platform
  zh: 儿童尺寸3D打印igus人形开放平台
  ko: 어린이 크기의 3D 프린팅 igus 휴머노이드 오픈 플랫폼
summary:
  en: Presents the igus Humanoid Open Platform, a 90 cm child-sized, low-cost, fully 3D-printed humanoid robot with open-source
    ROS software, and reports its mechanical/electrical design and dynamic-motion demonstrations.
  zh: 本文介绍了igus Humanoid Open Platform，一款90厘米高、低成本、完全3D打印的儿童尺寸人形机器人，其开源ROS软件已发布。该平台旨在降低人形机器人研究门槛，并展示了其机械/电气设计与动态运动演示。
  ko: 90cm 높이의 저비용 완전 3D 프린팅 어린이 크기 휴머노이드 로봇인 igus 휴머노이드 오픈 플랫폼을 소개하고, 오픈소스 ROS 소프트웨어와 기계/전기 설계 및 동적 동작 시연을 보고한다.
domains:
- 06_design_engineering
- 03_manufacturing_processes
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
tags:
- igus_humanoid_open_platform
- 3d_printed_humanoid
- child_sized_robot
- open_source_hardware
- ros
- dynamixel
- fused_angles
- omnidirectional_walking
- robocup
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.10701v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (664 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Child-sized 3D Printed igus Humanoid Open Platform
  url: https://arxiv.org/abs/1809.10701
  date: '2015'
  accessed_at: '2026-06-28'
theoretical_depth:
- system
- method
---
## 概述
在人形机器人领域，标准平台能加速研究并降低新团队的入门难度。现有60厘米以下的低成本平台较多，但更大尺寸的平台往往价格昂贵且难以维护。本文提出的igus Humanoid Open Platform填补了这一空白：它是一款90厘米高、成本可控、易于定制的人形机器人标准平台。该机器人完全采用3D打印制造，重量轻且外观吸引人，具备足够的扭矩和计算能力，可支持多种研究方向。论文详细介绍了其机械与电气设计，并讨论了配套开源ROS软件的主要功能，所有3D CAD文件均已开源发布。

## 核心内容
### 背景与动机
- 人形机器人标准平台可加速研究，但现有60厘米以上平台成本高、操作维护困难。
- 需要一款儿童尺寸（约90厘米）、低成本、易维护且可定制的开源平台。

### 平台设计
- **尺寸与结构**：机器人高90厘米，完全3D打印，重量轻且设计美观，适合与人类尺度环境交互。
- **硬件配置**：配备足够扭矩的关节电机和计算单元，支持动态运动与复杂任务。
- **开源资源**：所有3D CAD文件、ROS软件及设计文档均开源发布，便于用户修改与扩展。

### 实验与演示
- 论文展示了机器人的动态运动能力，包括行走、平衡等基础动作。
- 实验验证了机械结构的可靠性与电气系统的稳定性，未报告具体数值指标（如步态周期或扭矩参数）。

### 结论
- igus Humanoid Open Platform为儿童尺寸人形机器人研究提供了低成本、高灵活性的标准平台，降低了硬件门槛，并鼓励社区协作开发。

## Overview
The use of standard platforms in the field of humanoid robotics can accelerate research, and lower the entry barrier for new research groups. While many affordable humanoid standard platforms exist in the lower size ranges of up to 60cm, beyond this the few available standard platforms quickly become significantly more expensive, and difficult to operate and maintain. In this paper, the igus Humanoid Open Platform is presented---a new, affordable, versatile and easily customisable standard platform for humanoid robots in the child-sized range. At 90cm, the robot is large enough to interact with a human-scale environment in a meaningful way, and is equipped with enough torque and computing power to foster research in many possible directions. The structure of the robot is entirely 3D printed, allowing for a lightweight and appealing design. The electrical and mechanical designs of the robot are presented, and the main features of the corresponding open-source ROS software are discussed. The 3D CAD files for all of the robot parts have been released open-source in conjunction with this paper.

## Overview
The use of standard platforms in the field of humanoid robotics can accelerate research and lower the entry barrier for new research groups. While many affordable humanoid standard platforms exist in the lower size ranges of up to 60cm, beyond this the few available standard platforms quickly become significantly more expensive, and difficult to operate and maintain. In this paper, the igus Humanoid Open Platform is presented—a new, affordable, versatile and easily customisable standard platform for humanoid robots in the child-sized range. At 90cm, the robot is large enough to interact with a human-scale environment in a meaningful way, and is equipped with enough torque and computing power to foster research in many possible directions. The structure of the robot is entirely 3D printed, allowing for a lightweight and appealing design. The electrical and mechanical designs of the robot are presented, and the main features of the corresponding open-source ROS software are discussed. The 3D CAD files for all of the robot parts have been released open-source in conjunction with this paper.

## Content
The use of standard platforms in the field of humanoid robotics can accelerate research and lower the entry barrier for new research groups. While many affordable humanoid standard platforms exist in the lower size ranges of up to 60cm, beyond this the few available standard platforms quickly become significantly more expensive, and difficult to operate and maintain. In this paper, the igus Humanoid Open Platform is presented—a new, affordable, versatile and easily customisable standard platform for humanoid robots in the child-sized range. At 90cm, the robot is large enough to interact with a human-scale environment in a meaningful way, and is equipped with enough torque and computing power to foster research in many possible directions. The structure of the robot is entirely 3D printed, allowing for a lightweight and appealing design. The electrical and mechanical designs of the robot are presented, and the main features of the corresponding open-source ROS software are discussed. The 3D CAD files for all of the robot parts have been released open-source in conjunction with this paper.

## 参考
- http://arxiv.org/abs/1809.10701v1

## 개요
휴머노이드 로봇 분야에서 표준 플랫폼은 연구를 가속화하고 새로운 팀의 진입 장벽을 낮출 수 있습니다. 기존에는 60cm 이하의 저비용 플랫폼이 많지만, 더 큰 크기의 플랫폼은 종종 가격이 비싸고 유지보수가 어렵습니다. 본 논문에서 제안하는 igus Humanoid Open Platform은 이러한 공백을 메웁니다: 90cm 높이, 비용이 통제 가능하며, 맞춤화가 용이한 휴머노이드 로봇 표준 플랫폼입니다. 이 로봇은 완전히 3D 프린팅으로 제작되어 가볍고 외관이 매력적이며, 다양한 연구 방향을 지원할 수 있는 충분한 토크와 계산 능력을 갖추고 있습니다. 논문은 기계적 및 전기적 설계를 자세히 설명하고, 함께 제공되는 오픈소스 ROS 소프트웨어의 주요 기능을 논의하며, 모든 3D CAD 파일은 오픈소스로 공개되었습니다.

## 핵심 내용
### 배경 및 동기
- 휴머노이드 로봇 표준 플랫폼은 연구를 가속화할 수 있지만, 기존 60cm 이상 플랫폼은 비용이 높고 운영 및 유지보수가 어렵습니다.
- 어린이 크기(약 90cm), 저비용, 유지보수가 용이하며 맞춤화가 가능한 오픈소스 플랫폼이 필요합니다.

### 플랫폼 설계
- **크기 및 구조**: 로봇은 높이 90cm로 완전히 3D 프린팅되며, 가볍고 디자인이 미려하여 인간 규모 환경과의 상호작용에 적합합니다.
- **하드웨어 구성**: 동적 운동과 복잡한 작업을 지원할 수 있는 충분한 토크의 관절 모터와 계산 유닛을 갖추고 있습니다.
- **오픈소스 리소스**: 모든 3D CAD 파일, ROS 소프트웨어 및 설계 문서가 오픈소스로 공개되어 사용자가 수정 및 확장하기 용이합니다.

### 실험 및 시연
- 논문은 걷기, 균형 유지 등 기본 동작을 포함한 로봇의 동적 운동 능력을 보여줍니다.
- 실험은 기계 구조의 신뢰성과 전기 시스템의 안정성을 검증했으며, 구체적인 수치 지표(예: 보행 주기 또는 토크 매개변수)는 보고되지 않았습니다.

### 결론
- igus Humanoid Open Platform은 어린이 크기 휴머노이드 로봇 연구를 위한 저비용, 고유연성 표준 플랫폼을 제공하여 하드웨어 진입 장벽을 낮추고 커뮤니티 협업 개발을 장려합니다.
