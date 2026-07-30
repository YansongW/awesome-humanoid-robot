---
$id: ent_paper_an_robotic_assistant_completing_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models'
  zh: Robotic Assistant
  ko: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models'
summary:
  en: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
  zh: Robotic Assistant 是 2025 年由 ETH Zurich、MIT、Stanford University 联合提出的大型视觉-语言-动作模型，用于灵巧的人机协作任务。其核心贡献在于通过 FiLM 条件化、辅助意图预测头与动作空间后处理，在最小语言提示下将预训练
    VLA 模型（Open-VLA）适配至灵巧操作，并实现约 0.3 秒延迟的实时长程行为组合。
  ko: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (Robotic Assistant),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by ETH Zurich, MIT, Stanford University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_assistant
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25713v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Robotic Assistant: Completing Collaborative Tasks with Dexterous Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.25713
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Robotic Assistant source
  url: https://doi.org/10.48550/arXiv.2510.25713
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该工作基于预训练的 Open-VLA 模型进行微调，使其能通过极少的语言指令完成灵巧的人机协作操作。研究者引入了三项关键改进：在视觉骨干网络中加入 FiLM 条件化以实现任务感知；增加辅助意图头来预测协作者的手部姿态与目标线索；以及通过动作空间后处理预测紧凑的增量（位置/旋转）与经 PCA 降维的手指关节，再映射为完整指令。实验采用多视角遥操作 Franka 与 Mimic-hand 数据集，并利用 MediaPipe 手部姿态进行增强，结果表明增量动作表现良好，四个主成分即可解释约 96% 的手部关节方差。消融实验显示动作后处理是性能提升的主要驱动因素，辅助意图头有一定帮助，FiLM 效果不一，而方向性运动损失则有害。整个系统在单张 RTX 4090 上可实现约 0.3 秒的实时延迟，并能将“拿起”与“传递”组合为长程行为。

## 核心内容
### 方法架构
- 基于预训练的 Open-VLA 模型进行适配，通过最小语言提示实现灵巧人机协作。
- **FiLM 条件化**：在视觉骨干网络中加入 FiLM 层，使模型能根据任务需求调整视觉特征提取。
- **辅助意图头**：额外预测协作者的手部姿态（通过 MediaPipe 提取）与目标线索，增强对协作意图的理解。
- **动作空间后处理**：预测紧凑的增量（位置/旋转）与经 PCA 降维的手指关节，再映射为完整指令。该方法避免了直接预测高维动作空间带来的不稳定性。

### 实验设置
- **数据集**：使用多视角遥操作 Franka 与 Mimic-hand 数据集，并利用 MediaPipe 手部姿态进行增强。
- **关键指标**：增量动作表现良好，四个主成分即可解释约 96% 的手部关节方差。
- **硬件**：单张 RTX 4090 实现约 0.3 秒的实时延迟。

### 消融实验与结论
- **动作后处理**：被识别为性能提升的主要驱动因素。
- **辅助意图头**：有一定帮助，但效果不如动作后处理显著。
- **FiLM 条件化**：效果不一，在某些任务中可能引入噪声。
- **方向性运动损失**：被证明有害，会降低模型性能。
- **主要局限**：模型存在“训练者过拟合”问题，即过度适应特定演示者的操作风格，导致泛化能力受限。

### 长程行为组合
- 系统能够将“拿起”与“传递”等原子动作组合为长程协作行为，展示了在真实场景中的实用性。

## Overview
We adapt a pre-trained Vision-Language-Action (VLA) model (Open-VLA) for dexterous human-robot collaboration with minimal language prompting. Our approach adds (i) FiLM conditioning to visual backbones for task-aware perception, (ii) an auxiliary intent head that predicts collaborator hand pose and target cues, and (iii) action-space post-processing that predicts compact deltas (position/rotation) and PCA-reduced finger joints before mapping to full commands. Using a multi-view, teleoperated Franka and Mimic-hand dataset augmented with MediaPipe hand poses, we demonstrate that delta actions are well-behaved and that four principal components explain ~96% of hand-joint variance. Ablations identify action post-processing as the primary performance driver; auxiliary intent helps, FiLM is mixed, and a directional motion loss is detrimental. A real-time stack (~0.3 s latency on one RTX 4090) composes "pick-up" and "pass" into a long-horizon behavior. We surface "trainer overfitting" to specific demonstrators as the key limitation.

## 개요
우리는 최소한의 언어 프롬프트로 정교한 인간-로봇 협업을 위해 사전 훈련된 Vision-Language-Action (VLA) 모델(Open-VLA)을 적용합니다. 우리의 접근 방식은 (i) 작업 인식 지각을 위한 시각적 백본에 FiLM 조건화 추가, (ii) 협업자 손 자세 및 대상 신호를 예측하는 보조 의도 헤드, (iii) 전체 명령으로 매핑하기 전에 압축된 델타(위치/회전) 및 PCA 축소 손가락 관절을 예측하는 행동 공간 후처리를 추가합니다. MediaPipe 손 자세로 증강된 다중 뷰, 원격 조작 Franka 및 Mimic-hand 데이터셋을 사용하여 델타 행동이 잘 작동하며 네 개의 주성분이 손 관절 분산의 약 96%를 설명함을 입증합니다. 절제 연구는 행동 후처리가 주요 성능 동인임을 식별합니다. 보조 의도는 도움이 되고, FiLM은 혼합적이며, 방향성 운동 손실은 해롭습니다. 실시간 스택(하나의 RTX 4090에서 약 0.3초 지연 시간)은 "집기"와 "전달"을 장기 행동으로 구성합니다. 우리는 특정 시연자에 대한 "훈련자 과적합"을 주요 한계로 제시합니다.

## 핵심 내용
우리는 최소한의 언어 프롬프트로 정교한 인간-로봇 협업을 위해 사전 훈련된 Vision-Language-Action (VLA) 모델(Open-VLA)을 적용합니다. 우리의 접근 방식은 (i) 작업 인식 지각을 위한 시각적 백본에 FiLM 조건화 추가, (ii) 협업자 손 자세 및 대상 신호를 예측하는 보조 의도 헤드, (iii) 전체 명령으로 매핑하기 전에 압축된 델타(위치/회전) 및 PCA 축소 손가락 관절을 예측하는 행동 공간 후처리를 추가합니다. MediaPipe 손 자세로 증강된 다중 뷰, 원격 조작 Franka 및 Mimic-hand 데이터셋을 사용하여 델타 행동이 잘 작동하며 네 개의 주성분이 손 관절 분산의 약 96%를 설명함을 입증합니다. 절제 연구는 행동 후처리가 주요 성능 동인임을 식별합니다. 보조 의도는 도움이 되고, FiLM은 혼합적이며, 방향성 운동 손실은 해롭습니다. 실시간 스택(하나의 RTX 4090에서 약 0.3초 지연 시간)은 "집기"와 "전달"을 장기 행동으로 구성합니다. 우리는 특정 시연자에 대한 "훈련자 과적합"을 주요 한계로 제시합니다.

## 参考
- http://arxiv.org/abs/2510.25713v1
