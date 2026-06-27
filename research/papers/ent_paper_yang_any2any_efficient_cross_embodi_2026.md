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
  en: Any2Any transfers pretrained whole-body tracking policies across humanoid embodiments
    by first aligning the source and target kinematics, then fine-tuning only dynamics-sensitive
    modules with lightweight LoRA adapters. Experiments show competitive or better
    tracking using roughly 1% of the data and compute needed to train from scratch,
    including real-world deployment on LimX Oli.
  zh: Any2Any 通过首先对齐源机器人和目标机器人的运动学空间，然后仅对动力学敏感模块使用轻量级 LoRA 适配器进行微调，实现预训练全身跟踪策略在不同人形机器人本体间的迁移。实验表明，该方法仅使用从头训练约
    1% 的数据和计算量即可达到有竞争力或更优的跟踪性能，并已在 LimX Oli 上完成真实部署。
  ko: Any2Any는 먼저 소스와 타깃 휴머노이드의 운동학적 공간을 정렬한 후, 동역학에 민감한 모듈만 경량 LoRA 어댑터로 미세 조정하여
    사전 학습된 전신 추적 정책을 다른 구현체로 전이한다. 실험 결과, 처음부터 학습하는 데 필요한 데이터와 연산량의 약 1%만으로 경쟁력 있거나
    우수한 추적 성능을 달성했으며, LimX Oli에서 실제 배포되었다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from abstract and supplied metadata; exact section-level citations,
    full reference list, and real-world experimental details require human review
    before full verification.
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

## Overview

Whole-body tracking (WBT) policies let humanoid robots imitate diverse motions with high fidelity, but training them from scratch demands large motion datasets and substantial computation. Any2Any addresses this bottleneck by reusing a pretrained source WBT policy and adapting it to a new target humanoid. The framework first performs kinematic alignment between the source and target embodiments, mapping their observation and action spaces so that the source policy can run meaningfully on the target robot. It then carries out dynamics adaptation by inserting low-rank parameter-efficient fine-tuning (LoRA) modules into the policy components most affected by dynamics differences, while keeping the bulk of the pretrained backbone frozen.

The two-level design preserves the behavioral priors learned by the source policy and only updates a small number of parameters to correct for target-specific dynamics. The authors evaluate Any2Any across multiple source-target pairs and two pretrained backbones, showing faster convergence and lower training cost than training from scratch. Notably, they report transferring a Sonic policy pretrained on Unitree G1 to LimX Oli and LimX Luna using only about 1% of the data and compute required for full training, with competitive or improved tracking performance.

The paper also analyzes where LoRA should be placed, finding that the residual dynamics are best absorbed by modules handling proprioceptive input, action output, and critic estimation.

## Key Contributions

- First systematic demonstration that pretrained robot-specific humanoid whole-body tracking policies can transfer across embodiments.
- Any2Any two-stage framework: kinematic alignment of observations and actions followed by LoRA-based dynamics adaptation.
- Empirical result that transfer succeeds with roughly 1% of the data and compute of training from scratch across multiple humanoid pairs.
- Validation across two pretrained backbones and four humanoid embodiments, including real-world deployment on LimX Oli.
- Guidance that LoRA should be concentrated in proprioception input, action output, and critic modules to best capture dynamics residuals.

## Relevance to Humanoid Robotics

Any2Any directly reduces the cost of deploying whole-body controllers on new humanoid platforms, which is critical for scalable mass production and heterogeneous fleets. By reusing pretrained policies instead of training from scratch, manufacturers and operators can shorten the bring-up time for new robot hardware. The inclusion of real-world LimX Oli results and the focus on widely used humanoid platforms (Unitree G1, Unitree H1, LimX Oli, LimX Luna) makes the work strongly aligned with the humanoid-robot industry chain.
