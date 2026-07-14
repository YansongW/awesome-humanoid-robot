---
$id: ent_paper_deng_stereovla_enhancing_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision'
  zh: StereoVLA
  ko: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision'
summary:
  en: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (StereoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong Kong, Institute of Automation,
    Chinese Academy of Sciences, Beijing Academy of Artificial Intelligence, Xiamen University Malaysia.'
  zh: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (StereoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong Kong, Institute of Automation,
    Chinese Academy of Sciences, Beijing Academy of Artificial Intelligence, Xiamen University Malaysia.'
  ko: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (StereoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Galbot, Peking University, The University of Hong Kong, Institute of Automation,
    Chinese Academy of Sciences, Beijing Academy of Artificial Intelligence, Xiamen University Malaysia.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- stereovla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.21970v2.
sources:
- id: src_001
  type: paper
  title: 'StereoVLA: Enhancing Vision-Language-Action Models with Stereo Vision (arXiv)'
  url: https://arxiv.org/abs/2512.21970
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: StereoVLA source
  url: https://doi.org/10.48550/arXiv.2512.21970
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
While Vision-Language-Action (VLA) models excel in generalist manipulation, they often lack fine-grained spatial awareness and show limited viewpoint robustness. This limitation largely stems from the reliance on pretrained RGB encoders, which lack explicit geometric cues and prioritize semantic alignment over geometric representation. We argue that effective visual representations for VLA models must jointly encode both semantic and geometric information. In this paper, we introduce StereoVLA, the first VLA model to incorporate rich geometric cues from large-scale synthetic stereo data. StereoVLA employs a Geometric-and-Semantic (GeoSem) vision encoder that extracts geometric cues from subtle stereo-view disparities for precise spatial perception, while simultaneously capturing semantic features from pixel observations to support language-conditioned manipulation. Additionally, we introduce two synergistic co-training objectives: Interaction-Region Depth Estimation for precise spatial reasoning, and Camera Parameter Estimation to implicitly align perception and action coordinate systems. Compared with baselines that employ various input modalities, StereoVLA achieves a 33.4% absolute gain in success rate in real-world experiments and demonstrates robustness to near-hemispheric camera perspectives. Project page: https://shengliangd.github.io/StereoVLA-Webpage.

## 核心内容
While Vision-Language-Action (VLA) models excel in generalist manipulation, they often lack fine-grained spatial awareness and show limited viewpoint robustness. This limitation largely stems from the reliance on pretrained RGB encoders, which lack explicit geometric cues and prioritize semantic alignment over geometric representation. We argue that effective visual representations for VLA models must jointly encode both semantic and geometric information. In this paper, we introduce StereoVLA, the first VLA model to incorporate rich geometric cues from large-scale synthetic stereo data. StereoVLA employs a Geometric-and-Semantic (GeoSem) vision encoder that extracts geometric cues from subtle stereo-view disparities for precise spatial perception, while simultaneously capturing semantic features from pixel observations to support language-conditioned manipulation. Additionally, we introduce two synergistic co-training objectives: Interaction-Region Depth Estimation for precise spatial reasoning, and Camera Parameter Estimation to implicitly align perception and action coordinate systems. Compared with baselines that employ various input modalities, StereoVLA achieves a 33.4% absolute gain in success rate in real-world experiments and demonstrates robustness to near-hemispheric camera perspectives. Project page: https://shengliangd.github.io/StereoVLA-Webpage.

## 参考
- http://arxiv.org/abs/2512.21970v2

