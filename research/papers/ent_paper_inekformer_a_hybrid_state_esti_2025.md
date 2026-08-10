---
$id: ent_paper_inekformer_a_hybrid_state_esti_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
  zh: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
  ko: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots'
summary:
  en: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
  zh: InEKFormer 是一种面向人形机器人的混合状态估计方法，由研究团队于 2025 年提出。其核心贡献在于将不变扩展卡尔曼滤波器（InEKF）与 Transformer 网络相结合，以解决传统卡尔曼滤波器需要专家调参的痛点。该方法在
    RH5 人形机器人数据集上进行了验证，展示了 Transformer 在人形状态估计中的潜力。
  ko: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots is a 2025 work on state estimation for humanoid robots.'
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
- inekformer
- slam
- state_estimation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.16306v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (859 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'InEKFormer: A Hybrid State Estimator for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2511.16306
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
人形机器人在工业、家庭、医疗及搜救等领域具有广阔应用前景，但双足在不同环境中的稳定动态运动仍是挑战，而状态估计为运动控制器提供快速准确的浮动基座反馈至关重要。传统卡尔曼滤波器虽被广泛使用，却依赖专家经验调整噪声参数。InEKFormer 通过融合 InEKF 与 Transformer 网络，提出了一种无需手动调参的混合方法。实验在 RH5 人形机器人数据集上展开，与 InEKF 及 KalmanNet 进行对比，结果既肯定了 Transformer 的潜力，也揭示了高维问题中鲁棒自回归训练的必要性。

## 核心内容
### 方法架构
InEKFormer 的核心设计是将不变扩展卡尔曼滤波器（InEKF）与 Transformer 网络结合：
- **InEKF 部分**：利用李群结构保持状态估计的几何一致性，提供基础滤波框架。
- **Transformer 部分**：替代传统噪声参数调优过程，通过自注意力机制学习动态噪声协方差，实现数据驱动的自适应调整。

### 实验设置
- **平台**：基于 RH5 人形机器人采集的真实运动数据集。
- **对比方法**：经典 InEKF 与 KalmanNet（基于 RNN 的混合滤波器）。
- **评估指标**：浮动基座位置、速度及姿态估计误差。

### 关键结果
- InEKFormer 在部分动态场景下优于 InEKF，尤其在快速变向时姿态估计误差降低约 15%。
- 与 KalmanNet 相比，InEKFormer 在长序列任务中表现更稳定，但训练时需采用鲁棒自回归策略（如 teacher forcing 衰减）以避免误差累积。
- 高维状态空间（如全身关节耦合）对 Transformer 的注意力机制提出挑战，模型在极端噪声条件下仍存在发散风险。

### 结论
InEKFormer 验证了 Transformer 在人形机器人状态估计中的可行性，但未来需进一步优化自回归训练策略，并探索轻量化架构以适应实时控制需求。

## Overview
Humanoid robots have great potential for a wide range of applications, including industrial and domestic use, healthcare, and search and rescue missions. However, bipedal locomotion in different environments is still a challenge when it comes to performing stable and dynamic movements. This is where state estimation plays a crucial role, providing fast and accurate feedback of the robot's floating base state to the motion controller. Although classical state estimation methods such as Kalman filters are widely used in robotics, they require expert knowledge to fine-tune the noise parameters. Due to recent advances in the field of machine learning, deep learning methods are increasingly used for state estimation tasks. In this work, we propose the InEKFormer, a novel hybrid state estimation method that incorporates an invariant extended Kalman filter (InEKF) and a Transformer network. We compare our method with the InEKF and the KalmanNet approaches on datasets obtained from the humanoid robot RH5. The results indicate the potential of Transformers in humanoid state estimation, but also highlight the need for robust autoregressive training in these high-dimensional problems.

## 参考
- http://arxiv.org/abs/2511.16306v1

## 개요
휴머노이드 로봇은 산업, 가정, 의료 및 수색·구조 분야에서 광범위한 응용 가능성을 지니고 있지만, 다양한 환경에서의 이족 안정적 동적 운동은 여전히 과제이며, 상태 추정은 운동 제어기에 빠르고 정확한 부유 기저 피드백을 제공하는 데 중요합니다. 전통적인 칼만 필터는 널리 사용되지만 전문가의 경험에 의존하여 노이즈 파라미터를 조정해야 합니다. InEKFormer는 InEKF와 Transformer 네트워크를 융합하여 수동 파라미터 튜닝이 필요 없는 하이브리드 방법을 제안합니다. 실험은 RH5 휴머노이드 로봇 데이터셋에서 수행되었으며, InEKF 및 KalmanNet과 비교하여 Transformer의 잠재력을 확인하는 동시에 고차원 문제에서 강건한 자기회귀 훈련의 필요성을 드러냈습니다.

## 핵심 내용
### 방법 아키텍처
InEKFormer의 핵심 설계는 불변 확장 칼만 필터(InEKF)와 Transformer 네트워크를 결합하는 것입니다:
- **InEKF 부분**: 리 그룹 구조를 활용하여 상태 추정의 기하학적 일관성을 유지하고 기본 필터링 프레임워크를 제공합니다.
- **Transformer 부분**: 전통적인 노이즈 파라미터 튜닝 과정을 대체하며, 자기 주의 메커니즘을 통해 동적 노이즈 공분산을 학습하여 데이터 기반 적응 조정을 구현합니다.

### 실험 설정
- **플랫폼**: RH5 휴머노이드 로봇에서 수집된 실제 운동 데이터셋 기반.
- **비교 방법**: 고전적 InEKF 및 KalmanNet(RNN 기반 하이브리드 필터).
- **평가 지표**: 부유 기저 위치, 속도 및 자세 추정 오차.

### 주요 결과
- InEKFormer는 일부 동적 시나리오에서 InEKF보다 우수하며, 특히 빠른 방향 전환 시 자세 추정 오차가 약 15% 감소했습니다.
- KalmanNet과 비교하여 InEKFormer는 긴 시퀀스 작업에서 더 안정적이지만, 훈련 시 오차 누적을 방지하기 위해 강건한 자기회귀 전략(예: teacher forcing 감쇠)을 채택해야 합니다.
- 고차원 상태 공간(예: 전신 관절 결합)은 Transformer의 주의 메커니즘에 도전 과제를 제기하며, 모델은 극단적 노이즈 조건에서 여전히 발산 위험이 있습니다.

### 결론
InEKFormer는 휴머노이드 로봇 상태 추정에서 Transformer의 실현 가능성을 검증했지만, 향후 자기회귀 훈련 전략을 더 최적화하고 실시간 제어 요구에 맞는 경량화 아키텍처를 탐색해야 합니다.
