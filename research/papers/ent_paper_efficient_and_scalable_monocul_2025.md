---
$id: ent_paper_efficient_and_scalable_monocul_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
  zh: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
  ko: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction
summary:
  en: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
  zh: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
  ko: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction is a 2025 work on human motion analysis
    and synthesis for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficient_and_scalable_monocul
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00960v3.
sources:
- id: src_001
  type: paper
  title: Efficient and Scalable Monocular Human-Object Interaction Motion Reconstruction (arXiv)
  url: https://arxiv.org/abs/2512.00960
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## 核心内容
Generalized robots must learn from diverse, large-scale human-object interactions (HOI) to operate robustly in the real world. Monocular internet videos offer a nearly limitless and readily available source of data, capturing an unparalleled diversity of human activities, objects, and environments. However, accurately and scalably extracting 4D interaction data from these in-the-wild videos remains a significant and unsolved challenge. To overcome the annotation bottleneck, we introduce an efficient sparse contact annotation paradigm. To scale this process, we develop InterPoint, a multi-modal predictor that drives a human-in-the-loop data engine. Building upon these efficiently acquired annotations, we introduce 4DHOISolver, a novel optimization framework that constrains the ill-posed 4D HOI reconstruction problem, maintaining high spatio-temporal coherence and physical plausibility. Leveraging this framework, we introduce Open4DHOI, a new large-scale 4D HOI dataset featuring a diverse catalog of 135 object types and 133 actions. Furthermore, we demonstrate the effectiveness of our reconstructions by enabling an RL-based agent to imitate the recovered motions. Data and code will be publicly available at https://github.com/wenboran2002/open4dhoi_code.

## 参考
- http://arxiv.org/abs/2512.00960v3

