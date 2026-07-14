---
$id: ent_paper_stemvlaan_open_source_vision_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  zh: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  ko: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
summary:
  en: "arXiv:2602.23721v2 Announce Type: replace \nAbstract: Vision-language-action (VLA) models integrate visual observations\
    \ and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However,\
    \ most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly\
    \ modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning\
    \ and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework\
    \ that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations\
    \ into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future\
    \ spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations.\
    \ Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry\
    \ transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal\
    \ attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly\
    \ modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive\
    \ world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an\
    \ average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset."
  zh: "arXiv:2602.23721v2 Announce Type: replace \nAbstract: Vision-language-action (VLA) models integrate visual observations\
    \ and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However,\
    \ most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly\
    \ modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning\
    \ and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework\
    \ that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations\
    \ into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future\
    \ spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations.\
    \ Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry\
    \ transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal\
    \ attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly\
    \ modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive\
    \ world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an\
    \ average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset."
  ko: "arXiv:2602.23721v2 Announce Type: replace \nAbstract: Vision-language-action (VLA) models integrate visual observations\
    \ and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However,\
    \ most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly\
    \ modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning\
    \ and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework\
    \ that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations\
    \ into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future\
    \ spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations.\
    \ Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry\
    \ transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal\
    \ attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly\
    \ modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive\
    \ world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an\
    \ average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset."
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
- stemvla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.23721v2.
sources:
- id: src_001
  type: paper
  title: StemVLA:An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation
  url: https://arxiv.org/abs/2602.23721
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## 核心内容
Vision-language-action (VLA) models integrate visual observations and language instructions to predict robot actions, demonstrating promising generalization in manipulation tasks. However, most existing approaches primarily rely on direct mappings from 2D visual inputs to action sequences, without explicitly modeling the underlying 3D spatial structure or temporal world dynamics. Such representations may limit spatial reasoning and long-horizon decision-making in dynamic environments. To address this limitation, we propose StemVLA, a novel framework that explicitly incorporates both future-oriented 3D spatial knowledge and historical 4D spatiotemporal representations into action prediction. First, instead of relying solely on observed images, StemVLA forecasts structured 3D future spatial-geometric world knowledge, enabling the model to anticipate upcoming scene geometry and object configurations. Second, to capture temporal consistency and motion dynamics, we feed historical image frames into a pretrained video-geometry transformer backbone to extract implicit 3D world representations, and further aggregate them across time using a temporal attention module, termed VideoFormer [20], forming a unified 4D historical spatiotemporal representation. By jointly modeling 2D observations, predicted 3D future structure, and aggregated 4D temporal dynamics, StemVLA enables more comprehensive world understanding for robot manipulation. Extensive experiments in simulation demonstrate that Stem-VLA achieves an average accuracy of 92.0% across the LIBERO subsets, and 86.0% on the long-horizon LIBERO-Long subset.

## 参考
- http://arxiv.org/abs/2602.23721v2

