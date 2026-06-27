---
$id: ent_paper_fahmideh_a_study_of_influential_factors_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A study of influential factors in designing self-reconfigurable robots for green
    manufacturing
  zh: 面向绿色制造的自重构机器人设计影响因素研究
  ko: 녹색 제조를 위한 자체 재구성 로봇 설계 영향 요인 연구
summary:
  en: Fahmideh and Lammers (2018) propose a preliminary research model of design-time,
    run-time, and hardware factors that influence whether self-reconfigurable robots
    enable green manufacturing, and outline a two-phase empirical validation plan.
  zh: Fahmideh 与 Lammers（2018）提出了一个包含设计时、运行时与硬件因素的初步研究模型，用以解释自重构机器人如何影响绿色制造，并规划了两阶段实证验证方案。
  ko: Fahmideh와 Lammers(2018)는 자체 재구성 로봇이 녹색 제조를 가능하게 하는지에 영향을 미치는 설계 시점, 실행 시점 및
    하드웨어 요인에 대한 예비 연구 모델을 제안하고 두 단계의 실증 검증 계획을 제시한다.
domains:
- 06_design_engineering
- 03_manufacturing_processes
- 02_components
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
tags:
- green_manufacturing
- self_reconfigurable_robots
- energy_efficiency
- sustainable_design
- modular_robots
- design_time_factors
- runtime_adaptation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from abstract and metadata; full text of arXiv 2004.08024 not
    independently read. Empirical validation is planned, not completed.
sources:
- id: src_001
  type: paper
  title: A study of influential factors in designing self-reconfigurable robots for
    green manufacturing
  url: https://arxiv.org/abs/2004.08024
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This ACIS 2018 research-in-progress paper by Fahmideh and Lammers examines the interdisciplinary design factors that determine whether self-reconfigurable robots support green manufacturing. The authors observe that while prior work has largely focused on technical, energy-reduction mechanisms for modular robots, the broader software and hardware design decisions that enable or impede sustainability remain underexplored. They therefore develop a preliminary research model that organizes influential factors into three constructs: software design-time, software run-time, and hardware design.

The proposed validation plan is two-phase: first, semi-structured interviews with engineers experienced in building self-reconfigurable robots for agriculture; second, a longitudinal survey intended to test the relationships between design factors and green manufacturing outcomes. The paper does not yet report empirical results; it presents the model, constructs, and intended methodology.

## Key Contributions

- Identifies and analyzes design factors for green-aware self-reconfigurable robots across software and hardware domains.
- Proposes a preliminary research model balancing software design-time, software run-time, and hardware design aspects.
- Outlines an empirical validation strategy combining semi-structured interviews with a longitudinal practitioner survey.
- Strengthens the conceptual link between robot design decisions and green manufacturing outcomes.

## Relevance to Humanoid Robotics

Although the paper focuses on modular self-reconfigurable robots used in manufacturing and greenhouse agriculture, its green-aware design principles are directly transferable to humanoid robotics. Energy-efficient software design, runtime adaptation policies, and low-environmental-impact hardware/material selection are all critical for reducing the carbon footprint and operating cost of humanoid robots deployed at scale. The identified constructs can inform life-cycle design decisions for humanoid platforms intended for mass production and industrial service.
