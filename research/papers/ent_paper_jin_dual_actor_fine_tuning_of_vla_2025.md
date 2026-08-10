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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.13774v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (876 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.13774v1

## 개요
본 연구는 시각-언어-행동 모델이 복잡한 실제 환경에서 일반화 능력이 제한되는 문제를 해결하기 위해, 강화 학습 기반의 인간-로봇 협력 이중 에이전트 미세 조정 프레임워크를 제안한다. 프레임워크는 주 에이전트(다중 작업 강건 실행 담당)와 정밀 조정 에이전트(잠재 공간 적응 조정 담당)를 포함하며, 혁신적으로 경량화된 "대화-조정" 방식을 도입하여 인간의 수정 명령을 의미론적 언어 명령으로 변환해 훈련 데이터를 생성한다. 실제 다중 작업 실험에서, 이 방법은 101분 온라인 미세 조정 후 세 가지 작업에서 100% 성공률을 달성했으며, 장시간 작업에서는 연속 12회 조작에서 50% 성공률을 유지했다. 이중 로봇 협동 훈련 시 효율은 최대 2배 향상되었다.

## 핵심 내용
### 방법 아키텍처
- **이중 에이전트 프레임워크**: 주 에이전트(primary actor)는 사전 훈련된 VLA 모델을 통해 다중 작업 기본 능력을 구현하고, 정밀 조정 에이전트(refinement actor)는 잠재 공간에서 국소 정책 조정을 수행하며, 두 에이전트는 공유 가치 네트워크를 통해 협력 최적화된다.
- **대화-조정 메커니즘**: 인간의 물리적 개입(예: 로봇 팔 궤적 수정)을 경량 언어 모델을 통해 구조화된 명령(예: "빨간 블록을 왼쪽으로 5cm 이동")으로 변환하여, 의미론적으로 정렬된 수정 데이터 세트를 구축해 정책 학습에 사용한다.

### 실험 설정
- **작업 시나리오**: 3가지 기본 조작 작업(잡기, 놓기, 쌓기)과 1가지 장시간 작업(12단계 연속 조작)을 포함한다.
- **훈련 구성**: 단일 UR5 로봇 팔을 사용해 101분 온라인 미세 조정을 수행했으며, 이중 로봇 실험은 두 대의 UR5 협동 작업을 사용했다.
- **비교 기준선**: 표준 지도 미세 조정(SFT), 순수 강화 학습(RL) 및 단일 에이전트 방법과 비교했다.

### 주요 결과
- **다중 작업 성능**: 세 가지 기본 작업 모두 100% 성공률을 달성했으며, SFT 기준선의 평균 성공률은 67%에 불과했다.
- **장시간 작업**: 연속 12회 조작에서 50% 성공률을 유지하여, RL 방법의 12% 성공률보다 크게 우수했다.
- **다중 로봇 확장**: 이중 로봇 협동 훈련 시 정책 수렴 속도가 2배 향상되었다(202분에서 101분으로 단축).
- **절제 실험**: 대화-조정 메커니즘을 제거하면 성공률이 78%로 하락하여, 의미 명령 생성 모듈의 유효성을 검증했다.

### 결론
본 연구는 인간의 언어 수정과 이중 에이전트 강화 학습을 처음으로 결합하여, 실제 로봇 조작에서 효율적인 미세 조정을 구현했으며, VLA 모델의 복잡한 산업 환경 배포를 위한 확장 가능한 솔루션을 제공한다. 실험 비디오와 코드는 오픈소스로 공개되었다.
