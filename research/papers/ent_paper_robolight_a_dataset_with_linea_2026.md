---
$id: ent_paper_robolight_a_dataset_with_linea_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboLight: A Dataset with Linearly Composable Illumination for Robotic Manipulation'
  zh: 'RoboLight: A Dataset with Linearly Composable Illumination for Robotic Manipulation'
  ko: ''
summary:
  en: "arXiv:2603.04249v2 Announce Type: replace \nAbstract: In this paper, we introduce\
    \ RoboLight, the first real-world robotic manipulation dataset capturing synchronized\
    \ episodes under systematically varied lighting conditions. RoboLight consists\
    \ of two components. (a) RoboLight-Real contains 2,800 real-world episodes collected\
    \ in our custom Light Cube setup, a calibrated system equipped with eight programmable\
    \ RGB LED lights. It includes structured illumination variation along three independently\
    \ controlled dimensions: color, direction, and intensity. Each dimension is paired\
    \ with a dedicated task featuring objects of diverse geometries and materials\
    \ to induce perceptual challenges. All image data are recorded in high-dynamic-range\
    \ (HDR) format to preserve radiometric accuracy. Leveraging the linearity of light\
    \ transport, we introduce (b) RoboLight-Synthetic, comprising 196,000 episodes\
    \ synthesized through interpolation in the HDR image space of RoboLight-Real.\
    \ In principle, RoboLight-Synthetic can be arbitrarily expanded by refining the\
    \ interpolation granularity. We further verify the dataset quality through qualitative\
    \ analysis and real-world policy roll-outs, analyzing task difficulty, distributional\
    \ diversity, and the effectiveness of synthesized data. We additionally demonstrate\
    \ three representative use cases of the proposed dataset. The full dataset, along\
    \ with the system software and hardware design, will be released as open-source\
    \ to support continued research."
  zh: "arXiv:2603.04249v2 Announce Type: replace \nAbstract: In this paper, we introduce\
    \ RoboLight, the first real-world robotic manipulation dataset capturing synchronized\
    \ episodes under systematically varied lighting conditions. RoboLight consists\
    \ of two components. (a) RoboLight-Real contains 2,800 real-world episodes collected\
    \ in our custom Light Cube setup, a calibrated system equipped with eight programmable\
    \ RGB LED lights. It includes structured illumination variation along three independently\
    \ controlled dimensions: color, direction, and intensity. Each dimension is paired\
    \ with a dedicated task featuring objects of diverse geometries and materials\
    \ to induce perceptual challenges. All image data are recorded in high-dynamic-range\
    \ (HDR) format to preserve radiometric accuracy. Leveraging the linearity of light\
    \ transport, we introduce (b) RoboLight-Synthetic, comprising 196,000 episodes\
    \ synthesized through interpolation in the HDR image space of RoboLight-Real.\
    \ In principle, RoboLight-Synthetic can be arbitrarily expanded by refining the\
    \ interpolation granularity. We further verify the dataset quality through qualitative\
    \ analysis and real-world policy roll-outs, analyzing task difficulty, distributional\
    \ diversity, and the effectiveness of synthesized data. We additionally demonstrate\
    \ three representative use cases of the proposed dataset. The full dataset, along\
    \ with the system software and hardware design, will be released as open-source\
    \ to support continued research."
  ko: ''
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
- robolight
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-10'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: 'RoboLight: A Dataset with Linearly Composable Illumination for Robotic Manipulation
    (arXiv)'
  url: https://arxiv.org/abs/2603.04249
  date: '2026'
  accessed_at: '2026-07-10'
---

arXiv:2603.04249v2 Announce Type: replace 
Abstract: In this paper, we introduce RoboLight, the first real-world robotic manipulation dataset capturing synchronized episodes under systematically varied lighting conditions. RoboLight consists of two components. (a) RoboLight-Real contains 2,800 real-world episodes collected in our custom Light Cube setup, a calibrated system equipped with eight programmable RGB LED lights. It includes structured illumination variation along three independently controlled dimensions: color, direction, and intensity. Each dimension is paired with a dedicated task featuring objects of diverse geometries and materials to induce perceptual challenges. All image data are recorded in high-dynamic-range (HDR) format to preserve radiometric accuracy. Leveraging the linearity of light transport, we introduce (b) RoboLight-Synthetic, comprising 196,000 episodes synthesized through interpolation in the HDR image space of RoboLight-Real. In principle, RoboLight-Synthetic can be arbitrarily expanded by refining the interpolation granularity. We further verify the dataset quality through qualitative analysis and real-world policy roll-outs, analyzing task difficulty, distributional diversity, and the effectiveness of synthesized data. We additionally demonstrate three representative use cases of the proposed dataset. The full dataset, along with the system software and hardware design, will be released as open-source to support continued research.
