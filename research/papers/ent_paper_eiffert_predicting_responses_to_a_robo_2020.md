---
$id: ent_paper_eiffert_predicting_responses_to_a_robo_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Predicting Responses to a Robot's Future Motion using Generative Recurrent Neural
    Networks
  zh: 利用生成式循环神经网络预测机器人未来运动的响应
  ko: 생성 순환 신경망을 이용한 로봇의 미래 동작에 대한 반응 예측
summary:
  en: Proposes ResponseRNN, a spatio-temporal graph RNN that conditions future trajectory
    predictions of surrounding pedestrians or livestock on a robot's planned next
    action, improving close-range interaction prediction and enabling simulation of
    agent responses without hand-crafted interaction rules.
  zh: 提出 ResponseRNN，一种将周围行人或牲畜的未来轨迹预测条件于机器人规划动作之上的时空图循环神经网络，提升了近距离交互预测精度，并能在无需手工交互规则的情况下模拟周围智能体对机器人动作的响应。
  ko: ResponseRNN을 제안하는데, 이는 로봇의 계획된 다음 행동을 조건으로 주변 보행자나 가축의 미래 궤적을 예측하는 시공간 그래프 RNN으로,
    근거리 상호작용 예측 정확도를 높이고 수작업 상호작용 규칙 없이 주변 개체의 반응을 시뮬레이션할 수 있음을 보였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- trajectory_prediction
- social_navigation
- interaction_aware_prediction
- response_rnn
- generative_recurrent_network
- crowd_navigation
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv abstract and provided metadata; human review
    recommended before full verification.
sources:
- id: src_001
  type: paper
  title: Predicting Responses to a Robot's Future Motion using Generative Recurrent
    Neural Networks
  url: https://arxiv.org/abs/1909.13486
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

{'en': "Existing recurrent-neural-network (RNN) trajectory predictors forecast the future motion of nearby agents from observed positions alone. They do not incorporate the robot's own planned future action, so they cannot estimate how people or animals will move in response to the robot's intended path. Eiffert and Sukkarieh address this gap by proposing ResponseRNN, which takes the robot's next planned action as an additional input alongside the current states of surrounding individuals.\n\nResponseRNN is built as a spatio-temporal graph factorized into node and edge RNNs with attention, allowing it to handle heterogeneous agent types such as pedestrians, vehicles, bicycles, and livestock. The model outputs a bivariate Gaussian distribution over each non-controlled agent's future trajectory and is trained with a negative log-likelihood loss. By linking robot actions to observed responses during training, the network learns an implicit interaction model rather than relying on hand-crafted rules. At inference time it can therefore simulate state transitions for candidate robot actions, effectively acting as a learned forward model of multi-agent interaction.\n\nThe authors validate the approach on two real-world datasets: the Stanford Drone Dataset (SDD), which captures mixed pedestrian-vehicle-bicycle interactions in a university campus, and ARATH (A Robot Amongst the Herd), which records livestock interacting with a robotic vehicle. Results show improved prediction accuracy in close-range interactions compared with baselines that ignore the robot's planned action.", 'zh': '现有基于循环神经网络（RNN）的轨迹预测模型仅根据观测到的周围智能体位置预测未来运动，未考虑机器人自身的计划动作，因此无法估计人或动物会如何响应机器人预期路径。Eiffert 与 Sukkarieh 通过提出 ResponseRNN 弥补了这一空白，该方法将机器人的下一个计划动作与周围个体的当前状态一起作为输入。\n\nResponseRNN 采用可分解为节点 RNN 与边 RNN 并引入注意力机制的时空图结构，能够处理行人、车辆、自行车和牲畜等异构智能体类型。模型输出每个非受控智能体未来轨迹的双变量高斯分布，并通过负对数似然损失进行训练。通过在训练中将机器人动作与观测到的响应关联起来，网络学习到隐式的交互模型，而非依赖手工设计的规则。因此在推理阶段，它能够为候选机器人动作模拟状态转移，有效地充当多智能体交互的学习型前向模型。\n\n作者在两类真实数据集上验证了该方法：一是记录大学校园内行人与车辆/自行车混合交互的 Stanford Drone Dataset（SDD），二是记录牲畜与机器人车辆交互的 ARATH（A Robot Amongst the Herd）数据集。结果表明，与忽略机器人计划动作的基线相比，该方法在近距离交互中的预测精度更高。', 'ko': '기존 순환 신경망(RNN) 기반 궤적 예측 모델은 관찰된 주변 개체의 위치만으로 미래 운동을 예측하며, 로봇 자신의 계획된 미래 동작을 반영하지 않아 사람이나 동물이 로봇의 의도된 경로에 어떻게 반응할지 추정할 수 없다. Eiffert와 Sukkarieh는 ResponseRNN을 제안하여 이 격차를 해소하였는데, 해당 방법은 주변 개체의 현재 상태와 함께 로봇의 다음 계획 동작을 추가 입력으로 사용한다.\n\nResponseRNN은 노드 RNN과 엣지 RNN로 분해되고 어텐션을 갖는 시공간 그래프 구조로 구성되어 보행자, 차량, 자전거, 가축 등 이종 개체 유형을 처리할 수 있다. 모델은 통제되지 않은 각 개체의 미래 궤적에 대한 이변량 정규분포를 출력하며 negative log-likelihood 손실로 학습된다. 학습 중 로봇 동작과 관찰된 반응을 연결함으로써 네트워크는 수작업 규칙에 의존하지 않고 암시적 상호작용 모델을 학습한다. 따라서 추론 단계에서 후보 로봇 동작에 대한 상태 전이를 시뮬레이션하여 다중 개체 상호작용에 대한 학습된 전방 모델 역할을 할 수 있다.\n\n저자들은 대학 캠퍼스에서 보행자-차량-자전거 혼합 상호작용을 담은 Stanford Drone Dataset(SDD)와 가축이 로봇 차량과 상호작용하는 ARATH(A Robot Amongst the Herd) 데이터셋, 두 가지 실제 데이터셋에서 방법을 검증하였다. 결과는 로봇의 계획 동작을 무시하는 기준 모델에 비해 근거리 상호작용에서 예측 정확도가 향상되었음을 보여준다.'}

