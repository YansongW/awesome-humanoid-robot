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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21690v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1082 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.21690v4

## 개요
이 연구는 휴머노이드 로봇 탁구에서의 빠른 인지, 전신 조화, 민첩한 풋워크의 도전 과제를 해결하기 위해 강화 학습 기반의 통합 제어 프레임워크를 제안합니다. 이 프레임워크는 공 위치 관측을 전신 관절 명령으로 직접 매핑하고, 경량 학습 예측기를 통해 정책의 의사 결정 능력을 강화하며, 물리 예측기를 활용해 밀집 보상 신호를 구성하여 탐색을 유도합니다. 시뮬레이션 환경에서 정책은 다양한 발사 범위에서 92% 이상의 성공률을 유지했으며, 절제 실험을 통해 예측 모듈과 보상 설계의 필요성을 검증했습니다. 실제 배포에서는 23자유도 Booster T1 휴머노이드 로봇이 조화로운 횡방향 및 전후 풋워크와 정확한 리턴 능력을 보여주었습니다.

## 핵심 내용
### 방법 아키텍처
- **통합 제어 정책**: 엔드투엔드 강화 학습을 채택하여 연속적인 공 위치 관측을 전신 관절 위치 명령으로 직접 매핑하며, 팔 스윙과 다리 움직임을 동시에 제어합니다.
- **예측 강화 메커니즘**:
  - 경량 학습 예측기(LSTM 구조)는 과거 공 위치 시퀀스를 기반으로 향후 0.2초 내의 공 상태(위치, 속도, 회전)를 예측하여 정책 관측의 확장 입력으로 사용합니다.
  - 물리 예측기(공기 역학 및 충돌 모델 기반)는 훈련 단계에서 정확한 미래 상태를 제공하여 밀집 보상 함수를 구성하는 데 사용됩니다.
- **보상 설계**: 물리적 안내를 받는 밀집 보상 항목(예: 타점 오차 패널티(<0.05m), 리턴 속도 보상(>5m/s), 보행 안정성 보상(몸통 기울기 각도<15°))과 희소한 라운드 승패 보상을 포함합니다.

### 실험 설정
- **시뮬레이션 환경**: MuJoCo 기반으로 구축되었으며, 무작위 발사기(속도 범위 3-12m/s, 회전 강도 0-50rad/s, 착점이 탁구대의 80% 영역을 커버)를 포함합니다.
- **훈련 구성**: PPO 알고리즘, 정책 네트워크는 256×256 MLP이며, 학습 예측기는 별도로 사전 훈련 후 공동 미세 조정하며, 훈련 시간은 약 72시간(8×RTX 4090)입니다.
- **평가 지표**: 타구율(공이 네트를 넘고 상대 탁구대에 떨어짐), 성공률(연속 3라운드 유효 타구), 풋워크 효율(횡방향 이동 속도>1.2m/s).

### 주요 결과
- **시뮬레이션 성능**: 5가지 발사 범위(근대/중대/원대/좌회전/우회전)에서 타구율≥96%, 성공률≥92%, 평균 리턴 속도 6.8m/s를 달성했습니다.
- **절제 실험**:
  - 학습 예측기 제거: 타구율이 78%로 하락하고 풋워크 조화가 크게 저하됨.
  - 물리 예측 보상 제거: 훈련 수렴 속도가 40% 느려지고 최종 성공률이 81%에 그침.
  - 둘 다 제거: 정책이 유효한 타구를 완료하지 못함(타구율<15%).
- **실제 배포**: Booster T1 휴머노이드 로봇(23개 회전 관절, 1.7m 키)에 제로샷 전이하여 20회 무작위 발사 테스트에서 18회 유효 리턴을 완료했으며, 풋워크 패턴은 횡방향 슬라이딩 스텝과 전후 교차 스텝을 포함합니다.

### 결론
이 연구는 예측 강화와 물리적 안내 보상이 엔드투엔드 휴머노이드 제어에서 효과적임을 입증했으며, 복잡한 동적 작업에 이식 가능한 강화 학습 패러다임을 제공합니다. 오픈 소스 코드는 GitHub 저장소에 공개되었습니다.
