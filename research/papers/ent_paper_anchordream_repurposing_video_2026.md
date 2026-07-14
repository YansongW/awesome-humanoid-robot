---
$id: ent_paper_anchordream_repurposing_video_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
  zh: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
  ko: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis'
summary:
  en: "arXiv:2512.11797v2 Announce Type: replace \nAbstract: The collection of large-scale and diverse robot demonstrations\
    \ remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited\
    \ diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing\
    \ methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies\
    \ that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model\
    \ that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process\
    \ on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments\
    \ consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method\
    \ scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments\
    \ show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of\
    \ 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding\
    \ generative world models in robot motion provides a practical path toward scaling imitation learning."
  zh: "arXiv:2512.11797v2 Announce Type: replace \nAbstract: The collection of large-scale and diverse robot demonstrations\
    \ remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited\
    \ diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing\
    \ methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies\
    \ that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model\
    \ that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process\
    \ on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments\
    \ consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method\
    \ scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments\
    \ show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of\
    \ 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding\
    \ generative world models in robot motion provides a practical path toward scaling imitation learning."
  ko: "arXiv:2512.11797v2 Announce Type: replace \nAbstract: The collection of large-scale and diverse robot demonstrations\
    \ remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited\
    \ diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing\
    \ methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies\
    \ that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model\
    \ that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process\
    \ on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments\
    \ consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method\
    \ scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments\
    \ show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of\
    \ 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding\
    \ generative world models in robot motion provides a practical path toward scaling imitation learning."
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
- anchordream
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11797v2.
sources:
- id: src_001
  type: paper
  title: 'AnchorDream: Repurposing Video Diffusion for Embodiment-Aware Robot Data Synthesis (arXiv)'
  url: https://arxiv.org/abs/2512.11797
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## 核心内容
The collection of large-scale and diverse robot demonstrations remains a major bottleneck for imitation learning, as real-world data acquisition is costly and simulators offer limited diversity and fidelity with pronounced sim-to-real gaps. While generative models present an attractive solution, existing methods often alter only visual appearances without creating new behaviors, or suffer from embodiment inconsistencies that yield implausible motions. To address these limitations, we introduce AnchorDream, an embodiment-aware world model that repurposes pretrained video diffusion models for robot data synthesis. AnchorDream conditions the diffusion process on robot motion renderings, anchoring the embodiment to prevent hallucination while synthesizing objects and environments consistent with the robot's kinematics. Starting from only a handful of human teleoperation demonstrations, our method scales them into large, diverse, high-quality datasets without requiring explicit environment modeling. Experiments show that the generated data leads to consistent improvements in downstream policy learning, with relative gains of 36.4% in simulator benchmarks and nearly double performance in real-world studies. These results suggest that grounding generative world models in robot motion provides a practical path toward scaling imitation learning.

## 参考
- http://arxiv.org/abs/2512.11797v2

