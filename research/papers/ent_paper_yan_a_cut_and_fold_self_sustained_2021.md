---
$id: ent_paper_yan_a_cut_and_fold_self_sustained_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A cut-and-fold self-sustained compliant oscillator for autonomous actuation of origami-inspired robots
  zh: 用于折纸启发式机器人自主驱动的切割折叠自持续柔顺振荡器
  ko: 오리가미에서 영감받은 로봇의 자율 구동을 위한 컷-앤-폴드 자가 지속 컴플라이언트 오실레이터
summary:
  en: Presents a printable self-sustained compliant oscillator built from two mechanically coupled self-opening switches—each
    combining a bistable buckled beam with a conductive supercoiled polymer (CSCP) thermal actuator—that generates periodic
    actuation from a constant electrical current without discrete electronics or control hardware.
  zh: 本文提出一种可打印的自持柔性振荡器，由两个机械耦合的自开开关构成，每个开关结合双稳态屈曲梁与导电超螺旋聚合物热致动器，仅需恒定电流即可产生周期性运动，无需分立电子元件或控制硬件。该振荡器具有鲁棒性（10个原型中9个首次成功）、可配置性（周期3-12秒可调）、高功率（驱动游泳器以约1.6体长/分钟前进）和长寿命（约10^3次循环），并能在水下和高磁场环境中工作。
  ko: 두 개의 기계적으로 결합된 자가 개방 스위치로 구성된 프린터블 자가 지속 컴플라이언트 오실레이터를 제안한다. 각 스위치는 바이스테이블 벅빔(bistable buckled beam)과 전도성 초나선형 폴리머(CSCP)
    열 구동기를 결합하여 이산 전자부품이나 제어 하드웨어 없이 일정한 전류로 주기적 구동을 생성한다.
