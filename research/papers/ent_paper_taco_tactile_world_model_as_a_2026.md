---
$id: ent_paper_taco_tactile_world_model_as_a_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training'
  zh: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training'
  ko: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training'
summary:
  en: "arXiv:2607.02840v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA) models have shown promising generalization\
    \ in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause\
    \ unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level\
    \ semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling\
    \ such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined\
    \ rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent\
    \ trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training\
    \ in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware\
    \ world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile\
    \ generation model imagines local correction segments, and the progress-action model labels them with executable corrective\
    \ actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile\
    \ adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading\
    \ pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile\
    \ corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO\
    \ achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated\
    \ tactile adaptation."
  zh: "arXiv:2607.02840v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA) models have shown promising generalization\
    \ in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause\
    \ unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level\
    \ semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling\
    \ such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined\
    \ rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent\
    \ trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training\
    \ in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware\
    \ world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile\
    \ generation model imagines local correction segments, and the progress-action model labels them with executable corrective\
    \ actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile\
    \ adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading\
    \ pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile\
    \ corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO\
    \ achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated\
    \ tactile adaptation."
  ko: "arXiv:2607.02840v1 Announce Type: new \nAbstract: Vision-Language-Action (VLA) models have shown promising generalization\
    \ in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause\
    \ unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level\
    \ semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling\
    \ such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined\
    \ rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent\
    \ trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training\
    \ in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware\
    \ world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile\
    \ generation model imagines local correction segments, and the progress-action model labels them with executable corrective\
    \ actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile\
    \ adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading\
    \ pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile\
    \ corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO\
    \ achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated\
    \ tactile adaptation."
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
- taco
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02840v1.
sources:
- id: src_001
  type: paper
  title: 'TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training (arXiv)'
  url: https://arxiv.org/abs/2607.02840
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## 核心内容
Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

## 参考
- http://arxiv.org/abs/2607.02840v1

