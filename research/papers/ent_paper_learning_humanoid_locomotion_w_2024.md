---
$id: ent_paper_learning_humanoid_locomotion_w_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Humanoid Locomotion with Perceptive Internal Model
  zh: Learning Humanoid Locomotion with Perceptive Internal Model
  ko: Learning Humanoid Locomotion with Perceptive Internal Model
summary:
  en: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
  zh: 《Learning Humanoid Locomotion with Perceptive Internal Model》是2024年提出的人形机器人运动控制方法。其核心贡献在于设计了基于实时更新高程地图的感知内部模型（PIM），通过混合内部模型（HIM）优化策略，使机器人能清晰感知脚下地形，在3小时内完成训练，并成功实现连续爬楼梯等复杂地形运动。
  ko: Learning Humanoid Locomotion with Perceptive Internal Model is a 2024 work on locomotion for humanoid robots.
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.14386v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (712 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning Humanoid Locomotion with Perceptive Internal Model (arXiv)
  url: https://arxiv.org/abs/2411.14386
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
与四足机器人不同，人形机器人因高自由度与不稳定的形态，必须依赖精确感知才能稳定运动。但直接引入感知信号常会引入扰动，降低鲁棒性与效率。本文提出的PIM方法利用机器人周围持续更新的高程地图作为感知输入，在仿真中基于真实障碍物高度训练策略，推理时则从构建的地图中采样高度数据。该方法无需渲染深度图，计算成本极低，在RTX 4090 GPU上仅需3小时即可完成训练。实验验证了该方法在不同人形机器人、室内外地形、楼梯及多种传感器配置下的有效性，尤其能实现连续爬楼梯功能，有望成为未来人形控制算法的基础。

## 核心内容
### 方法架构
- **感知内部模型（PIM）**：以机器人为中心，实时构建并更新周围地形的高程地图，作为感知输入。
- **训练策略**：在仿真环境中使用地面真实障碍物高度数据，基于混合内部模型（HIM）优化策略。
- **推理阶段**：从构建的高程地图中采样高度数据，替代直接编码深度图或原始点云的方法。

### 关键设计
- **抗干扰能力**：通过清晰感知脚下地形，减少相机运动或噪声对感知的干扰。
- **计算效率**：无需在仿真中渲染深度图，仅增加极小的计算开销，训练时间缩短至3小时（RTX 4090 GPU）。

### 实验设置与结果
- **机器人平台**：多种人形机器人（具体型号未在正文中列出）。
- **测试场景**：室内外地形、楼梯、不同传感器配置。
- **核心成果**：实现人形机器人连续爬楼梯，验证了方法在复杂地形下的鲁棒性与泛化能力。

### 结论
PIM方法通过轻量级高程地图感知，解决了人形机器人感知引入扰动的问题，为未来人形控制算法提供了基础框架。

## Overview
In contrast to quadruped robots that can navigate diverse terrains using a "blind" policy, humanoid robots require accurate perception for stable locomotion due to their high degrees of freedom and inherently unstable morphology. However, incorporating perceptual signals often introduces additional disturbances to the system, potentially reducing its robustness, generalizability, and efficiency. This paper presents the Perceptive Internal Model (PIM), which relies on onboard, continuously updated elevation maps centered around the robot to perceive its surroundings. We train the policy using ground-truth obstacle heights surrounding the robot in simulation, optimizing it based on the Hybrid Internal Model (HIM), and perform inference with heights sampled from the constructed elevation map. Unlike previous methods that directly encode depth maps or raw point clouds, our approach allows the robot to perceive the terrain beneath its feet clearly and is less affected by camera movement or noise. Furthermore, since depth map rendering is not required in simulation, our method introduces minimal additional computational costs and can train the policy in 3 hours on an RTX 4090 GPU. We verify the effectiveness of our method across various humanoid robots, various indoor and outdoor terrains, stairs, and various sensor configurations. Our method can enable a humanoid robot to continuously climb stairs and has the potential to serve as a foundational algorithm for the development of future humanoid control methods.

## 参考
- http://arxiv.org/abs/2411.14386v1

## 개요
사족 로봇과 달리, 휴머노이드 로봇은 높은 자유도와 불안정한 형태로 인해 정밀한 인식에 의존해야 안정적으로 움직일 수 있습니다. 그러나 인식 신호를 직접 도입하면 종종 교란이 발생하여 강건성과 효율성이 저하됩니다. 본 논문에서 제안하는 PIM 방법은 로봇 주변에서 지속적으로 업데이트되는 고도 지도를 인식 입력으로 활용하며, 시뮬레이션에서 실제 장애물 높이를 기반으로 정책을 훈련하고, 추론 시에는 구축된 지도에서 높이 데이터를 샘플링합니다. 이 방법은 깊이 맵을 렌더링할 필요가 없어 계산 비용이 매우 낮으며, RTX 4090 GPU에서 단 3시간 만에 훈련을 완료할 수 있습니다. 실험을 통해 이 방법이 다양한 휴머노이드 로봇, 실내외 지형, 계단 및 다양한 센서 구성에서 효과적임을 검증했으며, 특히 연속 계단 오르기 기능을 구현하여 향후 휴머노이드 제어 알고리즘의 기반이 될 가능성을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **인식 내부 모델(PIM)**: 로봇 중심으로 주변 지형의 고도 지도를 실시간으로 구축하고 업데이트하여 인식 입력으로 사용합니다.
- **훈련 전략**: 시뮬레이션 환경에서 실제 장애물 높이 데이터를 사용하고, 혼합 내부 모델(HIM)을 기반으로 정책을 최적화합니다.
- **추론 단계**: 구축된 고도 지도에서 높이 데이터를 샘플링하여 깊이 맵이나 원시 포인트 클라우드를 직접 인코딩하는 방식을 대체합니다.

### 핵심 설계
- **교란 저항 능력**: 발 아래 지형을 명확히 인식하여 카메라 움직임이나 노이즈가 인식에 미치는 교란을 줄입니다.
- **계산 효율성**: 시뮬레이션에서 깊이 맵을 렌더링할 필요가 없어 추가 계산 오버헤드가 매우 작으며, 훈련 시간이 3시간(RTX 4090 GPU)으로 단축됩니다.

### 실험 설정 및 결과
- **로봇 플랫폼**: 다양한 휴머노이드 로봇(구체적인 모델은 본문에 나열되지 않음).
- **테스트 시나리오**: 실내외 지형, 계단, 다양한 센서 구성.
- **핵심 성과**: 휴머노이드 로봇의 연속 계단 오르기를 구현하여 복잡한 지형에서의 강건성과 일반화 능력을 검증했습니다.

### 결론
PIM 방법은 경량 고도 지도 인식을 통해 휴머노이드 로봇의 인식 도입으로 인한 교란 문제를 해결하며, 향후 휴머노이드 제어 알고리즘을 위한 기본 프레임워크를 제공합니다.
