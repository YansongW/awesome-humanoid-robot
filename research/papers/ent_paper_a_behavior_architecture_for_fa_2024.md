---
$id: ent_paper_a_behavior_architecture_for_fa_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Behavior Architecture for Fast Humanoid Robot Door Traversals
  zh: A Behavior Architecture for Fast Humanoid Robot Door Traversals
  ko: A Behavior Architecture for Fast Humanoid Robot Door Traversals
summary:
  en: A Behavior Architecture for Fast Humanoid Robot Door Traversals is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  zh: A Behavior Architecture for Fast Humanoid Robot Door Traversals is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
  ko: A Behavior Architecture for Fast Humanoid Robot Door Traversals is a 2024 work on loco-manipulation and whole-body-control
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a_behavior_architecture_for_fa
- humanoid
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.03532v1.
sources:
- id: src_001
  type: paper
  title: A Behavior Architecture for Fast Humanoid Robot Door Traversals (arXiv)
  url: https://arxiv.org/abs/2411.03532
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: A Behavior Architecture for Fast Humanoid Robot Door Traversals project page
  url: https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Towards the role of humanoid robots as squad mates in urban operations and other domains, we identified doors as a major area lacking capability development. In this paper, we focus on the ability of humanoid robots to navigate and deal with doors. Human-sized doors are ubiquitous in many environment domains and the humanoid form factor is uniquely suited to operate and traverse them. We present an architecture which incorporates GPU accelerated perception and a tree based interactive behavior coordination system with a whole body motion and walking controller. Our system is capable of performing door traversals on a variety of door types. It supports rapid authoring of behaviors for unseen door types and techniques to achieve re-usability of those authored behaviors. The behaviors are modelled using trees and feature logical reactivity and action sequences that can be executed with layered concurrency to increase speed. Primitive actions are built on top of our existing whole body controller which supports manipulation while walking. We include a perception system using both neural networks and classical computer vision for door mechanism detection outside of the lab environment. We present operator-robot interdependence analysis charts to explore how human cognition is combined with artificial intelligence to produce complex robot behavior. Finally, we present and discuss real robot performances of fast door traversals on our Nadia humanoid robot. Videos online at https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy.

## 核心内容
Towards the role of humanoid robots as squad mates in urban operations and other domains, we identified doors as a major area lacking capability development. In this paper, we focus on the ability of humanoid robots to navigate and deal with doors. Human-sized doors are ubiquitous in many environment domains and the humanoid form factor is uniquely suited to operate and traverse them. We present an architecture which incorporates GPU accelerated perception and a tree based interactive behavior coordination system with a whole body motion and walking controller. Our system is capable of performing door traversals on a variety of door types. It supports rapid authoring of behaviors for unseen door types and techniques to achieve re-usability of those authored behaviors. The behaviors are modelled using trees and feature logical reactivity and action sequences that can be executed with layered concurrency to increase speed. Primitive actions are built on top of our existing whole body controller which supports manipulation while walking. We include a perception system using both neural networks and classical computer vision for door mechanism detection outside of the lab environment. We present operator-robot interdependence analysis charts to explore how human cognition is combined with artificial intelligence to produce complex robot behavior. Finally, we present and discuss real robot performances of fast door traversals on our Nadia humanoid robot. Videos online at https://www.youtube.com/playlist?list=PLXuyT8w3JVgMPaB5nWNRNHtqzRK8i68dy.

## 参考
- http://arxiv.org/abs/2411.03532v1

