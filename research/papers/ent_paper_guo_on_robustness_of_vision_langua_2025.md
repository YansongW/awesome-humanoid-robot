---
$id: ent_paper_guo_on_robustness_of_vision_langua_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
  zh: RobustVLA
  ko: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations
summary:
  en: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
  zh: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
  ko: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (RobustVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Tsinghua University, PKU-Psibot Lab,
    Beihang University, Peking University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- robustvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.00037v4.
sources:
- id: src_001
  type: paper
  title: On Robustness of Vision-Language-Action Model against Multi-Modal Perturbations (arXiv)
  url: https://arxiv.org/abs/2510.00037
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RobustVLA source
  url: https://doi.org/10.48550/arXiv.2510.00037
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In Vision-Language-Actionf(VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## 核心内容
In Vision-Language-Actionf(VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## 参考
- http://arxiv.org/abs/2510.00037v4

## Overview
In Vision-Language-Action (VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## Content
In Vision-Language-Action (VLA) models, robustness to real-world perturbations is critical for deployment. Existing methods target simple visual disturbances, overlooking the broader multi-modal perturbations that arise in actions, instructions, environments, and observations. Here, we first evaluate the robustness of mainstream VLAs under 17 perturbations across four modalities. We find (1) actions as the most fragile modality, (2) Existing visual-robust VLA do not gain robustness in other modality, and (3) pi0 demonstrates superior robustness. To build multi-modal robust VLAs, we propose RobustVLA against perturbations in VLA inputs and outputs. For output robustness, we perform offline robust optimization against worst-case action noise that maximizes mismatch in flow matching objective. This can be seen as adversarial training, label smoothing, and outlier penalization. For input robustness, we enforce consistent actions across input variations that preserve task semantics. To account for multiple perturbations, we formulate robustness as a multi-armed bandit problem and apply an upper confidence bound algorithm to automatically identify the most harmful noise. Experiments on LIBERO demonstrate our RobustVLA delivers absolute gains over baselines of 12.6% on the pi0 backbone and 10.4% on the OpenVLA backbone across all 17 perturbations, achieving 50.6x faster inference than existing visual-robust BYOVLA that requires external LLMs, and a 10.4% gain under mixed perturbations. On the real-world FR5 robot, under four types of multimodal perturbations, RobustVLA shows strong low-data performance, outperforming pi0 by 65.6% success rate with 25 demonstrations. Even with abundant demos, our method still outperform pi0 by 30% success rate. Code and demo videos available at https://github.com/gakakulicc/RobustVLA.

## 개요
Vision-Language-Action(VLA) 모델에서 실제 환경의 교란에 대한 강건성은 배포에 매우 중요합니다. 기존 방법은 단순한 시각적 교란에 초점을 맞추며, 행동, 명령, 환경 및 관찰에서 발생하는 더 광범위한 다중 모달 교란을 간과합니다. 본 연구에서는 먼저 4가지 모달리티에 걸친 17가지 교란 하에서 주류 VLA의 강건성을 평가합니다. 그 결과 (1) 행동이 가장 취약한 모달리티이며, (2) 기존의 시각적 강건 VLA는 다른 모달리티에서 강건성을 확보하지 못하며, (3) pi0가 우수한 강건성을 보임을 발견했습니다. 다중 모달 강건 VLA를 구축하기 위해, 우리는 VLA 입력 및 출력의 교란에 대응하는 RobustVLA를 제안합니다. 출력 강건성을 위해, 흐름 매칭 목표에서 불일치를 최대화하는 최악의 행동 노이즈에 대해 오프라인 강건 최적화를 수행합니다. 이는 적대적 훈련, 레이블 스무딩 및 이상치 페널티 부여로 볼 수 있습니다. 입력 강건성을 위해, 작업 의미를 유지하는 입력 변동 전반에 걸쳐 일관된 행동을 강제합니다. 여러 교란을 처리하기 위해, 강건성을 다중 팔 밴딧 문제로 공식화하고 상한 신뢰 구간 알고리즘을 적용하여 가장 해로운 노이즈를 자동으로 식별합니다. LIBERO 실험에서 RobustVLA는 pi0 백본에서 12.6%, OpenVLA 백본에서 10.4%의 절대적 성능 향상을 모든 17가지 교란에 대해 달성하며, 외부 LLM이 필요한 기존 시각적 강건 BYOVLA보다 50.6배 빠른 추론 속도를 보이고, 혼합 교란 하에서 10.4%의 향상을 보입니다. 실제 FR5 로봇에서 4가지 유형의 다중 모달 교란 하에 RobustVLA는 강력한 저데이터 성능을 보여, 25개의 데모로 pi0보다 65.6% 높은 성공률을 기록합니다. 풍부한 데모가 있어도, 우리 방법은 pi0보다 30% 높은 성공률을 유지합니다. 코드 및 데모 비디오는 https://github.com/gakakulicc/RobustVLA에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action(VLA) 모델에서 실제 환경의 교란에 대한 강건성은 배포에 매우 중요합니다. 기존 방법은 단순한 시각적 교란에 초점을 맞추며, 행동, 명령, 환경 및 관찰에서 발생하는 더 광범위한 다중 모달 교란을 간과합니다. 본 연구에서는 먼저 4가지 모달리티에 걸친 17가지 교란 하에서 주류 VLA의 강건성을 평가합니다. 그 결과 (1) 행동이 가장 취약한 모달리티이며, (2) 기존의 시각적 강건 VLA는 다른 모달리티에서 강건성을 확보하지 못하며, (3) pi0가 우수한 강건성을 보임을 발견했습니다. 다중 모달 강건 VLA를 구축하기 위해, 우리는 VLA 입력 및 출력의 교란에 대응하는 RobustVLA를 제안합니다. 출력 강건성을 위해, 흐름 매칭 목표에서 불일치를 최대화하는 최악의 행동 노이즈에 대해 오프라인 강건 최적화를 수행합니다. 이는 적대적 훈련, 레이블 스무딩 및 이상치 페널티 부여로 볼 수 있습니다. 입력 강건성을 위해, 작업 의미를 유지하는 입력 변동 전반에 걸쳐 일관된 행동을 강제합니다. 여러 교란을 처리하기 위해, 강건성을 다중 팔 밴딧 문제로 공식화하고 상한 신뢰 구간 알고리즘을 적용하여 가장 해로운 노이즈를 자동으로 식별합니다. LIBERO 실험에서 RobustVLA는 pi0 백본에서 12.6%, OpenVLA 백본에서 10.4%의 절대적 성능 향상을 모든 17가지 교란에 대해 달성하며, 외부 LLM이 필요한 기존 시각적 강건 BYOVLA보다 50.6배 빠른 추론 속도를 보이고, 혼합 교란 하에서 10.4%의 향상을 보입니다. 실제 FR5 로봇에서 4가지 유형의 다중 모달 교란 하에 RobustVLA는 강력한 저데이터 성능을 보여, 25개의 데모로 pi0보다 65.6% 높은 성공률을 기록합니다. 풍부한 데모가 있어도, 우리 방법은 pi0보다 30% 높은 성공률을 유지합니다. 코드 및 데모 비디오는 https://github.com/gakakulicc/RobustVLA에서 확인할 수 있습니다.
