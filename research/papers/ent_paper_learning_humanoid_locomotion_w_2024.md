---
$id: ent_paper_learning_humanoid_locomotion_w_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion with Perceptive Internal Model
  zh: Learning Humanoid Locomotion with Perceptive Internal Model
  ko: Learning Humanoid Locomotion with Perceptive Internal Model
summary:
  en: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
  zh: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
  ko: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_humanoid_locomotion_w
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.14386v1.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion with Perceptive Internal Model (arXiv)
  url: https://arxiv.org/abs/2411.14386
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## 核心内容
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## 参考
- http://arxiv.org/abs/2411.14386v1

## Overview
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## Content
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## 개요
사족 보행 로봇이 "블라인드" 정책을 사용하여 다양한 지형을 탐색할 수 있는 것과 달리, 휴머노이드 로봇은 높은 자유도와 본질적으로 불안정한 형태로 인해 안정적인 보행을 위해 정확한 인식이 필요합니다. 그러나 인식 신호를 통합하면 시스템에 추가적인 교란이 발생하여 견고성, 일반화 가능성 및 효율성이 저하될 수 있습니다. 본 논문에서는 로봇 주변을 중심으로 지속적으로 업데이트되는 탑재 고도 지도에 의존하여 주변 환경을 인식하는 Perceptive Internal Model (PIM)을 제시합니다. 우리는 시뮬레이션에서 로봇 주변의 실제 장애물 높이를 사용하여 정책을 훈련하고, Hybrid Internal Model (HIM)을 기반으로 최적화하며, 구축된 고도 지도에서 샘플링된 높이로 추론을 수행합니다. 깊이 맵이나 원시 포인트 클라우드를 직접 인코딩하는 이전 방법과 달리, 우리의 접근 방식은 로봇이 발 아래의 지형을 명확하게 인식할 수 있게 하며 카메라 움직임이나 노이즈의 영향을 덜 받습니다. 또한 시뮬레이션에서 깊이 맵 렌더링이 필요하지 않기 때문에, 우리의 방법은 최소한의 추가 계산 비용만을 도입하며 RTX 4090 GPU에서 3시간 만에 정책을 훈련할 수 있습니다. 우리는 다양한 휴머노이드 로봇, 다양한 실내외 지형, 계단 및 다양한 센서 구성에서 우리 방법의 효과를 검증합니다. 우리의 방법은 휴머노이드 로봇이 계단을 지속적으로 오를 수 있게 하며, 미래 휴머노이드 제어 방법 개발을 위한 기초 알고리즘으로서의 잠재력을 가지고 있습니다.

## 핵심 내용
사족 보행 로봇이 "블라인드" 정책을 사용하여 다양한 지형을 탐색할 수 있는 것과 달리, 휴머노이드 로봇은 높은 자유도와 본질적으로 불안정한 형태로 인해 안정적인 보행을 위해 정확한 인식이 필요합니다. 그러나 인식 신호를 통합하면 시스템에 추가적인 교란이 발생하여 견고성, 일반화 가능성 및 효율성이 저하될 수 있습니다. 본 논문에서는 로봇 주변을 중심으로 지속적으로 업데이트되는 탑재 고도 지도에 의존하여 주변 환경을 인식하는 Perceptive Internal Model (PIM)을 제시합니다. 우리는 시뮬레이션에서 로봇 주변의 실제 장애물 높이를 사용하여 정책을 훈련하고, Hybrid Internal Model (HIM)을 기반으로 최적화하며, 구축된 고도 지도에서 샘플링된 높이로 추론을 수행합니다. 깊이 맵이나 원시 포인트 클라우드를 직접 인코딩하는 이전 방법과 달리, 우리의 접근 방식은 로봇이 발 아래의 지형을 명확하게 인식할 수 있게 하며 카메라 움직임이나 노이즈의 영향을 덜 받습니다. 또한 시뮬레이션에서 깊이 맵 렌더링이 필요하지 않기 때문에, 우리의 방법은 최소한의 추가 계산 비용만을 도입하며 RTX 4090 GPU에서 3시간 만에 정책을 훈련할 수 있습니다. 우리는 다양한 휴머노이드 로봇, 다양한 실내외 지형, 계단 및 다양한 센서 구성에서 우리 방법의 효과를 검증합니다. 우리의 방법은 휴머노이드 로봇이 계단을 지속적으로 오를 수 있게 하며, 미래 휴머노이드 제어 방법 개발을 위한 기초 알고리즘으로서의 잠재력을 가지고 있습니다.
