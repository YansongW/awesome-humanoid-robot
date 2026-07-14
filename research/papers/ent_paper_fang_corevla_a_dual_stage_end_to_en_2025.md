---
$id: ent_paper_fang_corevla_a_dual_stage_end_to_en_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine'
  zh: CoReVLA
  ko: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine'
summary:
  en: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
  zh: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
  ko: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (CoReVLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by College of Transportation, Tongji
    University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- corevla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15968v1.
sources:
- id: src_001
  type: paper
  title: 'CoReVLA: A Dual-Stage End-to-End Autonomous Driving Framework for Long-Tail Scenarios via Collect-and-Refine (arXiv)'
  url: https://arxiv.org/abs/2509.15968
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoReVLA source
  url: https://doi.org/10.48550/arXiv.2509.15968
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 核心内容
Autonomous Driving (AD) systems have made notable progress, but their performance in long-tail, safety-critical scenarios remains limited. These rare cases contribute a disproportionate number of accidents. Vision-Language Action (VLA) models have strong reasoning abilities and offer a potential solution, but their effectiveness is limited by the lack of high-quality data and inefficient learning in such conditions. To address these challenges, we propose CoReVLA, a continual learning end-to-end autonomous driving framework that improves the performance in long-tail scenarios through a dual-stage process of data Collection and behavior Refinement. First, the model is jointly fine-tuned on a mixture of open-source driving QA datasets, allowing it to acquire a foundational understanding of driving scenarios. Next, CoReVLA is deployed within the Cave Automatic Virtual Environment (CAVE) simulation platform, where driver takeover data is collected from real-time interactions. Each takeover indicates a long-tail scenario that CoReVLA fails to handle reliably. Finally, the model is refined via Direct Preference Optimization (DPO), allowing it to learn directly from human preferences and thereby avoid reward hacking caused by manually designed rewards. Extensive open-loop and closed-loop experiments demonstrate that the proposed CoReVLA model can accurately perceive driving scenarios and make appropriate decisions. On the Bench2Drive benchmark, CoReVLA achieves a Driving Score (DS) of 72.18 and a Success Rate (SR) of 50%, outperforming state-of-the-art methods by 7.96 DS and 15% SR under long-tail, safety-critical scenarios. Furthermore, case studies demonstrate the model's ability to continually improve its performance in similar failure-prone scenarios by leveraging past takeover experiences. All codea and preprocessed datasets are available at: https://github.com/FanGShiYuu/CoReVLA

## 参考
- http://arxiv.org/abs/2509.15968v1

