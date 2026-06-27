---
$id: ent_paper_garg_semantics_for_robotic_mapping_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Semantics for Robotic Mapping, Perception and Interaction: A Survey'
  zh: 机器人建图、感知与交互中的语义研究综述
  ko: '로봇 매핑, 인식 및 상호작용을 위한 의미론: 서베이'
summary:
  en: A 2020 survey that proposes a four-category taxonomy for semantics research
    in robotics and reviews more than 900 works spanning computer-vision fundamentals,
    semantic mapping, navigation, human-robot interaction, and deployment enablers.
  zh: 2020年发表的一篇综述，提出了机器人语义研究的四类别分类法，并调研了900多篇相关文献，涵盖计算机视觉基础、语义建图、导航、人机交互以及实际部署使能技术。
  ko: 2020년에 발표된 서베이로, 로봇 공학에서 의미론 연구를 위한 네 가지 범주 분류법을 제안하고 컴퓨터 비전 기초, 의미론적 매핑, 내비게이션,
    인간-로봇 상호작용, 실제 배포 가능성 기술을 포함하여 900개 이상의 관련 연구를 조사한다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- semantic_mapping
- perception
- human_robot_interaction
- scene_understanding
- semantic_slam
- object_detection
- affordance
- survey
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    is required before promotion.
sources:
- id: src_001
  type: paper
  title: 'Semantics for Robotic Mapping, Perception and Interaction: A Survey'
  url: https://arxiv.org/abs/2101.00443
  date: '2020'
  accessed_at: '2026-06-27'
  doi: 10.1561/2300000059
theoretical_depth:
- method
---

## Overview

This paper provides a broad survey of semantics research in robotics. It proposes a four-category taxonomy—static/un-embodied scene understanding, dynamic environment understanding and mapping, interacting with humans and the world, and improving task capability—and uses it to organize over 900 cited works. The survey connects computer-vision fundamentals such as classification, detection, and segmentation with robotics topics including semantic SLAM, navigation, object affordances, grasping, manipulation, and human-robot interaction. It also examines practical enablers such as large-scale datasets, cloud computing, GPUs, FPGAs, and neuromorphic sensors, and discusses major application domains where semantic understanding is expected to play a central role.

The authors position their work as a unifying reference that complements prior, more narrowly focused surveys. Rather than treating semantics as a single problem, they trace how semantic information is extracted from sensory data and then used to improve robotic mapping, perception, planning, and interaction. The survey is intended to help researchers across academia and industry identify connections between subfields and find promising directions for future work.

The paper further notes that the rapid growth of deep learning, the increasing availability of annotated data, and advances in computational hardware have accelerated progress in semantic robotics. At the same time, it highlights remaining challenges such as robustness in unstructured environments, integration across modalities, and the gap between visual semantics and richer forms of robot-world meaning.

## Key Contributions

- Proposes a unified four-category taxonomy for semantics research spanning both extraction and use of semantic information in robotics.
- Surveys computer-vision fundamentals and robotics topics including semantic SLAM, segmentation, object detection, and human-robot interaction.
- Covers practical deployment considerations and technology enablers such as datasets, cloud compute, GPUs, FPGAs, and hardware accelerators.
- Provides a comprehensive reference consolidating more than 900 cited works.
- Identifies remaining challenges and future research directions for semantics in robotics.

## Relevance to Humanoid Robotics

Humanoid robots operating in human-centered environments must interpret scenes, recognize objects and their affordances, navigate safely, and interact naturally with people. This survey maps the core perceptual and cognitive capabilities required for such deployments, including semantic mapping, object detection, affordance reasoning, grasping and manipulation, and human-robot interaction. Because it links these capabilities to underlying computer-vision methods and enabling technologies, it serves as a valuable roadmap for humanoid-robot development. Its emphasis on unstructured, real-world settings aligns with the long-term goal of deploying humanoid robots at scale in homes, workplaces, and public spaces.
