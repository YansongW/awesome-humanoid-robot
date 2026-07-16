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
  en: A review that presents a unified reductive framework deriving continuum electrochemical battery models from a high-fidelity
    microscale model down to the Single Particle Model, with critical discussion of assumptions, limitations, and coupled
    thermal extensions.
  zh: Physics-based electrochemical battery models derived from porous electrode theory are a very powerful tool for understanding
    lithium-ion batteries, as well as for improving their design and management. Different model fidelity, and thus model
    complexity, is needed for different applications. For example, in battery design we can afford longer computational times
    and the use of powerful computers, while for real-time battery control (e.g. in electric vehicles) we need to perform
    very fast calculations using simple devices. For this reason, simplified models that retain most of the features at a
  ko: 고충실도 미시규모 모델에서 단일 입자 모델까지의 연속 전기화학 배터리 모델을 유도하는 통합적 환원 프레임워크를 제시하고, 가정들과 한계, 열-전기화학 결합 확장에 대해 비판적으로 논의한 리뷰이다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.16091v1.
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

## 概述
Physics-based electrochemical battery models derived from porous electrode theory are a very powerful tool for understanding lithium-ion batteries, as well as for improving their design and management. Different model fidelity, and thus model complexity, is needed for different applications. For example, in battery design we can afford longer computational times and the use of powerful computers, while for real-time battery control (e.g. in electric vehicles) we need to perform very fast calculations using simple devices. For this reason, simplified models that retain most of the features at a lower computational cost are widely used. Even though in the literature we often find these simplified models posed independently, leading to inconsistencies between models, they can actually be derived from more complicated models using a unified and systematic framework. In this review, we showcase this reductive framework, starting from a high-fidelity microscale model and reducing it all the way down to the Single Particle Model (SPM), deriving in the process other common models, such as the Doyle-Fuller-Newman (DFN) model. We also provide a critical discussion on the advantages and shortcomings of each of the models, which can aid model selection for a particular application. Finally, we provide an overview of possible extensions to the models, with a special focus on thermal models. Any of these extensions could be incorporated into the microscale model and the reductive framework re-applied to lead to a new generation of simplified, multi-physics models.

## 核心内容
Physics-based electrochemical battery models derived from porous electrode theory are a very powerful tool for understanding lithium-ion batteries, as well as for improving their design and management. Different model fidelity, and thus model complexity, is needed for different applications. For example, in battery design we can afford longer computational times and the use of powerful computers, while for real-time battery control (e.g. in electric vehicles) we need to perform very fast calculations using simple devices. For this reason, simplified models that retain most of the features at a lower computational cost are widely used. Even though in the literature we often find these simplified models posed independently, leading to inconsistencies between models, they can actually be derived from more complicated models using a unified and systematic framework. In this review, we showcase this reductive framework, starting from a high-fidelity microscale model and reducing it all the way down to the Single Particle Model (SPM), deriving in the process other common models, such as the Doyle-Fuller-Newman (DFN) model. We also provide a critical discussion on the advantages and shortcomings of each of the models, which can aid model selection for a particular application. Finally, we provide an overview of possible extensions to the models, with a special focus on thermal models. Any of these extensions could be incorporated into the microscale model and the reductive framework re-applied to lead to a new generation of simplified, multi-physics models.

## 参考
- http://arxiv.org/abs/2203.16091v1

## Overview
Physics-based electrochemical battery models derived from porous electrode theory are a very powerful tool for understanding lithium-ion batteries, as well as for improving their design and management. Different model fidelity, and thus model complexity, is needed for different applications. For example, in battery design we can afford longer computational times and the use of powerful computers, while for real-time battery control (e.g. in electric vehicles) we need to perform very fast calculations using simple devices. For this reason, simplified models that retain most of the features at a lower computational cost are widely used. Even though in the literature we often find these simplified models posed independently, leading to inconsistencies between models, they can actually be derived from more complicated models using a unified and systematic framework. In this review, we showcase this reductive framework, starting from a high-fidelity microscale model and reducing it all the way down to the Single Particle Model (SPM), deriving in the process other common models, such as the Doyle-Fuller-Newman (DFN) model. We also provide a critical discussion on the advantages and shortcomings of each of the models, which can aid model selection for a particular application. Finally, we provide an overview of possible extensions to the models, with a special focus on thermal models. Any of these extensions could be incorporated into the microscale model and the reductive framework re-applied to lead to a new generation of simplified, multi-physics models.

