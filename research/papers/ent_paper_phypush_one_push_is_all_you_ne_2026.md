---
$id: ent_paper_phypush_one_push_is_all_you_ne_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation with Physics-Guided Transformers'
  zh: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation with Physics-Guided Transformers'
  ko: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation with Physics-Guided Transformers'
summary:
  en: 'arXiv:2605.26284v2 Announce Type: replace Abstract: Accurately estimating object mass and friction is fundamental to
    reliable robotic manipulation. While interactive perception is powerful, most approaches rely on specialized hardware
    like force/torque sensors, limiting scalability. This paper introduces PhyPush, a physics-guided Transformer that estimates
    an object''s mass and friction coefficient using only end-effector velocity from a single push, data readily available
    on standard robotic arms. By incorporating Newton''s second law and the Coulomb friction model through a physics-guided
    loss, the model improves physical consistency and generalizes to unseen objects and surfaces. Across diverse setups, PhyPush
    consistently achieves highly accurate estimations in challenging out-of-domain conditions. In simulation, it reduces error
    by over 10% compared to a baseline with privileged force data, while in real-world experiments, it successfully zero-shot
    transfers from simulation to outperform a purely data-driven baseline.'
  zh: PhyPush 是一种物理引导的 Transformer 模型，由研究团队提出，仅利用标准机械臂末端执行器在一次推动中的速度数据，即可估计物体的质量和摩擦系数。其核心贡献在于通过物理引导损失函数融入牛顿第二定律和库仑摩擦模型，提升了物理一致性，并实现了对未见物体和表面的泛化。
  ko: 'arXiv:2605.26284v2 Announce Type: replace Abstract: Accurately estimating object mass and friction is fundamental to
    reliable robotic manipulation. While interactive perception is powerful, most approaches rely on specialized hardware
    like force/torque sensors, limiting scalability. This paper introduces PhyPush, a physics-guided Transformer that estimates
    an object''s mass and friction coefficient using only end-effector velocity from a single push, data readily available
    on standard robotic arms. By incorporating Newton''s second law and the Coulomb friction model through a physics-guided
    loss, the model improves physical consistency and generalizes to unseen objects and surfaces. Across diverse setups, PhyPush
    consistently achieves highly accurate estimations in challenging out-of-domain conditions. In simulation, it reduces error
    by over 10% compared to a baseline with privileged force data, while in real-world experiments, it successfully zero-shot
    transfers from simulation to outperform a purely data-driven baseline.'
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
- phypush
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.26284v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (833 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'PhyPush: One Push is All You Need for Sensorless Physical Property Estimation with Physics-Guided Transformers (arXiv)'
  url: https://arxiv.org/abs/2605.26284
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
PhyPush 解决了机器人操作中依赖力/力矩传感器进行质量与摩擦估计的局限性。该模型仅需单次推动的末端速度作为输入，通过物理引导损失函数将牛顿第二定律和库仑摩擦模型嵌入 Transformer 架构，从而增强估计的物理合理性。在仿真实验中，PhyPush 相比使用特权力数据的基线方法误差降低超过 10%；在真实世界实验中，它成功实现了从仿真到现实的零样本迁移，性能优于纯数据驱动基线。

## 核心内容
### 方法
- **输入**：仅使用标准机械臂末端执行器在一次推动中的速度数据，无需力/力矩传感器。
- **架构**：基于 Transformer 模型，通过物理引导损失函数（physics-guided loss）将牛顿第二定律和库仑摩擦模型显式嵌入训练过程。
- **物理约束**：损失函数强制模型输出满足物理定律的质量和摩擦系数估计，提升物理一致性和泛化能力。

### 实验设置
- **仿真环境**：使用多样化物体和表面进行训练与测试，基线方法使用特权力数据（即直接访问真实力信息）。
- **真实世界实验**：将仿真训练的模型直接迁移到真实机器人平台，无需额外微调（零样本迁移）。
- **对比基线**：纯数据驱动模型（无物理引导）和基于特权力数据的模型。

### 关键结果
- **仿真性能**：PhyPush 相比使用特权力数据的基线方法，误差降低超过 10%。
- **真实世界性能**：零样本迁移后，PhyPush 在真实实验中优于纯数据驱动基线，验证了物理引导的有效性。
- **泛化能力**：模型成功泛化到训练中未见的物体和表面，在挑战性的域外条件下保持高精度。

### 结论
PhyPush 通过物理引导的 Transformer 架构，仅利用单次推动的末端速度数据，实现了无需传感器的质量与摩擦估计。其物理一致性损失函数显著提升了泛化能力，并在仿真和真实实验中均优于基线方法，为可扩展的机器人操作提供了新思路。

## Overview
Accurately estimating object mass and friction is fundamental to reliable robotic manipulation. While interactive perception is powerful, most approaches rely on specialized hardware like force/torque sensors, limiting scalability. This paper introduces PhyPush, a physics-guided Transformer that estimates an object's mass and friction coefficient using only end-effector velocity from a single push, data readily available on standard robotic arms. By incorporating Newton's second law and the Coulomb friction model through a physics-guided loss, the model improves physical consistency and generalizes to unseen objects and surfaces. Across diverse setups, PhyPush consistently achieves highly accurate estimations in challenging out-of-domain conditions. In simulation, it reduces error by over 10% compared to a baseline with privileged force data, while in real-world experiments, it successfully zero-shot transfers from simulation to outperform a purely data-driven baseline.

## 参考
- http://arxiv.org/abs/2605.26284v2

## 개요
PhyPush는 로봇 조작에서 힘/토크 센서에 의존하는 질량 및 마찰 추정의 한계를 해결합니다. 이 모델은 단 한 번의 밀기에서 얻은 엔드 이펙터 속도만을 입력으로 사용하며, 물리 기반 손실 함수를 통해 뉴턴 제2법칙과 쿨롱 마찰 모델을 Transformer 아키텍처에 내장하여 추정의 물리적 타당성을 강화합니다. 시뮬레이션 실험에서 PhyPush는 특권 데이터를 사용하는 기준 방법보다 오류를 10% 이상 줄였으며, 실제 세계 실험에서는 시뮬레이션에서 실제로의 제로샷 전이를 성공적으로 달성하여 순수 데이터 기반 기준선보다 우수한 성능을 보였습니다.

## 핵심 내용
### 방법
- **입력**: 표준 로봇 팔 엔드 이펙터의 한 번의 밀기 속도 데이터만 사용하며, 힘/토크 센서가 필요 없습니다.
- **아키텍처**: Transformer 모델 기반으로, 물리 기반 손실 함수(physics-guided loss)를 통해 뉴턴 제2법칙과 쿨롱 마찰 모델을 훈련 과정에 명시적으로 내장합니다.
- **물리적 제약**: 손실 함수는 모델 출력이 물리 법칙을 충족하는 질량 및 마찰 계수 추정을 강제하여 물리적 일관성과 일반화 능력을 향상시킵니다.

### 실험 설정
- **시뮬레이션 환경**: 다양한 객체와 표면을 사용하여 훈련 및 테스트를 수행하며, 기준 방법은 특권 데이터(즉, 실제 힘 정보에 직접 접근)를 사용합니다.
- **실제 세계 실험**: 시뮬레이션에서 훈련된 모델을 추가 미세 조정 없이 실제 로봇 플랫폼에 직접 전이합니다(제로샷 전이).
- **비교 기준선**: 순수 데이터 기반 모델(물리 기반 없음) 및 특권 데이터 기반 모델.

### 주요 결과
- **시뮬레이션 성능**: PhyPush는 특권 데이터를 사용하는 기준 방법보다 오류를 10% 이상 줄였습니다.
- **실제 세계 성능**: 제로샷 전이 후, PhyPush는 실제 실험에서 순수 데이터 기반 기준선보다 우수하여 물리 기반 유도의 효과를 검증했습니다.
- **일반화 능력**: 모델은 훈련에서 보지 못한 객체와 표면으로 성공적으로 일반화되었으며, 도전적인 도메인 외 조건에서도 높은 정확도를 유지했습니다.

### 결론
PhyPush는 물리 기반 Transformer 아키텍처를 통해 단 한 번의 밀기에서 얻은 엔드 이펙터 속도 데이터만으로 센서 없는 질량 및 마찰 추정을 구현합니다. 물리적 일관성 손실 함수는 일반화 능력을 크게 향상시켰으며, 시뮬레이션 및 실제 실험 모두에서 기준 방법보다 우수하여 확장 가능한 로봇 조작에 새로운 방향을 제시합니다.
