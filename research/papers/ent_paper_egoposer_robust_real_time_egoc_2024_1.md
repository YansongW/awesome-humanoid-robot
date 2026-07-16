---
$id: ent_paper_egoposer_robust_real_time_egoc_2024_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere'
  zh: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere'
  ko: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere'
summary:
  en: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere is a 2024
    work on human motion analysis and synthesis for humanoid robots, with open-source code available.'
  zh: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere is a 2024
    work on human motion analysis and synthesis for humanoid robots, with open-source code available.'
  ko: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere is a 2024
    work on human motion analysis and synthesis for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- egoposer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2308.06493v3.
sources:
- id: src_001
  type: website
  title: 'EgoPoser: Robust Real-Time Egocentric Pose Estimation from Sparse and Intermittent Observations Everywhere project
    page'
  url: https://siplab.org/projects/EgoPoser
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Full-body egocentric pose estimation from head and hand poses alone has become an active area of research to power articulate avatar representations on headset-based platforms. However, existing methods over-rely on the indoor motion-capture spaces in which datasets were recorded, while simultaneously assuming continuous joint motion capture and uniform body dimensions. We propose EgoPoser to overcome these limitations with four main contributions. 1) EgoPoser robustly models body pose from intermittent hand position and orientation tracking only when inside a headset's field of view. 2) We rethink input representations for headset-based ego-pose estimation and introduce a novel global motion decomposition method that predicts full-body pose independent of global positions. 3) We enhance pose estimation by capturing longer motion time series through an efficient SlowFast module design that maintains computational efficiency. 4) EgoPoser generalizes across various body shapes for different users. We experimentally evaluate our method and show that it outperforms state-of-the-art methods both qualitatively and quantitatively while maintaining a high inference speed of over 600fps. EgoPoser establishes a robust baseline for future work where full-body pose estimation no longer needs to rely on outside-in capture and can scale to large-scale and unseen environments.

## 核心内容
Full-body egocentric pose estimation from head and hand poses alone has become an active area of research to power articulate avatar representations on headset-based platforms. However, existing methods over-rely on the indoor motion-capture spaces in which datasets were recorded, while simultaneously assuming continuous joint motion capture and uniform body dimensions. We propose EgoPoser to overcome these limitations with four main contributions. 1) EgoPoser robustly models body pose from intermittent hand position and orientation tracking only when inside a headset's field of view. 2) We rethink input representations for headset-based ego-pose estimation and introduce a novel global motion decomposition method that predicts full-body pose independent of global positions. 3) We enhance pose estimation by capturing longer motion time series through an efficient SlowFast module design that maintains computational efficiency. 4) EgoPoser generalizes across various body shapes for different users. We experimentally evaluate our method and show that it outperforms state-of-the-art methods both qualitatively and quantitatively while maintaining a high inference speed of over 600fps. EgoPoser establishes a robust baseline for future work where full-body pose estimation no longer needs to rely on outside-in capture and can scale to large-scale and unseen environments.

## 参考
- http://arxiv.org/abs/2308.06493v3

## Overview
Full-body egocentric pose estimation from head and hand poses alone has become an active area of research to power articulate avatar representations on headset-based platforms. However, existing methods over-rely on the indoor motion-capture spaces in which datasets were recorded, while simultaneously assuming continuous joint motion capture and uniform body dimensions. We propose EgoPoser to overcome these limitations with four main contributions. 1) EgoPoser robustly models body pose from intermittent hand position and orientation tracking only when inside a headset's field of view. 2) We rethink input representations for headset-based ego-pose estimation and introduce a novel global motion decomposition method that predicts full-body pose independent of global positions. 3) We enhance pose estimation by capturing longer motion time series through an efficient SlowFast module design that maintains computational efficiency. 4) EgoPoser generalizes across various body shapes for different users. We experimentally evaluate our method and show that it outperforms state-of-the-art methods both qualitatively and quantitatively while maintaining a high inference speed of over 600fps. EgoPoser establishes a robust baseline for future work where full-body pose estimation no longer needs to rely on outside-in capture and can scale to large-scale and unseen environments.

