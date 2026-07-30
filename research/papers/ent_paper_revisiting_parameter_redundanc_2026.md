---
$id: ent_paper_revisiting_parameter_redundanc_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation'
  zh: 'Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation'
  ko: 'Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation'
summary:
  en: 'arXiv:2606.31382v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have made significant strides in
    embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However,
    the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity
    to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning
    or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed parameters
    are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm masks the indiscriminate
    pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA adaptation, first quantifying
    the spatial distribution of parameter divergence during adaptation to reveal structured patterns across different modules.
    Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing the direct impact of removing different
    parameter subsets on VLA performance without any fine-tuning, we establish a causal link between adaptation-induced divergence
    signals and functional contributions. Based on the discovered modular heterogeneities, we design a multi-module joint
    pruning scheme. Evaluations on the LIBERO benchmark demonstrate that our approach reduces the parameters of OpenVLA and
    $\pi_{0.5}$ by 12\%--30\% while maintaining approximately 90\% of the original performance without any post-pruning recovery.
    In contrast, existing parameter pruning criteria result in total performance collapse when evaluated under the same recovery-free
    constraints. Our study reveals the parameter evolution mechanism in VLA adaptation and provides a new path for deploying
    efficient, robust robotic policies in resource-constrained environments.'
  zh: 本文挑战了视觉-语言-动作（VLA）模型剪枝后必须通过微调恢复性能的常规认知。作者通过分析VLM到VLA适配过程中的参数发散空间分布，发现不同模块存在结构化冗余差异，并据此提出一种无需后恢复的多模块联合剪枝方案。在LIBERO基准上，该方法将OpenVLA和π₀.₅的参数量减少12%–30%，同时保持约90%的原始性能。
  ko: 'arXiv:2606.31382v1 Announce Type: new Abstract: Vision-Language-Action (VLA) models have made significant strides in
    embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However,
    the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity
    to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning
    or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed parameters
    are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm masks the indiscriminate
    pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA adaptation, first quantifying
    the spatial distribution of parameter divergence during adaptation to reveal structured patterns across different modules.
    Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing the direct impact of removing different
    parameter subsets on VLA performance without any fine-tuning, we establish a causal link between adaptation-induced divergence
    signals and functional contributions. Based on the discovered modular heterogeneities, we design a multi-module joint
    pruning scheme. Evaluations on the LIBERO benchmark demonstrate that our approach reduces the parameters of OpenVLA and
    $\pi_{0.5}$ by 12\%--30\% while maintaining approximately 90\% of the original performance without any post-pruning recovery.
    In contrast, existing parameter pruning criteria result in total performance collapse when evaluated under the same recovery-free
    constraints. Our study reveals the parameter evolution mechanism in VLA adaptation and provides a new path for deploying
    efficient, robust robotic policies in resource-constrained environments.'
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
- revisiting_parameter_redundanc
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31382v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation'
  url: https://arxiv.org/abs/2606.31382
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
该研究重新审视了VLA模型中的参数冗余问题，指出当前剪枝范式可能因无差别移除关键参数而导致性能下降，进而依赖微调恢复。作者从VLM到VLA适配的视角出发，量化了适配过程中参数发散的空间分布，揭示了不同模块间的结构化模式。通过引入无微调的控制剪枝作为诊断工具，他们建立了适配诱导发散信号与功能贡献之间的因果关系。基于发现的模块异质性，设计的多模块联合剪枝方案在LIBERO基准上验证了有效性，实现了12%–30%的参数缩减，同时保持约90%的原始性能，且无需任何后剪枝恢复。

## 核心内容
### 核心问题与动机
- VLA模型通过整合预训练VLM的强大表征在具身智能中取得显著进展，但其庞大的参数量带来沉重计算负担，且对参数剪枝极度敏感。
- 现有范式通常将剪枝后的性能退化视为不可避免，依赖微调或低秩校正来恢复效果。本文质疑：如果VLA剪枝必须通过性能恢复才能生效，那么被移除的参数是否真正冗余？这种范式是否掩盖了对关键参数的无差别剪枝？

### 方法与架构
- **参数发散空间分布量化**：从VLM到VLA适配的视角出发，首次量化适配过程中参数发散的空间分布，揭示不同模块（如视觉编码器、语言编码器、动作解码器）间的结构化模式。
- **控制剪枝作为诊断探针**：引入无微调的控制剪枝，通过比较移除不同参数子集对VLA性能的直接冲击，建立适配诱导发散信号与功能贡献之间的因果联系。
- **多模块联合剪枝方案**：基于发现的模块异质性（即不同模块对剪枝的敏感度不同），设计联合剪枝策略，避免无差别移除关键参数。

### 实验设置与关键结果
- **基准与模型**：在LIBERO基准上评估，测试模型包括OpenVLA和π₀.₅。
- **性能表现**：该方法将OpenVLA和π₀.₅的参数量减少12%–30%，同时保持约90%的原始性能，且无需任何后剪枝恢复（如微调或低秩校正）。
- **对比分析**：在相同的无恢复约束下，现有参数剪枝准则（如基于幅度或梯度的剪枝）导致性能完全崩溃，验证了本文方法的有效性。

