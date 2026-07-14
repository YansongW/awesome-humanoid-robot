---
$id: ent_paper_anchorvla_bridging_discrete_de_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action
    Planning'
  zh: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action
    Planning'
  ko: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action
    Planning'
summary:
  en: "arXiv:2607.03182v1 Announce Type: new \nAbstract: Autonomous driving planning\
    \ requires translating navigation intent, traffic rules, dynamic interactions,\
    \ and language instructions into executable continuous trajectories. Vision-Language-Action\
    \ models have been introduced into driving planning to improve long-tail generalization,\
    \ commonsense reasoning, high-level semantic understanding, and explainability.\
    \ However, existing VLA planners mainly follow planning-head-based trajectory\
    \ prediction or full-trajectory autoregressive generation. The former only weakly\
    \ constrains continuous trajectory generation with VLA reasoning, while the latter\
    \ relies on long sequences of low-information-density coordinate tokens, making\
    \ semantic-action alignment difficult and leading to discretization errors and\
    \ inefficient inference. To address these limitations, we propose AnchorVLA, a\
    \ hierarchical decision-anchored VLA planning framework that uses trajectory-pattern\
    \ anchors as an explicit interface between high-level VLA reasoning and continuous\
    \ trajectory execution. Specifically, Decision-as-Anchor Representation represents\
    \ behavior-level driving decisions with anchor tokens, each encoding an entire\
    \ local motion pattern rather than a single coordinate point. Decision-Anchored\
    \ Residual Flow then generates fine-grained continuous trajectories in the selected\
    \ anchor-defined residual space, capturing multi-modal execution refinements after\
    \ high-level decision making. By reasoning over compact and semantically meaningful\
    \ anchors instead of autoregressively generating waypoint sequences, AnchorVLA\
    \ preserves LLM-based decision making while improving inference efficiency, semantic-action\
    \ alignment, and continuous generation flexibility. Experiments on the Bench2Drive\
    \ closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success\
    \ Rate of 77.28 and a competitive Driving Score of 89.92."
  zh: "arXiv:2607.03182v1 Announce Type: new \nAbstract: Autonomous driving planning\
    \ requires translating navigation intent, traffic rules, dynamic interactions,\
    \ and language instructions into executable continuous trajectories. Vision-Language-Action\
    \ models have been introduced into driving planning to improve long-tail generalization,\
    \ commonsense reasoning, high-level semantic understanding, and explainability.\
    \ However, existing VLA planners mainly follow planning-head-based trajectory\
    \ prediction or full-trajectory autoregressive generation. The former only weakly\
    \ constrains continuous trajectory generation with VLA reasoning, while the latter\
    \ relies on long sequences of low-information-density coordinate tokens, making\
    \ semantic-action alignment difficult and leading to discretization errors and\
    \ inefficient inference. To address these limitations, we propose AnchorVLA, a\
    \ hierarchical decision-anchored VLA planning framework that uses trajectory-pattern\
    \ anchors as an explicit interface between high-level VLA reasoning and continuous\
    \ trajectory execution. Specifically, Decision-as-Anchor Representation represents\
    \ behavior-level driving decisions with anchor tokens, each encoding an entire\
    \ local motion pattern rather than a single coordinate point. Decision-Anchored\
    \ Residual Flow then generates fine-grained continuous trajectories in the selected\
    \ anchor-defined residual space, capturing multi-modal execution refinements after\
    \ high-level decision making. By reasoning over compact and semantically meaningful\
    \ anchors instead of autoregressively generating waypoint sequences, AnchorVLA\
    \ preserves LLM-based decision making while improving inference efficiency, semantic-action\
    \ alignment, and continuous generation flexibility. Experiments on the Bench2Drive\
    \ closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success\
    \ Rate of 77.28 and a competitive Driving Score of 89.92."
  ko: "arXiv:2607.03182v1 Announce Type: new \nAbstract: Autonomous driving planning\
    \ requires translating navigation intent, traffic rules, dynamic interactions,\
    \ and language instructions into executable continuous trajectories. Vision-Language-Action\
    \ models have been introduced into driving planning to improve long-tail generalization,\
    \ commonsense reasoning, high-level semantic understanding, and explainability.\
    \ However, existing VLA planners mainly follow planning-head-based trajectory\
    \ prediction or full-trajectory autoregressive generation. The former only weakly\
    \ constrains continuous trajectory generation with VLA reasoning, while the latter\
    \ relies on long sequences of low-information-density coordinate tokens, making\
    \ semantic-action alignment difficult and leading to discretization errors and\
    \ inefficient inference. To address these limitations, we propose AnchorVLA, a\
    \ hierarchical decision-anchored VLA planning framework that uses trajectory-pattern\
    \ anchors as an explicit interface between high-level VLA reasoning and continuous\
    \ trajectory execution. Specifically, Decision-as-Anchor Representation represents\
    \ behavior-level driving decisions with anchor tokens, each encoding an entire\
    \ local motion pattern rather than a single coordinate point. Decision-Anchored\
    \ Residual Flow then generates fine-grained continuous trajectories in the selected\
    \ anchor-defined residual space, capturing multi-modal execution refinements after\
    \ high-level decision making. By reasoning over compact and semantically meaningful\
    \ anchors instead of autoregressively generating waypoint sequences, AnchorVLA\
    \ preserves LLM-based decision making while improving inference efficiency, semantic-action\
    \ alignment, and continuous generation flexibility. Experiments on the Bench2Drive\
    \ closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success\
    \ Rate of 77.28 and a competitive Driving Score of 89.92."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- anchorvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action
    Planning (arXiv)'
  url: https://arxiv.org/abs/2607.03182
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2607.03182v1 Announce Type: new 
Abstract: Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## Overview
arXiv:2607.03182v1 Announce Type: new 
Abstract: Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.

## 개요
arXiv:2607.03182v1 Announce Type: new 
Abstract: Autonomous driving planning requires translating navigation intent, traffic rules, dynamic interactions, and language instructions into executable continuous trajectories. Vision-Language-Action models have been introduced into driving planning to improve long-tail generalization, commonsense reasoning, high-level semantic understanding, and explainability. However, existing VLA planners mainly follow planning-head-based trajectory prediction or full-trajectory autoregressive generation. The former only weakly constrains continuous trajectory generation with VLA reasoning, while the latter relies on long sequences of low-information-density coordinate tokens, making semantic-action alignment difficult and leading to discretization errors and inefficient inference. To address these limitations, we propose AnchorVLA, a hierarchical decision-anchored VLA planning framework that uses trajectory-pattern anchors as an explicit interface between high-level VLA reasoning and continuous trajectory execution. Specifically, Decision-as-Anchor Representation represents behavior-level driving decisions with anchor tokens, each encoding an entire local motion pattern rather than a single coordinate point. Decision-Anchored Residual Flow then generates fine-grained continuous trajectories in the selected anchor-defined residual space, capturing multi-modal execution refinements after high-level decision making. By reasoning over compact and semantically meaningful anchors instead of autoregressively generating waypoint sequences, AnchorVLA preserves LLM-based decision making while improving inference efficiency, semantic-action alignment, and continuous generation flexibility. Experiments on the Bench2Drive closed-loop benchmark show that AnchorVLA achieves a state-of-the-art Success Rate of 77.28 and a competitive Driving Score of 89.92.
