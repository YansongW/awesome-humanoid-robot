---
$id: ent_paper_from_generated_human_videos_to_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: From Generated Human Videos to Physically Plausible Robot Trajectories
  zh: 生成视频不能直接给机器人用
  ko: From Generated Human Videos to Physically Plausible Robot Trajectories
summary:
  en: From Generated Human Videos to Physically Plausible Robot Trajectories is a knowledge node related to paper in the humanoid
    robot value chain.
  zh: 'Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding
    the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research
    question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This
    challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation
    difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into
    a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement
    learning policy conditioned on 3D keypoints, and trained with symmetry reg'
  ko: From Generated Human Videos to Physically Plausible Robot Trajectories is a knowledge node related to paper in the humanoid
    robot value chain.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- data_collection
- human_demonstration
- human_video
- interaction_fidelity
- motion_retargeting
- teleoperation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.05094v2.
sources:
- id: src_001
  type: paper
  title: From Generated Human Videos to Physically Plausible Robot Trajectories (arXiv)
  url: https://arxiv.org/abs/2512.05094
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 生成视频不能直接给机器人用 project page
  url: https://genmimic.github.io/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## 核心内容
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic-a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## 参考
- http://arxiv.org/abs/2512.05094v2

## Overview
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic—a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## Content
Video generation models are rapidly improving in their ability to synthesize human actions in novel contexts, holding the potential to serve as high-level planners for contextual robot control. To realize this potential, a key research question remains open: how can a humanoid execute the human actions from generated videos in a zero-shot manner? This challenge arises because generated videos are often noisy and exhibit morphological distortions that make direct imitation difficult compared to real video. To address this, we introduce a two-stage pipeline. First, we lift video pixels into a 4D human representation and then retarget to the humanoid morphology. Second, we propose GenMimic—a physics-aware reinforcement learning policy conditioned on 3D keypoints, and trained with symmetry regularization and keypoint-weighted tracking rewards. As a result, GenMimic can mimic human actions from noisy, generated videos. We curate GenMimicBench, a synthetic human-motion dataset generated using two video generation models across a spectrum of actions and contexts, establishing a benchmark for assessing zero-shot generalization and policy robustness. Extensive experiments demonstrate improvements over strong baselines in simulation and confirm coherent, physically stable motion tracking on a Unitree G1 humanoid robot without fine-tuning. This work offers a promising path to realizing the potential of video generation models as high-level policies for robot control.

## 개요
비디오 생성 모델은 새로운 맥락에서 인간의 동작을 합성하는 능력이 빠르게 향상되고 있으며, 상황에 맞는 로봇 제어를 위한 고수준 계획자 역할을 할 잠재력을 지니고 있습니다. 이러한 잠재력을 실현하기 위해 핵심 연구 질문이 남아 있습니다: 휴머노이드가 생성된 비디오의 인간 동작을 제로샷 방식으로 어떻게 실행할 수 있을까? 이는 생성된 비디오가 종종 노이즈가 많고 형태적 왜곡을 보여 실제 비디오에 비해 직접 모방이 어렵기 때문에 발생하는 과제입니다. 이를 해결하기 위해 우리는 두 단계 파이프라인을 도입합니다. 첫째, 비디오 픽셀을 4D 인간 표현으로 변환한 후 휴머노이드 형태로 재타겟팅합니다. 둘째, 3D 키포인트에 조건화되고 대칭 정규화 및 키포인트 가중 추적 보상으로 훈련된 물리 인식 강화 학습 정책인 GenMimic을 제안합니다. 그 결과, GenMimic은 노이즈가 많은 생성된 비디오에서 인간 동작을 모방할 수 있습니다. 우리는 두 가지 비디오 생성 모델을 사용하여 다양한 동작과 맥락에 걸쳐 생성된 합성 인간 동작 데이터셋인 GenMimicBench를 구성하여 제로샷 일반화 및 정책 견고성을 평가하기 위한 벤치마크를 구축합니다. 광범위한 실험을 통해 시뮬레이션에서 강력한 기준선 대비 개선을 입증하고, 미세 조정 없이 Unitree G1 휴머노이드 로봇에서 일관되고 물리적으로 안정적인 동작 추적을 확인했습니다. 이 연구는 비디오 생성 모델을 로봇 제어를 위한 고수준 정책으로 실현할 수 있는 유망한 경로를 제시합니다.

## 핵심 내용
비디오 생성 모델은 새로운 맥락에서 인간의 동작을 합성하는 능력이 빠르게 향상되고 있으며, 상황에 맞는 로봇 제어를 위한 고수준 계획자 역할을 할 잠재력을 지니고 있습니다. 이러한 잠재력을 실현하기 위해 핵심 연구 질문이 남아 있습니다: 휴머노이드가 생성된 비디오의 인간 동작을 제로샷 방식으로 어떻게 실행할 수 있을까? 이는 생성된 비디오가 종종 노이즈가 많고 형태적 왜곡을 보여 실제 비디오에 비해 직접 모방이 어렵기 때문에 발생하는 과제입니다. 이를 해결하기 위해 우리는 두 단계 파이프라인을 도입합니다. 첫째, 비디오 픽셀을 4D 인간 표현으로 변환한 후 휴머노이드 형태로 재타겟팅합니다. 둘째, 3D 키포인트에 조건화되고 대칭 정규화 및 키포인트 가중 추적 보상으로 훈련된 물리 인식 강화 학습 정책인 GenMimic을 제안합니다. 그 결과, GenMimic은 노이즈가 많은 생성된 비디오에서 인간 동작을 모방할 수 있습니다. 우리는 두 가지 비디오 생성 모델을 사용하여 다양한 동작과 맥락에 걸쳐 생성된 합성 인간 동작 데이터셋인 GenMimicBench를 구성하여 제로샷 일반화 및 정책 견고성을 평가하기 위한 벤치마크를 구축합니다. 광범위한 실험을 통해 시뮬레이션에서 강력한 기준선 대비 개선을 입증하고, 미세 조정 없이 Unitree G1 휴머노이드 로봇에서 일관되고 물리적으로 안정적인 동작 추적을 확인했습니다. 이 연구는 비디오 생성 모델을 로봇 제어를 위한 고수준 정책으로 실현할 수 있는 유망한 경로를 제시합니다.
