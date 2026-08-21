---
$id: ent_paper_coral_auv_cfd_oriented_reinfor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
  zh: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
  ko: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles'
summary:
  en: 'arXiv:2607.09557v1 Announce Type: new Abstract: Fine grain control and positioning of autonomous underwater vehicles
    (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor
    intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning
    (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR).
    However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics
    are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD)
    provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its
    computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of
    a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy
    on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31%
    lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with
    19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping
    design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller
    that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive
    testing of the policies'' capabilities.'
  zh: CORAL-AUV 提出了一种结合计算流体动力学（CFD）与强化学习（RL）的方法，用于自主水下航行器（AUV）的精细控制。该研究首次在六自由度AUV上成功部署零样本RL策略，通过训练基于CFD数据的替代阻力模型（SDMs）实现快速推理。实验表明，相比传统简化物理控制器，该方法能耗降低31%，航点间穿越速度提升11%，误差减少19%。
  ko: 'arXiv:2607.09557v1 Announce Type: new Abstract: Fine grain control and positioning of autonomous underwater vehicles
    (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor
    intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning
    (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR).
    However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics
    are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD)
    provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its
    computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of
    a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy
    on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31%
    lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with
    19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping
    design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller
    that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive
    testing of the policies'' capabilities.'
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
- robotics
- coral_auv
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09557v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (826 chars, DeepSeek). [2026-08-21] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles (arXiv)'
  url: https://arxiv.org/abs/2607.09557
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述

CORAL-AUV 提出一种面向自主水下航行器（AUV）的 CFD 导向强化学习框架，核心是用 OpenFOAM 稳态 CFD 数据构建系统拖曳模型（SDM），替代传统惯性箱或 System ID 拖曳模型，以缩小仿真到现实的差距。作者在 IsaacSim 中训练 RL 策略，并在 Lameshur Bay 与 Yawzi Reef 两处野外环境完成零样本部署验证，证明 SDM 在领域随机化与真实海况下具有更优的迁移鲁棒性。

## 它改变了什么

水下航行器 RL 策略的 sim-to-real 迁移长期受制于水动力建模精度：传统做法要么用惯性箱（inertia box）这类粗粒度拖曳模型，要么用 System ID 拟合对角阻尼矩阵，两者都忽略了流体动力学中关键的交叉耦合效应。本文真正改变的是将 CFD 仿真数据作为拖曳模型的“唯一事实来源”，而不是把 CFD 当作离线验证工具或奖励整形参考——这使训练环境中的动力学偏差从“经验猜测”变为“物理可解释的系统辨识”。

这一转变的深层意义在于：作者用实验证明，拖曳系数的数值与比值对学习结果高度敏感，而 SDM 中嵌入的交叉耦合项是降低 sim-to-real 差距的主因（Figure A.2）。这直接挑战了领域随机化（DR）作为通用迁移手段的有效性——在尾部加载 2 lbs 配重的实验中，仅 CFD 策略成功迁移，说明 DR 无法补偿模型结构错误，只能缓解参数扰动。

## 方法拆解

### 拖曳模型构建
- **惯性箱模型**：以体积和 COB-COM 偏移为中心进行随机化，默认参数见表 1（质量 25.90 kg，体积 0.025977 m³，COB-COM 偏移 [0.00, 0.00, 0.01] m）。
- **System ID 模型**：具有与惯性箱相同的对角结构，但系数通过系统辨识获得。
- **SDM（基于 CFD）**：使用 OpenFOAM 稳态 CFD 数据集构建，显式包含交叉耦合项，这是与前述两种模型的本质区别。

