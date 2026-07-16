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
  zh: 'arXiv:2606.29173v2 Announce Type: replace Abstract: Touch resolves the physical-property ambiguity left by vision:
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.29173v2.
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
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## 核心内容
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## 参考
- http://arxiv.org/abs/2606.29173v2

## Overview
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## Content
Touch resolves the physical-property ambiguity left by vision: exploratory contact recovers shape, texture, compliance, and material, and visuo-haptic object representations converge in ventral visual cortex. We ask whether representation learning can reproduce this grounding. TacGen mitigates the tactile-data scarcity bottleneck by combining pre-specified V+T contrastive alignment with a latent-space residual-MLP V->T generator that synthesizes tactile latents from RGB for tactile-data scaling. With matched DINOv2 backbones, splits, and probes, V+T improves matched V-only on mass (Delta R^2=+0.570), density (Delta acc=+0.067), hardness (+0.117), and uncertainty-banded force labels (Delta R^2=+0.281); all CIs exclude zero. The same representation lifts matched-capacity TACTO manipulation 0.246->0.979 while V-only capacity scaling accounts for only 4.5% of the gap, preserving 95.5%. The generator reaches cross-seed +0.589, with real tactile +0.585 inside the seed interval; the architecture comparison shows a 13pp downstream gap between reconstruction quality and representation utility. Across five-seed SSVTP/TVL reproductions, YCB-Sight transfer, three-backbone checks, permutation/random-feature controls, hash-verified manifests, and measured-force validation checks, the evidence supports the claim that touch supplies a necessary physical evidence channel for representations of contact-dependent properties.

## 개요
촉각은 시각이 남긴 물리적 속성의 모호성을 해결합니다. 탐색적 접촉은 형태, 질감, 유연성 및 재질을 복원하며, 시각-촉각 객체 표현은 복측 시각 피질에서 수렴합니다. 우리는 표현 학습이 이러한 기반을 재현할 수 있는지 질문합니다. TacGen은 사전 지정된 V+T 대비 정렬과 잠재 공간 잔차 MLP V->T 생성기를 결합하여 촉각 데이터 희소성 병목 현상을 완화합니다. 이 생성기는 RGB로부터 촉각 잠재 변수를 합성하여 촉각 데이터 확장을 가능하게 합니다. 일치된 DINOv2 백본, 분할 및 프로브를 사용하여 V+T는 일치된 V-only보다 질량(Delta R^2=+0.570), 밀도(Delta acc=+0.067), 경도(+0.117) 및 불확실성 대역 힘 레이블(Delta R^2=+0.281)에서 개선되었습니다. 모든 신뢰 구간은 0을 배제합니다. 동일한 표현은 일치된 용량의 TACTO 조작을 0.246에서 0.979로 향상시키는 반면, V-only 용량 확장은 격차의 4.5%만을 설명하여 95.5%를 유지합니다. 생성기는 교차 시드에서 +0.589에 도달하고, 실제 촉각은 시드 구간 내에서 +0.585를 기록합니다. 아키텍처 비교는 재구성 품질과 표현 유용성 간에 13pp의 하류 격차를 보여줍니다. 5개 시드 SSVTP/TVL 재현, YCB-Sight 전이, 3개 백본 검증, 순열/랜덤 특징 제어, 해시 검증 매니페스트 및 측정된 힘 검증 확인을 통해, 촉각이 접촉 의존적 속성의 표현에 필요한 물리적 증거 채널을 제공한다는 주장을 뒷받침하는 증거가 제시됩니다.

## 핵심 내용
촉각은 시각이 남긴 물리적 속성의 모호성을 해결합니다. 탐색적 접촉은 형태, 질감, 유연성 및 재질을 복원하며, 시각-촉각 객체 표현은 복측 시각 피질에서 수렴합니다. 우리는 표현 학습이 이러한 기반을 재현할 수 있는지 질문합니다. TacGen은 사전 지정된 V+T 대비 정렬과 잠재 공간 잔차 MLP V->T 생성기를 결합하여 촉각 데이터 희소성 병목 현상을 완화합니다. 이 생성기는 RGB로부터 촉각 잠재 변수를 합성하여 촉각 데이터 확장을 가능하게 합니다. 일치된 DINOv2 백본, 분할 및 프로브를 사용하여 V+T는 일치된 V-only보다 질량(Delta R^2=+0.570), 밀도(Delta acc=+0.067), 경도(+0.117) 및 불확실성 대역 힘 레이블(Delta R^2=+0.281)에서 개선되었습니다. 모든 신뢰 구간은 0을 배제합니다. 동일한 표현은 일치된 용량의 TACTO 조작을 0.246에서 0.979로 향상시키는 반면, V-only 용량 확장은 격차의 4.5%만을 설명하여 95.5%를 유지합니다. 생성기는 교차 시드에서 +0.589에 도달하고, 실제 촉각은 시드 구간 내에서 +0.585를 기록합니다. 아키텍처 비교는 재구성 품질과 표현 유용성 간에 13pp의 하류 격차를 보여줍니다. 5개 시드 SSVTP/TVL 재현, YCB-Sight 전이, 3개 백본 검증, 순열/랜덤 특징 제어, 해시 검증 매니페스트 및 측정된 힘 검증 확인을 통해, 촉각이 접촉 의존적 속성의 표현에 필요한 물리적 증거 채널을 제공한다는 주장을 뒷받침하는 증거가 제시됩니다.
