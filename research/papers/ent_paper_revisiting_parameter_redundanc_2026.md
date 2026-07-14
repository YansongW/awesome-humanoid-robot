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
  en: "arXiv:2606.31382v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA) models have made significant strides\
    \ in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However,\
    \ the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity\
    \ to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on\
    \ fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed\
    \ parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm\
    \ masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA\
    \ adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured\
    \ patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing\
    \ the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a\
    \ causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular\
    \ heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that\
    \ our approach reduces the parameters of OpenVLA and $\\pi_{0.5}$ by 12\\%--30\\% while maintaining approximately 90\\\
    % of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result\
    \ in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter\
    \ evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained\
    \ environments."
  zh: "arXiv:2606.31382v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA) models have made significant strides\
    \ in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However,\
    \ the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity\
    \ to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on\
    \ fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed\
    \ parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm\
    \ masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA\
    \ adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured\
    \ patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing\
    \ the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a\
    \ causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular\
    \ heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that\
    \ our approach reduces the parameters of OpenVLA and $\\pi_{0.5}$ by 12\\%--30\\% while maintaining approximately 90\\\
    % of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result\
    \ in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter\
    \ evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained\
    \ environments."
  ko: "arXiv:2606.31382v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA) models have made significant strides\
    \ in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However,\
    \ the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity\
    \ to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on\
    \ fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed\
    \ parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm\
    \ masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA\
    \ adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured\
    \ patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing\
    \ the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a\
    \ causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular\
    \ heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that\
    \ our approach reduces the parameters of OpenVLA and $\\pi_{0.5}$ by 12\\%--30\\% while maintaining approximately 90\\\
    % of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result\
    \ in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter\
    \ evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained\
    \ environments."
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31382v1.
sources:
- id: src_001
  type: paper
  title: 'Revisiting Parameter Redundancy in Vision-Language-Action Models: Insights from VLM-to-VLA Adaptation'
  url: https://arxiv.org/abs/2606.31382
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have made significant strides in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However, the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that our approach reduces the parameters of OpenVLA and $π_{0.5}$ by 12\%--30\% while maintaining approximately 90\% of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained environments.

## 核心内容
Vision-Language-Action (VLA) models have made significant strides in embodied intelligence by integrating the powerful representations of pre-trained Vision-Language Models (VLMs). However, the massive parameter scale of VLAs imposes a heavy computational burden, and these models exhibit extreme sensitivity to parameter pruning. Current paradigms often treat the resulting performance degradation as inevitable, relying on fine-tuning or low-rank corrections to recover efficacy. We challenge this convention by questioning whether the removed parameters are truly redundant if VLA pruning necessitates performance recovery to be effective, or if this paradigm masks the indiscriminate pruning of critical parameters. We revisit parameter redundancy through the lens of VLM-to-VLA adaptation, first quantifying the spatial distribution of parameter divergence during adaptation to reveal structured patterns across different modules. Subsequently, we introduce controlled pruning as a diagnostic probe: by comparing the direct impact of removing different parameter subsets on VLA performance without any fine-tuning, we establish a causal link between adaptation-induced divergence signals and functional contributions. Based on the discovered modular heterogeneities, we design a multi-module joint pruning scheme. Evaluations on the LIBERO benchmark demonstrate that our approach reduces the parameters of OpenVLA and $π_{0.5}$ by 12\%--30\% while maintaining approximately 90\% of the original performance without any post-pruning recovery. In contrast, existing parameter pruning criteria result in total performance collapse when evaluated under the same recovery-free constraints. Our study reveals the parameter evolution mechanism in VLA adaptation and provides a new path for deploying efficient, robust robotic policies in resource-constrained environments.

## 参考
- http://arxiv.org/abs/2606.31382v1