### 奖励整形与迭代流程
- 三组配置从保守到激进迭代：
  - \(\mathcal{C}_{conservative} = \{\lambda_p=0.20, \lambda_q=0.50, \lambda_v=0.05, \lambda_a=0.20\}\)
  - \(\mathcal{C}_{balanced} = \{\lambda_p=0.40, \lambda_q=0.90, \lambda_v=0.00, \lambda_a=0.20\}\)
  - \(\mathcal{C}_{aggressive} = \{\lambda_p=0.20, \lambda_q=1.0, \lambda_v=0.00, \lambda_a=0.08\}\)
- 迭代流程：从 Conservative 开始，基于零样本部署性能逐步调整至 Balanced 和 Aggressive。

### 训练与部署
- 仿真平台：IsaacSim 用于 RL 训练与奖励曲线记录。
- 野外部署：Lameshur Bay（相对平静）与 Yawzi Reef（暴露海域，风速 10-20 mph）。
- 任务轨迹：Yawzi Reef 为箱形轨迹，每边长 4 m，每个角暂停 4 秒，深度约 7 m；Lameshur Bay 为 U 形轨迹，三段各 1.7 m。
- 领域随机化实验：车辆尾部额外加载 2 lbs（两个 1 lb 潜水配重，分别置于尾部两侧）。

## 关键创新

1. **CFD 数据作为拖曳模型的直接构建来源**：不同于将 CFD 用于验证或奖励设计，本文用 OpenFOAM 稳态数据构建 SDM 并嵌入 RL 训练管线，使动力学模型具有物理一致性。这是对“仿真环境动力学精度”这一根本问题的正面回应。

2. **交叉耦合项的显式建模**：作者通过消融对比（惯性箱 vs System ID vs SDM）证明，交叉耦合是降低 sim-to-real 差距的关键因素。这一发现为后续水下 RL 研究提供了明确的建模方向——忽略耦合项的对角模型即使参数精确也无法替代结构正确的模型。

3. **奖励整形迭代与零样本部署的闭环**：从 Conservative 到 Aggressive 的迭代不是离线调参，而是基于真实部署性能的在线调整。这种“训练-部署-再训练”的流程设计，使奖励系数选择从启发式变为数据驱动。

## 实验与结果

| 实验设置 | 关键结果 |
|---------|---------|
| 惯性箱模型 + DR | 无法学习达到相似奖励水平的行为 |
| System ID 模型 | 与惯性箱具有相同对角结构，但学习结果差异显著 |
| SDM（CFD 导向） | 在尾部加载 2 lbs 时，仅 CFD 策略成功迁移（Figure 6） |
| Yawzi Reef 野外部署 | 暴露海域（风速 10-20 mph），7 m 深度完成箱形轨迹 |
| Lameshur Bay 野外部署 | 相对平静海域，U 形轨迹三段各 1.7 m |

结果含义：SDM 的零样本迁移成功并非源于更精确的参数拟合，而是源于模型结构对真实水动力耦合的捕捉。System ID 与惯性箱的对比进一步说明，即使系数经过辨识，对角结构本身限制了策略在扰动下的鲁棒性。论文未明确给出各模型的具体成功率数字。

## 边界与局限

- 作者未对拖曳系数与学习敏感性的关系进行完整研究，仅指出学习对系数值和比值高度敏感，列为未来工作。
- 惯性箱拖曳模型在领域随机化下无法学习达到相似奖励水平的行为，说明 DR 的补偿能力存在上限，但论文未明确该上限的定量边界。
- 野外实验仅在两种海域环境验证，未覆盖强流、深水或复杂地形场景；论文未明确多机协同或长时程任务的表现。
- 论文未明确给出各拖曳模型在相同训练预算下的计算开销对比，CFD 数据集的生成成本与离线预处理时间未提及。

## 工程启示

