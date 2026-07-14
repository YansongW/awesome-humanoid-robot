---
$id: ent_paper_learn_weightlessness_imitate_n_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
  zh: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
  ko: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
summary:
  en: "arXiv:2604.21351v2 Announce Type: replace \nAbstract: The integration of imitation and reinforcement learning has enabled\
    \ remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on\
    \ environment-dependent motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting\
    \ physical interactions with the environment. We observe that humans naturally exploit a \"weightless\" state during non-self-stabilizing\
    \ (NSS) motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing\
    \ the body and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling\
    \ strategy for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines\
    \ which joints to relax and to what level, together enabling effective environmental interaction while executing target\
    \ motions. We evaluate our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on\
    \ beds with different inclinations, and leaning against walls via shoulder or elbow. Extensive experiments in simulation\
    \ and on the Unitree G1 robot demonstrate that our WM method, trained on single-action demonstrations without any task-specific\
    \ tuning, achieves strong generalization across diverse environmental configurations while maintaining motion stability.\
    \ Our work bridges the gap between precise trajectory tracking and adaptive environmental interaction, offering a biologically-inspired\
    \ solution for contact-rich humanoid control."
  zh: "arXiv:2604.21351v2 Announce Type: replace \nAbstract: The integration of imitation and reinforcement learning has enabled\
    \ remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on\
    \ environment-dependent motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting\
    \ physical interactions with the environment. We observe that humans naturally exploit a \"weightless\" state during non-self-stabilizing\
    \ (NSS) motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing\
    \ the body and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling\
    \ strategy for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines\
    \ which joints to relax and to what level, together enabling effective environmental interaction while executing target\
    \ motions. We evaluate our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on\
    \ beds with different inclinations, and leaning against walls via shoulder or elbow. Extensive experiments in simulation\
    \ and on the Unitree G1 robot demonstrate that our WM method, trained on single-action demonstrations without any task-specific\
    \ tuning, achieves strong generalization across diverse environmental configurations while maintaining motion stability.\
    \ Our work bridges the gap between precise trajectory tracking and adaptive environmental interaction, offering a biologically-inspired\
    \ solution for contact-rich humanoid control."
  ko: "arXiv:2604.21351v2 Announce Type: replace \nAbstract: The integration of imitation and reinforcement learning has enabled\
    \ remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on\
    \ environment-dependent motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting\
    \ physical interactions with the environment. We observe that humans naturally exploit a \"weightless\" state during non-self-stabilizing\
    \ (NSS) motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing\
    \ the body and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling\
    \ strategy for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines\
    \ which joints to relax and to what level, together enabling effective environmental interaction while executing target\
    \ motions. We evaluate our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on\
    \ beds with different inclinations, and leaning against walls via shoulder or elbow. Extensive experiments in simulation\
    \ and on the Unitree G1 robot demonstrate that our WM method, trained on single-action demonstrations without any task-specific\
    \ tuning, achieves strong generalization across diverse environmental configurations while maintaining motion stability.\
    \ Our work bridges the gap between precise trajectory tracking and adaptive environmental interaction, offering a biologically-inspired\
    \ solution for contact-rich humanoid control."
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
- learn_weightlessness
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.21351v2.
sources:
- id: src_001
  type: paper
  title: 'Learn Weightlessness: Imitate Non-Self-Stabilizing Motions on Humanoid Robot'
  url: https://arxiv.org/abs/2604.21351
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
The integration of imitation and reinforcement learning has enabled remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on environment-dependent motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting physical interactions with the environment. We observe that humans naturally exploit a "weightless" state during non-self-stabilizing (NSS) motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing the body and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling strategy for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines which joints to relax and to what level, together enabling effective environmental interaction while executing target motions. We evaluate our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on beds with different inclinations, and leaning against walls via shoulder or elbow. Extensive experiments in simulation and on the Unitree G1 robot demonstrate that our WM method, trained on single-action demonstrations without any task-specific tuning, achieves strong generalization across diverse environmental configurations while maintaining motion stability. Our work bridges the gap between precise trajectory tracking and adaptive environmental interaction, offering a biologically-inspired solution for contact-rich humanoid control.

## 核心内容
The integration of imitation and reinforcement learning has enabled remarkable advances in humanoid whole-body control, facilitating diverse human-like behaviors. However, research on environment-dependent motions remains limited. Existing methods typically enforce rigid trajectory tracking while neglecting physical interactions with the environment. We observe that humans naturally exploit a "weightless" state during non-self-stabilizing (NSS) motions--selectively relaxing specific joints to allow passive body--environment contact, thereby stabilizing the body and completing the motion. Inspired by this biological mechanism, we design a weightlessness-state auto-labeling strategy for dataset annotation; and we propose the Weightlessness Mechanism (WM), a method that dynamically determines which joints to relax and to what level, together enabling effective environmental interaction while executing target motions. We evaluate our approach on 3 representative NSS tasks: sitting on chairs of varying heights, lying down on beds with different inclinations, and leaning against walls via shoulder or elbow. Extensive experiments in simulation and on the Unitree G1 robot demonstrate that our WM method, trained on single-action demonstrations without any task-specific tuning, achieves strong generalization across diverse environmental configurations while maintaining motion stability. Our work bridges the gap between precise trajectory tracking and adaptive environmental interaction, offering a biologically-inspired solution for contact-rich humanoid control.

## 参考
- http://arxiv.org/abs/2604.21351v2

