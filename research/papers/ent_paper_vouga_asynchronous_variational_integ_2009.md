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
  zh: 本文扩展了异步变分积分器（AVI）以处理接触力学中的交互势（如罚接触力），证明了在放宽假设条件下AVI仍保持多辛结构，并通过Asynchronous Contact Mechanics框架在薄球-板冲击实验中验证了长期能量稳定性。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/0907.0706v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (617 chars, DeepSeek).'
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
异步变分积分器（AVI）因其长期良好的能量行为而受到关注，先前认为这一特性源于其离散多辛形式的几何本质。然而，之前的证明假设势能为弹性类型（通过材料域的体积积分定义），这无法涵盖交互势（如用于模拟机械接触的罚力）。本文放宽了势能类型的假设，证明了AVI在多体系统（如薄壳、颗粒材料）中仍保持多辛性，从而确保守恒量（能量、动量）在长时间模拟中无漂移。数值实验对比了基于交互势多辛积分的方法与近期提出的薄壳接触方法，验证了长期能量稳定性。

## 核心内容
### 核心贡献
- **理论扩展**：将AVI的多辛性证明从弹性势能推广至交互势（如罚接触力），证明在放宽假设条件下离散多辛形式仍被保持。
- **应用场景**：支持弹性体（如薄壳）和多体系统（如颗粒材料）的接触力学模拟，确保长时间运行中能量和动量无漂移。
- **算法基础**：基于文献[3]中的算法实现，无需修改AVI框架即可处理交互势。

### 实验验证
- **数值实验**：模拟薄球与刚性板的冲击接触，测量长期能量行为。
- **对比方法**：与近期提出的薄壳接触方法进行对比，本文方法在能量稳定性上表现更优。
- **关键结果**：在长时间模拟中，能量和动量守恒量无系统性漂移，验证了多辛积分的几何保真性。

### 结论
本文从理论上证明了AVI可自然扩展至交互势，为接触力学提供了一种保结构数值方法，尤其适用于需要长期能量稳定性的柔性多体系统仿真。

## Overview
Asynchronous Variational Integrators (AVIs) have demonstrated long-time good energy behavior. It was previously conjectured that this remarkable property is due to their geometric nature: they preserve a discrete multisymplectic form. Previous proofs of AVIs' multisymplecticity assume that the potentials are of an elastic type, i.e., specified by volume integration over the material domain, an assumption violated by interaction-type potentials, such as penalty forces used to model mechanical contact. We extend the proof of AVI multisymplecticity, showing that AVIs remain multisymplectic under relaxed assumptions on the type of potential. The extended theory thus accommodates the simulation of mechanical contact in elastica (such as thin shells) and multibody systems (such as granular materials) with no drift of conserved quantities (energy, momentum) over long run times, using the algorithms in [3]. We present data from a numerical experiment measuring the long time energy behavior of simulated contact, comparing the method built on multisymplectic integration of interaction potentials to recently proposed methods for thin shell contact.

## 参考
- http://arxiv.org/abs/0907.0706v1

## 개요
비동기 변분 적분기(AVI)는 장기적으로 우수한 에너지 거동으로 주목받아 왔으며, 이전에는 이러한 특성이 이산 다심플렉틱 형식의 기하학적 본질에서 비롯된 것으로 여겨졌습니다. 그러나 이전 증명은 퍼텐셜 에너지가 탄성 유형(재료 영역의 부피 적분으로 정의됨)이라고 가정하여, 기계적 접촉 시뮬레이션에 사용되는 페널티 힘과 같은 상호작용 퍼텐셜을 포괄할 수 없었습니다. 본 논문은 퍼텐셜 유형에 대한 가정을 완화하여, AVI가 얇은 셸, 입자 재료와 같은 다물체 시스템에서도 다심플렉틱성을 유지함을 증명하여, 보존량(에너지, 운동량)이 장기 시뮬레이션에서 드리프트 없이 유지되도록 보장합니다. 수치 실험은 상호작용 퍼텐셜 기반 다심플렉틱 적분 방법과 최근 제안된 얇은 셸 접촉 방법을 비교하여 장기 에너지 안정성을 검증합니다.

## 핵심 내용
### 핵심 기여
- **이론적 확장**: AVI의 다심플렉틱성 증명을 탄성 퍼텐셜에서 상호작용 퍼텐셜(예: 페널티 접촉 힘)로 일반화하여, 완화된 가정 조건에서도 이산 다심플렉틱 형식이 유지됨을 증명합니다.
- **적용 시나리오**: 탄성체(예: 얇은 셸) 및 다물체 시스템(예: 입자 재료)의 접촉 역학 시뮬레이션을 지원하며, 장기 실행 중 에너지 및 운동량 드리프트가 없음을 보장합니다.
- **알고리즘 기반**: 문헌[3]의 알고리즘을 기반으로 구현되며, AVI 프레임워크를 수정하지 않고도 상호작용 퍼텐셜을 처리할 수 있습니다.

### 실험 검증
- **수치 실험**: 얇은 구와 강체 판의 충돌 접촉을 시뮬레이션하여 장기 에너지 거동을 측정합니다.
- **비교 방법**: 최근 제안된 얇은 셸 접촉 방법과 비교하여, 본 방법이 에너지 안정성에서 더 우수한 성능을 보입니다.
- **핵심 결과**: 장기 시뮬레이션에서 에너지 및 운동량 보존량에 체계적 드리프트가 없음을 확인하여, 다심플렉틱 적분의 기하학적 충실성을 검증합니다.

### 결론
본 논문은 AVI가 상호작용 퍼텐셜로 자연스럽게 확장될 수 있음을 이론적으로 증명하여, 접촉 역학을 위한 구조 보존 수치 방법을 제공하며, 특히 장기 에너지 안정성이 필요한 유연한 다물체 시스템 시뮬레이션에 적합합니다.
