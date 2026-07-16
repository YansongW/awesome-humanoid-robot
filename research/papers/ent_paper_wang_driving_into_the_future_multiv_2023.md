---
$id: ent_paper_wang_driving_into_the_future_multiv_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Drive-WM: Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving'
  zh: Drive-WM：面向自动驾驶的多视角视觉预测与世界模型规划
  ko: 'Drive-WM: 자율주행을 위한 다중 시각 예측 및 세계 모델 기반 계획'
summary:
  en: Drive-WM is a latent video diffusion world model for autonomous driving that generates high-fidelity multi-view videos
    through view-factorized spatial-temporal modeling, supports unified conditioning from images, text, layouts, and ego actions,
    and is applied to tree-based trajectory planning with image-based rewards.
  zh: Drive-WM是一个用于自动驾驶的隐式视频扩散世界模型，通过视图分解的时空建模生成高保真多视角视频，支持来自图像、文本、布局和自车动作的统一条件输入，并应用于基于图像奖励的树状轨迹规划。
  ko: Drive-WM은 자율주행을 위한 잠재 비디오 확산 세계 모델로, 뷰 분해를 통한 시공간 모델링으로 고화질 다중 뷰 영상을 생성하고 이미지, 텍스트, 레이아웃, 자차 행동 등의 통합 조건 입력을 지원하며, 이미지
    기반 보상을 이용한 트리 기반 궤적 계획에 적용되었다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- world_model
- video_diffusion
- multiview_forecasting
- view_factorization
- trajectory_planning
- safety_planning
- autonomous_driving
- image_based_rewards
- ood_simulation
- latent_diffusion
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.17918v1.
sources:
- id: src_001
  type: paper
  title: 'Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving'
  url: https://arxiv.org/abs/2311.17918
  date: '2023'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

## 核心内容
In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

## 参考
- http://arxiv.org/abs/2311.17918v1

## Overview
In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

## Content
In autonomous driving, predicting future events in advance and evaluating the foreseeable risks empowers autonomous vehicles to better plan their actions, enhancing safety and efficiency on the road. To this end, we propose Drive-WM, the first driving world model compatible with existing end-to-end planning models. Through a joint spatial-temporal modeling facilitated by view factorization, our model generates high-fidelity multiview videos in driving scenes. Building on its powerful generation ability, we showcase the potential of applying the world model for safe driving planning for the first time. Particularly, our Drive-WM enables driving into multiple futures based on distinct driving maneuvers, and determines the optimal trajectory according to the image-based rewards. Evaluation on real-world driving datasets verifies that our method could generate high-quality, consistent, and controllable multiview videos, opening up possibilities for real-world simulations and safe planning.

## 개요
자율 주행에서 미리 미래 사건을 예측하고 예측 가능한 위험을 평가하는 것은 자율 주행 차량이 더 나은 행동 계획을 수립하도록 하여 도로 안전성과 효율성을 향상시킵니다. 이를 위해 우리는 기존의 종단간 계획 모델과 호환되는 최초의 주행 월드 모델인 Drive-WM을 제안합니다. 뷰 분해를 통해 촉진된 공동 시공간 모델링을 통해 우리의 모델은 주행 장면에서 고충실도의 멀티뷰 비디오를 생성합니다. 강력한 생성 능력을 바탕으로, 우리는 처음으로 안전한 주행 계획을 위해 월드 모델을 적용할 가능성을 보여줍니다. 특히, Drive-WM은 서로 다른 주행 기동에 기반하여 여러 미래로 주행할 수 있게 하며, 이미지 기반 보상에 따라 최적의 궤적을 결정합니다. 실제 주행 데이터셋에 대한 평가는 우리의 방법이 고품질, 일관성 있고 제어 가능한 멀티뷰 비디오를 생성할 수 있음을 확인하며, 실제 시뮬레이션과 안전한 계획을 위한 가능성을 열어줍니다.

## 핵심 내용
자율 주행에서 미리 미래 사건을 예측하고 예측 가능한 위험을 평가하는 것은 자율 주행 차량이 더 나은 행동 계획을 수립하도록 하여 도로 안전성과 효율성을 향상시킵니다. 이를 위해 우리는 기존의 종단간 계획 모델과 호환되는 최초의 주행 월드 모델인 Drive-WM을 제안합니다. 뷰 분해를 통해 촉진된 공동 시공간 모델링을 통해 우리의 모델은 주행 장면에서 고충실도의 멀티뷰 비디오를 생성합니다. 강력한 생성 능력을 바탕으로, 우리는 처음으로 안전한 주행 계획을 위해 월드 모델을 적용할 가능성을 보여줍니다. 특히, Drive-WM은 서로 다른 주행 기동에 기반하여 여러 미래로 주행할 수 있게 하며, 이미지 기반 보상에 따라 최적의 궤적을 결정합니다. 실제 주행 데이터셋에 대한 평가는 우리의 방법이 고품질, 일관성 있고 제어 가능한 멀티뷰 비디오를 생성할 수 있음을 확인하며, 실제 시뮬레이션과 안전한 계획을 위한 가능성을 열어줍니다.
