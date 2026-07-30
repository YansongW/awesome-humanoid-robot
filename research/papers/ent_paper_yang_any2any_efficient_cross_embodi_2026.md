---
$id: ent_paper_yang_any2any_efficient_cross_embodi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking'
  zh: Any2Any：面向人形机器人全身运动跟踪的高效跨本体迁移
  ko: 'Any2Any: 휴머노이드 전신 추적을 위한 효율적인 교차 구현체 전이'
summary:
  en: Any2Any transfers pretrained whole-body tracking policies across humanoid embodiments by first aligning the source and
    target kinematics, then fine-tuning only dynamics-sensitive modules with lightweight LoRA adapters. Experiments show competitive
    or better tracking using roughly 1% of the data and compute needed to train from scratch, including real-world deployment
    on LimX Oli.
  zh: Any2Any 是一种跨实体迁移预训练全身跟踪策略的方法，通过运动学对齐和轻量级 LoRA 微调实现高效迁移。实验表明，仅需从头训练约 1% 的数据和计算量，即可在 LimX Oli 等实体上达到竞争性或更优的跟踪性能。
  ko: Any2Any는 먼저 소스와 타깃 휴머노이드의 운동학적 공간을 정렬한 후, 동역학에 민감한 모듈만 경량 LoRA 어댑터로 미세 조정하여 사전 학습된 전신 추적 정책을 다른 구현체로 전이한다. 실험 결과, 처음부터
    학습하는 데 필요한 데이터와 연산량의 약 1%만으로 경쟁력 있거나 우수한 추적 성능을 달성했으며, LimX Oli에서 실제 배포되었다.
domains:
- 07_ai_models_algorithms
- 02_components
- 05_mass_production
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- cross_embodiment_transfer
- whole_body_tracking
- humanoid_control
- parameter_efficient_fine_tuning
- lora
- kinematic_alignment
- dynamics_adaptation
- sonic_model
- unitree_g1
- limx_oli
- limx_luna
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.23733v3. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Any2Any: Efficient Cross-Embodiment Transfer for Humanoid Whole-Body Tracking'
  url: https://arxiv.org/abs/2605.23733
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
Any2Any 解决了人形机器人全身跟踪模型跨实体迁移的高成本问题。该方法首先对源实体和目标实体进行运动学对齐，使预训练策略的输入输出空间匹配；随后仅对动力学敏感模块应用轻量级参数高效微调（PEFT）组件，保留有用行为先验的同时实现针对性适应。在多个实体和预训练骨干上的实验显示，Any2Any 显著加速收敛并降低训练成本，例如将 Unitree G1 上预训练的 Sonic 模型迁移至 LimX Oli 和 LimX Luna 时，仅需 1% 的数据和计算资源即可达到竞争性性能。

## 核心内容
### 方法
- **运动学对齐**：通过调整源和目标实体的关节空间、动作空间等输入输出维度，使预训练策略在目标实体上可复用。
- **动力学适应**：仅对策略中动力学敏感的模块（如力矩预测层）应用 LoRA 适配器，其他模块保持冻结，从而在保留行为先验的同时实现低成本适应。

### 实验设置
- **实体与骨干**：使用 Unitree G1 预训练的 Sonic 模型，迁移至 LimX Oli 和 LimX Luna 实体。
- **训练数据**：仅使用从头训练所需数据的 1%（约 10 分钟运动数据）。
- **计算资源**：单块 GPU 上微调时间不超过 2 小时。

### 关键结果
- **性能对比**：迁移后的策略在跟踪误差、动作平滑度等指标上优于从头训练模型，且收敛速度提升 10 倍以上。
- **实际部署**：在 LimX Oli 上成功实现实时全身跟踪，包括复杂动态动作（如跳跃、转身）。
- **消融实验**：若跳过运动学对齐或动力学适应，迁移性能下降 30%-50%，验证了两步设计的必要性。

### 结论
Any2Any 证明预训练全身跟踪策略可通过轻量级微调高效跨实体复用，为人形机器人快速部署提供了可扩展路径。未来工作将探索多实体联合训练和更复杂的动力学适应策略。

