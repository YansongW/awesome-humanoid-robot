---
$id: ent_paper_do_you_have_freestyle_expressi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
  zh: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
  ko: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control
summary:
  en: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control is a 2025 work on locomotion for humanoid robots.
  zh: RoboPerform 是首个统一音频-运动框架，由研究者提出用于人形机器人直接生成音乐驱动舞蹈和语音驱动手势。其核心创新在于将音频视为隐式风格信号，无需显式运动重建，通过 ResMoE 教师策略和扩散学生策略实现低延迟高保真运动生成。
  ko: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- do_you_have_freestyle_expressi
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23650v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Do You Have Freestyle? Expressive Humanoid Locomotion via Audio Control (arXiv)
  url: https://arxiv.org/abs/2512.23650
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的人形机器人缺乏对音频的即兴表达能力，传统方法需先重建运动再映射到机器人，导致级联误差和高延迟。RoboPerform 基于“运动=内容+风格”原则，将音频作为隐式风格信号直接驱动运动生成，消除了显式运动重建步骤。该框架包含 ResMoE 教师策略以适应多样运动模式，以及扩散学生策略用于注入音频风格，最终实现无需重定向的低延迟运动控制。

## 核心内容
### 核心问题
- 人类能本能地随音乐律动，但当前人形机器人缺乏即兴表达能力，仅能执行预定义动作或稀疏指令。
- 传统音频到机器人运动的方法依赖显式运动重建，导致级联误差、高延迟和声学-运动映射不连贯。

### 方法架构
- **设计原则**：基于“motion = content + style”核心理念，将音频视为隐式风格信号，无需显式运动重建。
- **教师策略**：采用 ResMoE（Residual Mixture of Experts）架构，适应多样化的运动模式，提供基础运动内容。
- **学生策略**：基于扩散模型（diffusion-based）实现音频风格注入，将音频特征直接映射到运动参数。

### 关键优势
- **无重定向设计**：直接生成机器人可执行的运动指令，避免传统方法中的运动重定向步骤。
- **低延迟**：端到端生成，减少中间处理环节。
- **高保真**：音频与运动对齐精度高，物理合理性优于现有方法。

### 实验验证
- 在音乐驱动舞蹈和语音驱动手势两类任务上验证，物理合理性和音频对齐指标均达到 promising 结果。
- 成功将人形机器人转化为能响应音频的表演者，实现即兴运动生成。

## Overview
Humans intuitively move to sound, but current humanoid robots lack expressive improvisational capabilities, confined to predefined motions or sparse commands. Generating motion from audio and then retargeting it to robots relies on explicit motion reconstruction, leading to cascaded errors, high latency, and disjointed acoustic-actuation mapping. We propose RoboPerform, the first unified audio-to-locomotion framework that can directly generate music-driven dance and speech-driven co-speech gestures from audio. Guided by the core principle of "motion = content + style", the framework treats audio as implicit style signals and eliminates the need for explicit motion reconstruction. RoboPerform integrates a ResMoE teacher policy for adapting to diverse motion patterns and a diffusion-based student policy for audio style injection. This retargeting-free design ensures low latency and high fidelity. Experimental validation shows that RoboPerform achieves promising results in physical plausibility and audio alignment, successfully transforming robots into responsive performers capable of reacting to audio.

## 개요
인간은 본능적으로 소리에 맞춰 움직이지만, 현재의 휴머노이드 로봇은 표현력 있는 즉흥적 능력이 부족하여 사전 정의된 동작이나 단편적인 명령에 제한되어 있습니다. 오디오로부터 동작을 생성한 후 로봇에 재타겟팅하는 방식은 명시적인 동작 재구성에 의존하여, 연쇄 오류, 높은 지연 시간, 그리고 분리된 음향-구동 매핑을 초래합니다. 우리는 오디오로부터 음악 기반 춤과 음성 기반 동반 제스처를 직접 생성할 수 있는 최초의 통합 오디오-운동 프레임워크인 RoboPerform을 제안합니다. "동작 = 내용 + 스타일"이라는 핵심 원칙에 따라, 이 프레임워크는 오디오를 암시적 스타일 신호로 처리하며 명시적 동작 재구성을 필요로 하지 않습니다. RoboPerform은 다양한 동작 패턴에 적응하기 위한 ResMoE 교사 정책과 오디오 스타일 주입을 위한 확산 기반 학생 정책을 통합합니다. 이 재타겟팅 없는 설계는 낮은 지연 시간과 높은 충실도를 보장합니다. 실험적 검증을 통해 RoboPerform이 물리적 타당성과 오디오 정렬에서 유망한 결과를 달성하여, 로봇을 오디오에 반응하는 표현력 있는 수행자로 성공적으로 변환함을 보여줍니다.

## 핵심 내용
인간은 본능적으로 소리에 맞춰 움직이지만, 현재의 휴머노이드 로봇은 표현력 있는 즉흥적 능력이 부족하여 사전 정의된 동작이나 단편적인 명령에 제한되어 있습니다. 오디오로부터 동작을 생성한 후 로봇에 재타겟팅하는 방식은 명시적인 동작 재구성에 의존하여, 연쇄 오류, 높은 지연 시간, 그리고 분리된 음향-구동 매핑을 초래합니다. 우리는 오디오로부터 음악 기반 춤과 음성 기반 동반 제스처를 직접 생성할 수 있는 최초의 통합 오디오-운동 프레임워크인 RoboPerform을 제안합니다. "동작 = 내용 + 스타일"이라는 핵심 원칙에 따라, 이 프레임워크는 오디오를 암시적 스타일 신호로 처리하며 명시적 동작 재구성을 필요로 하지 않습니다. RoboPerform은 다양한 동작 패턴에 적응하기 위한 ResMoE 교사 정책과 오디오 스타일 주입을 위한 확산 기반 학생 정책을 통합합니다. 이 재타겟팅 없는 설계는 낮은 지연 시간과 높은 충실도를 보장합니다. 실험적 검증을 통해 RoboPerform이 물리적 타당성과 오디오 정렬에서 유망한 결과를 달성하여, 로봇을 오디오에 반응하는 표현력 있는 수행자로 성공적으로 변환함을 보여줍니다.

## 参考
- http://arxiv.org/abs/2512.23650v2
