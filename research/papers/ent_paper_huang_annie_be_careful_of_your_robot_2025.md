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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.03383v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
시각-언어-행동(VLA) 모델을 구현형 AI(EAI) 로봇에 통합함으로써 인간 중심 환경에서 복잡하고 장기적인 작업을 수행하는 능력이 빠르게 발전하고 있습니다. 그러나 EAI 시스템은 중요한 보안 위험을 초래합니다. 손상된 VLA 모델은 감각 입력에 대한 적대적 교란을 안전하지 않은 물리적 행동으로 직접 변환할 수 있습니다. 기계 학습 커뮤니티의 전통적인 안전 정의와 방법론은 더 이상 충분하지 않습니다. EAI 시스템은 안전이 무엇인지, 어떻게 측정할지, 물리적으로 기반을 둔 상호작용 환경에서 효과적인 공격 및 방어 메커니즘을 어떻게 설계할지와 같은 새로운 질문을 제기합니다. 본 연구에서는 인간-로봇 상호작용에 대한 ISO 표준에 기반하여 구현형 AI 시스템에 대한 적대적 안전 공격의 첫 번째 체계적 연구를 제시합니다. 우리는 (1) 분리 거리, 속도, 충돌 경계와 같은 물리적 제약 조건을 기반으로 안전 위반(심각, 위험, 위험성)의 원칙적 분류 체계를 공식화하고, (2) 구현형 안전 평가를 위한 2,400개의 비디오-행동 시퀀스를 포함한 9가지 안전 중요 시나리오의 벤치마크인 ANNIEBench를 소개하며, (3) 장기 목표를 프레임 수준 교란으로 분해하는 공격 리더 모델을 갖춘 작업 인식 적대적 프레임워크인 ANNIE-Attack을 소개합니다. 대표적인 EAI 모델에 대한 평가 결과, 모든 안전 범주에서 50%를 초과하는 공격 성공률을 보여줍니다. 또한 희소 및 적응형 공격 전략을 입증하고 물리적 로봇 실험을 통해 실제 세계 영향을 검증합니다. 이러한 결과는 구현형 AI 시스템에서 이전에 충분히 탐구되지 않았지만 매우 중요한 공격 표면을 드러내며, 물리적 AI 시대에 보안 중심 방어의 시급한 필요성을 강조합니다. 코드는 https://github.com/RLCLab/Annie에서 확인할 수 있습니다.

## 핵심 내용
시각-언어-행동(VLA) 모델을 구현형 AI(EAI) 로봇에 통합함으로써 인간 중심 환경에서 복잡하고 장기적인 작업을 수행하는 능력이 빠르게 발전하고 있습니다. 그러나 EAI 시스템은 중요한 보안 위험을 초래합니다. 손상된 VLA 모델은 감각 입력에 대한 적대적 교란을 안전하지 않은 물리적 행동으로 직접 변환할 수 있습니다. 기계 학습 커뮤니티의 전통적인 안전 정의와 방법론은 더 이상 충분하지 않습니다. EAI 시스템은 안전이 무엇인지, 어떻게 측정할지, 물리적으로 기반을 둔 상호작용 환경에서 효과적인 공격 및 방어 메커니즘을 어떻게 설계할지와 같은 새로운 질문을 제기합니다. 본 연구에서는 인간-로봇 상호작용에 대한 ISO 표준에 기반하여 구현형 AI 시스템에 대한 적대적 안전 공격의 첫 번째 체계적 연구를 제시합니다. 우리는 (1) 분리 거리, 속도, 충돌 경계와 같은 물리적 제약 조건을 기반으로 안전 위반(심각, 위험, 위험성)의 원칙적 분류 체계를 공식화하고, (2) 구현형 안전 평가를 위한 2,400개의 비디오-행동 시퀀스를 포함한 9가지 안전 중요 시나리오의 벤치마크인 ANNIEBench를 소개하며, (3) 장기 목표를 프레임 수준 교란으로 분해하는 공격 리더 모델을 갖춘 작업 인식 적대적 프레임워크인 ANNIE-Attack을 소개합니다. 대표적인 EAI 모델에 대한 평가 결과, 모든 안전 범주에서 50%를 초과하는 공격 성공률을 보여줍니다. 또한 희소 및 적응형 공격 전략을 입증하고 물리적 로봇 실험을 통해 실제 세계 영향을 검증합니다. 이러한 결과는 구현형 AI 시스템에서 이전에 충분히 탐구되지 않았지만 매우 중요한 공격 표면을 드러내며, 물리적 AI 시대에 보안 중심 방어의 시급한 필요성을 강조합니다. 코드는 https://github.com/RLCLab/Annie에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2509.03383v1
