---
$id: ent_paper_avery_shape_sensing_of_variable_stif_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shape Sensing of Variable Stiffness Soft Robots using Electrical Impedance Tomography
  zh: 基于电阻抗断层扫描的变刚度软体机器人形状感知
  ko: 전기 임피던스 단층촬영법을 이용한 가변 강성 소프트 로봇의 형상 감지
summary:
  en: This paper presents a proprioceptive soft actuator that uses conductive saline as both the actuation fluid and the sensing
    medium, enabling shape reconstruction via Electrical Impedance Tomography (EIT) with a custom Frequency Division Multiplexed
    (FDM) system.
  zh: 本文提出一种使用导电盐水同时作为驱动与传感介质的自感知软体执行器，通过定制频分复用（FDM）系统实现基于电阻抗断层成像（EIT）的形状重建。该研究由团队开发，核心贡献在于将EIT技术集成至变刚度软体机器人中，实现低成本、低轮廓的形状传感，并验证了其在两种二自由度设计中的可行性。
  ko: 본 논문은 전도성 식염수를 구동 유체와 센싱 매질로 동시에 사용하는 본체감각형 소프트 액추에이터를 제안하며, 맞춤형 주파수 분할 다중화 전기 임피던스 단층촬영(FDM-EIT) 시스템을 통해 형상 재구성을 수행한다.
domains:
- 02_components
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- process
tags:
- soft_robotics
- shape_sensing
- electrical_impedance_tomography
- eit
- frequency_division_multiplexing
- fdm_eit
- conductive_fluid
- proprioception
- variable_stiffness
- soft_actuator
- laser_welding
- compliant_joints
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.02429v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (692 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Shape Sensing of Variable Stiffness Soft Robots using Electrical Impedance Tomography
  url: https://arxiv.org/abs/1904.02429
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
软体机器人因减少组织创伤和可进入曲折路径而在微创手术中具有优势，但其变形特性对形状建模和术中传感提出挑战。本文提出一种自感知软体执行器，利用导电盐水作为工作流体，通过六个电极的电阻抗测量实现EIT断层成像。新开发的FDM-EIT系统具备66 dB信噪比和20 ms时间分辨率。研究在液压铰链执行器和气动手指执行器两种二自由度设计中验证了该方法，证明阻抗测量可推断形状变化，且EIT图像在驱动过程中显示出与各自由度对应的独特模式。尽管存在机械滞后，但测量和图像的可重复性较高，表明FDM-EIT在软体机器人形状传感中具有潜力。

## 核心内容
### 方法
- 使用导电盐水作为驱动流体和传感介质，通过六个电极采集电阻抗数据。
- 基于EIT技术进行断层成像重建，利用新开发的FDM系统实现多路复用测量。

### 系统架构
- FDM-EIT系统：支持66 dB信噪比和20 ms时间分辨率，适用于实时形状传感。
- 两种二自由度设计：
  - 液压铰链执行器：通过液压驱动实现弯曲运动。
  - 气动手指执行器：结合液压梁结构，实现气动驱动下的形状变化。

### 实验设置
- 在两种执行器上分别进行驱动测试，记录阻抗测量数据并重建EIT图像。
- 观察机械滞后现象，但测量和图像的可重复性较高。

### 关键数字
- 信噪比：66 dB
- 时间分辨率：20 ms
- 自由度：2（每种设计）

### 结论
- 阻抗测量可有效推断形状变化，EIT图像显示与各自由度对应的独特模式。
- FDM-EIT作为低成本、低轮廓的形状传感器，在软体机器人中具有应用潜力。

## Overview
Soft robotic systems offer benefits over traditional rigid systems through reduced contact trauma with soft tissues and by enabling access through tortuous paths in minimally invasive surgery. However, the inherent deformability of soft robots places both a greater onus on accurate modelling of their shape, and greater challenges in realising intraoperative shape sensing. Herein we present a proprioceptive (self-sensing) soft actuator, with an electrically conductive working fluid. Electrical impedance measurements from up to six electrodes enabled tomographic reconstructions using Electrical Impedance Tomography (EIT). A new Frequency Division Multiplexed (FDM) EIT system was developed capable of measurements of 66 dB SNR with 20 ms temporal resolution. The concept was examined in two two-degree-of-freedom designs: a hydraulic hinged actuator and a pneumatic finger actuator with hydraulic beams. Both cases demonstrated that impedance measurements could be used to infer shape changes, and EIT images reconstructed during actuation showed distinct patterns with respect to each degree of freedom (DOF). Whilst there was some mechanical hysteresis observed, the repeatability of the measurements and resultant images was high. The results show the potential of FDM-EIT as a low-cost, low profile shape sensor in soft robots.

## 参考
- http://arxiv.org/abs/1904.02429v2

## 개요
소프트 로봇은 조직 손상을 줄이고 구불구불한 경로로 접근할 수 있어 최소 침습 수술에서 장점이 있지만, 변형 특성으로 인해 형상 모델링과 수술 중 센싱에 어려움이 있습니다. 본 논문은 전도성 식염수를 작동 유체로 사용하고, 6개 전극의 전기 임피던스 측정을 통해 EIT 단층 촬영을 구현하는 자가 감지 소프트 액추에이터를 제안합니다. 새로 개발된 FDM-EIT 시스템은 66 dB 신호 대 잡음비와 20 ms 시간 분해능을 갖습니다. 연구는 유압 힌지 액추에이터와 공압 핑거 액추에이터라는 두 가지 2자유도 설계에서 이 방법을 검증하여, 임피던스 측정이 형상 변화를 추론할 수 있고 EIT 이미지가 구동 중 각 자유도에 해당하는 고유한 패턴을 보여줌을 입증했습니다. 기계적 히스테리시스가 존재하지만 측정 및 이미지의 반복성은 높아, FDM-EIT가 소프트 로봇 형상 센싱에서 잠재력을 지님을 시사합니다.

## 핵심 내용
### 방법
- 전도성 식염수를 구동 유체 및 센싱 매체로 사용하고, 6개 전극을 통해 전기 임피던스 데이터를 수집합니다.
- EIT 기술을 기반으로 단층 촬영 재구성을 수행하며, 새로 개발된 FDM 시스템을 통해 다중화 측정을 구현합니다.

### 시스템 아키텍처
- FDM-EIT 시스템: 66 dB 신호 대 잡음비와 20 ms 시간 분해능을 지원하여 실시간 형상 센싱에 적합합니다.
- 두 가지 2자유도 설계:
  - 유압 힌지 액추에이터: 유압 구동을 통해 굽힘 운동을 구현합니다.
  - 공압 핑거 액추에이터: 유압 빔 구조를 결합하여 공압 구동 하의 형상 변화를 구현합니다.

### 실험 설정
- 두 액추에이터에서 각각 구동 테스트를 수행하고, 임피던스 측정 데이터를 기록하며 EIT 이미지를 재구성합니다.
- 기계적 히스테리시스 현상이 관찰되지만, 측정 및 이미지의 반복성은 높습니다.

### 주요 수치
- 신호 대 잡음비: 66 dB
- 시간 분해능: 20 ms
- 자유도: 2 (각 설계)

### 결론
- 임피던스 측정은 형상 변화를 효과적으로 추론할 수 있으며, EIT 이미지는 각 자유도에 해당하는 고유한 패턴을 보여줍니다.
- FDM-EIT는 저비용, 저프로파일 형상 센서로서 소프트 로봇에서 응용 잠재력을 지닙니다.
