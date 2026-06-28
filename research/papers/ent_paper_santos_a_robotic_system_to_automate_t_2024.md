---
$id: ent_paper_santos_a_robotic_system_to_automate_t_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Robotic System to Automate the Disassembly of PCB Components
  zh: 用于自动化拆解印刷电路板元件的机器人系统
  ko: PCB 부품 자동 분해를 위한 로봇 시스템
summary:
  en: Santos, Marques, and Neto present a robotic system that automates desoldering
    and extraction of PCB components from e-waste using a customized tool on a collaborative
    robot arm with Cartesian force control, reporting approximately 100% desoldering
    success for larger components.
  zh: Santos、Marques 和 Neto 提出了一种机器人系统，该系统利用安装在协作机械臂上的定制工具，结合笛卡尔力控制，实现电子废弃物中印刷电路板元件的自动去焊与提取，并对较大尺寸元件报告了接近
    100% 的去焊成功率。
  ko: Santos, Marques, Neto는 협동 로봇 암에 장착된 맞춤형 도구와 카르테시안 힘 제어를 사용하여 전자 폐기물에서 PCB 부품의
    자동 납땜 제거 및 추출을 수행하는 로봇 시스템을 제안하며, 큰 부품에 대해 약 100%의 납땜 제거 성공률을 보고한다.
domains:
- 03_manufacturing_processes
- 04_assembly_integration_testing
- 02_components
layers:
- midstream
functional_roles:
- knowledge
- process
- tool_equipment
tags:
- robotic_disassembly
- pcb_recycling
- e_waste
- force_control
- compliant_manipulation
- end_effector
- collaborative_robot
- desoldering
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the abstract and provided metadata; hardware details, citation
    sections, and quantitative claims require human verification against the full
    paper.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: A Robotic System to Automate the Disassembly of PCB Components
  url: https://arxiv.org/abs/2403.05309
  date: '2024'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

The disposal and recycling of electronic waste is a major global challenge, and the non-destructive disassembly of printed circuit board (PCB) components is a critical step for efficient recycling. Manual disassembly remains common because of the variety and complexity of components, so this work develops a robotic system to automate desoldering and component extraction. The system combines a collaborative robot arm, a two-finger gripper, a customized desoldering/grasping tool, a hot-air device, and a heated plate to melt solder, apply controlled contact force, grasp the loosened component, and transport it away.

The core manipulation strategy is a Cartesian-level force-motion controller. It commands a desired contact force along the extraction direction while remaining compliant in the other directions, so the tool can maintain stable contact with the PCB component as the solder melts. The custom end-effector uses a push-pull mechanism integrated with the gripper: it pushes to desolder and then pulls to grasp and remove the component. This design is intended to handle real, densely populated PCBs, including boards taken from mobile phones.

The disassembly process is organized into six phases: approach, contact, melting, grasping, transport, and release. Experiments show that the desoldering step itself is highly reliable, with approximately 100% success reported for larger components. However, the overall autonomous removal rate is limited by a grasping success rate of roughly 50%, and the current prototype lacks automated vision and automated hot-air application by a second arm.

## Key Contributions

- A novel robotic tool design that combines a push-pull desoldering mechanism with a two-finger gripper for PCB component removal.
- A force-motion control strategy that maintains desired contact force along the extraction direction while providing compliance in other directions.
- Experimental validation on real PCBs, including mobile-phone boards, demonstrating approximately 100% desoldering success for larger components.
- A six-phase pipeline (approach, contact, melting, grasping, transport, release) for automated PCB component disassembly.

## Relevance to Humanoid Robotics

Although the paper targets PCB recycling rather than humanoid robots, the underlying techniques are directly transferable to humanoid manufacturing and end-of-life handling. Force-controlled compliant manipulation, custom end-effector design, and staged assembly/disassembly pipelines are exactly the skills needed for precise insertion, fastening, and removal tasks during humanoid robot production and field servicing. The work also illustrates how collaborative robot arms can be adapted with specialized tooling to perform delicate contact tasks, a paradigm relevant to humanoid upper-body manipulation cells.
