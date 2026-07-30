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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21192v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
Vision-Language-Action (VLA) 모델은 적대적 공격에 취약하지만, 대부분의 기존 패치가 단일 모델에 과적합되어 블랙박스 환경에서 실패하기 때문에 보편적이고 전이 가능한 공격은 아직 충분히 연구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 알려지지 않은 아키텍처, 미세 조정 변형, 시뮬레이션-실제 전환 하에서 VLA 기반 로봇을 대상으로 하는 보편적이고 전이 가능한 적대적 패치에 대한 체계적인 연구를 제시합니다. 우리는 UPA-RFAS(Universal Patch Attack via Robust Feature, Attention, and Semantics)를 소개합니다. 이는 공유된 특징 공간에서 단일 물리적 패치를 학습하면서 교차 모델 전이를 촉진하는 통합 프레임워크입니다. UPA-RFAS는 (i) $\ell_1$ 편차 사전 및 반발 InfoNCE 손실을 포함한 특징 공간 목표를 결합하여 전이 가능한 표현 변화를 유도하고, (ii) 내부 루프가 보이지 않는 샘플별 섭동을 학습하고 외부 루프가 이 강화된 이웃에 대해 보편적 패치를 최적화하는 강건성 강화 2단계 최소-최대 절차, (iii) 두 가지 VLA 특화 손실, 즉 텍스트→비전 주의를 탈취하는 패치 주의 지배(Patch Attention Dominance)와 레이블 없이 이미지-텍스트 불일치를 유도하는 패치 의미 불일치(Patch Semantic Misalignment)를 결합합니다. 다양한 VLA 모델, 조작 스위트, 물리적 실행에 걸친 실험은 UPA-RFAS가 모델, 작업, 시점 간에 일관되게 전이되어 실용적인 패치 기반 공격 표면을 노출하고 향후 방어를 위한 강력한 기준선을 수립함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 적대적 공격에 취약하지만, 대부분의 기존 패치가 단일 모델에 과적합되어 블랙박스 환경에서 실패하기 때문에 보편적이고 전이 가능한 공격은 아직 충분히 연구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 알려지지 않은 아키텍처, 미세 조정 변형, 시뮬레이션-실제 전환 하에서 VLA 기반 로봇을 대상으로 하는 보편적이고 전이 가능한 적대적 패치에 대한 체계적인 연구를 제시합니다. 우리는 UPA-RFAS(Universal Patch Attack via Robust Feature, Attention, and Semantics)를 소개합니다. 이는 공유된 특징 공간에서 단일 물리적 패치를 학습하면서 교차 모델 전이를 촉진하는 통합 프레임워크입니다. UPA-RFAS는 (i) $\ell_1$ 편차 사전 및 반발 InfoNCE 손실을 포함한 특징 공간 목표를 결합하여 전이 가능한 표현 변화를 유도하고, (ii) 내부 루프가 보이지 않는 샘플별 섭동을 학습하고 외부 루프가 이 강화된 이웃에 대해 보편적 패치를 최적화하는 강건성 강화 2단계 최소-최대 절차, (iii) 두 가지 VLA 특화 손실, 즉 텍스트→비전 주의를 탈취하는 패치 주의 지배(Patch Attention Dominance)와 레이블 없이 이미지-텍스트 불일치를 유도하는 패치 의미 불일치(Patch Semantic Misalignment)를 결합합니다. 다양한 VLA 모델, 조작 스위트, 물리적 실행에 걸친 실험은 UPA-RFAS가 모델, 작업, 시점 간에 일관되게 전이되어 실용적인 패치 기반 공격 표면을 노출하고 향후 방어를 위한 강력한 기준선을 수립함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2511.21192v3
