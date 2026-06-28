---
$id: ent_paper_correll_materials_that_make_robots_sma_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Materials that make robots smart
  zh: 使机器人智能化的材料
  ko: 로봇을 스마트하게 만드는 재료
summary:
  en: This paper argues that embodied artificial intelligence is also a materials
    problem, defines "robotic materials" as composites that tightly integrate structure,
    sensing, actuation, computation, and communication, surveys existing prototypes,
    and identifies interdisciplinary challenges in manufacturing, networking, materials
    science, and control.
  zh: 本文提出具身人工智能也是一个材料问题，将“机器人材料”定义为紧密集成结构、传感、驱动、计算和通信的复合材料，综述了现有原型，并指出了制造、网络、材料科学和控制领域的跨学科挑战。
  ko: 본 논문은 구체화된 인공지능 역시 재료 문제이며, 구조, 센싱, 구동, 계산, 통신을 긴밀히 통합한 복합 재료인 “로봇 재료”를 정의하고,
    기존 프로토타입을 조사하며 제조, 네트워킹, 재료 과학 및 제어 분야의 학제간 과제를 제시한다.
domains:
- 02_components
- 01_raw_materials
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- robotic_materials
- smart_materials
- tactile_sensing_skin
- morphological_computation
- humanoid_skin
- multi_material_manufacturing
- wireless_sensor_networks
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the provided abstract and metadata; full-text verification
    is needed before marking as verified.
sources:
- id: src_001
  type: paper
  title: Materials that make robots smart
  url: https://arxiv.org/abs/1711.00537
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- principle
- method
---

## Overview

Correll and Heckman argue that embodied artificial intelligence is not only a computational problem but also a materials problem. They define "robotic materials" as composite systems that combine structural, sensing, actuation, and computational phases into a single material, enabling functionality to be abstracted away from the central controller. This integration is inspired by biological tissues, where heterogeneous components such as bone, muscle, skin, and neural tissue are tightly co-located and cooperate to produce robust behavior.

The authors survey existing prototypes that illustrate the concept, including camouflage skins, texture-sensing skin, shape-changing beams, gesture-detecting skin, smart fabrics, and interactive facades. They distinguish between perceptual robotic materials, which primarily embed sensing and computation, and actuating robotic materials, which also include active actuation. The survey is used to argue that embedding sensing and computation into materials can offload central processing and simplify robot design through morphological computation.

Finally, the paper identifies the interdisciplinary challenges that must be overcome for robotic materials to become practical. These include wireless power and communication, multi-material manufacturing across length scales, advances in polymer science, and the integration of expertise from robotics, wireless sensor networks, materials science, and chemistry.

## Key Contributions

- Formalizes the properties that define robotic materials: functionality independent of size, self-similarity or bulk reconfigurability, and robustness to element failure.
- Surveys state-of-the-art robotic material prototypes including camouflage skins, texture-sensing skin, shape-changing beams, gesture-detecting skin, smart fabrics, and interactive facades.
- Argues that embedding sensing and computation into materials can offload central processing and simplify robot design via morphological computation.
- Identifies key enabling technologies and open challenges: wireless power and communication, multi-material manufacturing across length scales, polymer science, and interdisciplinary system integration.
- Suggests that perceptual robotic materials are nearer-term than actuating materials.

## Relevance to Humanoid Robotics

Robotic materials are directly relevant to humanoid robotics because they could provide scalable, self-contained tactile skin, load-sensing structural bones, and muscle-like actuators. By abstracting low-level sensing and control into the material itself, humanoid robots could become easier to mass produce and more robust to deploy in unstructured environments. The paper explicitly frames this vision in terms of bones that measure load, muscles that move, skin that reports tactile sensations, eyes that extract high-level information, and brain-like material that provides scalable computation.