## Content
Full-body egocentric pose estimation from head and hand poses alone has become an active area of research to power articulate avatar representations on headset-based platforms. However, existing methods over-rely on the indoor motion-capture spaces in which datasets were recorded, while simultaneously assuming continuous joint motion capture and uniform body dimensions. We propose EgoPoser to overcome these limitations with four main contributions. 1) EgoPoser robustly models body pose from intermittent hand position and orientation tracking only when inside a headset's field of view. 2) We rethink input representations for headset-based ego-pose estimation and introduce a novel global motion decomposition method that predicts full-body pose independent of global positions. 3) We enhance pose estimation by capturing longer motion time series through an efficient SlowFast module design that maintains computational efficiency. 4) EgoPoser generalizes across various body shapes for different users. We experimentally evaluate our method and show that it outperforms state-of-the-art methods both qualitatively and quantitatively while maintaining a high inference speed of over 600fps. EgoPoser establishes a robust baseline for future work where full-body pose estimation no longer needs to rely on outside-in capture and can scale to large-scale and unseen environments.

## 개요
헤드셋 기반 플랫폼에서 정교한 아바타 표현을 구현하기 위해 머리와 손의 포즈만으로 전신 자아 중심 포즈 추정을 수행하는 연구가 활발히 진행되고 있습니다. 그러나 기존 방법들은 데이터셋이 기록된 실내 모션 캡처 공간에 과도하게 의존하는 동시에, 지속적인 관절 움직임 캡처와 균일한 신체 치수를 가정합니다. 본 논문에서는 이러한 한계를 극복하기 위해 EgoPoser를 제안하며, 네 가지 주요 기여를 합니다. 1) EgoPoser는 헤드셋 시야 내에 있을 때만 간헐적인 손 위치 및 방향 추적을 통해 신체 포즈를 강건하게 모델링합니다. 2) 헤드셋 기반 자아 포즈 추정을 위한 입력 표현을 재고하고, 전역 위치와 무관하게 전신 포즈를 예측하는 새로운 전역 움직임 분해 방법을 도입합니다. 3) 효율적인 SlowFast 모듈 설계를 통해 더 긴 움직임 시계열을 포착하여 포즈 추정을 향상시키면서 계산 효율성을 유지합니다. 4) EgoPoser는 다양한 사용자의 여러 신체 형태에 일반화됩니다. 실험적 평가를 통해 본 방법이 정성적 및 정량적으로 최신 방법을 능가하면서도 600fps 이상의 높은 추론 속도를 유지함을 입증합니다. EgoPoser는 향후 전신 포즈 추정이 더 이상 외부에서 내부로의 캡처에 의존하지 않고 대규모 및 미지의 환경으로 확장될 수 있는 강력한 기준선을 제공합니다.

## 핵심 내용
머리와 손의 포즈만으로 전신 자아 중심 포즈 추정을 수행하는 것은 헤드셋 기반 플랫폼에서 정교한 아바타 표현을 구현하기 위해 활발히 연구되는 분야입니다. 그러나 기존 방법들은 데이터셋이 기록된 실내 모션 캡처 공간에 과도하게 의존하며, 지속적인 관절 움직임 캡처와 균일한 신체 치수를 가정합니다. 본 논문에서는 이러한 한계를 극복하기 위해 EgoPoser를 제안하며, 네 가지 주요 기여를 합니다. 1) EgoPoser는 헤드셋 시야 내에 있을 때만 간헐적인 손 위치 및 방향 추적을 통해 신체 포즈를 강건하게 모델링합니다. 2) 헤드셋 기반 자아 포즈 추정을 위한 입력 표현을 재고하고, 전역 위치와 무관하게 전신 포즈를 예측하는 새로운 전역 움직임 분해 방법을 도입합니다. 3) 효율적인 SlowFast 모듈 설계를 통해 더 긴 움직임 시계열을 포착하여 포즈 추정을 향상시키면서 계산 효율성을 유지합니다. 4) EgoPoser는 다양한 사용자의 여러 신체 형태에 일반화됩니다. 실험적 평가를 통해 본 방법이 정성적 및 정량적으로 최신 방법을 능가하면서도 600fps 이상의 높은 추론 속도를 유지함을 입증합니다. EgoPoser는 향후 전신 포즈 추정이 더 이상 외부에서 내부로의 캡처에 의존하지 않고 대규모 및 미지의 환경으로 확장될 수 있는 강력한 기준선을 제공합니다.
