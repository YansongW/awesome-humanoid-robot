---
$id: ent_paper_lamp_learning_vision_language_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  zh: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  ko: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
summary:
  en: "arXiv:2603.25399v2 Announce Type: replace-cross \nAbstract: We introduce \\textbf{LaMP}, a dual-expert Vision-Language-Action\
    \ framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress\
    \ actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This\
    \ implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching\
    \ \\emph{Motion Expert} with a policy-predicting \\emph{Action Expert} through gated cross-attention.Specifically, the\
    \ Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert\
    \ without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation\
    \ benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus,\
    \ and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets.\
    \ On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\\% gain over the strongest prior\
    \ baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/."
  zh: "arXiv:2603.25399v2 Announce Type: replace-cross \nAbstract: We introduce \\textbf{LaMP}, a dual-expert Vision-Language-Action\
    \ framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress\
    \ actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This\
    \ implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching\
    \ \\emph{Motion Expert} with a policy-predicting \\emph{Action Expert} through gated cross-attention.Specifically, the\
    \ Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert\
    \ without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation\
    \ benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus,\
    \ and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets.\
    \ On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\\% gain over the strongest prior\
    \ baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/."
  ko: "arXiv:2603.25399v2 Announce Type: replace-cross \nAbstract: We introduce \\textbf{LaMP}, a dual-expert Vision-Language-Action\
    \ framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress\
    \ actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This\
    \ implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching\
    \ \\emph{Motion Expert} with a policy-predicting \\emph{Action Expert} through gated cross-attention.Specifically, the\
    \ Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert\
    \ without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation\
    \ benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus,\
    \ and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets.\
    \ On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\\% gain over the strongest prior\
    \ baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/."
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
- lamp
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2603.25399v2.
sources:
- id: src_001
  type: paper
  title: 'LaMP: Learning Vision-Language-Action Policy with 3D Scene Flow as Latent Motion Prior'
  url: https://arxiv.org/abs/2603.25399
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## 核心内容
We introduce \textbf{LaMP}, a dual-expert Vision-Language-Action framework that embeds dense 3D scene flow as a latent motion prior for robotic manipulation.Existing VLA models regress actions directly from 2D semantic visual features, forcing them to learn complex 3D physical interactions implicitly.This implicit learning strategy degrades under unfamiliar spatial dynamics.LaMP addresses this limitation by aligning a flow-matching \emph{Motion Expert} with a policy-predicting \emph{Action Expert} through gated cross-attention.Specifically, the Motion Expert generates a one-step partially denoised 3D scene flow, and its hidden states condition the Action Expert without full multi-step reconstruction.We evaluate LaMP on the LIBERO, LIBERO-Plus, and SimplerEnv-WidowX simulation benchmarks as well as real-world experiments.LaMP consistently outperforms evaluated VLA baselines across LIBERO, LIBERO-Plus, and SimplerEnv-WidowX benchmarks, achieving the highest reported average success rates under the same training budgets. On LIBERO-Plus OOD perturbations, LaMP shows improved robustness with an average 9.7\% gain over the strongest prior baseline.Our project page is available at https://summerwxk.github.io/lamp-project-page/.

## 参考
- http://arxiv.org/abs/2603.25399v2

