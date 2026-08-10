---
$id: ent_robot_system_berkeley_humanoid_lite
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Berkeley Humanoid Lite
  zh: 伯克利轻量人形机器人
  ko: Berkeley Humanoid Lite
summary:
  en: An open-source 0.8 m, 16 kg humanoid robot from UC Berkeley with 22 active degrees of freedom and a sub-5,000 USD bill
    of materials, built around self-designed quasi-direct-drive actuators with 3D-printed cycloidal reducers, trained in NVIDIA
    Isaac Lab with zero-shot sim-to-real reinforcement learning.
  zh: Berkeley Humanoid Lite 是 UC Berkeley 开源的轻量人形机器人，身高 0.8 m、重 16 kg，22 个主动自由度，整机 BOM 美国采购约 4,312 美元、中国采购约 3,236 美元，核心为
    3D 打印摆线针轮减速的自研准直驱执行器，基于 NVIDIA Isaac Lab 训练并实现零样本 sim-to-real 的 RL 行走。
  ko: An open-source 0.8 m, 16 kg humanoid robot from UC Berkeley with 22 active degrees of freedom and a sub-5,000 USD bill
    of materials, built around self-designed quasi-direct-drive actuators with 3D-printed cycloidal reducers, trained in NVIDIA
    Isaac Lab with zero-shot sim-to-real reinforcement learning.
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
- berkeley_humanoid_lite
- uc_berkeley
- quasi_direct_drive
- cycloidal_reducer
- 3d_printed
- reinforcement_learning
- research_platform
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/berkeley-humanoid-lite.md（访问日期 2026-07-01），事实均来自其列出的 GitHub 仓库、项目主页、论文 arXiv:2504.17249
    与 Berkeley EECS 技术报告 EECS-2025-207。 | WP4 trilingual backfill 2026-08-10: en body retranslated from zh deep-read (1799
    chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: HybridRobotics/Berkeley-Humanoid-Lite GitHub Repository
  url: https://github.com/HybridRobotics/Berkeley-Humanoid-Lite
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Berkeley Humanoid Lite Project Page
  url: https://lite.berkeley-humanoid.org/
  accessed_at: '2026-07-01'
- id: src_003
  type: paper
  title: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot (arXiv:2504.17249)'
  url: https://arxiv.org/abs/2504.17249
  accessed_at: '2026-07-01'
---
## 概述

Berkeley Humanoid Lite 是 UC Berkeley 混合机器人实验室（Hybrid Robotics Group，Koushil Sreenath 团队）与 SLICE 实验室发起的开源轻量人形机器人，属 BAIR Commons HIC 仓库，论文 arXiv:2504.17249（2025-04）。整机高 0.8 m、重 16 kg，22 个主动自由度（每条腿 6、每条臂 5），整机 BOM 美国采购约 4,312 美元、中国采购约 3,236 美元，官方宣传口径"低于 $5,000"（来源：调研档案 berkeley-humanoid-lite.md，下同）。

许可证方面，代码采用 MIT License，CAD 等其他资产采用 CC BY-SA 4.0。项目性价比在开源人形中属第一梯队：GitHub 仓库 `HybridRobotics/Berkeley-Humanoid-Lite` 约 1,417 stars / 215 forks（2026-07-01 快照，活跃），有 Discord 社区与微信群。全部结构件可用普通桌面 FDM 打印机（PLA）制造，组装周期约 3 天（现货件一周内到货、打印约一周）。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 0.8 m / 16 kg | 论文 arXiv:2504.17249 |
| 主动自由度 | 22（腿 6×2、臂 5×2） | 技术报告对比表 |
| 硬件成本（BOM） | 美国约 $4,312 / 中国约 $3,236（官方口径 sub-$5,000） | EECS-2025-207 技术报告 |
| 主控 | Intel N95 迷你 PC（约 $129） | 论文 |
| 通信 | 四肢各一条 CAN 2.0 总线（1 Mbps），执行器与 IMU 250 Hz | 论文 |
| 传感器 | BNO085 IMU（经 Arduino 以 USB 接入）；SteamVR 基站 + 手柄遥操作 | 论文 |
| 电池 | 6S 4000 mAh LiPo，约 30 分钟续航 | 论文 |
| 新手友好度 | 3.5 / 5（调研档案评估） | 调研档案 |

### 执行器方案

- 两种规格自研准直驱（quasi-direct-drive）执行器：6512（10 台）与 5010（12 台），核心为 3D 打印摆线针轮（cycloidal）减速器，全部结构件可用桌面 FDM 打印机（PLA）制造。
- 6512 执行器 BOM 约 $188（美国）/ $157（中国）：MAD Components M6C12 150KV 无人机无刷电机（$129）+ ST B-G431B-ESC1 驱动板（$19）+ AS5600 磁编码器（$3）+ 轴承/紧固件/打印件。
- 摆线齿轮多齿分担载荷，论文用 60 小时耐久测试验证塑料齿轮可靠性；兼容 Moteus / ODrive / VESC 等第三方驱动器。
- 单条 CAN 总线最多 64 设备，便于重构成四足/双足/半人马等形态；另有成人尺寸扩展构型（7 自由度腿 + 灵巧手）。

### 软件栈

- 训练与仿真基于 NVIDIA Isaac Lab 组织目录结构，URDF / MJCF / USD 三种描述格式齐全，支持策略训练与 sim2sim 验证。
- RL 运动控制策略实现零样本 sim-to-real；部署代码 `berkeley_humanoid_lite_lowlevel` 为真机底层 C 代码，独立于训练栈，单独拷到机上即可部署。
- 支持动捕、SteamVR 遥操作双臂（魔方、写字、搭积木演示）。

### 适合人群

- 适合：有一定动手能力、目标是做 RL 运动控制研究的个人/实验室——$4–5k 就能造出能跑 RL 行走的 22 自由度人形，文档 + BOM + 打印文件齐全，社区活跃。
- 门槛：需要自己打印摆线减速器并装配 22 台执行器、焊接 CAN 总线、烧录 FOC 固件，嵌入式与 3D 打印经验不足者容易卡壳；16 kg 机型已需要一定的操作安全意识；非零基础友好。

## 参考

- [HybridRobotics/Berkeley-Humanoid-Lite GitHub 仓库](https://github.com/HybridRobotics/Berkeley-Humanoid-Lite)
- [项目主页](https://lite.berkeley-humanoid.org/)
- [论文 arXiv:2504.17249](https://arxiv.org/abs/2504.17249)
- [Berkeley EECS 技术报告 EECS-2025-207（完整 BOM 表）](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf)

## 개요

Berkeley Humanoid Lite는 UC Berkeley 혼합 로봇 연구실(Hybrid Robotics Group, Koushil Sreenath 팀)과 SLICE 연구소가 시작한 오픈소스 경량 휴머노이드 로봇으로, BAIR Commons HIC 저장소에 속하며 논문 arXiv:2504.17249(2025-04)에 해당합니다. 전체 기계 높이 0.8m, 무게 16kg, 22개의 능동 자유도(다리 각 6개, 팔 각 5개)를 가지며, 전체 BOM은 미국 조달 시 약 4,312달러, 중국 조달 시 약 3,236달러로, 공식 홍보 문구는 "5,000달러 미만"입니다(출처: 조사 파일 berkeley-humanoid-lite.md, 이하 동일).

라이선스 측면에서 코드는 MIT License를, CAD 등 기타 자산은 CC BY-SA 4.0을 따릅니다. 프로젝트의 가성비는 오픈소스 휴머노이드 중 최상위권에 속합니다. GitHub 저장소 `HybridRobotics/Berkeley-Humanoid-Lite`는 약 1,417 stars / 215 forks(2026-07-01 스냅샷, 활성 상태)이며, Discord 커뮤니티와 위챗 그룹이 있습니다. 모든 구조 부품은 일반 데스크탑 FDM 프린터(PLA)로 제작 가능하며, 조립 주기는 약 3일입니다(재고 부품은 일주일 내 도착, 출력은 약 일주일 소요).

## 핵심 내용

### 주요 파라미터

| 항목 | 수치 | 출처 |
|---|---|---|
| 키 / 무게 | 0.8 m / 16 kg | 논문 arXiv:2504.17249 |
| 능동 자유도 | 22(다리 6×2, 팔 5×2) | 기술 보고서 비교표 |
| 하드웨어 비용(BOM) | 미국 약 $4,312 / 중국 약 $3,236(공식 문구 sub-$5,000) | EECS-2025-207 기술 보고서 |
| 메인 컨트롤러 | Intel N95 미니 PC(약 $129) | 논문 |
| 통신 | 사지 각각 하나의 CAN 2.0 버스(1 Mbps), 액추에이터 및 IMU 250 Hz | 논문 |
| 센서 | BNO085 IMU(Arduino를 통해 USB 연결); SteamVR 베이스 스테이션 + 컨트롤러 원격 조작 | 논문 |
| 배터리 | 6S 4000 mAh LiPo, 약 30분 사용 시간 | 논문 |
| 초보자 친화도 | 3.5 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 솔루션

- 두 가지 사양의 자체 개발 준직접 구동(quasi-direct-drive) 액추에이터: 6512(10대) 및 5010(12대), 핵심은 3D 프린팅 사이클로이드 감속기(cycloidal reducer)이며, 모든 구조 부품은 데스크탑 FDM 프린터(PLA)로 제작 가능.
- 6512 액추에이터 BOM 약 $188(미국) / $157(중국): MAD Components M6C12 150KV 드론 브러시리스 모터($129) + ST B-G431B-ESC1 드라이버 보드($19) + AS5600 자기 엔코더($3) + 베어링/체결구/출력물.
- 사이클로이드 기어는 다중 톱니가 하중을 분담하며, 논문에서는 60시간 내구성 테스트로 플라스틱 기어의 신뢰성을 검증; Moteus / ODrive / VESC 등 타사 드라이버와 호환.
- 단일 CAN 버스는 최대 64개 장치를 지원하여, 사족/이족/켄타우로스 등 다양한 형태로 재구성 용이; 성인 크기 확장 구성(7자유도 다리 + 다관절 손)도 있음.

### 소프트웨어 스택

- 훈련 및 시뮬레이션은 NVIDIA Isaac Lab 기반으로 디렉토리 구조를 구성하며, URDF / MJCF / USD 세 가지 설명 형식을 모두 갖추어 정책 훈련 및 sim2sim 검증 지원.
- RL 운동 제어 정책은 제로샷 sim-to-real 구현; 배포 코드 `berkeley_humanoid_lite_lowlevel`은 실제 기계 저수준 C 코드로, 훈련 스택과 독립적이며 기계에 별도로 복사하여 배포 가능.
- 모션 캡처, SteamVR 원격 조작 양팔(큐브 맞추기, 글쓰기, 블록 쌓기 데모) 지원.

### 적합한 대상

- 적합: 어느 정도 실무 능력을 갖추고 RL 운동 제어 연구를 목표로 하는 개인/연구실 — $4–5k로 RL 보행이 가능한 22자유도 휴머노이드를 제작할 수 있으며, 문서 + BOM + 출력 파일이 완비되고 커뮤니티가 활성화되어 있음.
- 진입 장벽: 사이클로이드 감속기를 직접 출력하고 22대의 액추에이터를 조립하며, CAN 버스를 납땜하고 FOC 펌웨어를 플래싱해야 하므로, 임베디드 및 3D 프린팅 경험이 부족한 경우 어려움을 겪을 수 있음; 16kg 기종은 이미 일정 수준의 작업 안전 의식이 필요; 초보자에게 친화적이지 않음.

## Overview

Berkeley Humanoid Lite is an open-source lightweight humanoid robot initiated by UC Berkeley's Hybrid Robotics Group (Koushil Sreenath's team) and the SLICE Lab. It is part of the BAIR Commons HIC repository, with the paper arXiv:2504.17249 (2025-04). The robot stands 0.8 m tall, weighs 16 kg, and has 22 active degrees of freedom (6 per leg, 5 per arm). The total BOM costs approximately $4,312 when sourced in the US and approximately $3,236 when sourced in China, with the official promotional claim of "under $5,000" (source: research archive berkeley-humanoid-lite.md, same below).

In terms of licensing, the code is under the MIT License, while other assets such as CAD files are under CC BY-SA 4.0. The project's cost-effectiveness ranks among the top tier of open-source humanoids: the GitHub repository `HybridRobotics/Berkeley-Humanoid-Lite` has approximately 1,417 stars / 215 forks (snapshot as of 2026-07-01, active), with a Discord community and WeChat group. All structural components can be manufactured using a standard desktop FDM printer (PLA), with an assembly cycle of about 3 days (off-the-shelf parts arrive within a week, printing takes about a week).

## Content

### Key Parameters

| Item | Value | Source |
|---|---|---|
| Height / Weight | 0.8 m / 16 kg | Paper arXiv:2504.17249 |
| Active Degrees of Freedom | 22 (legs 6×2, arms 5×2) | Technical report comparison table |
| Hardware Cost (BOM) | US approximately $4,312 / China approximately $3,236 (official claim sub-$5,000) | EECS-2025-207 technical report |
| Main Controller | Intel N95 mini PC (approximately $129) | Paper |
| Communication | One CAN 2.0 bus per limb (1 Mbps), actuators and IMU at 250 Hz | Paper |
| Sensors | BNO085 IMU (connected via USB through Arduino); SteamVR base stations + controllers for teleoperation | Paper |
| Battery | 6S 4000 mAh LiPo, approximately 30 minutes of runtime | Paper |
| Beginner Friendliness | 3.5 / 5 (assessment from research archive) | Research archive |

### Actuator Design

- Two variants of custom quasi-direct-drive actuators: 6512 (10 units) and 5010 (12 units), centered around 3D-printed cycloidal reducers, with all structural components manufacturable using a desktop FDM printer (PLA).
- The 6512 actuator BOM is approximately $188 (US) / $157 (China): MAD Components M6C12 150KV drone brushless motor ($129) + ST B-G431B-ESC1 driver board ($19) + AS5600 magnetic encoder ($3) + bearings/fasteners/printed parts.
- The cycloidal gears distribute load across multiple teeth, and the paper validates the reliability of plastic gears through 60-hour endurance testing; compatible with third-party drivers such as Moteus / ODrive / VESC.
- A single CAN bus supports up to 64 devices, facilitating reconfiguration into quadruped/biped/centaur forms; an adult-sized extended configuration (7-DOF legs + dexterous hands) is also available.

### Software Stack

- Training and simulation are based on NVIDIA Isaac Lab with an organized directory structure, providing URDF / MJCF / USD description formats, supporting policy training and sim2sim validation.
- RL locomotion control policies achieve zero-shot sim-to-real transfer; the deployment code `berkeley_humanoid_lite_lowlevel` is low-level C code for the real robot, independent of the training stack, and can be deployed by simply copying it to the robot.
- Supports motion capture and SteamVR teleoperation of both arms (demonstrations include solving a Rubik's cube, writing, and stacking blocks).

### Target Audience

- Suitable for: individuals/labs with some hands-on ability aiming to research RL locomotion control—for $4–5k, you can build a 22-DOF humanoid capable of RL walking, with complete documentation + BOM + print files and an active community.
- Barriers: you need to print the cycloidal reducers yourself, assemble 22 actuators, solder the CAN bus, and flash FOC firmware; those lacking embedded systems and 3D printing experience may get stuck; the 16 kg platform already requires a certain awareness of operational safety; not beginner-friendly.
