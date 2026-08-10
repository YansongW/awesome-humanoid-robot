---
$id: ent_paper_stability_aware_retargeting_fo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
  zh: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
  ko: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation
summary:
  en: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
  zh: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation 是2025年提出的一种面向人形机器人多接触遥操作的重定向方法。该方法通过动态调整接触点与姿态，提升在非共面表面等困难场景下的稳定性。核心贡献在于提出了一种基于质心稳定性的重定向技术，并利用稳定性裕度梯度的解析计算来指导遥操作设定点的局部调整。
  ko: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation is a 2025 work on teleoperation for humanoid robots.
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
- stability_aware_retargeting_fo
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.04353v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (587 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Stability-Aware Retargeting for Humanoid Multi-Contact Teleoperation (arXiv)
  url: https://arxiv.org/abs/2510.04353
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人遥操作中因手部接触与非共面表面导致的电机扭矩饱和或滑移失稳问题，提出了一种质心稳定性感知的重定向方法。方法的核心是高效解析计算稳定性裕度梯度，以此识别对遥操作设定点高度敏感的场景，并局部调整这些设定点以增强稳定性。通过在仿真和硬件上对人形机器人进行遥操作操控任务验证，该方法显著提升了稳定性裕度。实验还表明，更高的稳定性裕度与更好的脉冲抗扰能力和关节扭矩裕度正相关。

## 核心内容
### 方法概述
- **问题背景**：人形机器人遥操作在涉及手部接触和非共面表面时，容易因电机扭矩饱和或滑移导致失稳。
- **核心方法**：提出一种基于质心稳定性的重定向方法，动态调整接触点和姿态。
- **关键技术**：高效解析计算稳定性裕度梯度，用于识别对遥操作设定点高度敏感的场景，并局部调整这些设定点。

### 实验设置
- **验证方式**：在仿真和硬件平台上，通过遥操作人形机器人执行操控任务进行验证。
- **评估指标**：稳定性裕度、脉冲抗扰能力、关节扭矩裕度。

### 关键结果
- **稳定性提升**：所提方法显著增加了稳定性裕度。
- **相关性验证**：实验证明，更高的稳定性裕度与更好的脉冲抗扰能力和关节扭矩裕度正相关。

### 结论
该方法有效解决了多接触遥操作中的稳定性难题，为复杂环境下的机器人操控提供了可靠方案。

## Overview
Teleoperation is a powerful method to generate reference motions and enable humanoid robots to perform a broad range of tasks. However, teleoperation becomes challenging when using hand contacts and non-coplanar surfaces, often leading to motor torque saturation or loss of stability through slipping. We propose a centroidal stability-based retargeting method that dynamically adjusts contact points and posture during teleoperation to enhance stability in these difficult scenarios. Central to our approach is an efficient analytical calculation of the stability margin gradient. This gradient is used to identify scenarios for which stability is highly sensitive to teleoperation setpoints and inform the local adjustment of these setpoints. We validate the framework in simulation and hardware by teleoperating manipulation tasks on a humanoid, demonstrating increased stability margins. We also demonstrate empirically that higher stability margins correlate with improved impulse resilience and joint torque margin.

## 参考
- http://arxiv.org/abs/2510.04353v1

## 개요
본 연구는 인간형 로봇 원격 조작에서 손 접촉 및 비공면 표면으로 인한 모터 토크 포화 또는 미끄러짐 불안정 문제를 해결하기 위해, 질량 중심 안정성 인식 리다이렉션 방법을 제안한다. 이 방법의 핵심은 안정성 여유 기울기를 효율적으로 해석적으로 계산하여, 원격 조작 설정점에 매우 민감한 시나리오를 식별하고, 이러한 설정점을 국부적으로 조정하여 안정성을 강화하는 것이다. 시뮬레이션과 하드웨어에서 인간형 로봇을 원격 조작하는 작업을 통해 검증한 결과, 이 방법은 안정성 여유를 크게 향상시켰다. 실험은 또한 더 높은 안정성 여유가 더 나은 펄스 외란 저항 능력 및 관절 토크 여유와 양의 상관관계가 있음을 보여주었다.

## 핵심 내용
### 방법 개요
- **문제 배경**: 인간형 로봇 원격 조작은 손 접촉 및 비공면 표면을 포함할 때 모터 토크 포화 또는 미끄러짐으로 인해 불안정해지기 쉽다.
- **핵심 방법**: 질량 중심 안정성 기반 리다이렉션 방법을 제안하여 접촉점과 자세를 동적으로 조정한다.
- **핵심 기술**: 안정성 여유 기울기를 효율적으로 해석적으로 계산하여, 원격 조작 설정점에 매우 민감한 시나리오를 식별하고, 이러한 설정점을 국부적으로 조정한다.

### 실험 설정
- **검증 방식**: 시뮬레이션 및 하드웨어 플랫폼에서 인간형 로봇을 원격 조작하여 조작 작업을 수행함으로써 검증한다.
- **평가 지표**: 안정성 여유, 펄스 외란 저항 능력, 관절 토크 여유.

### 핵심 결과
- **안정성 향상**: 제안된 방법은 안정성 여유를 크게 증가시켰다.
- **상관성 검증**: 실험은 더 높은 안정성 여유가 더 나은 펄스 외란 저항 능력 및 관절 토크 여유와 양의 상관관계가 있음을 증명했다.

### 결론
이 방법은 다중 접촉 원격 조작에서의 안정성 문제를 효과적으로 해결하며, 복잡한 환경에서의 로봇 조작에 신뢰할 수 있는 솔루션을 제공한다.
