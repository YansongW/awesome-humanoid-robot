---
$id: ent_robot_system_poppy_humanoid
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Poppy Humanoid
  zh: Poppy 人形机器人
  ko: Poppy Humanoid
summary:
  en: An open-source 3D-printed humanoid robot created by Inria's Flowers team, about 84 cm and 3.5 kg with 25 degrees of
    freedom including a 5-DoF bio-inspired spine, driven by 25 ROBOTIS Dynamixel servos and programmed in Python or Scratch
    via the pypot library, designed for education and HRI research.
  zh: Poppy Humanoid 是法国 Inria Flowers 团队发起的开源 3D 打印人形机器人，约 84 cm / 3.5 kg，25 个自由度（含 5 自由度仿生脊柱），由 25 台 ROBOTIS Dynamixel 智能舵机驱动，基于树莓派与自研
    pypot Python 库，支持 Scratch 图形化编程与柔顺反驱示教，是教育与 HRI 研究的经典平台。
  ko: An open-source 3D-printed humanoid robot created by Inria's Flowers team, about 84 cm and 3.5 kg with 25 degrees of
    freedom including a 5-DoF bio-inspired spine, driven by 25 ROBOTIS Dynamixel servos and programmed in Python or Scratch
    via the pypot library, designed for education and HRI research.
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
- poppy
- inria
- education
- hri
- dynamixel
- 3d_printed
- pypot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: 内容整理自调研档案 data/roadmap/research/poppy-humanoid.md（访问日期 2026-07-01）。主 GitHub 仓库最后 push 为 2021-12-06，官方文档最后更新 2022-12-20，维护基本停滞；成本为
    2014 年官方口径与后续社区估算。
sources:
- id: src_001
  type: website
  title: poppy-project/poppy-humanoid GitHub Repository
  url: https://github.com/poppy-project/poppy-humanoid
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Poppy Project Documentation
  url: https://docs.poppy-project.org/en/
  accessed_at: '2026-07-01'
---

## 概述

Poppy Humanoid 是法国 Inria Bordeaux Sud-Ouest 的 Flowers 团队（联合 Ensta ParisTech）于 2012 年发起的开源 3D 打印人形机器人，源于 Matthieu Lapeyre 的博士论文（导师 Pierre-Yves Oudeyer），ERC Explorer 资助，现由非营利组织 Poppy Station 维护社区。整机约 84 cm / 3.5 kg，25 个自由度（含 5 自由度全驱动仿生脊柱，屈膝式腿构型）（来源：调研档案 poppy-humanoid.md，下同）。

许可证：硬件 CC BY-SA 4.0、软件 GPLv3、文档 CC-BY-SA 4.0。成本：约 €7,500–8,000（2014 年官方口径，其中电机约 €5,000）；Génération Robots 套件约 €9,000；社区估算全套约 €9,588——高成本主要来自 25 台高端舵机。GitHub `poppy-project/poppy-humanoid` 约 1,007 stars / 281 forks，但主仓库最后 push 为 2021-12-06，官方文档最后更新 2022-12-20，维护基本停滞。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 身高 / 重量 | 约 84 cm / 约 3.5 kg | 2014 年媒体报道 |
| 自由度 | 25（含 5 自由度全驱动仿生脊柱） | 官方文档 |
| 硬件成本 | 约 €7,500–8,000（2014 官方口径）；套件约 €9,000；社区估算约 €9,588 | 媒体 / 经销商 / 社区估算 |
| 主控 | Raspberry Pi 3/4（或 Odroid），经 USB2AX / U2D2 接 Dynamixel 总线 | 官方文档 |
| 传感器（2014 完整版） | 16 个 FSR 力传感器、2 个 PS Eye 相机、1 个 IMU、4.3 英寸 LCD 屏、双麦克风 | 媒体报道 |
| 供电 | 早期版本需外接电源（无电池），移动性受限 | 调研档案 |
| 新手友好度 | 3.5 / 5（调研档案评估） | 调研档案 |

### 执行器与机械

- 25 台 ROBOTIS Dynamixel 智能舵机，TTL 串行总线级联；按关节扭矩需求混用 AX 系列（肢体小关节）与 MX 系列（躯干/大腿等高扭矩关节），装配手册注明 MX-28 已迭代为 MX-28AT。
- 高减速比舵机 + 串联弹性/柔顺模式：可手动反驱（compliant mode），适合"手把手"示教编程，这是 Poppy 教学设计的核心卖点。
- 全身结构件 3D 打印（家用打印机即可），骨架轻量化、仿生比例。

### 软件栈

- pypot（项目自研 Python Dynamixel 库）+ 各机器人专属 Python 包；支持 Jupyter Notebook、Scratch/Snap! 图形化编程、REST API/Web 控制。
- 仿真：CoppeliaSim（原 V-REP）官方模型 + 轻量 3D Web 查看器，可零硬件开发调试；提供 ROS 桥接（社区维护）；预配置系统镜像（SD 卡刷入即用）。
- 文档：docs.poppy-project.org 结构化文档（入门/装配/安装/编程四部分），25 步装配手册 + 25 集装配视频。

### 适合人群

- 适合：看重教学体系与人机交互（而非运动性能）的教育者；想做具身认知/HRI 研究的团队——Python/Scratch 双轨、柔顺反驱示教、仿真先行、装配视频完整，教育与科研案例丰富（发展机器人学、HRI、行走研究数十篇论文）。
- 门槛：约 €9,000 的套件价格远超当代替代品；主仓库停更意味着新系统/新 Python 版本兼容性要自己踩坑；25 台 Dynamixel 的采购与维护成本高；想做行走/RL 的新手建议转看 ToddlerBot 等新一代平台。

