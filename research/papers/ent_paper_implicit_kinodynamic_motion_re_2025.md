---
$id: ent_paper_implicit_kinodynamic_motion_re_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
  zh: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
  ko: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning
summary:
  en: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
  zh: IKMR（Implicit Kinodynamic Motion Retargeting）是2025年提出的一种用于人形机器人模仿学习的隐式运动重定向方法。它通过骨架图卷积双自编码器将人体与机器人运动映射到共享拓扑潜空间，并利用物理感知精炼阶段保证生成数据的物理可行性。该方法实现了超过5000帧/秒的数据转换吞吐量，并能自动过滤源数据中的噪声与抖动。
  ko: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.
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
- implicit_kinodynamic_motion_re
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15443v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (712 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Implicit Kinodynamic Motion Retargeting for Human-to-humanoid Imitation Learning (arXiv)
  url: https://arxiv.org/abs/2509.15443
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人模仿学习面临两大挑战：人体运动数据（来自视频、动作捕捉或生成模型）常包含空间噪声、抖动和帧级闪烁，这些在重定向过程中会被放大；现有逐帧数值优化方法计算成本过高，难以用于大规模数据集合成。IKMR通过隐式运动重定向框架解决了这些问题，其核心是骨架图卷积双自编码器，用于将人体与机器人运动映射到共享拓扑潜空间。框架还包含物理感知精炼阶段，利用模拟物理跟踪反馈学习鲁棒运动先验，从而保证生成数据的物理可行性。IKMR将计算负担从在线优化转移到离线推理，实现了超过5000帧/秒的数据转换吞吐量，同时作为内在数据筛选机制，自动过滤源数据中的高频噪声和空间抖动，生成平滑轨迹以确保硬件安全。

## 核心内容
### 方法架构
IKMR由两个核心组件构成：
- **骨架图卷积双自编码器**：将人体与机器人运动映射到共享拓扑潜空间，实现跨结构运动配置的隐式对齐。
- **物理感知精炼阶段**：利用模拟物理跟踪反馈学习鲁棒运动先验，保证生成数据的物理可行性。

### 实验设置
- **数据来源**：使用来自视频、动作捕捉系统和生成模型的人体运动数据。
- **评估方式**：在真实人形机器人上进行全身控制部署，验证IKMR的实际效果。

### 关键数字与结论
- **数据转换吞吐量**：超过5000帧/秒，远超传统逐帧优化方法。
- **噪声过滤能力**：自动过滤源数据中的高频噪声和空间抖动，生成平滑轨迹。
- **物理可行性**：通过物理感知精炼阶段，确保生成的运动在物理上安全且可行。
- **实际部署**：在真实人形机器人上成功实现全身控制，验证了IKMR在桥接人体运动与机器人数据方面的有效性。

## Overview
Human-to-humanoid imitation learning presents a promising pathway to address the severe data scarcity bottleneck in robotics by utilizing abundant, large-scale human motion collections. However, scaling this paradigm requires addressing two key challenges. First, human motion data acquired from videos, motion capture systems, or generative models often contains spatial noise, jitter, and frame-level flickering, which can be amplified during retargeting and lead to unsafe or physically infeasible robot motions. Second, existing motion retargeting methods typically rely on frame-by-frame numerical optimization, making them too computationally expensive for large-scale dataset synthesis. To overcome these limitations, we introduce Implicit Kinodynamic Motion Retargeting (IKMR), a highly scalable, neural-based data transformation pipeline. IKMR leverages a skeleton-based graph convolutional dual autoencoder to map cross-structural human and humanoid kinematic configurations into a shared topological latent space. To guarantee the physical viability of the generated data, the framework incorporates a physics-informed refinement phase that utilizes simulated physical tracking feedback to learn a robust motion prior. This implicit formulation fundamentally resolves both challenges. By shifting the computational burden from online optimization to offline inference, IKMR achieves an unprecedented data conversion throughput exceeding 5000 frames per second. Furthermore, leveraging the learned motion prior, it functions as an intrinsic data curation mechanism and naturally filters out high-frequency noise and spatial jitters from source data, yielding smooth trajectories that ensure physical hardware safety. Extensive evaluations, including real-world whole-body control deployments on humanoid robot, confirm that IKMR bridges the gap between human motion and robotic data.

## 参考
- http://arxiv.org/abs/2509.15443v2

## 개요
휴머노이드 로봇 모방 학습은 두 가지 주요 과제에 직면합니다: 인체 모션 데이터(비디오, 모션 캡처 또는 생성 모델에서 얻은)는 종종 공간 노이즈, 떨림 및 프레임 수준의 깜빡임을 포함하며, 이는 리타겟팅 과정에서 증폭됩니다; 기존의 프레임별 수치 최적화 방법은 계산 비용이 너무 높아 대규모 데이터셋 합성에 사용하기 어렵습니다. IKMR은 암시적 모션 리타겟팅 프레임워크를 통해 이러한 문제를 해결하며, 핵심은 골격 그래프 컨볼루션 이중 오토인코더로, 인간과 로봇 모션을 공유 토폴로지 잠재 공간에 매핑합니다. 프레임워크는 또한 물리 인지 정제 단계를 포함하며, 시뮬레이션 물리 추적 피드백을 활용하여 강건한 모션 사전을 학습함으로써 생성 데이터의 물리적 타당성을 보장합니다. IKMR은 계산 부담을 온라인 최적화에서 오프라인 추론으로 전환하여 초당 5000프레임 이상의 데이터 변환 처리량을 달성하고, 동시에 내재적 데이터 필터링 메커니즘으로 작동하여 소스 데이터의 고주파 노이즈와 공간 떨림을 자동으로 필터링하고, 하드웨어 안전을 보장하는 부드러운 궤적을 생성합니다.

## 핵심 내용
### 방법 아키텍처
IKMR은 두 가지 핵심 구성 요소로 이루어져 있습니다:
- **골격 그래프 컨볼루션 이중 오토인코더**: 인간과 로봇 모션을 공유 토폴로지 잠재 공간에 매핑하여 구조 간 모션 구성을 암시적으로 정렬합니다.
- **물리 인지 정제 단계**: 시뮬레이션 물리 추적 피드백을 활용하여 강건한 모션 사전을 학습하고, 생성 데이터의 물리적 타당성을 보장합니다.

### 실험 설정
- **데이터 소스**: 비디오, 모션 캡처 시스템 및 생성 모델에서 얻은 인체 모션 데이터를 사용합니다.
- **평가 방식**: 실제 휴머노이드 로봇에서 전신 제어 배포를 수행하여 IKMR의 실제 효과를 검증합니다.

### 주요 수치 및 결론
- **데이터 변환 처리량**: 초당 5000프레임 이상으로, 기존 프레임별 최적화 방법을 크게 능가합니다.
- **노이즈 필터링 능력**: 소스 데이터의 고주파 노이즈와 공간 떨림을 자동으로 필터링하고 부드러운 궤적을 생성합니다.
- **물리적 타당성**: 물리 인지 정제 단계를 통해 생성된 모션이 물리적으로 안전하고 실행 가능함을 보장합니다.
- **실제 배포**: 실제 휴머노이드 로봇에서 전신 제어를 성공적으로 구현하여, IKMR이 인간 모션과 로봇 데이터를 연결하는 데 있어 효과적임을 검증합니다.
