---
$id: ent_paper_learning_whole_body_human_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
  zh: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
  ko: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations
summary:
  en: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
  zh: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
  ko: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations is a 2026 work on loco-manipulation and
    whole-body-control for humanoid robots.
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
- learning_whole_body_human_huma
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.09518v1.
sources:
- id: src_001
  type: paper
  title: Learning Whole-Body Human-Humanoid Interaction from Human-Human Demonstrations (arXiv)
  url: https://arxiv.org/abs/2601.09518
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

## 核心内容
Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

## 参考
- http://arxiv.org/abs/2601.09518v1

## Overview
Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

## Content
Enabling humanoid robots to physically interact with humans is a critical frontier, but progress is hindered by the scarcity of high-quality Human-Humanoid Interaction (HHoI) data. While leveraging abundant Human-Human Interaction (HHI) data presents a scalable alternative, we first demonstrate that standard retargeting fails by breaking the essential contacts. We address this with PAIR (Physics-Aware Interaction Retargeting), a contact-centric, two-stage pipeline that preserves contact semantics across morphology differences to generate physically consistent HHoI data. This high-quality data, however, exposes a second failure: conventional imitation learning policies merely mimic trajectories and lack interactive understanding. We therefore introduce D-STAR (Decoupled Spatio-Temporal Action Reasoner), a hierarchical policy that disentangles when to act from where to act. In D-STAR, Phase Attention (when) and a Multi-Scale Spatial module (where) are fused by the diffusion head to produce synchronized whole-body behaviors beyond mimicry. By decoupling these reasoning streams, our model learns robust temporal phases without being distracted by spatial noise, leading to responsive, synchronized collaboration. We validate our framework through extensive and rigorous simulations, demonstrating significant performance gains over baseline approaches and a complete, effective pipeline for learning complex whole-body interactions from HHI data.

## 개요
휴머노이드 로봇이 인간과 물리적으로 상호작용할 수 있게 하는 것은 중요한 연구 분야이지만, 고품질의 인간-휴머노이드 상호작용(HHoI) 데이터 부족으로 인해 진전이 더디게 이루어지고 있습니다. 풍부한 인간-인간 상호작용(HHI) 데이터를 활용하는 것은 확장 가능한 대안이 될 수 있지만, 먼저 표준 리타겟팅이 필수적인 접촉을 깨뜨려 실패한다는 것을 입증합니다. 우리는 이를 접촉 중심의 2단계 파이프라인인 PAIR(Physics-Aware Interaction Retargeting)로 해결하여, 형태학적 차이를 넘어 접촉 의미론을 보존하고 물리적으로 일관된 HHoI 데이터를 생성합니다. 그러나 이 고품질 데이터는 두 번째 실패를 드러냅니다: 기존의 모방 학습 정책은 단순히 궤적을 모방할 뿐 상호작용 이해가 부족하다는 점입니다. 따라서 우리는 D-STAR(Decoupled Spatio-Temporal Action Reasoner)를 도입합니다. 이는 행동할 시기와 장소를 분리하는 계층적 정책입니다. D-STAR에서 위상 주의(시기)와 다중 스케일 공간 모듈(장소)은 확산 헤드에 의해 융합되어 모방을 넘어선 동기화된 전신 행동을 생성합니다. 이러한 추론 흐름을 분리함으로써, 우리 모델은 공간적 노이즈에 방해받지 않고 강건한 시간적 위상을 학습하여 반응적이고 동기화된 협업을 이끌어냅니다. 우리는 광범위하고 엄격한 시뮬레이션을 통해 프레임워크를 검증하며, 기준 접근법 대비 상당한 성능 향상과 HHI 데이터로부터 복잡한 전신 상호작용을 학습하는 완전하고 효과적인 파이프라인을 입증합니다.

## 핵심 내용
휴머노이드 로봇이 인간과 물리적으로 상호작용할 수 있게 하는 것은 중요한 연구 분야이지만, 고품질의 인간-휴머노이드 상호작용(HHoI) 데이터 부족으로 인해 진전이 더디게 이루어지고 있습니다. 풍부한 인간-인간 상호작용(HHI) 데이터를 활용하는 것은 확장 가능한 대안이 될 수 있지만, 먼저 표준 리타겟팅이 필수적인 접촉을 깨뜨려 실패한다는 것을 입증합니다. 우리는 이를 접촉 중심의 2단계 파이프라인인 PAIR(Physics-Aware Interaction Retargeting)로 해결하여, 형태학적 차이를 넘어 접촉 의미론을 보존하고 물리적으로 일관된 HHoI 데이터를 생성합니다. 그러나 이 고품질 데이터는 두 번째 실패를 드러냅니다: 기존의 모방 학습 정책은 단순히 궤적을 모방할 뿐 상호작용 이해가 부족하다는 점입니다. 따라서 우리는 D-STAR(Decoupled Spatio-Temporal Action Reasoner)를 도입합니다. 이는 행동할 시기와 장소를 분리하는 계층적 정책입니다. D-STAR에서 위상 주의(시기)와 다중 스케일 공간 모듈(장소)은 확산 헤드에 의해 융합되어 모방을 넘어선 동기화된 전신 행동을 생성합니다. 이러한 추론 흐름을 분리함으로써, 우리 모델은 공간적 노이즈에 방해받지 않고 강건한 시간적 위상을 학습하여 반응적이고 동기화된 협업을 이끌어냅니다. 우리는 광범위하고 엄격한 시뮬레이션을 통해 프레임워크를 검증하며, 기준 접근법 대비 상당한 성능 향상과 HHI 데이터로부터 복잡한 전신 상호작용을 학습하는 완전하고 효과적인 파이프라인을 입증합니다.
