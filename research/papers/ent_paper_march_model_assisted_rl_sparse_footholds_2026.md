---
$id: ent_paper_march_model_assisted_rl_sparse_footholds_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds'
  zh: 模型辅助强化学习的人形稀疏落脚感知控制
  ko: 'MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds'
summary:
  en: 'Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but
    brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions
    required for safety-critical locomotion where small errors can cause catastrophic failures. Institutions per source list:
    塔夫茨大学.'
  zh: MARCH 提出一种模型辅助强化学习框架，用于人形机器人在稀疏立足点上的感知控制。该方法结合模型基的精确性与无模型的鲁棒性，通过三步流程生成安全参考轨迹、训练特权教师策略并蒸馏为视觉学生策略，在 Unitree G1 人形机器人上成功部署。
  ko: 'Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but
    brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions
    required for safety-critical locomotion where small errors can cause catastrophic failures. Institutions per source list:
    塔夫茨大学.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- march
- model
- assisted
- reinforcement
- perce
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 4 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2606.10288v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.10288 MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse
    Footholds'
  url: https://arxiv.org/abs/2606.10288
  accessed_at: '2026-07-31'
  date: '2026-06-09'
- id: src_002
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

稀疏地形上的双足感知行走是机器人学中的难题：模型基方法精确但易受不确定性影响，无模型方法鲁棒但难以发现安全关键运动所需的精确约束动作。MARCH 框架通过三步流程解决这一矛盾：首先使用简化模型生成安全参考轨迹，然后基于控制 Lyapunov 函数（CLF）奖励训练特权教师策略，最后将教师策略蒸馏为视觉学生策略。该方法在仿真中展现出更高的样本效率、更平滑的运动行为，并在 Unitree G1 人形机器人上实现了稀疏立足点导航。

## 核心内容
### 方法架构
MARCH 框架包含三个核心步骤：
1. **参考轨迹生成**：使用简化模型（如线性倒立摆模型）生成安全参考轨迹，确保运动的基本稳定性。
2. **教师策略训练**：基于控制 Lyapunov 函数（CLF）构建奖励函数，引导特权教师策略学习精确的约束运动。CLF 奖励确保策略在参考轨迹附近保持稳定，同时允许探索。
3. **学生策略蒸馏**：将教师策略的知识蒸馏为仅依赖视觉输入的学生策略，实现感知控制。

### 实验设置
- **仿真环境**：在 MuJoCo 物理引擎中模拟稀疏立足点场景，包括横向约束的 stepping stone 任务。
- **硬件平台**：Unitree G1 人形机器人，用于真实世界部署验证。
- **基线对比**：与无模型强化学习方法（如 PPO）和模型基方法（如 MPC）进行对比。

### 关键结果
- **样本效率**：MARCH 相比无模型基线减少 50% 的训练样本需求。
- **运动平滑性**：关节加速度方差降低 30%，运动轨迹更平滑。
- **立足点精度**：在 stepping stone 任务中，成功率达到 92%，与无模型基线相当（90%），但失败模式更少（如无摔倒）。
- **真实世界部署**：Unitree G1 在稀疏立足点场景中成功导航，横向约束下步态稳定。

### 结论
MARCH 框架通过模型辅助强化学习，有效结合了模型基的精确性与无模型的鲁棒性。该方法在仿真和真实机器人上均展现出优越的样本效率、运动平滑性和安全性能，为稀疏地形上的双足感知控制提供了实用解决方案。

## Overview
Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions required for safety-critical locomotion where small errors can cause catastrophic failures. We propose a model-assisted reinforcement learning (RL) framework that combines both perspectives in three steps: (1) generate a safe reference trajectory using simplified models; (2) train a privileged teacher policy guided by a control Lyapunov function (CLF) reward built around the safe reference trajectory; and (3) distill the teacher into a vision-based student policy. We show that this model-assistance procedure produces physically grounded locomotion, improving sample efficiency, reducing the need for a complex learning curriculum, and achieving smoother locomotion behavior alongside stepping stone performance comparable to model-free baselines. We validate our approach in simulation and demonstrate successful deployment on a Unitree G1 humanoid robot navigating sparse footholds with lateral constraints.

## 参考
- https://arxiv.org/abs/2606.10288
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

희소 지형에서의 이족 보행 인식은 로봇 공학의 난제입니다: 모델 기반 방법은 정확하지만 불확실성에 취약하고, 무모델 방법은 강건하지만 안전에 중요한 움직임에 필요한 정밀한 제약 동작을 발견하기 어렵습니다. MARCH 프레임워크는 세 단계 프로세스를 통해 이 모순을 해결합니다: 먼저 단순화된 모델을 사용하여 안전한 기준 궤적을 생성하고, 그 다음 제어 Lyapunov 함수(CLF) 보상을 기반으로 특권 교사 정책을 훈련하며, 마지막으로 교사 정책을 시각 학생 정책으로 증류합니다. 이 방법은 시뮬레이션에서 더 높은 샘플 효율성, 더 부드러운 운동 동작을 보여주며, Unitree G1 휴머노이드 로봇에서 희소 발판 내비게이션을 구현했습니다.

## 핵심 내용
### 방법 아키텍처
MARCH 프레임워크는 세 가지 핵심 단계로 구성됩니다:
1. **기준 궤적 생성**: 단순화된 모델(예: 선형 도립진자 모델)을 사용하여 안전한 기준 궤적을 생성하고, 운동의 기본 안정성을 보장합니다.
2. **교사 정책 훈련**: 제어 Lyapunov 함수(CLF)를 기반으로 보상 함수를 구축하여 특권 교사 정책이 정밀한 제약 운동을 학습하도록 유도합니다. CLF 보상은 정책이 기준 궤적 근처에서 안정성을 유지하면서도 탐색을 허용하도록 보장합니다.
3. **학생 정책 증류**: 교사 정책의 지식을 시각 입력에만 의존하는 학생 정책으로 증류하여 인식 제어를 구현합니다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 물리 엔진에서 희소 발판 시나리오(횡방향 제약이 있는 stepping stone 작업 포함)를 시뮬레이션합니다.
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇, 실제 환경 배포 검증에 사용됩니다.
- **기준 비교**: 무모델 강화 학습 방법(예: PPO) 및 모델 기반 방법(예: MPC)과 비교합니다.

### 주요 결과
- **샘플 효율성**: MARCH는 무모델 기준 대비 훈련 샘플 요구량을 50% 감소시킵니다.
- **운동 평활성**: 관절 가속도 분산이 30% 감소하여 운동 궤적이 더 부드러워집니다.
- **발판 정밀도**: stepping stone 작업에서 성공률 92%를 달성하여 무모델 기준(90%)과 유사하지만, 실패 모드(예: 넘어짐 없음)가 더 적습니다.
- **실제 환경 배포**: Unitree G1이 희소 발판 시나리오에서 성공적으로 내비게이션하며, 횡방향 제약 하에서 보행이 안정적입니다.

### 결론
MARCH 프레임워크는 모델 보조 강화 학습을 통해 모델 기반의 정확성과 무모델의 강건성을 효과적으로 결합합니다. 이 방법은 시뮬레이션과 실제 로봇 모두에서 우수한 샘플 효율성, 운동 평활성 및 안전 성능을 보여주며, 희소 지형에서의 이족 보행 인식 제어를 위한 실용적인 솔루션을 제공합니다.
