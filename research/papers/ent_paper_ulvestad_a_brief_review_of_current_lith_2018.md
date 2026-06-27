---
$id: ent_paper_ulvestad_a_brief_review_of_current_lith_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Brief Review of Current Lithium Ion Battery Technology and Potential Solid
    State Battery Technologies
  zh: 当前锂离子电池技术与潜在固态电池技术简要综述
  ko: 현재 리튬 이온 전지 기술 및 잠재적 고체 전해질 전지 기술에 대한 간단한 리뷰
summary:
  en: A 2018 review by Andrew Ulvestad that benchmarks state-of-the-art lithium-ion
    batteries against emerging solid-state batteries with lithium-metal anodes, comparing
    sulfide, polymer, and oxide solid electrolytes and surveying commercial SSB programs.
  zh: Andrew Ulvestad于2018年发表的综述，将最先进的锂离子电池与采用锂金属负极的新兴固态电池进行基准比较，比较了硫化物、聚合物和氧化物固态电解质，并调研了商用固态电池项目。
  ko: Andrew Ulvestad가 2018년에 발표한 개관 논문으로, 최첨단 리튬 이온 전지와 리튬 금속 음극을 사용하는 신흥 고체 전해질
    전지를 비교하며, 황화물·고분자·산화물 고체 전해질 및 상용 SSB 프로그램을 조사한다.
domains:
- 02_components
- 01_raw_materials
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- lithium_ion_battery
- solid_state_battery
- solid_electrolyte
- lithium_metal_anode
- energy_density
- battery_safety
- power_source
- mobile_energy_storage
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: A Brief Review of Current Lithium Ion Battery Technology and Potential Solid
    State Battery Technologies
  url: https://arxiv.org/abs/1803.04317
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- system
---

## Overview

This 2018 arXiv review by Andrew Ulvestad surveys the state of the art in liquid-electrolyte lithium-ion batteries (LIBs) and evaluates whether emerging solid-state batteries (SSBs) can surpass them. The paper begins with commercial LIBs, estimating current gravimetric energy density around 270 Wh/kg and volumetric energy density around 732 Wh/L for Panasonic 18650 cells used in Tesla vehicles, and notes that the current chemistry may reach roughly 400 Wh/kg and 1200 Wh/L. It emphasizes that cost parity near $100/kWh is likely within reach for conventional LIBs, driven by scale and manufacturing learning.

The review then examines SSBs, whose primary technical motivation is enabling lithium-metal (Li metal) anodes by using a solid electrolyte as a physical barrier to dendrites. It derives that replacing the carbon anode with lithium metal yields only about a 19% gravimetric and 8% volumetric improvement for a typical cell, because cell-level energy density depends nonlinearly on the capacities and densities of both electrodes plus inactive mass. The paper evaluates three solid-electrolyte families—sulfides, polymers, and oxides—and concludes that sulfides currently offer the best conductivity and lowest density, while polymers are easier to manufacture but require elevated temperature, and oxides are stable but dense and difficult to process.

Finally, the paper surveys commercial SSB efforts, including programs by Toyota/AIST, BMW/SolidPower, Bolloré, SEEO, and Solid Energy, and argues that unresolved interfacial impedance, air/moisture sensitivity, and inconsistent reporting of inactive material weights mean no reported SSB yet matches the full performance envelope of state-of-the-art LIBs.

## Key Contributions

- Quantifies the ~20% gravimetric energy-density upside of enabling Li-metal anodes via solid electrolytes, using a specific-cell-capacity model that accounts for cathode/anode capacities, masses, voltages, and inactive material.
- Compares sulfide, polymer, and oxide solid-state electrolyte classes on conductivity, density, manufacturability, and interfacial stability, identifying sulfides as the leading class at the time of writing.
- Compiles reported functioning solid-state battery cells and highlights inconsistent reporting of inactive-material and excess-lithium weights that complicate fair comparison with liquid-electrolyte LIBs.
- Surveys commercial SSB programs (Toyota/AIST, BMW/SolidPower, Bolloré, Medtronic, SEEO, Solid Energy, and others) and their publicly claimed performance.
- Argues that liquid-electrolyte LIBs will likely remain dominant in the near term because of rapidly falling costs and unresolved solid-electrolyte challenges.

## Relevance to Humanoid Robotics

Humanoid robots operating untethered require power sources that simultaneously deliver high gravimetric and volumetric energy density, long cycle life, and inherent safety. This review directly addresses those criteria by benchmarking current lithium-ion cells and the main solid-state alternatives on energy density, coulombic efficiency, and manufacturability. Its conclusion that conventional LIBs are still the most mature and cost-effective option provides a useful baseline for selecting onboard power systems in humanoid platforms.

At the same time, the paper identifies the conditions under which solid-state batteries could become advantageous—such as high-rate discharge, wide temperature operation, and improved safety—attributes that are highly relevant to dynamic, mobile humanoids. By cataloging solid-electrolyte material classes, their processing constraints, and commercial development status, the review supports knowledge-base entries for battery components, raw materials, and mass-production considerations in humanoid-robot design.
