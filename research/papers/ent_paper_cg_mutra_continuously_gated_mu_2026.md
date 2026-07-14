---
$id: ent_paper_cg_mutra_continuously_gated_mu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid
    Fall Recovery and Locomotion'
  zh: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid
    Fall Recovery and Locomotion'
  ko: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid
    Fall Recovery and Locomotion'
summary:
  en: "arXiv:2606.08922v2 Announce Type: replace \nAbstract: Falling is an inherent\
    \ risk for humanoid robots operating in unstructured environments. Existing reinforcement\
    \ learning methods that leverage expert motion priors are predominantly trained\
    \ on flat-ground fall-recovery tasks and typically rely on hard switching between\
    \ separate recovery and locomotion controllers. As a result, such policies struggle\
    \ to achieve smooth and robust recovery behaviors when deployed on complex terrains\
    \ such as slopes and gravel. This paper presents \\textbf{CG-MuTra}, a unified\
    \ continuously-gated multi-scale discriminator framework for multi-terrain adaptive\
    \ fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate\
    \ $\\alpha = f(z_{\\mathrm{root}}, s)$ that softly blends three discriminators\
    \ operating at different temporal horizons: frame-level stability ($\\Phi_{\\\
    mathrm{frame}}$, $H=1$), temporal smoothness ($\\Phi_{\\mathrm{seq}}$, $H=5$),\
    \ and gait periodicity ($\\Phi_{\\mathrm{gait}}$, $H=10$). This design enables\
    \ seamless recovery-to-locomotion transitions without explicit mode switching.\
    \ Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly\
    \ couples dangerous edge initial poses with terrain dynamics during training,\
    \ forming a closed-loop synergy with the terrain-privileged shaping term $\\Xi_\\\
    kappa$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\\\
    circ$--$15^\\circ$), and gravel in both simulation and hardware. Experimental\
    \ results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery\
    \ and locomotion transitions across multiple terrains while maintaining a single\
    \ deployable policy."
  zh: "arXiv:2606.08922v2 Announce Type: replace \nAbstract: Falling is an inherent\
    \ risk for humanoid robots operating in unstructured environments. Existing reinforcement\
    \ learning methods that leverage expert motion priors are predominantly trained\
    \ on flat-ground fall-recovery tasks and typically rely on hard switching between\
    \ separate recovery and locomotion controllers. As a result, such policies struggle\
    \ to achieve smooth and robust recovery behaviors when deployed on complex terrains\
    \ such as slopes and gravel. This paper presents \\textbf{CG-MuTra}, a unified\
    \ continuously-gated multi-scale discriminator framework for multi-terrain adaptive\
    \ fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate\
    \ $\\alpha = f(z_{\\mathrm{root}}, s)$ that softly blends three discriminators\
    \ operating at different temporal horizons: frame-level stability ($\\Phi_{\\\
    mathrm{frame}}$, $H=1$), temporal smoothness ($\\Phi_{\\mathrm{seq}}$, $H=5$),\
    \ and gait periodicity ($\\Phi_{\\mathrm{gait}}$, $H=10$). This design enables\
    \ seamless recovery-to-locomotion transitions without explicit mode switching.\
    \ Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly\
    \ couples dangerous edge initial poses with terrain dynamics during training,\
    \ forming a closed-loop synergy with the terrain-privileged shaping term $\\Xi_\\\
    kappa$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\\\
    circ$--$15^\\circ$), and gravel in both simulation and hardware. Experimental\
    \ results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery\
    \ and locomotion transitions across multiple terrains while maintaining a single\
    \ deployable policy."
  ko: "arXiv:2606.08922v2 Announce Type: replace \nAbstract: Falling is an inherent\
    \ risk for humanoid robots operating in unstructured environments. Existing reinforcement\
    \ learning methods that leverage expert motion priors are predominantly trained\
    \ on flat-ground fall-recovery tasks and typically rely on hard switching between\
    \ separate recovery and locomotion controllers. As a result, such policies struggle\
    \ to achieve smooth and robust recovery behaviors when deployed on complex terrains\
    \ such as slopes and gravel. This paper presents \\textbf{CG-MuTra}, a unified\
    \ continuously-gated multi-scale discriminator framework for multi-terrain adaptive\
    \ fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate\
    \ $\\alpha = f(z_{\\mathrm{root}}, s)$ that softly blends three discriminators\
    \ operating at different temporal horizons: frame-level stability ($\\Phi_{\\\
    mathrm{frame}}$, $H=1$), temporal smoothness ($\\Phi_{\\mathrm{seq}}$, $H=5$),\
    \ and gait periodicity ($\\Phi_{\\mathrm{gait}}$, $H=10$). This design enables\
    \ seamless recovery-to-locomotion transitions without explicit mode switching.\
    \ Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly\
    \ couples dangerous edge initial poses with terrain dynamics during training,\
    \ forming a closed-loop synergy with the terrain-privileged shaping term $\\Xi_\\\
    kappa$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\\\
    circ$--$15^\\circ$), and gravel in both simulation and hardware. Experimental\
    \ results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery\
    \ and locomotion transitions across multiple terrains while maintaining a single\
    \ deployable policy."
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
- cg_mutra
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
  title: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified
    Humanoid Fall Recovery and Locomotion (arXiv)'
  url: https://arxiv.org/abs/2606.08922
  date: '2026'
  accessed_at: '2026-07-08'
---

## 概述
arXiv:2606.08922v2 Announce Type: replace 
Abstract: Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $\alpha = f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($\Phi_{\mathrm{frame}}$, $H=1$), temporal smoothness ($\Phi_{\mathrm{seq}}$, $H=5$), and gait periodicity ($\Phi_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $\Xi_\kappa$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## Overview
arXiv:2606.08922v2 Announce Type: replace 
Abstract: Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $\alpha = f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($\Phi_{\mathrm{frame}}$, $H=1$), temporal smoothness ($\Phi_{\mathrm{seq}}$, $H=5$), and gait periodicity ($\Phi_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $\Xi_\kappa$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## 개요
arXiv:2606.08922v2 Announce Type: replace 
Abstract: Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $\alpha = f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($\Phi_{\mathrm{frame}}$, $H=1$), temporal smoothness ($\Phi_{\mathrm{seq}}$, $H=5$), and gait periodicity ($\Phi_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $\Xi_\kappa$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.