domains:
- 02_components
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- cut_and_fold
- origami_robotics
- compliant_mechanism
- bistable_beam
- conductive_supercoiled_polymer
- cscp_actuator
- thermal_actuator
- self_sustained_oscillator
- printable_actuator
- electronics_free
- soft_actuator
- autonomous_actuation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2108.08449v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (816 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: A cut-and-fold self-sustained compliant oscillator for autonomous actuation of origami-inspired robots
  url: https://arxiv.org/abs/2108.08449
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
- system
---
## 概述
该研究针对折纸机器人依赖笨重刚性组件或电子控制的问题，提出一种完全可打印的柔性振荡器。其核心创新在于利用双稳态屈曲梁与CSCP热致动器的机械耦合，实现从恒定电流到周期性运动的自主转换。振荡器通过解析模型可编程设计周期参数，并支持与折纸系统无缝集成，最终器件具有轻量、低成本、柔性、无电子元件和非磁性等特性。实验展示了其在自主游泳器、LED闪烁和流体搅拌中的功能，为全打印自主机器人奠定基础。

## 核心内容
### 方法与架构
- **核心组件**：振荡器由两个机械耦合的自开开关组成，每个开关包含一个双稳态屈曲梁（提供机械双稳态）和一个导电超螺旋聚合物（CSCP）热致动器（通过焦耳热驱动形变）。
- **工作机制**：恒定电流加热CSCP致动器，使其收缩并触发屈曲梁从稳态切换；机械耦合使两个开关交替开闭，形成自持振荡。
- **可打印制造**：所有组件通过切割和折叠柔性2D片材或线材实现，无需传统电子装配。

### 实验设置与关键性能
- **鲁棒性**：10个原型中9个首次运行成功，成功率90%。
- **可配置性**：通过调整CSCP长度或屈曲梁几何参数，振荡周期可在3秒至12秒范围内调节。
- **功率输出**：驱动游泳器克服流体阻力，以约1.6体长/分钟的速度持续前进。
- **耐久性**：可稳定运行约10^3次循环。
- **环境适应性**：完全在水下和高磁场（如MRI环境）中正常工作。

### 应用演示
- **自主游泳器**：振荡器驱动柔性鳍片实现自主滑行。
- **LED闪烁**：通过振荡器周期性通断控制LED亮灭。
- **流体搅拌**：振荡器带动搅拌桨实现液体混合。

### 结论
该工作通过机械-热耦合设计消除了对分立电子元件的依赖，实现了可打印、可编程的自主振荡器。解析模型为周期参数提供设计指导，使其能集成于折纸机器人中，推动低成本、轻量化、无电子化自主系统的实用化。

## Overview
Origami-inspired robots are of particular interest given their potential for rapid and accessible design and fabrication of elegant designs and complex functionalities through cutting and folding of flexible 2D sheets or even strings, i.e.printable manufacturing. Yet, origami robots still require bulky, rigid components or electronics for actuation and control to accomplish tasks with reliability, programmability, ability to output substantial force, and durability, restricting their full potential. Here, we present a printable self-sustained compliant oscillator that generates periodic actuation using only constant electrical power, without discrete components or electronic control hardware. This oscillator is robust (9 out of 10 prototypes worked successfully on the first try), configurable (with tunable periods from 3 s to 12 s), powerful (can overcome hydrodynamic resistance to consistently propel a swimmer at ~1.6 body lengths/min), and long-lasting (~10^3 cycles); it enables driving macroscale devices with prescribed autonomous behaviors, e.g. locomotion and sequencing. This oscillator is also fully functional underwater and in high magnetic fields. Our analytical model characterizes essential parameters of the oscillation period, enabling programmable design of the oscillator. The printable oscillator can be integrated into origami-inspired systems seamlessly and monolithically, allowing rapid design and prototyping; the resulting integrated devices are lightweight, low-cost, compliant, electronic-free, and nonmagnetic, enabling practical applications in extreme areas. We demonstrate the functionalities of the oscillator with: (i) autonomous gliding of a printable swimmer, (ii) LED flashing, and (iii) fluid stirring. This work paves the way for realizing fully printable autonomous robots with a high integration of actuation and control.

## Overview
Origami-inspired robots are of particular interest given their potential for rapid and accessible design and fabrication of elegant designs and complex functionalities through cutting and folding of flexible 2D sheets or even strings, i.e., printable manufacturing. Yet, origami robots still require bulky, rigid components or electronics for actuation and control to accomplish tasks with reliability, programmability, ability to output substantial force, and durability, restricting their full potential. Here, we present a printable self-sustained compliant oscillator that generates periodic actuation using only constant electrical power, without discrete components or electronic control hardware. This oscillator is robust (9 out of 10 prototypes worked successfully on the first try), configurable (with tunable periods from 3 s to 12 s), powerful (can overcome hydrodynamic resistance to consistently propel a swimmer at ~1.6 body lengths/min), and long-lasting (~10^3 cycles); it enables driving macroscale devices with prescribed autonomous behaviors, e.g., locomotion and sequencing. This oscillator is also fully functional underwater and in high magnetic fields. Our analytical model characterizes essential parameters of the oscillation period, enabling programmable design of the oscillator. The printable oscillator can be integrated into origami-inspired systems seamlessly and monolithically, allowing rapid design and prototyping; the resulting integrated devices are lightweight, low-cost, compliant, electronic-free, and nonmagnetic, enabling practical applications in extreme areas. We demonstrate the functionalities of the oscillator with: (i) autonomous gliding of a printable swimmer, (ii) LED flashing, and (iii) fluid stirring. This work paves the way for realizing fully printable autonomous robots with a high integration of actuation and control.

## Content
Origami-inspired robots are of particular interest given their potential for rapid and accessible design and fabrication of elegant designs and complex functionalities through cutting and folding of flexible 2D sheets or even strings, i.e., printable manufacturing. Yet, origami robots still require bulky, rigid components or electronics for actuation and control to accomplish tasks with reliability, programmability, ability to output substantial force, and durability, restricting their full potential. Here, we present a printable self-sustained compliant oscillator that generates periodic actuation using only constant electrical power, without discrete components or electronic control hardware. This oscillator is robust (9 out of 10 prototypes worked successfully on the first try), configurable (with tunable periods from 3 s to 12 s), powerful (can overcome hydrodynamic resistance to consistently propel a swimmer at ~1.6 body lengths/min), and long-lasting (~10^3 cycles); it enables driving macroscale devices with prescribed autonomous behaviors, e.g., locomotion and sequencing. This oscillator is also fully functional underwater and in high magnetic fields. Our analytical model characterizes essential parameters of the oscillation period, enabling programmable design of the oscillator. The printable oscillator can be integrated into origami-inspired systems seamlessly and monolithically, allowing rapid design and prototyping; the resulting integrated devices are lightweight, low-cost, compliant, electronic-free, and nonmagnetic, enabling practical applications in extreme areas. We demonstrate the functionalities of the oscillator with: (i) autonomous gliding of a printable swimmer, (ii) LED flashing, and (iii) fluid stirring. This work paves the way for realizing fully printable autonomous robots with a high integration of actuation and control.

## 参考
- http://arxiv.org/abs/2108.08449v1

## 개요
이 연구는 종이접기 로봇이 무겁고 딱딱한 부품이나 전자 제어에 의존하는 문제를 해결하기 위해, 완전히 인쇄 가능한 유연한 발진기를 제안한다. 핵심 혁신은 쌍안정 좌굴 빔과 CSCP 열작동기의 기계적 결합을 활용하여 일정 전류에서 주기적 운동으로의 자율적 전환을 실현하는 것이다. 발진기는 해석 모델을 통해 주기 매개변수를 프로그래밍 가능하게 설계할 수 있으며, 종이접기 시스템과의 원활한 통합을 지원한다. 최종 소자는 경량, 저비용, 유연성, 무전자 부품, 비자성 특성을 갖는다. 실험은 자율 수영기, LED 점멸, 유체 교반에서의 기능을 입증하여 전인쇄 자율 로봇의 기반을 마련한다.

## 핵심 내용
### 방법 및 구조
- **핵심 구성 요소**: 발진기는 기계적으로 결합된 두 개의 자가 개폐 스위치로 구성되며, 각 스위치는 쌍안정 좌굴 빔(기계적 쌍안정성 제공)과 전도성 초나선 폴리머(CSCP) 열작동기(줄 열로 변형 구동)를 포함한다.
- **작동 메커니즘**: 일정 전류가 CSCP 작동기를 가열하여 수축시키고 좌굴 빔의 안정 상태 전환을 유발한다. 기계적 결합으로 두 스위치가 교대로 열리고 닫히며 자립 발진을 형성한다.
- **인쇄 가능한 제조**: 모든 구성 요소는 유연한 2D 시트나 와이어를 절단하고 접어서 구현되며, 전통적인 전자 조립이 필요 없다.

### 실험 설정 및 주요 성능
- **견고성**: 10개 프로토타입 중 9개가 첫 실행에서 성공하여 성공률 90%를 기록했다.
- **구성 가능성**: CSCP 길이나 좌굴 빔 기하 매개변수를 조정하여 발진 주기를 3초에서 12초 범위로 조절할 수 있다.
- **출력 성능**: 수영기가 유체 저항을 극복하고 약 1.6체장/분의 속도로 지속 전진한다.
- **내구성**: 약 10^3회 사이클 동안 안정적으로 작동한다.
- **환경 적응성**: 완전히 수중 및 고자기장(예: MRI 환경)에서 정상 작동한다.

### 응용 시연
- **자율 수영기**: 발진기가 유연한 지느러미를 구동하여 자율 활주를 구현한다.
- **LED 점멸**: 발진기의 주기적 개폐로 LED 점멸을 제어한다.
- **유체 교반**: 발진기가 교반 날개를 구동하여 액체 혼합을 실현한다.

### 결론
이 연구는 기계-열 결합 설계를 통해 분리된 전자 부품에 대한 의존성을 제거하고, 인쇄 가능하고 프로그래밍 가능한 자율 발진기를 구현했다. 해석 모델은 주기 매개변수에 대한 설계 지침을 제공하여 종이접기 로봇에 통합할 수 있게 하며, 저비용, 경량화, 무전자 자율 시스템의 실용화를 촉진한다.
