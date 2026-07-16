---
$id: ent_paper_guo_improving_vision_language_acti_2025_1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Vision-Language-Action Model with Online Reinforcement Learning
  zh: Improving Vision-Language-Action Model with Online Reinforcement Learning
  ko: Improving Vision-Language-Action Model with Online Reinforcement Learning
summary:
  en: Improving Vision-Language-Action Model with Online Reinforcement Learning (Improving Vision-Language-Action Model with
    Online Reinforcement Learning), is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua
    University, University of California, Berkeley, Shanghai Qi Zhi Institute, and published at ICRA25.
  zh: Improving Vision-Language-Action Model with Online Reinforcement Learning (Improving Vision-Language-Action Model with
    Online Reinforcement Learning), is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua
    University, University of California, Berkeley, Shanghai Qi Zhi Institute, and published at ICRA25.
  ko: Improving Vision-Language-Action Model with Online Reinforcement Learning (Improving Vision-Language-Action Model with
    Online Reinforcement Learning), is a 2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua
    University, University of California, Berkeley, Shanghai Qi Zhi Institute, and published at ICRA25.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- improving_vision_language_acti
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.16664v1.
sources:
- id: src_001
  type: website
  title: Improving Vision-Language-Action Model with Online Reinforcement Learning source
  url: https://doi.org/10.1109/ICRA55743.2025.11127299
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models. Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question. In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models. However, we find that directly applying online RL to large VLA models presents significant challenges, including training instability that severely impacts the performance of large models, and computing burdens that exceed the capabilities of most local machines. To address these challenges, we propose iRe-VLA framework, which iterates between Reinforcement Learning and Supervised Learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning. Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## 核心内容
Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models. Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question. In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models. However, we find that directly applying online RL to large VLA models presents significant challenges, including training instability that severely impacts the performance of large models, and computing burdens that exceed the capabilities of most local machines. To address these challenges, we propose iRe-VLA framework, which iterates between Reinforcement Learning and Supervised Learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning. Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## 参考
- http://arxiv.org/abs/2501.16664v1

## Overview
Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models. Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question. In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models. However, we find that directly applying online RL to large VLA models presents significant challenges, including training instability that severely impacts the performance of large models, and computing burdens that exceed the capabilities of most local machines. To address these challenges, we propose iRe-VLA framework, which iterates between Reinforcement Learning and Supervised Learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning. Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## Content
Recent studies have successfully integrated large vision-language models (VLMs) into low-level robotic control by supervised fine-tuning (SFT) with expert robotic datasets, resulting in what we term vision-language-action (VLA) models. Although the VLA models are powerful, how to improve these large models during interaction with environments remains an open question. In this paper, we explore how to further improve these VLA models via Reinforcement Learning (RL), a commonly used fine-tuning technique for large models. However, we find that directly applying online RL to large VLA models presents significant challenges, including training instability that severely impacts the performance of large models, and computing burdens that exceed the capabilities of most local machines. To address these challenges, we propose iRe-VLA framework, which iterates between Reinforcement Learning and Supervised Learning to effectively improve VLA models, leveraging the exploratory benefits of RL while maintaining the stability of supervised learning. Experiments in two simulated benchmarks and a real-world manipulation suite validate the effectiveness of our method.

## 개요
최근 연구들은 전문가 로봇 데이터셋을 활용한 지도 미세 조정(SFT)을 통해 대규모 시각-언어 모델(VLM)을 저수준 로봇 제어에 성공적으로 통합하여, 시각-언어-행동(VLA) 모델을 구축했습니다. VLA 모델은 강력하지만, 환경과의 상호작용 중에 이러한 대규모 모델을 어떻게 개선할지에 대한 문제는 여전히 해결되지 않은 과제입니다. 본 논문에서는 대규모 모델에 일반적으로 사용되는 미세 조정 기법인 강화 학습(RL)을 통해 VLA 모델을 추가로 개선하는 방법을 탐구합니다. 그러나 대규모 VLA 모델에 온라인 RL을 직접 적용할 경우, 대규모 모델의 성능에 심각한 영향을 미치는 훈련 불안정성과 대부분의 로컬 머신의 능력을 초과하는 계산 부담이라는 중요한 문제가 발생함을 발견했습니다. 이러한 문제를 해결하기 위해, 우리는 강화 학습과 지도 학습을 반복적으로 수행하여 VLA 모델을 효과적으로 개선하는 iRe-VLA 프레임워크를 제안합니다. 이 프레임워크는 RL의 탐색적 이점을 활용하면서도 지도 학습의 안정성을 유지합니다. 두 개의 시뮬레이션 벤치마크와 실제 환경 조작 스위트에서의 실험을 통해 우리 방법의 효과성을 검증했습니다.

## 핵심 내용
최근 연구들은 전문가 로봇 데이터셋을 활용한 지도 미세 조정(SFT)을 통해 대규모 시각-언어 모델(VLM)을 저수준 로봇 제어에 성공적으로 통합하여, 시각-언어-행동(VLA) 모델을 구축했습니다. VLA 모델은 강력하지만, 환경과의 상호작용 중에 이러한 대규모 모델을 어떻게 개선할지에 대한 문제는 여전히 해결되지 않은 과제입니다. 본 논문에서는 대규모 모델에 일반적으로 사용되는 미세 조정 기법인 강화 학습(RL)을 통해 VLA 모델을 추가로 개선하는 방법을 탐구합니다. 그러나 대규모 VLA 모델에 온라인 RL을 직접 적용할 경우, 대규모 모델의 성능에 심각한 영향을 미치는 훈련 불안정성과 대부분의 로컬 머신의 능력을 초과하는 계산 부담이라는 중요한 문제가 발생함을 발견했습니다. 이러한 문제를 해결하기 위해, 우리는 강화 학습과 지도 학습을 반복적으로 수행하여 VLA 모델을 효과적으로 개선하는 iRe-VLA 프레임워크를 제안합니다. 이 프레임워크는 RL의 탐색적 이점을 활용하면서도 지도 학습의 안정성을 유지합니다. 두 개의 시뮬레이션 벤치마크와 실제 환경 조작 스위트에서의 실험을 통해 우리 방법의 효과성을 검증했습니다.
