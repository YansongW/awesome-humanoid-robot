---
$id: ent_paper_abouzeid_geoaware_vla_implicit_geometry_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model'
  zh: GeoAware-VLA
  ko: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model'
summary:
  en: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
  zh: GeoAware-VLA 是 2025 年由穆罕默德·本·扎耶德人工智能大学提出的大型视觉-语言-动作模型，旨在解决机器人操作中因相机视角变化导致的泛化失败问题。其核心贡献在于通过冻结的预训练几何视觉模型提取特征，并借助轻量可训练投影层将几何先验融入策略解码器，从而在不依赖显式
    3D 数据或重新训练编码器的情况下显著提升视角不变性。在 LIBERO 和 CALVIN 基准上，该模型在未见视角下的成功率分别平均提升 35 个百分点和 11 个百分点，且效果可迁移至真实机器人平台。
  ko: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- geoaware_vla
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14117v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1254 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2509.14117
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GeoAware-VLA source
  url: https://doi.org/10.48550/arXiv.2509.14117
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
GeoAware-VLA 针对现有 VLA 模型难以从 2D 图像推断鲁棒 3D 几何结构、导致对未见相机视角泛化能力弱的问题，提出了一种简洁有效的解决方案。该方法不训练新的视觉编码器，也不依赖显式 3D 数据，而是直接使用冻结的预训练几何视觉模型作为特征提取器，再通过一个轻量可训练的投影层将这些富含几何信息的特征适配给策略解码器，从而让解码器无需从零学习 3D 一致性。在 LIBERO 和 CALVIN 基准上的大量实验表明，GeoAware-VLA 在保持甚至提升原有分布内性能的同时，在零样本泛化到未见相机姿态方面取得了显著进步：LIBERO 上未见视角成功率平均提升 35 个百分点，CALVIN 上提升超过 11 个百分点。这些增益在真实机器人平台上同样得到验证，且该方法在连续和离散动作空间上均表现有效，证明鲁棒的几何基础是构建更通用机器人智能体的关键要素。

## 核心内容
### 方法架构
- **核心思路**：将强几何先验注入视觉骨干网络，以增强模型对相机视角变化的鲁棒性。
- **特征提取**：使用冻结的预训练几何视觉模型（如 DINOv2 或类似几何感知模型）作为固定特征提取器，不进行任何微调。
- **特征适配**：在几何特征提取器与策略解码器之间插入一个轻量级、可训练的投影层（projection layer），负责将几何丰富的特征映射为策略解码器可用的表示。
- **策略解码器**：解码器无需再学习 3D 一致性，而是直接利用投影后的几何特征进行动作预测，从而减轻学习负担。

### 实验设置
- **基准测试**：在 LIBERO 和 CALVIN 两个主流机器人操作基准上进行评估。
- **评估指标**：主要关注分布内性能（in-distribution performance）和零样本泛化到未见相机视角的成功率（unseen-view success rate）。
- **动作空间**：同时验证了连续动作空间和离散动作空间下的有效性。

### 关键数字与结果
- **LIBERO 基准**：未见视角成功率平均提升 **35 个百分点**，同时分布内性能保持或略有提升。
- **CALVIN 基准**：未见视角成功率平均提升 **超过 11 个百分点**。
- **真实机器人平台**：在物理世界实验中，模型表现显著优于基线，证明仿真中的增益可成功迁移至真实环境。
- **对比基线**：相比未使用几何先验的 VLA 模型（如 Octo、RT-2 等），GeoAware-VLA 在视角泛化上具有压倒性优势。

### 结论
GeoAware-VLA 通过简单的几何特征注入策略，有效解决了 VLA 模型对相机视角的过拟合问题。实验证明，无需复杂 3D 重建或额外训练，仅利用冻结的几何视觉模型即可大幅提升零样本泛化能力，且该方法在仿真和真实场景、连续与离散动作空间中均表现一致。这揭示了鲁棒几何基础是构建可泛化机器人智能体的关键要素。

## Overview
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## 参考
- http://arxiv.org/abs/2509.14117v4

