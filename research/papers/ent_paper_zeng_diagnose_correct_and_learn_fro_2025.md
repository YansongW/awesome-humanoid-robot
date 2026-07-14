---
$id: ent_paper_zeng_diagnose_correct_and_learn_fro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
  zh: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
  ko: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols
summary:
  en: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
  zh: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
  ko: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (Diagnose Correct and Learn from Manipulation
    Failures via Visual Symbols), is a 2025 large vision-language-action model for robotic manipulation, introduced by Beihang
    University, Shanghai Innovation Institute, Southern University of Science and Technology, Shanghai Jiao Tong University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diagnose_correct_and_learn_fro
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02787v3.
sources:
- id: src_001
  type: paper
  title: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols (arXiv)
  url: https://arxiv.org/abs/2512.02787
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Diagnose Correct and Learn from Manipulation Failures via Visual Symbols source
  url: https://doi.org/10.48550/arXiv.2512.02787
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## 核心内容
Vision-Language-Action (VLA) models have recently achieved remarkable progress in robotic manipulation, yet they remain limited in failure diagnosis and learning from failures. Additionally, existing failure datasets are mostly generated programmatically in simulation, which limits their generalization to the real world. In light of these, we introduce ViFailback, a framework designed to diagnose robotic manipulation failures and provide both textual and visual correction guidance. Our framework utilizes explicit visual symbols to enhance annotation efficiency. We further release the ViFailback dataset, a large-scale collection of 58,126 Visual Question Answering (VQA) pairs along with their corresponding 5,202 real-world manipulation trajectories. Based on the dataset, we establish ViFailback-Bench, a benchmark of 11 fine-grained VQA tasks designed to assess the failure diagnosis and correction abilities of Vision-Language Models (VLMs), featuring ViFailback-Bench Lite for closed-ended and ViFailback-Bench Hard for open-ended evaluation. To demonstrate the effectiveness of our framework, we built the ViFailback-8B VLM, which not only achieves significant overall performance improvement on ViFailback-Bench but also generates visual symbols for corrective action guidance. Finally, by integrating ViFailback-8B with a VLA model, we conduct real-world robotic experiments demonstrating its ability to assist the VLA model in recovering from failures. Project Website: https://x1nyuzhou.github.io/vifailback.github.io/

## 参考
- http://arxiv.org/abs/2512.02787v3

