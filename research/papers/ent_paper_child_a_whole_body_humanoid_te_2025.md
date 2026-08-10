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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.00162v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (657 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2508.00162v2

## 개요
기존 원격 조작 연구는 주로 복잡한 조작 작업에 초점을 맞추고 있지만, 인간형 로봇의 전신 관절 수준 제어를 지원하지 못해 작업 다양성에 제한이 있었습니다. CHILD 시스템은 표준 유아용 캐리어에 장착할 수 있는 컴팩트한 장치를 설계하여, 조작자가 로봇의 사지를 동시에 제어할 수 있게 하고, 직접 관절 매핑을 통한 전신 제어와 이동 조작을 지원합니다. 또한 시스템은 적응형 힘 피드백 메커니즘을 도입하여 조작 경험을 최적화하고 안전하지 않은 관절 움직임을 방지합니다. 단일 인간형 로봇과 다중 이중 팔 시스템에서의 이동 조작 및 전신 제어 시연을 통해 시스템 성능을 검증했으며, 하드웨어 설계는 오픈소스로 공개되었습니다.

## 핵심 내용
### 시스템 아키텍처 및 설계
- **하드웨어 설계**: CHILD 시스템은 컴팩트하고 재구성 가능한 구조를 채택하여 전체가 표준 유아용 캐리어에 장착될 수 있어, 조작자가 휴대하고 사용하기 용이합니다.
- **제어 모드**: 두 가지 모드를 지원합니다:
  - **직접 관절 매핑**: 조작자의 관절 각도를 로봇 관절에 실시간 매핑하여 전신 제어에 사용합니다.
  - **이동 조작**: 이동과 조작 작업을 결합하여 작업 다양성을 확장합니다.
- **힘 피드백 메커니즘**: 적응형 힘 피드백을 통합하여 조작 상태에 따라 동적으로 조정하며, 관절 움직임이 안전 범위를 초과하지 않도록 방지하고 조작자의 몰입감을 향상시킵니다.

### 실험 검증
- **테스트 플랫폼**: 단일 인간형 로봇과 다중 이중 팔 시스템에서 검증을 완료했습니다.
- **시연 작업**: 이동 조작(예: 보행 중 물체 잡기)과 전신 제어(예: 사지를 조정하여 복잡한 자세 수행)를 포함합니다.
- **주요 결과**: 시스템이 전신 관절 수준 제어를 성공적으로 구현했으며, 작업 완성도와 조작 안정성이 검증되었습니다.

### 오픈소스 및 재현성
- 하드웨어 설계는 완전히 오픈소스로 공개되었으며, 프로젝트 웹사이트에서 상세 문서와 코드를 제공하여 커뮤니티의 재현 및 개선을 촉진합니다.
- 프로젝트 웹사이트: https://uiuckimlab.github.io/CHILD-pages
