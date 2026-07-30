---
$id: ent_robot_system_inmoov
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: InMoov
  zh: InMoov 3D 打印人形机器人
  ko: InMoov
summary:
  en: The first open-source 3D-printed life-size humanoid robot, started in 2012 by French sculptor Gael Langevin, printable
    on a home printer for as little as several hundred dollars in parts, with tendon-driven five-finger hands, standard hobby
    servos, Arduino low-level control and the MyRobotLab interaction framework, defaulting to an upper body without legs.
  zh: InMoov 是法国雕塑家 Gaël Langevin 于 2012 年发起的开源 3D 打印真人尺寸人形机器人，全部零件可在家用 3D 打印机上复现，成本可低至数百美元，标志性子系统为腱驱动五指手，采用标准航模舵机 + Arduino
    低层控制 + MyRobotLab 交互框架，默认仅为上半身（无腿），是历史上被复制最多的开源人形机器人。
  ko: The first open-source 3D-printed life-size humanoid robot, started in 2012 by French sculptor Gael Langevin, printable
    on a home printer for as little as several hundred dollars in parts, with tendon-driven five-finger hands, standard hobby
    servos, Arduino low-level control and the MyRobotLab interaction framework, defaulting to an upper body without legs.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- intelligence
functional_roles:
- system
- knowledge
tags:
- open_source
- humanoid_robot
- inmoov
- 3d_printed
- myrobotlab
- arduino
- hobby_servo
- tendon_driven_hand
- maker
- hri
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 内容整理自调研档案 data/roadmap/research/inmoov.md（访问日期 2026-07-01）。无官方 BOM，成本为媒体/第三方数据库估算区间；身高/重量/自由度因构建者而异，所列数值为第三方报道口径。3D
    打印部件为 CC BY-NC 3.0 非商业许可。
sources:
- id: src_001
  type: website
  title: InMoov Official Project Page
  url: https://inmoov.fr/project/
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MyRobotLab GitHub Repository
  url: https://github.com/MyRobotLab/myrobotlab
  accessed_at: '2026-07-01'
---

## 概述

InMoov 是法国雕塑家/模型师 Gaël Langevin（Factice Ateliers）于 2012 年 1 月发起的个人开源项目，是首个可用家用 3D 打印机复现的真人尺寸开源人形机器人，软件生态依托 MyRobotLab 社区。整机真人尺寸（约 1.75–1.8 m 的报道口径），默认仅为上半身（头、躯干、双臂、双手），无腿；重量因构建而异（第三方报道约 30 kg，非官方数据）（来源：调研档案 inmoov.md，下同）。

许可证：3D 打印部件 CC BY-NC 3.0（署名-非商业）；MyRobotLab 框架历史上 GPLv2，现 GitHub 仓库标注 Apache-2.0。无官方 BOM，成本为媒体估算：约 $800（2015 年整机报道）；$900+ 且不含躯干与头部（2013 年报道）；$800–2,500 视舵机/电子件选型（2025 年第三方数据库）。到 2018 年全球已有近 1,000 台 InMoov 复制机（ESILV 报道），是历史上被复制最多的开源人形机器人。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 约 1.75–1.8 m / 约 30 kg（均第三方报道口径，非官方） | 第三方数据库 |
| 自由度 | 典型全构建约 28 台舵机、22–30 个可控自由度（第三方口径）；另有"约 45 关节"报道 | 第三方数据库 |
| 硬件成本 | 无官方 BOM；$800–2,500 估算区间 | 媒体 / 第三方数据库 |
| 低层控制 | Arduino Mega（舵机 PWM） | 调研档案 |
| 高层控制 | PC 运行 MyRobotLab（Java 框架，Python 绑定） | 调研档案 |
| 供电 | 通常台式电源（AC），移动底座版本可配电池 | 调研档案 |
| 新手友好度 | 3 / 5（调研档案评估） | 调研档案 |

### 执行器与机械

- 标准航模舵机（MG996R、HS-805BB 等社区常用型号），无定制执行器。
- 手部为腱（渔线）驱动五指，可抓握、比划手语级手势，是 InMoov 最具标志性的子系统（单手打印约 13–14 小时）；双手为全驱动五指（每手 5–6 舵机）。
- 设计软件为开源的 Blender；所有部件可在 12×12×12 cm 打印区间的家用 3D 打印机上复现。
- 工程量大：290 个零件、约 600 小时 3D 打印 + 约 400 小时装配调试（ESILV 学生团队报道口径）。

### 软件栈与传感器

- MyRobotLab（MRL）：服务化机器人框架，内置语音识别、OpenCV 视觉、聊天机器人（Program AB）、Web UI、手势捕捉等；主要面向交互而非运动控制。
- 社区有 ROS 移植（如 alansrobotlab/inmoov_ros，46 stars，2019 年后停更）；近年社区常见 Jetson/Raspberry Pi + LLM 的现代化改造。
- 传感器为社区自定义：双眼 USB 摄像头、麦克风（语音识别）、可选 Kinect/超声/IMU/RealSense。
- 无官方运动学/动力学仿真栈（Gazebo/Isaac/MuJoCo 均无官方支持）——它不是为行走研究设计的平台。

### 适合人群

- 适合：想低成本体验"造一台真人尺寸机器人"的 maker、艺术/教育/HRI 场景——零件全部家用打印机可造、舵机+Arduino 技术栈门槛低、社区大、做成后交互演示效果（语音、视觉、手势）震撼，是极佳的"机器人 maker 入门第一课"。
- 门槛：非商业许可限制商用；装配工程数百小时；没有腿、不能行走，动力学/RL/ROS 等现代人形技术栈在这里学不到；舵机精度与寿命有限。

