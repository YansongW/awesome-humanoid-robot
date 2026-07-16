---
$id: rel_ent_paper_mishra_artitwinsplat_interactable_dig_2026_uses_ent_software_nvidia_isaac_sim_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_mishra_artitwinsplat_interactable_dig_2026
  name:
    en: 'ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos'
    zh: ArtiTwinSplat：基于RGB-D视频的高斯溅射可交互数字孪生重建
target:
  id: ent_software_nvidia_isaac_sim_2024
  name:
    en: NVIDIA Isaac Sim
    zh: NVIDIA Isaac Sim
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: 'ArtiTwinSplat: Interactable Digital Twin Reconstruction via Gaussian Splatting from RGB-D videos uses NVIDIA Isaac
    Sim.'
  zh: ArtiTwinSplat：基于RGB-D视频的高斯溅射可交互数字孪生重建使用NVIDIA Isaac Sim。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 重建的模型可导出为URDF并在NVIDIA Isaac Sim中使用。 | 证据: Reconstructed
    models can be exported directly as URDFs and used in NVIDIA Isaac Sim, providing a practical bridge from casual RGB-D
    capture to downstream robot planning and learning systems.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_mishra_artitwinsplat_interactable_dig_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_mishra_artitwinsplat_interactable_dig_2026/
  accessed_at: '2026-07-16'
---
