---
$id: ent_paper_zeng_transporter_networks_rearrangi_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation'
  zh: Transporter Networks
  ko: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation'
summary:
  en: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
  zh: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
  ko: 'Transporter Networks: Rearranging the Visual World for Robotic Manipulation (Transporter Networks), is a 2020 generalized
    vision-language-action model for robotic manipulation, introduced by Robotics at Google, and published at CoRL 2020.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- transporter_networks
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2010.14406v3.
sources:
- id: src_001
  type: paper
  title: Transporter Networks source
  url: https://proceedings.mlr.press/v155/zeng21a.html
  date: '2020'
  accessed_at: '2026-07-01'
---
## 概述
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## 核心内容
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## 参考
- http://arxiv.org/abs/2010.14406v3

## Overview
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## Content
Robotic manipulation can be formulated as inducing a sequence of spatial displacements: where the space being moved can encompass an object, part of an object, or end effector. In this work, we propose the Transporter Network, a simple model architecture that rearranges deep features to infer spatial displacements from visual input - which can parameterize robot actions. It makes no assumptions of objectness (e.g. canonical poses, models, or keypoints), it exploits spatial symmetries, and is orders of magnitude more sample efficient than our benchmarked alternatives in learning vision-based manipulation tasks: from stacking a pyramid of blocks, to assembling kits with unseen objects; from manipulating deformable ropes, to pushing piles of small objects with closed-loop feedback. Our method can represent complex multi-modal policy distributions and generalizes to multi-step sequential tasks, as well as 6DoF pick-and-place. Experiments on 10 simulated tasks show that it learns faster and generalizes better than a variety of end-to-end baselines, including policies that use ground-truth object poses. We validate our methods with hardware in the real world. Experiment videos and code are available at https://transporternets.github.io

## 개요
로봇 조작은 일련의 공간적 변위를 유도하는 것으로 정식화될 수 있습니다. 여기서 이동되는 공간은 객체, 객체의 일부 또는 엔드 이펙터를 포함할 수 있습니다. 본 연구에서는 Transporter Network라는 간단한 모델 아키텍처를 제안합니다. 이는 딥 특징을 재배열하여 시각적 입력으로부터 공간적 변위를 추론하며, 이를 통해 로봇 동작을 매개변수화할 수 있습니다. 이 방법은 객체성(예: 표준 자세, 모델 또는 키포인트)에 대한 가정을 하지 않으며, 공간적 대칭성을 활용하고, 벤치마크된 대안들보다 시각 기반 조작 작업 학습에서 샘플 효율성이 훨씬 뛰어납니다. 블록 피라미드 쌓기부터 보지 못한 객체가 포함된 키트 조립, 변형 가능한 로프 조작부터 폐루프 피드백을 통한 작은 객체 더미 밀기까지 다양한 작업을 다룹니다. 우리의 방법은 복잡한 다중 모드 정책 분포를 표현할 수 있으며, 다단계 순차 작업 및 6DoF 픽 앤 플레이스로 일반화됩니다. 10가지 시뮬레이션 작업에 대한 실험은 이 방법이 실제 객체 자세를 사용하는 정책을 포함한 다양한 엔드 투 엔드 기준선보다 더 빠르게 학습하고 더 잘 일반화됨을 보여줍니다. 우리는 실제 하드웨어를 통해 방법을 검증했습니다. 실험 비디오와 코드는 https://transporternets.github.io 에서 확인할 수 있습니다.

## 핵심 내용
로봇 조작은 일련의 공간적 변위를 유도하는 것으로 정식화될 수 있습니다. 여기서 이동되는 공간은 객체, 객체의 일부 또는 엔드 이펙터를 포함할 수 있습니다. 본 연구에서는 Transporter Network라는 간단한 모델 아키텍처를 제안합니다. 이는 딥 특징을 재배열하여 시각적 입력으로부터 공간적 변위를 추론하며, 이를 통해 로봇 동작을 매개변수화할 수 있습니다. 이 방법은 객체성(예: 표준 자세, 모델 또는 키포인트)에 대한 가정을 하지 않으며, 공간적 대칭성을 활용하고, 벤치마크된 대안들보다 시각 기반 조작 작업 학습에서 샘플 효율성이 훨씬 뛰어납니다. 블록 피라미드 쌓기부터 보지 못한 객체가 포함된 키트 조립, 변형 가능한 로프 조작부터 폐루프 피드백을 통한 작은 객체 더미 밀기까지 다양한 작업을 다룹니다. 우리의 방법은 복잡한 다중 모드 정책 분포를 표현할 수 있으며, 다단계 순차 작업 및 6DoF 픽 앤 플레이스로 일반화됩니다. 10가지 시뮬레이션 작업에 대한 실험은 이 방법이 실제 객체 자세를 사용하는 정책을 포함한 다양한 엔드 투 엔드 기준선보다 더 빠르게 학습하고 더 잘 일반화됨을 보여줍니다. 우리는 실제 하드웨어를 통해 방법을 검증했습니다. 실험 비디오와 코드는 https://transporternets.github.io 에서 확인할 수 있습니다.
