---
$id: ent_paper_sim_and_real_co_training_a_sim_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation'
  zh: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation'
  ko: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation'
summary:
  en: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation is a 2025 work on manipulation for
    humanoid robots.'
  zh: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation is a 2025 work on manipulation for
    humanoid robots.'
  ko: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation is a 2025 work on manipulation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- manipulation
- sim_and_real_co_training
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.24361v2.
sources:
- id: src_001
  type: paper
  title: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2503.24361
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Sim-and-Real Co-Training: A Simple Recipe for Vision-Based Robotic Manipulation project page'
  url: https://co-training.github.io/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive. Simulation has great potential in supplementing large-scale data, especially with recent advances in generative AI and automated data generation tools that enable scalable creation of robot behavior datasets. However, training a policy solely in simulation and transferring it to the real world often demands substantial human effort to bridge the reality gap. A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets. Preliminary studies have recently shown this strategy to substantially improve the performance of a policy over one trained on a limited amount of real-world data. Nonetheless, the community lacks a systematic understanding of sim-and-real co-training and what it takes to reap the benefits of simulation data for real-robot learning. This work presents a simple yet effective recipe for utilizing simulation data to solve vision-based robotic manipulation tasks. We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets. Using two domains--a robot arm and a humanoid--across diverse tasks, we demonstrate that simulation data can enhance real-world task performance by an average of 38%, even with notable differences between the simulation and real-world data. Videos and additional results can be found at https://co-training.github.io/

## 核心内容
Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive. Simulation has great potential in supplementing large-scale data, especially with recent advances in generative AI and automated data generation tools that enable scalable creation of robot behavior datasets. However, training a policy solely in simulation and transferring it to the real world often demands substantial human effort to bridge the reality gap. A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets. Preliminary studies have recently shown this strategy to substantially improve the performance of a policy over one trained on a limited amount of real-world data. Nonetheless, the community lacks a systematic understanding of sim-and-real co-training and what it takes to reap the benefits of simulation data for real-robot learning. This work presents a simple yet effective recipe for utilizing simulation data to solve vision-based robotic manipulation tasks. We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets. Using two domains--a robot arm and a humanoid--across diverse tasks, we demonstrate that simulation data can enhance real-world task performance by an average of 38%, even with notable differences between the simulation and real-world data. Videos and additional results can be found at https://co-training.github.io/

## 参考
- http://arxiv.org/abs/2503.24361v2

## Overview
Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive. Simulation has great potential in supplementing large-scale data, especially with recent advances in generative AI and automated data generation tools that enable scalable creation of robot behavior datasets. However, training a policy solely in simulation and transferring it to the real world often demands substantial human effort to bridge the reality gap. A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets. Preliminary studies have recently shown this strategy to substantially improve the performance of a policy over one trained on a limited amount of real-world data. Nonetheless, the community lacks a systematic understanding of sim-and-real co-training and what it takes to reap the benefits of simulation data for real-robot learning. This work presents a simple yet effective recipe for utilizing simulation data to solve vision-based robotic manipulation tasks. We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets. Using two domains--a robot arm and a humanoid--across diverse tasks, we demonstrate that simulation data can enhance real-world task performance by an average of 38%, even with notable differences between the simulation and real-world data. Videos and additional results can be found at https://co-training.github.io/

## Content
Large real-world robot datasets hold great potential to train generalist robot models, but scaling real-world human data collection is time-consuming and resource-intensive. Simulation has great potential in supplementing large-scale data, especially with recent advances in generative AI and automated data generation tools that enable scalable creation of robot behavior datasets. However, training a policy solely in simulation and transferring it to the real world often demands substantial human effort to bridge the reality gap. A compelling alternative is to co-train the policy on a mixture of simulation and real-world datasets. Preliminary studies have recently shown this strategy to substantially improve the performance of a policy over one trained on a limited amount of real-world data. Nonetheless, the community lacks a systematic understanding of sim-and-real co-training and what it takes to reap the benefits of simulation data for real-robot learning. This work presents a simple yet effective recipe for utilizing simulation data to solve vision-based robotic manipulation tasks. We derive this recipe from comprehensive experiments that validate the co-training strategy on various simulation and real-world datasets. Using two domains--a robot arm and a humanoid--across diverse tasks, we demonstrate that simulation data can enhance real-world task performance by an average of 38%, even with notable differences between the simulation and real-world data. Videos and additional results can be found at https://co-training.github.io/

