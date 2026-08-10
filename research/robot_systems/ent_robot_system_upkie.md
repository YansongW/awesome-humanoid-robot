---
$id: ent_robot_system_upkie
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Upkie Wheeled Biped Robot
  zh: Upkie 轮足双足机器人
  ko: Upkie Wheeled Biped Robot
summary:
  en: A fully open-source wheeled biped robot built from about 3,000 USD of off-the-shelf components plus 3D-printed parts,
    using mjbots quasi-direct-drive actuators and a Raspberry Pi 4, with Python-first software and out-of-the-box PID, MPC
    and reinforcement-learning balancing examples.
  zh: Upkie 是社区驱动的全开源轮足双足机器人（wheeled biped），约 3,000 美元现成组件加 60 小时以上 3D 打印即可复现，采用 mjbots qdd100 准直驱执行器与树莓派 4 主控，Python 优先的软件栈开箱自带
    PID、MPC、强化学习三种平衡控制示例，是个人在真实硬件上学习平衡控制的低门槛路径。
  ko: A fully open-source wheeled biped robot built from about 3,000 USD of off-the-shelf components plus 3D-printed parts,
    using mjbots quasi-direct-drive actuators and a Raspberry Pi 4, with Python-first software and out-of-the-box PID, MPC
    and reinforcement-learning balancing examples.
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
- wheeled_biped
- upkie
- mjbots
- quasi_direct_drive
- raspberry_pi
- python
- education
- balancing_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/upkie.md（访问日期 2026-07-01），事实均来自其列出的 GitHub 仓库、Hackaday 项目页、PyPI 文档与 FOSDEM 2026
    演讲页。身高/重量未见官方统一数值，标注为未知。 | WP4 trilingual backfill 2026-08-10: en body retranslated from zh deep-read (1551 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: upkie/upkie GitHub Repository
  url: https://github.com/upkie/upkie
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Upkie Wheeled Biped Robots on Hackaday
  url: https://hackaday.io/project/185729-upkie-wheeled-biped-robots
  accessed_at: '2026-07-01'
- id: src_003
  type: website
  title: upkie on PyPI
  url: https://pypi.org/project/upkie/
  accessed_at: '2026-07-01'
---
## 概述

Upkie 是社区驱动的开源轮足双足机器人（wheeled biped），核心作者为 Stéphane Caron（Inria）等，建立在 mjbots 开源执行器生态之上，含 Upkie Zero / Upkie Standard / 2026 硬件 v2 等构型。整机约 3,000 美元现成组件 + 60 小时以上 3D 打印即可复现（官方 Hackaday 口径），6 个自由度（每腿 3：髋、膝、驱动轮）；身高/重量未见官方统一数值（来源：调研档案 upkie.md，下同）。

许可证为 Apache-2.0（轮胎网格 CC BY 4.0），所用 mjbots 执行器的固件/硬件/软件同样全开源——从电机固件到上层控制全链路可改。GitHub 仓库 `upkie/upkie` 386 stars / 52 forks（2026-07-01 快照，仍高频更新），`upkie/parts`（CAD/打印件）与 `upkie/upkie_description`（URDF）同步维护，被 awesome-open-source-robots 等知名清单收录。轮足形态靠轮保持平衡、靠腿应对不平地形，相比纯步行双足控制难度与机械风险显著降低。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 自由度 | 6（每腿 3：髋、膝、驱动轮） | 调研档案 |
| 硬件成本 | 约 $3,000 现成组件 + 60 小时以上 3D 打印 | Hackaday 官方项目页 |
| 主控 | Raspberry Pi 4 + mjbots pi3hat（CAN 扩展板）+ 电源分配板 | 调研档案 |
| 传感器 | IMU 集成于 pi3hat；可选 OAK-D Lite 相机支架等社区配件 | 调研档案 |
| 身高 / 重量 | 未知（桌面级轮足，因构型而异） | 调研档案 |
| 新手友好度 | 4 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- mjbots qdd100 准直驱（quasi-direct-drive）无刷伺服 ×4（髋/膝）+ moteus 驱动器（轮），全部固件开源、可力控。
- 轮足混合形态：靠轮保持平衡、靠腿应对不平地形，摔机代价小，成功率高。

### 软件栈

- Python 或 C++，Linux/macOS 开发、部署到机上树莓派；`pixi`/`uv` 一条命令即可跑仿真示例（PyBullet），仿真零成本上手，无需先买硬件。
- 开箱自带三种平衡控制范式示例：PID、MPC（qpmpc）、强化学习（Stable-Baselines3）；Gymnasium 标准接口；另有社区 GPU RL 方案（MjLab Upkie）。
- 不依赖 ROS（可用 xacro/URDF 描述，兼容 Pinocchio 等库）。

### 文档与社区

- 逐步构建指南（step-by-step build instructions）+ Hackaday 项目页 + GitHub Discussions/聊天室；FOSDEM 2026 有官方经验分享演讲并现场发布硬件 v2（躯干一体化打印、腿部重新设计、宽度缩减 6 cm）。
- 中文创客社区（DFRobot 等）有翻译报道。

### 适合人群

- 适合：想在真实硬件上学平衡控制/RL 部署的个人开发者与课程项目；可作为进阶纯双足（如 Berkeley Humanoid Lite）前的练兵平台。
- 门槛：60+ 小时打印与装配仍需耐心；轮足不是"走路"的人形，若目标是仿人步态研究则不匹配。

## 参考

- [upkie/upkie GitHub 仓库](https://github.com/upkie/upkie)
- [Hackaday 官方项目页（$3,000 组件、60+ 小时打印）](https://hackaday.io/project/185729-upkie-wheeled-biped-robots)
- [PyPI 文档](https://pypi.org/project/upkie/)
- [FOSDEM 2026 演讲页](https://fosdem.org/2026/schedule/event/8PUMMD-open-source-robotics-practice-upkie-wheeled-bipeds/)

## 개요

Upkie는 커뮤니티 주도의 오픈소스 바퀴 달린 이족 보행 로봇(wheeled biped)으로, 핵심 저자는 Stéphane Caron(Inria) 등이며, mjbots 오픈소스 액추에이터 생태계를 기반으로 구축되었습니다. Upkie Zero / Upkie Standard / 2026 하드웨어 v2 등의 구성을 포함합니다. 약 3,000달러의 기성 부품과 60시간 이상의 3D 프린팅으로 재현 가능합니다(공식 Hackaday 기준). 6자유도(각 다리당 3개: 엉덩이, 무릎, 구동 휠); 키/무게에 대한 공식 통일 값은 없습니다(출처: 조사 파일 upkie.md, 이하 동일).

라이선스는 Apache-2.0(타이어 메시 CC BY 4.0)이며, 사용된 mjbots 액추에이터의 펌웨어/하드웨어/소프트웨어 역시 모두 오픈소스입니다——모터 펌웨어부터 상위 제어까지 전체 체인을 수정할 수 있습니다. GitHub 저장소 `upkie/upkie`는 386 stars / 52 forks(2026-07-01 스냅샷, 여전히 높은 업데이트 빈도), `upkie/parts`(CAD/출력물)와 `upkie/upkie_description`(URDF)이 함께 유지 관리되며, awesome-open-source-robots 등의 유명 목록에 포함되어 있습니다. 바퀴 달린 이족 형태는 바퀴로 균형을 유지하고 다리로 불규칙한 지형에 대응하며, 순수 보행 이족 로봇에 비해 제어 난이도와 기계적 위험이 크게 낮습니다.

## 핵심 내용

### 주요 파라미터

| 항목 | 값 | 출처 |
|---|---|---|
| 자유도 | 6(각 다리당 3개: 엉덩이, 무릎, 구동 휠) | 조사 파일 |
| 하드웨어 비용 | 약 $3,000 기성 부품 + 60시간 이상 3D 프린팅 | Hackaday 공식 프로젝트 페이지 |
| 메인 컨트롤러 | Raspberry Pi 4 + mjbots pi3hat(CAN 확장 보드) + 전원 분배 보드 | 조사 파일 |
| 센서 | IMU가 pi3hat에 통합됨; 선택적 OAK-D Lite 카메라 마운트 등 커뮤니티 액세서리 | 조사 파일 |
| 키 / 무게 | 알 수 없음(데스크톱급 바퀴 달린 이족, 구성에 따라 다름) | 조사 파일 |
| 초보자 친화도 | 4 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 방식

- mjbots qdd100 준직접 구동(quasi-direct-drive) 브러시리스 서보 ×4(엉덩이/무릎) + moteus 드라이버(휠), 모두 펌웨어 오픈소스, 힘 제어 가능.
- 바퀴-다리 혼합 형태: 바퀴로 균형 유지, 다리로 불규칙한 지형 대응, 추락 위험이 적고 성공률이 높음.

### 소프트웨어 스택

- Python 또는 C++, Linux/macOS에서 개발하여 온보드 Raspberry Pi에 배포; `pixi`/`uv` 한 줄 명령으로 시뮬레이션 예제(PyBullet) 실행 가능, 시뮬레이션은 비용 없이 시작 가능, 하드웨어를 먼저 구매할 필요 없음.
- 기본적으로 세 가지 균형 제어 패러다임 예제 제공: PID, MPC(qpmpc), 강화 학습(Stable-Baselines3); Gymnasium 표준 인터페이스; 별도 커뮤니티 GPU RL 솔루션(MjLab Upkie)도 있음.
- ROS에 의존하지 않음(xacro/URDF 설명 사용 가능, Pinocchio 등 라이브러리와 호환).

### 문서 및 커뮤니티

- 단계별 구축 가이드(step-by-step build instructions) + Hackaday 프로젝트 페이지 + GitHub Discussions/채팅방; FOSDEM 2026에서 공식 경험 공유 발표 및 하드웨어 v2 현장 출시(본체 일체형 프린팅, 다리 재설계, 폭 6cm 축소).
- 중국어 메이커 커뮤니티(DFRobot 등)에서 번역 보도 있음.

### 적합한 대상

- 적합: 실제 하드웨어에서 균형 제어/RL 배포를 배우고자 하는 개인 개발자 및 코스 프로젝트; 고급 순수 이족 로봇(예: Berkeley Humanoid Lite)으로 가기 전 연습 플랫폼으로 사용 가능.
- 진입 장벽: 60시간 이상의 프린팅 및 조립에 인내심 필요; 바퀴 달린 이족은 "걷는" 휴머노이드가 아니므로, 인간형 보행 연구가 목표라면 적합하지 않음.

## Overview

Upkie is a community-driven open-source wheeled biped robot, with core authors including Stéphane Caron (Inria) and others. It is built on the mjbots open-source actuator ecosystem and comes in configurations such as Upkie Zero / Upkie Standard / 2026 hardware v2. The entire robot can be replicated with approximately $3,000 in off-the-shelf components plus over 60 hours of 3D printing (per the official Hackaday description), featuring 6 degrees of freedom (3 per leg: hip, knee, and drive wheel). Height/weight figures are not officially unified (source: research archive upkie.md, same below).

The license is Apache-2.0 (wheel mesh CC BY 4.0), and the firmware/hardware/software of the mjbots actuators used are also fully open-source—from motor firmware to high-level control, the entire pipeline is modifiable. The GitHub repository `upkie/upkie` has 386 stars / 52 forks (snapshot as of 2026-07-01, still frequently updated), with `upkie/parts` (CAD/printed parts) and `upkie/upkie_description` (URDF) maintained in sync, and it is featured in well-known lists such as awesome-open-source-robots. The wheeled biped form maintains balance via wheels and handles uneven terrain with legs, significantly reducing control complexity and mechanical risk compared to purely walking bipeds.

## Content

### Key Parameters

| Item | Value | Source |
|---|---|---|
| Degrees of Freedom | 6 (3 per leg: hip, knee, drive wheel) | Research archive |
| Hardware Cost | Approximately $3,000 in off-the-shelf components + over 60 hours of 3D printing | Official Hackaday project page |
| Main Controller | Raspberry Pi 4 + mjbots pi3hat (CAN expansion board) + power distribution board | Research archive |
| Sensors | IMU integrated into pi3hat; optional OAK-D Lite camera mount and other community accessories | Research archive |
| Height / Weight | Unknown (desktop-class wheeled biped, varies by configuration) | Research archive |
| Beginner Friendliness | 4 / 5 (assessed in research archive) | Research archive |

### Actuator Solution

- mjbots qdd100 quasi-direct-drive brushless servos ×4 (hip/knee) + moteus drivers (wheels), all with open-source firmware and force control capability.
- Hybrid wheeled biped form: maintains balance via wheels, handles uneven terrain with legs, low fall damage cost, and high success rate.

### Software Stack

- Python or C++, developed on Linux/macOS and deployed to the onboard Raspberry Pi; `pixi`/`uv` can run simulation examples (PyBullet) with a single command, offering zero-cost simulation onboarding without needing to purchase hardware first.
- Comes with three built-in balance control paradigm examples: PID, MPC (qpmpc), and reinforcement learning (Stable-Baselines3); Gymnasium standard interface; plus community GPU RL solutions (MjLab Upkie).
- Does not depend on ROS (can use xacro/URDF descriptions, compatible with libraries such as Pinocchio).

### Documentation and Community

- Step-by-step build instructions + Hackaday project page + GitHub Discussions/chat rooms; FOSDEM 2026 featured an official experience-sharing talk with on-site release of hardware v2 (integrated torso printing, redesigned legs, width reduced by 6 cm).
- Chinese maker communities (such as DFRobot) have published translated coverage.

### Target Audience

- Suitable for: individual developers and course projects wanting to learn balance control/RL deployment on real hardware; can serve as a training platform before advancing to full bipeds (e.g., Berkeley Humanoid Lite).
- Barrier: 60+ hours of printing and assembly still requires patience; the wheeled biped is not a "walking" humanoid—if the goal is humanoid gait research, it is not a match.
