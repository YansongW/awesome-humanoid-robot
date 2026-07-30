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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2108.08449v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
종이접기에서 영감을 받은 로봇은 유연한 2D 시트나 심지어 끈을 자르고 접는 방식(즉, 인쇄 가능한 제조)을 통해 우아한 디자인과 복잡한 기능을 빠르고 접근성 있게 설계 및 제작할 수 있는 잠재력 때문에 특히 주목받고 있습니다. 그러나 종이접기 로봇은 여전히 신뢰성, 프로그래밍 가능성, 상당한 힘 출력 능력, 내구성을 갖춘 작업을 수행하기 위해 부피가 크고 딱딱한 부품이나 전자 장치를 구동 및 제어에 필요로 하여, 그 잠재력을 완전히 발휘하지 못하고 있습니다. 여기서 우리는 개별 부품이나 전자 제어 하드웨어 없이 일정한 전력만으로 주기적인 구동을 생성하는 인쇄 가능한 자립형 순응 발진기를 제시합니다. 이 발진기는 견고하며(10개 프로토타입 중 9개가 첫 시도에 성공), 구성 가능하고(3초에서 12초까지 조정 가능한 주기), 강력하며(유체 저항을 극복하여 수영체를 약 1.6 체장/분으로 일관되게 추진), 오래 지속됩니다(~10^3 사이클). 이를 통해 이동 및 순서화와 같은 규정된 자율 행동을 가진 거시적 장치를 구동할 수 있습니다. 이 발진기는 수중 및 높은 자기장에서도 완전히 작동합니다. 우리의 분석 모델은 발진 주기의 필수 매개변수를 특성화하여 발진기의 프로그래밍 가능한 설계를 가능하게 합니다. 인쇄 가능한 발진기는 종이접기에서 영감을 받은 시스템에 매끄럽고 단일체로 통합되어 빠른 설계 및 프로토타이핑을 허용하며, 결과적으로 통합된 장치는 가볍고, 저렴하며, 순응적이고, 전자 장치가 없으며, 비자성체여서 극한 환경에서 실용적인 응용이 가능합니다. 우리는 발진기의 기능을 (i) 인쇄 가능한 수영체의 자율 활공, (ii) LED 점멸, (iii) 유체 교반을 통해 시연합니다. 이 연구는 구동과 제어의 높은 통합을 갖춘 완전히 인쇄 가능한 자율 로봇을 실현하는 길을 열어줍니다.

## 핵심 내용
종이접기에서 영감을 받은 로봇은 유연한 2D 시트나 심지어 끈을 자르고 접는 방식(즉, 인쇄 가능한 제조)을 통해 우아한 디자인과 복잡한 기능을 빠르고 접근성 있게 설계 및 제작할 수 있는 잠재력 때문에 특히 주목받고 있습니다. 그러나 종이접기 로봇은 여전히 신뢰성, 프로그래밍 가능성, 상당한 힘 출력 능력, 내구성을 갖춘 작업을 수행하기 위해 부피가 크고 딱딱한 부품이나 전자 장치를 구동 및 제어에 필요로 하여, 그 잠재력을 완전히 발휘하지 못하고 있습니다. 여기서 우리는 개별 부품이나 전자 제어 하드웨어 없이 일정한 전력만으로 주기적인 구동을 생성하는 인쇄 가능한 자립형 순응 발진기를 제시합니다. 이 발진기는 견고하며(10개 프로토타입 중 9개가 첫 시도에 성공), 구성 가능하고(3초에서 12초까지 조정 가능한 주기), 강력하며(유체 저항을 극복하여 수영체를 약 1.6 체장/분으로 일관되게 추진), 오래 지속됩니다(~10^3 사이클). 이를 통해 이동 및 순서화와 같은 규정된 자율 행동을 가진 거시적 장치를 구동할 수 있습니다. 이 발진기는 수중 및 높은 자기장에서도 완전히 작동합니다. 우리의 분석 모델은 발진 주기의 필수 매개변수를 특성화하여 발진기의 프로그래밍 가능한 설계를 가능하게 합니다. 인쇄 가능한 발진기는 종이접기에서 영감을 받은 시스템에 매끄럽고 단일체로 통합되어 빠른 설계 및 프로토타이핑을 허용하며, 결과적으로 통합된 장치는 가볍고, 저렴하며, 순응적이고, 전자 장치가 없으며, 비자성체여서 극한 환경에서 실용적인 응용이 가능합니다. 우리는 발진기의 기능을 (i) 인쇄 가능한 수영체의 자율 활공, (ii) LED 점멸, (iii) 유체 교반을 통해 시연합니다. 이 연구는 구동과 제어의 높은 통합을 갖춘 완전히 인쇄 가능한 자율 로봇을 실현하는 길을 열어줍니다.

## 参考
- http://arxiv.org/abs/2108.08449v1
