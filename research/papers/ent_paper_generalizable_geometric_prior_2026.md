---
$id: ent_paper_generalizable_geometric_prior_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation
  zh: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation
  ko: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation
summary:
  en: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation is a 2026 work
    on manipulation for humanoid robots.
  zh: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation is a 2026 work
    on manipulation for humanoid robots.
  ko: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation is a 2026 work
    on manipulation for humanoid robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalizable_geometric_prior
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.09031v1.
sources:
- id: src_001
  type: paper
  title: Generalizable Geometric Prior and Recurrent Spiking Feature Learning for Humanoid Robot Manipulation (arXiv)
  url: https://arxiv.org/abs/2601.09031
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robot manipulation is a crucial research area for executing diverse human-level tasks, involving high-level semantic reasoning and low-level action generation. However, precise scene understanding and sample-efficient learning from human demonstrations remain critical challenges, severely hindering the applicability and generalizability of existing frameworks. This paper presents a novel RGMP-S, Recurrent Geometric-prior Multimodal Policy with Spiking features, facilitating both high-level skill reasoning and data-efficient motion synthesis. To ground high-level reasoning in physical reality, we leverage lightweight 2D geometric inductive biases to enable precise 3D scene understanding within the vision-language model. Specifically, we construct a Long-horizon Geometric Prior Skill Selector that effectively aligns the semantic instructions with spatial constraints, ultimately achieving robust generalization in unseen environments. For the data efficiency issue in robotic action generation, we introduce a Recursive Adaptive Spiking Network. We parameterize robot-object interactions via recursive spiking for spatiotemporal consistency, fully distilling long-horizon dynamic features while mitigating the overfitting issue in sparse demonstration scenarios. Extensive experiments are conducted across the Maniskill simulation benchmark and three heterogeneous real-world robotic systems, encompassing a custom-developed humanoid, a desktop manipulator, and a commercial robotic platform. Empirical results substantiate the superiority of our method over state-of-the-art baselines and validate the efficacy of the proposed modules in diverse generalization scenarios. To facilitate reproducibility, the source code and video demonstrations are publicly available at https://github.com/xtli12/RGMP-S.git.

## 核心内容
Humanoid robot manipulation is a crucial research area for executing diverse human-level tasks, involving high-level semantic reasoning and low-level action generation. However, precise scene understanding and sample-efficient learning from human demonstrations remain critical challenges, severely hindering the applicability and generalizability of existing frameworks. This paper presents a novel RGMP-S, Recurrent Geometric-prior Multimodal Policy with Spiking features, facilitating both high-level skill reasoning and data-efficient motion synthesis. To ground high-level reasoning in physical reality, we leverage lightweight 2D geometric inductive biases to enable precise 3D scene understanding within the vision-language model. Specifically, we construct a Long-horizon Geometric Prior Skill Selector that effectively aligns the semantic instructions with spatial constraints, ultimately achieving robust generalization in unseen environments. For the data efficiency issue in robotic action generation, we introduce a Recursive Adaptive Spiking Network. We parameterize robot-object interactions via recursive spiking for spatiotemporal consistency, fully distilling long-horizon dynamic features while mitigating the overfitting issue in sparse demonstration scenarios. Extensive experiments are conducted across the Maniskill simulation benchmark and three heterogeneous real-world robotic systems, encompassing a custom-developed humanoid, a desktop manipulator, and a commercial robotic platform. Empirical results substantiate the superiority of our method over state-of-the-art baselines and validate the efficacy of the proposed modules in diverse generalization scenarios. To facilitate reproducibility, the source code and video demonstrations are publicly available at https://github.com/xtli12/RGMP-S.git.

## 参考
- http://arxiv.org/abs/2601.09031v1

## Overview
Humanoid robot manipulation is a crucial research area for executing diverse human-level tasks, involving high-level semantic reasoning and low-level action generation. However, precise scene understanding and sample-efficient learning from human demonstrations remain critical challenges, severely hindering the applicability and generalizability of existing frameworks. This paper presents a novel RGMP-S, Recurrent Geometric-prior Multimodal Policy with Spiking features, facilitating both high-level skill reasoning and data-efficient motion synthesis. To ground high-level reasoning in physical reality, we leverage lightweight 2D geometric inductive biases to enable precise 3D scene understanding within the vision-language model. Specifically, we construct a Long-horizon Geometric Prior Skill Selector that effectively aligns the semantic instructions with spatial constraints, ultimately achieving robust generalization in unseen environments. For the data efficiency issue in robotic action generation, we introduce a Recursive Adaptive Spiking Network. We parameterize robot-object interactions via recursive spiking for spatiotemporal consistency, fully distilling long-horizon dynamic features while mitigating the overfitting issue in sparse demonstration scenarios. Extensive experiments are conducted across the Maniskill simulation benchmark and three heterogeneous real-world robotic systems, encompassing a custom-developed humanoid, a desktop manipulator, and a commercial robotic platform. Empirical results substantiate the superiority of our method over state-of-the-art baselines and validate the efficacy of the proposed modules in diverse generalization scenarios. To facilitate reproducibility, the source code and video demonstrations are publicly available at https://github.com/xtli12/RGMP-S.git.

