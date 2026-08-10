---
$id: ent_paper_tacgen_touch_is_a_necessary_di_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with Scalable
    Vision-to-Touch Alignment and Generation'
  zh: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with Scalable
    Vision-to-Touch Alignment and Generation'
  ko: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with Scalable
    Vision-to-Touch Alignment and Generation'
summary:
  en: 'arXiv:2606.29173v2 Announce Type: replace Abstract: Touch resolves the physical-property ambiguity left by vision:
    exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge
    in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data
    scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator
    that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes,
    V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded
    force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation
    0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches
    cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream
    gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer,
    three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks,
    the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent
    properties.'
  zh: TacGen 由研究团队提出，旨在解决触觉数据稀缺问题。其核心贡献是通过视觉-触觉对比对齐与潜在空间残差 MLP 生成器，从 RGB 图像合成触觉潜在表示，实现触觉数据规模化。实验表明，该方法在质量、密度、硬度等物理属性预测上显著优于纯视觉模型，并大幅提升
    TACTO 操作任务性能。
  ko: 'arXiv:2606.29173v2 Announce Type: replace Abstract: Touch resolves the physical-property ambiguity left by vision:
    exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge
    in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data
    scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator
    that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes,
    V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded
    force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation
    0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches
    cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream
    gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer,
    three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks,
    the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent
    properties.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- tacgen
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.29173v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1039 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'TacGen: Touch Is a Necessary Dimension of Physical-World Representation -- Addressing Tactile Data Scarcity with
    Scalable Vision-to-Touch Alignment and Generation'
  url: https://arxiv.org/abs/2606.29173
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
TacGen 结合预定义的视觉-触觉对比对齐与潜在空间残差 MLP 生成器，从 RGB 图像合成触觉潜在表示，从而缓解触觉数据稀缺瓶颈。在匹配 DINOv2 骨干网络、数据划分和探测器的条件下，视觉-触觉联合表示在质量（Delta R²=+0.570）、密度（Delta acc=+0.067）、硬度（+0.117）以及不确定性带力标签（Delta R²=+0.281）上均优于纯视觉模型，所有置信区间均不包含零。该表示将匹配容量的 TACTO 操作任务性能从 0.246 提升至 0.979，而纯视觉容量缩放仅能解释 4.5% 的差距，保留 95.5%。生成器在跨种子设置下达到 +0.589，真实触觉在种子区间内达到 +0.585；架构比较显示，重建质量与表示效用之间存在 13 个百分点的下游差距。

## 核心内容
### 方法
TacGen 采用两阶段策略解决触觉数据稀缺问题：
- **视觉-触觉对比对齐**：预定义的对比学习目标将视觉与触觉表示在共享潜在空间中对齐。
- **潜在空间残差 MLP 生成器**：从 RGB 图像合成触觉潜在表示，实现触觉数据规模化生成。

### 实验设置
- **骨干网络**：所有实验使用匹配的 DINOv2 骨干网络。
- **数据划分与探测器**：采用相同的数据划分和线性探测协议。
- **基准任务**：包括质量、密度、硬度预测，以及不确定性带力标签回归和 TACTO 操作任务。

### 关键结果
- **物理属性预测**：视觉-触觉联合表示在质量（Delta R²=+0.570）、密度（Delta acc=+0.067）、硬度（+0.117）和不确定性带力标签（Delta R²=+0.281）上均显著优于纯视觉模型，所有置信区间不包含零。
- **TACTO 操作任务**：匹配容量的视觉-触觉表示将性能从 0.246 提升至 0.979，而纯视觉容量缩放仅能解释 4.5% 的差距，保留 95.5%。
- **生成器性能**：跨种子设置下达到 +0.589，真实触觉在种子区间内达到 +0.585。
- **架构比较**：重建质量与表示效用之间存在 13 个百分点的下游差距。

### 验证与结论
- 通过五种子 SSVTP/TVL 复现、YCB-Sight 迁移、三种骨干网络检查、排列/随机特征控制、哈希验证清单以及测量力验证检查，结果一致支持触觉为接触依赖属性表示提供了必要的物理证据通道。

## Overview
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## 参考
- http://arxiv.org/abs/2606.29173v2

## 개요
TacGen은 사전 정의된 시각-촉각 대비 정렬과 잠재 공간 잔차 MLP 생성기를 결합하여 RGB 이미지에서 촉각 잠재 표현을 합성함으로써 촉각 데이터 희소성 병목을 완화합니다. DINOv2 백본, 데이터 분할 및 프로브를 일치시킨 조건에서 시각-촉각 결합 표현은 품질(Delta R²=+0.570), 밀도(Delta acc=+0.067), 경도(+0.117) 및 불확실성 밴드 힘 라벨(Delta R²=+0.281)에서 순수 시각 모델보다 우수하며, 모든 신뢰 구간은 0을 포함하지 않습니다. 이 표현은 일치 용량의 TACTO 조작 작업 성능을 0.246에서 0.979로 향상시키며, 순수 시각 용량 확장은 격차의 4.5%만 설명하고 95.5%를 유지합니다. 생성기는 교차 시드 설정에서 +0.589, 시드 구간 내 실제 촉각에서 +0.585를 달성합니다. 아키텍처 비교는 재구성 품질과 표현 효용 사이에 13% 포인트의 하류 격차를 보여줍니다.

## 핵심 내용
### 방법
TacGen은 촉각 데이터 희소성 문제를 해결하기 위해 두 단계 전략을 채택합니다:
- **시각-촉각 대비 정렬**: 사전 정의된 대비 학습 목표가 시각 및 촉각 표현을 공유 잠재 공간에서 정렬합니다.
- **잠재 공간 잔차 MLP 생성기**: RGB 이미지에서 촉각 잠재 표현을 합성하여 촉각 데이터의 대규모 생성을 가능하게 합니다.

### 실험 설정
- **백본 네트워크**: 모든 실험은 일치된 DINOv2 백본을 사용합니다.
- **데이터 분할 및 프로브**: 동일한 데이터 분할 및 선형 프로브 프로토콜을 적용합니다.
- **기준 작업**: 품질, 밀도, 경도 예측, 불확실성 밴드 힘 라벨 회귀 및 TACTO 조작 작업을 포함합니다.

### 핵심 결과
- **물리적 속성 예측**: 시각-촉각 결합 표현은 품질(Delta R²=+0.570), 밀도(Delta acc=+0.067), 경도(+0.117) 및 불확실성 밴드 힘 라벨(Delta R²=+0.281)에서 순수 시각 모델보다 유의미하게 우수하며, 모든 신뢰 구간은 0을 포함하지 않습니다.
- **TACTO 조작 작업**: 일치 용량의 시각-촉각 표현은 성능을 0.246에서 0.979로 향상시키며, 순수 시각 용량 확장은 격차의 4.5%만 설명하고 95.5%를 유지합니다.
- **생성기 성능**: 교차 시드 설정에서 +0.589, 시드 구간 내 실제 촉각에서 +0.585를 달성합니다.
- **아키텍처 비교**: 재구성 품질과 표현 효용 사이에 13% 포인트의 하류 격차가 존재합니다.

### 검증 및 결론
- 5개 시드 SSVTP/TVL 재현, YCB-Sight 전이, 3가지 백본 검사, 순열/무작위 특징 제어, 해시 검증 체크리스트 및 측정 힘 검증을 통해 결과는 일관되게 촉각이 접촉 의존 속성 표현에 필요한 물리적 증거 채널을 제공한다는 것을 지지합니다.
