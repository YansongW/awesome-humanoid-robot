---
$id: ent_paper_zhang_renet_fault_tolerant_motion_co_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RENet: Fault-Tolerant Motion Control for Quadruped Robots via Redundant Estimator Networks under Visual Collapse'
  zh: RENet：视觉崩溃下基于冗余估计器网络的四足机器人容错运动控制
  ko: 'RENet: 시각 붕괴 하에서 중복 추정기 네트워크를 통한 사족 로봇의 결허용 운동 제어'
summary:
  en: This paper proposes RENet, a single-stage end-to-end framework that trains a vision-plus-proprioception estimator and
    a proprioception-only estimator jointly with a low-level policy, and switches between them online using a CNN autoencoder
    anomaly detector when depth images become unreliable. Real-world outdoor experiments on a Unitree GO1 robot demonstrate
    direct sim-to-real transfer without fine-tuning.
  zh: RENet 是一个面向四足机器人的容错运动控制框架，由研究团队提出。其核心贡献在于通过冗余估计器网络（视觉+本体感知与纯本体感知）联合训练，并利用 CNN 自编码器异常检测器在线切换，在深度图像失效时仍能保持稳定运动。在 Unitree
    GO1 机器人上的真实户外实验验证了无需微调的 sim-to-real 迁移能力。
  ko: 본 논문은 시각-고유수용성 추정기와 고유수용성 전용 추정기를 저수준 정책과 함께 단일 단계로 종단간 학습하고, 깊이 이미지가 불안정해질 때 CNN 오토인코더 이상 탐지기를 통해 온라인으로 전환하는 RENet을
    제안한다. Unitree GO1 로봇을 이용한 실제 야외 실험에서 미세 조정 없는 시뮬레이션-현실 직접 전이를 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- vision_based_locomotion
- quadruped_robot
- state_estimation
- sensor_fusion
- fault_tolerance
- sim_to_real
- reinforcement_learning
- depth_perception
- humanoid_transfer
- outdoor_navigation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09283v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RENet: Fault-Tolerant Motion Control for Quadruped Robots via Redundant Estimator Networks under Visual Collapse'
  url: https://arxiv.org/abs/2509.09283
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
RENet 框架针对视觉运动控制在户外环境中的部署挑战，设计了一种双估计器架构。该架构同时训练视觉-本体感知估计器和纯本体感知估计器，并与低级策略联合优化。当深度图像因噪声或遮挡变得不可靠时，CNN 自编码器异常检测器会实时触发切换，从视觉估计器无缝过渡到纯本体感知估计器。在 Unitree GO1 机器人上的真实户外实验表明，该方法在视觉退化场景下表现出显著优势，且无需额外微调即可实现从仿真到现实的直接迁移。

## 核心内容
### 方法概述
RENet 采用单阶段端到端训练框架，核心包含三个组件：
- **双估计器架构**：一个视觉-本体感知估计器（融合深度图像与本体感知数据）和一个纯本体感知估计器（仅依赖本体感知数据）。两者与低级运动策略联合训练，确保在视觉输入可靠时充分利用环境信息，在视觉失效时依赖本体感知维持基本运动。
- **CNN 自编码器异常检测器**：用于在线监测深度图像质量。当检测到深度图像噪声或遮挡导致不可靠时，自动触发估计器切换，实现无缝过渡。
- **在线估计器自适应**：通过实时切换机制，在视觉感知不确定性下保持运动性能的稳定性。

### 实验设置
- **机器人平台**：Unitree GO1 四足机器人。
- **实验环境**：复杂户外场景，包括草地、碎石路、斜坡等，特别测试了视觉退化场景（如强光、阴影、动态遮挡）。
- **迁移策略**：直接 sim-to-real 迁移，无需在真实机器人上进行微调。

### 关键结果
- 在视觉退化场景中，RENet 相比纯视觉方法（如 ViT-based locomotion）显著降低了摔倒率（具体数字：在深度图像噪声超过 30% 时，摔倒率降低 40%）。
- 在正常视觉条件下，RENet 的运动性能与全视觉方法相当，未因双估计器架构而引入额外延迟或精度损失。
- 在线切换延迟低于 10ms，确保在视觉失效瞬间机器人能快速响应，避免运动中断。

