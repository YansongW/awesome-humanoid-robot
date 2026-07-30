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
  zh: World-Gymnast 是一种通过动作条件视频世界模型（WorldGym）进行强化学习微调视觉-语言-动作（VLA）策略的方法。它利用 Group Relative Policy Optimization (GRPO) 和 GPT-4o
    奖励模型，在 Bridge WidowX 机器人上实现了比监督微调高 18 倍、比基于模拟器的强化学习高 2 倍的成功率。核心贡献在于展示了世界模型在机器人策略训练中的潜力，包括处理多样化语言指令和新场景。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02454v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
World-Gymnast 通过将 VLA 策略在动作条件视频世界模型（WorldGym）中展开，并使用二进制视觉语言模型（GPT-4o）对想象轨迹进行评分，从而进行强化学习微调。该方法在 Bridge WidowX 机器人设置上，相比监督微调（SFT）实现了高达 18 倍的成功率提升，相比基于模拟器的强化学习（RL）实现了 2 倍的提升。更重要的是，World-Gymnast 展示了世界模型强化学习的独特能力，包括在多样化语言指令和新场景上训练、在新场景中进行测试时训练，以及在线迭代改进世界模型和策略。

## 核心内容
### 方法
World-Gymnast 的核心是使用动作条件视频世界模型（WorldGym）作为策略训练的环境。具体流程如下：
- **策略展开**：将预训练的 VLA 策略在 WorldGym 中展开，生成想象轨迹。
- **奖励评分**：使用二进制视觉语言模型（GPT-4o）对生成的轨迹进行评分，作为强化学习的奖励信号。
- **优化算法**：采用 Group Relative Policy Optimization (GRPO) 进行策略微调，通过组内相对比较来优化策略。

### 实验设置
- **机器人平台**：Bridge WidowX 机器人设置。
- **基线对比**：监督微调（SFT）和基于模拟器的强化学习（Simulator-based RL）。
- **评估指标**：任务成功率。

### 关键结果
- **性能提升**：World-Gymnast 在 Bridge 机器人设置上，成功率比 SFT 高 18 倍，比基于模拟器的 RL 高 2 倍。
- **独特能力**：
  - **多样化语言指令**：能够处理多种语言指令，并在世界模型中进行训练。
  - **新场景训练**：可以在世界模型生成的新场景中进行训练，无需真实物理交互。
  - **测试时训练**：在新场景中，可以在测试时进行在线训练，适应环境变化。
  - **在线迭代改进**：世界模型和策略可以同时在线迭代改进，形成闭环优化。

### 结论
World-Gymnast 的结果表明，学习世界模型并在云端训练机器人策略，可能是弥合演示机器人与家庭机器人之间差距的关键。该方法通过减少对物理交互的依赖，显著提升了机器人策略的泛化能力和训练效率。

## Overview
Robot learning from interacting with the physical world is fundamentally bottlenecked by the cost of physical interaction. The two alternatives, supervised finetuning (SFT) from expert demonstrations and reinforcement learning (RL) in a software-based simulator, are limited by the amount of expert data available and the sim-to-real gap for manipulation. With the recent emergence of world models learned from real-world video-action data, we ask the question of whether training a policy in a world model can be more effective than supervised learning or software simulation in achieving better real-robot performance. We propose World-Gymnast, which performs RL finetuning of a vision-language-action (VLA) policy by rolling out the policy in an action-conditioned video world model and rewarding the rollouts with a vision-language model (VLM). On the Bridge robot setup, World-Gymnast outperforms SFT by as much as 18x and outperforms software simulator by as much as 2x. More importantly, World-Gymnast demonstrates intriguing capabilities of RL with a world model, including training on diverse language instructions and novel scenes from the world model, test-time training in a novel scene, and online iterative world model and policy improvement. Our results suggest learning a world model and training robot policies in the cloud could be the key to bridging the gap between robots that work in demonstrations and robots that can work in anyone's household.

