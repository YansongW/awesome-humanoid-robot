---
$id: ent_paper_dvg_wm_disentangled_video_gene_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
  zh: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
  ko: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
summary:
  en: 'arXiv:2606.32028v1 Announce Type: new Abstract: Video-based embodied world models provide an appealing substrate for
    robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement:
    accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands
    expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative
    planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video
    Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning
    and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible
    sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos.
    Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics
    to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO
    and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled
    video generation can be an efficient embodied world model for robotic manipulation.'
  zh: 'arXiv:2606.32028v1 Announce Type: new Abstract: Video-based embodied world models provide an appealing substrate for
    robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement:
    accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands
    expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative
    planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video
    Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning
    and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible
    sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos.
    Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics
    to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO
    and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled
    video generation can be an efficient embodied world model for robotic manipulation.'
  ko: 'arXiv:2606.32028v1 Announce Type: new Abstract: Video-based embodied world models provide an appealing substrate for
    robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement:
    accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands
    expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative
    planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video
    Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning
    and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible
    sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos.
    Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics
    to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO
    and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled
    video generation can be an efficient embodied world model for robotic manipulation.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dvg_wm
- humanoid
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.32028v2.
sources:
- id: src_001
  type: paper
  title: 'DVG-WM: Disentangled Video Generation Enables Efficient Embodied World Model for Robotic Manipulation'
  url: https://arxiv.org/abs/2606.32028
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Video-based embodied world models provide an appealing substrate for robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement: accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos. Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled video generation can be an efficient embodied world model for robotic manipulation.

## 核心内容
Video-based embodied world models provide an appealing substrate for robotic manipulation by predicting future states, yet current approaches remain limited by a fundamental entanglement: accurately modeling dynamics typically requires low-level temporal reasoning, while producing high-resolution frames demands expansive visual synthesis according to high-level semantics. This entanglement results in slow inference speed for iterative planning or too coarse predictions to retain contact-rich details. To solve this dilemma, we present Disentangled Video Generation World Model (DVG-WM), an efficient framework that explicitly decomposes world modeling into dynamics learning and visual synthesis. Conditioned on an initial observation and a language instruction, our model first generates a plausible sequence of intermediate visual states to preview the physical interaction and refines them to obtain high-fidelity videos. Furthermore, an efficient cascading mechanism is proposed, where DVG-WM uses flow matching to directly map the dynamics to video latents, and introduces a latent degradation mechanism to regenerate contact-rich details. Experiments on LIBERO and real-world platforms demonstrate improved video quality with up to 3.97 times acceleration, validating that disentangled video generation can be an efficient embodied world model for robotic manipulation.

## 参考
- http://arxiv.org/abs/2606.32028v2

