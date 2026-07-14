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
  zh: Any2Any 通过首先对齐源机器人和目标机器人的运动学空间，然后仅对动力学敏感模块使用轻量级 LoRA 适配器进行微调，实现预训练全身跟踪策略在不同人形机器人本体间的迁移。实验表明，该方法仅使用从头训练约 1% 的数据和计算量即可达到有竞争力或更优的跟踪性能，并已在
    LimX Oli 上完成真实部署。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2605.23733v3.
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
Whole-body tracking (WBT) models have become a key foundation for humanoid robots, enabling them to imitate diverse motions with high fidelity. Training such models from scratch requires large-scale data and computation, making rapid deployment on new humanoid platforms costly. This raises a natural question: Can pretrained WBT models transfer across embodiments with minimal adaptation? To answer this question, we propose Any2Any, a paradigm that efficiently transfers an existing WBT specialist to a new humanoid embodiment with only a small amount of data and compute. Any2Any first performs kinematic alignment between source and target humanoids, aligning their input and output spaces so that the pretrained source policy can be meaningfully reused on the target embodiment.Any2Any then performs dynamics adaptation by applying lightweight parameter-efficient fine-tuning (PEFT) components to selected dynamics-sensitive modules, preserving useful behavioral priors while enabling targeted adaptation to the target robot. Extensive experiments on multiple humanoid platforms and pretrained backbones show that Any2Any substantially accelerates convergence and reduces training cost compared with training from scratch, while achieving competitive or superior tracking performance. Notably, using only 1% of the compute and data required for full training, Any2Any successfully transfers Sonic models pre-trained on Unitree G1 to LimX Oli and LimX Luna. These results suggest that pretrained WBT specialists can be efficiently reused across embodiments, providing a scalable path toward deploying humanoid whole-body control on new robots. More results and videos are available on our project page: https://any2any.top/.

## 核心内容
Whole-body tracking (WBT) models have become a key foundation for humanoid robots, enabling them to imitate diverse motions with high fidelity. Training such models from scratch requires large-scale data and computation, making rapid deployment on new humanoid platforms costly. This raises a natural question: Can pretrained WBT models transfer across embodiments with minimal adaptation? To answer this question, we propose Any2Any, a paradigm that efficiently transfers an existing WBT specialist to a new humanoid embodiment with only a small amount of data and compute. Any2Any first performs kinematic alignment between source and target humanoids, aligning their input and output spaces so that the pretrained source policy can be meaningfully reused on the target embodiment.Any2Any then performs dynamics adaptation by applying lightweight parameter-efficient fine-tuning (PEFT) components to selected dynamics-sensitive modules, preserving useful behavioral priors while enabling targeted adaptation to the target robot. Extensive experiments on multiple humanoid platforms and pretrained backbones show that Any2Any substantially accelerates convergence and reduces training cost compared with training from scratch, while achieving competitive or superior tracking performance. Notably, using only 1% of the compute and data required for full training, Any2Any successfully transfers Sonic models pre-trained on Unitree G1 to LimX Oli and LimX Luna. These results suggest that pretrained WBT specialists can be efficiently reused across embodiments, providing a scalable path toward deploying humanoid whole-body control on new robots. More results and videos are available on our project page: https://any2any.top/.

## 参考
- http://arxiv.org/abs/2605.23733v3

