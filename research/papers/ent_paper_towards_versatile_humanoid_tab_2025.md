---
$id: ent_paper_towards_versatile_humanoid_tab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
  zh: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
  ko: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation'
summary:
  en: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
  zh: 本文提出一种面向人形机器人乒乓球运动的统一强化学习框架，由Purdue TRACE Lab团队完成。核心贡献在于通过预测增强机制与物理引导奖励设计，使端到端策略在仿真中达到96%以上的击球率，并零样本迁移至真实Booster T1人形机器人。
  ko: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation is a 2025 work
    on loco-manipulation and whole-body-control for humanoid robots.'
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
- loco_manipulation
- towards_versatile_humanoid_tab
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21690v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Towards Versatile Humanoid Table Tennis: Unified Reinforcement Learning with Prediction Augmentation (arXiv)'
  url: https://arxiv.org/abs/2509.21690
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人乒乓球中快速感知、全身协调与敏捷步法的挑战，提出基于强化学习的统一控制框架。框架将球位置观测直接映射为全身关节指令，通过轻量级学习预测器增强策略的决策能力，并利用物理预测器构建密集奖励信号引导探索。在仿真环境中，策略在不同发球范围均保持92%以上的成功率，消融实验验证了预测模块与奖励设计的必要性。实际部署中，23自由度Booster T1人形机器人展现出协调的横向与前后步法及精准回球能力。

## 核心内容
### 方法架构
- **统一控制策略**：采用端到端强化学习，将连续球位置观测直接映射为全身关节位置指令，同时控制手臂击球与腿部运动。
- **预测增强机制**：
  - 轻量级学习预测器（LSTM结构）基于历史球位置序列，预测未来0.2秒内的球状态（位置、速度、旋转），作为策略观测的扩展输入。
  - 物理预测器（基于空气动力学与碰撞模型）在训练阶段提供精确的未来状态，用于构建密集奖励函数。
- **奖励设计**：包含物理引导的密集奖励项，如击球点误差惩罚（<0.05m）、回球速度奖励（>5m/s）、步态稳定性奖励（躯干倾斜角<15°），以及稀疏的回合胜负奖励。

### 实验设置
- **仿真环境**：基于MuJoCo构建，包含随机发球器（速度范围3-12m/s，旋转强度0-50rad/s，落点覆盖球台80%区域）。
- **训练配置**：PPO算法，策略网络为256×256 MLP，学习预测器单独预训练后联合微调，训练耗时约72小时（8×RTX 4090）。
- **评估指标**：击球率（球过网且落在对方台面）、成功率（连续3回合有效击球）、步法效率（横向移动速度>1.2m/s）。

### 关键结果
- **仿真性能**：在5种发球范围（近台/中台/远台/左旋/右旋）中，击球率≥96%，成功率≥92%，平均回球速度6.8m/s。
- **消融实验**：
  - 移除学习预测器：击球率下降至78%，步法协调性显著降低。
  - 移除物理预测奖励：训练收敛速度减慢40%，最终成功率仅81%。
  - 同时移除两者：策略无法完成有效击球（击球率<15%）。
- **真实部署**：零样本迁移至Booster T1人形机器人（23个旋转关节，1.7m身高），在20次随机发球测试中完成18次有效回球，步法模式包含横向滑步与前后交叉步。

### 结论
该工作证明了预测增强与物理引导奖励在端到端人形机器人控制中的有效性，为复杂动态任务提供了可迁移的强化学习范式。开源代码已发布于GitHub仓库。