- 复现时优先核对拖曳模型的**结构**而非仅系数：确保 SDM 包含交叉耦合项，否则即使参数与 CFD 完全一致，迁移性能也会显著退化。
- 领域随机化不能替代模型精度：在尾部加载 2 lbs 的实验中，DR 未能挽救惯性箱模型，说明 DR 适合处理参数扰动，但无法修正模型结构错误。建议在训练前先做模型结构消融。
- 奖励整形迭代务必以零样本部署性能为准，而非仿真奖励曲线：从 Conservative 到 Aggressive 的调整应基于真实环境反馈，否则容易过拟合仿真动力学。
- 野外部署前先确认环境条件与训练分布的匹配度：Yawzi Reef 的风速（10-20 mph）与波浪条件显著影响迁移，若目标海域更恶劣，需重新评估 SDM 的适用性。
- 最易踩坑处：COB-COM 偏移（[0.00, 0.00, 0.01] m）与体积（0.025977 m³）的随机化范围设置不当会导致训练与部署动力学失配，建议以 CFD 数据集的参数中心为基准，而非均匀采样。

## 参考
- http://arxiv.org/abs/2607.09557v1

## 개요
전통적인 AUV 제어 방법은 노동 집약적이며 구성이나 환경 변화에 대한 견고성이 부족합니다. 반면 강화 학습은 도메인 무작위화(DR)를 통해 배포 매개변수 변화를 처리할 수 있지만, 시뮬레이션이 실제 물리(특히 항력 모델)를 모델링하는 능력에 제한을 받습니다. 계산 유체 역학은 고충실도 항력 모델을 제공할 수 있지만, 계산 비용 때문에 RL 프레임워크에 직접 통합하기 어렵습니다. 이를 위해 본 논문은 CFD 데이터 기반의 대체 항력 모델(SDMs)을 훈련하여 RL 파이프라인에서 빠른 추론을 가능하게 하는 방법을 제안합니다. 이 제로샷 정책은 6자유도 AUV에서 성공적으로 배포되었으며, 통제된 수조와 현장 환경 모두에서 검증되어 더 우수한 제로샷 전이 예측 능력과 보상 함수 설계에 대한 견고성을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **핵심 아이디어**: 계산 유체 역학(CFD)을 활용해 고충실도 항력 데이터를 생성하고, 대체 항력 모델(SDMs)을 빠른 추론 에이전트로 훈련하여 기존의 단순화된 물리 모델을 대체해 강화 학습(RL) 파이프라인에 통합합니다.
- **정책 훈련**: 6자유도(6-DOF) AUV에서 SDMs 기반 정책 훈련을 수행하여, 실제 환경에서의 미세 조정 없이 제로샷(zero-shot) 배포를 구현합니다.

### 실험 설정
- **비교 기준선**: 단순화된 물리 모델 기반 제어기를 비교 기준으로 사용합니다.
- **평가 환경**: 통제된 수조(controlled tank) 및 현장(field) 환경에서 웨이포인트 내비게이션 작업을 포함한 광범위한 테스트를 수행합니다.
- **도메인 무작위화(DR) 테스트**: 매개변수 교란 조건에서 정책 전이 능력을 평가합니다.

### 주요 결과
- **성능 향상**: 단순화된 물리 제어기와 비교해 SDM 기반 RL 제어기는 웨이포인트 간 이동 시 에너지 소비를 31% 절감하고, 속도를 11% 향상시키며, 경로 오차를 19% 줄였습니다.
- **제로샷 전이**: SDM 정책은 제로샷 전이 효과를 더 정확하게 예측하며, 보상 함수 설계(reward shaping)에 대한 견고성이 더 강합니다.
- **도메인 무작위화 성능**: 매개변수 교란 작업에서 CFD 기반 정책은 유일하게 성공적으로 전이된 제어기였으며, 다른 제어기는 모두 실패했습니다.

### 결론
본 논문은 CFD 데이터의 대체 모델을 훈련함으로써 RL 프레임워크에서 고충실도 항력 물리를 효율적으로 활용할 수 있음을 처음으로 입증했으며, AUV 제어기의 에너지 효율, 속도 및 정밀도를 크게 향상시키고 배포 조건 변화에 대한 견고성을 강화했습니다.
