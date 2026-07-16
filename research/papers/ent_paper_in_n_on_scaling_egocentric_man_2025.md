---
$id: ent_paper_in_n_on_scaling_egocentric_man_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data'
  zh: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data'
  ko: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data'
summary:
  en: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data is a 2025 work on manipulation for humanoid
    robots.'
  zh: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data is a 2025 work on manipulation for humanoid
    robots.'
  ko: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data is a 2025 work on manipulation for humanoid
    robots.'
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
- in_n_on
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15704v1.
sources:
- id: src_001
  type: paper
  title: 'In-N-On: Scaling Egocentric Manipulation with in-the-wild and on-task Data (arXiv)'
  url: https://arxiv.org/abs/2511.15704
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 核心内容
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 参考
- http://arxiv.org/abs/2511.15704v1

## Overview
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## Content
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 개요
자기중심적 비디오는 조작 정책을 학습하기 위한 가치 있고 확장 가능한 데이터 소스입니다. 그러나 상당한 데이터 이질성으로 인해 대부분의 기존 접근 방식은 인간 데이터를 단순한 사전 학습에 사용하여 그 잠재력을 완전히 활용하지 못합니다. 본 논문은 먼저 인간 데이터를 인더와일드(in-the-wild)와 온태스크(on-task)의 두 범주로 분류하고 데이터 사용 방법에 대한 체계적 분석을 제공함으로써 자기중심적 데이터를 수집하고 사용하기 위한 확장 가능한 레시피를 제시합니다. 우리는 먼저 PHSD 데이터셋을 구축했으며, 이 데이터셋은 1,000시간 이상의 다양한 인더와일드 자기중심적 데이터와 대상 조작 작업에 직접 정렬된 20시간 이상의 온태스크 데이터를 포함합니다. 이를 통해 대규모 자기중심적 언어 조건부 흐름 매칭 정책인 Human0을 학습할 수 있습니다. 도메인 적응 기술을 통해 Human0은 인간과 휴머노이드 간의 격차를 최소화합니다. 실험적으로, 우리는 Human0이 인간 데이터 확장을 통해 여러 새로운 특성을 달성함을 보여줍니다. 여기에는 인간 데이터만으로 지시를 따르는 언어 이해, 퓨샷 학습, 온태스크 데이터를 사용한 향상된 견고성이 포함됩니다. 프로젝트 웹사이트: https://xiongyicai.github.io/In-N-On/

## 핵심 내용
자기중심적 비디오는 조작 정책을 학습하기 위한 가치 있고 확장 가능한 데이터 소스입니다. 그러나 상당한 데이터 이질성으로 인해 대부분의 기존 접근 방식은 인간 데이터를 단순한 사전 학습에 사용하여 그 잠재력을 완전히 활용하지 못합니다. 본 논문은 먼저 인간 데이터를 인더와일드(in-the-wild)와 온태스크(on-task)의 두 범주로 분류하고 데이터 사용 방법에 대한 체계적 분석을 제공함으로써 자기중심적 데이터를 수집하고 사용하기 위한 확장 가능한 레시피를 제시합니다. 우리는 먼저 PHSD 데이터셋을 구축했으며, 이 데이터셋은 1,000시간 이상의 다양한 인더와일드 자기중심적 데이터와 대상 조작 작업에 직접 정렬된 20시간 이상의 온태스크 데이터를 포함합니다. 이를 통해 대규모 자기중심적 언어 조건부 흐름 매칭 정책인 Human0을 학습할 수 있습니다. 도메인 적응 기술을 통해 Human0은 인간과 휴머노이드 간의 격차를 최소화합니다. 실험적으로, 우리는 Human0이 인간 데이터 확장을 통해 여러 새로운 특성을 달성함을 보여줍니다. 여기에는 인간 데이터만으로 지시를 따르는 언어 이해, 퓨샷 학습, 온태스크 데이터를 사용한 향상된 견고성이 포함됩니다. 프로젝트 웹사이트: https://xiongyicai.github.io/In-N-On/
