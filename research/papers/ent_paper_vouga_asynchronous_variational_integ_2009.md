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
  en: Extends asynchronous variational integrators (AVIs) to interaction potentials such as penalty contact forces, proves
    that AVIs remain multisymplectic under relaxed assumptions, and validates long-term energy stability on a thin sphere-plate
    impact using the Asynchronous Contact Mechanics framework.
  zh: 将异步变分积分器（AVI）扩展至惩罚接触力等相互作用势能，在放宽的假设下证明其多辛结构保持性，并通过异步接触力学框架在薄球-板冲击实验中验证了长期能量稳定性。
  ko: 비동기 변분 적분기(AVI)를 페널티 접촉력과 같은 상호작용 포텐셜로 확장하고, 완화된 가정 하에서 다중심플렉틱성을 증명하며, 비동기 접촉 역학(ACM) 프레임워크를 통해 얇은 구-판 충격에서 장기 에너지 안정성을
    검증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/0907.0706v1.
sources:
- id: src_001
  type: paper
  title: Asynchronous Variational Integration of Interaction Potentials for Contact Mechanics
  url: https://arxiv.org/abs/0907.0706
  date: '2009'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Asynchronous Variational Integrators (AVIs) have demonstrated long-time good energy behavior. It was previously conjectured that this remarkable property is due to their geometric nature: they preserve a discrete multisymplectic form. Previous proofs of AVIs' multisymplecticity assume that the potentials are of an elastic type, i.e., specified by volume integration over the material domain, an assumption violated by interaction-type potentials, such as penalty forces used to model mechanical contact. We extend the proof of AVI multisymplecticity, showing that AVIs remain multisymplectic under relaxed assumptions on the type of potential. The extended theory thus accommodates the simulation of mechanical contact in elastica (such as thin shells) and multibody systems (such as granular materials) with no drift of conserved quantities (energy, momentum) over long run times, using the algorithms in [3]. We present data from a numerical experiment measuring the long time energy behavior of simulated contact, comparing the method built on multisymplectic integration of interaction potentials to recently proposed methods for thin shell contact.

## 核心内容
Asynchronous Variational Integrators (AVIs) have demonstrated long-time good energy behavior. It was previously conjectured that this remarkable property is due to their geometric nature: they preserve a discrete multisymplectic form. Previous proofs of AVIs' multisymplecticity assume that the potentials are of an elastic type, i.e., specified by volume integration over the material domain, an assumption violated by interaction-type potentials, such as penalty forces used to model mechanical contact. We extend the proof of AVI multisymplecticity, showing that AVIs remain multisymplectic under relaxed assumptions on the type of potential. The extended theory thus accommodates the simulation of mechanical contact in elastica (such as thin shells) and multibody systems (such as granular materials) with no drift of conserved quantities (energy, momentum) over long run times, using the algorithms in [3]. We present data from a numerical experiment measuring the long time energy behavior of simulated contact, comparing the method built on multisymplectic integration of interaction potentials to recently proposed methods for thin shell contact.

## 参考
- http://arxiv.org/abs/0907.0706v1

