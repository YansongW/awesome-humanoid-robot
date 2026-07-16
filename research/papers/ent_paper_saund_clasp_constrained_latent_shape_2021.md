---
$id: ent_paper_saund_clasp_constrained_latent_shape_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLASP: Constrained Latent Shape Projection for Refining Object Shape from Robot Contact'
  zh: CLASP：基于机器人接触的约束潜在形状投影以细化物体形状
  ko: 'CLASP: 로봇 접촉을 이용한 물체 형상 정제를 위한 제약 잠재 형상 투영'
summary:
  en: CLASP fuses RGB-D shape-completion priors with binary robot contact observations by maintaining a particle filter in
    the latent space of a variational shape network and projecting particles onto the contact manifold, consistently reducing
    Chamfer distance to ground-truth scenes.
  zh: CLASP 通过在变分形状网络的潜在空间中维护粒子滤波器，并将粒子投影到接触流形上，融合 RGB-D 形状补全先验与二值机器人接触观测，持续降低预测场景与真实场景之间的 Chamfer 距离。
  ko: CLASP는 변분 형상 네트워크의 잠재 공간에서 입자 필터를 유지하고 입자를 접촉 다양체로 투영함으로써 RGB-D 형상 완성 사전 정보와 이진 로봇 접촉 관측을 융합하여 예측 장면과 실제 장면 간 Chamfer
    거리를 지속적으로 줄인다.
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
- shape_completion
- contact_sensing
- rgbd_contact_fusion
- latent_shape_projection
- particle_filter
- object_state_estimation
- manipulation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2110.08719v1.
sources:
- id: src_001
  type: paper
  title: 'CLASP: Constrained Latent Shape Projection for Refining Object Shape from Robot Contact'
  url: https://arxiv.org/abs/2110.08719
  date: '2021'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Robots need both visual and contact sensing to effectively estimate the state of their environment. Camera RGBD data provides rich information of the objects surrounding the robot, and shape priors can help correct noise and fill in gaps and occluded regions. However, when the robot senses unexpected contact, the estimate should be updated to explain the contact. To address this need, we propose CLASP: Constrained Latent Shape Projection. This approach consists of a shape completion network that generates a prior from RGBD data and a procedure to generate shapes consistent with both the network prior and robot contact observations. We find CLASP consistently decreases the Chamfer Distance between the predicted and ground truth scenes, while other approaches do not benefit from contact information.

## 核心内容
Robots need both visual and contact sensing to effectively estimate the state of their environment. Camera RGBD data provides rich information of the objects surrounding the robot, and shape priors can help correct noise and fill in gaps and occluded regions. However, when the robot senses unexpected contact, the estimate should be updated to explain the contact. To address this need, we propose CLASP: Constrained Latent Shape Projection. This approach consists of a shape completion network that generates a prior from RGBD data and a procedure to generate shapes consistent with both the network prior and robot contact observations. We find CLASP consistently decreases the Chamfer Distance between the predicted and ground truth scenes, while other approaches do not benefit from contact information.

## 参考
- http://arxiv.org/abs/2110.08719v1

## Overview
Robots need both visual and contact sensing to effectively estimate the state of their environment. Camera RGBD data provides rich information of the objects surrounding the robot, and shape priors can help correct noise and fill in gaps and occluded regions. However, when the robot senses unexpected contact, the estimate should be updated to explain the contact. To address this need, we propose CLASP: Constrained Latent Shape Projection. This approach consists of a shape completion network that generates a prior from RGBD data and a procedure to generate shapes consistent with both the network prior and robot contact observations. We find CLASP consistently decreases the Chamfer Distance between the predicted and ground truth scenes, while other approaches do not benefit from contact information.

## Content
Robots need both visual and contact sensing to effectively estimate the state of their environment. Camera RGBD data provides rich information of the objects surrounding the robot, and shape priors can help correct noise and fill in gaps and occluded regions. However, when the robot senses unexpected contact, the estimate should be updated to explain the contact. To address this need, we propose CLASP: Constrained Latent Shape Projection. This approach consists of a shape completion network that generates a prior from RGBD data and a procedure to generate shapes consistent with both the network prior and robot contact observations. We find CLASP consistently decreases the Chamfer Distance between the predicted and ground truth scenes, while other approaches do not benefit from contact information.

## 개요
로봇은 환경 상태를 효과적으로 추정하기 위해 시각 및 접촉 감지가 모두 필요합니다. 카메라 RGBD 데이터는 로봇 주변 객체에 대한 풍부한 정보를 제공하며, 형상 사전 정보는 노이즈를 보정하고 빈 공간 및 가려진 영역을 채우는 데 도움을 줍니다. 그러나 로봇이 예상치 못한 접촉을 감지하면, 해당 접촉을 설명하기 위해 추정치를 업데이트해야 합니다. 이러한 필요성을 해결하기 위해, 우리는 CLASP: Constrained Latent Shape Projection을 제안합니다. 이 접근법은 RGBD 데이터로부터 사전 정보를 생성하는 형상 완성 네트워크와, 네트워크 사전 정보 및 로봇 접촉 관측치 모두와 일관된 형상을 생성하는 절차로 구성됩니다. 우리는 CLASP가 예측 장면과 실제 장면 간의 Chamfer Distance를 지속적으로 감소시키는 반면, 다른 접근법들은 접촉 정보로부터 이점을 얻지 못함을 발견했습니다.

## 핵심 내용
로봇은 환경 상태를 효과적으로 추정하기 위해 시각 및 접촉 감지가 모두 필요합니다. 카메라 RGBD 데이터는 로봇 주변 객체에 대한 풍부한 정보를 제공하며, 형상 사전 정보는 노이즈를 보정하고 빈 공간 및 가려진 영역을 채우는 데 도움을 줍니다. 그러나 로봇이 예상치 못한 접촉을 감지하면, 해당 접촉을 설명하기 위해 추정치를 업데이트해야 합니다. 이러한 필요성을 해결하기 위해, 우리는 CLASP: Constrained Latent Shape Projection을 제안합니다. 이 접근법은 RGBD 데이터로부터 사전 정보를 생성하는 형상 완성 네트워크와, 네트워크 사전 정보 및 로봇 접촉 관측치 모두와 일관된 형상을 생성하는 절차로 구성됩니다. 우리는 CLASP가 예측 장면과 실제 장면 간의 Chamfer Distance를 지속적으로 감소시키는 반면, 다른 접근법들은 접촉 정보로부터 이점을 얻지 못함을 발견했습니다.
