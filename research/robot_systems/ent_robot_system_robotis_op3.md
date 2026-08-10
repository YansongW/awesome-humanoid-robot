---
$id: ent_robot_system_robotis_op3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: ROBOTIS OP3 (DARwIn-OP Series)
  zh: ROBOTIS OP3 人形机器人（DARwIn-OP 系列）
  ko: ROBOTIS OP3 (DARwIn-OP Series)
summary:
  en: A 510 mm, 3.5 kg open-platform humanoid robot from ROBOTIS, the third generation of the NSF-funded DARwIn-OP line, with
    20 degrees of freedom driven by DYNAMIXEL XM430-W350-R smart servos, an Intel NUC onboard computer and a ROS2-native software
    stack, widely used in education and RoboCup.
  zh: ROBOTIS OP3 是韩国 ROBOTIS 推出的开放平台人形机器人，为 NSF 资助的 DARwIn-OP（达尔文开放平台）产品线第三代，身高约 510 mm、重约 3.5 kg，20 个自由度由 20 台 DYNAMIXEL
    XM430-W350-R 智能舵机驱动，主控 Intel NUC + OpenCR，2025 年复刻版原生转向 ROS2，教学文档与 RoboCup 生态成熟。
  ko: A 510 mm, 3.5 kg open-platform humanoid robot from ROBOTIS, the third generation of the NSF-funded DARwIn-OP line, with
    20 degrees of freedom driven by DYNAMIXEL XM430-W350-R smart servos, an Intel NUC onboard computer and a ROS2-native software
    stack, widely used in education and RoboCup.
