---
$id: ent_paper_child_a_whole_body_humanoid_te_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CHILD: a Whole-Body Humanoid Teleoperation System'
  zh: 'CHILD: a Whole-Body Humanoid Teleoperation System'
  ko: 'CHILD: a Whole-Body Humanoid Teleoperation System'
summary:
  en: 'CHILD: a Whole-Body Humanoid Teleoperation System is a 2025 work on teleoperation for humanoid robots.'
  zh: CHILD 是一套 2025 年提出的全身人形机器人遥操作系统，由研究团队开发，核心贡献在于实现了紧凑可重构的关节级控制，支持全身映射与移动操作，并集成了自适应力反馈以提升安全性与操作体验。
  ko: 'CHILD: a Whole-Body Humanoid Teleoperation System is a 2025 work on teleoperation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- child
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.00162v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CHILD: a Whole-Body Humanoid Teleoperation System (arXiv)'
  url: https://arxiv.org/abs/2508.00162
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有遥操作研究多聚焦于复杂操作任务，但缺乏对人形机器人全身关节级控制的支持，限制了任务多样性。CHILD 系统通过设计一款可装入标准婴儿背带的紧凑装置，使操作员能同时控制机器人四肢，并支持直接关节映射的全身控制与移动操作。系统还引入自适应力反馈机制，以优化操作体验并防止不安全关节运动。通过在单台人形机器人及多套双臂系统上进行的移动操作与全身控制演示，验证了系统能力，且硬件设计已开源。

## 核心内容
### 系统架构与设计
- **硬件设计**：CHILD 系统采用紧凑可重构结构，整体可装入标准婴儿背带，便于操作员携带与使用。
- **控制模式**：支持两种模式：
  - **直接关节映射**：实现操作员关节角度到机器人关节的实时映射，用于全身控制。
  - **移动操作**：结合移动与操作任务，扩展任务多样性。
- **力反馈机制**：集成自适应力反馈，根据操作状态动态调整，防止关节运动超出安全范围，同时提升操作员沉浸感。

### 实验验证
- **测试平台**：在单台人形机器人及多套双臂系统上完成验证。
- **演示任务**：包括移动操作（如行走中抓取物体）与全身控制（如协调四肢完成复杂姿态）。
- **关键结果**：系统成功实现全身关节级控制，任务完成度与操作稳定性得到验证。

### 开源与可复现性
- 硬件设计已完全开源，项目网站提供详细文档与代码，旨在促进社区复现与改进。
- 项目网站：https://uiuckimlab.github.io/CHILD-pages

## Overview
Recent advances in teleoperation have demonstrated robots performing complex manipulation tasks. However, existing works rarely support whole-body joint-level teleoperation for humanoid robots, limiting the diversity of tasks that can be accomplished. This work presents Controller for Humanoid Imitation and Live Demonstration (CHILD), a compact reconfigurable teleoperation system that enables joint level control over humanoid robots. CHILD fits within a standard baby carrier, allowing the operator control over all four limbs, and supports both direct joint mapping for full-body control and loco-manipulation. Adaptive force feedback is incorporated to enhance operator experience and prevent unsafe joint movements. We validate the capabilities of this system by conducting loco-manipulation and full-body control demonstrations on a humanoid robot and multiple dual-arm systems. Lastly, we open-source the design of the hardware promoting accessibility and reproducibility. Additional details and open-source information are available at our project website: https://uiuckimlab.github.io/CHILD-pages.

## 개요
최근 원격 조작 기술의 발전으로 로봇이 복잡한 조작 작업을 수행하는 것이 입증되었습니다. 그러나 기존 연구들은 휴머노이드 로봇의 전신 관절 수준 원격 조작을 거의 지원하지 않아 수행 가능한 작업의 다양성이 제한됩니다. 본 연구는 휴머노이드 로봇의 관절 수준 제어를 가능하게 하는 소형 재구성 가능 원격 조작 시스템인 CHILD(Controller for Humanoid Imitation and Live Demonstration)를 제시합니다. CHILD는 표준 아기 캐리어에 맞춰 제작되어 조작자가 네 팔다리를 모두 제어할 수 있으며, 전신 제어를 위한 직접 관절 매핑과 이동 조작(loco-manipulation)을 모두 지원합니다. 또한 적응형 힘 피드백을 통합하여 조작자 경험을 향상시키고 안전하지 않은 관절 움직임을 방지합니다. 우리는 휴머노이드 로봇과 여러 이중 팔 시스템에서 이동 조작 및 전신 제어 시연을 통해 이 시스템의 성능을 검증합니다. 마지막으로, 하드웨어 설계를 오픈소스로 공개하여 접근성과 재현성을 높입니다. 추가 세부 사항 및 오픈소스 정보는 프로젝트 웹사이트(https://uiuckimlab.github.io/CHILD-pages)에서 확인할 수 있습니다.

## 핵심 내용
최근 원격 조작 기술의 발전으로 로봇이 복잡한 조작 작업을 수행하는 것이 입증되었습니다. 그러나 기존 연구들은 휴머노이드 로봇의 전신 관절 수준 원격 조작을 거의 지원하지 않아 수행 가능한 작업의 다양성이 제한됩니다. 본 연구는 휴머노이드 로봇의 관절 수준 제어를 가능하게 하는 소형 재구성 가능 원격 조작 시스템인 CHILD(Controller for Humanoid Imitation and Live Demonstration)를 제시합니다. CHILD는 표준 아기 캐리어에 맞춰 제작되어 조작자가 네 팔다리를 모두 제어할 수 있으며, 전신 제어를 위한 직접 관절 매핑과 이동 조작(loco-manipulation)을 모두 지원합니다. 또한 적응형 힘 피드백을 통합하여 조작자 경험을 향상시키고 안전하지 않은 관절 움직임을 방지합니다. 우리는 휴머노이드 로봇과 여러 이중 팔 시스템에서 이동 조작 및 전신 제어 시연을 통해 이 시스템의 성능을 검증합니다. 마지막으로, 하드웨어 설계를 오픈소스로 공개하여 접근성과 재현성을 높입니다. 추가 세부 사항 및 오픈소스 정보는 프로젝트 웹사이트(https://uiuckimlab.github.io/CHILD-pages)에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2508.00162v2