## Content
Humanoid robot manipulation is a crucial research area for executing diverse human-level tasks, involving high-level semantic reasoning and low-level action generation. However, precise scene understanding and sample-efficient learning from human demonstrations remain critical challenges, severely hindering the applicability and generalizability of existing frameworks. This paper presents a novel RGMP-S, Recurrent Geometric-prior Multimodal Policy with Spiking features, facilitating both high-level skill reasoning and data-efficient motion synthesis. To ground high-level reasoning in physical reality, we leverage lightweight 2D geometric inductive biases to enable precise 3D scene understanding within the vision-language model. Specifically, we construct a Long-horizon Geometric Prior Skill Selector that effectively aligns the semantic instructions with spatial constraints, ultimately achieving robust generalization in unseen environments. For the data efficiency issue in robotic action generation, we introduce a Recursive Adaptive Spiking Network. We parameterize robot-object interactions via recursive spiking for spatiotemporal consistency, fully distilling long-horizon dynamic features while mitigating the overfitting issue in sparse demonstration scenarios. Extensive experiments are conducted across the Maniskill simulation benchmark and three heterogeneous real-world robotic systems, encompassing a custom-developed humanoid, a desktop manipulator, and a commercial robotic platform. Empirical results substantiate the superiority of our method over state-of-the-art baselines and validate the efficacy of the proposed modules in diverse generalization scenarios. To facilitate reproducibility, the source code and video demonstrations are publicly available at https://github.com/xtli12/RGMP-S.git.

## 개요
휴머노이드 로봇 조작은 다양한 인간 수준의 작업을 수행하기 위한 중요한 연구 분야로, 고수준의 의미론적 추론과 저수준의 행동 생성을 포함합니다. 그러나 정밀한 장면 이해와 인간 시연으로부터의 샘플 효율적 학습은 여전히 중요한 과제로 남아 있으며, 기존 프레임워크의 적용 가능성과 일반화 능력을 심각하게 저해합니다. 본 논문은 스파이킹 특징을 갖춘 순환 기하학적 사전 다중 모드 정책(RGMP-S)을 제시하여, 고수준의 기술 추론과 데이터 효율적인 동작 합성을 모두 촉진합니다. 고수준 추론을 물리적 현실에 기반하기 위해, 우리는 경량 2D 기하학적 귀납적 편향을 활용하여 비전-언어 모델 내에서 정밀한 3D 장면 이해를 가능하게 합니다. 구체적으로, 장기 기하학적 사전 기술 선택기를 구축하여 의미론적 명령을 공간적 제약 조건과 효과적으로 정렬함으로써, 보지 못한 환경에서 강건한 일반화를 궁극적으로 달성합니다. 로봇 행동 생성의 데이터 효율성 문제를 해결하기 위해, 우리는 순환 적응형 스파이킹 네트워크를 도입합니다. 순환 스파이킹을 통해 로봇-객체 상호작용을 매개변수화하여 시공간적 일관성을 확보하고, 장기 동적 특징을 완전히 추출하면서 희소 시연 시나리오에서의 과적합 문제를 완화합니다. 광범위한 실험은 Maniskill 시뮬레이션 벤치마크와 맞춤형 휴머노이드, 데스크탑 매니퓰레이터, 상업용 로봇 플랫폼을 포함한 세 가지 이기종 실제 로봇 시스템에서 수행되었습니다. 실증 결과는 최신 기준선에 비해 우리 방법의 우수성을 입증하고, 다양한 일반화 시나리오에서 제안된 모듈의 효능을 검증합니다. 재현성을 촉진하기 위해, 소스 코드와 비디오 데모는 https://github.com/xtli12/RGMP-S.git에서 공개적으로 제공됩니다.

## 핵심 내용
휴머노이드 로봇 조작은 다양한 인간 수준의 작업을 실행하기 위한 중요한 연구 분야로, 고수준의 의미론적 추론과 저수준의 행동 생성을 포함합니다. 그러나 정밀한 장면 이해와 인간 시연으로부터의 샘플 효율적 학습은 여전히 중요한 과제로 남아 있으며, 기존 프레임워크의 적용 가능성과 일반화 능력을 심각하게 저해합니다. 본 논문은 스파이킹 특징을 갖춘 순환 기하학적 사전 다중 모드 정책(RGMP-S)을 제시하여, 고수준의 기술 추론과 데이터 효율적인 동작 합성을 모두 촉진합니다. 고수준 추론을 물리적 현실에 기반하기 위해, 우리는 경량 2D 기하학적 귀납적 편향을 활용하여 비전-언어 모델 내에서 정밀한 3D 장면 이해를 가능하게 합니다. 구체적으로, 장기 기하학적 사전 기술 선택기를 구축하여 의미론적 명령을 공간적 제약 조건과 효과적으로 정렬함으로써, 보지 못한 환경에서 강건한 일반화를 궁극적으로 달성합니다. 로봇 행동 생성의 데이터 효율성 문제를 해결하기 위해, 우리는 순환 적응형 스파이킹 네트워크를 도입합니다. 순환 스파이킹을 통해 로봇-객체 상호작용을 매개변수화하여 시공간적 일관성을 확보하고, 장기 동적 특징을 완전히 추출하면서 희소 시연 시나리오에서의 과적합 문제를 완화합니다. 광범위한 실험은 Maniskill 시뮬레이션 벤치마크와 맞춤형 휴머노이드, 데스크탑 매니퓰레이터, 상업용 로봇 플랫폼을 포함한 세 가지 이기종 실제 로봇 시스템에서 수행되었습니다. 실증 결과는 최신 기준선에 비해 우리 방법의 우수성을 입증하고, 다양한 일반화 시나리오에서 제안된 모듈의 효능을 검증합니다. 재현성을 촉진하기 위해, 소스 코드와 비디오 데모는 https://github.com/xtli12/RGMP-S.git에서 공개적으로 제공됩니다.
