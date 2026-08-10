---
$id: ent_paper_hiking_in_the_wild_a_scalable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids'
  zh: 脚落在哪里，比走得多快更重要
  ko: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids'
summary:
  en: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids is a knowledge node related to paper in the
    humanoid robot value chain.'
  zh: 《Hiking in the Wild》提出了一种可扩展的端到端感知跑酷框架，用于实现人形机器人在复杂非结构化环境中的稳健徒步。该工作由研究团队开发，核心贡献包括：通过地形边缘检测与足部体积点结合的立足点安全机制，以及平坦补丁采样策略，在单阶段强化学习下直接映射原始深度输入与本体感知到关节动作，无需外部状态估计。全尺寸人形机器人实地实验表明，该策略支持最高2.5
    m/s的速度穿越复杂地形。
  ko: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids is a knowledge node related to paper in the
    humanoid robot value chain.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.07718v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1123 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Hiking in the Wild: A Scalable Perceptive Parkour Framework for Humanoids (arXiv)'
  url: https://arxiv.org/abs/2601.07718
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 脚落在哪里，比走得多快更重要 project page
  url: https://project-instinct.github.io/hiking-in-the-wild
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
该框架旨在解决人形机器人从反应式本体感知向主动感知过渡的挑战，克服了基于地图方法的状态估计漂移（如LiDAR方法无法处理躯干抖动）以及现有端到端方法可扩展性差、训练复杂的问题。通过引入立足点安全机制（结合可扩展的地形边缘检测与足部体积点）防止边缘灾难性滑移，以及平坦补丁采样策略缓解奖励黑客攻击，实现了安全稳定的训练。系统采用单阶段强化学习，直接处理原始深度图像与本体感知数据，输出关节动作，无需外部状态估计。全尺寸人形机器人在实地实验中验证了其稳健性，最高速度达2.5 m/s，且训练与部署代码已开源以促进可重复研究。

## 核心内容
### 方法架构
- **感知与动作映射**：采用单阶段强化学习方案，将原始深度输入（来自深度相机）与本体感知（如关节角度、IMU数据）直接映射到关节动作，避免使用外部状态估计（如SLAM或里程计）。
- **立足点安全机制**：
  - **地形边缘检测（Terrain Edge Detection）**：可扩展的算法，实时识别地形边缘（如岩石边界、台阶棱角）。
  - **足部体积点（Foot Volume Points）**：在足部周围定义一组虚拟点，用于检测与边缘的碰撞风险，防止立足点滑移。
- **平坦补丁采样策略（Flat Patch Sampling）**：在训练过程中，从环境中采样平坦区域作为导航目标，避免奖励黑客攻击（如机器人通过非自然动作获取高奖励）。

### 实验设置
- **机器人平台**：全尺寸人形机器人（具体型号未在正文中指定，但提及“full-size humanoid”）。
- **训练环境**：基于物理仿真器（如Isaac Gym或MuJoCo）进行训练，使用随机生成的非结构化地形（包括斜坡、台阶、碎石等）。
- **部署**：代码开源，支持在真实机器人上直接部署，无需大量硬件修改。

### 关键数字与结论
- **速度**：在复杂地形上实现最高2.5 m/s的稳健徒步速度。
- **训练稳定性**：立足点安全机制与平坦补丁采样策略显著减少了训练过程中的失败案例（如摔倒或滑移）。
- **可扩展性**：框架支持在不同地形类型（如草地、岩石、泥地）上泛化，无需针对每种地形单独调整策略。
- **对比基线**：相比基于地图的方法（如LiDAR+SLAM），本方法避免了状态估计漂移；相比现有端到端方法（如虚拟障碍物逐例实现），本方法通过统一机制提升了可扩展性。

### 结论
该工作证明了通过单阶段强化学习与感知-动作直接映射，人形机器人可以在非结构化环境中实现高速稳健徒步，且框架具有可扩展性与可复现性。开源代码为后续研究提供了基础。

## Overview
Achieving robust humanoid hiking in complex, unstructured environments requires transitioning from reactive proprioception to proactive perception. However, integrating exteroception remains a significant challenge: mapping-based methods suffer from state estimation drift; for instance, LiDAR-based methods do not handle torso jitter well. Existing end-to-end approaches often struggle with scalability and training complexity; specifically, some previous works using virtual obstacles are implemented case-by-case. In this work, we present \textit{Hiking in the Wild}, a scalable, end-to-end parkour perceptive framework designed for robust humanoid hiking. To ensure safety and training stability, we introduce two key mechanisms: a foothold safety mechanism combining scalable \textit{Terrain Edge Detection} with \textit{Foot Volume Points} to prevent catastrophic slippage on edges, and a \textit{Flat Patch Sampling} strategy that mitigates reward hacking by generating feasible navigation targets. Our approach utilizes a single-stage reinforcement learning scheme, mapping raw depth inputs and proprioception directly to joint actions, without relying on external state estimation. Extensive field experiments on a full-size humanoid demonstrate that our policy enables robust traversal of complex terrains at speeds up to 2.5 m/s. The training and deployment code is open-sourced to facilitate reproducible research and deployment on real robots with minimal hardware modifications.

