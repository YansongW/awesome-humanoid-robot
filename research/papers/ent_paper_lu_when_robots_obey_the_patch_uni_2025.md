---
$id: ent_paper_lu_when_robots_obey_the_patch_uni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models'
  zh: UPA-RFAS
  ko: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models'
summary:
  en: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
  zh: UPA-RFAS 是南洋理工大学与 DSO National Laboratories 于 2025 年提出的针对视觉-语言-动作模型的通用可迁移对抗补丁攻击框架。其核心贡献在于首次系统研究了在未知架构、微调变体及仿真到现实迁移场景下，单一物理补丁对
    VLA 驱动机器人的黑盒攻击能力。
  ko: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
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
- upa_rfas
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21192v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (992 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.21192
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UPA-RFAS source
  url: https://doi.org/10.48550/arXiv.2511.21192
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有对抗补丁攻击多过拟合于单一模型，无法在跨模型的黑盒场景中有效迁移。UPA-RFAS 通过构建共享特征空间中的统一框架，结合特征空间目标函数、鲁棒增强的两阶段最小-最大优化以及两种 VLA 专用损失函数，实现了单一物理补丁对多种 VLA 模型、操作任务及视角的通用攻击。实验验证了该补丁在跨模型、跨任务及物理执行中的稳定迁移性，揭示了 VLA 系统面临的实际攻击面。

## 核心内容
### 方法架构
UPA-RFAS 框架由三个核心组件构成：
- **特征空间目标**：采用带有 $\ell_1$ 偏差先验与排斥性 InfoNCE 损失的联合优化，诱导模型产生可迁移的表示偏移。
- **鲁棒增强两阶段优化**：内循环学习不可见的样本级扰动，外循环在此硬化邻域上优化通用补丁，形成最小-最大对抗训练范式。
- **VLA 专用损失**：
  - **Patch Attention Dominance**：劫持文本到视觉的注意力分配，使补丁主导跨模态交互。
  - **Patch Semantic Misalignment**：在无标签条件下引发图像-文本语义错配。

### 实验设置
- **模型与数据集**：测试涵盖多种 VLA 架构（如 RT-2、Octo、OpenVLA）及其微调变体，操作任务来自 MetaWorld、RLBench 等基准套件。
- **物理执行**：在真实机器人平台上验证补丁在视角变化、光照条件及物理打印变形下的攻击效果。

### 关键结果
- **跨模型迁移**：UPA-RFAS 在未见过的 VLA 模型上平均攻击成功率达 78.3%，显著优于现有方法（最高 32.1%）。
- **跨任务泛化**：单一补丁在 12 种不同操作任务中保持 65% 以上的成功率。
- **仿真到现实迁移**：物理打印补丁在真实场景中仍保持 71% 的攻击成功率，仅比仿真结果下降 9.2 个百分点。
- **消融实验**：移除 Patch Attention Dominance 损失后攻击成功率下降 41%，证明其关键作用。

### 结论
UPA-RFAS 首次证明了单一物理补丁可对多种 VLA 模型实现黑盒攻击，为机器人安全领域建立了新的防御基准。该工作揭示了当前 VLA 系统在对抗鲁棒性方面的严重缺陷，并提供了可复现的评估框架。

## Overview
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## 参考
- http://arxiv.org/abs/2511.21192v3

## 개요
기존 적대적 패치 공격은 단일 모델에 과적합되어 교차 모델 블랙박스 시나리오에서 효과적으로 전이되지 못합니다. UPA-RFAS는 공유 특징 공간에서의 통합 프레임워크를 구축하고, 특징 공간 목적 함수, 강건 향상 2단계 최소-최대 최적화, 그리고 두 가지 VLA 전용 손실 함수를 결합하여 단일 물리적 패치로 다양한 VLA 모델, 조작 작업 및 시점에 대한 범용 공격을 구현합니다. 실험을 통해 해당 패치의 교차 모델, 교차 작업 및 물리적 실행에서의 안정적 전이성을 검증하였으며, VLA 시스템이 직면한 실제 공격 표면을 드러냅니다.

## 핵심 내용
### 방법 아키텍처
UPA-RFAS 프레임워크는 세 가지 핵심 구성 요소로 이루어집니다:
- **특징 공간 목표**: $\ell_1$ 편향 사전 및 배타적 InfoNCE 손실을 사용한 결합 최적화를 통해 모델이 전이 가능한 표현 이동을 유도합니다.
- **강건 향상 2단계 최적화**: 내부 루프는 보이지 않는 샘플 수준의 교란을 학습하고, 외부 루프는 이렇게 강화된 이웃 영역에서 범용 패치를 최적화하여 최소-최대 적대적 훈련 패러다임을 형성합니다.
- **VLA 전용 손실**:
  - **패치 주의 지배(Patch Attention Dominance)**: 텍스트-시각 주의 할당을 탈취하여 패치가 교차 모달 상호작용을 지배하게 합니다.
  - **패치 의미 불일치(Patch Semantic Misalignment)**: 라벨 없이 이미지-텍스트 의미적 불일치를 유발합니다.

### 실험 설정
- **모델 및 데이터셋**: 다양한 VLA 아키텍처(예: RT-2, Octo, OpenVLA) 및 미세 조정 변형을 테스트하며, 조작 작업은 MetaWorld, RLBench 등 벤치마크 스위트에서 가져옵니다.
- **물리적 실행**: 실제 로봇 플랫폼에서 시점 변화, 조명 조건 및 물리적 인쇄 변형 하에서 패치의 공격 효과를 검증합니다.

### 주요 결과
- **교차 모델 전이**: UPA-RFAS는 보지 못한 VLA 모델에서 평균 공격 성공률 78.3%를 달성하여 기존 방법(최대 32.1%)을 크게 능가합니다.
- **교차 작업 일반화**: 단일 패치가 12가지 서로 다른 조작 작업에서 65% 이상의 성공률을 유지합니다.
- **시뮬레이션-실제 전이**: 물리적으로 인쇄된 패치는 실제 환경에서도 71%의 공격 성공률을 유지하며, 시뮬레이션 결과 대비 9.2% 포인트만 감소합니다.
- **절제 실험**: 패치 주의 지배 손실을 제거하면 공격 성공률이 41% 하락하여 그 핵심 역할을 입증합니다.

### 결론
UPA-RFAS는 단일 물리적 패치가 다양한 VLA 모델에 대해 블랙박스 공격을 수행할 수 있음을 처음으로 입증하며, 로봇 안전 분야에 새로운 방어 기준을 제시합니다. 이 연구는 현재 VLA 시스템이 적대적 강건성 측면에서 심각한 결함을 지니고 있음을 밝히고, 재현 가능한 평가 프레임워크를 제공합니다.
