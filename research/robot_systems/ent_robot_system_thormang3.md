---
$id: ent_robot_system_thormang3
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: THORMANG3
  zh: THORMANG3 全尺寸人形机器人
  ko: THORMANG3
summary:
  en: A 137.5 cm, 42 kg full-size humanoid robot from ROBOTIS descending from the DARPA Robotics Challenge 2015 finals, with
    29 degrees of freedom driven by DYNAMIXEL-P series servos, dual Intel NUC computers, ankle force-torque sensors and a
    complete ROS1 software stack, sold as a commercial platform with open-source control software and public STP models.
  zh: THORMANG3（Tactical Hazardous Operations Robot 3）是韩国 ROBOTIS 的全尺寸人形机器人，源于 DARPA Robotics Challenge 2015 决赛平台，身高 137.5
    cm、重 42 kg，29 个自由度由 29 台 DYNAMIXEL-P 系列一体化伺服驱动，双 Intel NUC 分工运动控制与感知，配脚踝六维力/力矩传感器与完整 ROS1 软件栈，整机 STP 模型官方公开。
  ko: A 137.5 cm, 42 kg full-size humanoid robot from ROBOTIS descending from the DARPA Robotics Challenge 2015 finals, with
    29 degrees of freedom driven by DYNAMIXEL-P series servos, dual Intel NUC computers, ankle force-torque sensors and a
    complete ROS1 software stack, sold as a commercial platform with open-source control software and public STP models.
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
- thormang3
- robotis
- dynamixel_p
- full_size_humanoid
- ros1
- darpa_robotics_challenge
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/thormang3.md（访问日期 2026-07-01）。官方无公开标价，经销商为询价制（交货期 12 周）；本质是商业整机 + 开源控制软件，ROS 软件包长期停更（多数仓库
    2016-2018 年后无实质更新）。 | WP4 trilingual backfill 2026-08-10: en body retranslated from zh deep-read (1743 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: THORMANG3 e-Manual
  url: https://emanual.robotis.com/docs/en/platform/thormang3/introduction/
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ROBOTIS-THORMANG-COMMON GitHub Repository
  url: https://github.com/robotis-git/robotis-thormang-common
  accessed_at: '2026-07-01'
---
## 概述

THORMANG3（Tactical Hazardous Operations Robot，第三代）是韩国 ROBOTIS 的全尺寸人形机器人，THOR 系列源于 DARPA Robotics Challenge 2015 决赛平台（Team ROBOTIS）。整机高 137.5 cm、重 42 kg，29 个自由度（来源：调研档案 thormang3.md，下同）。

开源属性：ROS 软件包开源于 GitHub（ROBOTIS-GIT/ROBOTIS-THORMANG-* 系列，COMMON 包许可证标记为"Other/未明确"）；整机 STP 三维模型官方公开下载；本质是商业整机 + 开源控制软件。硬件成本未知——官方无公开标价，经销商页面标注"需询价、交货期 12 周"（Cyber Robotics HK，2025 年页面）；历史定位为"相对可负担的全尺寸平台"。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 137.5 cm / 42 kg | e-Manual |
| 自由度 | 29 | e-Manual |
| 价格 | 未知（需询价、交货期 12 周） | 经销商页面 |
| 计算 | 2 台 Intel NUC（Core i5、8GB DDR4、128GB M.2 SSD），分工运动控制（MPC）与感知（PPC）；机载 D-Link DIR-806A 无线路由 | e-Manual |
| 传感器 | Logitech C920 相机；Intel RealSense（选配）；Hokuyo UTM-30LX-EW 激光雷达（选配）；双脚踝 ATI Mini58 六维力/力矩传感器 ×2；MicroStrain 3DM-GX4-25 IMU | e-Manual |
| 电池 | 22V 22000 mAh + 18.5V 11000 mAh 双电池；也可外接电源（执行器需 0-30V/100A 电源） | e-Manual |
| 新手友好度 | 1 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- 29 台 DYNAMIXEL-P（原 DYNAMIXEL PRO）系列一体化伺服（2019 年 6 月起由 PRO 换型为 P 系列）：
  - PH54-200-S500-R（200W）× 10（腿部大关节）
  - PH54-100-S500-R（100W）× 11
  - PH42-020-S300-R（20W）× 8（小关节）
- 谐波减速 + 高功率密度伺服是 DRC 时代全尺寸平台的典型方案，扭矩充足但单台舵机价格昂贵，整机成本主要在此。
- 附带无线急停、吊装带（carabiner + rope）与升降架——全尺寸机型的安全标配。

### 软件栈与文档

- Ubuntu LTS 64 位 + ROS1，C++ 开发；官方提供行走（walking）、操作（manipulation）、感知（PPC）、Gazebo 仿真（COMMON 包）等完整 ROS 包；未提供 ROS2 官方支持（检索时点未见）。
- 全套 e-Manual 教程（快速上手、校准、教程、开发），完善程度与 OP3 同级；STP 模型可用于二次机械设计。
- GitHub `ROBOTIS-GIT/ROBOTIS-THORMANG-COMMON` 仅 5 stars / 10 forks，最后 push 2018-04-01；MPC/PPC/Tools 等兄弟仓库均为 2016 年创建、长期停更，软件栈停留在 ROS1 时代。

### 适合人群

- 适合：有全尺寸平台刚性需求的大学/研究所实验室——29 自由度全尺寸平台、F/T 传感器 + 激光雷达配置齐全、ROBOTIS 文档规范、DRC 血统。
- 门槛：42 kg、137 cm 的全尺寸机型对场地/安全/人员要求极高；价格需询价且必然远超个人预算；ROS1 软件栈陈旧，维护投入大；完全不适合个人新手——想玩全尺寸请直接看 OpenLoong 的仿真框架。

## 参考

- [THORMANG3 e-Manual](https://emanual.robotis.com/docs/en/platform/thormang3/introduction/)
- [ROBOTIS-THORMANG-COMMON 仓库](https://github.com/robotis-git/robotis-thormang-common)
- [ROS wiki: ROBOTIS](http://wiki.ros.org/ROBOTIS)

## 개요

THORMANG3（Tactical Hazardous Operations Robot, 3세대）는 한국 ROBOTIS의 전신 크기 휴머노이드 로봇으로, THOR 시리즈는 DARPA Robotics Challenge 2015 결승전 플랫폼(Team ROBOTIS)에서 비롯되었습니다. 전체 높이 137.5 cm, 무게 42 kg, 29 자유도(출처: 조사 파일 thormang3.md, 이하 동일).

오픈소스 속성: ROS 소프트웨어 패키지는 GitHub(ROBOTIS-GIT/ROBOTIS-THORMANG-* 시리즈, COMMON 패키지 라이선스는 "기타/명확하지 않음"으로 표시)에 오픈소스로 제공됨; 전체 STP 3D 모델은 공식적으로 공개 다운로드 가능; 본질적으로 상용 완제품 + 오픈소스 제어 소프트웨어입니다. 하드웨어 비용은 알 수 없음——공식 공개 가격 없음, 딜러 페이지에는 "가격 문의 필요, 납기 12주"라고 표시됨(Cyber Robotics HK, 2025년 페이지); 역사적으로 "상대적으로 저렴한 전신 크기 플랫폼"으로 포지셔닝됨.

## 핵심 내용

### 주요 사양

| 항목 | 수치 | 출처 |
|---|---|---|
| 키 / 무게 | 137.5 cm / 42 kg | e-Manual |
| 자유도 | 29 | e-Manual |
| 가격 | 알 수 없음(가격 문의 필요, 납기 12주) | 딜러 페이지 |
| 컴퓨팅 | Intel NUC 2대(Core i5, 8GB DDR4, 128GB M.2 SSD), 운동 제어(MPC)와 인식(PPC) 분담; 탑재 D-Link DIR-806A 무선 라우터 | e-Manual |
| 센서 | Logitech C920 카메라; Intel RealSense(옵션); Hokuyo UTM-30LX-EW 레이저 레이더(옵션); 양발목 ATI Mini58 6축 힘/토크 센서 ×2; MicroStrain 3DM-GX4-25 IMU | e-Manual |
| 배터리 | 22V 22000 mAh + 18.5V 11000 mAh 이중 배터리; 외부 전원 공급 가능(액추에이터는 0-30V/100A 전원 필요) | e-Manual |
| 초보자 친화도 | 1 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 구성

- DYNAMIXEL-P(구 DYNAMIXEL PRO) 시리즈 일체형 서보 29대(2019년 6월부터 PRO에서 P 시리즈로 교체):
  - PH54-200-S500-R(200W) × 10(다리 대형 관절)
  - PH54-100-S500-R(100W) × 11
  - PH42-020-S300-R(20W) × 8(소형 관절)
- 하모닉 감속 + 고전력 밀도 서보는 DRC 시대 전신 크기 플랫폼의 전형적인 구성으로, 토크는 충분하지만 단일 서보 가격이 매우 비싸며 전체 비용의 주요 부분을 차지합니다.
- 무선 비상 정지, 카라비너 + 로프 리깅, 리프트 프레임 포함——전신 크기 모델의 안전 기본 사양.

### 소프트웨어 스택 및 문서

- Ubuntu LTS 64비트 + ROS1, C++ 개발; 공식적으로 보행(walking), 조작(manipulation), 인식(PPC), Gazebo 시뮬레이션(COMMON 패키지) 등 완전한 ROS 패키지 제공; ROS2 공식 지원 없음(검색 시점 기준 미확인).
- 전체 e-Manual 튜토리얼(빠른 시작, 캘리브레이션, 튜토리얼, 개발) 제공, 완성도는 OP3와 동등; STP 모델은 2차 기계 설계에 사용 가능.
- GitHub `ROBOTIS-GIT/ROBOTIS-THORMANG-COMMON`은 별 5개 / 포크 10개에 불과, 마지막 푸시 2018-04-01; MPC/PPC/Tools 등 관련 저장소는 모두 2016년 생성, 장기간 업데이트 중단, 소프트웨어 스택은 ROS1 시대에 머물러 있음.

### 적합한 사용자

- 적합: 전신 크기 플랫폼이 필요한 대학/연구소 실험실——29 자유도 전신 크기 플랫폼, F/T 센서 + 레이저 레이더 완비, ROBOTIS의 체계적인 문서, DRC 계보.
- 진입 장벽: 42 kg, 137 cm의 전신 크기 모델은 공간/안전/인력 요구사항이 매우 높음; 가격은 문의 필요하며 개인 예산을 훨씬 초과할 것임; ROS1 소프트웨어 스택은 구식으로 유지보수 비용이 큼; 개인 초보자에게는 전혀 적합하지 않음——전신 크기를 체험하려면 OpenLoong의 시뮬레이션 프레임워크를 바로 확인하세요.

## Overview

THORMANG3 (Tactical Hazardous Operations Robot, 3rd Generation) is a full-sized humanoid robot by ROBOTIS, South Korea. The THOR series originates from the DARPA Robotics Challenge 2015 finals platform (Team ROBOTIS). The entire unit stands 137.5 cm tall, weighs 42 kg, and has 29 degrees of freedom (source: research archive thormang3.md, same below).

Open-source attributes: ROS software packages are open-sourced on GitHub (ROBOTIS-GIT/ROBOTIS-THORMANG-* series, with the COMMON package license marked as "Other/Not specified"); the full STP 3D model is officially available for public download; essentially, it is a commercial unit with open-source control software. Hardware cost is unknown—no official public pricing, with dealer pages noting "price on request, 12-week lead time" (Cyber Robotics HK, 2025 page); historically positioned as a "relatively affordable full-sized platform."

## Content

### Key Specifications

| Item | Value | Source |
|---|---|---|
| Height / Weight | 137.5 cm / 42 kg | e-Manual |
| Degrees of Freedom | 29 | e-Manual |
| Price | Unknown (price on request, 12-week lead time) | Dealer page |
| Computing | 2x Intel NUC (Core i5, 8GB DDR4, 128GB M.2 SSD), split for motion control (MPC) and perception (PPC); onboard D-Link DIR-806A wireless router | e-Manual |
| Sensors | Logitech C920 camera; Intel RealSense (optional); Hokuyo UTM-30LX-EW LiDAR (optional); dual ankle ATI Mini58 6-axis force/torque sensors ×2; MicroStrain 3DM-GX4-25 IMU | e-Manual |
| Battery | 22V 22000 mAh + 18.5V 11000 mAh dual battery; external power also supported (actuators require 0-30V/100A supply) | e-Manual |
| Beginner-friendliness | 1 / 5 (research archive assessment) | Research archive |

### Actuator Configuration

- 29 DYNAMIXEL-P (formerly DYNAMIXEL PRO) series integrated servos (switched from PRO to P series since June 2019):
  - PH54-200-S500-R (200W) × 10 (large leg joints)
  - PH54-100-S500-R (100W) × 11
  - PH42-020-S300-R (20W) × 8 (small joints)
- Harmonic drive + high power-density servos is a typical approach for full-sized platforms from the DRC era, offering ample torque, but individual servos are expensive, and this constitutes the bulk of the total cost.
- Includes wireless emergency stop, lifting sling (carabiner + rope), and hoist frame—standard safety equipment for full-sized models.

### Software Stack and Documentation

- Ubuntu LTS 64-bit + ROS1, C++ development; official ROS packages provided for walking, manipulation, perception (PPC), and Gazebo simulation (COMMON package); no official ROS2 support (none found at time of search).
- Full e-Manual tutorials (quick start, calibration, tutorials, development), with completeness on par with OP3; STP models available for secondary mechanical design.
- GitHub `ROBOTIS-GIT/ROBOTIS-THORMANG-COMMON` has only 5 stars / 10 forks, last push 2018-04-01; sibling repos like MPC/PPC/Tools were created in 2016 and have been dormant for a long time, with the software stack stuck in the ROS1 era.

### Target Audience

- Suitable for: university/research institute labs with rigid requirements for a full-sized platform—29-DOF full-size, complete F/T sensors + LiDAR configuration, standardized ROBOTIS documentation, DRC pedigree.
- Barriers: the 42 kg, 137 cm full-sized model demands extremely high standards for space, safety, and personnel; pricing requires inquiry and will inevitably exceed personal budgets; the ROS1 software stack is outdated and requires significant maintenance; completely unsuitable for individual beginners—for full-size experimentation, look directly at OpenLoong's simulation framework.
