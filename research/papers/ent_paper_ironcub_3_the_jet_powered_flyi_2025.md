---
$id: ent_paper_ironcub_3_the_jet_powered_flyi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'iRonCub 3: The Jet-Powered Flying Humanoid Robot'
  zh: 'iRonCub 3: The Jet-Powered Flying Humanoid Robot'
  ko: 'iRonCub 3: The Jet-Powered Flying Humanoid Robot'
summary:
  en: 'iRonCub 3: The Jet-Powered Flying Humanoid Robot is a 2025 work on hardware design for humanoid robots.'
  zh: iRonCub 3 是 2025 年发布的一款喷气动力全尺寸人形机器人，由意大利理工学院（IIT）团队开发。其核心贡献在于首次实现了喷气动力人形机器人的实际起飞实验，并提出了针对此类系统的控制、估计与实验安全架构。
  ko: 'iRonCub 3: The Jet-Powered Flying Humanoid Robot is a 2025 work on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- ironcub_3
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01125v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (718 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'iRonCub 3: The Jet-Powered Flying Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2506.01125
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
iRonCub 3 旨在突破传统飞行器形态，利用人形全身结构实现飞行。该机器人面临控制、状态估计与系统集成的独特挑战，团队为此设计了专用的推进系统、控制框架与实验基础设施。研究先在仿真中验证了起飞与轨迹跟踪能力，随后首次在真实环境中完成了喷气动力人形机器人的离地实验。此外，论文还详细阐述了如何设计围绕喷气动力人形机器人的实验区域，以应对远超室内人形机器人实验的复杂性与安全要求。

## 核心内容
### 硬件与软件架构
- **推进系统**：iRonCub 3 在躯干与四肢集成了微型喷气发动机，提供垂直升力与姿态控制所需的推力。
- **控制框架**：采用分层控制结构，上层负责轨迹规划与力分配，下层执行关节级与推力矢量控制。
- **估计系统**：融合 IMU、关节编码器与外部运动捕捉数据，实时估计机器人状态。

### 实验验证
- **仿真实验**：首先在 Gazebo 环境中进行起飞与参考轨迹跟踪测试，验证控制与估计算法的可行性。
- **真实实验**：首次实现喷气动力人形机器人的实际离地（liftoff），尽管飞行时间与高度有限，但标志着从地面到空中机动性的关键一步。

### 实验区域设计
- **安全隔离**：实验区域需设置防火屏障与远程操作站，操作员与机器人保持安全距离。
- **环境监控**：部署热成像摄像头与气流传感器，实时监测喷气发动机的排气温度与推力分布。
- **应急机制**：配备紧急停机系统与自动灭火装置，应对发动机故障或失控风险。

### 结论
iRonCub 3 证明了喷气动力人形机器人飞行的可行性，但当前仍处于早期阶段。未来工作需解决续航、姿态稳定性与自主着陆等挑战。

## Overview
This article presents iRonCub 3, a jet-powered humanoid robot, and its first flight experiments. Unlike traditional aerial vehicles, iRonCub 3 aims to achieve flight using a full-body humanoid form, which poses unique challenges in control, estimation, and system integration. We highlight the robot's current mechanical and software architecture, including its propulsion system, control framework, and experimental infrastructure. The control and estimation framework is first validated in simulation by performing a takeoff and tracking a reference trajectory. Then, we demonstrate, for the first time, a liftoff of a jet-powered humanoid robot - an initial but significant step toward aerial humanoid mobility. Also, we detail how the experimental area around a jet-powered humanoid robot should be designed in order to deal with a level of complexity that is substantially superior than indoor humanoid robot experiments.

## 参考
- http://arxiv.org/abs/2506.01125v1

## 개요
iRonCub 3는 전통적인 비행체 형태를 넘어, 인간형 전신 구조를 활용한 비행을 목표로 합니다. 이 로봇은 제어, 상태 추정 및 시스템 통합에 있어 독특한 도전 과제를 안고 있으며, 팀은 이를 위해 전용 추진 시스템, 제어 프레임워크 및 실험 인프라를 설계했습니다. 연구는 먼저 시뮬레이션에서 이륙 및 궤적 추적 능력을 검증한 후, 실제 환경에서 제트 추진 인간형 로봇의 첫 이륙 실험을 완료했습니다. 또한, 논문은 실내 인간형 로봇 실험보다 훨씬 복잡하고 안전 요구 사항이 높은 제트 추진 인간형 로봇을 위한 실험 구역 설계 방법을 자세히 설명합니다.

## 핵심 내용
### 하드웨어 및 소프트웨어 아키텍처
- **추진 시스템**: iRonCub 3는 몸통과 팔다리에 마이크로 제트 엔진을 통합하여 수직 양력 및 자세 제어에 필요한 추력을 제공합니다.
- **제어 프레임워크**: 계층적 제어 구조를 채택하며, 상위 계층은 궤적 계획과 힘 분배를 담당하고 하위 계층은 관절 수준 및 추력 벡터 제어를 실행합니다.
- **추정 시스템**: IMU, 관절 엔코더 및 외부 모션 캡처 데이터를 융합하여 로봇 상태를 실시간으로 추정합니다.

### 실험 검증
- **시뮬레이션 실험**: 먼저 Gazebo 환경에서 이륙 및 기준 궤적 추적 테스트를 수행하여 제어 및 추정 알고리즘의 타당성을 검증했습니다.
- **실제 실험**: 제트 추진 인간형 로봇의 실제 이륙(liftoff)을 최초로 구현했습니다. 비행 시간과 고도는 제한적이었지만, 지상에서 공중 기동성으로의 전환에 있어 중요한 이정표가 되었습니다.

### 실험 구역 설계
- **안전 격리**: 실험 구역에는 방화벽과 원격 조작 스테이션을 설치하여 작업자와 로봇 간의 안전 거리를 유지해야 합니다.
- **환경 모니터링**: 열화상 카메라와 기류 센서를 배치하여 제트 엔진의 배기 온도와 추력 분포를 실시간으로 모니터링합니다.
- **비상 메커니즘**: 엔진 고장 또는 통제 불능 위험에 대비해 비상 정지 시스템과 자동 소화 장치를 갖춥니다.

### 결론
iRonCub 3는 제트 추진 인간형 로봇 비행의 가능성을 입증했지만, 현재는 초기 단계에 머물러 있습니다. 향후 작업은 배터리 수명, 자세 안정성 및 자율 착륙과 같은 도전 과제를 해결해야 합니다.
