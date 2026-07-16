---
$id: ent_paper_efficient_and_scalable_monocul_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
  zh: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
  ko: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
summary:
  en: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
  zh: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
  ko: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficient_and_scalable_monocul
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00960v3.
sources:
- id: src_001
  type: paper
  title: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction (arXiv)
  url: https://arxiv.org/abs/2512.00960
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## 核心内容
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## 参考
- http://arxiv.org/abs/2512.00960v3

## Overview
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## Content
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## 개요
일반화된 로봇은 실제 세계에서 강건하게 작동하기 위해 다양하고 대규모의 인간-객체 상호작용(HOI)으로부터 학습해야 합니다. 단안 인터넷 비디오는 거의 무한하고 쉽게 이용 가능한 데이터 소스를 제공하며, 인간 활동, 객체 및 환경의 비할 데 없는 다양성을 포착합니다. 그러나 이러한 실제 비디오에서 4D 상호작용 데이터를 정확하고 확장 가능하게 추출하는 것은 여전히 중요하고 해결되지 않은 과제로 남아 있습니다. 주석 병목 현상을 극복하기 위해, 우리는 효율적인 희소 접촉 주석 패러다임을 도입합니다. 이 과정을 확장하기 위해, 우리는 인간-인-더-루프 데이터 엔진을 구동하는 다중 모달 예측기인 InterPoint를 개발합니다. 이러한 효율적으로 획득된 주석을 기반으로, 우리는 4DHOISolver를 도입합니다. 이는 잘못된 조건의 4D HOI 재구성 문제를 제약하고 높은 시공간 일관성과 물리적 타당성을 유지하는 새로운 최적화 프레임워크입니다. 이 프레임워크를 활용하여, 우리는 135개의 객체 유형과 133개의 동작을 포함하는 다양한 카탈로그를 갖춘 새로운 대규모 4D HOI 데이터셋인 Open4DHOI를 소개합니다. 또한, 우리는 RL 기반 에이전트가 복원된 동작을 모방할 수 있도록 하여 재구성의 효과를 입증합니다. 데이터와 코드는 https://github.com/wenboran2002/open4dhoi_code에서 공개될 예정입니다.

## 핵심 내용
일반화된 로봇은 실제 세계에서 강건하게 작동하기 위해 다양하고 대규모의 인간-객체 상호작용(HOI)으로부터 학습해야 합니다. 단안 인터넷 비디오는 거의 무한하고 쉽게 이용 가능한 데이터 소스를 제공하며, 인간 활동, 객체 및 환경의 비할 데 없는 다양성을 포착합니다. 그러나 이러한 실제 비디오에서 4D 상호작용 데이터를 정확하고 확장 가능하게 추출하는 것은 여전히 중요하고 해결되지 않은 과제로 남아 있습니다. 주석 병목 현상을 극복하기 위해, 우리는 효율적인 희소 접촉 주석 패러다임을 도입합니다. 이 과정을 확장하기 위해, 우리는 인간-인-더-루프 데이터 엔진을 구동하는 다중 모달 예측기인 InterPoint를 개발합니다. 이러한 효율적으로 획득된 주석을 기반으로, 우리는 4DHOISolver를 도입합니다. 이는 잘못된 조건의 4D HOI 재구성 문제를 제약하고 높은 시공간 일관성과 물리적 타당성을 유지하는 새로운 최적화 프레임워크입니다. 이 프레임워크를 활용하여, 우리는 135개의 객체 유형과 133개의 동작을 포함하는 다양한 카탈로그를 갖춘 새로운 대규모 4D HOI 데이터셋인 Open4DHOI를 소개합니다. 또한, 우리는 RL 기반 에이전트가 복원된 동작을 모방할 수 있도록 하여 재구성의 효과를 입증합니다. 데이터와 코드는 https://github.com/wenboran2002/open4dhoi_code에서 공개될 예정입니다.
