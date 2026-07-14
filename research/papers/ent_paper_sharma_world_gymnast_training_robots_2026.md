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
  en: World-Gymnast fine-tunes a vision-language-action (VLA) policy via Group Relative Policy Optimization (GRPO) by rolling
    it out in an action-conditioned video world model (WorldGym) and scoring imagined trajectories with a binary vision-language-model
    (GPT-4o) reward. On the Bridge WidowX robot setup it achieves up to 18× higher success than supervised fine-tuning and
    2× higher than simulator-based RL.
  zh: World-Gymnast 通过在动作条件化视频世界模型（WorldGym）中 rollout 视觉-语言-动作（VLA）策略，并使用视觉语言模型（GPT-4o）给出二元任务完成奖励，以 GRPO 进行强化学习微调；在 Bridge
    WidowX 机器人平台上，其成功率较监督微调最高提升 18 倍，较基于软件仿真器的强化学习最高提升 2 倍。
  ko: World-Gymnast는 동작 조건부 비디오 월드 모델(WorldGym)에서 VLA 정책을 롤아웃하고 VLM(GPT-4o) 이진 태스크 완료 보상을 부여한 후 GRPO로 강화학습 미세조정을 수행한다. Bridge
    WidowX 로봇 플랫폼에서 SFT보다 최대 18배, 시뮬레이터 기반 RL보다 최대 2배 높은 성공률을 달성했다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02454v1.
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
## 概述
Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world model can be more effective than supervised learning or software simulation in achieving better real-robot performance. We propose World-Gymnast, which performs RL finetuning of a vision-language-action (VLA) policy by rolling out the policy in an action-conditioned video world model and rewarding the rollouts with a vision-language model (VLM). On the Bridge robot setup, World-Gymnast outperforms SFT by as much as 18x and outperforms software simulator by as much as 2x. More importantly, World-Gymnast demonstrates intriguing capabilities of RL with a world model, including training on diverse language instructions and novel scenes from the world model, test-time training in a novel scene, and online iterative world model and policy improvement. Our results suggest learning a world model and training robot policies in the cloud could be the key to bridging the gap between robots that work in demonstrations and robots that can work in anyone's household.

## 核心内容
Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world model can be more effective than supervised learning or software simulation in achieving better real-robot performance. We propose World-Gymnast, which performs RL finetuning of a vision-language-action (VLA) policy by rolling out the policy in an action-conditioned video world model and rewarding the rollouts with a vision-language model (VLM). On the Bridge robot setup, World-Gymnast outperforms SFT by as much as 18x and outperforms software simulator by as much as 2x. More importantly, World-Gymnast demonstrates intriguing capabilities of RL with a world model, including training on diverse language instructions and novel scenes from the world model, test-time training in a novel scene, and online iterative world model and policy improvement. Our results suggest learning a world model and training robot policies in the cloud could be the key to bridging the gap between robots that work in demonstrations and robots that can work in anyone's household.

## 参考
- http://arxiv.org/abs/2602.02454v1

