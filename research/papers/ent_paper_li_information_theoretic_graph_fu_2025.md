---
$id: ent_paper_li_information_theoretic_graph_fu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control
  zh: GF-VLA
  ko: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control
summary:
  en: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control (GF-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Alabama at Birmingham.
  zh: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control (GF-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Alabama at Birmingham.
  ko: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control (GF-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by University of Alabama at Birmingham.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gf_vla
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.05342v2.
sources:
- id: src_001
  type: paper
  title: Information-Theoretic Graph Fusion with Vision-Language-Action Model for Policy Reasoning and Dual Robotic Control
    (arXiv)
  url: https://arxiv.org/abs/2508.05342
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GF-VLA source
  url: https://doi.org/10.48550/arXiv.2508.05342
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Teaching robots dexterous skills from human videos remains challenging due to the reliance on low-level trajectory imitation, which fails to generalize across object types, spatial layouts, and manipulator configurations. We propose Graph-Fused Vision-Language-Action (GF-VLA), a framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB and Depth human demonstrations. GF-VLA first extracts Shannon-information-based cues to identify hands and objects with the highest task relevance, then encodes these cues into temporally ordered scene graphs that capture both hand-object and object-object interactions. These graphs are fused with a language-conditioned transformer that generates hierarchical behavior trees and interpretable Cartesian motion commands. To improve execution efficiency in bimanual settings, we further introduce a cross-hand selection policy that infers optimal gripper assignment without explicit geometric reasoning. We evaluate GF-VLA on four structured dual-arm block assembly tasks involving symbolic shape construction and spatial generalization. Experimental results show that the information-theoretic scene representation achieves over 95 percent graph accuracy and 93 percent subtask segmentation, supporting the LLM planner in generating reliable and human-readable task policies. When executed by the dual-arm robot, these policies yield 94 percent grasp success, 89 percent placement accuracy, and 90 percent overall task success across stacking, letter-building, and geometric reconfiguration scenarios, demonstrating strong generalization and robustness across diverse spatial and semantic variations.

## 核心内容
Teaching robots dexterous skills from human videos remains challenging due to the reliance on low-level trajectory imitation, which fails to generalize across object types, spatial layouts, and manipulator configurations. We propose Graph-Fused Vision-Language-Action (GF-VLA), a framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB and Depth human demonstrations. GF-VLA first extracts Shannon-information-based cues to identify hands and objects with the highest task relevance, then encodes these cues into temporally ordered scene graphs that capture both hand-object and object-object interactions. These graphs are fused with a language-conditioned transformer that generates hierarchical behavior trees and interpretable Cartesian motion commands. To improve execution efficiency in bimanual settings, we further introduce a cross-hand selection policy that infers optimal gripper assignment without explicit geometric reasoning. We evaluate GF-VLA on four structured dual-arm block assembly tasks involving symbolic shape construction and spatial generalization. Experimental results show that the information-theoretic scene representation achieves over 95 percent graph accuracy and 93 percent subtask segmentation, supporting the LLM planner in generating reliable and human-readable task policies. When executed by the dual-arm robot, these policies yield 94 percent grasp success, 89 percent placement accuracy, and 90 percent overall task success across stacking, letter-building, and geometric reconfiguration scenarios, demonstrating strong generalization and robustness across diverse spatial and semantic variations.

## 参考
- http://arxiv.org/abs/2508.05342v2

## Overview
Teaching robots dexterous skills from human videos remains challenging due to the reliance on low-level trajectory imitation, which fails to generalize across object types, spatial layouts, and manipulator configurations. We propose Graph-Fused Vision-Language-Action (GF-VLA), a framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB and Depth human demonstrations. GF-VLA first extracts Shannon-information-based cues to identify hands and objects with the highest task relevance, then encodes these cues into temporally ordered scene graphs that capture both hand-object and object-object interactions. These graphs are fused with a language-conditioned transformer that generates hierarchical behavior trees and interpretable Cartesian motion commands. To improve execution efficiency in bimanual settings, we further introduce a cross-hand selection policy that infers optimal gripper assignment without explicit geometric reasoning. We evaluate GF-VLA on four structured dual-arm block assembly tasks involving symbolic shape construction and spatial generalization. Experimental results show that the information-theoretic scene representation achieves over 95 percent graph accuracy and 93 percent subtask segmentation, supporting the LLM planner in generating reliable and human-readable task policies. When executed by the dual-arm robot, these policies yield 94 percent grasp success, 89 percent placement accuracy, and 90 percent overall task success across stacking, letter-building, and geometric reconfiguration scenarios, demonstrating strong generalization and robustness across diverse spatial and semantic variations.

## Content
Teaching robots dexterous skills from human videos remains challenging due to the reliance on low-level trajectory imitation, which fails to generalize across object types, spatial layouts, and manipulator configurations. We propose Graph-Fused Vision-Language-Action (GF-VLA), a framework that enables dual-arm robotic systems to perform task-level reasoning and execution directly from RGB and Depth human demonstrations. GF-VLA first extracts Shannon-information-based cues to identify hands and objects with the highest task relevance, then encodes these cues into temporally ordered scene graphs that capture both hand-object and object-object interactions. These graphs are fused with a language-conditioned transformer that generates hierarchical behavior trees and interpretable Cartesian motion commands. To improve execution efficiency in bimanual settings, we further introduce a cross-hand selection policy that infers optimal gripper assignment without explicit geometric reasoning. We evaluate GF-VLA on four structured dual-arm block assembly tasks involving symbolic shape construction and spatial generalization. Experimental results show that the information-theoretic scene representation achieves over 95 percent graph accuracy and 93 percent subtask segmentation, supporting the LLM planner in generating reliable and human-readable task policies. When executed by the dual-arm robot, these policies yield 94 percent grasp success, 89 percent placement accuracy, and 90 percent overall task success across stacking, letter-building, and geometric reconfiguration scenarios, demonstrating strong generalization and robustness across diverse spatial and semantic variations.

## 개요
인간의 비디오로부터 로봇에게 정교한 기술을 가르치는 것은 여전히 어려운 과제로 남아 있습니다. 이는 낮은 수준의 궤적 모방에 의존하기 때문에 객체 유형, 공간 배치 및 조작기 구성에 걸쳐 일반화되지 못하기 때문입니다. 본 논문에서는 Graph-Fused Vision-Language-Action (GF-VLA) 프레임워크를 제안합니다. 이 프레임워크는 이중 암 로봇 시스템이 RGB 및 Depth 인간 시연으로부터 직접 작업 수준의 추론과 실행을 수행할 수 있도록 합니다. GF-VLA는 먼저 Shannon 정보 기반 단서를 추출하여 가장 높은 작업 관련성을 가진 손과 객체를 식별한 후, 이러한 단서를 시간 순서대로 정렬된 장면 그래프로 인코딩하여 손-객체 및 객체-객체 상호작용을 모두 포착합니다. 이러한 그래프는 언어 조건부 트랜스포머와 융합되어 계층적 행동 트리와 해석 가능한 데카르트 운동 명령을 생성합니다. 양손 설정에서 실행 효율성을 높이기 위해, 명시적인 기하학적 추론 없이 최적의 그리퍼 할당을 추론하는 교차 손 선택 정책을 추가로 도입합니다. 우리는 GF-VLA를 기호적 형태 구성 및 공간 일반화를 포함하는 네 가지 구조화된 이중 암 블록 조립 작업에서 평가합니다. 실험 결과, 정보 이론적 장면 표현은 95% 이상의 그래프 정확도와 93%의 하위 작업 분할을 달성하여 LLM 플래너가 신뢰할 수 있고 사람이 읽을 수 있는 작업 정책을 생성하도록 지원합니다. 이중 암 로봇이 실행할 때, 이러한 정책은 쌓기, 문자 만들기 및 기하학적 재구성 시나리오에서 94%의 잡기 성공률, 89%의 배치 정확도 및 90%의 전체 작업 성공률을 보여주며, 다양한 공간적 및 의미적 변형에 걸쳐 강력한 일반화와 견고성을 입증합니다.

## 핵심 내용
인간의 비디오로부터 로봇에게 정교한 기술을 가르치는 것은 여전히 어려운 과제로 남아 있습니다. 이는 낮은 수준의 궤적 모방에 의존하기 때문에 객체 유형, 공간 배치 및 조작기 구성에 걸쳐 일반화되지 못하기 때문입니다. 본 논문에서는 Graph-Fused Vision-Language-Action (GF-VLA) 프레임워크를 제안합니다. 이 프레임워크는 이중 암 로봇 시스템이 RGB 및 Depth 인간 시연으로부터 직접 작업 수준의 추론과 실행을 수행할 수 있도록 합니다. GF-VLA는 먼저 Shannon 정보 기반 단서를 추출하여 가장 높은 작업 관련성을 가진 손과 객체를 식별한 후, 이러한 단서를 시간 순서대로 정렬된 장면 그래프로 인코딩하여 손-객체 및 객체-객체 상호작용을 모두 포착합니다. 이러한 그래프는 언어 조건부 트랜스포머와 융합되어 계층적 행동 트리와 해석 가능한 데카르트 운동 명령을 생성합니다. 양손 설정에서 실행 효율성을 높이기 위해, 명시적인 기하학적 추론 없이 최적의 그리퍼 할당을 추론하는 교차 손 선택 정책을 추가로 도입합니다. 우리는 GF-VLA를 기호적 형태 구성 및 공간 일반화를 포함하는 네 가지 구조화된 이중 암 블록 조립 작업에서 평가합니다. 실험 결과, 정보 이론적 장면 표현은 95% 이상의 그래프 정확도와 93%의 하위 작업 분할을 달성하여 LLM 플래너가 신뢰할 수 있고 사람이 읽을 수 있는 작업 정책을 생성하도록 지원합니다. 이중 암 로봇이 실행할 때, 이러한 정책은 쌓기, 문자 만들기 및 기하학적 재구성 시나리오에서 94%의 잡기 성공률, 89%의 배치 정확도 및 90%의 전체 작업 성공률을 보여주며, 다양한 공간적 및 의미적 변형에 걸쳐 강력한 일반화와 견고성을 입증합니다.
