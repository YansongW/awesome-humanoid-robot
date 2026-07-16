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
  zh: 'Asynchronous Variational Integrators (AVIs) have demonstrated long-time good energy behavior. It was previously conjectured
    that this remarkable property is due to their geometric nature: they preserve a discrete multisymplectic form. Previous
    proofs of AVIs'' multisymplecticity assume that the potentials are of an elastic type, i.e., specified by volume integration
    over the material domain, an assumption violated by interaction-type potentials, such as penalty forces used to model
    mechanical contact. We extend the proof of AVI multisymplecticity, showing that AVIs remain multisymplectic under'
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

## Overview
Asynchronous Variational Integrators (AVIs) have demonstrated long-time good energy behavior. It was previously conjectured that this remarkable property is due to their geometric nature: they preserve a discrete multisymplectic form. Previous proofs of AVIs' multisymplecticity assume that the potentials are of an elastic type, i.e., specified by volume integration over the material domain, an assumption violated by interaction-type potentials, such as penalty forces used to model mechanical contact. We extend the proof of AVI multisymplecticity, showing that AVIs remain multisymplectic under relaxed assumptions on the type of potential. The extended theory thus accommodates the simulation of mechanical contact in elastica (such as thin shells) and multibody systems (such as granular materials) with no drift of conserved quantities (energy, momentum) over long run times, using the algorithms in [3]. We present data from a numerical experiment measuring the long time energy behavior of simulated contact, comparing the method built on multisymplectic integration of interaction potentials to recently proposed methods for thin shell contact.

## Content
Asynchronous Variational Integrators (AVIs) have demonstrated long-time good energy behavior. It was previously conjectured that this remarkable property is due to their geometric nature: they preserve a discrete multisymplectic form. Previous proofs of AVIs' multisymplecticity assume that the potentials are of an elastic type, i.e., specified by volume integration over the material domain, an assumption violated by interaction-type potentials, such as penalty forces used to model mechanical contact. We extend the proof of AVI multisymplecticity, showing that AVIs remain multisymplectic under relaxed assumptions on the type of potential. The extended theory thus accommodates the simulation of mechanical contact in elastica (such as thin shells) and multibody systems (such as granular materials) with no drift of conserved quantities (energy, momentum) over long run times, using the algorithms in [3]. We present data from a numerical experiment measuring the long time energy behavior of simulated contact, comparing the method built on multisymplectic integration of interaction potentials to recently proposed methods for thin shell contact.

## 개요
비동기 변분 적분기(AVI)는 장시간 동안 우수한 에너지 거동을 보여주었습니다. 이 놀라운 특성은 기하학적 성질, 즉 이산 다중 심플렉틱 형식을 보존하기 때문이라는 추측이 있었습니다. AVI의 다중 심플렉틱성에 대한 기존 증명은 퍼텐셜이 탄성 유형, 즉 재료 영역에 대한 부피 적분으로 지정된다고 가정하는데, 이는 기계적 접촉을 모델링하는 데 사용되는 페널티 힘과 같은 상호작용 유형 퍼텐셜에 의해 위반됩니다. 우리는 AVI 다중 심플렉틱성 증명을 확장하여 퍼텐셜 유형에 대한 완화된 가정 하에서도 AVI가 다중 심플렉틱성을 유지함을 보여줍니다. 따라서 확장된 이론은 [3]의 알고리즘을 사용하여 탄성체(예: 얇은 쉘) 및 다물체 시스템(예: 입상 재료)에서 기계적 접촉 시뮬레이션을 장시간 동안 보존량(에너지, 운동량)의 드리프트 없이 수용합니다. 우리는 시뮬레이션된 접촉의 장시간 에너지 거동을 측정한 수치 실험 데이터를 제시하며, 상호작용 퍼텐셜의 다중 심플렉틱 적분에 기반한 방법을 최근 제안된 얇은 쉘 접촉 방법과 비교합니다.

## 핵심 내용
비동기 변분 적분기(AVI)는 장시간 동안 우수한 에너지 거동을 보여주었습니다. 이 놀라운 특성은 기하학적 성질, 즉 이산 다중 심플렉틱 형식을 보존하기 때문이라는 추측이 있었습니다. AVI의 다중 심플렉틱성에 대한 기존 증명은 퍼텐셜이 탄성 유형, 즉 재료 영역에 대한 부피 적분으로 지정된다고 가정하는데, 이는 기계적 접촉을 모델링하는 데 사용되는 페널티 힘과 같은 상호작용 유형 퍼텐셜에 의해 위반됩니다. 우리는 AVI 다중 심플렉틱성 증명을 확장하여 퍼텐셜 유형에 대한 완화된 가정 하에서도 AVI가 다중 심플렉틱성을 유지함을 보여줍니다. 따라서 확장된 이론은 [3]의 알고리즘을 사용하여 탄성체(예: 얇은 쉘) 및 다물체 시스템(예: 입상 재료)에서 기계적 접촉 시뮬레이션을 장시간 동안 보존량(에너지, 운동량)의 드리프트 없이 수용합니다. 우리는 시뮬레이션된 접촉의 장시간 에너지 거동을 측정한 수치 실험 데이터를 제시하며, 상호작용 퍼텐셜의 다중 심플렉틱 적분에 기반한 방법을 최근 제안된 얇은 쉘 접촉 방법과 비교합니다.
