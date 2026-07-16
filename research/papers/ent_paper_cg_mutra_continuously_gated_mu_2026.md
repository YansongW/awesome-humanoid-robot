---
$id: ent_paper_cg_mutra_continuously_gated_mu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid Fall Recovery and Locomotion'
  zh: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid Fall Recovery and Locomotion'
  ko: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid Fall Recovery and Locomotion'
summary:
  en: 'arXiv:2606.08922v2 Announce Type: replace Abstract: Falling is an inherent risk for humanoid robots operating in unstructured
    environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on
    flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers.
    As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains
    such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator
    framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $\alpha
    = f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level
    stability ($\Phi_{\mathrm{frame}}$, $H=1$), temporal smoothness ($\Phi_{\mathrm{seq}}$, $H=5$), and gait periodicity ($\Phi_{\mathrm{gait}}$,
    $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore,
    we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain
    dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $\Xi_\kappa$. We validate
    CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware.
    Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions
    across multiple terrains while maintaining a single deployable policy.'
  zh: 'arXiv:2606.08922v2 Announce Type: replace Abstract: Falling is an inherent risk for humanoid robots operating in unstructured
    environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on
    flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers.
    As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains
    such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator
    framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $\alpha
    = f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level
    stability ($\Phi_{\mathrm{frame}}$, $H=1$), temporal smoothness ($\Phi_{\mathrm{seq}}$, $H=5$), and gait periodicity ($\Phi_{\mathrm{gait}}$,
    $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore,
    we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain
    dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $\Xi_\kappa$. We validate
    CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware.
    Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions
    across multiple terrains while maintaining a single deployable policy.'
  ko: 'arXiv:2606.08922v2 Announce Type: replace Abstract: Falling is an inherent risk for humanoid robots operating in unstructured
    environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on
    flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers.
    As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains
    such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator
    framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $\alpha
    = f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level
    stability ($\Phi_{\mathrm{frame}}$, $H=1$), temporal smoothness ($\Phi_{\mathrm{seq}}$, $H=5$), and gait periodicity ($\Phi_{\mathrm{gait}}$,
    $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore,
    we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain
    dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $\Xi_\kappa$. We validate
    CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware.
    Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions
    across multiple terrains while maintaining a single deployable policy.'
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.08922v2.
sources:
- id: src_001
  type: paper
  title: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid Fall Recovery and Locomotion (arXiv)'
  url: https://arxiv.org/abs/2606.08922
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $α= f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($Φ_{\mathrm{frame}}$, $H=1$), temporal smoothness ($Φ_{\mathrm{seq}}$, $H=5$), and gait periodicity ($Φ_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $Ξ_κ$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## 核心内容
Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $α= f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($Φ_{\mathrm{frame}}$, $H=1$), temporal smoothness ($Φ_{\mathrm{seq}}$, $H=5$), and gait periodicity ($Φ_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $Ξ_κ$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## 参考
- http://arxiv.org/abs/2606.08922v2

## Overview
Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $α= f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($Φ_{\mathrm{frame}}$, $H=1$), temporal smoothness ($Φ_{\mathrm{seq}}$, $H=5$), and gait periodicity ($Φ_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $Ξ_κ$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## Content
Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $α= f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($Φ_{\mathrm{frame}}$, $H=1$), temporal smoothness ($Φ_{\mathrm{seq}}$, $H=5$), and gait periodicity ($Φ_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $Ξ_κ$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## 개요
넘어짐은 비정형 환경에서 작동하는 휴머노이드 로봇에게 내재된 위험입니다. 전문가 동작 사전을 활용하는 기존 강화 학습 방법은 주로 평지에서의 낙상 회복 작업에 대해 훈련되며, 일반적으로 별도의 회복 및 보행 컨트롤러 간의 하드 스위칭에 의존합니다. 결과적으로 이러한 정책은 경사면이나 자갈과 같은 복잡한 지형에 배치될 때 부드럽고 강건한 회복 동작을 달성하는 데 어려움을 겪습니다. 본 논문은 다중 지형 적응형 낙상 회복을 위한 통합 연속 게이트 다중 스케일 판별기 프레임워크인 \textbf{CG-MuTra}를 제시합니다. CG-MuTra는 고유 감각에서 파생된 연속 게이트 $α= f(z_{\mathrm{root}}, s)$를 도입하여 서로 다른 시간적 범위에서 작동하는 세 가지 판별기(프레임 수준 안정성 $Φ_{\mathrm{frame}}$, $H=1$), 시간적 매끄러움($Φ_{\mathrm{seq}}$, $H=5$), 보행 주기성($Φ_{\mathrm{gait}}$, $H=10$))를 부드럽게 혼합합니다. 이 설계는 명시적인 모드 전환 없이 원활한 회복-보행 전환을 가능하게 합니다. 또한, 훈련 중 위험한 가장자리 초기 자세를 지형 역학과 명시적으로 결합하는 지형-자세 위험 결합 샘플러(TPRCS)를 제안하여 지형 특권 형상 항 $Ξ_κ$와 폐쇄 루프 시너지를 형성합니다. 우리는 시뮬레이션과 하드웨어 모두에서 잔디, 경사면($10^\circ$--$15^\circ$), 자갈 지형에 걸쳐 Unitree G1 휴머노이드에서 CG-MuTra를 검증합니다. 실험 결과는 CG-MuTra가 단일 배포 가능 정책을 유지하면서 여러 지형에서 부드럽고 매우 강건한 낙상 회복 및 보행 전환을 달성함을 보여줍니다.

## 핵심 내용
넘어짐은 비정형 환경에서 작동하는 휴머노이드 로봇에게 내재된 위험입니다. 전문가 동작 사전을 활용하는 기존 강화 학습 방법은 주로 평지에서의 낙상 회복 작업에 대해 훈련되며, 일반적으로 별도의 회복 및 보행 컨트롤러 간의 하드 스위칭에 의존합니다. 결과적으로 이러한 정책은 경사면이나 자갈과 같은 복잡한 지형에 배치될 때 부드럽고 강건한 회복 동작을 달성하는 데 어려움을 겪습니다. 본 논문은 다중 지형 적응형 낙상 회복을 위한 통합 연속 게이트 다중 스케일 판별기 프레임워크인 \textbf{CG-MuTra}를 제시합니다. CG-MuTra는 고유 감각에서 파생된 연속 게이트 $α= f(z_{\mathrm{root}}, s)$를 도입하여 서로 다른 시간적 범위에서 작동하는 세 가지 판별기(프레임 수준 안정성 $Φ_{\mathrm{frame}}$, $H=1$), 시간적 매끄러움($Φ_{\mathrm{seq}}$, $H=5$), 보행 주기성($Φ_{\mathrm{gait}}$, $H=10$))를 부드럽게 혼합합니다. 이 설계는 명시적인 모드 전환 없이 원활한 회복-보행 전환을 가능하게 합니다. 또한, 훈련 중 위험한 가장자리 초기 자세를 지형 역학과 명시적으로 결합하는 지형-자세 위험 결합 샘플러(TPRCS)를 제안하여 지형 특권 형상 항 $Ξ_κ$와 폐쇄 루프 시너지를 형성합니다. 우리는 시뮬레이션과 하드웨어 모두에서 잔디, 경사면($10^\circ$--$15^\circ$), 자갈 지형에 걸쳐 Unitree G1 휴머노이드에서 CG-MuTra를 검증합니다. 실험 결과는 CG-MuTra가 단일 배포 가능 정책을 유지하면서 여러 지형에서 부드럽고 매우 강건한 낙상 회복 및 보행 전환을 달성함을 보여줍니다.