### 结论与意义
- 该研究揭示了VLA适配中的参数演化机制，表明参数冗余并非均匀分布，而是呈现模块化结构。
- 为资源受限环境中部署高效、鲁棒的机器人策略提供了新路径，无需依赖昂贵的后剪枝恢复步骤。

## Overview
Vision-Language-Action (VLA) models have made significant strides in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However, the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that our approach reduces the parameters of OpenVLA and $π_{0.5}$ by 12\%--30\% while maintaining approximately 90\% of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained environments.

## 개요
Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Models (VLM)의 강력한 표현을 통합하여 구현 지능 분야에서 큰 진전을 이루었습니다. 그러나 VLA의 방대한 파라미터 규모는 심각한 계산 부담을 초래하며, 이러한 모델은 파라미터 가지치기에 극도로 민감합니다. 현재의 패러다임은 결과적인 성능 저하를 불가피한 것으로 간주하고, 미세 조정이나 저랭크 보정을 통해 효능을 회복하는 데 의존합니다. 우리는 이러한 관행에 도전하며, VLA 가지치기가 효과적이기 위해 성능 회복이 필요하다면 제거된 파라미터가 정말로 중복된 것인지, 아니면 이 패러다임이 중요한 파라미터의 무분별한 가지치기를 가리고 있는지 의문을 제기합니다. 우리는 VLM-to-VLA 적응의 관점에서 파라미터 중복성을 재검토하며, 먼저 적응 중 파라미터 발산의 공간적 분포를 정량화하여 다양한 모듈에 걸친 구조적 패턴을 밝힙니다. 이후, 통제된 가지치기를 진단 도구로 도입합니다: 미세 조정 없이 서로 다른 파라미터 하위 집합을 제거하는 것이 VLA 성능에 미치는 직접적인 영향을 비교함으로써, 적응 유도 발산 신호와 기능적 기여 사이의 인과 관계를 확립합니다. 발견된 모듈 이질성을 바탕으로, 우리는 다중 모듈 공동 가지치기 방식을 설계합니다. LIBERO 벤치마크에서의 평가는 우리의 접근 방식이 OpenVLA와 $π_{0.5}$의 파라미터를 12\%--30\% 줄이면서도 가지치기 후 회복 없이 원래 성능의 약 90\%를 유지함을 보여줍니다. 반대로, 기존 파라미터 가지치기 기준은 동일한 회복 없는 제약 조건에서 평가될 때 완전한 성능 붕괴를 초래합니다. 우리의 연구는 VLA 적응에서의 파라미터 진화 메커니즘을 밝히고, 자원이 제한된 환경에서 효율적이고 강건한 로봇 정책을 배포하기 위한 새로운 경로를 제공합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 사전 훈련된 Vision-Language Models (VLM)의 강력한 표현을 통합하여 구현 지능 분야에서 큰 진전을 이루었습니다. 그러나 VLA의 방대한 파라미터 규모는 심각한 계산 부담을 초래하며, 이러한 모델은 파라미터 가지치기에 극도로 민감합니다. 현재의 패러다임은 결과적인 성능 저하를 불가피한 것으로 간주하고, 미세 조정이나 저랭크 보정을 통해 효능을 회복하는 데 의존합니다. 우리는 이러한 관행에 도전하며, VLA 가지치기가 효과적이기 위해 성능 회복이 필요하다면 제거된 파라미터가 정말로 중복된 것인지, 아니면 이 패러다임이 중요한 파라미터의 무분별한 가지치기를 가리고 있는지 의문을 제기합니다. 우리는 VLM-to-VLA 적응의 관점에서 파라미터 중복성을 재검토하며, 먼저 적응 중 파라미터 발산의 공간적 분포를 정량화하여 다양한 모듈에 걸친 구조적 패턴을 밝힙니다. 이후, 통제된 가지치기를 진단 도구로 도입합니다: 미세 조정 없이 서로 다른 파라미터 하위 집합을 제거하는 것이 VLA 성능에 미치는 직접적인 영향을 비교함으로써, 적응 유도 발산 신호와 기능적 기여 사이의 인과 관계를 확립합니다. 발견된 모듈 이질성을 바탕으로, 우리는 다중 모듈 공동 가지치기 방식을 설계합니다. LIBERO 벤치마크에서의 평가는 우리의 접근 방식이 OpenVLA와 $π_{0.5}$의 파라미터를 12\%--30\% 줄이면서도 가지치기 후 회복 없이 원래 성능의 약 90\%를 유지함을 보여줍니다. 반대로, 기존 파라미터 가지치기 기준은 동일한 회복 없는 제약 조건에서 평가될 때 완전한 성능 붕괴를 초래합니다. 우리의 연구는 VLA 적응에서의 파라미터 진화 메커니즘을 밝히고, 자원이 제한된 환경에서 효율적이고 강건한 로봇 정책을 배포하기 위한 새로운 경로를 제공합니다.

## 参考
- http://arxiv.org/abs/2606.31382v1
