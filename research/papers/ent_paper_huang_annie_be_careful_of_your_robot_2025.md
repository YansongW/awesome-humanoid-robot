---
$id: ent_paper_huang_annie_be_careful_of_your_robot_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ANNIE: Be Careful of Your Robots'
  zh: ANNIE
  ko: 'ANNIE: Be Careful of Your Robots'
summary:
  en: 'ANNIE: Be Careful of Your Robots (ANNIE), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Institute of Automation, Chinese Academy of Sciences, Georgia Institute of Technology, University of Texas at Dallas,
    Institute of Computing Technology, Chinese Academy of Sciences.'
  zh: ANNIE 是由中国科学院自动化研究所、佐治亚理工学院、德克萨斯大学达拉斯分校及中国科学院计算技术研究所于2025年提出的大型视觉-语言-动作模型，专注于机器人操作。其核心贡献在于首次系统性地研究了具身AI系统的对抗性安全攻击，基于ISO人机交互标准定义了安全违规分类，并发布了包含9个安全关键场景的ANNIEBench基准和任务感知的ANNIE-Attack攻击框架。实验表明，攻击成功率在所有安全类别中均超过50%，并通过物理机器人实验验证了实际影响。
  ko: 'ANNIE: Be Careful of Your Robots (ANNIE), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by Institute of Automation, Chinese Academy of Sciences, Georgia Institute of Technology, University of Texas at Dallas,
    Institute of Computing Technology, Chinese Academy of Sciences.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- annie
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.03383v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (753 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ANNIE: Be Careful of Your Robots (arXiv)'
  url: https://arxiv.org/abs/2509.03383
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ANNIE source
  url: https://doi.org/10.48550/arXiv.2509.03383
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
ANNIE 针对具身AI系统在人类环境中执行复杂长时任务时面临的安全风险，提出了首个系统性的对抗性安全攻击研究。该工作基于ISO人机交互标准，将安全违规形式化为关键、危险、风险三个等级，并依据分离距离、速度、碰撞边界等物理约束进行定义。为评估具身安全，研究团队构建了包含9个安全关键场景、2400个视频-动作序列的ANNIEBench基准。此外，还提出了ANNIE-Attack任务感知对抗框架，通过攻击领导者模型将长时目标分解为帧级扰动。在代表性具身AI模型上的评估显示，攻击成功率在所有安全类别中均超过50%，并通过物理机器人实验验证了实际威胁。

## 核心内容
### 方法
- **安全违规分类**：基于ISO人机交互标准，依据物理约束（分离距离、速度、碰撞边界）将安全违规形式化为三个等级：关键（Critical）、危险（Dangerous）、风险（Risky）。
- **ANNIE-Attack框架**：任务感知的对抗攻击框架，包含攻击领导者模型，可将长时目标分解为帧级扰动，实现稀疏和自适应攻击策略。

### 实验设置
- **基准**：ANNIEBench包含9个安全关键场景，共2400个视频-动作序列，用于评估具身安全。
- **评估模型**：覆盖代表性具身AI模型。
- **实验验证**：除仿真评估外，还通过物理机器人实验验证实际影响。

### 关键数字
- 攻击成功率在所有安全类别中均超过50%。
- 基准包含9个场景、2400个视频-动作序列。

### 结论
- 该工作揭示了具身AI系统中此前未被充分探索但后果严重的攻击面，强调了在物理AI时代迫切需要安全驱动的防御机制。
- 代码已开源：https://github.com/RLCLab/Annie

## Overview
The integration of vision-language-action (VLA) models into embodied AI (EAI) robots is rapidly advancing their ability to perform complex, long-horizon tasks in humancentric environments. However, EAI systems introduce critical security risks: a compromised VLA model can directly translate adversarial perturbations on sensory input into unsafe physical actions. Traditional safety definitions and methodologies from the machine learning community are no longer sufficient. EAI systems raise new questions, such as what constitutes safety, how to measure it, and how to design effective attack and defense mechanisms in physically grounded, interactive settings. In this work, we present the first systematic study of adversarial safety attacks on embodied AI systems, grounded in ISO standards for human-robot interactions. We (1) formalize a principled taxonomy of safety violations (critical, dangerous, risky) based on physical constraints such as separation distance, velocity, and collision boundaries; (2) introduce ANNIEBench, a benchmark of nine safety-critical scenarios with 2,400 video-action sequences for evaluating embodied safety; and (3) ANNIE-Attack, a task-aware adversarial framework with an attack leader model that decomposes long-horizon goals into frame-level perturbations. Our evaluation across representative EAI models shows attack success rates exceeding 50% across all safety categories. We further demonstrate sparse and adaptive attack strategies and validate the real-world impact through physical robot experiments. These results expose a previously underexplored but highly consequential attack surface in embodied AI systems, highlighting the urgent need for security-driven defenses in the physical AI era. Code is available at https://github.com/RLCLab/Annie.

## 参考
- http://arxiv.org/abs/2509.03383v1

## 개요
ANNIE는 인간 환경에서 복잡한 장기 과제를 수행하는 구현형 AI 시스템이 직면하는 안전 위험에 대해 최초의 체계적인 적대적 안전 공격 연구를 제안한다. 이 연구는 ISO 인간-로봇 상호작용 표준을 기반으로 안전 위반을 중요(Critical), 위험(Dangerous), 위험(Risky)의 세 등급으로 형식화하고, 분리 거리, 속도, 충돌 경계 등의 물리적 제약에 따라 정의한다. 구현형 안전을 평가하기 위해 연구팀은 9개의 안전 핵심 시나리오와 2400개의 비디오-행동 시퀀스를 포함하는 ANNIEBench 벤치마크를 구축했다. 또한, 장기 목표를 프레임 수준의 교란으로 분해하는 리더 모델을 공격하는 ANNIE-Attack 작업 인식 적대적 프레임워크를 제안한다. 대표적인 구현형 AI 모델에 대한 평가는 모든 안전 범주에서 공격 성공률이 50%를 초과함을 보여주며, 물리적 로봇 실험을 통해 실제 위협을 검증한다.

## 핵심 내용
### 방법
- **안전 위반 분류**: ISO 인간-로봇 상호작용 표준을 기반으로 물리적 제약(분리 거리, 속도, 충돌 경계)에 따라 안전 위반을 세 등급으로 형식화: 중요(Critical), 위험(Dangerous), 위험(Risky).
- **ANNIE-Attack 프레임워크**: 작업 인식 적대적 공격 프레임워크로, 리더 모델을 공격하여 장기 목표를 프레임 수준의 교란으로 분해하고, 희소 및 적응형 공격 전략을 구현한다.

### 실험 설정
- **벤치마크**: ANNIEBench는 9개의 안전 핵심 시나리오와 총 2400개의 비디오-행동 시퀀스를 포함하여 구현형 안전을 평가한다.
- **평가 모델**: 대표적인 구현형 AI 모델을 포괄한다.
- **실험 검증**: 시뮬레이션 평가 외에도 물리적 로봇 실험을 통해 실제 영향을 검증한다.

### 핵심 수치
- 모든 안전 범주에서 공격 성공률이 50%를 초과한다.
- 벤치마크는 9개 시나리오와 2400개의 비디오-행동 시퀀스를 포함한다.

### 결론
- 이 연구는 구현형 AI 시스템에서 이전에 충분히 탐구되지 않았지만 심각한 결과를 초래하는 공격 표면을 드러내며, 물리적 AI 시대에 안전 중심의 방어 메커니즘이 시급히 필요함을 강조한다.
- 코드는 오픈소스로 공개됨: https://github.com/RLCLab/Annie
