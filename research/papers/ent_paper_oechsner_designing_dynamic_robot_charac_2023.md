---
$id: ent_paper_oechsner_designing_dynamic_robot_charac_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Designing Dynamic Robot Characters to Improve Robot-Human Communications
  zh: 设计动态机器人角色以改善人机通信
  ko: 로봇-인간 커뮤니케이션 향상을 위한 동적 로봇 캐릭터 설계
summary:
  en: A CHI 2023 workshop position paper that synthesizes two decades of Human-Robot
    Communication research to argue for dynamic robot personalities which adapt from
    an initially transparent, extraverted "getting-to-know" phase toward a more subdued,
    habituated phase to sustain long-term trust and acceptance in Socially Assistive
    Robots.
  zh: 该CHI 2023研讨会立场论文综合了二十年的人机通信研究，主张为社交辅助机器人设计动态人格：从最初的透明、外向的“相识”阶段过渡到更克制、习惯化的阶段，以维持长期信任与接受度。
  ko: 이 CHI 2023 워크숍 포지션 논문은 20년간의 인간-로봇 커뮤니케이션 연구를 종합하여, 사회적 보조 로봇에서 장기적 신뢰와 수용성을
    유지하기 위해 초기 투명하고 외향적인 '알아가기' 단계에서 점차 절제되고 습관화된 단계로 적응하는 동적 로봇 성격 설계를 주장한다.
domains:
- 06_design_engineering
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- socially_assistive_robots
- human_robot_communication
- dynamic_personality
- robot_personality
- multimodal_communication
- robot_transparency
- habituation
- long_term_interaction
- embodiment
- hci
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Designing Dynamic Robot Characters to Improve Robot-Human Communications
  url: https://arxiv.org/abs/2303.05219
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This CHI 2023 workshop position paper by Carl Oechsner and Daniel Ullrich (LMU Munich) argues that Socially Assistive Robots (SARs) operate in sensitive environments where sustained user trust and acceptance depend on transparent, coherent communication. The authors observe that although individual communication modalities have been studied extensively, long-term studies examining how users' communication needs change as novelty effects fade are scarce. Drawing on two decades of Human-Robot Communication research, they frame the design of dynamic robot personalities as a way to unlock the full potential of SARs.

The paper reviews prior work on robot reasoning and communication (verbal and non-verbal cues, movement, gestures, gaze), personality and embodiment, and the evolving user-robot relationship including habituation. It argues that a robot's perceived personality helps users predict behavior and understand reasoning, but that a static, consistently extraverted personality may become draining over long-term use. Instead, the authors propose a two-phase dynamic personality: an initial "getting-to-know" phase that is open, transparent, and inviting, followed by a habituation phase in which extraversion, communication frequency, and explanatory detail are gradually reduced while reliability remains high.

The authors acknowledge risks: humans value personality consistency, so adaptation must be subtle enough to avoid undermining trust. They call for more long-term studies and for coherence across verbal, non-verbal, movement, and gaze channels.

## Key Contributions

- Synthesizes prior work on robot communication, personality, embodiment, and user-robot relationships.
- Proposes designing dynamic robot personalities that adapt over long-term interaction.
- Recommends transitioning from high-transparency, extraverted initial behavior to toned-down behavior as users habituate.
- Argues for coherence across verbal, non-verbal, movement, and gaze communication channels.
- Highlights the need for more long-term studies on changing communication requirements.

## Relevance to Humanoid Robotics

The paper's focus on coherent multimodal communication, dynamic personality design, and long-term trust is directly applicable to deploying humanoid robots in assistive and social roles where sustained user acceptance is critical. Humanoid robots typically combine speech, gaze, gesture, and full-body movement, making the integration and temporal adaptation of these channels especially relevant. The proposed two-phase personality framework can inform the design of humanoid behaviors in eldercare, education, therapy, and collaborative service settings.
