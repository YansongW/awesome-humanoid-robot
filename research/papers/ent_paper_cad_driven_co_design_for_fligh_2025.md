---
$id: ent_paper_cad_driven_co_design_for_fligh_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
  zh: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
  ko: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
summary:
  en: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids is a 2025 work on hardware design for humanoid robots.
  zh: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids is a 2025 work on hardware design for humanoid robots.
  ko: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids is a 2025 work on hardware design for humanoid robots.
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
- cad_driven_co_design_for_fligh
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14935v1.
sources:
- id: src_001
  type: paper
  title: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids (arXiv)
  url: https://arxiv.org/abs/2509.14935
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
This paper presents a CAD-driven co-design framework for optimizing jet-powered aerial humanoid robots to execute dynamically constrained trajectories. Starting from the iRonCub-Mk3 model, a Design of Experiments (DoE) approach is used to generate 5,000 geometrically varied and mechanically feasible designs by modifying limb dimensions, jet interface geometry (e.g., angle and offset), and overall mass distribution. Each model is constructed through CAD assemblies to ensure structural validity and compatibility with simulation tools. To reduce computational cost and enable parameter sensitivity analysis, the models are clustered using K-means, with representative centroids selected for evaluation. A minimum-jerk trajectory is used to assess flight performance, providing position and velocity references for a momentum-based linearized Model Predictive Control (MPC) strategy. A multi-objective optimization is then conducted using the NSGA-II algorithm, jointly exploring the space of design centroids and MPC gain parameters. The objectives are to minimize trajectory tracking error and mechanical energy expenditure. The framework outputs a set of flight-ready humanoid configurations with validated control parameters, offering a structured method for selecting and implementing feasible aerial humanoid designs.

## 核心内容
This paper presents a CAD-driven co-design framework for optimizing jet-powered aerial humanoid robots to execute dynamically constrained trajectories. Starting from the iRonCub-Mk3 model, a Design of Experiments (DoE) approach is used to generate 5,000 geometrically varied and mechanically feasible designs by modifying limb dimensions, jet interface geometry (e.g., angle and offset), and overall mass distribution. Each model is constructed through CAD assemblies to ensure structural validity and compatibility with simulation tools. To reduce computational cost and enable parameter sensitivity analysis, the models are clustered using K-means, with representative centroids selected for evaluation. A minimum-jerk trajectory is used to assess flight performance, providing position and velocity references for a momentum-based linearized Model Predictive Control (MPC) strategy. A multi-objective optimization is then conducted using the NSGA-II algorithm, jointly exploring the space of design centroids and MPC gain parameters. The objectives are to minimize trajectory tracking error and mechanical energy expenditure. The framework outputs a set of flight-ready humanoid configurations with validated control parameters, offering a structured method for selecting and implementing feasible aerial humanoid designs.

## 参考
- http://arxiv.org/abs/2509.14935v1