## 参考

- [InMoov 官方项目页](https://inmoov.fr/project/)
- [MyRobotLab/myrobotlab GitHub 仓库](https://github.com/MyRobotLab/myrobotlab)
- [MyRobotLab/InMoov2（新一代构建包）](https://github.com/MyRobotLab/InMoov2)

## 개요

InMoov는 프랑스 조각가/모델러 Gaël Langevin(Factice Ateliers)이 2012년 1월에 시작한 개인 오픈소스 프로젝트로, 가정용 3D 프린터로 재현 가능한 최초의 실물 크기 오픈소스 휴머노이드 로봇이며, 소프트웨어 생태계는 MyRobotLab 커뮤니티에 기반을 두고 있습니다. 전체 기계는 실물 크기(약 1.75–1.8m로 보고됨)이며, 기본적으로 상반신(머리, 몸통, 양팔, 양손)만 있고 다리는 없습니다. 무게는 제작 방식에 따라 다릅니다(제3자 보고 약 30kg, 비공식 데이터)(출처: 조사 파일 inmoov.md, 이하 동일).

라이선스: 3D 프린팅 부품은 CC BY-NC 3.0(저작자표시-비영리)입니다. MyRobotLab 프레임워크는 역사적으로 GPLv2였으나, 현재 GitHub 저장소에는 Apache-2.0으로 표시되어 있습니다. 공식 BOM은 없으며, 비용은 미디어 추정치입니다: 약 $800(2015년 전체 기계 보고); $900+이며 몸통과 머리 제외(2013년 보고); $800–2,500(서보 모터/전자 부품 선택에 따라 다름, 2025년 제3자 데이터베이스). 2018년까지 전 세계에 약 1,000대의 InMoov 복제 기계가 있었으며(ESILV 보고), 역사상 가장 많이 복제된 오픈소스 휴머노이드 로봇입니다.

## 핵심 내용

### 주요 매개변수

| 항목 | 값 | 출처 |
|---|---|---|
| 키 / 무게 | 약 1.75–1.8m / 약 30kg(모두 제3자 보고口径, 비공식) | 제3자 데이터베이스 |
| 자유도 | 일반적인 전체 구성 약 28개 서보 모터, 22–30개의 제어 가능한 자유도(제3자口径); "약 45개 관절" 보고도 있음 | 제3자 데이터베이스 |
| 하드웨어 비용 | 공식 BOM 없음; $800–2,500 추정 범위 | 미디어 / 제3자 데이터베이스 |
| 저수준 제어 | Arduino Mega(서보 모터 PWM) | 조사 파일 |
| 고수준 제어 | PC에서 MyRobotLab 실행(Java 프레임워크, Python 바인딩) | 조사 파일 |
| 전원 공급 | 일반적으로 데스크탑 전원 공급 장치(AC), 이동 베이스 버전은 배터리 가능 | 조사 파일 |
| 초보자 친화도 | 3 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 및 기계

- 표준 항공기 모델 서보 모터(MG996R, HS-805BB 등 커뮤니티에서 흔히 사용되는 모델), 맞춤형 액추에이터 없음.
- 손은 힘줄(낚싯줄)로 구동되는 5손가락으로, 쥐기, 수화 수준의 제스처가 가능하며, InMoov의 가장 상징적인 하위 시스템입니다(한 손 인쇄 약 13–14시간). 양손은 완전 구동 5손가락(손당 5–6 서보 모터).
- 설계 소프트웨어는 오픈소스 Blender입니다. 모든 부품은 12×12×12cm 인쇄 영역의 가정용 3D 프린터로 재현 가능합니다.
- 엔지니어링 작업량이 큽니다: 290개 부품, 약 600시간 3D 프린팅 + 약 400시간 조립 및 조정(ESILV 학생 팀 보고口径).

### 소프트웨어 스택 및 센서

- MyRobotLab(MRL): 서비스화된 로봇 프레임워크로, 음성 인식, OpenCV 비전, 챗봇(Program AB), Web UI, 제스처 캡처 등이 내장되어 있습니다. 주로 상호작용을 지향하며 운동 제어는 아닙니다.
- 커뮤니티에는 ROS 포트(예: alansrobotlab/inmoov_ros, 46 stars, 2019년 이후 업데이트 중단)가 있습니다. 최근 커뮤니티에서는 Jetson/Raspberry Pi + LLM을 사용한 현대화 개조가 흔합니다.
- 센서는 커뮤니티 맞춤형입니다: 양안 USB 카메라, 마이크(음성 인식), 선택적 Kinect/초음파/IMU/RealSense.
- 공식 운동학/동역학 시뮬레이션 스택(Gazebo/Isaac/MuJoCo 모두 공식 지원 없음)이 없습니다. 걷기 연구를 위해 설계된 플랫폼이 아닙니다.

### 적합한 사용자

- 적합: 저렴하게 "실물 크기 로봇을 만드는" 경험을 원하는 메이커, 예술/교육/HRI 시나리오. 모든 부품을 가정용 프린터로 제작 가능하고, 서보 모터+Arduino 기술 스택의 진입 장벽이 낮으며, 커뮤니티가 크고, 완성 후 상호작용 시연(음성, 비전, 제스처)이 인상적이어서 "로봇 메이커 입문 첫걸음"으로 훌륭합니다.
- 장벽: 비영리 라이선스로 상업적 사용 제한. 조립 엔지니어링에 수백 시간 소요. 다리가 없고 걷지 못하며, 동역학/강화학습/ROS 등 현대 휴머노이드 기술 스택을 여기서 배울 수 없음. 서보 모터의 정밀도와 수명이 제한적입니다.
