---
$id: ent_paper_armor_egocentric_perception_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning'
  zh: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning'
  ko: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning'
summary:
  en: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning is a 2024 work on navigation
    for humanoid robots.'
  zh: ARMOR 是 2024 年提出的一种面向人形机器人的自我中心感知系统，由团队通过软硬件集成开发。其核心贡献在于采用分布式感知方案增强空间意识，并结合基于 Transformer 的模仿学习策略实现动态避障，在仿真和真实机器人上均显著优于传统多摄像头方案。
  ko: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning is a 2024 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- armor
- humanoid
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.00396v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'ARMOR: Egocentric Perception for Humanoid Robot Collision Avoidance and Motion Planning (arXiv)'
  url: https://arxiv.org/abs/2412.00396
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人在密集环境中的运动规划常受限于感知能力的不足。ARMOR 系统通过集成类似可穿戴设备的深度传感器，以分布式方式提升机器人的空间感知能力，从而支持更敏捷的运动规划。研究团队利用 AMASS 数据集中的约 86 小时人类真实运动数据，在仿真中训练了一个基于 Transformer 的模仿学习策略，用于动态碰撞避免。实验表明，ARMOR 相比多个头戴式和外置深度摄像头的组合方案，碰撞次数减少 63.7%，成功率提升 78.7%；其模仿学习策略相比基于采样的运动规划专家 cuRobo，碰撞减少 31.6%，成功率提高 16.9%，计算延迟降低 26 倍。该系统已在 Fourier Intelligence 的 GR1 人形机器人上完成真实部署。

## 核心内容
### 方法
- **感知系统设计**：ARMOR 采用分布式感知架构，在机器人身体关键位置集成类似可穿戴设备的深度传感器，以弥补传统头戴式或外置摄像头在密集环境中的感知盲区。
- **运动规划与避障**：基于 Transformer 的模仿学习策略在仿真环境中训练，训练数据来自 AMASS 数据集中的约 86 小时人类真实运动数据，使机器人能够学习动态避障行为。

### 实验设置与关键结果
- **对比基准**：与多组密集头戴式和外置深度摄像头方案对比，ARMOR 实现：
  - 碰撞次数减少 63.7%
  - 成功率提升 78.7%
- **策略对比**：与基于采样的运动规划专家 cuRobo 对比，ARMOR 的模仿学习策略实现：
  - 碰撞减少 31.6%
  - 成功率提高 16.9%
  - 计算延迟降低 26 倍
- **真实部署**：系统已在 Fourier Intelligence 的 GR1 人形机器人上完成部署验证。

### 结论
ARMOR 通过软硬件协同的自我中心感知方案，显著提升了人形机器人在密集环境中的避障与运动规划能力，并在仿真和真实场景中均展现出优于传统方法的性能。

## Overview
Humanoid robots have significant gaps in their sensing and perception, making it hard to perform motion planning in dense environments. To address this, we introduce ARMOR, a novel egocentric perception system that integrates both hardware and software, specifically incorporating wearable-like depth sensors for humanoid robots. Our distributed perception approach enhances the robot's spatial awareness, and facilitates more agile motion planning. We also train a transformer-based imitation learning (IL) policy in simulation to perform dynamic collision avoidance, by leveraging around 86 hours worth of human realistic motions from the AMASS dataset. We show that our ARMOR perception is superior against a setup with multiple dense head-mounted, and externally mounted depth cameras, with a 63.7% reduction in collisions, and 78.7% improvement on success rate. We also compare our IL policy against a sampling-based motion planning expert cuRobo, showing 31.6% less collisions, 16.9% higher success rate, and 26x reduction in computational latency. Lastly, we deploy our ARMOR perception on our real-world GR1 humanoid from Fourier Intelligence. We are going to update the link to the source code, HW description, and 3D CAD files in the arXiv version of this text.

## 개요
휴머노이드 로봇은 감지 및 인식에 상당한 격차가 있어 밀집된 환경에서 동작 계획을 수행하기 어렵습니다. 이를 해결하기 위해, 우리는 하드웨어와 소프트웨어를 통합한 새로운 자기중심적 인식 시스템인 ARMOR를 소개하며, 특히 휴머노이드 로봇을 위한 웨어러블 형태의 깊이 센서를 포함합니다. 분산 인식 접근 방식은 로봇의 공간 인식을 향상시키고 더 민첩한 동작 계획을 용이하게 합니다. 또한, AMASS 데이터셋의 약 86시간 분량의 인간 사실적 동작을 활용하여 시뮬레이션에서 트랜스포머 기반 모방 학습(IL) 정책을 훈련하여 동적 충돌 회피를 수행합니다. 우리는 ARMOR 인식이 다수의 밀집된 머리 장착형 및 외부 장착형 깊이 카메라 설정보다 우수함을 보여주며, 충돌 63.7% 감소, 성공률 78.7% 향상을 달성했습니다. 또한, IL 정책을 샘플링 기반 동작 계획 전문가인 cuRobo와 비교하여 충돌 31.6% 감소, 성공률 16.9% 향상, 계산 지연 시간 26배 감소를 보여줍니다. 마지막으로, 우리는 Fourier Intelligence의 실제 GR1 휴머노이드에 ARMOR 인식을 배포합니다. 소스 코드, 하드웨어 설명 및 3D CAD 파일에 대한 링크는 이 텍스트의 arXiv 버전에서 업데이트할 예정입니다.

## 핵심 내용
휴머노이드 로봇은 감지 및 인식에 상당한 격차가 있어 밀집된 환경에서 동작 계획을 수행하기 어렵습니다. 이를 해결하기 위해, 우리는 하드웨어와 소프트웨어를 통합한 새로운 자기중심적 인식 시스템인 ARMOR를 소개하며, 특히 휴머노이드 로봇을 위한 웨어러블 형태의 깊이 센서를 포함합니다. 분산 인식 접근 방식은 로봇의 공간 인식을 향상시키고 더 민첩한 동작 계획을 용이하게 합니다. 또한, AMASS 데이터셋의 약 86시간 분량의 인간 사실적 동작을 활용하여 시뮬레이션에서 트랜스포머 기반 모방 학습(IL) 정책을 훈련하여 동적 충돌 회피를 수행합니다. 우리는 ARMOR 인식이 다수의 밀집된 머리 장착형 및 외부 장착형 깊이 카메라 설정보다 우수함을 보여주며, 충돌 63.7% 감소, 성공률 78.7% 향상을 달성했습니다. 또한, IL 정책을 샘플링 기반 동작 계획 전문가인 cuRobo와 비교하여 충돌 31.6% 감소, 성공률 16.9% 향상, 계산 지연 시간 26배 감소를 보여줍니다. 마지막으로, 우리는 Fourier Intelligence의 실제 GR1 휴머노이드에 ARMOR 인식을 배포합니다. 소스 코드, 하드웨어 설명 및 3D CAD 파일에 대한 링크는 이 텍스트의 arXiv 버전에서 업데이트할 예정입니다.

## 参考
- http://arxiv.org/abs/2412.00396v1
