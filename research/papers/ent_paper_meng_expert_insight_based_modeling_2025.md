---
$id: ent_paper_meng_expert_insight_based_modeling_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Expert Insight-Based Modeling of Non-Kinetic Strategic Deterrence of Rare Earth
    Supply Disruption: A Simulation-Driven Systematic Framework'
  zh: 基于专家洞见的稀土供应中断非动能战略威慑建模：一种仿真驱动的系统化框架
  ko: '전문가 통찰 기반 희토류 공급 중단의 비동력 전략 억제 모델링: 시뮬레이션 중심 체계적 프레임워크'
summary:
  en: Wei Meng's 2025 arXiv paper proposes a simulation-driven REG-CAP framework that
    maps rare-earth resource dependencies to military equipment, technology generations,
    and combat capabilities, using HGNN, LSTM, ODEs, and strategic signal functions
    to model non-kinetic deterrence trajectories under supply disruption.
  zh: Wei Meng 于 2025 年在 arXiv 发表本文，提出一种仿真驱动的 REG-CAP 框架，将稀土资源依赖映射至军事装备、技术代际与作战能力，并结合
    HGNN、LSTM、常微分方程与战略信号函数，对供应中断情境下的非动能威慑路径进行建模。
  ko: Wei Meng의 2025년 arXiv 논문은 희토류 자원 의존성을 군사 장비·기술 세대·전투 능력에 매핑하는 REG-CAP 프레임워크를
    제안하고, HGNN·LSTM·상미분방정식·전략 신호 함수를 활용해 공급 중단 상황에서 비동력 억제 궤적을 모델링한다.
domains:
- 01_raw_materials
- 05_mass_production
- 12_policy_regulation_ethics
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- rare_earth_elements
- supply_chain_disruption
- strategic_deterrence
- geopolitical_risk
- actuator_materials
- mass_production_risk
- hgnn
- lstm
- ode_modeling
- security_critical_zones
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: 'Expert Insight-Based Modeling of Non-Kinetic Strategic Deterrence of Rare
    Earth Supply Disruption: A Simulation-Driven Systematic Framework'
  url: https://arxiv.org/abs/2506.11645
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

This 2025 arXiv paper by Wei Meng develops a quantifiable, simulation-driven framework for non-kinetic strategic deterrence triggered by rare-earth supply disruption. The core architecture is the Resource-Equipment-Generation Gap-Capability (REG-CAP) multilayer graph, which couples rare-earth resource nodes (Nd, Dy, Tb, Ce, Ga, Ge) to equipment platforms, technology-generation layers, and warfighting capability clusters. The paper proposes four interlocking modelling components—Security Critical Zones (SCZ), Strategic Signal Injection Function (SSIF), System-Capability Migration Function (SCIF), and Policy-Capability Transfer Function (PCTF)—to capture how institutional deterrence signals propagate through the system and produce nonlinear suppression trajectories.

Methodologically, the work combines hierarchical graph neural networks (HGNN/GAT/GraphSAGE) and LSTM networks for structural dependency learning and time-series forecasting, together with parametric ordinary differential equations, piecewise functions, and path-overlap covariance matrices to represent the tempo and coupling of degradation. The empirical basis consists of multi-round expert interviews led by Dr. Daniel O'Connor of the Rare Earth Exchange and open scenario analyses focusing on U.S.-China competition in intelligence/surveillance/reconnaissance (ISR), electronic warfare, and rare-earth control.

The results highlight that institutional deterrence signals exhibit strong tempo effects and path-coupling effects, and can cause rapid, disintegrative ruptures of capability systems within short lag windows. The framework is presented as adaptable to other national strategic-resource contexts and as extensible to AI sandbox engines for counterfactual and situational modelling.

## Key Contributions

- Introduces the REG-CAP multilayer coupled framework that maps rare-earth resources to equipment, generational technology, and combat capability.
- Proposes Security Critical Zones (SCZ) to identify high-coupling, low-lag capability clusters at risk of synchronous collapse.
- Develops an HGNN + LSTM joint model for structural dependency learning and nonlinear degradation-trajectory prediction.
- Combines ODEs, piecewise functions, the Strategic Signal Injection Function (SSIF), and the Policy-Capability Transfer Function (PCTF) to capture institutional deterrence tempo.
- Provides quantitative visualisation tools—Strategic Suppression Rhythm Map, Multi-Path Convergence Risk Map, Strategic Deterrence Corridor Map, and Strategic Policy Impact Surface—for policy windows.

## Relevance to Humanoid Robotics

Although the paper does not study humanoid robots directly, its analysis of rare-earth supply-chain dependency is materially relevant to humanoid robotics. Humanoid actuators and drive motors typically rely on high-performance rare-earth permanent magnets (chiefly Nd-Fe-B, often doped with Dy or Tb), and large-scale production would expose manufacturers to the same geopolitical supply-disruption risks modeled here.

The REG-CAP framework, SCZ identification, and signal-injection functions could therefore be extrapolated to forecast chokepoints in humanoid-robot mass production, evaluate alternative-material strategies, and inform policy buffers for critical actuator materials. This relevance is inferred from the technology domain; the paper itself does not mention humanoid robots or actuators.
