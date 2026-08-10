---
$id: ent_paper_real_world_humanoid_locomotion_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real-World Humanoid Locomotion with Reinforcement Learning
  zh: Real-World Humanoid Locomotion with Reinforcement Learning
  ko: Real-World Humanoid Locomotion with Reinforcement Learning
summary:
  en: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
  zh: 本文提出了一种基于强化学习的全学习型人形机器人运动控制方法。该方法由因果Transformer模型驱动，通过大规模模拟训练后零样本迁移至真实世界，使机器人能够在多种户外地形上稳健行走并抵抗外部干扰。
  ko: Real-World Humanoid Locomotion with Reinforcement Learning is a 2023 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- real_world_humanoid_locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.03381v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (842 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Real-World Humanoid Locomotion with Reinforcement Learning (arXiv)
  url: https://arxiv.org/abs/2303.03381
  date: '2023'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Real-World Humanoid Locomotion with Reinforcement Learning project page
  url: https://learning-humanoid-locomotion.github.io/
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对传统人形机器人控制器泛化能力不足的问题，提出了一种完全基于学习的运动控制方案。核心创新在于使用因果Transformer架构，通过处理本体感知观测与动作的历史序列来预测下一步动作，利用上下文信息实现行为自适应而无需更新模型权重。模型在模拟环境中通过无模型强化学习进行大规模训练，并在多样化随机化环境中完成学习后，直接部署到真实人形机器人上实现零样本迁移。实验证明，该控制器能够使机器人在多种户外地形上稳定行走，并具备抵抗外部干扰和上下文自适应能力。

## 核心内容
### 方法架构
- **控制器设计**：采用因果Transformer模型，输入为历史本体感知观测（如关节角度、IMU数据）与动作序列，输出为下一步动作指令。
- **核心假设**：观测-动作历史序列蕴含环境动态信息，Transformer可通过上下文学习（in-context learning）自适应调整行为，无需权重更新。

### 训练策略
- **强化学习框架**：使用无模型（model-free）强化学习算法，在模拟环境中进行大规模训练。
- **环境随机化**：构建包含多种地形、摩擦系数、外部扰动等参数的随机化环境集合，增强模型泛化能力。
- **零样本迁移**：训练完成后直接部署至真实人形机器人，无需额外微调或领域适配。

### 实验设置与结果
- **硬件平台**：未明确指定具体人形机器人型号，但强调在真实世界户外场景测试。
- **性能表现**：
  - 能够稳定行走于草地、碎石路、斜坡等多种户外地形。
  - 对外部推挤、负载变化等干扰具有鲁棒性。
  - 通过上下文历史信息实现实时行为调整（如根据地形变化自动调整步态）。
- **关键数字**：未提供具体成功率或步态参数，但强调零样本迁移的成功实现。

### 结论
该工作证明了纯学习型方法在真实世界人形机器人运动控制中的可行性，Transformer的上下文自适应能力为复杂环境下的泛化提供了新路径。

## Overview
Humanoid robots that can autonomously operate in diverse environments have the potential to help address labour shortages in factories, assist elderly at homes, and colonize new planets. While classical controllers for humanoid robots have shown impressive results in a number of settings, they are challenging to generalize and adapt to new environments. Here, we present a fully learning-based approach for real-world humanoid locomotion. Our controller is a causal transformer that takes the history of proprioceptive observations and actions as input and predicts the next action. We hypothesize that the observation-action history contains useful information about the world that a powerful transformer model can use to adapt its behavior in-context, without updating its weights. We train our model with large-scale model-free reinforcement learning on an ensemble of randomized environments in simulation and deploy it to the real world zero-shot. Our controller can walk over various outdoor terrains, is robust to external disturbances, and can adapt in context.

## 参考
- http://arxiv.org/abs/2303.03381v2

## 개요
본 연구는 전통적인 휴머노이드 로봇 컨트롤러의 일반화 능력 부족 문제를 해결하기 위해 완전히 학습 기반의 운동 제어 방안을 제안한다. 핵심 혁신은 인과적 Transformer 아키텍처를 사용하여, 본체 인식 관측과 행동의 과거 시퀀스를 처리해 다음 행동을 예측하고, 컨텍스트 정보를 활용해 모델 가중치 업데이트 없이 행동을 자가 적응시키는 것이다. 모델은 시뮬레이션 환경에서 모델 프리 강화 학습을 통해 대규모 훈련을 거치며, 다양한 무작위 환경에서 학습을 완료한 후 실제 휴머노이드 로봇에 직접 배포하여 제로샷 전이를 구현한다. 실험 결과, 이 컨트롤러는 로봇이 다양한 야외 지형에서 안정적으로 보행할 수 있게 하며, 외부 간섭 저항 및 컨텍스트 자가 적응 능력을 갖추고 있음을 증명한다.

## 핵심 내용
### 방법 아키텍처
- **컨트롤러 설계**: 인과적 Transformer 모델을 사용하며, 입력은 과거 본체 인식 관측(예: 관절 각도, IMU 데이터)과 행동 시퀀스이고, 출력은 다음 행동 명령이다.
- **핵심 가정**: 관측-행동 과거 시퀀스는 환경 동적 정보를 포함하며, Transformer는 컨텍스트 학습(in-context learning)을 통해 가중치 업데이트 없이 행동을 자가 적응시킬 수 있다.

### 훈련 전략
- **강화 학습 프레임워크**: 모델 프리(model-free) 강화 학습 알고리즘을 사용하여 시뮬레이션 환경에서 대규모 훈련을 수행한다.
- **환경 무작위화**: 다양한 지형, 마찰 계수, 외부 교란 등의 매개변수를 포함한 무작위 환경 집합을 구축하여 모델 일반화 능력을 강화한다.
- **제로샷 전이**: 훈련 완료 후 추가 미세 조정이나 도메인 적응 없이 실제 휴머노이드 로봇에 직접 배포한다.

### 실험 설정 및 결과
- **하드웨어 플랫폼**: 특정 휴머노이드 로봇 모델은 명시되지 않았지만, 실제 세계 야외 시나리오에서 테스트되었음을 강조한다.
- **성능 표현**:
  - 잔디, 자갈길, 경사로 등 다양한 야외 지형에서 안정적으로 보행할 수 있다.
  - 외부 밀기, 부하 변화 등의 간섭에 대해 견고성을 갖는다.
  - 컨텍스트 과거 정보를 통해 실시간 행동 조정(예: 지형 변화에 따라 보행 자세 자동 조정)을 구현한다.
- **핵심 수치**: 구체적인 성공률이나 보행 매개변수는 제공되지 않았지만, 제로샷 전이의 성공적 구현을 강조한다.

### 결론
본 연구는 순수 학습 기반 방법이 실제 세계 휴머노이드 로봇 운동 제어에서 가능함을 증명했으며, Transformer의 컨텍스트 자가 적응 능력이 복잡한 환경에서의 일반화를 위한 새로운 경로를 제공한다.
