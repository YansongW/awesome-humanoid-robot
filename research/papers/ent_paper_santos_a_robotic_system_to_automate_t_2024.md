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
  en: Santos, Marques, and Neto present a robotic system that automates desoldering and extraction of PCB components from
    e-waste using a customized tool on a collaborative robot arm with Cartesian force control, reporting approximately 100%
    desoldering success for larger components.
  zh: Santos、Marques 和 Neto 提出了一种机器人系统，该系统利用安装在协作机械臂上的定制工具，结合笛卡尔力控制，实现电子废弃物中印刷电路板元件的自动去焊与提取，并对较大尺寸元件报告了接近 100% 的去焊成功率。
  ko: Santos, Marques, Neto는 협동 로봇 암에 장착된 맞춤형 도구와 카르테시안 힘 제어를 사용하여 전자 폐기물에서 PCB 부품의 자동 납땜 제거 및 추출을 수행하는 로봇 시스템을 제안하며, 큰 부품에
    대해 약 100%의 납땜 제거 성공률을 보고한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.05309v1.
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
## 概述
The disposal and recycling of electronic waste (e-waste) is a global challenge. The disassembly of components is a crucial step towards an efficient recycling process, avoiding the destructive methods. Although most disassembly work is still done manually due to the diversity and complexity of components, there is a growing interest in developing automated methods to improve efficiency and reduce labor costs. This study aims to robotize the desoldering process and extracting components from printed circuit boards (PCBs), with the goal of automating the process as much as possible. The proposed strategy consists of several phases, including the controlled contact of the robotic tool with the PCB components. A specific tool was developed to apply a controlled force against the PCB component, removing it from the board. The results demonstrate that it is feasible to remove the PCB components with a high success rate (approximately 100% for the bigger PCB components).

## 核心内容
The disposal and recycling of electronic waste (e-waste) is a global challenge. The disassembly of components is a crucial step towards an efficient recycling process, avoiding the destructive methods. Although most disassembly work is still done manually due to the diversity and complexity of components, there is a growing interest in developing automated methods to improve efficiency and reduce labor costs. This study aims to robotize the desoldering process and extracting components from printed circuit boards (PCBs), with the goal of automating the process as much as possible. The proposed strategy consists of several phases, including the controlled contact of the robotic tool with the PCB components. A specific tool was developed to apply a controlled force against the PCB component, removing it from the board. The results demonstrate that it is feasible to remove the PCB components with a high success rate (approximately 100% for the bigger PCB components).

## 参考
- http://arxiv.org/abs/2403.05309v1