## 参考

- [poppy-project/poppy-humanoid GitHub 仓库](https://github.com/poppy-project/poppy-humanoid)
- [Poppy 官方文档](https://docs.poppy-project.org/en/)
- [25 步装配手册](https://docs.poppy-project.org/en/assembly-guides/poppy-humanoid/)

## 개요

Poppy Humanoid는 프랑스 Inria Bordeaux Sud-Ouest의 Flowers 팀(Ensta ParisTech 공동)이 2012년에 시작한 오픈소스 3D 프린팅 휴머노이드 로봇으로, Matthieu Lapeyre의 박사 논문(지도교수 Pierre-Yves Oudeyer)에서 비롯되었으며 ERC Explorer의 지원을 받았습니다. 현재는 비영리 단체 Poppy Station이 커뮤니티를 관리하고 있습니다. 전체 크기는 약 84cm / 3.5kg이며, 25개의 자유도(5자유도 전구동 생체 모방 척추, 무릎 굽힘형 다리 구조 포함)를 갖추고 있습니다(출처: 조사 파일 poppy-humanoid.md, 이하 동일).

라이선스: 하드웨어 CC BY-SA 4.0, 소프트웨어 GPLv3, 문서 CC-BY-SA 4.0. 비용: 약 €7,500–8,000(2014년 공식 기준, 모터 약 €5,000 포함); Génération Robots 키트 약 €9,000; 커뮤니티 추정 전체 세트 약 €9,588——높은 비용은 주로 25대의 고급 서보 모터에서 발생합니다. GitHub `poppy-project/poppy-humanoid`는 약 1,007 stars / 281 forks이지만, 메인 저장소의 마지막 푸시는 2021-12-06이며, 공식 문서의 마지막 업데이트는 2022-12-20으로 유지보수가 거의 중단되었습니다.

## 핵심 내용

### 주요 사양

| 항목 | 수치 | 출처 |
|---|---|---|
| 키 / 무게 | 약 84 cm / 약 3.5 kg | 2014년 언론 보도 |
| 자유도 | 25(5자유도 전구동 생체 모방 척추 포함) | 공식 문서 |
| 하드웨어 비용 | 약 €7,500–8,000(2014 공식 기준); 키트 약 €9,000; 커뮤니티 추정 약 €9,588 | 언론 / 판매처 / 커뮤니티 추정 |
| 메인 컨트롤러 | Raspberry Pi 3/4(또는 Odroid), USB2AX / U2D2를 통해 Dynamixel 버스 연결 | 공식 문서 |
| 센서(2014 완전판) | 16개 FSR 힘 센서, 2개 PS Eye 카메라, 1개 IMU, 4.3인치 LCD 화면, 듀얼 마이크 | 언론 보도 |
| 전원 공급 | 초기 버전은 외부 전원 필요(배터리 없음), 이동성 제한 | 조사 파일 |
| 초보자 친화도 | 3.5 / 5(조사 파일 평가) | 조사 파일 |

### 액추에이터 및 기계

- 25대 ROBOTIS Dynamixel 스마트 서보 모터, TTL 직렬 버스 직렬 연결; 관절 토크 요구에 따라 AX 시리즈(팔다리 작은 관절)와 MX 시리즈(몸통/허벅지 등 고토크 관절) 혼용, 조립 매뉴얼에는 MX-28이 MX-28AT로 업데이트되었다고 명시.
- 고감속비 서보 모터 + 직렬 탄성/컴플라이언트 모드: 수동 역구동(compliant mode) 가능, '손으로 직접 가르치는' 시연 프로그래밍에 적합——이것이 Poppy 교육 설계의 핵심 장점.
- 전체 구조 부품 3D 프린팅(가정용 프린터로 가능), 골격 경량화, 생체 모방 비율.

### 소프트웨어 스택

- pypot(프로젝트 자체 개발 Python Dynamixel 라이브러리) + 각 로봇 전용 Python 패키지; Jupyter Notebook, Scratch/Snap! 그래픽 프로그래밍, REST API/웹 제어 지원.
- 시뮬레이션: CoppeliaSim(구 V-REP) 공식 모델 + 경량 3D 웹 뷰어, 하드웨어 없이 개발 및 디버깅 가능; ROS 브리지 제공(커뮤니티 유지보수); 사전 구성된 시스템 이미지(SD 카드에 굽기만 하면 사용 가능).
- 문서: docs.poppy-project.org 구조화된 문서(입문/조립/설치/프로그래밍 네 부분), 25단계 조립 매뉴얼 + 25편 조립 비디오.

### 적합한 사용자

- 적합: 운동 성능보다 교육 시스템과 인간-로봇 상호작용을 중시하는 교육자; 구현 인지/HRI 연구를 원하는 팀——Python/Scratch 이중 트랙, 컴플라이언트 역구동 시연, 시뮬레이션 우선, 완전한 조립 비디오, 교육 및 연구 사례 풍부(발달 로보틱스, HRI, 보행 연구 수십 편 논문).
- 진입 장벽: 약 €9,000의 키트 가격은 현대 대체품보다 훨씬 높음; 메인 저장소 업데이트 중단은 새 시스템/새 Python 버전 호환성을 직접 해결해야 함을 의미; 25대 Dynamixel의 구매 및 유지보수 비용 높음; 보행/강화학습을 원하는 초보자는 ToddlerBot 등 차세대 플랫폼을 고려하는 것이 좋음.