## 개요
대규모 실제 로봇 데이터셋은 범용 로봇 모델을 훈련하는 데 큰 잠재력을 가지고 있지만, 실제 환경에서 인간 데이터를 수집하는 것은 시간이 많이 소요되고 자원 집약적입니다. 시뮬레이션은 특히 생성형 AI 및 자동 데이터 생성 도구의 최근 발전으로 확장 가능한 로봇 행동 데이터셋을 생성할 수 있게 되면서, 대규모 데이터를 보완하는 데 큰 잠재력을 가지고 있습니다. 그러나 시뮬레이션에서만 정책을 훈련하고 이를 실제 환경으로 전이하려면 현실 격차를 해소하기 위해 상당한 인간의 노력이 필요합니다. 매력적인 대안은 시뮬레이션과 실제 데이터셋을 혼합하여 정책을 공동 훈련하는 것입니다. 최근 예비 연구들은 이 전략이 제한된 양의 실제 데이터로 훈련된 정책보다 성능을 크게 향상시킬 수 있음을 보여주었습니다. 그럼에도 불구하고, 커뮤니티는 시뮬레이션과 실제 공동 훈련에 대한 체계적인 이해와 실제 로봇 학습을 위해 시뮬레이션 데이터의 이점을 활용하는 방법에 대해 부족한 실정입니다. 본 연구는 시뮬레이션 데이터를 활용하여 비전 기반 로봇 조작 작업을 해결하기 위한 간단하면서도 효과적인 레시피를 제시합니다. 우리는 다양한 시뮬레이션 및 실제 데이터셋에서 공동 훈련 전략을 검증한 포괄적인 실험을 통해 이 레시피를 도출했습니다. 로봇 팔과 휴머노이드라는 두 도메인에서 다양한 작업을 수행하며, 시뮬레이션과 실제 데이터 간에 현저한 차이가 있음에도 불구하고 시뮬레이션 데이터가 실제 작업 성능을 평균 38% 향상시킬 수 있음을 입증했습니다. 비디오 및 추가 결과는 https://co-training.github.io/ 에서 확인할 수 있습니다.

## 핵심 내용
대규모 실제 로봇 데이터셋은 범용 로봇 모델을 훈련하는 데 큰 잠재력을 가지고 있지만, 실제 환경에서 인간 데이터를 수집하는 것은 시간이 많이 소요되고 자원 집약적입니다. 시뮬레이션은 특히 생성형 AI 및 자동 데이터 생성 도구의 최근 발전으로 확장 가능한 로봇 행동 데이터셋을 생성할 수 있게 되면서, 대규모 데이터를 보완하는 데 큰 잠재력을 가지고 있습니다. 그러나 시뮬레이션에서만 정책을 훈련하고 이를 실제 환경으로 전이하려면 현실 격차를 해소하기 위해 상당한 인간의 노력이 필요합니다. 매력적인 대안은 시뮬레이션과 실제 데이터셋을 혼합하여 정책을 공동 훈련하는 것입니다. 최근 예비 연구들은 이 전략이 제한된 양의 실제 데이터로 훈련된 정책보다 성능을 크게 향상시킬 수 있음을 보여주었습니다. 그럼에도 불구하고, 커뮤니티는 시뮬레이션과 실제 공동 훈련에 대한 체계적인 이해와 실제 로봇 학습을 위해 시뮬레이션 데이터의 이점을 활용하는 방법에 대해 부족한 실정입니다. 본 연구는 시뮬레이션 데이터를 활용하여 비전 기반 로봇 조작 작업을 해결하기 위한 간단하면서도 효과적인 레시피를 제시합니다. 우리는 다양한 시뮬레이션 및 실제 데이터셋에서 공동 훈련 전략을 검증한 포괄적인 실험을 통해 이 레시피를 도출했습니다. 로봇 팔과 휴머노이드라는 두 도메인에서 다양한 작업을 수행하며, 시뮬레이션과 실제 데이터 간에 현저한 차이가 있음에도 불구하고 시뮬레이션 데이터가 실제 작업 성능을 평균 38% 향상시킬 수 있음을 입증했습니다. 비디오 및 추가 결과는 https://co-training.github.io/ 에서 확인할 수 있습니다.
