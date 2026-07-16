---
$id: ent_paper_leverb_humanoid_whole_body_con_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
  zh: LeVERB｜具有潜在视觉语言指令的人形全身控制
  ko: 'LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction'
summary:
  en: 'Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet
    most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector
    pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors
    required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the
    first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories.
    We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework
    for humanoid vision-language WBC, the first of its kind. At the'
  zh: LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
  ko: LeVERB 的实现路径是先把语言指令、相机图像/多视角观测、仿真交互数据编码成多模态表征，再用ACT/行为克隆模仿学习、VLA 多模态动作模型、潜变量/动作 token预测全身轨迹/动作序列、动作 chunk/token、低层控制器目标。关键点是保留
    VLM 的语义理解，同时增加机器人状态和动作头，避免只停留在语言规划。
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- contact_planning
- leverb
- mobile_manipulation
- task_planning
- visual_closed_loop
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: LeVERB: Humanoid Whole-Body
    Control with Latent Vision-Language Instruction.'
sources:
- id: src_001
  type: website
  title: LeVERB project page
  url: https://github.com/ember-lab-berkeley/LeVERB-Website
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain a 80% success rate on simple visual navigation tasks, and 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## 核心内容
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action"vocabulary"such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain a 80% success rate on simple visual navigation tasks, and 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## 参考
- Semantic Scholar search: LeVERB: Humanoid Whole-Body Control with Latent Vision-Language Instruction

## Overview
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action "vocabulary" such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain an 80% success rate on simple visual navigation tasks, and a 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## Content
Vision-language-action (VLA) models have demonstrated strong semantic understanding and zero-shot generalization, yet most existing systems assume an accurate low-level controller with hand-crafted action "vocabulary" such as end-effector pose or root velocity. This assumption confines prior work to quasi-static tasks and precludes the agile, whole-body behaviors required by humanoid whole-body control (WBC) tasks. To capture this gap in the literature, we start by introducing the first sim-to-real-ready, vision-language, closed-loop benchmark for humanoid WBC, comprising over 150 tasks from 10 categories. We then propose LeVERB: Latent Vision-Language-Encoded Robot Behavior, a hierarchical latent instruction-following framework for humanoid vision-language WBC, the first of its kind. At the top level, a vision-language policy learns a latent action vocabulary from synthetically rendered kinematic demonstrations; at the low level, a reinforcement-learned WBC policy consumes these latent verbs to generate dynamics-level commands. In our benchmark, LeVERB can zero-shot attain an 80% success rate on simple visual navigation tasks, and a 58.5% success rate overall, outperforming naive hierarchical whole-body VLA implementation by 7.8 times.

## 개요
Vision-language-action (VLA) 모델은 강력한 의미 이해와 제로샷 일반화 능력을 보여주었지만, 대부분의 기존 시스템은 엔드 이펙터 자세나 루트 속도와 같은 수작업으로 설계된 동작 "어휘"를 가진 정확한 저수준 제어기를 가정합니다. 이러한 가정은 이전 연구를 준정적 작업으로 제한하며, 휴머노이드 전신 제어(WBC) 작업에 필요한 민첩한 전신 동작을 배제합니다. 문헌에서의 이러한 격차를 해소하기 위해, 우리는 먼저 10개 카테고리의 150개 이상의 작업으로 구성된 휴머노이드 WBC를 위한 최초의 시뮬레이션-실제 전환 가능, 비전-언어, 폐루프 벤치마크를 소개합니다. 그런 다음, 우리는 LeVERB: 잠재 비전-언어 인코딩 로봇 동작(Latent Vision-Language-Encoded Robot Behavior)을 제안합니다. 이는 휴머노이드 비전-언어 WBC를 위한 계층적 잠재 명령 추종 프레임워크로, 최초의 사례입니다. 상위 수준에서는 비전-언어 정책이 합성적으로 렌더링된 운동학적 데모에서 잠재 동작 어휘를 학습하고, 하위 수준에서는 강화 학습된 WBC 정책이 이러한 잠재 동사를 사용하여 동역학 수준 명령을 생성합니다. 우리의 벤치마크에서 LeVERB는 단순한 시각적 내비게이션 작업에서 제로샷으로 80%의 성공률을 달성하고, 전체적으로 58.5%의 성공률을 기록하여, 순진한 계층적 전신 VLA 구현보다 7.8배 더 뛰어난 성능을 보였습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 강력한 의미 이해와 제로샷 일반화 능력을 보여주었지만, 대부분의 기존 시스템은 엔드 이펙터 자세나 루트 속도와 같은 수작업으로 설계된 동작 "어휘"를 가진 정확한 저수준 제어기를 가정합니다. 이러한 가정은 이전 연구를 준정적 작업으로 제한하며, 휴머노이드 전신 제어(WBC) 작업에 필요한 민첩한 전신 동작을 배제합니다. 문헌에서의 이러한 격차를 해소하기 위해, 우리는 먼저 10개 카테고리의 150개 이상의 작업으로 구성된 휴머노이드 WBC를 위한 최초의 시뮬레이션-실제 전환 가능, 비전-언어, 폐루프 벤치마크를 소개합니다. 그런 다음, 우리는 LeVERB: 잠재 비전-언어 인코딩 로봇 동작(Latent Vision-Language-Encoded Robot Behavior)을 제안합니다. 이는 휴머노이드 비전-언어 WBC를 위한 계층적 잠재 명령 추종 프레임워크로, 최초의 사례입니다. 상위 수준에서는 비전-언어 정책이 합성적으로 렌더링된 운동학적 데모에서 잠재 동작 어휘를 학습하고, 하위 수준에서는 강화 학습된 WBC 정책이 이러한 잠재 동사를 사용하여 동역학 수준 명령을 생성합니다. 우리의 벤치마크에서 LeVERB는 단순한 시각적 내비게이션 작업에서 제로샷으로 80%의 성공률을 달성하고, 전체적으로 58.5%의 성공률을 기록하여, 순진한 계층적 전신 VLA 구현보다 7.8배 더 뛰어난 성능을 보였습니다.
