---
$id: ent_paper_ze_3d_diffusion_policy_generaliza_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'
  zh: DP3
  ko: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations'
summary:
  en: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
  zh: 3D Diffusion Policy (DP3) 是2024年由上海期智研究院、上海交通大学、清华大学、IIIS、上海人工智能实验室联合提出的通用化视觉-语言-动作模型，用于机器人操作。其核心贡献在于将紧凑的3D视觉表示（基于稀疏点云的点编码器）融入扩散策略，在仅需10次演示的72项仿真任务中实现24.2%的相对性能提升，并在真实机器人任务中以40次演示达到85%的成功率。
  ko: '3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations (DP3), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by Shanghai Qi Zhi Institute, Shanghai Jiao Tong University,
    Tsinghua University, IIIS, Shanghai AI Lab, and published at Robotics - Science and Systems 2024.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dp3
- generalist_policy
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.03954v7. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: DP3 source
  url: https://doi.org/10.15607/RSS.2024.XX.067
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
DP3通过将3D视觉表示与扩散策略结合，解决了模仿学习中复杂技能泛化性差且依赖大量演示数据的问题。该方法从稀疏点云中提取紧凑的3D特征，利用高效点编码器实现轻量化表示。在72项仿真任务中，DP3仅需10次演示即可完成多数任务，性能超越基线方法24.2%。在4项真实机器人任务中，仅用40次演示即达到85%的成功率，并在空间、视角、外观和实例维度展现出卓越泛化能力。值得注意的是，DP3在真实实验中几乎不违反安全约束，而基线方法频繁需要人工干预。

## 核心内容
### 方法架构
- **核心设计**：将3D视觉表示（基于稀疏点云的点编码器）与扩散策略（条件动作生成模型）结合，形成紧凑的视觉-动作映射。
- **表示提取**：使用高效点编码器从稀疏点云中提取紧凑3D特征，避免传统2D表示对视角和光照的敏感性。

### 实验设置
- **仿真任务**：覆盖72项多样化操作任务（如抓取、组装等），每项任务仅提供10次人类演示。
- **真实任务**：4项真实机器人操作任务（如拾取、放置等），每项任务提供40次演示。
- **基线对比**：与基于2D视觉的扩散策略、行为克隆等方法对比。

### 关键结果
- **仿真性能**：DP3在72项任务中成功处理多数任务，相对基线方法提升24.2%。
- **真实性能**：4项任务平均成功率85%，显著优于基线方法（如2D扩散策略成功率约60%）。
- **泛化能力**：在空间位置偏移、视角变化、物体外观替换、实例类型改变等场景中保持稳定性能。
- **安全表现**：真实实验中DP3几乎不违反安全约束（如碰撞、掉落），而基线方法频繁触发安全干预。

### 结论
3D视觉表示对真实世界机器人学习至关重要，DP3通过紧凑点云表示实现了高效、安全且泛化的操作策略。代码、数据和视频已开源。

## Overview
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizablely usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## Overview
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizably usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## Content
Imitation learning provides an efficient way to teach robots dexterous skills; however, learning complex skills robustly and generalizably usually consumes large amounts of human demonstrations. To tackle this challenging problem, we present 3D Diffusion Policy (DP3), a novel visual imitation learning approach that incorporates the power of 3D visual representations into diffusion policies, a class of conditional action generative models. The core design of DP3 is the utilization of a compact 3D visual representation, extracted from sparse point clouds with an efficient point encoder. In our experiments involving 72 simulation tasks, DP3 successfully handles most tasks with just 10 demonstrations and surpasses baselines with a 24.2% relative improvement. In 4 real robot tasks, DP3 demonstrates precise control with a high success rate of 85%, given only 40 demonstrations of each task, and shows excellent generalization abilities in diverse aspects, including space, viewpoint, appearance, and instance. Interestingly, in real robot experiments, DP3 rarely violates safety requirements, in contrast to baseline methods which frequently do, necessitating human intervention. Our extensive evaluation highlights the critical importance of 3D representations in real-world robot learning. Videos, code, and data are available on https://3d-diffusion-policy.github.io .

## 개요
모방 학습은 로봇에게 정교한 기술을 가르치는 효율적인 방법을 제공하지만, 복잡한 기술을 강건하고 일반화 가능하게 학습하려면 일반적으로 많은 양의 인간 시연이 필요합니다. 이 어려운 문제를 해결하기 위해, 우리는 3D 시각적 표현의 힘을 조건부 행동 생성 모델의 한 종류인 확산 정책에 통합한 새로운 시각적 모방 학습 접근법인 3D Diffusion Policy (DP3)를 제시합니다. DP3의 핵심 설계는 효율적인 포인트 인코더를 사용하여 희소 포인트 클라우드에서 추출된 컴팩트한 3D 시각적 표현을 활용하는 것입니다. 72개의 시뮬레이션 작업을 포함한 실험에서 DP3는 단 10개의 시연만으로 대부분의 작업을 성공적으로 처리했으며, 기준선 대비 24.2%의 상대적 개선을 달성했습니다. 4개의 실제 로봇 작업에서 DP3는 각 작업당 40개의 시연만으로 85%의 높은 성공률로 정밀한 제어를 보여주었으며, 공간, 시점, 외관, 인스턴스 등 다양한 측면에서 뛰어난 일반화 능력을 입증했습니다. 흥미롭게도, 실제 로봇 실험에서 DP3는 안전 요구 사항을 거의 위반하지 않은 반면, 기준선 방법은 자주 위반하여 인간의 개입이 필요했습니다. 우리의 광범위한 평가는 실제 로봇 학습에서 3D 표현의 중요한 중요성을 강조합니다. 비디오, 코드 및 데이터는 https://3d-diffusion-policy.github.io 에서 확인할 수 있습니다.

## 핵심 내용
모방 학습은 로봇에게 정교한 기술을 가르치는 효율적인 방법을 제공하지만, 복잡한 기술을 강건하고 일반화 가능하게 학습하려면 일반적으로 많은 양의 인간 시연이 필요합니다. 이 어려운 문제를 해결하기 위해, 우리는 3D 시각적 표현의 힘을 조건부 행동 생성 모델의 한 종류인 확산 정책에 통합한 새로운 시각적 모방 학습 접근법인 3D Diffusion Policy (DP3)를 제시합니다. DP3의 핵심 설계는 효율적인 포인트 인코더를 사용하여 희소 포인트 클라우드에서 추출된 컴팩트한 3D 시각적 표현을 활용하는 것입니다. 72개의 시뮬레이션 작업을 포함한 실험에서 DP3는 단 10개의 시연만으로 대부분의 작업을 성공적으로 처리했으며, 기준선 대비 24.2%의 상대적 개선을 달성했습니다. 4개의 실제 로봇 작업에서 DP3는 각 작업당 40개의 시연만으로 85%의 높은 성공률로 정밀한 제어를 보여주었으며, 공간, 시점, 외관, 인스턴스 등 다양한 측면에서 뛰어난 일반화 능력을 입증했습니다. 흥미롭게도, 실제 로봇 실험에서 DP3는 안전 요구 사항을 거의 위반하지 않은 반면, 기준선 방법은 자주 위반하여 인간의 개입이 필요했습니다. 우리의 광범위한 평가는 실제 로봇 학습에서 3D 표현의 중요한 중요성을 강조합니다. 비디오, 코드 및 데이터는 https://3d-diffusion-policy.github.io 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2403.03954v7
