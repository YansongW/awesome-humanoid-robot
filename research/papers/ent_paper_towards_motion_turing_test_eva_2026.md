---
$id: ent_paper_towards_motion_turing_test_eva_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
  zh: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
  ko: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots'
summary:
  en: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
  zh: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
  ko: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots is a 2026 work on simulation benchmark for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- simulation
- towards_motion_turing_test
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.06181v1.
sources:
- id: src_001
  type: paper
  title: 'Towards Motion Turing Test: Evaluating Human-Likeness in Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2603.06181
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## 核心内容
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## 参考
- http://arxiv.org/abs/2603.06181v1

## Overview
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## Content
Humanoid robots have achieved significant progress in motion generation and control, exhibiting movements that appear increasingly natural and human-like. Inspired by the Turing Test, we propose the Motion Turing Test, a framework that evaluates whether human observers can discriminate between humanoid robot and human poses using only kinematic information. To facilitate this evaluation, we present the Human-Humanoid Motion (HHMotion) dataset, which consists of 1,000 motion sequences spanning 15 action categories, performed by 11 humanoid models and 10 human subjects. All motion sequences are converted into SMPL-X representations to eliminate the influence of visual appearance. We recruited 30 annotators to rate the human-likeness of each pose on a 0-5 scale, resulting in over 500 hours of annotation. Analysis of the collected data reveals that humanoid motions still exhibit noticeable deviations from human movements, particularly in dynamic actions such as jumping, boxing, and running. Building on HHMotion, we formulate a human-likeness evaluation task that aims to automatically predict human-likeness scores from motion data. Despite recent progress in multimodal large language models, we find that they remain inadequate for assessing motion human-likeness. To address this, we propose a simple baseline model and demonstrate that it outperforms several contemporary LLM-based methods. The dataset, code, and benchmark will be publicly released to support future research in the community.

## 개요
휴머노이드 로봇은 동작 생성 및 제어 분야에서 상당한 진전을 이루었으며, 점점 더 자연스럽고 인간과 유사한 움직임을 보여주고 있습니다. 튜링 테스트에서 영감을 받아, 우리는 운동 정보만을 사용하여 인간 관찰자가 휴머노이드 로봇과 인간의 자세를 구별할 수 있는지 평가하는 프레임워크인 Motion Turing Test를 제안합니다. 이 평가를 지원하기 위해, 11개의 휴머노이드 모델과 10명의 인간 피험자가 수행한 15개 동작 범주에 걸친 1,000개의 동작 시퀀스로 구성된 Human-Humanoid Motion (HHMotion) 데이터셋을 소개합니다. 모든 동작 시퀀스는 시각적 외형의 영향을 제거하기 위해 SMPL-X 표현으로 변환됩니다. 우리는 30명의 주석 작업자를 모집하여 각 자세의 인간 유사성을 0-5 척도로 평가하도록 하였으며, 그 결과 500시간 이상의 주석 작업이 수행되었습니다. 수집된 데이터 분석 결과, 휴머노이드 동작은 특히 점프, 복싱, 달리기와 같은 역동적인 동작에서 인간의 움직임과 눈에 띄는 차이를 보이는 것으로 나타났습니다. HHMotion을 기반으로, 우리는 동작 데이터에서 인간 유사성 점수를 자동으로 예측하는 것을 목표로 하는 인간 유사성 평가 과제를 구성합니다. 최근 다중 모달 대규모 언어 모델의 발전에도 불구하고, 우리는 이러한 모델이 동작의 인간 유사성을 평가하는 데 여전히 부적합하다는 것을 발견했습니다. 이를 해결하기 위해, 우리는 간단한 기준 모델을 제안하고 이것이 여러 최신 LLM 기반 방법보다 우수함을 입증합니다. 데이터셋, 코드, 벤치마크는 커뮤니티의 향후 연구를 지원하기 위해 공개될 예정입니다.

## 핵심 내용
휴머노이드 로봇은 동작 생성 및 제어 분야에서 상당한 진전을 이루었으며, 점점 더 자연스럽고 인간과 유사한 움직임을 보여주고 있습니다. 튜링 테스트에서 영감을 받아, 우리는 운동 정보만을 사용하여 인간 관찰자가 휴머노이드 로봇과 인간의 자세를 구별할 수 있는지 평가하는 프레임워크인 Motion Turing Test를 제안합니다. 이 평가를 지원하기 위해, 11개의 휴머노이드 모델과 10명의 인간 피험자가 수행한 15개 동작 범주에 걸친 1,000개의 동작 시퀀스로 구성된 Human-Humanoid Motion (HHMotion) 데이터셋을 소개합니다. 모든 동작 시퀀스는 시각적 외형의 영향을 제거하기 위해 SMPL-X 표현으로 변환됩니다. 우리는 30명의 주석 작업자를 모집하여 각 자세의 인간 유사성을 0-5 척도로 평가하도록 하였으며, 그 결과 500시간 이상의 주석 작업이 수행되었습니다. 수집된 데이터 분석 결과, 휴머노이드 동작은 특히 점프, 복싱, 달리기와 같은 역동적인 동작에서 인간의 움직임과 눈에 띄는 차이를 보이는 것으로 나타났습니다. HHMotion을 기반으로, 우리는 동작 데이터에서 인간 유사성 점수를 자동으로 예측하는 것을 목표로 하는 인간 유사성 평가 과제를 구성합니다. 최근 다중 모달 대규모 언어 모델의 발전에도 불구하고, 우리는 이러한 모델이 동작의 인간 유사성을 평가하는 데 여전히 부적합하다는 것을 발견했습니다. 이를 해결하기 위해, 우리는 간단한 기준 모델을 제안하고 이것이 여러 최신 LLM 기반 방법보다 우수함을 입증합니다. 데이터셋, 코드, 벤치마크는 커뮤니티의 향후 연구를 지원하기 위해 공개될 예정입니다.
