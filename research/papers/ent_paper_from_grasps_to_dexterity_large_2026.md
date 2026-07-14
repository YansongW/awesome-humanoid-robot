---
$id: ent_paper_from_grasps_to_dexterity_large_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
  zh: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
  ko: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
summary:
  en: "arXiv:2606.30749v1 Announce Type: new \nAbstract: Large-scale dexterous grasp\
    \ datasets encode rich priors over hand-object interaction, but their use has\
    \ largely been confined to grasp generation and pick-and-place manipulation. We\
    \ study whether such data can instead support functional dexterity in articulated\
    \ tool use, where a robot must acquire a tool, maintain contact, and operate its\
    \ functional moving parts. We adapt a hierarchical imitation learning framework\
    \ that combines high-level hand sub-goal prediction with a low-level goal-conditioned\
    \ controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale\
    \ dexterous grasp annotations and use it to pretrain the low-level controller.\
    \ The controller is then fine-tuned on downstream task demonstrations. To evaluate\
    \ this setting, we introduce DexCraft, a simulation benchmark with six articulated\
    \ tool-use tasks requiring coordinated finger motion. Across simulation and real-world\
    \ experiments, our approach outperforms end-to-end diffusion policy baselines\
    \ and hierarchical policies trained from scratch. In the real world, it improves\
    \ full-task success by 33.3 percentage points over DP3. These results show that\
    \ grasp datasets can serve not only as resources for grasp synthesis, but also\
    \ as scalable pretraining data for contact-rich dexterous manipulation. Videos\
    \ are shown on https://yingyuan0414.github.io/grasp2dexterity/ ."
  zh: "arXiv:2606.30749v1 Announce Type: new \nAbstract: Large-scale dexterous grasp\
    \ datasets encode rich priors over hand-object interaction, but their use has\
    \ largely been confined to grasp generation and pick-and-place manipulation. We\
    \ study whether such data can instead support functional dexterity in articulated\
    \ tool use, where a robot must acquire a tool, maintain contact, and operate its\
    \ functional moving parts. We adapt a hierarchical imitation learning framework\
    \ that combines high-level hand sub-goal prediction with a low-level goal-conditioned\
    \ controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale\
    \ dexterous grasp annotations and use it to pretrain the low-level controller.\
    \ The controller is then fine-tuned on downstream task demonstrations. To evaluate\
    \ this setting, we introduce DexCraft, a simulation benchmark with six articulated\
    \ tool-use tasks requiring coordinated finger motion. Across simulation and real-world\
    \ experiments, our approach outperforms end-to-end diffusion policy baselines\
    \ and hierarchical policies trained from scratch. In the real world, it improves\
    \ full-task success by 33.3 percentage points over DP3. These results show that\
    \ grasp datasets can serve not only as resources for grasp synthesis, but also\
    \ as scalable pretraining data for contact-rich dexterous manipulation. Videos\
    \ are shown on https://yingyuan0414.github.io/grasp2dexterity/ ."
  ko: "arXiv:2606.30749v1 Announce Type: new \nAbstract: Large-scale dexterous grasp\
    \ datasets encode rich priors over hand-object interaction, but their use has\
    \ largely been confined to grasp generation and pick-and-place manipulation. We\
    \ study whether such data can instead support functional dexterity in articulated\
    \ tool use, where a robot must acquire a tool, maintain contact, and operate its\
    \ functional moving parts. We adapt a hierarchical imitation learning framework\
    \ that combines high-level hand sub-goal prediction with a low-level goal-conditioned\
    \ controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale\
    \ dexterous grasp annotations and use it to pretrain the low-level controller.\
    \ The controller is then fine-tuned on downstream task demonstrations. To evaluate\
    \ this setting, we introduce DexCraft, a simulation benchmark with six articulated\
    \ tool-use tasks requiring coordinated finger motion. Across simulation and real-world\
    \ experiments, our approach outperforms end-to-end diffusion policy baselines\
    \ and hierarchical policies trained from scratch. In the real world, it improves\
    \ full-task success by 33.3 percentage points over DP3. These results show that\
    \ grasp datasets can serve not only as resources for grasp synthesis, but also\
    \ as scalable pretraining data for contact-rich dexterous manipulation. Videos\
    \ are shown on https://yingyuan0414.github.io/grasp2dexterity/ ."
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- from_grasps_to_dexterity
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from arXiv cs.RO RSS feed.
sources:
- id: src_001
  type: paper
  title: 'From Grasps to Dexterity: Large-Scale Grasp Pretraining for Dexterous Manipulation'
  url: https://arxiv.org/abs/2606.30749
  date: '2026'
  accessed_at: '2026-07-01'
---

## 概述
arXiv:2606.30749v1 Announce Type: new 
Abstract: Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

## Overview
arXiv:2606.30749v1 Announce Type: new 
Abstract: Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .

## 개요
arXiv:2606.30749v1 Announce Type: new 
Abstract: Large-scale dexterous grasp datasets encode rich priors over hand-object interaction, but their use has largely been confined to grasp generation and pick-and-place manipulation. We study whether such data can instead support functional dexterity in articulated tool use, where a robot must acquire a tool, maintain contact, and operate its functional moving parts. We adapt a hierarchical imitation learning framework that combines high-level hand sub-goal prediction with a low-level goal-conditioned controller. We construct a 355k-trajectory grasp-pretraining dataset from large-scale dexterous grasp annotations and use it to pretrain the low-level controller. The controller is then fine-tuned on downstream task demonstrations. To evaluate this setting, we introduce DexCraft, a simulation benchmark with six articulated tool-use tasks requiring coordinated finger motion. Across simulation and real-world experiments, our approach outperforms end-to-end diffusion policy baselines and hierarchical policies trained from scratch. In the real world, it improves full-task success by 33.3 percentage points over DP3. These results show that grasp datasets can serve not only as resources for grasp synthesis, but also as scalable pretraining data for contact-rich dexterous manipulation. Videos are shown on https://yingyuan0414.github.io/grasp2dexterity/ .
