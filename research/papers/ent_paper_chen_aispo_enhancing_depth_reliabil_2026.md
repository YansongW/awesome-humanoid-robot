---
$id: ent_paper_chen_aispo_enhancing_depth_reliabil_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian Objects via Affine-Invariant Shape Prior'
  zh: AISPO：基于仿射不变形状先验的非朗伯物体机器人操作深度可靠性增强
  ko: 'AISPO: 아핀 불변 형상 사전을 활용한 비람베르티안 객체 로봇 조작을 위한 깊이 신뢰성 강화'
summary:
  en: AISPO is a depth completion framework that fuses multi-scale RGB-D features with an affine-invariant shape prior to
    improve depth reliability for robotic manipulation of transparent and specular objects.
  zh: Reliable depth perception is critical for robotic manipulation, especially for non-Lambertian objects such as transparent
    or highly specular surfaces, where raw depth measurements are often corrupted or missing. These failures frequently propagate
    to motion planning, resulting in invalid grasp poses and execution errors. We propose AISPO, a depth completion framework
    that improves depth reliability for manipulation in challenging sensing conditions. AISPO combines multi-scale RGB-D feature
    fusion with an affine-invariant shape prior to enforce geometric consistency and mitigate catastrophic de
  ko: AISPO는 다중 스케일 RGB-D 특징과 아핀 불변 형상 사전을 융합하여 투명하거나 반사성이 강한 비람베르티안 객체의 로봇 조작을 위한 깊이 신뢰성을 향상시키는 깊이 완성 프레임워크이다.
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
- depth_completion
- rgb_d_fusion
- non_lambertian_objects
- transparent_objects
- specular_objects
- robotic_grasping
- affine_invariant_shape_prior
- vision_transformer
- perception
- synthetic_training
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.25503v1.
sources:
- id: src_001
  type: paper
  title: 'AISPO: Enhancing Depth Reliability for Robotic Manipulation of Non-Lambertian Objects via Affine-Invariant Shape
    Prior'
  url: https://arxiv.org/abs/2606.25503
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
Reliable depth perception is critical for robotic manipulation, especially for non-Lambertian objects such as transparent or highly specular surfaces, where raw depth measurements are often corrupted or missing. These failures frequently propagate to motion planning, resulting in invalid grasp poses and execution errors. We propose AISPO, a depth completion framework that improves depth reliability for manipulation in challenging sensing conditions. AISPO combines multi-scale RGB-D feature fusion with an affine-invariant shape prior to enforce geometric consistency and mitigate catastrophic depth failures. Unlike methods that focus primarily on average depth accuracy, our approach emphasizes physical plausibility and structural integrity of the predicted depth maps. Extensive benchmark evaluations demonstrate competitive performance and strong generalization to unseen objects and novel scenes. Real-world grasping experiments further show that enhanced depth reliability significantly improves manipulation success rates, particularly for transparent objects where many existing methods fail to produce physically usable depth estimates.

## 核心内容
Reliable depth perception is critical for robotic manipulation, especially for non-Lambertian objects such as transparent or highly specular surfaces, where raw depth measurements are often corrupted or missing. These failures frequently propagate to motion planning, resulting in invalid grasp poses and execution errors. We propose AISPO, a depth completion framework that improves depth reliability for manipulation in challenging sensing conditions. AISPO combines multi-scale RGB-D feature fusion with an affine-invariant shape prior to enforce geometric consistency and mitigate catastrophic depth failures. Unlike methods that focus primarily on average depth accuracy, our approach emphasizes physical plausibility and structural integrity of the predicted depth maps. Extensive benchmark evaluations demonstrate competitive performance and strong generalization to unseen objects and novel scenes. Real-world grasping experiments further show that enhanced depth reliability significantly improves manipulation success rates, particularly for transparent objects where many existing methods fail to produce physically usable depth estimates.

## 参考
- http://arxiv.org/abs/2606.25503v1

