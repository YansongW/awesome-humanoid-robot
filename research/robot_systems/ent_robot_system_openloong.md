---
$id: ent_robot_system_openloong
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: OpenLoong (Qinglong) Open-Source Humanoid Robot
  zh: OpenLoong / 青龙开源人形机器人
  ko: OpenLoong (Qinglong) Open-Source Humanoid Robot
summary:
  en: The full-size open-source humanoid reference platform from China's National and Local Co-built Humanoid Robot Innovation
    Center, 185 cm and over 80 kg with 43 active degrees of freedom including dexterous hands, open-sourced under the OpenAtom
    Foundation with an MPC plus WBC whole-body control framework deployable in MuJoCo.
  zh: OpenLoong（开放龙）/ 青龙是国家地方共建人形机器人创新中心推出的全尺寸开源人形机器人公版机，身高超 185 cm、体重超 80 kg，全身 43 个主动自由度（含五指灵巧手），经开放原子开源基金会孵化运营，开源内容包括硬件图纸、基于
    MPC + WBC 的全身动力学控制框架（可部署于 MuJoCo 仿真）与数据集。
  ko: The full-size open-source humanoid reference platform from China's National and Local Co-built Humanoid Robot Innovation
    Center, 185 cm and over 80 kg with 43 active degrees of freedom including dexterous hands, open-sourced under the OpenAtom
    Foundation with an MPC plus WBC whole-body control framework deployable in MuJoCo.
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
- openloong
- qinglong
- full_size_humanoid
- mpc
- whole_body_control
- ethercat
- openatom
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/openloong-qinglong.md（访问日期 2026-07-01）。BOM 成本与执行器具体型号在公开检索中未见统一规格表，标注为未知；硬件/数据集仓库许可证为自定义或未明确（NOASSERTION）。
    | WP4 trilingual backfill 2026-08-10: en body retranslated from zh deep-read (1809 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: OpenLoong-Dyn-Control GitHub Repository (loongOpen)
  url: https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OpenLoong on AtomGit
  url: https://atomgit.com/openloong
  accessed_at: '2026-07-01'
---
## 概述

OpenLoong（开放龙）/ "青龙"（Qinglong）是由国家地方共建人形机器人创新中心（上海，2023-12-28 成立、2024-05-17 揭牌）与人形机器人（上海）有限公司推出的全尺寸开源人形机器人公版机，2024-12-19 通过开放原子开源基金会（OpenAtom）TOC 评审，捐赠基金会孵化运营。整机身高超 185 cm、体重超 80 kg，全身 43 个主动自由度（含五指灵巧手，覆盖头/臂/腿/腰/踝）（来源：调研档案 openloong-qinglong.md，下同）。

项目定位是产业"公版机/根技术"，被媒体称为全球首个全尺寸人形全栈开源（硬件图纸 + MPC/WBC 控制 + 数据集）。主要代码仓库采用 Apache-2.0 许可证；OpenLoong-Hardware、OpenLoong-Dataset 许可证为自定义/未明确（GitHub 标记 NOASSERTION）。硬件成本未知——开源公版机不自售，媒体口径"最终由生产商定价"。2025-08 社区另推出更轻量、更低成本的 NanoLoong（小型双足）并已开源。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 超 185 cm / 超 80 kg | 媒体与官方演讲口径 |
| 主动自由度 | 43（含五指灵巧手） | 媒体报道 |
| 硬件成本（BOM） | 未知（公版机不自售，由生产商定价） | 调研档案 |
| 主控 | 400 TOPS 高算力控制器；具身智能操作系统（us 级响应目标） | 2024 WAIC 发布口径 |
| 总线 | EtherCAT | 行业分析文章与 SDK 仓库佐证 |
| 新手友好度 | 2 / 5（调研档案评估） | 调研档案 |

### 执行器与硬件

- 2024 款"青龙"以旋转执行器为主驱动单元（2024 WAIC 官方演讲口径）；下一代公版机计划采用直线执行器。
- 具体电机/减速器型号、扭矩参数未见统一规格表，需查阅 OpenLoong-Hardware 仓库的选型文件。
- 硬件开源包含设计指标、STEP 模型、电路原理图、安装维护手册。
- 传感器：官方未发布统一清单；生态项目（dora-rs/dora-openloong）实机集成 Intel RealSense D435 RGB-D 相机与麦克风阵列。

### 软件栈

- OpenLoong-Dyn-Control：基于 MPC（模型预测控制）+ WBC（全身控制）的全身动力学控制框架，可部署于 MuJoCo 仿真，提供行走/跳跃/盲踩障碍三个示例，已在实物样机实现行走与盲踩障碍；内置主要依赖、分层模块化、强调易部署/易扩展/易理解。
- 其他仓库：Gymloong（训练平台）、MiniGym、Unity-RL-Playground、OpenLoong-ROS、OpenLoong-Brain（大模型技能调度）、loong_driver_sdk、loong_sim/loong_deployment、OpenLoong-Dataset（行走/桌面分拣/场景作业数据）。
- 同步发布于 GitHub（`loongOpen` 组织）与 AtomGit（atomgit.com/openloong）；软件层另有"朱雀"大脑大模型、"玄武"小脑强化学习模型、"白虎"数据集、"麒麟"训练场等配套体系（属创新中心整体生态，非全部开源）。

### 社区与适合人群

- openloong.org.cn 社区 + SIG 组 + 线上线下活动（ROSCon China、ROS 暑期学校合作）；中文文档为主，对国内开发者友好，英文资料少。
- GitHub 星标快照：OpenLoong-Dyn-Control 339 stars、Unity-RL-Playground 315 stars、OpenLoong-Hardware 115 stars（2026-07-01 检索时点），组织整体在维护。
- 适合：国内高校/企业团队做全尺寸整机二次开发；185 cm / 80 kg 全尺寸机型个人无法在家复现，个人新手建议只用其 MuJoCo 控制框架做学习，或关注 NanoLoong。

## 参考

- [OpenLoong-Dyn-Control 仓库（MPC+WBC 框架）](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md)
- [AtomGit 镜像](https://atomgit.com/openloong)
- [dora-rs/dora-openloong 生态项目](https://github.com/dora-rs/dora-openloong)

## 개요

OpenLoong(오픈롱) / "칭롱"(Qinglong)은 국가지방공동건설 휴머노이드 로봇 혁신센터(상하이, 2023-12-28 설립, 2024-05-17 제막)와 휴머노이드 로봇(상하이) 유한회사가 출시한 풀사이즈 오픈소스 휴머노이드 로봇 공용 모델로, 2024-12-19 오픈아톰 오픈소스 재단(OpenAtom) TOC 심의를 통과하여 재단에 기증되어 인큐베이팅 및 운영됩니다. 전체 기계 높이 185cm 이상, 체중 80kg 이상, 전신 43개의 능동 자유도(5지 다관절 핸드 포함, 머리/팔/다리/허리/발목 커버)(출처: 조사 파일 openloong-qinglong.md, 이하 동일).

프로젝트의 포지셔닝은 산업 "공용 모델/근본 기술"로, 미디어에서는 세계 최초의 풀사이즈 휴머노이드 풀스택 오픈소스(하드웨어 설계도 + MPC/WBC 제어 + 데이터셋)라고 불립니다. 주요 코드 저장소는 Apache-2.0 라이선스를 사용하며, OpenLoong-Hardware, OpenLoong-Dataset의 라이선스는 사용자 정의/미확정(GitHub에서 NOASSERTION으로 표시)입니다. 하드웨어 비용은 알 수 없음——오픈소스 공용 모델은 자체 판매하지 않으며, 미디어에서는 "최종적으로 생산자가 가격을 결정"한다고 밝혔습니다. 2025-08 커뮤니티에서는 더 가볍고 저렴한 NanoLoong(소형 이족 보행)을 추가로 출시하여 오픈소스화했습니다.

## 핵심 내용

### 주요 파라미터

| 항목 | 수치 | 출처 |
|---|---|---|
| 신장 / 체중 | 185cm 이상 / 80kg 이상 | 미디어 및 공식 발표 자료 |
| 능동 자유도 | 43(5지 다관절 핸드 포함) | 미디어 보도 |
| 하드웨어 비용(BOM) | 알 수 없음(공용 모델 자체 판매 안 함, 생산자가 가격 결정) | 조사 파일 |
| 메인 컨트롤러 | 400 TOPS 고연산 컨트롤러; 임베디드 지능 운영체제(us 수준 응답 목표) | 2024 WAIC 발표 자료 |
| 버스 | EtherCAT | 업계 분석 기사 및 SDK 저장소 증거 |
| 초보자 친화도 | 2 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 및 하드웨어

- 2024년형 "칭롱"은 회전 액추에이터를 주 구동 유닛으로 사용(2024 WAIC 공식 발표 자료); 차세대 공용 모델은 직선 액추에이터를 채택할 계획.
- 구체적인 모터/감속기 모델, 토크 파라미터는 통일된 사양표가 없으며, OpenLoong-Hardware 저장소의 선정 파일을 참조해야 함.
- 하드웨어 오픈소스에는 설계 사양, STEP 모델, 회로도, 설치 및 유지보수 매뉴얼이 포함됨.
- 센서: 공식적으로 통일된 목록이 발표되지 않음; 생태 프로젝트(dora-rs/dora-openloong) 실제 기계에는 Intel RealSense D435 RGB-D 카메라와 마이크 어레이가 통합됨.

### 소프트웨어 스택

- OpenLoong-Dyn-Control: MPC(모델 예측 제어) + WBC(전신 제어) 기반의 전신 동역학 제어 프레임워크로, MuJoCo 시뮬레이션에 배포 가능하며 걷기/점프/맹목 장애물 밟기 세 가지 예제를 제공하고, 실제 프로토타입에서 걷기와 맹목 장애물 밟기를 구현함; 주요 종속성 내장, 계층적 모듈화, 배포/확장/이해 용이성 강조.
- 기타 저장소: Gymloong(훈련 플랫폼), MiniGym, Unity-RL-Playground, OpenLoong-ROS, OpenLoong-Brain(대형 모델 스킬 스케줄링), loong_driver_sdk, loong_sim/loong_deployment, OpenLoong-Dataset(걷기/테이블 분류/현장 작업 데이터).
- GitHub(`loongOpen` 조직)와 AtomGit(atomgit.com/openloong)에 동시 게시; 소프트웨어 계층에는 "주작" 뇌 대형 모델, "현무" 소뇌 강화 학습 모델, "백호" 데이터셋, "기린" 훈련장 등 지원 시스템이 있음(혁신센터 전체 생태계에 속하며, 전부 오픈소스는 아님).

### 커뮤니티 및 적합 대상

- openloong.org.cn 커뮤니티 + SIG 그룹 + 온/오프라인 활동(ROSCon China, ROS 여름학교 협력); 중국어 문서 위주로 국내 개발자에게 친화적이며, 영어 자료는 적음.
- GitHub 스타 수 스냅샷: OpenLoong-Dyn-Control 339 stars, Unity-RL-Playground 315 stars, OpenLoong-Hardware 115 stars(2026-07-01 검색 시점), 조직 전체가 유지 관리 중.
- 적합 대상: 국내 대학/기업 팀의 풀사이즈 기계 2차 개발; 185cm / 80kg 풀사이즈 모델은 개인이 집에서 재현할 수 없으며, 개인 초보자는 MuJoCo 제어 프레임워크만 학습용으로 사용하거나 NanoLoong에 주목할 것을 권장.

## Overview

OpenLoong (Open Dragon) / "Qinglong" is a full-size open-source humanoid robot reference model launched by the National and Local Co-built Humanoid Robot Innovation Center (Shanghai, established 2023-12-28, unveiled 2024-05-17) and Humanoid Robot (Shanghai) Co., Ltd. On 2024-12-19, it passed the TOC review of the OpenAtom Foundation and was donated to the foundation for incubation and operation. The robot stands over 185 cm tall, weighs over 80 kg, and has 43 active degrees of freedom (including five-finger dexterous hands, covering head/arms/legs/waist/ankles) (source: research file openloong-qinglong.md, same below).

The project is positioned as an industry "reference model/root technology" and has been called by the media the world's first full-size humanoid full-stack open-source platform (hardware blueprints + MPC/WBC control + datasets). The main code repositories use the Apache-2.0 license; the OpenLoong-Hardware and OpenLoong-Dataset licenses are custom/unspecified (marked NOASSERTION on GitHub). Hardware cost is unknown—the open-source reference model is not sold directly, with media reports stating "pricing is ultimately set by manufacturers." In 2025-08, the community also released a lighter, lower-cost NanoLoong (small biped) which has been open-sourced.

## Content

### Key Parameters

| Item | Value | Source |
|---|---|---|
| Height / Weight | Over 185 cm / Over 80 kg | Media and official presentation statements |
| Active DOF | 43 (including five-finger dexterous hands) | Media reports |
| Hardware Cost (BOM) | Unknown (reference model not sold directly; priced by manufacturers) | Research file |
| Main Controller | 400 TOPS high-compute controller; embodied intelligence operating system (us-level response target) | 2024 WAIC release statements |
| Bus | EtherCAT | Industry analysis articles and SDK repository evidence |
| Beginner Friendliness | 2 / 5 (research file assessment) | Research file |

### Actuators and Hardware

- The 2024 "Qinglong" uses rotary actuators as the primary drive units (per 2024 WAIC official presentation); the next-generation reference model plans to adopt linear actuators.
- Specific motor/reducer models and torque parameters lack a unified specification table; refer to the selection files in the OpenLoong-Hardware repository.
- Open-source hardware includes design specifications, STEP models, circuit schematics, and installation/maintenance manuals.
- Sensors: no unified list officially released; ecosystem projects (dora-rs/dora-openloong) integrate Intel RealSense D435 RGB-D cameras and microphone arrays on real hardware.

### Software Stack

- OpenLoong-Dyn-Control: A whole-body dynamics control framework based on MPC (Model Predictive Control) + WBC (Whole-Body Control), deployable in MuJoCo simulation, providing three examples—walking, jumping, and blind obstacle stepping—with walking and blind obstacle stepping already demonstrated on physical prototypes; includes built-in core dependencies, modular layering, and emphasizes ease of deployment/extension/understanding.
- Other repositories: Gymloong (training platform), MiniGym, Unity-RL-Playground, OpenLoong-ROS, OpenLoong-Brain (large-model skill scheduling), loong_driver_sdk, loong_sim/loong_deployment, OpenLoong-Dataset (walking/tabletop sorting/scene operation data).
- Released simultaneously on GitHub (`loongOpen` organization) and AtomGit (atomgit.com/openloong); the software layer also includes supporting systems such as the "Zhuque" brain large model, "Xuanwu" cerebellum reinforcement learning model, "Baihu" dataset, and "Qilin" training ground (part of the innovation center's overall ecosystem, not all open-sourced).

### Community and Target Audience

- openloong.org.cn community + SIG groups + online/offline events (ROSCon China, ROS summer school collaborations); primarily Chinese documentation, friendly to domestic developers, with limited English resources.
- GitHub star snapshot: OpenLoong-Dyn-Control 339 stars, Unity-RL-Playground 315 stars, OpenLoong-Hardware 115 stars (as of 2026-07-01 retrieval), with the organization actively maintained.
- Suitable for: domestic university/enterprise teams conducting full-size machine secondary development; the 185 cm / 80 kg full-size model cannot be replicated at home by individuals—individual beginners are advised to use only its MuJoCo control framework for learning, or follow NanoLoong instead.
