---
$id: ent_paper_learning_humanoid_locomotion_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion with World Model Reconstruction
  zh: Learning Humanoid Locomotion with World Model Reconstruction
  ko: Learning Humanoid Locomotion with World Model Reconstruction
summary:
  en: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
  zh: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
  ko: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.16230v1.
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion with World Model Reconstruction (arXiv)
  url: https://arxiv.org/abs/2502.16230
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## 核心内容
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## 参考
- http://arxiv.org/abs/2502.16230v1

## Overview
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## Content
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## 개요
휴머노이드 로봇은 인간이 접근 가능한 환경을 다리로 탐색하도록 설계되었습니다. 그러나 기존 연구는 주로 통제된 실험실 환경에 초점을 맞추어, 복잡한 실제 지형을 탐색하기 위한 제어기 개발에 격차가 발생했습니다. 이러한 어려움은 주로 센서 데이터의 한계와 노이즈에서 비롯되며, 이는 로봇의 자기 및 환경 이해를 방해합니다. 본 연구에서는 도전적인 지형에서의 블라인드 휴머노이드 보행을 위한 엔드투엔드 학습 기반 접근법인 World Model Reconstruction (WMR)을 소개합니다. 우리는 추정기를 훈련시켜 세계 상태를 명시적으로 재구성하고, 이를 활용하여 보행 정책을 향상시킬 것을 제안합니다. 보행 정책은 재구성된 정보만을 입력으로 받습니다. 정책과 추정기는 공동으로 훈련되지만, 둘 사이의 그래디언트는 의도적으로 차단됩니다. 이는 추정기가 보행 정책의 업데이트와 독립적으로 세계 재구성에만 집중하도록 보장합니다. 우리는 실제 시나리오에서 거칠고 변형 가능하며 미끄러운 표면에서 모델을 평가하여 강력한 적응성과 간섭 저항성을 입증했습니다. 로봇은 인간의 도움 없이 3.2km 하이킹을 성공적으로 완료하며, 얼음과 눈으로 덮인 지형을 마스터했습니다.

## 핵심 내용
휴머노이드 로봇은 인간이 접근 가능한 환경을 다리로 탐색하도록 설계되었습니다. 그러나 기존 연구는 주로 통제된 실험실 환경에 초점을 맞추어, 복잡한 실제 지형을 탐색하기 위한 제어기 개발에 격차가 발생했습니다. 이러한 어려움은 주로 센서 데이터의 한계와 노이즈에서 비롯되며, 이는 로봇의 자기 및 환경 이해를 방해합니다. 본 연구에서는 도전적인 지형에서의 블라인드 휴머노이드 보행을 위한 엔드투엔드 학습 기반 접근법인 World Model Reconstruction (WMR)을 소개합니다. 우리는 추정기를 훈련시켜 세계 상태를 명시적으로 재구성하고, 이를 활용하여 보행 정책을 향상시킬 것을 제안합니다. 보행 정책은 재구성된 정보만을 입력으로 받습니다. 정책과 추정기는 공동으로 훈련되지만, 둘 사이의 그래디언트는 의도적으로 차단됩니다. 이는 추정기가 보행 정책의 업데이트와 독립적으로 세계 재구성에만 집중하도록 보장합니다. 우리는 실제 시나리오에서 거칠고 변형 가능하며 미끄러운 표면에서 모델을 평가하여 강력한 적응성과 간섭 저항성을 입증했습니다. 로봇은 인간의 도움 없이 3.2km 하이킹을 성공적으로 완료하며, 얼음과 눈으로 덮인 지형을 마스터했습니다.
