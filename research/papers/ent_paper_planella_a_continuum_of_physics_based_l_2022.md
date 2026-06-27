---
$id: ent_paper_planella_a_continuum_of_physics_based_l_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Continuum of Physics-Based Lithium-Ion Battery Models Reviewed
  zh: 基于物理的锂离子电池模型连续谱综述
  ko: 물리 기반 리튬 이온 배터리 모델의 연속체에 대한 리뷰
summary:
  en: A review that presents a unified reductive framework deriving continuum electrochemical
    battery models from a high-fidelity microscale model down to the Single Particle
    Model, with critical discussion of assumptions, limitations, and coupled thermal
    extensions.
  zh: 该综述提出了一个统一的约化框架，从高保真微尺度模型推导出单粒子模型等连续电化学电池模型，并批判性讨论了各种假设、局限性以及热耦合扩展。
  ko: 고충실도 미시규모 모델에서 단일 입자 모델까지의 연속 전기화학 배터리 모델을 유도하는 통합적 환원 프레임워크를 제시하고, 가정들과 한계,
    열-전기화학 결합 확장에 대해 비판적으로 논의한 리뷰이다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- lithium_ion_battery
- physics_based_modeling
- battery_management_system
- electrochemical_model
- thermal_management
- porous_electrode_theory
- doyle_fuller_newman_model
- single_particle_model
- single_particle_model_with_electrolyte
- microscale_model
- homogenised_model
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text section-level
    citations were not independently verified.
sources:
- id: src_001
  type: paper
  title: A Continuum of Physics-Based Lithium-Ion Battery Models Reviewed
  url: https://arxiv.org/abs/2203.16091
  date: '2022'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---

## Overview

This review article surveys physics-based lithium-ion battery models that are derived from porous electrode theory. Rather than treating simplified models as independent formulations, the authors organize them into a single reductive framework that begins with a detailed microscale model and proceeds through homogenised, Doyle-Fuller-Newman (DFN), Single Particle Model with electrolyte (SPMe), and Single Particle Model (SPM) representations. Each reduction step is tied to explicit physical and geometric assumptions, which clarifies why different model fidelities are appropriate for different applications.

The paper emphasizes that model selection should balance accuracy against computational cost. High-fidelity microscale and homogenised models can capture microstructural effects but require detailed geometric data and substantial compute resources; the DFN model offers a widely used compromise for cell-level simulation; and SPM-type models are suitable for fast calculations such as battery management and real-time control. The authors also provide a critical discussion of the strengths and weaknesses of each level, including parameter requirements and rate limitations.

Finally, the review surveys extensions beyond isothermal electrochemistry, with particular attention to coupled thermal models for large-format cells. Additional topics include phase-field models, double-layer capacitance, particle-size distributions, mechanical deformation, and degradation mechanisms such as solid electrolyte interphase growth.

## Key Contributions

- Unified reductive framework linking microscale, homogenised, DFN, SPMe, and SPM models through explicit assumptions.
- Critical comparison of the advantages and shortcomings of each model fidelity to aid application-specific model selection.
- Overview of coupled thermal-electrochemical models for large-format cells.
- Survey of extensions including phase-field models, double-layer capacitance, particle-size distributions, mechanical models, and degradation mechanisms.

## Relevance to Humanoid Robotics

Mobile humanoid robots depend on high-energy-density, safe, and reliable lithium-ion battery packs for untethered operation. The modeling hierarchy reviewed in this paper provides the electrochemical foundation needed to select appropriate cell models, design thermal management systems, and develop battery management algorithms for humanoid power systems. In particular, the trade-off between detailed DFN simulations for offline pack design and reduced-order SPM/SPMe models for online state estimation is directly relevant to mass-produced humanoid platforms.

Because humanoids impose dynamic load profiles and have limited space and mass budgets, accurate yet computationally efficient battery models are essential for predicting range, preventing thermal runaway, and optimizing charging strategies. This review offers a principled map of which physics-based simplifications are valid under which operating conditions, supporting safer and more efficient integration of lithium-ion power systems into humanoid robots.
