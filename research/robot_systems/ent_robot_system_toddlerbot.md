---
$id: ent_robot_system_toddlerbot
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: ToddlerBot
  zh: ToddlerBot 幼儿机器人
  ko: ToddlerBot
summary:
  en: An open-source child-size humanoid robot from Stanford University, 0.56 m tall and 3.4 kg, with 30 active degrees of
    freedom, a bill of materials of about 6,000 USD, ROBOTIS Dynamixel bus servos and an onboard Jetson Orin NX, designed
    for reproducible machine-learning loco-manipulation research at home.
  zh: ToddlerBot 是斯坦福大学开源的幼儿尺寸人形机器人，身高 0.56 m、重 3.4 kg，全身 30 个主动自由度，BOM 约 6,000 美元，采用 ROBOTIS Dynamixel 总线舵机与 Jetson Orin
    NX 机载电脑，纯 Python 软件栈，目标是在家可复现的机器学习全身运动操作研究平台。
  ko: An open-source child-size humanoid robot from Stanford University, 0.56 m tall and 3.4 kg, with 30 active degrees of
    freedom, a bill of materials of about 6,000 USD, ROBOTIS Dynamixel bus servos and an onboard Jetson Orin NX, designed
    for reproducible machine-learning loco-manipulation research at home.
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
- toddlerbot
- stanford
- research_platform
- dynamixel
- 3d_printed
- reinforcement_learning
- imitation_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/toddlerbot.md（访问日期 2026-07-01），事实均来自其列出的 GitHub 仓库、项目主页与论文 arXiv:2502.00893。 | WP4
    trilingual backfill 2026-08-10: en body retranslated from zh deep-read (1828 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: hshi74/toddlerbot GitHub Repository
  url: https://github.com/hshi74/toddlerbot
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ToddlerBot Project Page
  url: https://toddlerbot.github.io/
  accessed_at: '2026-07-01'
- id: src_003
  type: paper
  title: 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation (arXiv:2502.00893)'
  url: https://arxiv.org/html/2502.00893v2
  accessed_at: '2026-07-01'
---
## 概述

ToddlerBot 是斯坦福大学（TML 与 REALab，作者 Haochen Shi、Weizhuo Wang、Shuran Song、C. Karen Liu）发起的开源幼儿尺寸人形机器人，论文发表于 CoRL 2025（arXiv:2502.00893）。整机高 0.56 m、重 3.4 kg，全身 30 个主动自由度（每条臂 7、每条腿 6、颈 2、腰 2，不含末端执行器），总 BOM 约 6,000 美元，其中约 90% 花在电机与电脑上（来源：调研档案 toddlerbot.md，下同）。

许可证方面，代码与文档采用 MIT License；设计文件（Onshape、STL）采用非商业型 CC 许可，商用受限。项目设计目标是"在家可复现"：3D 打印结构件、现成舵机、pip 一键安装的纯 Python 软件栈，并有论文级复现验证——一名无硬件经验的 CS 学生 3 天内独立完成整机装配（含打印）。GitHub 仓库 `hshi74/toddlerbot` 约 718 stars / 88 forks（2026-07-01 快照，高度活跃），并有 Discord 与微信社区。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 0.56 m / 3.4 kg（3,484 g） | 论文 arXiv:2502.00893 |
| 主动自由度 | 30（臂 7×2、腿 6×2、颈 2、腰 2） | 项目主页 / 论文 |
| 硬件成本（BOM） | 约 $6,000（90% 为电机与电脑） | 论文 |
| 主控 | NVIDIA Jetson Orin NX 16GB | 论文 |
| 传感器 | 双鱼眼相机、胸部 IMU、扬声器、双麦克风 | 项目主页 |
| 续航 | 行走 RL 策略约 19 分钟（过热降频为止） | 项目主页 |
| 新手友好度 | 4.5 / 5（调研档案评估） | 调研档案 |

### 执行器与机械设计

- 采用 ROBOTIS Dynamixel 总线舵机，共 5 种型号按关节空间/扭矩/成本选型（具体型号清单在论文补充材料 VIII-E，档案未逐一列出）。
- 通信为 5V TTL 串行协议、2 Mbps 波特率，30 台电机全状态反馈 50 Hz，使用现成通信板即可。
- 传动设计：直齿轮（臂轴对齐）、耦合锥齿轮（腰 yaw/roll 两电机耦合）、平行连杆（膝、颈 pitch，降惯量）。
- 末端执行器两种可 2 分钟快换：平行夹爪与柔顺手掌；示教臂（leader arms）握把内嵌 FSR 力敏电阻。
- 损坏维修成本低：可承受约 7 次摔倒，修复仅需 21 分钟打印 + 14 分钟装配。

### 计算平台与软件栈

- 主控 Jetson Orin NX 16GB 机上实时推理：300M 参数扩散策略约 100 ms 延迟；2.0 版本用 Foundation Stereo 在机上跑 10 Hz 立体深度估计。
- 纯 Python、pip 一键安装（>= 3.10），含底层控制、RL 训练（MuJoCo / MJX，PPO）、扩散策略训练、真机部署全部代码；不依赖 ROS。
- 数字孪生：3D 打印零点校准治具（1 分钟内完成）+ 可迁移的电机系统辨识（同型号电机只做 1 次 sysID），支撑零样本 sim-to-real；策略在两台实例间零样本互迁，双臂操作 90% 成功率复现。
- 遥操作：同构示教臂 + 掌机（Steam Deck / ROG Ally X）；2.0 支持 Meta Quest 2 VR 遥操作。
- 版本脉络：2025-08-25 发布 ToddlerBot 2.0；2026-01 发布多技能全身运动系统（深度图技能分类器 + 多策略切换）。

### 适合人群

- 适合：想做全身 loco-manipulation、模仿/强化学习数据采集的研究生与进阶爱好者；零基础但动手能力强者亦可按手册完成；Python 栈对 ML 背景新手极友好；3.4 kg 小体型在家操作安全。
- 门槛：BOM $6,000 不算便宜；设计文件为非商业许可；Dynamixel 舵机性能上限（速度/扭矩/通信）制约高动态动作（论文自述）。

## 参考

- [hshi74/toddlerbot GitHub 仓库](https://github.com/hshi74/toddlerbot)
- [ToddlerBot 项目主页](https://toddlerbot.github.io/)
- [论文 arXiv:2502.00893v2](https://arxiv.org/html/2502.00893v2)

## 개요

ToddlerBot은 스탠포드 대학교(TML 및 REALab, 저자 Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu)에서 개발한 오픈소스 유아 크기 휴머노이드 로봇으로, 논문은 CoRL 2025(arXiv:2502.00893)에 게재되었습니다. 전체 높이 0.56m, 무게 3.4kg이며, 전신에 30개의 능동 자유도(각 팔 7개, 각 다리 6개, 목 2개, 허리 2개, 말단 조작기 제외)를 갖추고 있습니다. 총 BOM은 약 6,000달러이며, 이 중 약 90%가 모터와 컴퓨터에 사용됩니다(출처: 조사 파일 toddlerbot.md, 이하 동일).

라이선스 측면에서 코드와 문서는 MIT License를 따릅니다. 설계 파일(Onshape, STL)은 비상업적 CC 라이선스로 상업적 사용이 제한됩니다. 프로젝트 설계 목표는 "집에서 재현 가능"입니다: 3D 프린팅 구조 부품, 기성 서보 모터, pip 한 번 설치로 가능한 순수 Python 소프트웨어 스택, 그리고 논문 수준의 재현 검증이 포함됩니다. 하드웨어 경험이 없는 컴퓨터공학 학생이 3일 만에(프린팅 포함) 독립적으로 전체 조립을 완료했습니다. GitHub 저장소 `hshi74/toddlerbot`은 약 718 stars / 88 forks(2026-07-01 스냅샷, 매우 활발)이며, Discord 및 WeChat 커뮤니티가 운영 중입니다.

## 핵심 내용

### 주요 사양

| 항목 | 수치 | 출처 |
|---|---|---|
| 키 / 무게 | 0.56m / 3.4kg(3,484g) | 논문 arXiv:2502.00893 |
| 능동 자유도 | 30(팔 7×2, 다리 6×2, 목 2, 허리 2) | 프로젝트 홈페이지 / 논문 |
| 하드웨어 비용(BOM) | 약 $6,000(90%는 모터 및 컴퓨터) | 논문 |
| 메인 컨트롤러 | NVIDIA Jetson Orin NX 16GB | 논문 |
| 센서 | 듀얼 피쉬아이 카메라, 흉부 IMU, 스피커, 듀얼 마이크 | 프로젝트 홈페이지 |
| 배터리 지속 시간 | 보행 RL 정책 기준 약 19분(과열로 인한 성능 저하까지) | 프로젝트 홈페이지 |
| 초보자 친화도 | 4.5 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 및 기계 설계

- ROBOTIS Dynamixel 버스 서보 모터 사용, 총 5가지 모델을 관절 공간/토크/비용에 따라 선정(구체적인 모델 목록은 논문 부록 VIII-E에 있으며, 파일에는 개별 나열되지 않음).
- 통신은 5V TTL 직렬 프로토콜, 2Mbps 전송 속도, 30개 모터 전체 상태 피드백 50Hz, 기성 통신 보드 사용 가능.
- 구동 설계: 평기어(팔 축 정렬), 커플링 베벨 기어(허리 yaw/roll 두 모터 커플링), 평행 링크(무릎, 목 pitch, 관성 감소).
- 말단 조작기는 2분 내로 빠르게 교체 가능: 평행 그리퍼와 유연한 손바닥; 리더 암(leader arms) 그립에는 FSR 힘 감지 저항 내장.
- 손상 수리 비용 낮음: 약 7회 낙하 견딤, 수리는 21분 프린팅 + 14분 조립으로 완료.

### 컴퓨팅 플랫폼 및 소프트웨어 스택

- 메인 컨트롤러 Jetson Orin NX 16GB에서 실시간 추론: 300M 파라미터 확산 정책 약 100ms 지연; 2.0 버전은 Foundation Stereo를 사용하여 10Hz 스테레오 깊이 추정.
- 순수 Python, pip 한 번 설치(>= 3.10), 저수준 제어, RL 훈련(MuJoCo / MJX, PPO), 확산 정책 훈련, 실제 로봇 배포 코드 모두 포함; ROS 의존성 없음.
- 디지털 트윈: 3D 프린팅 영점 교정 지그(1분 내 완료) + 전이 가능한 모터 시스템 식별(동일 모델 모터는 1회 sysID만 수행), 제로샷 sim-to-real 지원; 정책은 두 인스턴스 간 제로샷 전이 가능, 양팔 조작 90% 성공률 재현.
- 원격 조작: 동형 리더 암 + 핸드헬드(Steam Deck / ROG Ally X); 2.0은 Meta Quest 2 VR 원격 조작 지원.
- 버전 연혁: 2025-08-25 ToddlerBot 2.0 발표; 2026-01 다중 스킬 전신 운동 시스템(깊이 맵 스킬 분류기 + 다중 정책 전환) 발표.

### 적합한 사용자

- 적합: 전신 loco-manipulation, 모방/강화 학습 데이터 수집을 원하는 대학원생 및 고급 애호가; 기초가 없지만 손재주가 있는 사람도 매뉴얼 따라 완성 가능; Python 스택은 ML 배경 초보자에게 매우 친숙; 3.4kg 소형 체형으로 집에서 안전하게 조작 가능.
- 진입 장벽: BOM $6,000으로 저렴하지 않음; 설계 파일은 비상업적 라이선스; Dynamixel 서보 모터 성능 한계(속도/토크/통신)가 고속 동작을 제한(논문 자체 언급).

## Overview

ToddlerBot is an open-source toddler-sized humanoid robot developed by Stanford University (TML and REALab, authors Haochen Shi, Weizhuo Wang, Shuran Song, C. Karen Liu), with the paper published at CoRL 2025 (arXiv:2502.00893). The robot stands 0.56 m tall, weighs 3.4 kg, and has 30 active degrees of freedom across the body (7 per arm, 6 per leg, 2 in the neck, 2 in the waist, excluding end effectors). The total BOM cost is approximately $6,000, with about 90% spent on motors and computers (source: research archive toddlerbot.md, same below).

In terms of licensing, the code and documentation are released under the MIT License; design files (Onshape, STL) use a non-commercial CC license, restricting commercial use. The project's design goal is "reproducible at home": 3D-printed structural parts, off-the-shelf servo motors, a pure Python software stack installable via pip, and paper-level reproducibility validation—a CS student with no hardware experience independently completed the full assembly (including printing) within 3 days. The GitHub repository `hshi74/toddlerbot` has approximately 718 stars / 88 forks (snapshot as of 2026-07-01, highly active), with Discord and WeChat communities.

## Content

### Key Specifications

| Item | Value | Source |
|---|---|---|
| Height / Weight | 0.56 m / 3.4 kg (3,484 g) | Paper arXiv:2502.00893 |
| Active DOF | 30 (arms 7×2, legs 6×2, neck 2, waist 2) | Project homepage / Paper |
| Hardware Cost (BOM) | ~$6,000 (90% motors and computer) | Paper |
| Main Controller | NVIDIA Jetson Orin NX 16GB | Paper |
| Sensors | Dual fisheye cameras, chest IMU, speaker, dual microphones | Project homepage |
| Battery Life | ~19 minutes of walking RL policy (until thermal throttling) | Project homepage |
| Beginner Friendliness | 4.5 / 5 (research archive assessment) | Research archive |

### Actuators and Mechanical Design

- Uses ROBOTIS Dynamixel bus servos, with 5 models selected based on joint space/torque/cost (specific model list in paper supplementary material VIII-E, not individually listed in the archive).
- Communication uses 5V TTL serial protocol at 2 Mbps baud rate, with full-state feedback from 30 motors at 50 Hz, using off-the-shelf communication boards.
- Transmission design: spur gears (arm axis alignment), coupled bevel gears (waist yaw/roll two-motor coupling), parallel linkages (knee, neck pitch, reducing inertia).
- Two end effectors with 2-minute quick-swap: parallel gripper and compliant palm; leader arms have embedded FSR force-sensing resistors in the grips.
- Low repair cost after damage: can withstand approximately 7 falls, with repair requiring only 21 minutes of printing + 14 minutes of assembly.

### Computing Platform and Software Stack

- Main controller Jetson Orin NX 16GB performs onboard real-time inference: 300M-parameter diffusion policy at ~100 ms latency; version 2.0 uses Foundation Stereo for onboard 10 Hz stereo depth estimation.
- Pure Python, pip one-click installation (>= 3.10), including all code for low-level control, RL training (MuJoCo / MJX, PPO), diffusion policy training, and real-robot deployment; no ROS dependency.
- Digital twin: 3D-printed zero-point calibration jig (completed within 1 minute) + transferable motor system identification (sysID performed only once per motor model), enabling zero-shot sim-to-real; policies transfer zero-shot between two robot instances, with 90% success rate reproduced for bimanual manipulation.
- Teleoperation: isomorphic leader arms + handheld console (Steam Deck / ROG Ally X); version 2.0 supports Meta Quest 2 VR teleoperation.
- Version timeline: ToddlerBot 2.0 released 2025-08-25; multi-skill whole-body motion system released 2026-01 (depth-map skill classifier + multi-policy switching).

### Target Audience

- Suitable for: graduate students and advanced hobbyists interested in whole-body loco-manipulation, imitation/reinforcement learning data collection; beginners with strong hands-on skills can also complete assembly following the manual; the Python stack is extremely friendly to newcomers with ML backgrounds; the 3.4 kg compact size is safe for home operation.
- Barriers: BOM of $6,000 is not cheap; design files use a non-commercial license; Dynamixel servo performance limits (speed/torque/communication) constrain highly dynamic motions (as stated in the paper).
