---
$id: ent_paper_yuan_robopoint_a_vision_language_mo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics'
  zh: RoboPoint
  ko: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics'
summary:
  en: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
  zh: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
  ko: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robopoint
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10721v1.
sources:
- id: src_001
  type: paper
  title: RoboPoint source
  url: https://proceedings.mlr.press/v270/yuan25c.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## 核心内容
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## 参考
- http://arxiv.org/abs/2406.10721v1

## Overview
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## Content
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## 개요
테이블 위의 물체를 재배열하는 것부터 식료품을 선반에 올리는 것까지, 로봇은 작업을 정확하고 신뢰성 있게 수행하기 위해 정밀한 동작 지점을 계획해야 합니다. 최근 로봇 행동 제어를 위해 시각-언어 모델(VLM)이 도입되었지만, VLM은 언어를 사용하여 로봇 동작을 정밀하게 표현하는 데 어려움을 겪습니다. 우리는 VLM을 로봇 도메인과 요구 사항에 맞게 명령어 튜닝하는 자동 합성 데이터 생성 파이프라인을 소개합니다. 이 파이프라인을 사용하여 언어 명령어가 주어졌을 때 이미지의 키포인트 어포던스를 예측하는 VLM인 RoboPoint를 훈련합니다. 대안 접근법과 비교하여, 우리의 방법은 실제 세계 데이터 수집이나 인간 시연이 필요하지 않아 다양한 환경과 시점으로 확장성이 훨씬 뛰어납니다. 또한 RoboPoint는 로봇 내비게이션, 조작, 증강 현실(AR) 지원과 같은 여러 하위 응용 프로그램을 가능하게 하는 일반 모델입니다. 실험 결과, RoboPoint는 공간 어포던스 예측 정확도에서 최신 VLM(GPT-4o) 및 시각적 프롬프트 기술(PIVOT)보다 21.8%, 하위 작업 성공률에서 30.5% 더 우수한 성능을 보였습니다. 프로젝트 웹사이트: https://robo-point.github.io.

## 핵심 내용
테이블 위의 물체를 재배열하는 것부터 식료품을 선반에 올리는 것까지, 로봇은 작업을 정확하고 신뢰성 있게 수행하기 위해 정밀한 동작 지점을 계획해야 합니다. 최근 로봇 행동 제어를 위해 시각-언어 모델(VLM)이 도입되었지만, VLM은 언어를 사용하여 로봇 동작을 정밀하게 표현하는 데 어려움을 겪습니다. 우리는 VLM을 로봇 도메인과 요구 사항에 맞게 명령어 튜닝하는 자동 합성 데이터 생성 파이프라인을 소개합니다. 이 파이프라인을 사용하여 언어 명령어가 주어졌을 때 이미지의 키포인트 어포던스를 예측하는 VLM인 RoboPoint를 훈련합니다. 대안 접근법과 비교하여, 우리의 방법은 실제 세계 데이터 수집이나 인간 시연이 필요하지 않아 다양한 환경과 시점으로 확장성이 훨씬 뛰어납니다. 또한 RoboPoint는 로봇 내비게이션, 조작, 증강 현실(AR) 지원과 같은 여러 하위 응용 프로그램을 가능하게 하는 일반 모델입니다. 실험 결과, RoboPoint는 공간 어포던스 예측 정확도에서 최신 VLM(GPT-4o) 및 시각적 프롬프트 기술(PIVOT)보다 21.8%, 하위 작업 성공률에서 30.5% 더 우수한 성능을 보였습니다. 프로젝트 웹사이트: https://robo-point.github.io.