## Content
Physics-based electrochemical battery models derived from porous electrode theory are a very powerful tool for understanding lithium-ion batteries, as well as for improving their design and management. Different model fidelity, and thus model complexity, is needed for different applications. For example, in battery design we can afford longer computational times and the use of powerful computers, while for real-time battery control (e.g. in electric vehicles) we need to perform very fast calculations using simple devices. For this reason, simplified models that retain most of the features at a lower computational cost are widely used. Even though in the literature we often find these simplified models posed independently, leading to inconsistencies between models, they can actually be derived from more complicated models using a unified and systematic framework. In this review, we showcase this reductive framework, starting from a high-fidelity microscale model and reducing it all the way down to the Single Particle Model (SPM), deriving in the process other common models, such as the Doyle-Fuller-Newman (DFN) model. We also provide a critical discussion on the advantages and shortcomings of each of the models, which can aid model selection for a particular application. Finally, we provide an overview of possible extensions to the models, with a special focus on thermal models. Any of these extensions could be incorporated into the microscale model and the reductive framework re-applied to lead to a new generation of simplified, multi-physics models.

## 개요
다공성 전극 이론에서 도출된 물리 기반 전기화학 배터리 모델은 리튬이온 배터리를 이해하고 설계 및 관리를 개선하는 데 매우 강력한 도구입니다. 다양한 응용 분야에 따라 서로 다른 모델 정밀도, 즉 모델 복잡성이 필요합니다. 예를 들어, 배터리 설계에서는 더 긴 계산 시간과 강력한 컴퓨터 사용이 가능하지만, 실시간 배터리 제어(예: 전기 자동차)에서는 간단한 장치를 사용하여 매우 빠른 계산을 수행해야 합니다. 이러한 이유로 대부분의 특징을 유지하면서 낮은 계산 비용을 제공하는 단순화된 모델이 널리 사용됩니다. 문헌에서 이러한 단순화된 모델이 독립적으로 제시되어 모델 간 불일치를 초래하는 경우가 많지만, 실제로는 통일되고 체계적인 프레임워크를 사용하여 더 복잡한 모델에서 도출될 수 있습니다. 본 리뷰에서는 고정밀 미세 규모 모델에서 시작하여 단일 입자 모델(SPM)까지 축소하는 이 축소 프레임워크를 소개하고, 그 과정에서 Doyle-Fuller-Newman(DFN) 모델과 같은 다른 일반적인 모델을 도출합니다. 또한 각 모델의 장점과 단점에 대한 비판적 논의를 제공하여 특정 응용 분야에 대한 모델 선택을 지원합니다. 마지막으로, 특히 열 모델에 중점을 두고 모델의 가능한 확장에 대한 개요를 제공합니다. 이러한 확장 중 어느 것이든 미세 규모 모델에 통합될 수 있으며, 축소 프레임워크를 재적용하여 새로운 세대의 단순화된 다중 물리 모델을 도출할 수 있습니다.

## 핵심 내용
다공성 전극 이론에서 도출된 물리 기반 전기화학 배터리 모델은 리튬이온 배터리를 이해하고 설계 및 관리를 개선하는 데 매우 강력한 도구입니다. 다양한 응용 분야에 따라 서로 다른 모델 정밀도, 즉 모델 복잡성이 필요합니다. 예를 들어, 배터리 설계에서는 더 긴 계산 시간과 강력한 컴퓨터 사용이 가능하지만, 실시간 배터리 제어(예: 전기 자동차)에서는 간단한 장치를 사용하여 매우 빠른 계산을 수행해야 합니다. 이러한 이유로 대부분의 특징을 유지하면서 낮은 계산 비용을 제공하는 단순화된 모델이 널리 사용됩니다. 문헌에서 이러한 단순화된 모델이 독립적으로 제시되어 모델 간 불일치를 초래하는 경우가 많지만, 실제로는 통일되고 체계적인 프레임워크를 사용하여 더 복잡한 모델에서 도출될 수 있습니다. 본 리뷰에서는 고정밀 미세 규모 모델에서 시작하여 단일 입자 모델(SPM)까지 축소하는 이 축소 프레임워크를 소개하고, 그 과정에서 Doyle-Fuller-Newman(DFN) 모델과 같은 다른 일반적인 모델을 도출합니다. 또한 각 모델의 장점과 단점에 대한 비판적 논의를 제공하여 특정 응용 분야에 대한 모델 선택을 지원합니다. 마지막으로, 특히 열 모델에 중점을 두고 모델의 가능한 확장에 대한 개요를 제공합니다. 이러한 확장 중 어느 것이든 미세 규모 모델에 통합될 수 있으며, 축소 프레임워크를 재적용하여 새로운 세대의 단순화된 다중 물리 모델을 도출할 수 있습니다.
