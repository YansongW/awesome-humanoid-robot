---
$id: ent_paper_labimus_a_simulation_and_bench_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  zh: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  ko: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
summary:
  en: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
  zh: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
  ko: 'arXiv:2606.31037v1 Announce Type: new Abstract: Laboratory automation has made remarkable progress through robotic
    platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain
    inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical
    manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity,
    no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus,
    to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs
    over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively
    covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory
    instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement
    pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory
    standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion,
    experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts
    and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks
    can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental
    disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid
    robots for scientific laboratories.'
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
- labimus
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31037v2.
sources:
- id: src_001
  type: paper
  title: 'Labimus: A Simulation and Benchmark for Humanoid Dexterous Manipulation in Chemical Laboratory'
  url: https://arxiv.org/abs/2606.31037
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity, no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus, to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion, experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid robots for scientific laboratories.

## 核心内容
Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity, no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus, to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion, experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid robots for scientific laboratories.

## 参考
- http://arxiv.org/abs/2606.31037v2

## Overview
Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity, no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus, to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion, experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid robots for scientific laboratories.

## Content
Laboratory automation has made remarkable progress through robotic platforms and AI-driven scientific reasoning. However, many laboratory operations (e.g., solid--solid transfer) remain inherently dynamic and require real-time adaptation to different materials and experimental conditions. Such precision-critical manipulations are difficult to standardize, motivating the use of humanoid robots with dexterous hands. Despite this opportunity, no existing benchmark evaluates humanoid manipulation in precision-critical laboratory environments. We present Labimus, to our knowledge, the first benchmark for humanoid dexterous manipulation in organic chemistry laboratories. Labimus reconstructs over 30 functionally faithful assets from real organic chemistry workstations through real-to-sim modeling, collectively covering the core operations of routine organic chemistry experiments. The benchmark integrates articulated laboratory instruments, particle-based powder physics, and closed-loop instrument readouts, enabling a complete manipulation-to-measurement pipeline. It further defines six atomic operations and a seven-step solid-weighing workflow derived from real laboratory standard operating procedures. We introduce a precision-aware evaluation protocol designed to jointly measure task completion, experimental precision, and long-horizon execution. We benchmark three representative policies under procedural layouts and environmental perturbations. Results reveal a precision gap: policies that successfully complete laboratory tasks can still fail to satisfy the quantitative tolerances required by experimental protocols. Our benchmark exposes a fundamental disconnect between task completion and experimental validity, providing a new testbed for developing reliable humanoid robots for scientific laboratories.

## 개요
로봇 플랫폼과 AI 기반 과학적 추론을 통해 실험실 자동화는 놀라운 진전을 이루었습니다. 그러나 많은 실험실 작업(예: 고체-고체 전달)은 본질적으로 동적이며, 다양한 재료와 실험 조건에 실시간으로 적응해야 합니다. 이러한 정밀도가 중요한 조작은 표준화하기 어려워, 손재주가 뛰어난 손을 가진 휴머노이드 로봇의 사용을 촉진합니다. 이러한 기회에도 불구하고, 정밀도가 중요한 실험실 환경에서 휴머노이드 조작을 평가하는 기존 벤치마크는 존재하지 않습니다. 우리는 유기화학 실험실에서 휴머노이드의 손재주 있는 조작을 위한 최초의 벤치마크인 Labimus를 제시합니다. Labimus는 실제 유기화학 워크스테이션의 30개 이상의 기능적으로 충실한 자산을 실제-시뮬레이션 모델링을 통해 재구성하여, 일상적인 유기화학 실험의 핵심 작업을 총체적으로 다룹니다. 이 벤치마크는 관절형 실험실 기기, 입자 기반 분말 물리, 폐쇄 루프 기기 판독값을 통합하여 완전한 조작-측정 파이프라인을 가능하게 합니다. 또한 실제 실험실 표준 운영 절차에서 파생된 6개의 원자 작업과 7단계 고체 칭량 워크플로우를 정의합니다. 우리는 작업 완료, 실험 정밀도, 장기 실행을 공동으로 측정하도록 설계된 정밀도 인식 평가 프로토콜을 도입합니다. 절차적 배치와 환경적 교란 하에서 세 가지 대표적인 정책을 벤치마킹합니다. 결과는 정밀도 격차를 드러냅니다. 실험실 작업을 성공적으로 완료하는 정책도 실험 프로토콜에 필요한 정량적 허용 오차를 충족하지 못할 수 있습니다. 우리의 벤치마크는 작업 완료와 실험적 타당성 사이의 근본적인 단절을 드러내며, 과학 실험실을 위한 신뢰할 수 있는 휴머노이드 로봇 개발을 위한 새로운 테스트베드를 제공합니다.

## 핵심 내용
로봇 플랫폼과 AI 기반 과학적 추론을 통해 실험실 자동화는 놀라운 진전을 이루었습니다. 그러나 많은 실험실 작업(예: 고체-고체 전달)은 본질적으로 동적이며, 다양한 재료와 실험 조건에 실시간으로 적응해야 합니다. 이러한 정밀도가 중요한 조작은 표준화하기 어려워, 손재주가 뛰어난 손을 가진 휴머노이드 로봇의 사용을 촉진합니다. 이러한 기회에도 불구하고, 정밀도가 중요한 실험실 환경에서 휴머노이드 조작을 평가하는 기존 벤치마크는 존재하지 않습니다. 우리는 유기화학 실험실에서 휴머노이드의 손재주 있는 조작을 위한 최초의 벤치마크인 Labimus를 제시합니다. Labimus는 실제 유기화학 워크스테이션의 30개 이상의 기능적으로 충실한 자산을 실제-시뮬레이션 모델링을 통해 재구성하여, 일상적인 유기화학 실험의 핵심 작업을 총체적으로 다룹니다. 이 벤치마크는 관절형 실험실 기기, 입자 기반 분말 물리, 폐쇄 루프 기기 판독값을 통합하여 완전한 조작-측정 파이프라인을 가능하게 합니다. 또한 실제 실험실 표준 운영 절차에서 파생된 6개의 원자 작업과 7단계 고체 칭량 워크플로우를 정의합니다. 우리는 작업 완료, 실험 정밀도, 장기 실행을 공동으로 측정하도록 설계된 정밀도 인식 평가 프로토콜을 도입합니다. 절차적 배치와 환경적 교란 하에서 세 가지 대표적인 정책을 벤치마킹합니다. 결과는 정밀도 격차를 드러냅니다. 실험실 작업을 성공적으로 완료하는 정책도 실험 프로토콜에 필요한 정량적 허용 오차를 충족하지 못할 수 있습니다. 우리의 벤치마크는 작업 완료와 실험적 타당성 사이의 근본적인 단절을 드러내며, 과학 실험실을 위한 신뢰할 수 있는 휴머노이드 로봇 개발을 위한 새로운 테스트베드를 제공합니다.
