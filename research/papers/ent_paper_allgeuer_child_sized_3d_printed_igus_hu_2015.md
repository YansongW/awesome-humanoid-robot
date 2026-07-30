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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.10701v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇 분야에서 표준 플랫폼을 사용하면 연구를 가속화하고 새로운 연구 그룹의 진입 장벽을 낮출 수 있습니다. 최대 60cm까지의 낮은 크기 범위에는 많은 저렴한 휴머노이드 표준 플랫폼이 존재하지만, 그 이상에서는 몇 안 되는 표준 플랫폼이 급격히 더 비싸지고 운영 및 유지보수가 어려워집니다. 본 논문에서는 igus Humanoid Open Platform을 소개합니다. 이는 어린이 크기 범위의 휴머노이드 로봇을 위한 새롭고 저렴하며 다재다능하고 쉽게 맞춤 설정할 수 있는 표준 플랫폼입니다. 90cm 크기의 이 로봇은 인간 규모의 환경과 의미 있게 상호작용할 수 있을 만큼 크며, 다양한 연구 방향을 촉진할 수 있는 충분한 토크와 컴퓨팅 성능을 갖추고 있습니다. 로봇의 구조는 완전히 3D 프린팅되어 가볍고 매력적인 디자인을 가능하게 합니다. 로봇의 전기 및 기계 설계가 제시되며, 해당 오픈소스 ROS 소프트웨어의 주요 기능이 논의됩니다. 모든 로봇 부품의 3D CAD 파일은 본 논문과 함께 오픈소스로 공개되었습니다.

## 핵심 내용
휴머노이드 로봇 분야에서 표준 플랫폼을 사용하면 연구를 가속화하고 새로운 연구 그룹의 진입 장벽을 낮출 수 있습니다. 최대 60cm까지의 낮은 크기 범위에는 많은 저렴한 휴머노이드 표준 플랫폼이 존재하지만, 그 이상에서는 몇 안 되는 표준 플랫폼이 급격히 더 비싸지고 운영 및 유지보수가 어려워집니다. 본 논문에서는 igus Humanoid Open Platform을 소개합니다. 이는 어린이 크기 범위의 휴머노이드 로봇을 위한 새롭고 저렴하며 다재다능하고 쉽게 맞춤 설정할 수 있는 표준 플랫폼입니다. 90cm 크기의 이 로봇은 인간 규모의 환경과 의미 있게 상호작용할 수 있을 만큼 크며, 다양한 연구 방향을 촉진할 수 있는 충분한 토크와 컴퓨팅 성능을 갖추고 있습니다. 로봇의 구조는 완전히 3D 프린팅되어 가볍고 매력적인 디자인을 가능하게 합니다. 로봇의 전기 및 기계 설계가 제시되며, 해당 오픈소스 ROS 소프트웨어의 주요 기능이 논의됩니다. 모든 로봇 부품의 3D CAD 파일은 본 논문과 함께 오픈소스로 공개되었습니다.

## 参考
- http://arxiv.org/abs/1809.10701v1
