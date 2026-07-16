---
$id: ent_paper_zhao_learning_fine_grained_bimanual_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
  zh: ACT
  ko: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware
summary:
  en: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Stanford University, UC Berkeley, Meta, and published at Robotics - Science
    and Systems 2023.
  zh: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Stanford University, UC Berkeley, Meta, and published at Robotics - Science
    and Systems 2023.
  ko: Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by Stanford University, UC Berkeley, Meta, and published at Robotics - Science
    and Systems 2023.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- act
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2304.13705v1.
sources:
- id: src_001
  type: website
  title: ACT source
  url: https://doi.org/10.15607/RSS.2023.XIX.016
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback. Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up. Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks? We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface. Imitation learning, however, presents its own challenges, particularly in high-precision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary. To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences. ACT allows the robot to learn 6 difficult tasks in the real world, such as opening a translucent condiment cup and slotting a battery with 80-90% success, with only 10 minutes worth of demonstrations. Project website: https://tonyzhaozh.github.io/aloha/

## 核心内容
Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback. Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up. Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks? We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface. Imitation learning, however, presents its own challenges, particularly in high-precision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary. To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences. ACT allows the robot to learn 6 difficult tasks in the real world, such as opening a translucent condiment cup and slotting a battery with 80-90% success, with only 10 minutes worth of demonstrations. Project website: https://tonyzhaozh.github.io/aloha/

## 参考
- http://arxiv.org/abs/2304.13705v1

## Overview
Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback. Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up. Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks? We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface. Imitation learning, however, presents its own challenges, particularly in high-precision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary. To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences. ACT allows the robot to learn 6 difficult tasks in the real world, such as opening a translucent condiment cup and slotting a battery with 80-90% success, with only 10 minutes worth of demonstrations. Project website: https://tonyzhaozh.github.io/aloha/

## Content
Fine manipulation tasks, such as threading cable ties or slotting a battery, are notoriously difficult for robots because they require precision, careful coordination of contact forces, and closed-loop visual feedback. Performing these tasks typically requires high-end robots, accurate sensors, or careful calibration, which can be expensive and difficult to set up. Can learning enable low-cost and imprecise hardware to perform these fine manipulation tasks? We present a low-cost system that performs end-to-end imitation learning directly from real demonstrations, collected with a custom teleoperation interface. Imitation learning, however, presents its own challenges, particularly in high-precision domains: errors in the policy can compound over time, and human demonstrations can be non-stationary. To address these challenges, we develop a simple yet novel algorithm, Action Chunking with Transformers (ACT), which learns a generative model over action sequences. ACT allows the robot to learn 6 difficult tasks in the real world, such as opening a translucent condiment cup and slotting a battery with 80-90% success, with only 10 minutes worth of demonstrations. Project website: https://tonyzhaozh.github.io/aloha/

## 개요
케이블 타이를 끼우거나 배터리를 장착하는 등의 정밀 조작 작업은 로봇에게 매우 어려운 작업으로 알려져 있습니다. 이러한 작업은 정밀도, 접촉 힘의 세심한 조정, 폐쇄 루프 시각적 피드백이 필요하기 때문입니다. 일반적으로 이러한 작업을 수행하려면 고급 로봇, 정확한 센서 또는 세심한 캘리브레이션이 필요하며, 이는 비용이 많이 들고 설정이 까다롭습니다. 학습을 통해 저비용이고 정밀하지 않은 하드웨어가 이러한 정밀 조작 작업을 수행할 수 있을까요? 본 연구에서는 맞춤형 원격 조작 인터페이스로 수집된 실제 시연으로부터 직접 종단 간 모방 학습을 수행하는 저비용 시스템을 제시합니다. 그러나 모방 학습은 특히 고정밀 분야에서 자체적인 과제를 안고 있습니다. 정책의 오류가 시간이 지남에 따라 누적될 수 있고, 인간의 시연이 비정상적일 수 있다는 점입니다. 이러한 과제를 해결하기 위해 우리는 Action Chunking with Transformers (ACT)라는 간단하면서도 새로운 알고리즘을 개발했습니다. 이는 행동 시퀀스에 대한 생성 모델을 학습합니다. ACT를 통해 로봇은 반투명 조미료 컵 열기, 배터리 장착과 같은 6가지 어려운 실제 작업을 단 10분 분량의 시연만으로 80-90%의 성공률로 학습할 수 있습니다. 프로젝트 웹사이트: https://tonyzhaozh.github.io/aloha/

## 핵심 내용
케이블 타이를 끼우거나 배터리를 장착하는 등의 정밀 조작 작업은 로봇에게 매우 어려운 작업으로 알려져 있습니다. 이러한 작업은 정밀도, 접촉 힘의 세심한 조정, 폐쇄 루프 시각적 피드백이 필요하기 때문입니다. 일반적으로 이러한 작업을 수행하려면 고급 로봇, 정확한 센서 또는 세심한 캘리브레이션이 필요하며, 이는 비용이 많이 들고 설정이 까다롭습니다. 학습을 통해 저비용이고 정밀하지 않은 하드웨어가 이러한 정밀 조작 작업을 수행할 수 있을까요? 본 연구에서는 맞춤형 원격 조작 인터페이스로 수집된 실제 시연으로부터 직접 종단 간 모방 학습을 수행하는 저비용 시스템을 제시합니다. 그러나 모방 학습은 특히 고정밀 분야에서 자체적인 과제를 안고 있습니다. 정책의 오류가 시간이 지남에 따라 누적될 수 있고, 인간의 시연이 비정상적일 수 있다는 점입니다. 이러한 과제를 해결하기 위해 우리는 Action Chunking with Transformers (ACT)라는 간단하면서도 새로운 알고리즘을 개발했습니다. 이는 행동 시퀀스에 대한 생성 모델을 학습합니다. ACT를 통해 로봇은 반투명 조미료 컵 열기, 배터리 장착과 같은 6가지 어려운 실제 작업을 단 10분 분량의 시연만으로 80-90%의 성공률로 학습할 수 있습니다. 프로젝트 웹사이트: https://tonyzhaozh.github.io/aloha/
