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
  zh: CG-MuTra 是一个由研究者提出的统一连续门控多尺度判别器框架，用于人形机器人在多地形下的自适应跌倒恢复。其核心贡献在于通过本体感知的连续门控机制，软性融合三个不同时间尺度的判别器，实现从恢复到行走的无缝过渡，并提出了地形-姿态风险耦合采样器（TPRCS）来增强训练鲁棒性。在
    Unitree G1 人形机器人上的仿真和硬件实验验证了其在草地、斜坡和砾石地形上的有效性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.08922v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'CG-MuTra: Continuously-Gated Multi-Terrain Adaptive Recovery for Unified Humanoid Fall Recovery and Locomotion (arXiv)'
  url: https://arxiv.org/abs/2606.08922
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
针对现有强化学习方法在复杂地形（如斜坡、砾石）上因依赖硬切换控制器而导致的恢复行为不流畅问题，CG-MuTra 提出了一种统一框架。该框架利用一个由本体感知导出的连续门控值 α，动态混合帧级稳定性、时序平滑性和步态周期性三个判别器，从而避免了显式的模式切换。同时，TPRCS 采样器在训练中显式地将危险初始姿态与地形动态耦合，与地形特权塑造项形成闭环协同。实验表明，CG-MuTra 在多种地形上均能实现平滑且鲁棒的跌倒恢复与行走过渡，且仅需单个可部署策略。

## 核心内容
### 方法架构
CG-MuTra 的核心是一个**连续门控多尺度判别器**框架，其关键设计包括：
- **连续门控机制**：通过一个本体感知的连续门控值 \( \alpha = f(z_{\mathrm{root}}, s) \) 实现，其中 \( z_{\mathrm{root}} \) 是根节点状态，\( s \) 是其他传感器信息。该门控值软性混合三个不同时间尺度的判别器：
  - **帧级稳定性判别器** (\( \Phi_{\mathrm{frame}} \), 时间窗口 \( H=1 \))：关注单步动作的即时稳定性。
  - **时序平滑性判别器** (\( \Phi_{\mathrm{seq}} \), \( H=5 \))：确保动作序列的连贯性。
  - **步态周期性判别器** (\( \Phi_{\mathrm{gait}} \), \( H=10 \))：维持行走的节律模式。
- **无缝过渡**：这种软混合设计使得策略能够在不依赖显式模式切换的情况下，从跌倒恢复状态平滑过渡到行走状态。

### 训练策略
- **Terrain-Pose Risk Coupling Sampler (TPRCS)**：在训练过程中，该采样器显式地将危险的边缘初始姿态（如即将跌倒的姿势）与地形动态（如斜坡角度、砾石摩擦力）耦合起来。这迫使策略学习应对最坏情况。
- **地形特权塑造项** (\( \Xi_\kappa \))：与 TPRCS 形成闭环协同，利用地形特权信息（如地形类型、坡度）来进一步引导策略学习，提升鲁棒性。

### 实验设置与结果
- **平台**：Unitree G1 人形机器人。
- **地形**：草地、斜坡（坡度 \( 10^\circ \) 至 \( 15^\circ \)）和砾石。
- **验证方式**：同时进行了仿真和硬件实验。
- **关键结论**：CG-MuTra 在所有这些复杂地形上均实现了平滑且高度鲁棒的跌倒恢复与行走过渡。与依赖硬切换的基线方法相比，其恢复行为更流畅，且无需为不同地形或恢复/行走模式准备多个策略，仅需**单个可部署策略**即可应对多种场景。

## Overview
Falling is an inherent risk for humanoid robots operating in unstructured environments. Existing reinforcement learning methods that leverage expert motion priors are predominantly trained on flat-ground fall-recovery tasks and typically rely on hard switching between separate recovery and locomotion controllers. As a result, such policies struggle to achieve smooth and robust recovery behaviors when deployed on complex terrains such as slopes and gravel. This paper presents \textbf{CG-MuTra}, a unified continuously-gated multi-scale discriminator framework for multi-terrain adaptive fall recovery. CG-MuTra introduces a proprioceptively-derived continuous gate $α= f(z_{\mathrm{root}}, s)$ that softly blends three discriminators operating at different temporal horizons: frame-level stability ($Φ_{\mathrm{frame}}$, $H=1$), temporal smoothness ($Φ_{\mathrm{seq}}$, $H=5$), and gait periodicity ($Φ_{\mathrm{gait}}$, $H=10$). This design enables seamless recovery-to-locomotion transitions without explicit mode switching. Furthermore, we propose a Terrain-Pose Risk Coupling Sampler (TPRCS) that explicitly couples dangerous edge initial poses with terrain dynamics during training, forming a closed-loop synergy with the terrain-privileged shaping term $Ξ_κ$. We validate CG-MuTra on a Unitree G1 humanoid across grass, slopes ($10^\circ$--$15^\circ$), and gravel in both simulation and hardware. Experimental results demonstrate that CG-MuTra achieves smooth, highly robust fall recovery and locomotion transitions across multiple terrains while maintaining a single deployable policy.

