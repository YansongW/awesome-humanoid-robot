---
$id: ent_paper_learning_locomotion_on_discret_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
  zh: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
  ko: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
summary:
  en: 'arXiv:2606.31912v1 Announce Type: new Abstract: Learning-based control has revolutionized dynamic locomotion, yet navigating
    unstructured terrain remains limited by a robot''s incomplete awareness of imminent ground contact. While global perception
    systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions,
    and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely
    reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost,
    high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors provide "pre-contact"
    feedback that is robust to self-occlusions and significantly less computationally demanding than conventional vision-based
    pipelines. By integrating these localized signals into a reinforcement learning framework, we enable the robot to anticipate
    terrain discontinuities such as gaps and stepping stones that are problematic for traditional perception stacks due to
    occlusions or state estimation drift. We demonstrate that such sparse, near-field sensing can be reliably modeled in simulation
    and transferred to the real world with high fidelity. Experimental results show that local proximity sensing substantially
    improves traversal robustness over discrete terrain and offers a low-power, low-latency alternative or complement to complex
    global perception suites in unpredictable environments. For more information about results and methods, please see the
    project website: https://sites.google.com/view/foot-tof/home.'
  zh: 本研究提出在四足机器人足部嵌入低成本、高频红外接近传感器，提供“预接触”反馈以增强离散地形（如间隙和踏脚石）的穿越鲁棒性。通过将局部信号集成到强化学习框架中，机器人能提前感知地形不连续性，克服传统视觉感知的延迟、遮挡和高计算成本问题。实验证明，这种稀疏近场传感可在仿真中可靠建模并高保真迁移至真实世界，为复杂全局感知系统提供低功耗、低延迟的替代或补充方案。
  ko: 'arXiv:2606.31912v1 Announce Type: new Abstract: Learning-based control has revolutionized dynamic locomotion, yet navigating
    unstructured terrain remains limited by a robot''s incomplete awareness of imminent ground contact. While global perception
    systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions,
    and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely
    reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost,
    high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors provide "pre-contact"
    feedback that is robust to self-occlusions and significantly less computationally demanding than conventional vision-based
    pipelines. By integrating these localized signals into a reinforcement learning framework, we enable the robot to anticipate
    terrain discontinuities such as gaps and stepping stones that are problematic for traditional perception stacks due to
    occlusions or state estimation drift. We demonstrate that such sparse, near-field sensing can be reliably modeled in simulation
    and transferred to the real world with high fidelity. Experimental results show that local proximity sensing substantially
    improves traversal robustness over discrete terrain and offers a low-power, low-latency alternative or complement to complex
    global perception suites in unpredictable environments. For more information about results and methods, please see the
    project website: https://sites.google.com/view/foot-tof/home.'
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
- learning_locomotion_on_discret
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31912v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (989 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Locomotion on Discrete Terrain via Minimal Proximity Sensing
  url: https://arxiv.org/abs/2606.31912
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
基于学习的控制方法已极大推动了动态运动的发展，但机器人在非结构化地形中仍受限于对即将发生的地面接触的不完全感知。全局感知系统（如LiDAR和深度相机）虽能提供环境上下文，却常受延迟、遮挡和密集几何重建的高计算成本困扰；而本体感觉反馈则完全被动，仅在冲击发生后启动修正。本研究探索在四足机器人足部嵌入一套最小化的低成本、高频红外接近传感器，这些传感器提供对自遮挡鲁棒且计算需求远低于传统视觉管线的“预接触”反馈。通过将这些局部信号集成到强化学习框架中，机器人能提前感知传统感知栈因遮挡或状态估计漂移而难以处理的间隙和踏脚石等地形不连续性。实验表明，这种稀疏近场传感可在仿真中可靠建模并高保真迁移至真实世界，显著提升离散地形的穿越鲁棒性，为不可预测环境中的复杂全局感知系统提供低功耗、低延迟的替代或补充方案。

## 核心内容
### 方法
- **传感器嵌入**：在四足机器人足部安装低成本、高频红外接近传感器（如ToF传感器），提供“预接触”反馈，对自遮挡鲁棒且计算需求低。
- **强化学习框架**：将局部接近信号集成到强化学习策略中，使机器人能提前感知地形不连续性（如间隙、踏脚石），弥补传统视觉感知因遮挡或状态估计漂移导致的不足。

### 实验设置
- **仿真训练**：在仿真环境中建模稀疏近场传感，训练机器人穿越离散地形（如间隙、踏脚石）。
- **真实世界迁移**：将仿真训练的策略直接部署到真实机器人，验证高保真迁移能力。

### 关键结果
- **穿越鲁棒性提升**：局部接近传感显著提高机器人在离散地形上的穿越成功率，尤其在传统感知栈易失败的场景（如遮挡或状态估计漂移）。
- **性能对比**：相比全局感知系统（LiDAR、深度相机），接近传感提供低功耗、低延迟的替代方案；相比纯本体感觉反馈，能提前预判地形变化，避免冲击后修正。
- **迁移保真度**：仿真中训练的稀疏近场传感策略可高保真迁移至真实世界，无需额外微调。

### 结论
- 局部接近传感为复杂全局感知系统提供低功耗、低延迟的替代或补充方案，尤其适用于不可预测环境。
- 该方法通过强化学习框架实现预接触反馈，显著提升四足机器人在离散地形上的运动鲁棒性。

更多结果与方法详见项目网站：https://sites.google.com/view/foot-tof/home。

## Overview
Learning-based control has revolutionized dynamic locomotion, yet navigating unstructured terrain remains limited by a robot's incomplete awareness of imminent ground contact. While global perception systems such as LiDARs and depth cameras provide environmental context, they are frequently plagued by latencies, occlusions, and the high computational cost of dense geometric reconstruction. On the other hand, proprioceptive feedback is purely reactive, initiating corrections only after impact has occurred. This work explores embedding a minimal suite of low-cost, high-frequency infrared proximity sensors directly into the feet of a quadrupedal robot. These sensors provide "pre-contact" feedback that is robust to self-occlusions and significantly less computationally demanding than conventional vision-based pipelines. By integrating these localized signals into a reinforcement learning framework, we enable the robot to anticipate terrain discontinuities such as gaps and stepping stones that are problematic for traditional perception stacks due to occlusions or state estimation drift. We demonstrate that such sparse, near-field sensing can be reliably modeled in simulation and transferred to the real world with high fidelity. Experimental results show that local proximity sensing substantially improves traversal robustness over discrete terrain and offers a low-power, low-latency alternative or complement to complex global perception suites in unpredictable environments. For more information about results and methods, please see the project website: https://sites.google.com/view/foot-tof/home.

## 参考
- http://arxiv.org/abs/2606.31912v2

## 개요
학습 기반 제어 방법은 동적 운동을 크게 발전시켰지만, 로봇은 비정형 지형에서 다가오는 지면 접촉에 대한 불완전한 인식으로 인해 여전히 제약을 받는다. LiDAR 및 깊이 카메라와 같은 전역 인식 시스템은 환경 맥락을 제공할 수 있지만, 지연, 폐색, 그리고 조밀한 기하학적 재구성의 높은 계산 비용으로 인해 자주 어려움을 겪는다. 반면 고유 감각 피드백은 완전히 수동적이며 충격 발생 후에만 수정을 시작한다. 본 연구는 네 발 달린 로봇의 발에 최소화된 저비용, 고주파 적외선 근접 센서 세트를 내장하는 방안을 탐구한다. 이 센서들은 자기 폐색에 강건하고 기존 비전 파이프라인보다 훨씬 낮은 계산 요구 사항을 가진 "접촉 전" 피드백을 제공한다. 이러한 로컬 신호를 강화 학습 프레임워크에 통합함으로써, 로봇은 폐색이나 상태 추정 드리프트로 인해 기존 인식 스택이 처리하기 어려운 간격 및 디딤돌과 같은 지형 불연속성을 사전에 감지할 수 있다. 실험은 이러한 희소 근거리 센싱이 시뮬레이션에서 안정적으로 모델링되고 실제 세계로 높은 충실도로 전이될 수 있음을 보여주며, 이산 지형 횡단 강건성을 크게 향상시켜 예측 불가능한 환경에서 복잡한 전역 인식 시스템에 대한 저전력, 저지연 대안 또는 보완책을 제공한다.

## 핵심 내용
### 방법
- **센서 내장**: 네 발 달린 로봇의 발에 저비용, 고주파 적외선 근접 센서(예: ToF 센서)를 설치하여 "접촉 전" 피드백을 제공하며, 자기 폐색에 강건하고 계산 요구 사항이 낮다.
- **강화 학습 프레임워크**: 로컬 근접 신호를 강화 학습 정책에 통합하여 로봇이 지형 불연속성(예: 간격, 디딤돌)을 사전에 감지할 수 있게 하며, 폐색이나 상태 추정 드리프트로 인한 기존 시각 인식의 한계를 보완한다.

### 실험 설정
- **시뮬레이션 훈련**: 시뮬레이션 환경에서 희소 근거리 센싱을 모델링하고, 로봇이 이산 지형(예: 간격, 디딤돌)을 횡단하도록 훈련한다.
- **실제 세계 전이**: 시뮬레이션에서 훈련된 정책을 실제 로봇에 직접 배포하여 높은 충실도 전이 능력을 검증한다.

### 주요 결과
- **횡단 강건성 향상**: 로컬 근접 센싱은 로봇의 이산 지형 횡단 성공률을 크게 향상시키며, 특히 기존 인식 스택이 실패하기 쉬운 시나리오(예: 폐색 또는 상태 추정 드리프트)에서 효과적이다.
- **성능 비교**: 전역 인식 시스템(LiDAR, 깊이 카메라)과 비교하여 근접 센싱은 저전력, 저지연 대안을 제공한다. 순수 고유 감각 피드백과 비교하여 지형 변화를 사전에 예측하여 충격 후 수정을 피할 수 있다.
- **전이 충실도**: 시뮬레이션에서 훈련된 희소 근거리 센싱 정책은 추가 미세 조정 없이 실제 세계로 높은 충실도로 전이될 수 있다.

### 결론
- 로컬 근접 센싱은 복잡한 전역 인식 시스템에 대한 저전력, 저지연 대안 또는 보완책을 제공하며, 특히 예측 불가능한 환경에 적합하다.
- 이 방법은 강화 학습 프레임워크를 통해 접촉 전 피드백을 구현하여 네 발 달린 로봇의 이산 지형 운동 강건성을 크게 향상시킨다.

더 많은 결과와 방법은 프로젝트 웹사이트에서 확인할 수 있다: https://sites.google.com/view/foot-tof/home.
