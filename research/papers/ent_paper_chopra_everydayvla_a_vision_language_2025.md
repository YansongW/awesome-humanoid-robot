---
$id: ent_paper_chopra_everydayvla_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation'
  zh: EveryDayVLA
  ko: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation'
summary:
  en: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (EveryDayVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pittsburgh, University of Pittsburgh Center for Research Computing.'
  zh: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (EveryDayVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pittsburgh, University of Pittsburgh Center for Research Computing.'
  ko: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (EveryDayVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pittsburgh, University of Pittsburgh Center for Research Computing.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- everydayvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.05397v1.
sources:
- id: src_001
  type: paper
  title: 'EveryDayVLA: A Vision-Language-Action Model for Affordable Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2511.05397
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EveryDayVLA source
  url: https://doi.org/10.48550/arXiv.2511.05397
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or cluttered scenes. We introduce EverydayVLA, a 6-DOF manipulator that can be assembled for under $300, capable of modest payloads and workspace. A single unified model jointly outputs discrete and continuous actions, and our adaptive-horizon ensemble monitors motion uncertainty to trigger on-the-fly re-planning for safe, reliable operation. On LIBERO, EverydayVLA matches state-of-the-art success rates, and in real-world tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution. By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model and paves the way for economical use in homes and research labs alike. Experiment videos and details: https://everydayvla.github.io/

## 核心内容
While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or cluttered scenes. We introduce EverydayVLA, a 6-DOF manipulator that can be assembled for under $300, capable of modest payloads and workspace. A single unified model jointly outputs discrete and continuous actions, and our adaptive-horizon ensemble monitors motion uncertainty to trigger on-the-fly re-planning for safe, reliable operation. On LIBERO, EverydayVLA matches state-of-the-art success rates, and in real-world tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution. By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model and paves the way for economical use in homes and research labs alike. Experiment videos and details: https://everydayvla.github.io/

## 参考
- http://arxiv.org/abs/2511.05397v1

## Overview
While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or cluttered scenes. We introduce EverydayVLA, a 6-DOF manipulator that can be assembled for under $300, capable of modest payloads and workspace. A single unified model jointly outputs discrete and continuous actions, and our adaptive-horizon ensemble monitors motion uncertainty to trigger on-the-fly re-planning for safe, reliable operation. On LIBERO, EverydayVLA matches state-of-the-art success rates, and in real-world tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution. By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model and paves the way for economical use in homes and research labs alike. Experiment videos and details: https://everydayvla.github.io/

## Content
While Vision-Language-Action (VLA) models map visual inputs and language instructions directly to robot actions, they often rely on costly hardware and struggle in novel or cluttered scenes. We introduce EverydayVLA, a 6-DOF manipulator that can be assembled for under $300, capable of modest payloads and workspace. A single unified model jointly outputs discrete and continuous actions, and our adaptive-horizon ensemble monitors motion uncertainty to trigger on-the-fly re-planning for safe, reliable operation. On LIBERO, EverydayVLA matches state-of-the-art success rates, and in real-world tests it outperforms prior methods by 49% in-distribution and 34.9% out-of-distribution. By combining a state-of-the-art VLA with cost-effective hardware, EverydayVLA democratizes access to a robotic foundation model and paves the way for economical use in homes and research labs alike. Experiment videos and details: https://everydayvla.github.io/

## 개요
Vision-Language-Action(VLA) 모델은 시각 입력과 언어 명령을 로봇 동작에 직접 매핑하지만, 종종 고가의 하드웨어에 의존하고 새로운 환경이나 복잡한 장면에서 어려움을 겪습니다. 우리는 300달러 미만으로 조립 가능하며 적당한 페이로드와 작업 공간을 갖춘 6-DOF 매니퓰레이터인 EverydayVLA를 소개합니다. 단일 통합 모델이 이산 동작과 연속 동작을 동시에 출력하며, 적응형 수평선 앙상블이 움직임 불확실성을 모니터링하여 안전하고 신뢰할 수 있는 운영을 위해 실시간 재계획을 트리거합니다. LIBERO에서 EverydayVLA는 최첨단 성공률과 일치하며, 실제 테스트에서는 분포 내에서 49%, 분포 외에서 34.9% 더 우수한 성능을 보입니다. 최첨단 VLA와 비용 효율적인 하드웨어를 결합함으로써 EverydayVLA는 로봇 기반 모델에 대한 접근성을 대중화하고 가정과 연구실에서 경제적으로 사용할 수 있는 길을 열어줍니다. 실험 비디오 및 세부 정보: https://everydayvla.github.io/

## 핵심 내용
Vision-Language-Action(VLA) 모델은 시각 입력과 언어 명령을 로봇 동작에 직접 매핑하지만, 종종 고가의 하드웨어에 의존하고 새로운 환경이나 복잡한 장면에서 어려움을 겪습니다. 우리는 300달러 미만으로 조립 가능하며 적당한 페이로드와 작업 공간을 갖춘 6-DOF 매니퓰레이터인 EverydayVLA를 소개합니다. 단일 통합 모델이 이산 동작과 연속 동작을 동시에 출력하며, 적응형 수평선 앙상블이 움직임 불확실성을 모니터링하여 안전하고 신뢰할 수 있는 운영을 위해 실시간 재계획을 트리거합니다. LIBERO에서 EverydayVLA는 최첨단 성공률과 일치하며, 실제 테스트에서는 분포 내에서 49%, 분포 외에서 34.9% 더 우수한 성능을 보입니다. 최첨단 VLA와 비용 효율적인 하드웨어를 결합함으로써 EverydayVLA는 로봇 기반 모델에 대한 접근성을 대중화하고 가정과 연구실에서 경제적으로 사용할 수 있는 길을 열어줍니다. 실험 비디오 및 세부 정보: https://everydayvla.github.io/
