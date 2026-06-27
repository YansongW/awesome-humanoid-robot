---
$id: ent_paper_yan_a_cut_and_fold_self_sustained_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A cut-and-fold self-sustained compliant oscillator for autonomous actuation
    of origami-inspired robots
  zh: 用于折纸启发式机器人自主驱动的切割折叠自持续柔顺振荡器
  ko: 오리가미에서 영감받은 로봇의 자율 구동을 위한 컷-앤-폴드 자가 지속 컴플라이언트 오실레이터
summary:
  en: Presents a printable self-sustained compliant oscillator built from two mechanically
    coupled self-opening switches—each combining a bistable buckled beam with a conductive
    supercoiled polymer (CSCP) thermal actuator—that generates periodic actuation
    from a constant electrical current without discrete electronics or control hardware.
  zh: 提出了一种可打印的自持续柔顺振荡器，该振荡器由两个机械耦合的自打开开关构成，每个开关将双稳态屈曲梁与导电超螺旋聚合物（CSCP）热驱动器相结合，可在无需离散电子元件或控制硬件的情况下，由恒定电流产生周期性驱动。
  ko: 두 개의 기계적으로 결합된 자가 개방 스위치로 구성된 프린터블 자가 지속 컴플라이언트 오실레이터를 제안한다. 각 스위치는 바이스테이블 벅빔(bistable
    buckled beam)과 전도성 초나선형 폴리머(CSCP) 열 구동기를 결합하여 이산 전자부품이나 제어 하드웨어 없이 일정한 전류로 주기적
    구동을 생성한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; quantitative claims
    and detailed citations require human review against the full paper.
sources:
- id: src_001
  type: paper
  title: A cut-and-fold self-sustained compliant oscillator for autonomous actuation
    of origami-inspired robots
  url: https://arxiv.org/abs/2108.08449
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
- system
---

## Overview

Origami-inspired robots promise rapid, low-cost fabrication by cutting and folding flexible 2D sheets, but they have traditionally required bulky rigid components and electronic control hardware for reliable actuation. This paper addresses that limitation by introducing a printable, self-sustained compliant oscillator that produces periodic motion using only a constant electrical current. The core building block is a self-opening switch formed by a bistable buckled beam paired with a conductive supercoiled polymer (CSCP) thermal actuator; two such switches are mechanically coupled to create a stable oscillation without discrete electronics or controllers.

The authors report that the oscillator is robust (9 of 10 prototypes worked on the first attempt), configurable (periods tunable from 3 s to 12 s), and durable (~10^3 cycles). It can output enough force to propel a printable swimmer at roughly 1.6 body lengths per minute, and it remains functional underwater and in high magnetic fields. An analytical model relates the oscillation period to material properties, geometric parameters, and supply current, supporting programmable design. Demonstrations include autonomous swimming, LED flashing, and fluid stirring, illustrating how the device can embed actuation and timing into monolithic, printable robotic structures.

## Key Contributions

- Design of a printable self-opening switch that implements a geometrically programmed time delay using a bistable buckled beam and a CSCP thermal actuator.
- Construction of a self-sustained oscillator from two coupled self-opening switches, producing periodic actuation from a constant electrical current without discrete components or control hardware.
- Analytical model characterizing how oscillation period depends on material, geometry, and supply current.
- Experimental demonstrations of autonomous gliding in a printable swimmer, LED flashing/animation, and fluid stirring.
- Validation that the oscillator operates underwater and in high magnetic fields, supporting extreme-environment applications.

## Relevance to Humanoid Robotics

Although the paper focuses on origami-inspired planar devices rather than humanoid robots, its actuation and manufacturing concepts are relevant to lightweight, mass-producible robotic hardware. The CSCP-based bistable switch provides a low-cost, compliant, electronics-free mechanism for generating timed, periodic motion, which could be adapted to soft joints, tendon-driven mechanisms, or deployable structures in future humanoids. Because the oscillator is monolithically integrable, printable, and nonmagnetic, it aligns with efforts to reduce dependence on conventional motors, gearboxes, and controllers in compact or extreme-environment robots.
