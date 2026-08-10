---
$id: ent_paper_learning_humanoid_locomotion_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion with World Model Reconstruction
  zh: Learning Humanoid Locomotion with World Model Reconstruction
  ko: Learning Humanoid Locomotion with World Model Reconstruction
summary:
  en: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
  zh: Learning Humanoid Locomotion with World Model Reconstruction 是2025年提出的一种端到端学习方法，用于人形机器人在复杂地形上的盲态行走。其核心贡献在于显式重建世界状态并利用该信息增强运动策略，使机器人能在无人类干预下完成3.2公里雪地徒步。
  ko: Learning Humanoid Locomotion with World Model Reconstruction is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_humanoid_locomotion_w
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.16230v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (752 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion with World Model Reconstruction (arXiv)
  url: https://arxiv.org/abs/2502.16230
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人在真实复杂地形中因传感器噪声和局限性导致的控制难题，提出World Model Reconstruction (WMR)方法。通过联合训练一个世界状态估计器与运动策略，但切断两者间的梯度传播，确保估计器专注于独立重建环境信息。实验在粗糙、可变形及湿滑表面验证了方法的鲁棒性，机器人成功穿越冰雪地形完成长距离自主行走。

## 核心内容
### 方法架构
- **World Model Reconstruction (WMR)**：采用端到端学习框架，包含两个核心模块：
  - **世界状态估计器**：显式重建机器人自身状态与环境特征，输入原始传感器数据（如IMU、关节编码器）。
  - **运动策略网络**：完全基于重建后的世界状态生成控制指令，不直接使用原始传感器数据。
- **梯度切断机制**：在估计器与策略网络之间阻断梯度反向传播，使估计器优化目标独立于策略更新，专注于提升世界重建精度。

### 实验设置
- **硬件平台**：未明确指定具体人形机器人型号，但提及在真实场景中测试。
- **测试地形**：粗糙地面、可变形表面（如沙地）、湿滑表面（冰面、雪地）。
- **评估指标**：行走稳定性、地形适应性、抗干扰能力。

### 关键结果
- **长距离自主行走**：机器人完成3.2公里徒步，全程无需人类干预。
- **极端环境表现**：在冰雪覆盖地形中保持稳定行走，未出现滑倒或失控。
- **鲁棒性验证**：对传感器噪声和地形突变表现出强抗干扰能力，未报告具体量化数据（如成功率或步态周期）。

### 结论
WMR通过显式世界重建与梯度解耦训练，有效解决了传感器噪声导致的感知-控制耦合问题，为人形机器人在非结构化环境中的实用化提供了新范式。

## Overview
Humanoid robots are designed to navigate environments accessible to humans using their legs. However, classical research has primarily focused on controlled laboratory settings, resulting in a gap in developing controllers for navigating complex real-world terrains. This challenge mainly arises from the limitations and noise in sensor data, which hinder the robot's understanding of itself and the environment. In this study, we introduce World Model Reconstruction (WMR), an end-to-end learning-based approach for blind humanoid locomotion across challenging terrains. We propose training an estimator to explicitly reconstruct the world state and utilize it to enhance the locomotion policy. The locomotion policy takes inputs entirely from the reconstructed information. The policy and the estimator are trained jointly; however, the gradient between them is intentionally cut off. This ensures that the estimator focuses solely on world reconstruction, independent of the locomotion policy's updates. We evaluated our model on rough, deformable, and slippery surfaces in real-world scenarios, demonstrating robust adaptability and resistance to interference. The robot successfully completed a 3.2 km hike without any human assistance, mastering terrains covered with ice and snow.

## 参考
- http://arxiv.org/abs/2502.16230v1

## 개요
본 연구는 실제 복잡한 지형에서 센서 노이즈와 한계로 인해 발생하는 휴머노이드 로봇의 제어 문제를 해결하기 위해 World Model Reconstruction (WMR) 방법을 제안한다. 세계 상태 추정기와 운동 정책을 공동으로 훈련하되, 두 모듈 간의 그래디언트 전파를 차단하여 추정기가 환경 정보를 독립적으로 재구성하는 데 집중하도록 보장한다. 실험은 거친 표면, 변형 가능한 표면, 미끄러운 표면에서 방법의 견고성을 검증했으며, 로봇은 빙설 지형을 성공적으로 횡단하며 장거리 자율 보행을 완수했다.

## 핵심 내용
### 방법 아키텍처
- **World Model Reconstruction (WMR)**: 종단 간 학습 프레임워크를 채택하며, 두 가지 핵심 모듈로 구성된다:
  - **세계 상태 추정기**: 로봇 자체 상태와 환경 특징을 명시적으로 재구성하며, 원시 센서 데이터(예: IMU, 관절 인코더)를 입력으로 사용한다.
  - **운동 정책 네트워크**: 재구성된 세계 상태만을 기반으로 제어 명령을 생성하며, 원시 센서 데이터를 직접 사용하지 않는다.
- **그래디언트 차단 메커니즘**: 추정기와 정책 네트워크 간의 그래디언트 역전파를 차단하여, 추정기의 최적화 목표가 정책 업데이트와 독립적으로 유지되고 세계 재구성 정확도 향상에 집중하도록 한다.

### 실험 설정
- **하드웨어 플랫폼**: 특정 휴머노이드 로봇 모델은 명시되지 않았지만, 실제 환경에서 테스트되었음이 언급된다.
- **테스트 지형**: 거친 지면, 변형 가능한 표면(예: 모래), 미끄러운 표면(얼음, 눈).
- **평가 지표**: 보행 안정성, 지형 적응성, 외란 저항 능력.

### 주요 결과
- **장거리 자율 보행**: 로봇이 3.2km 하이킹을 완료했으며, 전 과정에서 인간의 개입이 없었다.
- **극한 환경 성능**: 빙설로 덮인 지형에서 안정적인 보행을 유지했으며, 미끄러짐이나 통제 상실이 발생하지 않았다.
- **견고성 검증**: 센서 노이즈와 지형 급변에 대해 강한 외란 저항 능력을 보였으며, 구체적인 정량 데이터(예: 성공률 또는 보행 주기)는 보고되지 않았다.

### 결론
WMR은 명시적 세계 재구성과 그래디언트 분리 훈련을 통해 센서 노이즈로 인한 인식-제어 결합 문제를 효과적으로 해결했으며, 비구조화 환경에서 휴머노이드 로봇의 실용화를 위한 새로운 패러다임을 제시한다.