## 개요
넘어짐은 비정형 환경에서 작동하는 휴머노이드 로봇에게 내재된 위험입니다. 전문가 동작 사전을 활용하는 기존 강화 학습 방법은 주로 평지에서의 낙상 회복 작업에 대해 훈련되며, 일반적으로 별도의 회복 및 보행 컨트롤러 간의 하드 스위칭에 의존합니다. 결과적으로 이러한 정책은 경사면이나 자갈과 같은 복잡한 지형에 배치될 때 부드럽고 강건한 회복 동작을 달성하는 데 어려움을 겪습니다. 본 논문은 다중 지형 적응형 낙상 회복을 위한 통합 연속 게이트 다중 스케일 판별기 프레임워크인 \textbf{CG-MuTra}를 제시합니다. CG-MuTra는 고유 감각에서 파생된 연속 게이트 $α= f(z_{\mathrm{root}}, s)$를 도입하여 서로 다른 시간적 범위에서 작동하는 세 가지 판별기(프레임 수준 안정성 $Φ_{\mathrm{frame}}$, $H=1$), 시간적 매끄러움($Φ_{\mathrm{seq}}$, $H=5$), 보행 주기성($Φ_{\mathrm{gait}}$, $H=10$))를 부드럽게 혼합합니다. 이 설계는 명시적인 모드 전환 없이 원활한 회복-보행 전환을 가능하게 합니다. 또한, 훈련 중 위험한 가장자리 초기 자세를 지형 역학과 명시적으로 결합하는 지형-자세 위험 결합 샘플러(TPRCS)를 제안하여 지형 특권 형상 항 $Ξ_κ$와 폐쇄 루프 시너지를 형성합니다. 우리는 시뮬레이션과 하드웨어 모두에서 잔디, 경사면($10^\circ$--$15^\circ$), 자갈 지형에 걸쳐 Unitree G1 휴머노이드에서 CG-MuTra를 검증합니다. 실험 결과는 CG-MuTra가 단일 배포 가능 정책을 유지하면서 여러 지형에서 부드럽고 매우 강건한 낙상 회복 및 보행 전환을 달성함을 보여줍니다.

## 핵심 내용
넘어짐은 비정형 환경에서 작동하는 휴머노이드 로봇에게 내재된 위험입니다. 전문가 동작 사전을 활용하는 기존 강화 학습 방법은 주로 평지에서의 낙상 회복 작업에 대해 훈련되며, 일반적으로 별도의 회복 및 보행 컨트롤러 간의 하드 스위칭에 의존합니다. 결과적으로 이러한 정책은 경사면이나 자갈과 같은 복잡한 지형에 배치될 때 부드럽고 강건한 회복 동작을 달성하는 데 어려움을 겪습니다. 본 논문은 다중 지형 적응형 낙상 회복을 위한 통합 연속 게이트 다중 스케일 판별기 프레임워크인 \textbf{CG-MuTra}를 제시합니다. CG-MuTra는 고유 감각에서 파생된 연속 게이트 $α= f(z_{\mathrm{root}}, s)$를 도입하여 서로 다른 시간적 범위에서 작동하는 세 가지 판별기(프레임 수준 안정성 $Φ_{\mathrm{frame}}$, $H=1$), 시간적 매끄러움($Φ_{\mathrm{seq}}$, $H=5$), 보행 주기성($Φ_{\mathrm{gait}}$, $H=10$))를 부드럽게 혼합합니다. 이 설계는 명시적인 모드 전환 없이 원활한 회복-보행 전환을 가능하게 합니다. 또한, 훈련 중 위험한 가장자리 초기 자세를 지형 역학과 명시적으로 결합하는 지형-자세 위험 결합 샘플러(TPRCS)를 제안하여 지형 특권 형상 항 $Ξ_κ$와 폐쇄 루프 시너지를 형성합니다. 우리는 시뮬레이션과 하드웨어 모두에서 잔디, 경사면($10^\circ$--$15^\circ$), 자갈 지형에 걸쳐 Unitree G1 휴머노이드에서 CG-MuTra를 검증합니다. 실험 결과는 CG-MuTra가 단일 배포 가능 정책을 유지하면서 여러 지형에서 부드럽고 매우 강건한 낙상 회복 및 보행 전환을 달성함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2606.08922v2
