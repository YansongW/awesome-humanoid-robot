---
$id: ent_paper_sejnova_bridging_language_vision_and_a_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks'
  zh: Bridging Language Vision and Action
  ko: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks'
summary:
  en: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks (Bridging Language Vision and Action),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Czech Technical University in Prague,
    and published at IROS24.'
  zh: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks (Bridging Language Vision and Action),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Czech Technical University in Prague,
    and published at IROS24.'
  ko: 'Bridging Language, Vision and Action: Multimodal VAEs in Robotic Manipulation Tasks (Bridging Language Vision and Action),
    is a 2024 large vision-language-action model for robotic manipulation, introduced by Czech Technical University in Prague,
    and published at IROS24.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bridging_language_vision_and_a
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2404.01932v2.
sources:
- id: src_001
  type: website
  title: Bridging Language Vision and Action source
  url: https://doi.org/10.1109/IROS58592.2024.10802160
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
In this work, we focus on unsupervised vision-language-action mapping in the area of robotic manipulation. Recently, multiple approaches employing pre-trained large language and vision models have been proposed for this task. However, they are computationally demanding and require careful fine-tuning of the produced outputs. A more lightweight alternative would be the implementation of multimodal Variational Autoencoders (VAEs) which can extract the latent features of the data and integrate them into a joint representation, as has been demonstrated mostly on image-image or image-text data for the state-of-the-art models. Here we explore whether and how can multimodal VAEs be employed in unsupervised robotic manipulation tasks in a simulated environment. Based on the obtained results, we propose a model-invariant training alternative that improves the models' performance in a simulator by up to 55%. Moreover, we systematically evaluate the challenges raised by the individual tasks such as object or robot position variability, number of distractors or the task length. Our work thus also sheds light on the potential benefits and limitations of using the current multimodal VAEs for unsupervised learning of robotic motion trajectories based on vision and language.

## 核心内容
In this work, we focus on unsupervised vision-language-action mapping in the area of robotic manipulation. Recently, multiple approaches employing pre-trained large language and vision models have been proposed for this task. However, they are computationally demanding and require careful fine-tuning of the produced outputs. A more lightweight alternative would be the implementation of multimodal Variational Autoencoders (VAEs) which can extract the latent features of the data and integrate them into a joint representation, as has been demonstrated mostly on image-image or image-text data for the state-of-the-art models. Here we explore whether and how can multimodal VAEs be employed in unsupervised robotic manipulation tasks in a simulated environment. Based on the obtained results, we propose a model-invariant training alternative that improves the models' performance in a simulator by up to 55%. Moreover, we systematically evaluate the challenges raised by the individual tasks such as object or robot position variability, number of distractors or the task length. Our work thus also sheds light on the potential benefits and limitations of using the current multimodal VAEs for unsupervised learning of robotic motion trajectories based on vision and language.

## 参考
- http://arxiv.org/abs/2404.01932v2

