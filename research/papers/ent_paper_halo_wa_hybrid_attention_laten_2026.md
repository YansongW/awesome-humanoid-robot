---
$id: ent_paper_halo_wa_hybrid_attention_laten_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models'
  zh: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models'
  ko: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models'
summary:
  en: 'arXiv:2607.04265v1 Announce Type: new Abstract: World-action (WA) models can generate long-horizon action chunks for
    general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors
    in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA,
    a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features
    and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation
    to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of
    action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction
    requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks,
    where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by
    19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility,
    we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.'
  zh: 'arXiv:2607.04265v1 Announce Type: new Abstract: World-action (WA) models can generate long-horizon action chunks for
    general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors
    in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA,
    a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features
    and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation
    to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of
    action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction
    requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks,
    where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by
    19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility,
    we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.'
  ko: 'arXiv:2607.04265v1 Announce Type: new Abstract: World-action (WA) models can generate long-horizon action chunks for
    general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors
    in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA,
    a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features
    and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation
    to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of
    action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction
    requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks,
    where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by
    19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility,
    we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.'
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
- robotics
- halo_wa
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.04265v1.
sources:
- id: src_001
  type: paper
  title: 'HALO-WA: Hybrid-Attention Latent-Guided Online Reinforcement Learning for World-Action Models (arXiv)'
  url: https://arxiv.org/abs/2607.04265
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.

## 核心内容
World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.

## 参考
- http://arxiv.org/abs/2607.04265v1

## Overview
World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.

## Content
World-action (WA) models can generate long-horizon action chunks for general-purpose robotic manipulation, but they remain vulnerable to calibration, perception, and contact-dynamics errors in real-world precision tasks, often failing in the final few millimeters of alignment or insertion. We propose HALO-WA, a hybrid-attention latent-guided online reinforcement learning (RL) framework for WA models, which leverages latent features and action priors from the WA generation process through a lightweight actor-critic adapter to enable fast online adaptation to real deployment errors. HALO-WA introduces a hybrid-attention structure that preserves the temporal consistency of action chunks while reading task-relevant information from WA latents conditioned on visual context and end-stage correction requirements, thereby producing refined action chunks. We validate HALO-WA on four real-world precision manipulation tasks, where it improves the average success rate from 26.4\% for WA-base to 87.1\%, outperforming the strongest baseline by 19.2 percentage points while requiring only 45--75 minutes of online training per task. To facilitate reproducibility, we further conduct supplementary simulation experiments in RoboTwin and release the code at https://github.com/YeanRoot/HALO-WA.

## 개요
World-action (WA) 모델은 범용 로봇 조작을 위한 장기 행동 청크를 생성할 수 있지만, 실제 정밀 작업에서 캘리브레이션, 인식 및 접촉 역학 오류에 취약하여 정렬이나 삽입의 마지막 몇 밀리미터에서 종종 실패합니다. 우리는 WA 모델을 위한 하이브리드 어텐션 잠재 유도 온라인 강화 학습(RL) 프레임워크인 HALO-WA를 제안합니다. 이는 경량의 액터-크리틱 어댑터를 통해 WA 생성 과정의 잠재 특징과 행동 사전을 활용하여 실제 배포 오류에 빠르게 온라인 적응할 수 있도록 합니다. HALO-WA는 시각적 맥락과 최종 단계 보정 요구 사항에 따라 WA 잠재 변수에서 작업 관련 정보를 읽으면서 행동 청크의 시간적 일관성을 유지하는 하이브리드 어텐션 구조를 도입하여 정제된 행동 청크를 생성합니다. 우리는 네 가지 실제 정밀 조작 작업에서 HALO-WA를 검증했으며, WA-base의 평균 성공률을 26.4%에서 87.1%로 향상시켜 가장 강력한 기준선보다 19.2% 포인트 높은 성능을 보였으며, 작업당 45~75분의 온라인 훈련만 필요로 했습니다. 재현성을 높이기 위해 RoboTwin에서 추가 시뮬레이션 실험을 수행하고 코드를 https://github.com/YeanRoot/HALO-WA에서 공개합니다.

## 핵심 내용
World-action (WA) 모델은 범용 로봇 조작을 위한 장기 행동 청크를 생성할 수 있지만, 실제 정밀 작업에서 캘리브레이션, 인식 및 접촉 역학 오류에 취약하여 정렬이나 삽입의 마지막 몇 밀리미터에서 종종 실패합니다. 우리는 WA 모델을 위한 하이브리드 어텐션 잠재 유도 온라인 강화 학습(RL) 프레임워크인 HALO-WA를 제안합니다. 이는 경량의 액터-크리틱 어댑터를 통해 WA 생성 과정의 잠재 특징과 행동 사전을 활용하여 실제 배포 오류에 빠르게 온라인 적응할 수 있도록 합니다. HALO-WA는 시각적 맥락과 최종 단계 보정 요구 사항에 따라 WA 잠재 변수에서 작업 관련 정보를 읽으면서 행동 청크의 시간적 일관성을 유지하는 하이브리드 어텐션 구조를 도입하여 정제된 행동 청크를 생성합니다. 우리는 네 가지 실제 정밀 조작 작업에서 HALO-WA를 검증했으며, WA-base의 평균 성공률을 26.4%에서 87.1%로 향상시켜 가장 강력한 기준선보다 19.2% 포인트 높은 성능을 보였으며, 작업당 45~75분의 온라인 훈련만 필요로 했습니다. 재현성을 높이기 위해 RoboTwin에서 추가 시뮬레이션 실험을 수행하고 코드를 https://github.com/YeanRoot/HALO-WA에서 공개합니다.
