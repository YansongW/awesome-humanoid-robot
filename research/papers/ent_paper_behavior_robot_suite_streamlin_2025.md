---
$id: ent_paper_behavior_robot_suite_streamlin_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities'
  zh: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities'
  ko: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities'
summary:
  en: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  ko: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities is a 2025 work
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
- behavior_robot_suite
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.05652v2.
sources:
- id: src_001
  type: paper
  title: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities (arXiv)'
  url: https://arxiv.org/abs/2503.05652
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'BEHAVIOR Robot Suite: Streamlining Real-World Whole-Body Manipulation for Everyday Household Activities project
    page'
  url: https://behavior-robot-suite.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Real-world household tasks present significant challenges for mobile manipulation robots. An analysis of existing robotics benchmarks reveals that successful task performance hinges on three key whole-body control capabilities: bimanual coordination, stable and precise navigation, and extensive end-effector reachability. Achieving these capabilities requires careful hardware design, but the resulting system complexity further complicates visuomotor policy learning. To address these challenges, we introduce the BEHAVIOR Robot Suite (BRS), a comprehensive framework for whole-body manipulation in diverse household tasks. Built on a bimanual, wheeled robot with a 4-DoF torso, BRS integrates a cost-effective whole-body teleoperation interface for data collection and a novel algorithm for learning whole-body visuomotor policies. We evaluate BRS on five challenging household tasks that not only emphasize the three core capabilities but also introduce additional complexities, such as long-range navigation, interaction with articulated and deformable objects, and manipulation in confined spaces. We believe that BRS's integrated robotic embodiment, data collection interface, and learning framework mark a significant step toward enabling real-world whole-body manipulation for everyday household tasks. BRS is open-sourced at https://behavior-robot-suite.github.io/

## 核心内容
Real-world household tasks present significant challenges for mobile manipulation robots. An analysis of existing robotics benchmarks reveals that successful task performance hinges on three key whole-body control capabilities: bimanual coordination, stable and precise navigation, and extensive end-effector reachability. Achieving these capabilities requires careful hardware design, but the resulting system complexity further complicates visuomotor policy learning. To address these challenges, we introduce the BEHAVIOR Robot Suite (BRS), a comprehensive framework for whole-body manipulation in diverse household tasks. Built on a bimanual, wheeled robot with a 4-DoF torso, BRS integrates a cost-effective whole-body teleoperation interface for data collection and a novel algorithm for learning whole-body visuomotor policies. We evaluate BRS on five challenging household tasks that not only emphasize the three core capabilities but also introduce additional complexities, such as long-range navigation, interaction with articulated and deformable objects, and manipulation in confined spaces. We believe that BRS's integrated robotic embodiment, data collection interface, and learning framework mark a significant step toward enabling real-world whole-body manipulation for everyday household tasks. BRS is open-sourced at https://behavior-robot-suite.github.io/

## 参考
- http://arxiv.org/abs/2503.05652v2

## Overview
Real-world household tasks present significant challenges for mobile manipulation robots. An analysis of existing robotics benchmarks reveals that successful task performance hinges on three key whole-body control capabilities: bimanual coordination, stable and precise navigation, and extensive end-effector reachability. Achieving these capabilities requires careful hardware design, but the resulting system complexity further complicates visuomotor policy learning. To address these challenges, we introduce the BEHAVIOR Robot Suite (BRS), a comprehensive framework for whole-body manipulation in diverse household tasks. Built on a bimanual, wheeled robot with a 4-DoF torso, BRS integrates a cost-effective whole-body teleoperation interface for data collection and a novel algorithm for learning whole-body visuomotor policies. We evaluate BRS on five challenging household tasks that not only emphasize the three core capabilities but also introduce additional complexities, such as long-range navigation, interaction with articulated and deformable objects, and manipulation in confined spaces. We believe that BRS's integrated robotic embodiment, data collection interface, and learning framework mark a significant step toward enabling real-world whole-body manipulation for everyday household tasks. BRS is open-sourced at https://behavior-robot-suite.github.io/