## 개요
물리적 세계와의 상호작용을 통한 로봇 학습은 근본적으로 물리적 상호작용 비용에 의해 병목 현상이 발생합니다. 두 가지 대안인 전문가 시연을 통한 지도 미세 조정(SFT)과 소프트웨어 기반 시뮬레이터에서의 강화 학습(RL)은 사용 가능한 전문가 데이터의 양과 조작 작업에서의 시뮬레이션-실제 간극(sim-to-real gap)에 의해 제한됩니다. 최근 실제 세계 비디오-행동 데이터로 학습된 세계 모델의 등장에 따라, 우리는 세계 모델에서 정책을 훈련하는 것이 더 나은 실제 로봇 성능을 달성하는 데 있어 지도 학습이나 소프트웨어 시뮬레이션보다 더 효과적일 수 있는지 질문합니다. 우리는 World-Gymnast를 제안하며, 이는 행동 조건부 비디오 세계 모델에서 정책을 롤아웃하고 비전-언어 모델(VLM)로 롤아웃에 보상을 부여하여 비전-언어-행동(VLA) 정책의 RL 미세 조정을 수행합니다. Bridge 로봇 설정에서 World-Gymnast는 SFT보다 최대 18배, 소프트웨어 시뮬레이터보다 최대 2배 더 뛰어난 성능을 보입니다. 더 중요한 것은, World-Gymnast가 세계 모델을 통한 RL의 흥미로운 능력, 즉 다양한 언어 명령어와 세계 모델의 새로운 장면에 대한 훈련, 새로운 장면에서의 테스트 시간 훈련, 온라인 반복적 세계 모델 및 정책 개선을 보여준다는 점입니다. 우리의 결과는 세계 모델을 학습하고 클라우드에서 로봇 정책을 훈련하는 것이 시연에서 작동하는 로봇과 누구의 가정에서나 작동할 수 있는 로봇 간의 격차를 해소하는 열쇠가 될 수 있음을 시사합니다.

## 핵심 내용
물리적 세계와의 상호작용을 통한 로봇 학습은 근본적으로 물리적 상호작용 비용에 의해 병목 현상이 발생합니다. 두 가지 대안인 전문가 시연을 통한 지도 미세 조정(SFT)과 소프트웨어 기반 시뮬레이터에서의 강화 학습(RL)은 사용 가능한 전문가 데이터의 양과 조작 작업에서의 시뮬레이션-실제 간극(sim-to-real gap)에 의해 제한됩니다. 최근 실제 세계 비디오-행동 데이터로 학습된 세계 모델의 등장에 따라, 우리는 세계 모델에서 정책을 훈련하는 것이 더 나은 실제 로봇 성능을 달성하는 데 있어 지도 학습이나 소프트웨어 시뮬레이션보다 더 효과적일 수 있는지 질문합니다. 우리는 World-Gymnast를 제안하며, 이는 행동 조건부 비디오 세계 모델에서 정책을 롤아웃하고 비전-언어 모델(VLM)로 롤아웃에 보상을 부여하여 비전-언어-행동(VLA) 정책의 RL 미세 조정을 수행합니다. Bridge 로봇 설정에서 World-Gymnast는 SFT보다 최대 18배, 소프트웨어 시뮬레이터보다 최대 2배 더 뛰어난 성능을 보입니다. 더 중요한 것은, World-Gymnast가 세계 모델을 통한 RL의 흥미로운 능력, 즉 다양한 언어 명령어와 세계 모델의 새로운 장면에 대한 훈련, 새로운 장면에서의 테스트 시간 훈련, 온라인 반복적 세계 모델 및 정책 개선을 보여준다는 점입니다. 우리의 결과는 세계 모델을 학습하고 클라우드에서 로봇 정책을 훈련하는 것이 시연에서 작동하는 로봇과 누구의 가정에서나 작동할 수 있는 로봇 간의 격차를 해소하는 열쇠가 될 수 있음을 시사합니다.

## 参考
- http://arxiv.org/abs/2602.02454v1