domains:
- 02_components
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- system
- knowledge
tags:
- open_source
- humanoid_robot
- robotis_op3
- darwin_op
- robotis
- dynamixel
- ros2
- robocup
- education
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/robotis-op3-darwin-op.md（访问日期 2026-07-01）。该平台本质是"开放平台的商业整机"而非社区开源硬件项目：ROS 软件包 Apache-2.0，整机只能购买成品。
    | WP4 trilingual backfill 2026-08-10: en body retranslated from zh deep-read (1877 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: ROBOTIS OP3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/op3/introduction/
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ROBOTIS-GIT/ROBOTIS-OP3 GitHub Repository
  url: https://github.com/ROBOTIS-GIT/ROBOTIS-OP3
  accessed_at: '2026-07-01'
---
## 概述

ROBOTIS OP3 是韩国 ROBOTIS 主导的开放平台人形机器人，其前身为 DARwIn-OP（Dynamic Anthropomorphic Robot with Intelligence – Open Platform，达尔文开放平台）——2010 年由 Virginia Tech RoMeLa（Dennis Hong 团队）牵头，联合 University of Pennsylvania、Purdue University 与 ROBOTIS 开发，美国 NSF 资助。OP3 高约 510 mm、重约 3.5 kg（无外壳），20 个自由度（来源：调研档案 robotis-op3-darwin-op.md，下同）。

开源属性：OP3 ROS 软件包 Apache-2.0（GitHub ROBOTIS-GIT）；DARwIn-OP 硬件 CAD 与软件历史上免费公开（SourceForge `darwinop` 项目页仍可访问）；本质是"开放平台的商业整机"，非社区开源硬件项目。价格：OP3 现价 $13,764.35（robotis.us，2026 年页面快照）；Generation Robots 约 €12,113（含税）；DARwIn-OP 2010 年售价 $12,000（教育折扣 $9,600），第三方 3D 打印克隆约 $6,100。OP（DARwIn-OP）与 OP2 已停产（e-Manual 官方 WARNING），OP3 为当前在售型号。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | OP3 约 510 mm / 约 3.5 kg；DARwIn-OP 455 mm / 2.8 kg | e-Manual / RoMeLa |
| 自由度 | 20 | e-Manual |
| 价格 | OP3 $13,764.35（美国）/ 约 €12,113（欧洲） | robotis.us / Generation Robots |
| 主控 | Intel NUC（Core i3 双核、8GB DDR4、250GB M.2 SSD）；子控制器 OpenCR | e-Manual |
| 传感器 | Logitech C920 摄像头、IMU（陀螺+加速度计+磁力计各 3 轴）、扬声器、RGB LED、4 按键 | e-Manual |
| 电池 | 3 芯 11.1V LiPo（新版 3300 mAh），支持热插拔换电 | e-Manual |
| 新手友好度 | 3 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- OP3：20 台 DYNAMIXEL XM430-W350-R 智能舵机（减速比 353.5:1，失速扭矩 4.1 N·m，支持电流环力控、DYNAMIXEL Protocol 2.0）。
- DARwIn-OP：20 台 MX-28（内置 maxon RE-max 电机，失速扭矩 2.5 N·m，Protocol 1.0）。
- 高减速比舵机方案：位置控制精度高、易用，但无本体感知力控能力，不适合高动态运动控制研究。

### 软件栈与文档

- 2025 年 OP3 复刻版原生转向 ROS2（e-Manual 口径），配套 DYNAMIXEL SDK，C++ 开发，Ubuntu 64 位；官方提供行走/动作编辑（op3_action_editor）、Gazebo 仿真模型等 ROS 包。
- ROBOTIS e-Manual 极其完善（规格、装配、教程、ROS 包逐条文档），是行业文档标杆；RoboCup 足球生态积累深厚（DARwIn-OP 曾获 RoboCup 2011、2012 儿童组冠军）。
- GitHub `ROBOTIS-GIT/ROBOTIS-OP3` 约 157 stars / 65 forks，最近 push 2025-02-26（伴随 2025 ROS2 复刻更新）。

### 适合人群

- 适合：预算充足的学校/实验室教学与 RoboCup 参赛——开箱即用的成熟产品、文档顶级、舵机即插即用、ROS2 生态入门路径清晰；对只想写上层算法不想造硬件的用户省事。
- 门槛：约 $1.4 万美元的价格对个人爱好者过高；"开源"主要体现在软件与 CAD 层面，整机只能买成品；舵机方案学不到准直驱/力控等当前主流技术。

## 参考

- [ROBOTIS OP3 e-Manual](https://emanual.robotis.com/docs/en/platform/op3/introduction/)
- [ROBOTIS-GIT/ROBOTIS-OP3 GitHub 仓库](https://github.com/ROBOTIS-GIT/ROBOTIS-OP3)
- [DARwIn-OP 项目页（RoMeLa）](https://www.romela.org/darwin-op-open-platform-humanoid-robot-for-research-and-education/)

## 개요

ROBOTIS OP3는 한국 ROBOTIS가 주도하는 오픈 플랫폼 휴머노이드 로봇으로, 그 전신은 DARwIn-OP(Dynamic Anthropomorphic Robot with Intelligence – Open Platform, 다윈 오픈 플랫폼)입니다. 2010년 Virginia Tech RoMeLa(Dennis Hong 팀)가 주도하고 University of Pennsylvania, Purdue University 및 ROBOTIS가 공동 개발했으며, 미국 NSF의 지원을 받았습니다. OP3의 높이는 약 510mm, 무게는 약 3.5kg(외장 미포함), 20자유도를 가집니다(출처: 조사 파일 robotis-op3-darwin-op.md, 이하 동일).

오픈소스 속성: OP3 ROS 소프트웨어 패키지는 Apache-2.0 라이선스(GitHub ROBOTIS-GIT)입니다. DARwIn-OP 하드웨어 CAD와 소프트웨어는 역사적으로 무료로 공개되었습니다(SourceForge `darwinop` 프로젝트 페이지는 여전히 접근 가능). 본질적으로는 "오픈 플랫폼의 상용 완제품"이며, 커뮤니티 기반 오픈소스 하드웨어 프로젝트는 아닙니다. 가격: OP3 현재 가격 $13,764.35(robotis.us, 2026년 페이지 스냅샷 기준); Generation Robots 약 €12,113(세금 포함); DARwIn-OP 2010년 판매 가격 $12,000(교육 할인 $9,600), 서드파티 3D 프린팅 클론 약 $6,100. OP(DARwIn-OP)와 OP2는 단종되었으며(e-Manual 공식 WARNING), OP3가 현재 판매 중인 모델입니다.

## 핵심 내용

### 주요 사양

| 항목 | 수치 | 출처 |
|---|---|---|
| 높이 / 무게 | OP3 약 510mm / 약 3.5kg; DARwIn-OP 455mm / 2.8kg | e-Manual / RoMeLa |
| 자유도 | 20 | e-Manual |
| 가격 | OP3 $13,764.35(미국) / 약 €12,113(유럽) | robotis.us / Generation Robots |
| 메인 컨트롤러 | Intel NUC(Core i3 듀얼코어, 8GB DDR4, 250GB M.2 SSD); 서브 컨트롤러 OpenCR | e-Manual |
| 센서 | Logitech C920 카메라, IMU(자이로+가속도계+자력계 각 3축), 스피커, RGB LED, 4버튼 | e-Manual |
| 배터리 | 3셀 11.1V LiPo(신형 3300mAh), 핫스왑 배터리 교체 지원 | e-Manual |
| 초보자 친화도 | 3 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 구성

- OP3: 20대 DYNAMIXEL XM430-W350-R 스마트 서보모터(감속비 353.5:1, 스톨 토크 4.1 N·m, 전류 제어 힘 제어 지원, DYNAMIXEL Protocol 2.0).
- DARwIn-OP: 20대 MX-28(내장 maxon RE-max 모터, 스톨 토크 2.5 N·m, Protocol 1.0).
- 고감속비 서보모터 방식: 위치 제어 정밀도가 높고 사용이 간편하지만, 본체 감지 힘 제어 능력이 없어 고동적 운동 제어 연구에는 부적합합니다.

### 소프트웨어 스택 및 문서

- 2025년 OP3 리메이크 버전은 기본적으로 ROS2를 지원하며(e-Manual 기준), DYNAMIXEL SDK를 함께 제공하고 C++로 개발되며 Ubuntu 64비트를 사용합니다. 공식적으로 보행/동작 편집(op3_action_editor), Gazebo 시뮬레이션 모델 등의 ROS 패키지를 제공합니다.
- ROBOTIS e-Manual은 매우 완벽하여(사양, 조립, 튜토리얼, ROS 패키지별 문서) 업계 문서의 기준으로 꼽힙니다. RoboCup 축구 생태계의 축적이 깊습니다(DARwIn-OP는 RoboCup 2011, 2012 아동 그룹 챔피언을 차지했습니다).
- GitHub `ROBOTIS-GIT/ROBOTIS-OP3` 약 157 stars / 65 forks, 최근 push 2025-02-26(2025 ROS2 리메이크 업데이트 동반).

### 적합한 사용자

- 적합: 예산이 충분한 학교/연구소의 교육 및 RoboCup 참가 – 개봉 즉시 사용 가능한 성숙한 제품, 최고 수준의 문서, 서보모터 플러그 앤 플레이, ROS2 생태계 입문 경로가 명확함; 상위 알고리즘만 작성하고 하드웨어를 직접 만들고 싶지 않은 사용자에게 편리함.
- 진입 장벽: 약 $14,000의 가격은 개인 애호가에게 너무 높음; "오픈소스"는 주로 소프트웨어와 CAD 수준에 국한되며, 완제품만 구매 가능; 서보모터 방식으로는 준직구동/힘 제어 등 현재 주류 기술을 배울 수 없음.

## Overview

The ROBOTIS OP3 is an open-platform humanoid robot led by ROBOTIS of South Korea. Its predecessor is the DARwIn-OP (Dynamic Anthropomorphic Robot with Intelligence – Open Platform), developed in 2010 under the leadership of Virginia Tech's RoMeLa (Dennis Hong's team), in collaboration with the University of Pennsylvania, Purdue University, and ROBOTIS, with funding from the U.S. NSF. The OP3 stands approximately 510 mm tall, weighs about 3.5 kg (without the shell), and has 20 degrees of freedom (source: research archive robotis-op3-darwin-op.md, same below).

Open-source attributes: The OP3 ROS software packages are Apache-2.0 licensed (GitHub ROBOTIS-GIT); the DARwIn-OP hardware CAD and software were historically freely available (the SourceForge `darwinop` project page is still accessible); it is essentially a "commercial complete unit on an open platform," not a community open-source hardware project. Pricing: The OP3 currently sells for $13,764.35 (robotis.us, 2026 page snapshot); Generation Robots lists it at approximately €12,113 (including tax); the DARwIn-OP sold for $12,000 in 2010 (with an educational discount of $9,600), and third-party 3D-printed clones cost around $6,100. The OP (DARwIn-OP) and OP2 have been discontinued (official WARNING in the e-Manual), with the OP3 being the current model on sale.

## Content

### Key Specifications

| Item | Value | Source |
|---|---|---|
| Height / Weight | OP3 approx. 510 mm / approx. 3.5 kg; DARwIn-OP 455 mm / 2.8 kg | e-Manual / RoMeLa |
| Degrees of Freedom | 20 | e-Manual |
| Price | OP3 $13,764.35 (US) / approx. €12,113 (Europe) | robotis.us / Generation Robots |
| Main Controller | Intel NUC (Core i3 dual-core, 8GB DDR4, 250GB M.2 SSD); sub-controller OpenCR | e-Manual |
| Sensors | Logitech C920 camera, IMU (3-axis gyro + accelerometer + magnetometer), speaker, RGB LED, 4 buttons | e-Manual |
| Battery | 3-cell 11.1V LiPo (new version 3300 mAh), supports hot-swappable battery replacement | e-Manual |
| Beginner Friendliness | 3 / 5 (research archive assessment) | Research archive |

### Actuator Solution

- OP3: 20 DYNAMIXEL XM430-W350-R smart servos (gear ratio 353.5:1, stall torque 4.1 N·m, supports current-loop force control, DYNAMIXEL Protocol 2.0).
- DARwIn-OP: 20 MX-28 (built-in maxon RE-max motor, stall torque 2.5 N·m, Protocol 1.0).
- High-gear-ratio servo solution: High position control accuracy and ease of use, but lacks proprioceptive force control capability and is unsuitable for research on highly dynamic motion control.

### Software Stack and Documentation

- The 2025 OP3 replica natively transitions to ROS2 (per the e-Manual), paired with the DYNAMIXEL SDK, developed in C++, on Ubuntu 64-bit; official ROS packages include walking/action editing (op3_action_editor), Gazebo simulation models, and more.
- The ROBOTIS e-Manual is extremely comprehensive (specifications, assembly, tutorials, and item-by-item ROS package documentation), setting the industry benchmark for documentation; the RoboCup soccer ecosystem has deep accumulated expertise (the DARwIn-OP won the RoboCup 2011 and 2012 Kid-Size League championships).
- GitHub `ROBOTIS-GIT/ROBOTIS-OP3` has approximately 157 stars / 65 forks, with the latest push on 2025-02-26 (accompanying the 2025 ROS2 replica update).

### Target Audience

- Suitable for: Schools/laboratories with sufficient budgets for teaching and RoboCup participation—a mature, out-of-the-box product with top-tier documentation, plug-and-play servos, and a clear entry path into the ROS2 ecosystem; convenient for users who only want to write high-level algorithms without building hardware.
- Barriers: The approximately $14,000 price is too high for individual hobbyists; "open source" is mainly reflected at the software and CAD levels, as the complete unit can only be purchased as a finished product; the servo solution does not teach current mainstream technologies such as quasi-direct drive or force control.
