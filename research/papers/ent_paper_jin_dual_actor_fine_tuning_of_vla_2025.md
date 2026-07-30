---
$id: ent_paper_jin_dual_actor_fine_tuning_of_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach'
  zh: Dual-Actor Fine-Tuning of VLA Models
  ko: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach'
summary:
  en: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
  zh: 香港城市大学与北京小米机器人技术有限公司联合提出了一种名为Dual-Actor Fine-Tuning of VLA Models的人机协同微调框架，通过双智能体架构与“对话-调整”机制，在101分钟内实现三项操作任务100%成功率，并支持多机器人协同训练效率提升2倍。
  ko: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (Dual-Actor Fine-Tuning of VLA Models),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by City University of Hong Kong, Beijing
    Xiaomi Robot Technology Co., Ltd..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_actor_fine_tuning_of_vla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13774v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Dual-Actor Fine-Tuning of VLA Models: A Talk-and-Tweak Human-in-the-Loop Approach (arXiv)'
  url: https://arxiv.org/abs/2509.13774
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dual-Actor Fine-Tuning of VLA Models source
  url: https://doi.org/10.48550/arXiv.2509.13774
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对视觉-语言-动作模型在复杂真实场景中泛化能力受限的问题，提出基于强化学习的人机协同双智能体微调框架。框架包含主智能体（负责多任务鲁棒执行）与精调智能体（负责潜在空间适应性调整），并创新性地引入轻量级“对话-调整”方案，将人类修正指令转化为语义化语言命令以生成训练数据。在真实多任务实验中，该方法在101分钟在线微调后实现三项任务100%成功率；在长时域任务中，连续12次操作保持50%成功率。双机器人协同训练时效率提升达2倍。

## 核心内容
### 方法架构
- **双智能体框架**：主智能体（primary actor）通过预训练VLA模型实现多任务基础能力，精调智能体（refinement actor）在潜在空间进行局部策略调整，两者通过共享价值网络协同优化。
- **对话-调整机制**：将人类物理干预（如纠正机械臂轨迹）通过轻量级语言模型转化为结构化指令（如“将红色方块向左移动5厘米”），构建语义对齐的修正数据集用于策略学习。

### 实验设置
- **任务场景**：包含3项基础操作任务（抓取、放置、堆叠）与1项长时域任务（12步连续操作）。
- **训练配置**：使用单台UR5机械臂进行101分钟在线微调，双机器人实验采用两台UR5协同作业。
- **对比基线**：与标准监督微调（SFT）、纯强化学习（RL）及单智能体方法进行对比。

### 关键结果
- **多任务性能**：三项基础任务均达100%成功率，而SFT基线平均成功率仅67%。
- **长时域任务**：连续12次操作保持50%成功率，显著优于RL方法的12%成功率。
- **多机器人扩展**：双机器人协同训练时，策略收敛速度提升2倍（从202分钟缩短至101分钟）。
- **消融实验**：移除对话-调整机制后，成功率下降至78%，验证了语义指令生成模块的有效性。

### 结论
该工作首次将人类语言修正与双智能体强化学习结合，在真实机器人操作中实现高效微调，为VLA模型在复杂工业场景的部署提供了可扩展方案。实验视频与代码已开源。

## Overview
Vision-language-action (VLA) models demonstrate strong generalization in robotic manipulation but face challenges in complex, real-world tasks. While supervised fine-tuning with demonstrations is constrained by data quality, reinforcement learning (RL) offers a promising alternative. We propose a human-in-the-loop dual-actor fine-tuning framework grounded in RL. The framework integrates a primary actor for robust multi-task performance with a refinement actor for latent-space adaptation. Beyond standard physical interventions, we introduce a lightweight talk-and-tweak scheme that converts human corrections into semantically grounded language commands, thereby generating a new dataset for policy learning. In real-world multi-task experiments, our approach achieves 100% success across three tasks within 101 minutes of online fine-tuning. For long-horizon tasks, it sustains a 50% success rate over 12 consecutive operations. Furthermore, the framework scales effectively to multi-robot training, achieving up to a 2 times improvement in efficiency when using dual robots. The experiment videos are available at https://sites.google.com/view/hil-daft/.

## 개요
Vision-language-action (VLA) 모델은 로봇 조작에서 강력한 일반화 능력을 보여주지만, 복잡한 실제 작업에서는 어려움에 직면합니다. 시연 데이터를 통한 지도 미세 조정은 데이터 품질에 제약을 받는 반면, 강화 학습(RL)은 유망한 대안을 제시합니다. 우리는 RL에 기반한 인간-루프 이중 행동자 미세 조정 프레임워크를 제안합니다. 이 프레임워크는 강력한 다중 작업 성능을 위한 기본 행동자와 잠재 공간 적응을 위한 정제 행동자를 통합합니다. 표준적인 물리적 개입 외에도, 우리는 인간의 교정을 의미적으로 기반한 언어 명령으로 변환하여 정책 학습을 위한 새로운 데이터셋을 생성하는 경량의 talk-and-tweak 방식을 도입합니다. 실제 다중 작업 실험에서, 우리의 접근 방식은 101분의 온라인 미세 조정 내에 세 가지 작업에서 100% 성공률을 달성합니다. 장기 작업의 경우, 12회 연속 작업에서 50%의 성공률을 유지합니다. 또한, 이 프레임워크는 다중 로봇 훈련으로 효과적으로 확장되어, 이중 로봇 사용 시 최대 2배의 효율성 향상을 달성합니다. 실험 비디오는 https://sites.google.com/view/hil-daft/에서 확인할 수 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 로봇 조작에서 강력한 일반화 능력을 보여주지만, 복잡한 실제 작업에서는 어려움에 직면합니다. 시연 데이터를 통한 지도 미세 조정은 데이터 품질에 제약을 받는 반면, 강화 학습(RL)은 유망한 대안을 제시합니다. 우리는 RL에 기반한 인간-루프 이중 행동자 미세 조정 프레임워크를 제안합니다. 이 프레임워크는 강력한 다중 작업 성능을 위한 기본 행동자와 잠재 공간 적응을 위한 정제 행동자를 통합합니다. 표준적인 물리적 개입 외에도, 우리는 인간의 교정을 의미적으로 기반한 언어 명령으로 변환하여 정책 학습을 위한 새로운 데이터셋을 생성하는 경량의 talk-and-tweak 방식을 도입합니다. 실제 다중 작업 실험에서, 우리의 접근 방식은 101분의 온라인 미세 조정 내에 세 가지 작업에서 100% 성공률을 달성합니다. 장기 작업의 경우, 12회 연속 작업에서 50%의 성공률을 유지합니다. 또한, 이 프레임워크는 다중 로봇 훈련으로 효과적으로 확장되어, 이중 로봇 사용 시 최대 2배의 효율성 향상을 달성합니다. 실험 비디오는 https://sites.google.com/view/hil-daft/에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2509.13774v1
