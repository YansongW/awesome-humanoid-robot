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
  zh: CLASP 是一种融合视觉与触觉的物体形状精化方法，由研究团队提出。其核心贡献在于通过变分形状网络的隐空间粒子滤波与接触流形投影，持续降低预测形状与真实场景之间的 Chamfer 距离，使机器人能利用接触观测修正初始形状估计。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2110.08719v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (654 chars, DeepSeek).'
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
CLASP 方法首先利用 RGB-D 数据通过形状补全网络生成初始形状先验，随后引入二进制机器人接触观测作为约束。该方法在变分形状网络的隐空间中维护一个粒子滤波器，通过将粒子投影到接触流形上，确保生成的形状同时符合网络先验与接触信息。实验表明，CLASP 能一致性地降低预测形状与真实场景的 Chamfer 距离，而其他方法无法从接触信息中获益。

## 核心内容
### 方法架构
CLASP 由两个核心组件构成：
- **形状补全网络**：基于 RGB-D 数据生成初始形状先验，用于修正噪声、填补空洞与遮挡区域。
- **隐空间粒子滤波与投影**：在变分形状网络的隐空间中维护一组粒子，每个粒子代表一个可能的形状。当机器人检测到意外接触时，粒子被投影到接触流形上，从而更新形状估计以解释接触观测。

### 实验设置
- 使用真实场景的 ground-truth 形状作为基准，评估指标为 Chamfer Distance。
- 对比方法包括仅依赖视觉先验的基线，以及未利用接触信息的其他方法。

### 关键结果
- CLASP 在所有测试场景中一致性地降低了 Chamfer Distance，表明其能有效融合接触信息提升形状精度。
- 其他方法在引入接触观测后未表现出性能提升，甚至可能退化，凸显了 CLASP 在利用接触约束方面的独特优势。

### 结论
CLASP 通过将接触观测作为隐空间中的硬约束，实现了视觉与触觉感知的协同，为机器人环境状态估计提供了更可靠的形状精化方案。

## Overview
Robots need both visual and contact sensing to effectively estimate the state of their environment. Camera RGBD data provides rich information of the objects surrounding the robot, and shape priors can help correct noise and fill in gaps and occluded regions. However, when the robot senses unexpected contact, the estimate should be updated to explain the contact. To address this need, we propose CLASP: Constrained Latent Shape Projection. This approach consists of a shape completion network that generates a prior from RGBD data and a procedure to generate shapes consistent with both the network prior and robot contact observations. We find CLASP consistently decreases the Chamfer Distance between the predicted and ground truth scenes, while other approaches do not benefit from contact information.

## 参考
- http://arxiv.org/abs/2110.08719v1

## 개요
CLASP 방법은 먼저 RGB-D 데이터를 활용하여 형태 완성 네트워크를 통해 초기 형태 사전을 생성하고, 이후 이진 로봇 접촉 관측을 제약 조건으로 도입합니다. 이 방법은 변분 형태 네트워크의 잠재 공간에서 입자 필터를 유지하며, 입자를 접촉 다양체에 투영하여 생성된 형태가 네트워크 사전과 접촉 정보를 동시에 충족하도록 보장합니다. 실험 결과, CLASP는 예측 형태와 실제 장면 간의 Chamfer 거리를 일관되게 줄일 수 있었으며, 다른 방법들은 접촉 정보로부터 이점을 얻지 못했습니다.

## 핵심 내용
### 방법 구조
CLASP는 두 가지 핵심 구성 요소로 이루어져 있습니다:
- **형태 완성 네트워크**: RGB-D 데이터를 기반으로 초기 형태 사전을 생성하여 노이즈를 수정하고, 빈 공간과 가려진 영역을 채웁니다.
- **잠재 공간 입자 필터 및 투영**: 변분 형태 네트워크의 잠재 공간에서 입자 집합을 유지하며, 각 입자는 가능한 형태를 나타냅니다. 로봇이 예상치 못한 접촉을 감지하면 입자가 접촉 다양체에 투영되어 접촉 관측을 설명하도록 형태 추정이 업데이트됩니다.

### 실험 설정
- 실제 장면의 ground-truth 형태를 기준으로 사용하며, 평가 지표는 Chamfer Distance입니다.
- 비교 방법에는 시각적 사전에만 의존하는 기준선과 접촉 정보를 활용하지 않는 다른 방법들이 포함됩니다.

### 주요 결과
- CLASP는 모든 테스트 장면에서 Chamfer Distance를 일관되게 줄여, 접촉 정보를 효과적으로 융합하여 형태 정밀도를 향상시킬 수 있음을 보여줍니다.
- 다른 방법들은 접촉 관측을 도입한 후 성능 향상을 보이지 않았으며, 오히려 성능이 저하될 수 있어 접촉 제약 활용에 있어 CLASP의 독특한 장점을 부각시킵니다.

### 결론
CLASP는 접촉 관측을 잠재 공간의 하드 제약 조건으로 통합함으로써 시각 및 촉각 인식의 협력을 실현하며, 로봇 환경 상태 추정을 위한 더 신뢰할 수 있는 형태 정제 방안을 제공합니다.
