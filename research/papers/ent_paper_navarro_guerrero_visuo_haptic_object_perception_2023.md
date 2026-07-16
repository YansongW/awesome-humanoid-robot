---
$id: ent_paper_navarro_guerrero_visuo_haptic_object_perception_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Visuo-Haptic Object Perception for Robots: An Overview'
  zh: 机器人视触觉物体感知综述
  ko: 로봇을 위한 시각-촉각 물체 인식 개요
summary:
  en: This 2023 survey reviews the integration of visual and haptic sensing for robotic object perception, covering biological
    inspiration, sensor technologies, datasets, multimodal learning challenges, and applications in recognition, peripersonal
    space representation, and manipulation.
  zh: The object perception capabilities of humans are impressive, and this becomes even more evident when trying to develop
    solutions with a similar proficiency in autonomous robots. While there have been notable advancements in the technologies
    for artificial vision and touch, the effective integration of these two sensory modalities in robotic applications still
    needs to be improved, and several open challenges exist. Taking inspiration from how humans combine visual and haptic
    perception to perceive object properties and drive the execution of manual tasks, this article summarises the current
    st
  ko: 이 2023년 설문조사는 로봇 물체 인식을 위한 시각 및 촉각 감각 통합을 검토하며, 생물학적 영감, 센서 기술, 데이터셋, 다중모달 학습 과제, 인식, 근거리 공간 표현, 조작 응용 분야를 다룬다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- visuo_haptic_perception
- multimodal_learning
- tactile_sensing
- object_recognition
- manipulation
- robot_perception
- sensor_fusion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.11544v3.
sources:
- id: src_001
  type: paper
  title: 'Visuo-Haptic Object Perception for Robots: An Overview'
  url: https://arxiv.org/abs/2203.11544
  date: '2023'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## 概述
The object perception capabilities of humans are impressive, and this becomes even more evident when trying to develop solutions with a similar proficiency in autonomous robots. While there have been notable advancements in the technologies for artificial vision and touch, the effective integration of these two sensory modalities in robotic applications still needs to be improved, and several open challenges exist. Taking inspiration from how humans combine visual and haptic perception to perceive object properties and drive the execution of manual tasks, this article summarises the current state of the art of visuo-haptic object perception in robots. Firstly, the biological basis of human multimodal object perception is outlined. Then, the latest advances in sensing technologies and data collection strategies for robots are discussed. Next, an overview of the main computational techniques is presented, highlighting the main challenges of multimodal machine learning and presenting a few representative articles in the areas of robotic object recognition, peripersonal space representation and manipulation. Finally, informed by the latest advancements and open challenges, this article outlines promising new research directions.

## 核心内容
The object perception capabilities of humans are impressive, and this becomes even more evident when trying to develop solutions with a similar proficiency in autonomous robots. While there have been notable advancements in the technologies for artificial vision and touch, the effective integration of these two sensory modalities in robotic applications still needs to be improved, and several open challenges exist. Taking inspiration from how humans combine visual and haptic perception to perceive object properties and drive the execution of manual tasks, this article summarises the current state of the art of visuo-haptic object perception in robots. Firstly, the biological basis of human multimodal object perception is outlined. Then, the latest advances in sensing technologies and data collection strategies for robots are discussed. Next, an overview of the main computational techniques is presented, highlighting the main challenges of multimodal machine learning and presenting a few representative articles in the areas of robotic object recognition, peripersonal space representation and manipulation. Finally, informed by the latest advancements and open challenges, this article outlines promising new research directions.

## 参考
- http://arxiv.org/abs/2203.11544v3

