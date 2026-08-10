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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.02454v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (997 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2602.02454v1

## 개요
World-Gymnast는 VLA 정책을 액션 조건부 비디오 월드 모델(WorldGym)에서 전개하고, 이진 비전-언어 모델(GPT-4o)로 상상된 궤적을 평가하여 강화 학습 미세 조정을 수행합니다. 이 방법은 Bridge WidowX 로봇 설정에서 지도 미세 조정(SFT) 대비 최대 18배의 성공률 향상, 시뮬레이터 기반 강화 학습(RL) 대비 2배의 향상을 달성했습니다. 더 중요한 것은, World-Gymnast는 다양한 언어 명령과 새로운 시나리오에서의 훈련, 새로운 시나리오에서 테스트 시 훈련, 그리고 월드 모델과 정책의 온라인 반복 개선을 포함한 월드 모델 강화 학습의 독특한 능력을 보여줍니다.

## 핵심 내용
### 방법
World-Gymnast의 핵심은 액션 조건부 비디오 월드 모델(WorldGym)을 정책 훈련 환경으로 사용하는 것입니다. 구체적인 절차는 다음과 같습니다:
- **정책 전개**: 사전 훈련된 VLA 정책을 WorldGym에서 전개하여 상상된 궤적을 생성합니다.
- **보상 평가**: 이진 비전-언어 모델(GPT-4o)로 생성된 궤적을 평가하여 강화 학습의 보상 신호로 사용합니다.
- **최적화 알고리즘**: Group Relative Policy Optimization (GRPO)을 사용하여 정책을 미세 조정하며, 그룹 내 상대 비교를 통해 정책을 최적화합니다.

### 실험 설정
- **로봇 플랫폼**: Bridge WidowX 로봇 설정.
- **기준 비교**: 지도 미세 조정(SFT) 및 시뮬레이터 기반 강화 학습(Simulator-based RL).
- **평가 지표**: 작업 성공률.

### 주요 결과
- **성능 향상**: World-Gymnast는 Bridge 로봇 설정에서 SFT보다 성공률이 18배 높고, 시뮬레이터 기반 RL보다 2배 높습니다.
- **독특한 능력**:
  - **다양한 언어 명령**: 다양한 언어 명령을 처리하고 월드 모델에서 훈련할 수 있습니다.
  - **새로운 시나리오 훈련**: 실제 물리적 상호작용 없이 월드 모델에서 생성된 새로운 시나리오에서 훈련할 수 있습니다.
  - **테스트 시 훈련**: 새로운 시나리오에서 테스트 시 온라인 훈련을 통해 환경 변화에 적응할 수 있습니다.
  - **온라인 반복 개선**: 월드 모델과 정책을 동시에 온라인으로 반복 개선하여 폐쇄 루프 최적화를 형성할 수 있습니다.

### 결론
World-Gymnast의 결과는 월드 모델을 학습하고 클라우드에서 로봇 정책을 훈련하는 것이 데모 로봇과 가정용 로봇 간의 격차를 메우는 핵심이 될 수 있음을 시사합니다. 이 방법은 물리적 상호작용에 대한 의존도를 줄임으로써 로봇 정책의 일반화 능력과 훈련 효율성을 크게 향상시킵니다.