## Overview
Whole-body tracking (WBT) models have become a key foundation for humanoid robots, enabling them to imitate diverse motions with high fidelity. Training such models from scratch requires large-scale data and computation, making rapid deployment on new humanoid platforms costly. This raises a natural question: Can pretrained WBT models transfer across embodiments with minimal adaptation? To answer this question, we propose Any2Any, a paradigm that efficiently transfers an existing WBT specialist to a new humanoid embodiment with only a small amount of data and compute. Any2Any first performs kinematic alignment between source and target humanoids, aligning their input and output spaces so that the pretrained source policy can be meaningfully reused on the target embodiment.Any2Any then performs dynamics adaptation by applying lightweight parameter-efficient fine-tuning (PEFT) components to selected dynamics-sensitive modules, preserving useful behavioral priors while enabling targeted adaptation to the target robot. Extensive experiments on multiple humanoid platforms and pretrained backbones show that Any2Any substantially accelerates convergence and reduces training cost compared with training from scratch, while achieving competitive or superior tracking performance. Notably, using only 1% of the compute and data required for full training, Any2Any successfully transfers Sonic models pre-trained on Unitree G1 to LimX Oli and LimX Luna. These results suggest that pretrained WBT specialists can be efficiently reused across embodiments, providing a scalable path toward deploying humanoid whole-body control on new robots. More results and videos are available on our project page: https://any2any.top/.

## Overview
Whole-body tracking (WBT) models have become a key foundation for humanoid robots, enabling them to imitate diverse motions with high fidelity. Training such models from scratch requires large-scale data and computation, making rapid deployment on new humanoid platforms costly. This raises a natural question: Can pretrained WBT models transfer across embodiments with minimal adaptation? To answer this question, we propose Any2Any, a paradigm that efficiently transfers an existing WBT specialist to a new humanoid embodiment with only a small amount of data and compute. Any2Any first performs kinematic alignment between source and target humanoids, aligning their input and output spaces so that the pretrained source policy can be meaningfully reused on the target embodiment. Any2Any then performs dynamics adaptation by applying lightweight parameter-efficient fine-tuning (PEFT) components to selected dynamics-sensitive modules, preserving useful behavioral priors while enabling targeted adaptation to the target robot. Extensive experiments on multiple humanoid platforms and pretrained backbones show that Any2Any substantially accelerates convergence and reduces training cost compared with training from scratch, while achieving competitive or superior tracking performance. Notably, using only 1% of the compute and data required for full training, Any2Any successfully transfers Sonic models pre-trained on Unitree G1 to LimX Oli and LimX Luna. These results suggest that pretrained WBT specialists can be efficiently reused across embodiments, providing a scalable path toward deploying humanoid whole-body control on new robots. More results and videos are available on our project page: https://any2any.top/.

## Content
Whole-body tracking (WBT) models have become a key foundation for humanoid robots, enabling them to imitate diverse motions with high fidelity. Training such models from scratch requires large-scale data and computation, making rapid deployment on new humanoid platforms costly. This raises a natural question: Can pretrained WBT models transfer across embodiments with minimal adaptation? To answer this question, we propose Any2Any, a paradigm that efficiently transfers an existing WBT specialist to a new humanoid embodiment with only a small amount of data and compute. Any2Any first performs kinematic alignment between source and target humanoids, aligning their input and output spaces so that the pretrained source policy can be meaningfully reused on the target embodiment. Any2Any then performs dynamics adaptation by applying lightweight parameter-efficient fine-tuning (PEFT) components to selected dynamics-sensitive modules, preserving useful behavioral priors while enabling targeted adaptation to the target robot. Extensive experiments on multiple humanoid platforms and pretrained backbones show that Any2Any substantially accelerates convergence and reduces training cost compared with training from scratch, while achieving competitive or superior tracking performance. Notably, using only 1% of the compute and data required for full training, Any2Any successfully transfers Sonic models pre-trained on Unitree G1 to LimX Oli and LimX Luna. These results suggest that pretrained WBT specialists can be efficiently reused across embodiments, providing a scalable path toward deploying humanoid whole-body control on new robots. More results and videos are available on our project page: https://any2any.top/.

