---
$id: ent_paper_vouga_asynchronous_variational_integ_2009
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Asynchronous Variational Integration of Interaction Potentials for Contact Mechanics
  zh: 用于接触力学的相互作用势能异步变分积分法
  ko: 접촉 역학을 위한 상호작용 포텐셜의 비동기 변분 적분법
summary:
  en: Extends asynchronous variational integrators (AVIs) to interaction potentials
    such as penalty contact forces, proves that AVIs remain multisymplectic under
    relaxed assumptions, and validates long-term energy stability on a thin sphere-plate
    impact using the Asynchronous Contact Mechanics framework.
  zh: 将异步变分积分器（AVI）扩展至惩罚接触力等相互作用势能，在放宽的假设下证明其多辛结构保持性，并通过异步接触力学框架在薄球-板冲击实验中验证了长期能量稳定性。
  ko: 비동기 변분 적분기(AVI)를 페널티 접촉력과 같은 상호작용 포텐셜로 확장하고, 완화된 가정 하에서 다중심플렉틱성을 증명하며, 비동기 접촉
    역학(ACM) 프레임워크를 통해 얇은 구-판 충격에서 장기 에너지 안정성을 검증한다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- asynchronous_variational_integrator
- variational_integrator
- multisymplectic_integrator
- contact_mechanics
- penalty_method
- multibody_dynamics
- thin_shells
- energy_momentum_conservation
- foot_ground_contact
- articulated_dynamics
- long_time_simulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv PDF and abstract; human review is needed before
    full verification.
sources:
- id: src_001
  type: paper
  title: Asynchronous Variational Integration of Interaction Potentials for Contact
    Mechanics
  url: https://arxiv.org/abs/0907.0706
  date: '2009'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Variational integrators discretize a system's Lagrangian rather than its equations of motion, giving discrete analogues of Noether's theorem, momentum conservation, and symplectic structure. Asynchronous variational integrators (AVIs) generalize this idea by allowing each spatial element to advance with its own time step, avoiding the cost of integrating the whole system at the stiffest stable step. Prior AVI theory, however, required potentials to be of an elastic type—defined by volume integrals over the material domain—so its multisymplecticity proof did not cover interaction potentials such as penalty forces used for contact.

This paper relaxes that assumption. It proves that AVIs remain multisymplectic for a broader class of potentials, including interaction potentials, and presents a triangulation-free AVI formulation that supports arbitrary, possibly non-disjoint spatial stencils. The relaxation allows the same geometric integrator to handle penalty-based contact in elastica such as thin shells and in multibody systems such as granular materials, with no long-term drift of conserved quantities such as energy and momentum when using the algorithms of Harmon et al.'s Asynchronous Contact Mechanics framework.

The theoretical development is accompanied by a numerical experiment that reproduces the thin sphere-plate impact scenario from Cirak and West's Decomposition Contact Response (DCR) paper. The simulation uses ACM built on triangulation-free AVIs, and the reported total energy shows the high-frequency, low-amplitude oscillations typical of symplectic methods but no noticeable long-term drift, in contrast to the DCR baseline data.

## Key Contributions

- Extended multisymplecticity proof for AVIs that covers interaction potentials, including penalty contact forces.
- Triangulation-free AVI formulation supporting arbitrary, possibly overlapping spatial stencils.
- Enablement of long-duration contact simulation in elastica and multibody systems without drift of energy and momentum.
- Numerical validation on a thin sphere-plate impact using the Asynchronous Contact Mechanics framework, comparing energy behavior against Decomposition Contact Response.

## Relevance to Humanoid Robotics

Stable, energy- and momentum-conserving contact integration over long durations is directly relevant to humanoid robotics. Locomotion involves repeated foot-ground impacts, articulated multibody dynamics, and transient contact forces whose numerical drift can destabilize controllers or design studies. The asynchronous, multisymplectic integration of penalty-based contact potentials described here provides a principled way to simulate these phenomena with long-term stability, supporting both controller development and mechanical design evaluation.
