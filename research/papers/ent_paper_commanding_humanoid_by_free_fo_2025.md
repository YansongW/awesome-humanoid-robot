---
$id: ent_paper_commanding_humanoid_by_free_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary'
  zh: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary'
  ko: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary'
summary:
  en: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- commanding_humanoid_by_free_fo
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22963v3.
sources:
- id: src_001
  type: paper
  title: 'Commanding Humanoid by Free-form Language: A Large Language Action Model with Unified Motion Vocabulary (arXiv)'
  url: https://arxiv.org/abs/2511.22963
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to follow free-form natural language commands is a critical step toward seamless human-robot interaction and general-purpose embodied AI. However, existing methods remain limited, often constrained to simple instructions or forced to sacrifice motion diversity for physical plausibility. To address this gap, we present Humanoid-LLA, a Large Language Action model that translates unconstrained natural language directly into executable whole-body motions for humanoid robots. Our approach tackles two core challenges: paired language-humanoid motion data scarcity and physical instability. First, we bridge high-level language semantics with physically-grounded control by learning a unified human-humanoid motion vocabulary. Second, we introduce a novel two-stage fine-tuning framework that begins with supervised motion Chain-of-Thought learning, followed by reinforcement learning refined with physical feedback to ensure robustness and stability. Extensive evaluation in simulation and real-world cross-embodiment experiments demonstrates that Humanoid-LLA achieves superior generalization to novel language commands and diverse motion generation while maintaining high physical fidelity.

## 核心内容
Enabling humanoid robots to follow free-form natural language commands is a critical step toward seamless human-robot interaction and general-purpose embodied AI. However, existing methods remain limited, often constrained to simple instructions or forced to sacrifice motion diversity for physical plausibility. To address this gap, we present Humanoid-LLA, a Large Language Action model that translates unconstrained natural language directly into executable whole-body motions for humanoid robots. Our approach tackles two core challenges: paired language-humanoid motion data scarcity and physical instability. First, we bridge high-level language semantics with physically-grounded control by learning a unified human-humanoid motion vocabulary. Second, we introduce a novel two-stage fine-tuning framework that begins with supervised motion Chain-of-Thought learning, followed by reinforcement learning refined with physical feedback to ensure robustness and stability. Extensive evaluation in simulation and real-world cross-embodiment experiments demonstrates that Humanoid-LLA achieves superior generalization to novel language commands and diverse motion generation while maintaining high physical fidelity.

## 参考
- http://arxiv.org/abs/2511.22963v3

## Overview
Enabling humanoid robots to follow free-form natural language commands is a critical step toward seamless human-robot interaction and general-purpose embodied AI. However, existing methods remain limited, often constrained to simple instructions or forced to sacrifice motion diversity for physical plausibility. To address this gap, we present Humanoid-LLA, a Large Language Action model that translates unconstrained natural language directly into executable whole-body motions for humanoid robots. Our approach tackles two core challenges: paired language-humanoid motion data scarcity and physical instability. First, we bridge high-level language semantics with physically-grounded control by learning a unified human-humanoid motion vocabulary. Second, we introduce a novel two-stage fine-tuning framework that begins with supervised motion Chain-of-Thought learning, followed by reinforcement learning refined with physical feedback to ensure robustness and stability. Extensive evaluation in simulation and real-world cross-embodiment experiments demonstrates that Humanoid-LLA achieves superior generalization to novel language commands and diverse motion generation while maintaining high physical fidelity.

## Content
Enabling humanoid robots to follow free-form natural language commands is a critical step toward seamless human-robot interaction and general-purpose embodied AI. However, existing methods remain limited, often constrained to simple instructions or forced to sacrifice motion diversity for physical plausibility. To address this gap, we present Humanoid-LLA, a Large Language Action model that translates unconstrained natural language directly into executable whole-body motions for humanoid robots. Our approach tackles two core challenges: paired language-humanoid motion data scarcity and physical instability. First, we bridge high-level language semantics with physically-grounded control by learning a unified human-humanoid motion vocabulary. Second, we introduce a novel two-stage fine-tuning framework that begins with supervised motion Chain-of-Thought learning, followed by reinforcement learning refined with physical feedback to ensure robustness and stability. Extensive evaluation in simulation and real-world cross-embodiment experiments demonstrates that Humanoid-LLA achieves superior generalization to novel language commands and diverse motion generation while maintaining high physical fidelity.

## 개요
휴머노이드 로봇이 자유로운 자연어 명령을 따를 수 있도록 하는 것은 원활한 인간-로봇 상호작용과 범용 임베디드 AI를 위한 중요한 단계입니다. 그러나 기존 방법은 여전히 제한적이며, 종종 단순한 명령어에 국한되거나 물리적 타당성을 위해 동작 다양성을 희생해야 합니다. 이러한 격차를 해결하기 위해 우리는 Humanoid-LLA, 즉 제약 없는 자연어를 휴머노이드 로봇의 실행 가능한 전신 동작으로 직접 변환하는 대규모 언어 행동 모델을 제시합니다. 우리의 접근 방식은 두 가지 핵심 과제, 즉 짝을 이루는 언어-휴머노이드 동작 데이터 부족과 물리적 불안정성을 해결합니다. 첫째, 통합된 인간-휴머노이드 동작 어휘를 학습하여 고수준 언어 의미론을 물리적으로 기반한 제어와 연결합니다. 둘째, 감독된 동작 사고 사슬 학습으로 시작하여 물리적 피드백으로 정제된 강화 학습을 통해 견고성과 안정성을 보장하는 새로운 2단계 미세 조정 프레임워크를 도입합니다. 시뮬레이션 및 실제 교차 체현 실험에서의 광범위한 평가는 Humanoid-LLA가 높은 물리적 충실도를 유지하면서 새로운 언어 명령에 대한 뛰어난 일반화와 다양한 동작 생성을 달성함을 보여줍니다.

## 핵심 내용
휴머노이드 로봇이 자유로운 자연어 명령을 따를 수 있도록 하는 것은 원활한 인간-로봇 상호작용과 범용 임베디드 AI를 위한 중요한 단계입니다. 그러나 기존 방법은 여전히 제한적이며, 종종 단순한 명령어에 국한되거나 물리적 타당성을 위해 동작 다양성을 희생해야 합니다. 이러한 격차를 해결하기 위해 우리는 Humanoid-LLA, 즉 제약 없는 자연어를 휴머노이드 로봇의 실행 가능한 전신 동작으로 직접 변환하는 대규모 언어 행동 모델을 제시합니다. 우리의 접근 방식은 두 가지 핵심 과제, 즉 짝을 이루는 언어-휴머노이드 동작 데이터 부족과 물리적 불안정성을 해결합니다. 첫째, 통합된 인간-휴머노이드 동작 어휘를 학습하여 고수준 언어 의미론을 물리적으로 기반한 제어와 연결합니다. 둘째, 감독된 동작 사고 사슬 학습으로 시작하여 물리적 피드백으로 정제된 강화 학습을 통해 견고성과 안정성을 보장하는 새로운 2단계 미세 조정 프레임워크를 도입합니다. 시뮬레이션 및 실제 교차 체현 실험에서의 광범위한 평가는 Humanoid-LLA가 높은 물리적 충실도를 유지하면서 새로운 언어 명령에 대한 뛰어난 일반화와 다양한 동작 생성을 달성함을 보여줍니다.
