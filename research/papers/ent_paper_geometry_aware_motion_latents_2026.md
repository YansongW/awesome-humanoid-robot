---
$id: ent_paper_geometry_aware_motion_latents_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies
  zh: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies
  ko: ''
summary:
  en: "arXiv:2607.04714v1 Announce Type: new \nAbstract: Learning motion latents for\
    \ robotic manipulation heavily relies on extracting motion patterns from visual\
    \ sequences, yet effective action abstractions require understanding three-dimensional\
    \ geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion\
    \ Latents), which learns discrete motion latent codes by predicting how point\
    \ clouds evolve during manipulation rather than reconstructing visual observations.\
    \ This four-dimensional objective -- spatial geometry changing through time --\
    \ forces latent representations to encode actual physical motion rather than appearance\
    \ patterns. GeoMoLa achieves state-of-the-art performance using only single-view\
    \ RGB-D input, while existing methods require multi-view reconstruction, succeeding\
    \ across diverse manipulation benchmarks. Our ablations reveal that geometric\
    \ prediction is the key to driving performance, quantitatively validating that\
    \ manipulation depends on spatial understanding. Furthermore, the learned codes\
    \ exhibit effective motion abstraction: applying them to novel scenes produces\
    \ physically consistent transformations regardless of visual context. Our real-world\
    \ experiments also confirm this robustness capability, achieving robust manipulation\
    \ with minimal demonstrations in cluttered environments where geometric reasoning\
    \ determines success. Thus, we demonstrate that effective motion latents for robot\
    \ control can better emerge from understanding motion through its three-dimensional\
    \ effects rather than pixel-level patterns."
  zh: "arXiv:2607.04714v1 Announce Type: new \nAbstract: Learning motion latents for\
    \ robotic manipulation heavily relies on extracting motion patterns from visual\
    \ sequences, yet effective action abstractions require understanding three-dimensional\
    \ geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion\
    \ Latents), which learns discrete motion latent codes by predicting how point\
    \ clouds evolve during manipulation rather than reconstructing visual observations.\
    \ This four-dimensional objective -- spatial geometry changing through time --\
    \ forces latent representations to encode actual physical motion rather than appearance\
    \ patterns. GeoMoLa achieves state-of-the-art performance using only single-view\
    \ RGB-D input, while existing methods require multi-view reconstruction, succeeding\
    \ across diverse manipulation benchmarks. Our ablations reveal that geometric\
    \ prediction is the key to driving performance, quantitatively validating that\
    \ manipulation depends on spatial understanding. Furthermore, the learned codes\
    \ exhibit effective motion abstraction: applying them to novel scenes produces\
    \ physically consistent transformations regardless of visual context. Our real-world\
    \ experiments also confirm this robustness capability, achieving robust manipulation\
    \ with minimal demonstrations in cluttered environments where geometric reasoning\
    \ determines success. Thus, we demonstrate that effective motion latents for robot\
    \ control can better emerge from understanding motion through its three-dimensional\
    \ effects rather than pixel-level patterns."
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
- geometry_aware_motion_latents
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-08'
  confidence: medium
  notes: Imported via ingestion framework from source_type=paper.
sources:
- id: src_001
  type: paper
  title: Geometry-Aware Motion Latents for Learning Robust Manipulation Policies (arXiv)
  url: https://arxiv.org/abs/2607.04714
  date: '2026'
  accessed_at: '2026-07-08'
---

arXiv:2607.04714v1 Announce Type: new 
Abstract: Learning motion latents for robotic manipulation heavily relies on extracting motion patterns from visual sequences, yet effective action abstractions require understanding three-dimensional geometric transformations. Here, we introduce GeoMoLa (Geometry-Aware Motion Latents), which learns discrete motion latent codes by predicting how point clouds evolve during manipulation rather than reconstructing visual observations. This four-dimensional objective -- spatial geometry changing through time -- forces latent representations to encode actual physical motion rather than appearance patterns. GeoMoLa achieves state-of-the-art performance using only single-view RGB-D input, while existing methods require multi-view reconstruction, succeeding across diverse manipulation benchmarks. Our ablations reveal that geometric prediction is the key to driving performance, quantitatively validating that manipulation depends on spatial understanding. Furthermore, the learned codes exhibit effective motion abstraction: applying them to novel scenes produces physically consistent transformations regardless of visual context. Our real-world experiments also confirm this robustness capability, achieving robust manipulation with minimal demonstrations in cluttered environments where geometric reasoning determines success. Thus, we demonstrate that effective motion latents for robot control can better emerge from understanding motion through its three-dimensional effects rather than pixel-level patterns.