## Key Contributions

{'en': ["Introduces ResponseRNN, which conditions future trajectory predictions of surrounding agents on a controlled robot's planned future path.", 'Uses a spatio-temporal graph factorized into node and edge RNNs with attention to handle heterogeneous agent types.', 'Demonstrates improved prediction accuracy over baselines for close-range interactions in heterogeneous agent settings.', 'Shows the model can simulate how non-controlled agents would respond to different hypothetical robot actions without hand-crafted interaction rules.'], 'zh': ['提出 ResponseRNN，将周围智能体的未来轨迹预测条件于受控机器人的规划未来路径。', '采用分解为节点 RNN 与边 RNN 并引入注意力机制的时空图，以处理异构智能体类型。', '在异构智能体环境下的近距离交互中，展示出相比基线更高的预测精度。', '证明该模型能够模拟非受控智能体对不同假设机器人动作的响应，而无需手工设计的交互规则。'], 'ko': ['주변 개체의 미래 궤적 예측을 통제 로봇의 계획된 미래 경로에 조건화하는 ResponseRNN을 제안한다.', '이종 개체 유형을 처리하기 위해 노드 RNN과 엣지 RNN으로 분해되고 어텐션을 갖는 시공간 그래프를 사용한다.', '이종 개체 환경의 근거리 상호작용에서 기준 모델보다 향상된 예측 정확도를 입증한다.', '수작업 상호작용 규칙 없이 통제되지 않은 개체가 다양한 가상 로봇 동작에 어떻게 반응할지 시뮬레이션할 수 있음을 보인다.']}

## Relevance to Humanoid Robotics

{'en': 'Although the experiments use wheeled robots and vehicles, the learned interaction-aware prediction framework is directly transferable to humanoid robots navigating shared human environments. A humanoid can use ResponseRNN as a forward model to anticipate how pedestrians will react to candidate walking trajectories, supporting safer and more socially compliant motion planning in crowded spaces.', 'zh': '尽管实验使用的是轮式机器人和车辆，但所提出的交互感知预测框架可直接迁移到在共享人类环境中导航的人形机器人。人形机器人可将 ResponseRNN 用作前向模型，以预测行人对候选行走轨迹的反应，从而在拥挤空间中支持更安全、更符合社会规范的运动规划。', 'ko': '실험은 바퀴 로봇과 차량을 사용하지만, 학습된 상호작용 인식 예측 프레임워크는 인간과 공유하는 환경을 탐색하는 휴머노이드 로봇에 직접 적용할 수 있다. 휴머노이드는 ResponseRNN을 전방 모델로 사용하여 보행자가 후보 보행 궤적에 어떻게 반응할지 예측함으로써 혼잡한 공간에서 더 안전하고 사회적으로 적절한 동작 계획을 지원할 수 있다.'}