## Overview
Reliable depth perception is critical for robotic manipulation, especially for non-Lambertian objects such as transparent or highly specular surfaces, where raw depth measurements are often corrupted or missing. These failures frequently propagate to motion planning, resulting in invalid grasp poses and execution errors. We propose AISPO, a depth completion framework that improves depth reliability for manipulation in challenging sensing conditions. AISPO combines multi-scale RGB-D feature fusion with an affine-invariant shape prior to enforce geometric consistency and mitigate catastrophic depth failures. Unlike methods that focus primarily on average depth accuracy, our approach emphasizes physical plausibility and structural integrity of the predicted depth maps. Extensive benchmark evaluations demonstrate competitive performance and strong generalization to unseen objects and novel scenes. Real-world grasping experiments further show that enhanced depth reliability significantly improves manipulation success rates, particularly for transparent objects where many existing methods fail to produce physically usable depth estimates.

## Content
Reliable depth perception is critical for robotic manipulation, especially for non-Lambertian objects such as transparent or highly specular surfaces, where raw depth measurements are often corrupted or missing. These failures frequently propagate to motion planning, resulting in invalid grasp poses and execution errors. We propose AISPO, a depth completion framework that improves depth reliability for manipulation in challenging sensing conditions. AISPO combines multi-scale RGB-D feature fusion with an affine-invariant shape prior to enforce geometric consistency and mitigate catastrophic depth failures. Unlike methods that focus primarily on average depth accuracy, our approach emphasizes physical plausibility and structural integrity of the predicted depth maps. Extensive benchmark evaluations demonstrate competitive performance and strong generalization to unseen objects and novel scenes. Real-world grasping experiments further show that enhanced depth reliability significantly improves manipulation success rates, particularly for transparent objects where many existing methods fail to produce physically usable depth estimates.

## 개요
신뢰할 수 있는 깊이 인식은 로봇 조작, 특히 투명하거나 반사율이 높은 표면과 같은 비-람베르트 객체에서 중요하며, 이러한 경우 원시 깊이 측정값이 종종 손상되거나 누락됩니다. 이러한 실패는 종종 운동 계획으로 전파되어 잘못된 파지 자세와 실행 오류를 초래합니다. 본 논문에서는 까다로운 감지 조건에서 조작을 위한 깊이 신뢰성을 향상시키는 깊이 완성 프레임워크인 AISPO를 제안합니다. AISPO는 다중 스케일 RGB-D 특징 융합과 아핀 불변 형상 사전을 결합하여 기하학적 일관성을 강화하고 치명적인 깊이 오류를 완화합니다. 평균 깊이 정확도에 주로 초점을 맞춘 방법과 달리, 우리의 접근 방식은 예측된 깊이 맵의 물리적 타당성과 구조적 무결성을 강조합니다. 광범위한 벤치마크 평가는 경쟁력 있는 성능과 보이지 않는 객체 및 새로운 장면에 대한 강력한 일반화를 입증합니다. 실제 파지 실험은 향상된 깊이 신뢰성이 조작 성공률을 크게 향상시킴을 추가로 보여주며, 특히 많은 기존 방법이 물리적으로 사용 가능한 깊이 추정치를 생성하지 못하는 투명 객체에서 두드러집니다.

## 핵심 내용
신뢰할 수 있는 깊이 인식은 로봇 조작, 특히 투명하거나 반사율이 높은 표면과 같은 비-람베르트 객체에서 중요하며, 이러한 경우 원시 깊이 측정값이 종종 손상되거나 누락됩니다. 이러한 실패는 종종 운동 계획으로 전파되어 잘못된 파지 자세와 실행 오류를 초래합니다. 본 논문에서는 까다로운 감지 조건에서 조작을 위한 깊이 신뢰성을 향상시키는 깊이 완성 프레임워크인 AISPO를 제안합니다. AISPO는 다중 스케일 RGB-D 특징 융합과 아핀 불변 형상 사전을 결합하여 기하학적 일관성을 강화하고 치명적인 깊이 오류를 완화합니다. 평균 깊이 정확도에 주로 초점을 맞춘 방법과 달리, 우리의 접근 방식은 예측된 깊이 맵의 물리적 타당성과 구조적 무결성을 강조합니다. 광범위한 벤치마크 평가는 경쟁력 있는 성능과 보이지 않는 객체 및 새로운 장면에 대한 강력한 일반화를 입증합니다. 실제 파지 실험은 향상된 깊이 신뢰성이 조작 성공률을 크게 향상시킴을 추가로 보여주며, 특히 많은 기존 방법이 물리적으로 사용 가능한 깊이 추정치를 생성하지 못하는 투명 객체에서 두드러집니다.
