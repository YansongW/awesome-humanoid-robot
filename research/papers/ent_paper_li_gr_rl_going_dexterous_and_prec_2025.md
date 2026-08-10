---
$id: ent_paper_li_gr_rl_going_dexterous_and_prec_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation'
  zh: GR-RL
  ko: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation'
summary:
  en: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
  zh: GR-RL 是字节跳动 Seed 团队于 2025 年提出的机器人学习框架，旨在将通用视觉-语言-动作（VLA）策略转化为擅长长时程灵巧操作的专业化策略。其核心贡献在于通过多阶段训练流水线（过滤、增强、强化学习）处理人类演示中的噪声与次优性，首次实现自主穿鞋带任务（成功率
    83.3%），该任务要求毫米级精度与长时程推理。
  ko: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (GR-RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by ByteDance Seed.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_rl
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01801v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (796 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'GR-RL: Going Dexterous and Precise for Long-Horizon Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.01801
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-RL source
  url: https://doi.org/10.48550/arXiv.2512.01801
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有 VLA 策略通常假设人类演示具有最优性，但 GR-RL 指出在高度灵巧与精密操作任务中，人类演示存在噪声与次优性。为此，GR-RL 提出三阶段流水线：首先利用离线强化学习中的 Q 值作为鲁棒的进度函数，过滤演示轨迹中贡献正向的转换；其次引入形态对称增强技术提升泛化能力；最后通过在线强化学习训练隐空间噪声预测器，使策略与部署行为对齐。该框架在穿鞋带任务中达到 83.3% 成功率，展现了长时程推理、毫米级精度与柔性物体交互的协同能力。

## 核心内容
### 方法架构
GR-RL 的核心创新在于多阶段训练流水线，将通用 VLA 策略转化为灵巧操作专家：
- **阶段一：基于进度的轨迹过滤**  
  通过离线强化学习（稀疏奖励）学习视觉-语言条件任务进度函数，利用 Q 值评估每个转换对进度的贡献，仅保留正向贡献的演示片段。
- **阶段二：形态对称增强**  
  引入数据增强技术，利用机器人操作的对称性（如左右手互换）生成额外训练样本，显著提升策略的泛化能力与性能。
- **阶段三：在线强化学习对齐**  
  训练隐空间噪声预测器，在部署阶段实时修正策略动作，实现高精度控制。该模块通过在线 RL 优化策略与真实环境的交互行为。

### 实验设置与关键结果
- **任务**：自主穿鞋带（将鞋带穿过多个鞋眼），要求长时程推理（约 20 步）、毫米级精度及柔性物体交互。
- **成功率**：83.3%（首次实现学习策略自主完成该任务）。
- **对比基线**：未使用 GR-RL 流水线的原始 VLA 策略无法完成该任务，验证了过滤、增强与在线 RL 各阶段的必要性。

### 结论
GR-RL 证明了通过多阶段强化学习优化人类演示，通用机器人基础模型可转化为可靠的真实世界专家。该框架为长时程灵巧操作任务（如穿针引线、精密装配）提供了可扩展的解决方案。

## Overview
We present GR-RL, a robotic learning framework that turns a generalist vision-language-action (VLA) policy into a highly capable specialist for long-horizon dexterous manipulation. Assuming the optimality of human demonstrations is core to existing VLA policies. However, we claim that in highly dexterous and precise manipulation tasks, human demonstrations are noisy and suboptimal. GR-RL proposes a multi-stage training pipeline that filters, augments, and reinforces the demonstrations by reinforcement learning. First, GR-RL learns a vision-language-conditioned task progress, filters the demonstration trajectories, and only keeps the transitions that contribute positively to the progress. Specifically, we show that by directly applying offline RL with sparse reward, the resulting $Q$-values can be treated as a robust progress function. Next, we introduce morphological symmetry augmentation that greatly improves the generalization and performance of GR-RL. Lastly, to better align the VLA policy with its deployment behaviors for high-precision control, we perform online RL by learning a latent space noise predictor. With this pipeline, GR-RL is, to our knowledge, the first learning-based policy that can autonomously lace up a shoe by threading shoelaces through multiple eyelets with an 83.3% success rate, a task requiring long-horizon reasoning, millimeter-level precision, and compliant soft-body interaction. We hope GR-RL provides a step toward enabling generalist robot foundation models to specialize into reliable real-world experts.

## 参考
- http://arxiv.org/abs/2512.01801v3

## 개요
기존 VLA 정책은 일반적으로 인간 시연이 최적성을 가진다고 가정하지만, GR-RL은 고도로 정밀하고 섬세한 조작 작업에서 인간 시연에 노이즈와 차선성이 존재한다고 지적한다. 이를 위해 GR-RL은 3단계 파이프라인을 제안한다: 먼저 오프라인 강화 학습의 Q-값을 강건한 진행 함수로 활용하여 시연 궤적에서 긍정적 기여를 하는 전환을 필터링하고, 다음으로 형태 대칭 증강 기법을 도입하여 일반화 능력을 향상시키며, 마지막으로 온라인 강화 학습을 통해 잠재 공간 노이즈 예측기를 훈련하여 정책과 배포 행동을 정렬한다. 이 프레임워크는 신발 끈 묶기 작업에서 83.3%의 성공률을 달성하며, 장기 추론, 밀리미터급 정밀도 및 유연한 물체 상호작용의 협력 능력을 보여준다.

## 핵심 내용
### 방법 아키텍처
GR-RL의 핵심 혁신은 다단계 훈련 파이프라인으로, 일반 VLA 정책을 정밀 조작 전문가로 변환한다:
- **1단계: 진행 기반 궤적 필터링**  
  오프라인 강화 학습(희소 보상)을 통해 시각-언어 조건 작업 진행 함수를 학습하고, Q-값을 활용하여 각 전환이 진행에 기여하는 바를 평가하며, 긍정적 기여를 하는 시연 세그먼트만 유지한다.
- **2단계: 형태 대칭 증강**  
  데이터 증강 기법을 도입하여 로봇 조작의 대칭성(예: 좌우 손 교환)을 활용해 추가 훈련 샘플을 생성하고, 정책의 일반화 능력과 성능을 크게 향상시킨다.
- **3단계: 온라인 강화 학습 정렬**  
  잠재 공간 노이즈 예측기를 훈련하여 배포 단계에서 정책 동작을 실시간으로 수정하고, 고정밀 제어를 구현한다. 이 모듈은 온라인 RL을 통해 정책과 실제 환경 간의 상호작용 행동을 최적화한다.

### 실험 설정 및 주요 결과
- **작업**: 자율 신발 끈 묶기(신발 끈을 여러 신발 구멍에 통과시키기)로, 장기 추론(약 20단계), 밀리미터급 정밀도 및 유연한 물체 상호작용이 요구된다.
- **성공률**: 83.3%(학습 정책이 해당 작업을 자율적으로 완료한 최초 사례).
- **비교 기준선**: GR-RL 파이프라인을 사용하지 않은 원래 VLA 정책은 해당 작업을 완료할 수 없어, 필터링, 증강 및 온라인 RL 각 단계의 필요성을 검증한다.

### 결론
GR-RL은 다단계 강화 학습을 통해 인간 시연을 최적화함으로써, 일반 로봇 기반 모델이 신뢰할 수 있는 실제 세계 전문가로 변환될 수 있음을 입증한다. 이 프레임워크는 장기 정밀 조작 작업(예: 바늘 꿰기, 정밀 조립)에 확장 가능한 솔루션을 제공한다.
