---
$id: ent_paper_in_n_on_scaling_egocentric_man_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA'
  zh: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA'
  ko: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA'
summary:
  en: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA is a 2026 work on manipulation for humanoid
    robots.'
  zh: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA is a 2026 work on manipulation for humanoid
    robots.'
  ko: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA is a 2026 work on manipulation for humanoid
    robots.'
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
- in_n_on
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.15704v1.
sources:
- id: src_001
  type: website
  title: 'IN-N-ON: SCALING EGOCENTRIC MANIPULATION WITH IN-THE-WILD AND ON-TASK DATA project page'
  url: https://openreview.net/attachment?id=JoK1hJg0Td&name=pdf
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 核心内容
Egocentric videos are a valuable and scalable data source to learn manipulation policies. However, due to significant data heterogeneity, most existing approaches utilize human data for simple pre-training, which does not unlock its full potential. This paper first provides a scalable recipe for collecting and using egocentric data by categorizing human data into two categories: in-the-wild and on-task alongside with systematic analysis on how to use the data. We first curate a dataset, PHSD, which contains over 1,000 hours of diverse in-the-wild egocentric data and over 20 hours of on-task data directly aligned to the target manipulation tasks. This enables learning a large egocentric language-conditioned flow matching policy, Human0. With domain adaptation techniques, Human0 minimizes the gap between humans and humanoids. Empirically, we show Human0 achieves several novel properties from scaling human data, including language following of instructions from only human data, few-shot learning, and improved robustness using on-task data. Project website: https://xiongyicai.github.io/In-N-On/

## 参考
- http://arxiv.org/abs/2511.15704v1

