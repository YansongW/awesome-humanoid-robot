---
$id: ent_paper_endowing_gpt_4_with_a_humanoid_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World'
  zh: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World'
  ko: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World'
summary:
  en: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World is a 2025
    work on manipulation for humanoid robots.'
  zh: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World is a 2025
    work on manipulation for humanoid robots.'
  ko: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World is a 2025
    work on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- endowing_gpt_4_with_a_humanoid
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.00041v1.
sources:
- id: src_001
  type: paper
  title: 'Endowing GPT-4 with a Humanoid Body: Building the Bridge Between Off-the-Shelf VLMs and the Physical World (arXiv)'
  url: https://arxiv.org/abs/2511.00041
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## 核心内容
Humanoid agents often struggle to handle flexible and diverse interactions in open environments. A common solution is to collect massive datasets to train a highly capable model, but this approach can be prohibitively expensive. In this paper, we explore an alternative solution: empowering off-the-shelf Vision-Language Models (VLMs, such as GPT-4) to control humanoid agents, thereby leveraging their strong open-world generalization to mitigate the need for extensive data collection. To this end, we present \textbf{BiBo} (\textbf{B}uilding humano\textbf{I}d agent \textbf{B}y \textbf{O}ff-the-shelf VLMs). It consists of two key components: (1) an \textbf{embodied instruction compiler}, which enables the VLM to perceive the environment and precisely translate high-level user instructions (e.g., {\small\itshape ``have a rest''}) into low-level primitive commands with control parameters (e.g., {\small\itshape ``sit casually, location: (1, 2), facing: 90$^\circ$''}); and (2) a diffusion-based \textbf{motion executor}, which generates human-like motions from these commands, while dynamically adapting to physical feedback from the environment. In this way, BiBo is capable of handling not only basic interactions but also diverse and complex motions. Experiments demonstrate that BiBo achieves an interaction task success rate of 90.2\% in open environments, and improves the precision of text-guided motion execution by 16.3\% over prior methods. The code will be made publicly available.

## 参考
- http://arxiv.org/abs/2511.00041v1

