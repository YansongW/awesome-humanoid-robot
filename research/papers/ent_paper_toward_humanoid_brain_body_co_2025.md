---
$id: ent_paper_toward_humanoid_brain_body_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
  zh: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
  ko: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery'
summary:
  en: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
  zh: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
  ko: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery is a 2025 work
    on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- hardware_design
- humanoid
- toward_humanoid_brain_body_co
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.22336v2.
sources:
- id: src_001
  type: paper
  title: 'Toward Humanoid Brain-Body Co-design: Joint Optimization of Control and Morphology for Fall Recovery (arXiv)'
  url: https://arxiv.org/abs/2510.22336
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## 核心内容
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## 参考
- http://arxiv.org/abs/2510.22336v2

## Overview
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## Content
Humanoid robots represent a central frontier in embodied intelligence, as their anthropomorphic form enables natural deployment in humans' workspace. Brain-body co-design for humanoids presents a promising approach to realizing this potential by jointly optimizing control policies and physical morphology. Within this context, fall recovery emerges as a critical capability. It not only enhances safety and resilience but also integrates naturally with locomotion systems, thereby advancing the autonomy of humanoids. In this paper, we propose RoboCraft, a scalable humanoid co-design framework for fall recovery that iteratively improves performance through the coupled updates of control policy and morphology. A shared policy pretrained across multiple designs is progressively finetuned on high-performing morphologies, enabling efficient adaptation without retraining from scratch. Concurrently, morphology search is guided by human-inspired priors and optimization algorithms, supported by a priority buffer that balances reevaluation of promising candidates with the exploration of novel designs. Experiments show that RoboCraft achieves an average performance gain of 44.55% on seven public humanoid robots, with morphology optimization drives at least 40% of improvements in co-designing four humanoid robots, underscoring the critical role of humanoid co-design.

## 개요
휴머노이드 로봇은 체현 지능의 핵심 프론티어로, 인간형 형태 덕분에 인간의 작업 공간에서 자연스럽게 배치될 수 있습니다. 휴머노이드를 위한 두뇌-신체 공동 설계는 제어 정책과 물리적 형태를 동시에 최적화함으로써 이러한 잠재력을 실현하는 유망한 접근법을 제시합니다. 이러한 맥락에서 낙상 회복은 중요한 능력으로 부상합니다. 이는 안전성과 회복력을 향상시킬 뿐만 아니라 보행 시스템과 자연스럽게 통합되어 휴머노이드의 자율성을 발전시킵니다. 본 논문에서는 제어 정책과 형태의 결합된 업데이트를 통해 반복적으로 성능을 개선하는 확장 가능한 휴머노이드 공동 설계 프레임워크인 RoboCraft를 제안합니다. 여러 설계에 걸쳐 사전 학습된 공유 정책은 고성능 형태에 점진적으로 미세 조정되어 처음부터 재학습 없이 효율적인 적응을 가능하게 합니다. 동시에 형태 탐색은 인간에서 영감을 받은 사전 지식과 최적화 알고리즘에 의해 안내되며, 유망한 후보의 재평가와 새로운 설계 탐색 간의 균형을 맞추는 우선순위 버퍼에 의해 지원됩니다. 실험 결과, RoboCraft는 7개의 공개 휴머노이드 로봇에서 평균 44.55%의 성능 향상을 달성했으며, 형태 최적화는 4개의 휴머노이드 로봇 공동 설계에서 개선의 최소 40%를 주도하여 휴머노이드 공동 설계의 중요한 역할을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 체현 지능의 핵심 프론티어로, 인간형 형태 덕분에 인간의 작업 공간에서 자연스럽게 배치될 수 있습니다. 휴머노이드를 위한 두뇌-신체 공동 설계는 제어 정책과 물리적 형태를 동시에 최적화함으로써 이러한 잠재력을 실현하는 유망한 접근법을 제시합니다. 이러한 맥락에서 낙상 회복은 중요한 능력으로 부상합니다. 이는 안전성과 회복력을 향상시킬 뿐만 아니라 보행 시스템과 자연스럽게 통합되어 휴머노이드의 자율성을 발전시킵니다. 본 논문에서는 제어 정책과 형태의 결합된 업데이트를 통해 반복적으로 성능을 개선하는 확장 가능한 휴머노이드 공동 설계 프레임워크인 RoboCraft를 제안합니다. 여러 설계에 걸쳐 사전 학습된 공유 정책은 고성능 형태에 점진적으로 미세 조정되어 처음부터 재학습 없이 효율적인 적응을 가능하게 합니다. 동시에 형태 탐색은 인간에서 영감을 받은 사전 지식과 최적화 알고리즘에 의해 안내되며, 유망한 후보의 재평가와 새로운 설계 탐색 간의 균형을 맞추는 우선순위 버퍼에 의해 지원됩니다. 실험 결과, RoboCraft는 7개의 공개 휴머노이드 로봇에서 평균 44.55%의 성능 향상을 달성했으며, 형태 최적화는 4개의 휴머노이드 로봇 공동 설계에서 개선의 최소 40%를 주도하여 휴머노이드 공동 설계의 중요한 역할을 강조합니다.
