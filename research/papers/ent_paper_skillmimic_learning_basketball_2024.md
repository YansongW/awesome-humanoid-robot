---
$id: ent_paper_skillmimic_learning_basketball_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
  zh: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
  ko: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations'
summary:
  en: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
  zh: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
  ko: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations is a 2024 work on physics-based character animation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- skillmimic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2408.15270v2.
sources:
- id: src_001
  type: paper
  title: 'SkillMimic: Learning Basketball Interaction Skills from Demonstrations (arXiv)'
  url: https://arxiv.org/abs/2408.15270
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## 核心内容
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## 参考
- http://arxiv.org/abs/2408.15270v2

## Overview
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## Content
Traditional reinforcement learning methods for human-object interaction (HOI) rely on labor-intensive, manually designed skill rewards that do not generalize well across different interactions. We introduce SkillMimic, a unified data-driven framework that fundamentally changes how agents learn interaction skills by eliminating the need for skill-specific rewards. Our key insight is that a unified HOI imitation reward can effectively capture the essence of diverse interaction patterns from HOI datasets. This enables SkillMimic to learn a single policy that not only masters multiple interaction skills but also facilitates skill transitions, with both diversity and generalization improving as the HOI dataset grows. For evaluation, we collect and introduce two basketball datasets containing approximately 35 minutes of diverse basketball skills. Extensive experiments show that SkillMimic successfully masters a wide range of basketball skills including stylistic variations in dribbling, layup, and shooting. Moreover, these learned skills can be effectively composed by a high-level controller to accomplish complex and long-horizon tasks such as consecutive scoring, opening new possibilities for scalable and generalizable interaction skill learning. Project page: https://ingrid789.github.io/SkillMimic/

## 개요
인간-객체 상호작용(HOI)을 위한 전통적인 강화 학습 방법은 노동 집약적이고 수동으로 설계된 기술 보상에 의존하며, 이는 다양한 상호작용 간에 잘 일반화되지 않습니다. 우리는 SkillMimic을 소개합니다. 이는 기술별 보상의 필요성을 제거하여 에이전트가 상호작용 기술을 학습하는 방식을 근본적으로 변화시키는 통합 데이터 기반 프레임워크입니다. 우리의 핵심 통찰은 통합된 HOI 모방 보상이 HOI 데이터셋의 다양한 상호작용 패턴의 본질을 효과적으로 포착할 수 있다는 것입니다. 이를 통해 SkillMimic은 단일 정책을 학습하여 여러 상호작용 기술을 숙달할 뿐만 아니라 기술 전환을 용이하게 하며, HOI 데이터셋이 성장함에 따라 다양성과 일반화가 모두 향상됩니다. 평가를 위해 약 35분 분량의 다양한 농구 기술을 포함하는 두 개의 농구 데이터셋을 수집하고 소개합니다. 광범위한 실험 결과, SkillMimic은 드리블, 레이업, 슛의 스타일 변형을 포함한 다양한 농구 기술을 성공적으로 숙달함을 보여줍니다. 더욱이, 이러한 학습된 기술은 고수준 컨트롤러에 의해 효과적으로 구성되어 연속 득점과 같은 복잡하고 장기적인 작업을 수행할 수 있으며, 확장 가능하고 일반화 가능한 상호작용 기술 학습의 새로운 가능성을 열어줍니다. 프로젝트 페이지: https://ingrid789.github.io/SkillMimic/

## 핵심 내용
인간-객체 상호작용(HOI)을 위한 전통적인 강화 학습 방법은 노동 집약적이고 수동으로 설계된 기술 보상에 의존하며, 이는 다양한 상호작용 간에 잘 일반화되지 않습니다. 우리는 SkillMimic을 소개합니다. 이는 기술별 보상의 필요성을 제거하여 에이전트가 상호작용 기술을 학습하는 방식을 근본적으로 변화시키는 통합 데이터 기반 프레임워크입니다. 우리의 핵심 통찰은 통합된 HOI 모방 보상이 HOI 데이터셋의 다양한 상호작용 패턴의 본질을 효과적으로 포착할 수 있다는 것입니다. 이를 통해 SkillMimic은 단일 정책을 학습하여 여러 상호작용 기술을 숙달할 뿐만 아니라 기술 전환을 용이하게 하며, HOI 데이터셋이 성장함에 따라 다양성과 일반화가 모두 향상됩니다. 평가를 위해 약 35분 분량의 다양한 농구 기술을 포함하는 두 개의 농구 데이터셋을 수집하고 소개합니다. 광범위한 실험 결과, SkillMimic은 드리블, 레이업, 슛의 스타일 변형을 포함한 다양한 농구 기술을 성공적으로 숙달함을 보여줍니다. 더욱이, 이러한 학습된 기술은 고수준 컨트롤러에 의해 효과적으로 구성되어 연속 득점과 같은 복잡하고 장기적인 작업을 수행할 수 있으며, 확장 가능하고 일반화 가능한 상호작용 기술 학습의 새로운 가능성을 열어줍니다. 프로젝트 페이지: https://ingrid789.github.io/SkillMimic/
