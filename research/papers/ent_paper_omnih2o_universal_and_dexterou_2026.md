---
$id: ent_paper_omnih2o_universal_and_dexterou_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning'
  zh: 把遥操作升级成通用身体接口
  ko: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning'
summary:
  en: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning is a knowledge node related
    to paper in the humanoid robot value chain.'
  zh: We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy.
    Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized
    humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB
    camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models
    such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation
    or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop
    an RL-based sim-to-real pipeline, which involves large-scale retargeting a
  ko: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning is a knowledge node related
    to paper in the humanoid robot value chain.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.08858v1.
sources:
- id: src_001
  type: paper
  title: 'OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning (arXiv)'
  url: https://arxiv.org/abs/2406.08858
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 把遥操作升级成通用身体接口 project page
  url: https://omni.human2humanoid.com/
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## 核心内容
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## 参考
- http://arxiv.org/abs/2406.08858v1

## Overview
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## Content
We present OmniH2O (Omni Human-to-Humanoid), a learning-based system for whole-body humanoid teleoperation and autonomy. Using kinematic pose as a universal control interface, OmniH2O enables various ways for a human to control a full-sized humanoid with dexterous hands, including using real-time teleoperation through VR headset, verbal instruction, and RGB camera. OmniH2O also enables full autonomy by learning from teleoperated demonstrations or integrating with frontier models such as GPT-4. OmniH2O demonstrates versatility and dexterity in various real-world whole-body tasks through teleoperation or autonomy, such as playing multiple sports, moving and manipulating objects, and interacting with humans. We develop an RL-based sim-to-real pipeline, which involves large-scale retargeting and augmentation of human motion datasets, learning a real-world deployable policy with sparse sensor input by imitating a privileged teacher policy, and reward designs to enhance robustness and stability. We release the first humanoid whole-body control dataset, OmniH2O-6, containing six everyday tasks, and demonstrate humanoid whole-body skill learning from teleoperated datasets.

## 개요
우리는 OmniH2O(Omni Human-to-Humanoid)를 제시합니다. 이는 학습 기반의 전신 휴머노이드 원격 조작 및 자율 시스템입니다. 운동학적 포즈를 범용 제어 인터페이스로 사용하여, OmniH2O는 인간이 정교한 손을 가진 전신 휴머노이드를 제어할 수 있는 다양한 방법을 제공합니다. 여기에는 VR 헤드셋을 통한 실시간 원격 조작, 음성 명령, RGB 카메라가 포함됩니다. 또한 OmniH2O는 원격 조작 데모를 학습하거나 GPT-4와 같은 최첨단 모델과 통합하여 완전한 자율성을 가능하게 합니다. OmniH2O는 여러 스포츠 수행, 물체 이동 및 조작, 인간과의 상호작용 등 다양한 실제 전신 작업에서 원격 조작 또는 자율성을 통해 다재다능함과 정교함을 보여줍니다. 우리는 RL 기반의 시뮬레이션-실제 파이프라인을 개발했습니다. 여기에는 인간 동작 데이터셋의 대규모 리타겟팅 및 증강, 특권 교사 정책을 모방하여 희소 센서 입력으로 실제 배포 가능한 정책 학습, 강건성과 안정성을 향상시키기 위한 보상 설계가 포함됩니다. 우리는 6가지 일상 작업을 포함한 최초의 휴머노이드 전신 제어 데이터셋인 OmniH2O-6을 공개하고, 원격 조작 데이터셋으로부터 휴머노이드 전신 기술 학습을 시연합니다.

## 핵심 내용
우리는 OmniH2O(Omni Human-to-Humanoid)를 제시합니다. 이는 학습 기반의 전신 휴머노이드 원격 조작 및 자율 시스템입니다. 운동학적 포즈를 범용 제어 인터페이스로 사용하여, OmniH2O는 인간이 정교한 손을 가진 전신 휴머노이드를 제어할 수 있는 다양한 방법을 제공합니다. 여기에는 VR 헤드셋을 통한 실시간 원격 조작, 음성 명령, RGB 카메라가 포함됩니다. 또한 OmniH2O는 원격 조작 데모를 학습하거나 GPT-4와 같은 최첨단 모델과 통합하여 완전한 자율성을 가능하게 합니다. OmniH2O는 여러 스포츠 수행, 물체 이동 및 조작, 인간과의 상호작용 등 다양한 실제 전신 작업에서 원격 조작 또는 자율성을 통해 다재다능함과 정교함을 보여줍니다. 우리는 RL 기반의 시뮬레이션-실제 파이프라인을 개발했습니다. 여기에는 인간 동작 데이터셋의 대규모 리타겟팅 및 증강, 특권 교사 정책을 모방하여 희소 센서 입력으로 실제 배포 가능한 정책 학습, 강건성과 안정성을 향상시키기 위한 보상 설계가 포함됩니다. 우리는 6가지 일상 작업을 포함한 최초의 휴머노이드 전신 제어 데이터셋인 OmniH2O-6을 공개하고, 원격 조작 데이터셋으로부터 휴머노이드 전신 기술 학습을 시연합니다.