## 参考
- http://arxiv.org/abs/2601.07718v1

## 개요
이 프레임워크는 인간형 로봇이 반응적 자기 인식에서 능동적 인식으로 전환하는 과제를 해결하는 것을 목표로 하며, 지도 기반 방법의 상태 추정 드리프트(예: LiDAR 방법이 몸통 흔들림을 처리하지 못하는 문제) 및 기존 엔드투엔드 방법의 확장성 부족과 훈련 복잡성 문제를 극복한다. 착지점 안전 메커니즘(확장 가능한 지형 가장자리 감지와 발 부피 포인트 결합)을 도입하여 가장자리에서의 치명적 미끄러짐을 방지하고, 평평한 패치 샘플링 전략으로 보상 해킹을 완화하여 안전하고 안정적인 훈련을 구현한다. 시스템은 단일 단계 강화 학습을 채택하여 원시 깊이 이미지와 자기 인식 데이터를 직접 처리하고 관절 동작을 출력하며, 외부 상태 추정이 필요 없다. 전신 크기 인간형 로봇이 실외 실험에서 견고성을 검증했으며, 최고 속도는 2.5 m/s에 달하고, 훈련 및 배포 코드는 재현 가능한 연구를 위해 오픈소스로 공개되었다.

## 핵심 내용
### 방법 아키텍처
- **인식 및 동작 매핑**: 단일 단계 강화 학습 방식을 채택하여 원시 깊이 입력(깊이 카메라에서)과 자기 인식(관절 각도, IMU 데이터 등)을 관절 동작에 직접 매핑하며, 외부 상태 추정(예: SLAM 또는 주행 거리 측정)을 사용하지 않는다.
- **착지점 안전 메커니즘**:
  - **지형 가장자리 감지(Terrain Edge Detection)**: 확장 가능한 알고리즘으로, 지형 가장자리(예: 바위 경계, 계단 모서리)를 실시간으로 식별한다.
  - **발 부피 포인트(Foot Volume Points)**: 발 주변에 가상 포인트 집합을 정의하여 가장자리와의 충돌 위험을 감지하고 착지점 미끄러짐을 방지한다.
- **평평한 패치 샘플링 전략(Flat Patch Sampling)**: 훈련 중 환경에서 평평한 영역을 내비게이션 목표로 샘플링하여 보상 해킹(예: 로봇이 비자연적 동작으로 높은 보상을 얻는 것)을 방지한다.

### 실험 설정
- **로봇 플랫폼**: 전신 크기 인간형 로봇(본문에서 특정 모델은 명시되지 않았지만 "full-size humanoid"로 언급됨).
- **훈련 환경**: 물리 시뮬레이터(예: Isaac Gym 또는 MuJoCo) 기반 훈련, 무작위 생성된 비구조화 지형(경사로, 계단, 자갈 등 포함) 사용.
- **배포**: 코드는 오픈소스이며, 대규모 하드웨어 수정 없이 실제 로봇에 직접 배포 가능.

### 주요 수치 및 결론
- **속도**: 복잡한 지형에서 최고 2.5 m/s의 견고한 보행 속도 구현.
- **훈련 안정성**: 착지점 안전 메커니즘과 평평한 패치 샘플링 전략이 훈련 중 실패 사례(예: 넘어짐 또는 미끄러짐)를 크게 줄였다.
- **확장성**: 프레임워크는 다양한 지형 유형(예: 잔디, 바위, 진흙)에서 일반화를 지원하며, 각 지형에 대해 개별적으로 정책을 조정할 필요가 없다.
- **기준선 비교**: 지도 기반 방법(예: LiDAR+SLAM)과 비교하여 상태 추정 드리프트를 피했고, 기존 엔드투엔드 방법(예: 가상 장애물 사례별 구현)과 비교하여 통합 메커니즘으로 확장성을 향상시켰다.

### 결론
이 연구는 단일 단계 강화 학습과 인식-동작 직접 매핑을 통해 인간형 로봇이 비구조화 환경에서 고속 견고한 보행을 달성할 수 있음을 증명했으며, 프레임워크는 확장성과 재현성을 갖추고 있다. 오픈소스 코드는 후속 연구의 기반을 제공한다.
