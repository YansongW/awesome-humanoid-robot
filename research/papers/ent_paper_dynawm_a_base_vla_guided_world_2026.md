---
$id: ent_paper_dynawm_a_base_vla_guided_world_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
  zh: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
  ko: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation'
summary:
  en: "arXiv:2607.02604v1 Announce Type: cross \nAbstract: Although vision-language-action (VLA) models have received widespread\
    \ attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward\
    \ or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which\
    \ may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose\
    \ DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA\
    \ checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk\
    \ produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features\
    \ from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states.\
    \ These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for\
    \ moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories\
    \ of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation,\
    \ as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately\
    \ 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and\
    \ 10.94 over SmolVLA, X-VLA, {\\pi}0, and {\\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance\
    \ increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding\
    \ enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed."
  zh: "arXiv:2607.02604v1 Announce Type: cross \nAbstract: Although vision-language-action (VLA) models have received widespread\
    \ attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward\
    \ or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which\
    \ may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose\
    \ DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA\
    \ checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk\
    \ produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features\
    \ from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states.\
    \ These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for\
    \ moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories\
    \ of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation,\
    \ as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately\
    \ 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and\
    \ 10.94 over SmolVLA, X-VLA, {\\pi}0, and {\\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance\
    \ increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding\
    \ enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed."
  ko: "arXiv:2607.02604v1 Announce Type: cross \nAbstract: Although vision-language-action (VLA) models have received widespread\
    \ attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward\
    \ or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which\
    \ may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose\
    \ DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA\
    \ checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk\
    \ produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features\
    \ from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states.\
    \ These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for\
    \ moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories\
    \ of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation,\
    \ as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately\
    \ 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and\
    \ 10.94 over SmolVLA, X-VLA, {\\pi}0, and {\\pi}0.5, respectively. For coarse-tuned base-VLA checkpoints, performance\
    \ increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding\
    \ enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed."
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
- dynawm
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02604v1.
sources:
- id: src_001
  type: paper
  title: 'DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation (arXiv)'
  url: https://arxiv.org/abs/2607.02604
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## 核心内容
Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

## 参考
- http://arxiv.org/abs/2607.02604v1