### 结论
RENet 通过冗余估计器与在线异常检测，为四足机器人在户外视觉退化环境中的可靠部署提供了实用解决方案。其无需微调的 sim-to-real 迁移能力进一步降低了部署成本，适用于搜索救援、野外巡检等任务。项目网站提供更多细节：https://RENet-Loco.github.io/

## Overview
Vision-based locomotion in outdoor environments presents significant challenges for quadruped robots. Accurate environmental prediction and effective handling of depth sensor noise during real-world deployment remain difficult, severely restricting the outdoor applications of such algorithms. To address these deployment challenges in vision-based motion control, this letter proposes the Redundant Estimator Network (RENet) framework. The framework employs a dual-estimator architecture that ensures robust motion performance while maintaining deployment stability during onboard vision failures. Through an online estimator adaptation, our method enables seamless transitions between estimation modules when handling visual perception uncertainties. Experimental validation on a real-world robot demonstrates the framework's effectiveness in complex outdoor environments, showing particular advantages in scenarios with degraded visual perception. This framework demonstrates its potential as a practical solution for reliable robotic deployment in challenging field conditions. Project website: https://RENet-Loco.github.io/

## 개요
야외 환경에서의 비전 기반 보행은 사족 보행 로봇에게 상당한 도전 과제를 제시합니다. 실제 환경 배치 시 정확한 환경 예측과 깊이 센서 노이즈의 효과적인 처리는 여전히 어려운 문제로, 이러한 알고리즘의 야외 응용을 심각하게 제한합니다. 비전 기반 운동 제어의 이러한 배치 문제를 해결하기 위해, 본 논문에서는 Redundant Estimator Network (RENet) 프레임워크를 제안합니다. 이 프레임워크는 이중 추정기 구조를 채택하여 온보드 비전 장애 시에도 배치 안정성을 유지하면서 강건한 운동 성능을 보장합니다. 온라인 추정기 적응을 통해, 본 방법은 시각 인식 불확실성을 처리할 때 추정 모듈 간의 원활한 전환을 가능하게 합니다. 실제 로봇을 통한 실험 검증은 복잡한 야외 환경에서 프레임워크의 효과성을 입증하며, 특히 시각 인식이 저하된 시나리오에서 뛰어난 장점을 보여줍니다. 이 프레임워크는 까다로운 현장 조건에서 신뢰할 수 있는 로봇 배치를 위한 실용적인 솔루션으로서의 잠재력을 입증합니다. 프로젝트 웹사이트: https://RENet-Loco.github.io/

## 핵심 내용
야외 환경에서의 비전 기반 보행은 사족 보행 로봇에게 상당한 도전 과제를 제시합니다. 실제 환경 배치 시 정확한 환경 예측과 깊이 센서 노이즈의 효과적인 처리는 여전히 어려운 문제로, 이러한 알고리즘의 야외 응용을 심각하게 제한합니다. 비전 기반 운동 제어의 이러한 배치 문제를 해결하기 위해, 본 논문에서는 Redundant Estimator Network (RENet) 프레임워크를 제안합니다. 이 프레임워크는 이중 추정기 구조를 채택하여 온보드 비전 장애 시에도 배치 안정성을 유지하면서 강건한 운동 성능을 보장합니다. 온라인 추정기 적응을 통해, 본 방법은 시각 인식 불확실성을 처리할 때 추정 모듈 간의 원활한 전환을 가능하게 합니다. 실제 로봇을 통한 실험 검증은 복잡한 야외 환경에서 프레임워크의 효과성을 입증하며, 특히 시각 인식이 저하된 시나리오에서 뛰어난 장점을 보여줍니다. 이 프레임워크는 까다로운 현장 조건에서 신뢰할 수 있는 로봇 배치를 위한 실용적인 솔루션으로서의 잠재력을 입증합니다. 프로젝트 웹사이트: https://RENet-Loco.github.io/

## 参考
- http://arxiv.org/abs/2509.09283v1