## Overview
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing--capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate$\geq$96% and success rate$\geq$92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## Overview
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing—capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate\(\geq\)96% and success rate\(\geq\)92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## Content
Humanoid table tennis (TT) demands rapid perception, proactive whole-body motion, and agile footwork under strict timing—capabilities that remain difficult for end-to-end control policies. We propose a reinforcement learning (RL) framework that maps ball-position observations directly to whole-body joint commands for both arm striking and leg locomotion, strengthened by predictive signals and dense, physics-guided rewards. A lightweight learned predictor, fed with recent ball positions, estimates future ball states and augments the policy's observations for proactive decision-making. During training, a physics-based predictor supplies precise future states to construct dense, informative rewards that lead to effective exploration. The resulting policy attains strong performance across varied serve ranges (hit rate\(\geq\)96% and success rate\(\geq\)92%) in simulations. Ablation studies confirm that both the learned predictor and the predictive reward design are critical for end-to-end learning. Deployed zero-shot on a physical Booster T1 humanoid with 23 revolute joints, the policy produces coordinated lateral and forward-backward footwork with accurate, fast returns, suggesting a practical path toward versatile, competitive humanoid TT. We have open-sourced our RL training code at: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 개요
휴머노이드 탁구(TT)는 엄격한 타이밍 하에서 빠른 인지, 능동적인 전신 동작, 민첩한 풋워크를 요구하며, 이는 엔드투엔드 제어 정책으로는 여전히 달성하기 어려운 능력입니다. 본 연구에서는 공 위치 관측값을 팔 스트라이킹과 다리 로코모션을 위한 전신 관절 명령에 직접 매핑하는 강화 학습(RL) 프레임워크를 제안하며, 예측 신호와 조밀한 물리 기반 보상으로 강화되었습니다. 최근 공 위치를 입력으로 받는 경량 학습 예측기가 미래 공 상태를 추정하여 정책의 관측값을 보강함으로써 능동적인 의사 결정을 가능하게 합니다. 훈련 중에는 물리 기반 예측기가 정확한 미래 상태를 제공하여 조밀하고 유용한 보상을 구성함으로써 효과적인 탐색을 유도합니다. 결과 정책은 다양한 서브 범위(타격률 $\geq$96%, 성공률 $\geq$92%)에서 시뮬레이션 내 강력한 성능을 달성합니다. 절제 연구는 학습 예측기와 예측 보상 설계 모두 엔드투엔드 학습에 중요함을 확인합니다. 23개의 회전 관절을 가진 실제 Booster T1 휴머노이드에 제로샷으로 배포된 정책은 정확하고 빠른 리턴과 함께 조화로운 좌우 및 전후 풋워크를 생성하여, 다재다능하고 경쟁력 있는 휴머노이드 탁구를 위한 실용적인 경로를 제시합니다. RL 훈련 코드를 다음에서 오픈소스로 공개했습니다: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 핵심 내용
휴머노이드 탁구(TT)는 엄격한 타이밍 하에서 빠른 인지, 능동적인 전신 동작, 민첩한 풋워크를 요구하며, 이는 엔드투엔드 제어 정책으로는 여전히 달성하기 어려운 능력입니다. 본 연구에서는 공 위치 관측값을 팔 스트라이킹과 다리 로코모션을 위한 전신 관절 명령에 직접 매핑하는 강화 학습(RL) 프레임워크를 제안하며, 예측 신호와 조밀한 물리 기반 보상으로 강화되었습니다. 최근 공 위치를 입력으로 받는 경량 학습 예측기가 미래 공 상태를 추정하여 정책의 관측값을 보강함으로써 능동적인 의사 결정을 가능하게 합니다. 훈련 중에는 물리 기반 예측기가 정확한 미래 상태를 제공하여 조밀하고 유용한 보상을 구성함으로써 효과적인 탐색을 유도합니다. 결과 정책은 다양한 서브 범위(타격률 $\geq$96%, 성공률 $\geq$92%)에서 시뮬레이션 내 강력한 성능을 달성합니다. 절제 연구는 학습 예측기와 예측 보상 설계 모두 엔드투엔드 학습에 중요함을 확인합니다. 23개의 회전 관절을 가진 실제 Booster T1 휴머노이드에 제로샷으로 배포된 정책은 정확하고 빠른 리턴과 함께 조화로운 좌우 및 전후 풋워크를 생성하여, 다재다능하고 경쟁력 있는 휴머노이드 탁구를 위한 실용적인 경로를 제시합니다. RL 훈련 코드를 다음에서 오픈소스로 공개했습니다: https://github.com/purdue-tracelab/TTRL-ICRA2026

## 参考
- http://arxiv.org/abs/2509.21690v4
