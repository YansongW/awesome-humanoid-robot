---
$id: ent_paper_okami_teaching_humanoid_robots_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
  zh: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
  ko: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation'
summary:
  en: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
    humanoid robots.'
  zh: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
    humanoid robots.'
  ko: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation is a 2024 work on manipulation for
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
- humanoid
- manipulation
- okami
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.11792v1.
sources:
- id: src_001
  type: paper
  title: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation (arXiv)'
  url: https://arxiv.org/abs/2410.11792
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'OKAMI: Teaching Humanoid Robots Manipulation Skills through Single Video Imitation project page'
  url: https://ut-austin-rpl.github.io/OKAMI/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## 核心内容
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## 参考
- http://arxiv.org/abs/2410.11792v1

## Overview
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## Content
We study the problem of teaching humanoid robots manipulation skills by imitating from single video demonstrations. We introduce OKAMI, a method that generates a manipulation plan from a single RGB-D video and derives a policy for execution. At the heart of our approach is object-aware retargeting, which enables the humanoid robot to mimic the human motions in an RGB-D video while adjusting to different object locations during deployment. OKAMI uses open-world vision models to identify task-relevant objects and retarget the body motions and hand poses separately. Our experiments show that OKAMI achieves strong generalizations across varying visual and spatial conditions, outperforming the state-of-the-art baseline on open-world imitation from observation. Furthermore, OKAMI rollout trajectories are leveraged to train closed-loop visuomotor policies, which achieve an average success rate of 79.2% without the need for labor-intensive teleoperation. More videos can be found on our website https://ut-austin-rpl.github.io/OKAMI/.

## 개요
본 연구는 단일 비디오 시연을 모방하여 휴머노이드 로봇의 조작 기술을 가르치는 문제를 다룹니다. 우리는 단일 RGB-D 비디오로부터 조작 계획을 생성하고 실행 정책을 도출하는 방법인 OKAMI를 소개합니다. 이 접근법의 핵심은 객체 인식 리타겟팅(object-aware retargeting)으로, 휴머노이드 로봇이 RGB-D 비디오 속 인간의 동작을 모방하면서도 배치 시 다른 객체 위치에 적응할 수 있게 합니다. OKAMI는 개방형 세계 비전 모델(open-world vision models)을 사용하여 작업 관련 객체를 식별하고, 신체 동작과 손 자세를 별도로 리타겟팅합니다. 실험 결과, OKAMI는 다양한 시각적 및 공간적 조건에서 강력한 일반화 능력을 보여주며, 관찰로부터의 개방형 세계 모방(open-world imitation from observation)에서 최첨단 기준선(state-of-the-art baseline)을 능가합니다. 또한, OKAMI 롤아웃 궤적을 활용하여 폐쇄 루프 시각운동 정책(closed-loop visuomotor policies)을 훈련하며, 이는 노동 집약적인 원격 조작 없이 평균 성공률 79.2%를 달성합니다. 더 많은 비디오는 당사 웹사이트 https://ut-austin-rpl.github.io/OKAMI/에서 확인할 수 있습니다.

## 핵심 내용
본 연구는 단일 비디오 시연을 모방하여 휴머노이드 로봇의 조작 기술을 가르치는 문제를 다룹니다. 우리는 단일 RGB-D 비디오로부터 조작 계획을 생성하고 실행 정책을 도출하는 방법인 OKAMI를 소개합니다. 이 접근법의 핵심은 객체 인식 리타겟팅(object-aware retargeting)으로, 휴머노이드 로봇이 RGB-D 비디오 속 인간의 동작을 모방하면서도 배치 시 다른 객체 위치에 적응할 수 있게 합니다. OKAMI는 개방형 세계 비전 모델(open-world vision models)을 사용하여 작업 관련 객체를 식별하고, 신체 동작과 손 자세를 별도로 리타겟팅합니다. 실험 결과, OKAMI는 다양한 시각적 및 공간적 조건에서 강력한 일반화 능력을 보여주며, 관찰로부터의 개방형 세계 모방(open-world imitation from observation)에서 최첨단 기준선(state-of-the-art baseline)을 능가합니다. 또한, OKAMI 롤아웃 궤적을 활용하여 폐쇄 루프 시각운동 정책(closed-loop visuomotor policies)을 훈련하며, 이는 노동 집약적인 원격 조작 없이 평균 성공률 79.2%를 달성합니다. 더 많은 비디오는 당사 웹사이트 https://ut-austin-rpl.github.io/OKAMI/에서 확인할 수 있습니다.