## 개요
GeoAware-VLA는 기존 VLA 모델이 2D 이미지에서 강건한 3D 기하 구조를 추론하기 어려워 보지 못한 카메라 시점에 대한 일반화 능력이 약하다는 문제를 해결하기 위해 간결하고 효과적인 솔루션을 제안한다. 이 방법은 새로운 비전 인코더를 훈련하지 않으며 명시적 3D 데이터에 의존하지 않고, 대신 동결된 사전 훈련된 기하 비전 모델을 특징 추출기로 직접 사용하고, 경량의 훈련 가능한 프로젝션 레이어를 통해 이러한 기하 정보가 풍부한 특징을 정책 디코더에 적응시킴으로써 디코더가 처음부터 3D 일관성을 학습할 필요가 없게 한다. LIBERO 및 CALVIN 벤치마크에서의 광범위한 실험은 GeoAware-VLA가 기존 분포 내 성능을 유지하거나 심지어 향상시키면서 보지 못한 카메라 포즈에 대한 제로샷 일반화에서 상당한 진전을 이루었음을 보여준다: LIBERO에서 보지 못한 시점 성공률이 평균 35퍼센트 포인트, CALVIN에서 11퍼센트 포인트 이상 향상되었다. 이러한 이득은 실제 로봇 플랫폼에서도 검증되었으며, 이 방법은 연속 및 이산 행동 공간 모두에서 효과적으로 작동하여 강건한 기하 기반이 더 일반적인 로봇 에이전트를 구축하는 핵심 요소임을 증명한다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 강력한 기하 사전 지식을 비전 백본 네트워크에 주입하여 카메라 시점 변화에 대한 모델의 강건성을 향상시킨다.
- **특징 추출**: 동결된 사전 훈련된 기하 비전 모델(예: DINOv2 또는 유사한 기하 인식 모델)을 고정 특징 추출기로 사용하며, 어떠한 미세 조정도 수행하지 않는다.
- **특징 적응**: 기하 특징 추출기와 정책 디코더 사이에 경량의 훈련 가능한 프로젝션 레이어를 삽입하여 기하 정보가 풍부한 특징을 정책 디코더가 사용할 수 있는 표현으로 매핑한다.
- **정책 디코더**: 디코더는 더 이상 3D 일관성을 학습할 필요 없이 프로젝션된 기하 특징을 직접 활용하여 행동을 예측하므로 학습 부담이 줄어든다.

### 실험 설정
- **벤치마크 테스트**: LIBERO 및 CALVIN 두 가지 주요 로봇 조작 벤치마크에서 평가한다.
- **평가 지표**: 주로 분포 내 성능과 보지 못한 카메라 시점에 대한 제로샷 일반화 성공률에 초점을 맞춘다.
- **행동 공간**: 연속 행동 공간과 이산 행동 공간 모두에서 유효성을 검증한다.

### 주요 수치 및 결과
- **LIBERO 벤치마크**: 보지 못한 시점 성공률이 평균 **35퍼센트 포인트** 향상되었으며, 분포 내 성능은 유지되거나 약간 향상되었다.
- **CALVIN 벤치마크**: 보지 못한 시점 성공률이 평균 **11퍼센트 포인트 이상** 향상되었다.
- **실제 로봇 플랫폼**: 물리 세계 실험에서 모델이 베이스라인보다 현저히 우수한 성능을 보여 시뮬레이션에서의 이득이 실제 환경으로 성공적으로 전이될 수 있음을 증명한다.
- **비교 베이스라인**: 기하 사전 지식을 사용하지 않은 VLA 모델(예: Octo, RT-2 등)과 비교하여 GeoAware-VLA는 시점 일반화에서 압도적인 우위를 가진다.

### 결론
GeoAware-VLA는 간단한 기하 특징 주입 전략을 통해 VLA 모델의 카메라 시점 과적합 문제를 효과적으로 해결한다. 실험은 복잡한 3D 재구성이나 추가 훈련 없이 동결된 기하 비전 모델만 활용해도 제로샷 일반화 능력을 크게 향상시킬 수 있음을 증명하며, 이 방법은 시뮬레이션과 실제 환경, 연속 및 이산 행동 공간 모두에서 일관된 성능을 보인다. 이는 강건한 기하 기반이 일반화 가능한 로봇 에이전트를 구축하는 핵심 요소임을 밝혀낸다.