## Overview
The object perception capabilities of humans are impressive, and this becomes even more evident when trying to develop solutions with a similar proficiency in autonomous robots. While there have been notable advancements in the technologies for artificial vision and touch, the effective integration of these two sensory modalities in robotic applications still needs to be improved, and several open challenges exist. Taking inspiration from how humans combine visual and haptic perception to perceive object properties and drive the execution of manual tasks, this article summarises the current state of the art of visuo-haptic object perception in robots. Firstly, the biological basis of human multimodal object perception is outlined. Then, the latest advances in sensing technologies and data collection strategies for robots are discussed. Next, an overview of the main computational techniques is presented, highlighting the main challenges of multimodal machine learning and presenting a few representative articles in the areas of robotic object recognition, peripersonal space representation and manipulation. Finally, informed by the latest advancements and open challenges, this article outlines promising new research directions.

## Content
The object perception capabilities of humans are impressive, and this becomes even more evident when trying to develop solutions with a similar proficiency in autonomous robots. While there have been notable advancements in the technologies for artificial vision and touch, the effective integration of these two sensory modalities in robotic applications still needs to be improved, and several open challenges exist. Taking inspiration from how humans combine visual and haptic perception to perceive object properties and drive the execution of manual tasks, this article summarises the current state of the art of visuo-haptic object perception in robots. Firstly, the biological basis of human multimodal object perception is outlined. Then, the latest advances in sensing technologies and data collection strategies for robots are discussed. Next, an overview of the main computational techniques is presented, highlighting the main challenges of multimodal machine learning and presenting a few representative articles in the areas of robotic object recognition, peripersonal space representation and manipulation. Finally, informed by the latest advancements and open challenges, this article outlines promising new research directions.

## 개요
인간의 객체 인식 능력은 놀라우며, 자율 로봇에서 이와 유사한 수준의 솔루션을 개발하려 할 때 그 중요성이 더욱 부각됩니다. 인공 시각 및 촉각 기술에서는 눈에 띄는 발전이 있었지만, 로봇 응용 분야에서 이 두 감각 양식을 효과적으로 통합하는 것은 여전히 개선이 필요하며 여러 미해결 과제가 존재합니다. 인간이 시각과 촉각 인식을 결합하여 객체 속성을 인지하고 수동 작업을 수행하는 방식에서 영감을 받아, 본 논문은 로봇의 시각-촉각 객체 인식에 관한 최신 연구 동향을 요약합니다. 먼저 인간의 다중 감각 객체 인식의 생물학적 기반을 개괄합니다. 그런 다음 로봇을 위한 센싱 기술 및 데이터 수집 전략의 최신 발전을 논의합니다. 이어서 주요 계산 기법의 개요를 제시하며, 다중 감각 머신러닝의 주요 과제를 강조하고 로봇 객체 인식, 주변 공간 표현 및 조작 분야의 대표적인 연구 사례를 소개합니다. 마지막으로 최신 발전과 미해결 과제를 바탕으로 유망한 새로운 연구 방향을 제시합니다.

## 핵심 내용
인간의 객체 인식 능력은 놀라우며, 자율 로봇에서 이와 유사한 수준의 솔루션을 개발하려 할 때 그 중요성이 더욱 부각됩니다. 인공 시각 및 촉각 기술에서는 눈에 띄는 발전이 있었지만, 로봇 응용 분야에서 이 두 감각 양식을 효과적으로 통합하는 것은 여전히 개선이 필요하며 여러 미해결 과제가 존재합니다. 인간이 시각과 촉각 인식을 결합하여 객체 속성을 인지하고 수동 작업을 수행하는 방식에서 영감을 받아, 본 논문은 로봇의 시각-촉각 객체 인식에 관한 최신 연구 동향을 요약합니다. 먼저 인간의 다중 감각 객체 인식의 생물학적 기반을 개괄합니다. 그런 다음 로봇을 위한 센싱 기술 및 데이터 수집 전략의 최신 발전을 논의합니다. 이어서 주요 계산 기법의 개요를 제시하며, 다중 감각 머신러닝의 주요 과제를 강조하고 로봇 객체 인식, 주변 공간 표현 및 조작 분야의 대표적인 연구 사례를 소개합니다. 마지막으로 최신 발전과 미해결 과제를 바탕으로 유망한 새로운 연구 방향을 제시합니다.
