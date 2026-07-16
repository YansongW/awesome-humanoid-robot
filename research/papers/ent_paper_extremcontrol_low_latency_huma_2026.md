---
$id: ent_paper_extremcontrol_low_latency_huma_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
  zh: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
  ko: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control'
summary:
  en: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
  zh: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
  ko: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control is a 2026 work on teleoperation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- extremcontrol
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.11321v3.
sources:
- id: src_001
  type: paper
  title: 'ExtremControl: Low-Latency Humanoid Teleoperation with Direct Extremity Control (arXiv)'
  url: https://arxiv.org/abs/2602.11321
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## 核心内容
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## 参考
- http://arxiv.org/abs/2602.11321v3

## Overview
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## Content
Building a low-latency humanoid teleoperation system is essential for collecting diverse reactive and dynamic demonstrations. However, existing approaches rely on heavily pre-processed human-to-humanoid motion retargeting and position-only PD control, resulting in substantial latency that severely limits responsiveness and prevents tasks requiring rapid feedback and fast reactions. To address this problem, we propose ExtremControl, a low latency whole-body control framework that: (1) operates directly on SE(3) poses of selected rigid links, primarily humanoid extremities, to avoid full-body retargeting; (2) utilizes a Cartesian-space mapping to directly convert human motion to humanoid link targets; and (3) incorporates velocity feedforward control at low level to support highly responsive behavior under rapidly changing control interfaces. We further provide a unified theoretical formulation of ExtremControl and systematically validate its effectiveness through experiments in both simulation and real-world environments. Building on ExtremControl, we implement a low-latency humanoid teleoperation system that supports both optical motion capture and VR-based motion tracking, achieving end-to-end latency as low as 50ms and enabling highly responsive behaviors such as ping-pong ball balancing, juggling, and real-time return, thereby substantially surpassing the 200ms latency limit observed in prior work.

## 개요
저지연 휴머노이드 원격 조작 시스템을 구축하는 것은 다양한 반응형 및 동적 시연을 수집하는 데 필수적입니다. 그러나 기존 접근 방식은 과도하게 전처리된 인간-휴머노이드 모션 리타겟팅과 위치 전용 PD 제어에 의존하여 상당한 지연을 초래하며, 이는 응답성을 심각하게 제한하고 빠른 피드백과 신속한 반응이 필요한 작업을 방해합니다. 이 문제를 해결하기 위해 우리는 ExtremControl을 제안합니다. 이는 저지연 전신 제어 프레임워크로, (1) 전신 리타겟팅을 피하기 위해 선택된 강체 링크(주로 휴머노이드 말단)의 SE(3) 포즈를 직접 연산하고, (2) 데카르트 공간 매핑을 활용하여 인간의 움직임을 휴머노이드 링크 목표로 직접 변환하며, (3) 저수준에서 속도 피드포워드 제어를 통합하여 빠르게 변화하는 제어 인터페이스에서 높은 응답성을 지원합니다. 또한 ExtremControl의 통일된 이론적 정식화를 제공하고 시뮬레이션 및 실제 환경 실험을 통해 그 효과를 체계적으로 검증합니다. ExtremControl을 기반으로 광학 모션 캡처와 VR 기반 모션 트래킹을 모두 지원하는 저지연 휴머노이드 원격 조작 시스템을 구현하여 종단 간 지연을 최대 50ms까지 낮추고, 탁구공 균형 잡기, 저글링, 실시간 반환과 같은 높은 응답성을 요하는 동작을 가능하게 하여 이전 연구에서 관찰된 200ms 지연 한계를 크게 초과합니다.

## 핵심 내용
저지연 휴머노이드 원격 조작 시스템을 구축하는 것은 다양한 반응형 및 동적 시연을 수집하는 데 필수적입니다. 그러나 기존 접근 방식은 과도하게 전처리된 인간-휴머노이드 모션 리타겟팅과 위치 전용 PD 제어에 의존하여 상당한 지연을 초래하며, 이는 응답성을 심각하게 제한하고 빠른 피드백과 신속한 반응이 필요한 작업을 방해합니다. 이 문제를 해결하기 위해 우리는 ExtremControl을 제안합니다. 이는 저지연 전신 제어 프레임워크로, (1) 전신 리타겟팅을 피하기 위해 선택된 강체 링크(주로 휴머노이드 말단)의 SE(3) 포즈를 직접 연산하고, (2) 데카르트 공간 매핑을 활용하여 인간의 움직임을 휴머노이드 링크 목표로 직접 변환하며, (3) 저수준에서 속도 피드포워드 제어를 통합하여 빠르게 변화하는 제어 인터페이스에서 높은 응답성을 지원합니다. 또한 ExtremControl의 통일된 이론적 정식화를 제공하고 시뮬레이션 및 실제 환경 실험을 통해 그 효과를 체계적으로 검증합니다. ExtremControl을 기반으로 광학 모션 캡처와 VR 기반 모션 트래킹을 모두 지원하는 저지연 휴머노이드 원격 조작 시스템을 구현하여 종단 간 지연을 최대 50ms까지 낮추고, 탁구공 균형 잡기, 저글링, 실시간 반환과 같은 높은 응답성을 요하는 동작을 가능하게 하여 이전 연구에서 관찰된 200ms 지연 한계를 크게 초과합니다.