## Content
Real-world household tasks present significant challenges for mobile manipulation robots. An analysis of existing robotics benchmarks reveals that successful task performance hinges on three key whole-body control capabilities: bimanual coordination, stable and precise navigation, and extensive end-effector reachability. Achieving these capabilities requires careful hardware design, but the resulting system complexity further complicates visuomotor policy learning. To address these challenges, we introduce the BEHAVIOR Robot Suite (BRS), a comprehensive framework for whole-body manipulation in diverse household tasks. Built on a bimanual, wheeled robot with a 4-DoF torso, BRS integrates a cost-effective whole-body teleoperation interface for data collection and a novel algorithm for learning whole-body visuomotor policies. We evaluate BRS on five challenging household tasks that not only emphasize the three core capabilities but also introduce additional complexities, such as long-range navigation, interaction with articulated and deformable objects, and manipulation in confined spaces. We believe that BRS's integrated robotic embodiment, data collection interface, and learning framework mark a significant step toward enabling real-world whole-body manipulation for everyday household tasks. BRS is open-sourced at https://behavior-robot-suite.github.io/

## 개요
실제 가사 작업은 이동 조작 로봇에게 상당한 도전 과제를 제시합니다. 기존 로봇 벤치마크 분석에 따르면, 성공적인 작업 수행은 세 가지 핵심 전신 제어 능력, 즉 양손 협응, 안정적이고 정밀한 주행, 그리고 광범위한 엔드 이펙터 도달 범위에 달려 있습니다. 이러한 능력을 달성하려면 세심한 하드웨어 설계가 필요하지만, 그 결과 시스템 복잡성이 시각운동 정책 학습을 더욱 어렵게 만듭니다. 이러한 문제를 해결하기 위해 우리는 다양한 가사 작업에서 전신 조작을 위한 포괄적인 프레임워크인 BEHAVIOR Robot Suite (BRS)를 소개합니다. 4-DoF 몸통을 가진 양손 바퀴 달린 로봇을 기반으로 구축된 BRS는 데이터 수집을 위한 비용 효율적인 전신 원격 조작 인터페이스와 전신 시각운동 정책 학습을 위한 새로운 알고리즘을 통합합니다. 우리는 세 가지 핵심 능력을 강조할 뿐만 아니라 장거리 주행, 관절 및 변형 가능한 물체와의 상호 작용, 제한된 공간에서의 조작과 같은 추가적인 복잡성을 도입하는 다섯 가지 까다로운 가사 작업에서 BRS를 평가합니다. BRS의 통합된 로봇 구현, 데이터 수집 인터페이스 및 학습 프레임워크는 일상적인 가사 작업을 위한 실제 전신 조작을 가능하게 하는 중요한 진전이라고 믿습니다. BRS는 https://behavior-robot-suite.github.io/에서 오픈소스로 제공됩니다.

## 핵심 내용
실제 가사 작업은 이동 조작 로봇에게 상당한 도전 과제를 제시합니다. 기존 로봇 벤치마크 분석에 따르면, 성공적인 작업 수행은 세 가지 핵심 전신 제어 능력, 즉 양손 협응, 안정적이고 정밀한 주행, 그리고 광범위한 엔드 이펙터 도달 범위에 달려 있습니다. 이러한 능력을 달성하려면 세심한 하드웨어 설계가 필요하지만, 그 결과 시스템 복잡성이 시각운동 정책 학습을 더욱 어렵게 만듭니다. 이러한 문제를 해결하기 위해 우리는 다양한 가사 작업에서 전신 조작을 위한 포괄적인 프레임워크인 BEHAVIOR Robot Suite (BRS)를 소개합니다. 4-DoF 몸통을 가진 양손 바퀴 달린 로봇을 기반으로 구축된 BRS는 데이터 수집을 위한 비용 효율적인 전신 원격 조작 인터페이스와 전신 시각운동 정책 학습을 위한 새로운 알고리즘을 통합합니다. 우리는 세 가지 핵심 능력을 강조할 뿐만 아니라 장거리 주행, 관절 및 변형 가능한 물체와의 상호 작용, 제한된 공간에서의 조작과 같은 추가적인 복잡성을 도입하는 다섯 가지 까다로운 가사 작업에서 BRS를 평가합니다. BRS의 통합된 로봇 구현, 데이터 수집 인터페이스 및 학습 프레임워크는 일상적인 가사 작업을 위한 실제 전신 조작을 가능하게 하는 중요한 진전이라고 믿습니다. BRS는 https://behavior-robot-suite.github.io/에서 오픈소스로 제공됩니다.
