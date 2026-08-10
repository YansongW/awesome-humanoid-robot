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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.00396v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (854 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2412.00396v1

## 개요
휴머노이드 로봇의 밀집 환경에서의 운동 계획은 종종 인식 능력의 부족으로 제한됩니다. ARMOR 시스템은 웨어러블 기기와 유사한 깊이 센서를 통합하여 분산 방식으로 로봇의 공간 인식 능력을 향상시켜 더 민첩한 운동 계획을 지원합니다. 연구팀은 AMASS 데이터셋의 약 86시간 인간 실제 운동 데이터를 활용하여 시뮬레이션에서 Transformer 기반 모방 학습 정책을 훈련시켜 동적 충돌 회피를 구현했습니다. 실험 결과, ARMOR는 여러 헤드마운트 및 외장 깊이 카메라 조합 방식에 비해 충돌 횟수가 63.7% 감소하고 성공률이 78.7% 향상되었습니다. 또한, 모방 학습 정책은 샘플링 기반 운동 계획 전문가 cuRobo에 비해 충돌이 31.6% 감소하고 성공률이 16.9% 향상되었으며 계산 지연 시간이 26배 감소했습니다. 이 시스템은 Fourier Intelligence의 GR1 휴머노이드 로봇에서 실제 배포가 완료되었습니다.

## 핵심 내용
### 방법
- **인식 시스템 설계**: ARMOR는 분산 인식 아키텍처를 채택하여 로봇 신체의 주요 위치에 웨어러블 기기와 유사한 깊이 센서를 통합함으로써 기존 헤드마운트 또는 외장 카메라가 밀집 환경에서 가지는 인식 사각지대를 보완합니다.
- **운동 계획 및 충돌 회피**: Transformer 기반 모방 학습 정책이 시뮬레이션 환경에서 훈련되며, 훈련 데이터는 AMASS 데이터셋의 약 86시간 인간 실제 운동 데이터에서 비롯되어 로봇이 동적 충돌 회피 행동을 학습할 수 있게 합니다.

### 실험 설정 및 주요 결과
- **비교 기준**: 여러 밀집 헤드마운트 및 외장 깊이 카메라 조합과 비교하여 ARMOR는 다음을 달성했습니다:
  - 충돌 횟수 63.7% 감소
  - 성공률 78.7% 향상
- **정책 비교**: 샘플링 기반 운동 계획 전문가 cuRobo와 비교하여 ARMOR의 모방 학습 정책은 다음을 달성했습니다:
  - 충돌 31.6% 감소
  - 성공률 16.9% 향상
  - 계산 지연 시간 26배 감소
- **실제 배포**: 시스템은 Fourier Intelligence의 GR1 휴머노이드 로봇에서 배포 검증이 완료되었습니다.

### 결론
ARMOR는 소프트웨어와 하드웨어가 협력하는 자기 중심 인식 방식을 통해 밀집 환경에서 휴머노이드 로봇의 충돌 회피 및 운동 계획 능력을 크게 향상시켰으며, 시뮬레이션과 실제 시나리오 모두에서 기존 방법보다 우수한 성능을 입증했습니다.
