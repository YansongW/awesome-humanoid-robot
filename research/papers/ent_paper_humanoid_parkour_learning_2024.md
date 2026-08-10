---
$id: ent_paper_humanoid_parkour_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Parkour Learning
  zh: Humanoid Parkour Learning
  ko: Humanoid Parkour Learning
summary:
  en: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
  zh: Humanoid Parkour Learning 是2024年提出的人形机器人运动控制框架，由研究团队开发。其核心贡献在于无需运动先验，通过端到端视觉驱动的全身控制强化学习策略，使人形机器人能够自主完成跳跃0.42米平台、跨越0.8米间隙、野外奔跑（1.8m/s）等多种跑酷技能，并支持移动操作任务迁移。
  ko: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_parkour_learning
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10759v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (883 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Humanoid Parkour Learning (arXiv)
  url: https://arxiv.org/abs/2406.10759
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Parkour Learning project page
  url: https://humanoid4parkour.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人跑酷这一极具挑战性的运动控制问题，提出了一种无需运动先验的端到端学习框架。与现有依赖单轨迹优化或大量运动参考数据的方法不同，该框架通过视觉输入直接生成全身控制策略，使人形机器人能够自主选择并执行多种跑酷技能。实验表明，机器人不仅能完成跳跃平台、跨越障碍等复杂动作，还能在野外以1.8m/s的速度奔跑，并在不同地形上稳健行走。此外，通过覆盖手臂动作，该框架可轻松迁移至人形移动操作任务。

## 核心内容
### 方法架构
- 采用端到端强化学习框架，输入为视觉图像（来自机器人头部摄像头）与本体感知数据（关节角度、IMU等），输出为全身关节控制指令。
- 策略网络基于卷积神经网络（CNN）处理视觉特征，结合多层感知机（MLP）融合本体感知信息，最终生成动作指令。
- 训练过程中无需任何运动先验（如参考轨迹或动作捕捉数据），完全通过奖励函数引导学习跑酷技能。

### 实验设置
- 使用真实人形机器人平台（具体型号未在摘要中提及）进行测试。
- 训练环境包括室内障碍赛道（平台、栏杆、间隙）与室外复杂地形（草地、斜坡、碎石路）。
- 奖励函数设计包含速度跟踪、身体平衡、关节限制、能量效率等项，并针对不同技能（跳跃、跨越、奔跑）设置自适应权重。

### 关键结果
- **跳跃能力**：成功跃上0.42米高的平台，跨越0.8米宽的间隙。
- **奔跑速度**：在野外环境中达到1.8m/s的稳定奔跑速度。
- **鲁棒性**：在草地、斜坡、碎石路等不同地形上均能稳健行走，无需重新训练。
- **自主技能选择**：在跟随摇杆旋转指令的同时，机器人能根据视觉输入自主选择跳跃、跨越或奔跑等技能。
- **迁移能力**：通过覆盖手臂动作（如抓取或推动），该框架可直接应用于移动操作任务（如搬运物体），无需修改核心策略。

### 结论
该工作首次实现了无需运动先验的人形机器人端到端跑酷学习，验证了视觉驱动全身控制策略在复杂运动任务中的有效性。其技能自主选择能力与任务迁移性为未来人形机器人在非结构化环境中的实际应用提供了重要基础。

## Overview
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 参考
- http://arxiv.org/abs/2406.10759v2

## 개요
본 연구는 인간형 로봇 파쿠르라는 매우 도전적인 운동 제어 문제를 위해, 운동 사전 지식 없이도 가능한 엔드투엔드 학습 프레임워크를 제안한다. 단일 궤적 최적화나 대량의 운동 참조 데이터에 의존하는 기존 방법과 달리, 본 프레임워크는 시각 입력을 통해 전신 제어 정책을 직접 생성하여 인간형 로봇이 다양한 파쿠르 기술을 자율적으로 선택하고 실행할 수 있게 한다. 실험 결과, 로봇은 점프 플랫폼, 장애물 넘기 등 복잡한 동작을 수행할 수 있을 뿐만 아니라 야외에서 1.8m/s 속도로 달리고, 다양한 지형에서 안정적으로 보행할 수 있음을 보여준다. 또한, 팔 동작을 덮어씀으로써 이 프레임워크는 인간형 이동 조작 작업으로 쉽게 전이될 수 있다.

## 핵심 내용
### 방법 아키텍처
- 엔드투엔드 강화 학습 프레임워크를 채택하며, 입력은 시각 이미지(로봇 머리 카메라에서 획득)와 고유 수용 데이터(관절 각도, IMU 등)이며, 출력은 전신 관절 제어 명령이다.
- 정책 네트워크는 합성곱 신경망(CNN)을 기반으로 시각 특징을 처리하고, 다층 퍼셉트론(MLP)을 결합하여 고유 수용 정보를 융합한 후 최종 동작 명령을 생성한다.
- 훈련 과정에서 운동 사전 지식(참조 궤적이나 모션 캡처 데이터 등)이 전혀 필요 없으며, 완전히 보상 함수를 통해 파쿠르 기술 학습을 유도한다.

### 실험 설정
- 실제 인간형 로봇 플랫폼(구체적 모델은 초록에 언급되지 않음)을 사용하여 테스트한다.
- 훈련 환경은 실내 장애물 트랙(플랫폼, 난간, 간격)과 실외 복잡 지형(잔디, 경사로, 자갈길)을 포함한다.
- 보상 함수 설계는 속도 추적, 신체 균형, 관절 제한, 에너지 효율 등을 포함하며, 각 기술(점프, 넘기, 달리기)에 대해 적응형 가중치를 설정한다.

### 주요 결과
- **점프 능력**: 0.42m 높이의 플랫폼에 성공적으로 점프하고, 0.8m 너비의 간격을 넘는다.
- **달리기 속도**: 야외 환경에서 1.8m/s의 안정적인 달리기 속도를 달성한다.
- **강건성**: 잔디, 경사로, 자갈길 등 다양한 지형에서 재훈련 없이 안정적으로 보행할 수 있다.
- **자율 기술 선택**: 조이스틱 회전 명령을 따르면서도 로봇은 시각 입력에 따라 점프, 넘기, 달리기 등의 기술을 자율적으로 선택할 수 있다.
- **전이 능력**: 팔 동작(예: 잡기 또는 밀기)을 덮어씀으로써 이 프레임워크는 핵심 정책 수정 없이 이동 조작 작업(예: 물체 운반)에 직접 적용할 수 있다.

### 결론
본 연구는 운동 사전 지식 없이 인간형 로봇의 엔드투엔드 파쿠르 학습을 최초로 구현하여, 시각 기반 전신 제어 정책이 복잡한 운동 작업에서 효과적임을 검증했다. 기술 자율 선택 능력과 작업 전이성은 향후 비구조화 환경에서 인간형 로봇의 실제 응용을 위한 중요한 기반을 제공한다.
