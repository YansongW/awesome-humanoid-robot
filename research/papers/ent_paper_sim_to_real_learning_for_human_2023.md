---
$id: ent_paper_sim_to_real_learning_for_human_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
  zh: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
  ko: Sim-to-Real Learning for Humanoid Box Loco-Manipulation
summary:
  en: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
  zh: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
  ko: Sim-to-Real Learning for Humanoid Box Loco-Manipulation is a 2023 work on loco-manipulation and whole-body-control for
    humanoid robots.
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
- loco_manipulation
- sim_to_real_learning_for_human
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2310.03191v1.
sources:
- id: src_001
  type: paper
  title: Sim-to-Real Learning for Humanoid Box Loco-Manipulation (arXiv)
  url: https://arxiv.org/abs/2310.03191
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## 核心内容
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## 参考
- http://arxiv.org/abs/2310.03191v1

## Overview
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## Content
In this work we propose a learning-based approach to box loco-manipulation for a humanoid robot. This is a particularly challenging problem due to the need for whole-body coordination in order to lift boxes of varying weight, position, and orientation while maintaining balance. To address this challenge, we present a sim-to-real reinforcement learning approach for training general box pickup and carrying skills for the bipedal robot Digit. Our reward functions are designed to produce the desired interactions with the box while also valuing balance and gait quality. We combine the learned skills into a full system for box loco-manipulation to achieve the task of moving boxes from one table to another with a variety of sizes, weights, and initial configurations. In addition to quantitative simulation results, we demonstrate successful sim-to-real transfer on the humanoid r

## 개요
본 연구에서는 휴머노이드 로봇의 박스 이동 조작을 위한 학습 기반 접근법을 제안합니다. 이는 다양한 무게, 위치, 방향의 박스를 들어 올리면서 균형을 유지하기 위해 전신 협응이 필요하다는 점에서 특히 어려운 문제입니다. 이러한 과제를 해결하기 위해, 우리는 이족 보행 로봇 Digit을 위한 일반적인 박스 집기 및 운반 기술을 훈련하는 시뮬레이션-실제 강화 학습 접근법을 제시합니다. 보상 함수는 박스와의 원하는 상호작용을 유도하면서 균형과 보행 품질을 중시하도록 설계되었습니다. 학습된 기술을 결합하여 다양한 크기, 무게, 초기 구성의 박스를 한 테이블에서 다른 테이블로 옮기는 작업을 수행하는 완전한 박스 이동 조작 시스템을 구축합니다. 정량적 시뮬레이션 결과 외에도, 휴머노이드 로봇에서 성공적인 시뮬레이션-실제 전이를 시연합니다.

## 핵심 내용
본 연구에서는 휴머노이드 로봇의 박스 이동 조작을 위한 학습 기반 접근법을 제안합니다. 이는 다양한 무게, 위치, 방향의 박스를 들어 올리면서 균형을 유지하기 위해 전신 협응이 필요하다는 점에서 특히 어려운 문제입니다. 이러한 과제를 해결하기 위해, 우리는 이족 보행 로봇 Digit을 위한 일반적인 박스 집기 및 운반 기술을 훈련하는 시뮬레이션-실제 강화 학습 접근법을 제시합니다. 보상 함수는 박스와의 원하는 상호작용을 유도하면서 균형과 보행 품질을 중시하도록 설계되었습니다. 학습된 기술을 결합하여 다양한 크기, 무게, 초기 구성의 박스를 한 테이블에서 다른 테이블로 옮기는 작업을 수행하는 완전한 박스 이동 조작 시스템을 구축합니다. 정량적 시뮬레이션 결과 외에도, 휴머노이드 로봇에서 성공적인 시뮬레이션-실제 전이를 시연합니다.