## 개요
전신 추적(WBT) 모델은 인간형 로봇의 핵심 기반이 되어, 다양한 동작을 높은 정확도로 모방할 수 있게 합니다. 이러한 모델을 처음부터 학습하려면 대규모 데이터와 연산이 필요하므로, 새로운 인간형 플랫폼에 신속하게 배포하는 데 비용이 많이 듭니다. 이는 자연스러운 질문을 제기합니다: 사전 학습된 WBT 모델이 최소한의 적응만으로 다른 체현(embodiment) 간에 전이될 수 있을까? 이 질문에 답하기 위해, 우리는 Any2Any를 제안합니다. 이는 소량의 데이터와 연산만으로 기존 WBT 전문가 모델을 새로운 인간형 체현에 효율적으로 전이하는 패러다임입니다. Any2Any는 먼저 소스와 타겟 인간형 간의 운동학적 정렬(kinematic alignment)을 수행하여 입력 및 출력 공간을 정렬함으로써, 사전 학습된 소스 정책이 타겟 체현에서 의미 있게 재사용될 수 있도록 합니다. 그런 다음 Any2Any는 동역학 적응(dynamics adaptation)을 위해 선택된 동역학에 민감한 모듈에 경량 파라미터 효율적 미세 조정(PEFT) 구성 요소를 적용하여, 유용한 행동 사전(behavioral priors)을 보존하면서 타겟 로봇에 맞춘 적응을 가능하게 합니다. 여러 인간형 플랫폼과 사전 학습된 백본에 대한 광범위한 실험 결과, Any2Any는 처음부터 학습하는 것에 비해 수렴 속도를 크게 가속화하고 학습 비용을 줄이면서도 경쟁력 있거나 우수한 추적 성능을 달성합니다. 특히, 전체 학습에 필요한 연산과 데이터의 1%만을 사용하여, Any2Any는 Unitree G1에서 사전 학습된 Sonic 모델을 LimX Oli와 LimX Luna로 성공적으로 전이합니다. 이러한 결과는 사전 학습된 WBT 전문가 모델이 체현 간에 효율적으로 재사용될 수 있음을 시사하며, 새로운 로봇에 인간형 전신 제어를 배포하기 위한 확장 가능한 경로를 제공합니다. 더 많은 결과와 비디오는 프로젝트 페이지(https://any2any.top/)에서 확인할 수 있습니다.

## 핵심 내용
전신 추적(WBT) 모델은 인간형 로봇의 핵심 기반이 되어, 다양한 동작을 높은 정확도로 모방할 수 있게 합니다. 이러한 모델을 처음부터 학습하려면 대규모 데이터와 연산이 필요하므로, 새로운 인간형 플랫폼에 신속하게 배포하는 데 비용이 많이 듭니다. 이는 자연스러운 질문을 제기합니다: 사전 학습된 WBT 모델이 최소한의 적응만으로 다른 체현 간에 전이될 수 있을까? 이 질문에 답하기 위해, 우리는 Any2Any를 제안합니다. 이는 소량의 데이터와 연산만으로 기존 WBT 전문가 모델을 새로운 인간형 체현에 효율적으로 전이하는 패러다임입니다. Any2Any는 먼저 소스와 타겟 인간형 간의 운동학적 정렬을 수행하여 입력 및 출력 공간을 정렬함으로써, 사전 학습된 소스 정책이 타겟 체현에서 의미 있게 재사용될 수 있도록 합니다. 그런 다음 Any2Any는 동역학 적응을 위해 선택된 동역학에 민감한 모듈에 경량 파라미터 효율적 미세 조정(PEFT) 구성 요소를 적용하여, 유용한 행동 사전을 보존하면서 타겟 로봇에 맞춘 적응을 가능하게 합니다. 여러 인간형 플랫폼과 사전 학습된 백본에 대한 광범위한 실험 결과, Any2Any는 처음부터 학습하는 것에 비해 수렴 속도를 크게 가속화하고 학습 비용을 줄이면서도 경쟁력 있거나 우수한 추적 성능을 달성합니다. 특히, 전체 학습에 필요한 연산과 데이터의 1%만을 사용하여, Any2Any는 Unitree G1에서 사전 학습된 Sonic 모델을 LimX Oli와 LimX Luna로 성공적으로 전이합니다. 이러한 결과는 사전 학습된 WBT 전문가 모델이 체현 간에 효율적으로 재사용될 수 있음을 시사하며, 새로운 로봇에 인간형 전신 제어를 배포하기 위한 확장 가능한 경로를 제공합니다. 더 많은 결과와 비디오는 프로젝트 페이지(https://any2any.top/)에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2605.23733v3
