---
$id: ent_paper_sharma_world_gymnast_training_robots_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'World-Gymnast: Training Robots with Reinforcement Learning in a World Model'
  zh: World-Gymnast：在世界模型中利用强化学习训练机器人
  ko: 'World-Gymnast: 월드 모델에서 강화학습으로 로봇 훈련하기'
summary:
  en: World-Gymnast fine-tunes a vision-language-action (VLA) policy via Group Relative
    Policy Optimization (GRPO) by rolling it out in an action-conditioned video world
    model (WorldGym) and scoring imagined trajectories with a binary vision-language-model
    (GPT-4o) reward. On the Bridge WidowX robot setup it achieves up to 18× higher
    success than supervised fine-tuning and 2× higher than simulator-based RL.
  zh: World-Gymnast 通过在动作条件化视频世界模型（WorldGym）中 rollout 视觉-语言-动作（VLA）策略，并使用视觉语言模型（GPT-4o）给出二元任务完成奖励，以
    GRPO 进行强化学习微调；在 Bridge WidowX 机器人平台上，其成功率较监督微调最高提升 18 倍，较基于软件仿真器的强化学习最高提升 2 倍。
  ko: World-Gymnast는 동작 조건부 비디오 월드 모델(WorldGym)에서 VLA 정책을 롤아웃하고 VLM(GPT-4o) 이진 태스크
    완료 보상을 부여한 후 GRPO로 강화학습 미세조정을 수행한다. Bridge WidowX 로봇 플랫폼에서 SFT보다 최대 18배, 시뮬레이터
    기반 RL보다 최대 2배 높은 성공률을 달성했다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- world_model
- reinforcement_learning
- grpo
- vlm_reward
- sim_to_real
- bridge_data
- widowx
- action_conditioned_video_generation
- cloud_robot_training
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv full text; factual claims are backed by paper
    excerpts, but human review is required before full verification.
sources:
- id: src_001
  type: paper
  title: 'World-Gymnast: Training Robots with Reinforcement Learning in a World Model'
  url: https://arxiv.org/abs/2602.02454
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
related_entities:
- id: ent_dataset_open_x_embodiment
  relationship: uses_dataset
  description:
    en: OpenVLA and the WorldGym variant are pretrained on the Open X-Embodiment dataset.
    zh: OpenVLA 与 WorldGym 变体均在 Open X-Embodiment 数据集上进行预训练。
    ko: OpenVLA와 WorldGym 변형 모델은 Open X-Embodiment 데이터셋으로 사전학습되었다.
---

## Overview

Real-world robot learning is bottlenecked by the cost and risk of physical interaction. Supervised fine-tuning from demonstrations covers only a narrow slice of situations, and reinforcement learning in hand-engineered simulators suffers from a large sim-to-real visual and physical gap. World-Gymnast addresses this by training a VLA policy inside a learned action-conditioned video world model, using only imagined rollouts and a VLM-based reward signal.

The framework adopts Group Relative Policy Optimization (GRPO). For each language instruction and initial frame, it samples a group of trajectories from the policy in WorldGym, scores each rollout with a binary task-completion reward from GPT-4o, and normalizes those rewards within the group to compute advantages for policy updates. This design enables several emergent capabilities: training from arbitrary initial frames, augmenting language instructions, injecting synthetic distractors into scenes, test-time training on a novel real-robot frame without physical rollouts, and online iterative improvement of both the world model and policy in a Dyna-style loop.

The authors evaluate World-Gymnast on the Bridge robot platform with a WidowX arm, using AutoEval for real-robot assessment and SIMPLER as a software-simulator baseline. The base policy is OpenVLA-OFT initialized from OpenVLA 7B and fine-tuned on BridgeData V2. Across AutoEval manipulation tasks, World-Gymnast substantially outperforms both supervised fine-tuning and simulator-based RL, while ablations show gains from distractor training, novel-language training, and task scaling.

## Key Contributions

- RL fine-tuning of VLA policies inside a learned video world model using VLM-based binary rewards.
- Training from arbitrary initial frames, novel language instructions, and distractor-augmented scenes.
- Test-time training on novel real-robot frames without requiring physical rollouts.
- Iterative world model and policy improvement via Dyna-style online updates with real-world data.
- Real-robot evaluation on AutoEval showing up to 18× improvement over SFT and 2× over simulator-based RL.

## Relevance to Humanoid Robotics

Humanoid robots must operate in unstructured, diverse households where collecting large amounts of safe physical interaction data is impractical. World-Gymnast reduces dependence on expensive real-world trials and manual simulator engineering by enabling scalable, cloud-based RL training in a world model learned from real video-action data. The ability to train and test-time adapt on novel scenes and instructions, and to iteratively improve both policy and world model, is directly aligned with the scaling requirements for general-purpose humanoid systems.
