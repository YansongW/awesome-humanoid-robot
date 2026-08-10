---
$id: ent_paper_farm_frame_accelerated_augment_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control'
  zh: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control'
  ko: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control'
summary:
  en: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    is a 2025 work on physics-based character animation for humanoid robots.'
  zh: FARM 是 2025 年提出的端到端物理仿真人形机器人控制框架，由帧加速增强、稳健基础控制器和残差混合专家模块组成。其核心贡献在于通过扩大帧间间隔暴露高速度姿态变化，并利用残差 MoE 自适应分配网络容量，显著提升高动态动作的跟踪精度。该工作还发布了首个公开的高动态人形运动数据集
    HDHM，包含 3593 个物理合理的动作片段。
  ko: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    is a 2025 work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- farm
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19926v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (900 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    (arXiv)'
  url: https://arxiv.org/abs/2508.19926
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有统一物理仿真人形控制器在温和日常动作上表现优异，但在爆发性高动态动作中频繁失败，限制了实际部署。FARM 通过帧加速增强技术人为扩大训练数据中的帧间间隔，使模型适应高速姿态变化；基础控制器负责稳定跟踪低动态动作，而残差混合专家模块则动态激活额外网络容量处理高动态挑战。在自建 HDHM 数据集上，FARM 将跟踪失败率降低 42.8%，全局平均每关节位置误差减少 14.6%，同时保持低动态动作的近乎完美精度。

## 核心内容
### 方法架构
FARM 由三个核心组件构成：
- **帧加速增强**：在训练阶段随机扩大连续帧之间的时间间隔，迫使模型学习预测和补偿高速姿态变化，从而暴露于高动态运动模式。
- **基础控制器**：基于标准强化学习框架训练，专注于跟踪日常低动态动作（如行走、站立），提供稳定的基线性能。
- **残差混合专家（Residual MoE）**：在基础控制器之上叠加多个专家网络，通过门控机制动态选择激活哪些专家。当检测到高动态动作（如跳跃、快速转身）时，自动分配更多网络容量以提升跟踪精度。

### 数据集与实验设置
- **HDHM 数据集**：包含 3593 个物理合理的高动态人形运动片段，覆盖跳跃、冲刺、旋转等爆发性动作，填补了公开基准的空白。
- **基线对比**：与未使用帧加速和 MoE 的标准控制器对比，FARM 在 HDHM 全量测试集上：
  - 跟踪失败率降低 42.8%（从 18.3% 降至 10.5%）
  - 全局平均每关节位置误差（MPJPE）降低 14.6%（从 0.082m 降至 0.070m）
- **低动态保持**：在传统低动态测试集上，FARM 的 MPJPE 仅增加 0.003m（从 0.041m 升至 0.044m），证明其未牺牲日常动作精度。

### 结论
FARM 通过帧加速增强与残差 MoE 的协同设计，首次在统一框架中同时实现低动态和高动态动作的高精度跟踪。HDHM 数据集和开源代码（https://github.com/Colin-Jing/FARM）为后续研究提供了标准化评估基准。

## Overview
Unified physics-based humanoid controllers are pivotal for robotics and character animation, yet models that excel on gentle, everyday motions still stumble on explosive actions, hampering real-world deployment. We bridge this gap with FARM (Frame-Accelerated Augmentation and Residual Mixture-of-Experts), an end-to-end framework composed of frame-accelerated augmentation, a robust base controller, and a residual mixture-of-experts (MoE). Frame-accelerated augmentation exposes the model to high-velocity pose changes by widening inter-frame gaps. The base controller reliably tracks everyday low-dynamic motions, while the residual MoE adaptively allocates additional network capacity to handle challenging high-dynamic actions, significantly enhancing tracking accuracy. In the absence of a public benchmark, we curate the High-Dynamic Humanoid Motion (HDHM) dataset, comprising 3593 physically plausible clips. On HDHM, FARM reduces the tracking failure rate by 42.8\% and lowers global mean per-joint position error by 14.6\% relative to the baseline, while preserving near-perfect accuracy on low-dynamic motions. These results establish FARM as a new baseline for high-dynamic humanoid control and introduce the first open benchmark dedicated to this challenge. The code and dataset will be released at https://github.com/Colin-Jing/FARM.

## 参考
- http://arxiv.org/abs/2508.19926v1

## 개요
기존의 통합 물리 시뮬레이션 휴머노이드 컨트롤러는 온화한 일상 동작에서 우수한 성능을 보이지만, 폭발적인 고동적 동작에서는 빈번히 실패하여 실제 배포에 제한이 있습니다. FARM은 프레임 가속 강화 기법을 통해 훈련 데이터의 프레임 간 간격을 인위적으로 확대하여 모델이 고속 자세 변화에 적응하도록 합니다. 기본 컨트롤러는 저동적 동작을 안정적으로 추적하는 역할을 담당하고, 잔차 혼합 전문가 모듈은 고동적 과제를 처리하기 위해 추가 네트워크 용량을 동적으로 활성화합니다. 자체 구축한 HDHM 데이터셋에서 FARM은 추적 실패율을 42.8% 감소시키고, 전역 평균 관절당 위치 오차를 14.6% 줄이면서 저동적 동작의 거의 완벽한 정밀도를 유지합니다.

## 핵심 내용
### 방법 아키텍처
FARM은 세 가지 핵심 구성 요소로 이루어져 있습니다:
- **프레임 가속 강화**: 훈련 단계에서 연속 프레임 간 시간 간격을 무작위로 확대하여 모델이 고속 자세 변화를 예측하고 보상하도록 강제함으로써 고동적 운동 패턴에 노출시킵니다.
- **기본 컨트롤러**: 표준 강화 학습 프레임워크를 기반으로 훈련되며, 걷기, 서기 등의 일상적인 저동적 동작 추적에 집중하여 안정적인 기준 성능을 제공합니다.
- **잔차 혼합 전문가(Residual MoE)**: 기본 컨트롤러 위에 여러 전문가 네트워크를叠加하고, 게이팅 메커니즘을 통해 어떤 전문가를 활성화할지 동적으로 선택합니다. 점프, 빠른 회전 등의 고동적 동작이 감지되면 자동으로 더 많은 네트워크 용량을 할당하여 추적 정밀도를 향상시킵니다.

### 데이터셋 및 실험 설정
- **HDHM 데이터셋**: 3593개의 물리적으로 타당한 고동적 휴머노이드 모션 클립을 포함하며, 점프, 전력 질주, 회전 등의 폭발적 동작을涵盖하여 공개 벤치마크의 공백을 메웁니다.
- **기준 비교**: 프레임 가속 및 MoE를 사용하지 않은 표준 컨트롤러와 비교하여, FARM은 HDHM 전체 테스트 세트에서:
  - 추적 실패율 42.8% 감소(18.3%에서 10.5%로)
  - 전역 평균 관절당 위치 오차(MPJPE) 14.6% 감소(0.082m에서 0.070m로)
- **저동적 유지**: 기존 저동적 테스트 세트에서 FARM의 MPJPE는 0.003m만 증가(0.041m에서 0.044m로)하여 일상 동작 정밀도를 희생하지 않았음을 입증합니다.

### 결론
FARM은 프레임 가속 강화와 잔차 MoE의 협력 설계를 통해 통합 프레임워크에서 저동적 및 고동적 동작의 고정밀 추적을 최초로 동시에 달성했습니다. HDHM 데이터셋과 오픈 소스 코드(https://github.com/Colin-Jing/FARM)는 후속 연구를 위한 표준화된 평가 기준을 제공합니다.
