---
$id: ent_paper_towards_spatial_trace_with_rea_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
  zh: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
  ko: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics
summary:
  en: "arXiv:2512.13660v4 Announce Type: replace \nAbstract: Spatial tracing, as a fundamental embodied interaction ability\
    \ for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial\
    \ referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this\
    \ end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal\
    \ spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT).\
    \ Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive\
    \ process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT\
    \ and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop\
    \ scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging\
    \ benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines\
    \ in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance\
    \ on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated\
    \ with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered\
    \ real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer."
  zh: "arXiv:2512.13660v4 Announce Type: replace \nAbstract: Spatial tracing, as a fundamental embodied interaction ability\
    \ for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial\
    \ referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this\
    \ end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal\
    \ spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT).\
    \ Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive\
    \ process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT\
    \ and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop\
    \ scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging\
    \ benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines\
    \ in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance\
    \ on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated\
    \ with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered\
    \ real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer."
  ko: "arXiv:2512.13660v4 Announce Type: replace \nAbstract: Spatial tracing, as a fundamental embodied interaction ability\
    \ for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial\
    \ referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this\
    \ end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal\
    \ spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT).\
    \ Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive\
    \ process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT\
    \ and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop\
    \ scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging\
    \ benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines\
    \ in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance\
    \ on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated\
    \ with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered\
    \ real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer."
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
- towards_spatial_trace_with_rea
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.13660v4.
sources:
- id: src_001
  type: paper
  title: Towards Spatial Trace with Reasoning in Vision-Language Models for Robotics (arXiv)
  url: https://arxiv.org/abs/2512.13660
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## 核心内容
Spatial tracing, as a fundamental embodied interaction ability for robots, is inherently challenging as it requires multi-step metric-grounded reasoning compounded with complex spatial referring and real-world metric measurement. However, existing methods struggle with this compositional task. To this end, we propose RoboTracer, a 3D-aware VLM that first achieves both 3D spatial referring and measuring via a universal spatial encoder and a regression-supervised decoder to enhance scale awareness during supervised fine-tuning (SFT). Moreover, RoboTracer advances multi-step metric-grounded reasoning via reinforcement fine-tuning (RFT) with metric-sensitive process rewards, supervising key intermediate perceptual cues to accurately generate spatial traces. To support SFT and RFT training, we introduce TraceSpatial, a large-scale dataset of 30M QA pairs, spanning outdoor/indoor/tabletop scenes and supporting complex reasoning processes (up to 9 steps). We further present TraceSpatial-Bench, a challenging benchmark filling the gap to evaluate spatial tracing. Experimental results show that RoboTracer surpasses baselines in spatial understanding, measuring, and referring, with an average success rate of 79.1%, and also achieves SOTA performance on TraceSpatial-Bench by a large margin, exceeding Gemini-2.5-Pro by 36% accuracy. Notably, RoboTracer can be integrated with various control policies to execute long-horizon, dynamic tasks across diverse robots (UR5, G1 humanoid) in cluttered real-world scenes. Please see the project page at https://zhoues.github.io/RoboTracer.

## 参考
- http://arxiv.org/abs/2512.13660v4

