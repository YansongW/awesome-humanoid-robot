---
$id: ent_paper_agiloped_agile_open_source_hum_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AGILOped: Agile Open-Source Humanoid Robot for Research'
  zh: 'AGILOped: Agile Open-Source Humanoid Robot for Research'
  ko: 'AGILOped: Agile Open-Source Humanoid Robot for Research'
summary:
  en: 'AGILOped: Agile Open-Source Humanoid Robot for Research is a 2025 work on hardware design for humanoid robots.'
  zh: AGILOped 是一款 2025 年提出的开源人形机器人，由研究团队设计，旨在平衡高性能与可及性。其核心贡献在于采用高功率密度的商用可反向驱动执行器与标准电子元件，整机高 110 cm、重 14.5 kg，单人即可操作。实验验证了其在行走、跳跃、抗冲击与自主起身等任务中的研究可行性。
  ko: 'AGILOped: Agile Open-Source Humanoid Robot for Research is a 2025 work on hardware design for humanoid robots.'
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
- agiloped
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09364v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AGILOped: Agile Open-Source Humanoid Robot for Research (arXiv)'
  url: https://arxiv.org/abs/2509.09364
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前人形机器人领域虽涌现出多种定制化平台并展现出优异性能，但多数系统闭源或成本高昂。AGILOped 通过开源设计填补了这一空白，其硬件完全基于商用可反向驱动执行器与标准电子组件，降低了获取与维护门槛。机器人身高 110 cm、体重 14.5 kg，无需龙门架即可由单人操作，在行走、跳跃、冲击缓解与起身等实验中均验证了其作为研究平台的可靠性。

## 核心内容
### 设计目标与理念
AGILOped 旨在解决现有高性能人形机器人闭源或成本过高的问题，通过开源硬件设计使研究社区能够低成本复现与改进。

### 硬件架构
- **执行器**：采用商用高功率密度可反向驱动执行器，具备良好的力控与抗冲击能力。
- **电子元件**：全部使用标准商用组件，便于替换与维护。
- **物理参数**：身高 110 cm，重量仅 14.5 kg，轻量化设计使其无需龙门架即可由单人安全操作。

### 实验验证
- **行走与跳跃**：机器人能够稳定完成平地行走与跳跃动作，验证了运动控制基础能力。
- **冲击缓解**：通过反向驱动特性有效吸收落地冲击，保护硬件结构。
- **自主起身**：从倒地状态可自行恢复站立姿态，增强了实际部署中的鲁棒性。

### 结论
AGILOped 以开源、低成本、高性能的特点，为人形机器人研究提供了可复现的硬件平台，尤其适合需要频繁迭代与实验的学术场景。

## Overview
With academic and commercial interest for humanoid robots peaking, multiple platforms are being developed. Through a high level of customization, they showcase impressive performance. Most of these systems remain closed-source or have high acquisition and maintenance costs, however. In this work, we present AGILOped - an open-source humanoid robot that closes the gap between high performance and accessibility. Our robot is driven by off-the-shelf backdrivable actuators with high power density and uses standard electronic components. With a height of 110 cm and weighing only 14.5 kg, AGILOped can be operated without a gantry by a single person. Experiments in walking, jumping, impact mitigation and getting-up demonstrate its viability for use in research.

## 개요
휴머노이드 로봇에 대한 학계 및 상업적 관심이 최고조에 달하면서, 여러 플랫폼이 개발되고 있습니다. 높은 수준의 맞춤화를 통해 인상적인 성능을 보여주고 있지만, 대부분의 시스템은 폐쇄형 소스이거나 높은 도입 및 유지 비용이 듭니다. 본 연구에서는 고성능과 접근성 사이의 격차를 해소하는 오픈소스 휴머노이드 로봇 AGILOped를 소개합니다. 이 로봇은 높은 출력 밀도를 가진 상용 백드라이버블 액추에이터로 구동되며, 표준 전자 부품을 사용합니다. 키 110cm, 무게 14.5kg에 불과한 AGILOped는 한 명의 작업자가 갠트리 없이도 조작할 수 있습니다. 보행, 점프, 충격 완화 및 기립 실험을 통해 연구용으로의 실용성을 입증했습니다.

## 핵심 내용
휴머노이드 로봇에 대한 학계 및 상업적 관심이 최고조에 달하면서, 여러 플랫폼이 개발되고 있습니다. 높은 수준의 맞춤화를 통해 인상적인 성능을 보여주고 있지만, 대부분의 시스템은 폐쇄형 소스이거나 높은 도입 및 유지 비용이 듭니다. 본 연구에서는 고성능과 접근성 사이의 격차를 해소하는 오픈소스 휴머노이드 로봇 AGILOped를 소개합니다. 이 로봇은 높은 출력 밀도를 가진 상용 백드라이버블 액추에이터로 구동되며, 표준 전자 부품을 사용합니다. 키 110cm, 무게 14.5kg에 불과한 AGILOped는 한 명의 작업자가 갠트리 없이도 조작할 수 있습니다. 보행, 점프, 충격 완화 및 기립 실험을 통해 연구용으로의 실용성을 입증했습니다.

## 参考
- http://arxiv.org/abs/2509.09364v1
