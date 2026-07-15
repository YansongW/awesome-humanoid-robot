---
$id: ent_paper_mees_what_matters_in_language_condi_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data
  zh: HULC
  ko: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data
summary:
  en: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data (HULC), is a 2022 generalized
    vision-language-action model for robotic manipulation, introduced by University of Freiburg, University of Technology
    Nuremberg, and published at IEEE Robotics Autom. Lett. 2022.
  zh: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data (HULC), is a 2022 generalized
    vision-language-action model for robotic manipulation, introduced by University of Freiburg, University of Technology
    Nuremberg, and published at IEEE Robotics Autom. Lett. 2022.
  ko: What Matters in Language Conditioned Robotic Imitation Learning over Unstructured Data (HULC), is a 2022 generalized
    vision-language-action model for robotic manipulation, introduced by University of Freiburg, University of Technology
    Nuremberg, and published at IEEE Robotics Autom. Lett. 2022.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- hulc
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2204.06252v2.
sources:
- id: src_001
  type: website
  title: HULC source
  url: https://doi.org/10.1109/LRA.2022.3196123
  date: '2022'
  accessed_at: '2026-07-01'
---
## 概述
A long-standing goal in robotics is to build robots that can perform a wide range of daily tasks from perceptions obtained with their onboard sensors and specified only via natural language. While recently substantial advances have been achieved in language-driven robotics by leveraging end-to-end learning from pixels, there is no clear and well-understood process for making various design choices due to the underlying variation in setups. In this paper, we conduct an extensive study of the most critical challenges in learning language conditioned policies from offline free-form imitation datasets. We further identify architectural and algorithmic techniques that improve performance, such as a hierarchical decomposition of the robot control learning, a multimodal transformer encoder, discrete latent plans and a self-supervised contrastive loss that aligns video and language representations. By combining the results of our investigation with our improved model components, we are able to present a novel approach that significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation CALVIN benchmark. We have open-sourced our implementation to facilitate future research in learning to perform many complex manipulation skills in a row specified with natural language. Codebase and trained models available at http://hulc.cs.uni-freiburg.de

## 核心内容
A long-standing goal in robotics is to build robots that can perform a wide range of daily tasks from perceptions obtained with their onboard sensors and specified only via natural language. While recently substantial advances have been achieved in language-driven robotics by leveraging end-to-end learning from pixels, there is no clear and well-understood process for making various design choices due to the underlying variation in setups. In this paper, we conduct an extensive study of the most critical challenges in learning language conditioned policies from offline free-form imitation datasets. We further identify architectural and algorithmic techniques that improve performance, such as a hierarchical decomposition of the robot control learning, a multimodal transformer encoder, discrete latent plans and a self-supervised contrastive loss that aligns video and language representations. By combining the results of our investigation with our improved model components, we are able to present a novel approach that significantly outperforms the state of the art on the challenging language conditioned long-horizon robot manipulation CALVIN benchmark. We have open-sourced our implementation to facilitate future research in learning to perform many complex manipulation skills in a row specified with natural language. Codebase and trained models available at http://hulc.cs.uni-freiburg.de

## 参考
- http://arxiv.org/abs/2204.06252v2

