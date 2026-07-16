---
$id: ent_paper_song_germ_a_generalist_robotic_mode_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot'
  zh: GeRM
  ko: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot'
summary:
  en: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
  zh: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
  ko: 'GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot (GeRM), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by MiLAB, Westlake University, and published at IROS 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- germ
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.13358v2.
sources:
- id: src_001
  type: website
  title: GeRM source
  url: https://doi.org/10.1109/IROS58592.2024.10801816
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## 核心内容
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## 参考
- http://arxiv.org/abs/2403.13358v2

## Overview
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## Content
Multi-task robot learning holds significant importance in tackling diverse and complex scenarios. However, current approaches are hindered by performance issues and difficulties in collecting training datasets. In this paper, we propose GeRM (Generalist Robotic Model). We utilize offline reinforcement learning to optimize data utilization strategies to learn from both demonstrations and sub-optimal data, thus surpassing the limitations of human demonstrations. Thereafter, we employ a transformer-based VLA network to process multi-modal inputs and output actions. By introducing the Mixture-of-Experts structure, GeRM allows faster inference speed with higher whole model capacity, and thus resolves the issue of limited RL parameters, enhancing model performance in multi-task learning while controlling computational costs. Through a series of experiments, we demonstrate that GeRM outperforms other methods across all tasks, while also validating its efficiency in both training and inference processes. Additionally, we uncover its potential to acquire emergent skills. Additionally, we contribute the QUARD-Auto dataset, collected automatically to support our training approach and foster advancements in multi-task quadruped robot learning. This work presents a new paradigm for reducing the cost of collecting robot data and driving progress in the multi-task learning community. You can reach our project and video through the link: https://songwxuan.github.io/GeRM/ .

## 개요
멀티태스크 로봇 학습은 다양하고 복잡한 시나리오를 해결하는 데 중요한 의미를 갖습니다. 그러나 현재 접근 방식은 성능 문제와 훈련 데이터셋 수집의 어려움으로 인해 제약을 받고 있습니다. 본 논문에서는 GeRM(Generalist Robotic Model)을 제안합니다. 우리는 오프라인 강화 학습을 활용하여 데이터 활용 전략을 최적화함으로써 시연 데이터와 최적이 아닌 데이터 모두에서 학습할 수 있게 하여 인간 시연의 한계를 극복합니다. 이후 트랜스포머 기반 VLA 네트워크를 사용하여 다중 모달 입력을 처리하고 행동을 출력합니다. Mixture-of-Experts 구조를 도입함으로써 GeRM은 더 높은 전체 모델 용량을 유지하면서 더 빠른 추론 속도를 가능하게 하여, 제한된 RL 파라미터 문제를 해결하고 계산 비용을 통제하면서 멀티태스크 학습에서 모델 성능을 향상시킵니다. 일련의 실험을 통해 GeRM이 모든 작업에서 다른 방법보다 우수한 성능을 보일 뿐만 아니라 훈련 및 추론 과정 모두에서 효율성을 입증합니다. 또한, 우리는 창발적 기술을 습득할 수 있는 잠재력을 발견했습니다. 추가로, 우리의 훈련 접근 방식을 지원하고 멀티태스크 사족 로봇 학습의 발전을 촉진하기 위해 자동으로 수집된 QUARD-Auto 데이터셋을 기여합니다. 이 연구는 로봇 데이터 수집 비용을 줄이고 멀티태스크 학습 커뮤니티의 발전을 촉진하는 새로운 패러다임을 제시합니다. 프로젝트와 비디오는 다음 링크에서 확인할 수 있습니다: https://songwxuan.github.io/GeRM/ .

## 핵심 내용
멀티태스크 로봇 학습은 다양하고 복잡한 시나리오를 해결하는 데 중요한 의미를 갖습니다. 그러나 현재 접근 방식은 성능 문제와 훈련 데이터셋 수집의 어려움으로 인해 제약을 받고 있습니다. 본 논문에서는 GeRM(Generalist Robotic Model)을 제안합니다. 우리는 오프라인 강화 학습을 활용하여 데이터 활용 전략을 최적화함으로써 시연 데이터와 최적이 아닌 데이터 모두에서 학습할 수 있게 하여 인간 시연의 한계를 극복합니다. 이후 트랜스포머 기반 VLA 네트워크를 사용하여 다중 모달 입력을 처리하고 행동을 출력합니다. Mixture-of-Experts 구조를 도입함으로써 GeRM은 더 높은 전체 모델 용량을 유지하면서 더 빠른 추론 속도를 가능하게 하여, 제한된 RL 파라미터 문제를 해결하고 계산 비용을 통제하면서 멀티태스크 학습에서 모델 성능을 향상시킵니다. 일련의 실험을 통해 GeRM이 모든 작업에서 다른 방법보다 우수한 성능을 보일 뿐만 아니라 훈련 및 추론 과정 모두에서 효율성을 입증합니다. 또한, 우리는 창발적 기술을 습득할 수 있는 잠재력을 발견했습니다. 추가로, 우리의 훈련 접근 방식을 지원하고 멀티태스크 사족 로봇 학습의 발전을 촉진하기 위해 자동으로 수집된 QUARD-Auto 데이터셋을 기여합니다. 이 연구는 로봇 데이터 수집 비용을 줄이고 멀티태스크 학습 커뮤니티의 발전을 촉진하는 새로운 패러다임을 제시합니다. 프로젝트와 비디오는 다음 링크에서 확인할 수 있습니다: https://songwxuan.github.io/GeRM/ .
