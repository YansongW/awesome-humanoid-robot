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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.23650v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (710 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.23650v2

## 개요
기존의 휴머노이드 로봇은 오디오에 대한 즉흥적 표현 능력이 부족하며, 전통적인 방법은 먼저 모션을 재구성한 후 로봇에 매핑해야 하므로 계단식 오류와 높은 지연 시간이 발생합니다. RoboPerform는 "모션 = 콘텐츠 + 스타일" 원칙을 기반으로 오디오를 암시적 스타일 신호로 직접 모션 생성을 구동하여 명시적 모션 재구성 단계를 제거합니다. 이 프레임워크는 다양한 모션 패턴에 적응하기 위한 ResMoE 교사 정책과 오디오 스타일 주입을 위한 확산 학생 정책을 포함하며, 최종적으로 리타게팅 없이 저지연 모션 제어를 달성합니다.

## 핵심 내용
### 핵심 문제
- 인간은 본능적으로 음악에 맞춰 움직일 수 있지만, 현재 휴머노이드 로봇은 즉흥적 표현 능력이 부족하여 사전 정의된 동작이나 희소 명령만 수행할 수 있습니다.
- 전통적인 오디오-로봇 모션 방법은 명시적 모션 재구성에 의존하여 계단식 오류, 높은 지연 시간 및 음향-모션 매핑의 비일관성을 초래합니다.

### 방법 아키텍처
- **설계 원칙**: "motion = content + style" 핵심 개념을 기반으로 오디오를 암시적 스타일 신호로 간주하여 명시적 모션 재구성이 필요 없습니다.
- **교사 정책**: ResMoE(Residual Mixture of Experts) 아키텍처를 채택하여 다양한 모션 패턴에 적응하고 기본 모션 콘텐츠를 제공합니다.
- **학생 정책**: 확산 기반(diffusion-based) 모델을 통해 오디오 스타일 주입을 구현하며, 오디오 특징을 모션 파라미터에 직접 매핑합니다.

### 주요 장점
- **리타게팅 없는 설계**: 로봇이 실행 가능한 모션 명령을 직접 생성하여 전통적인 방법의 모션 리타게팅 단계를 피합니다.
- **저지연**: 엔드투엔드 생성으로 중간 처리 단계를 줄입니다.
- **고충실도**: 오디오와 모션의 정렬 정확도가 높으며, 물리적 합리성이 기존 방법보다 우수합니다.

### 실험 검증
- 음악 기반 댄스와 음성 기반 제스처 두 가지 작업에서 검증되었으며, 물리적 합리성과 오디오 정렬 지표 모두 유망한 결과를 달성했습니다.
- 휴머노이드 로봇을 오디오에 반응하는 공연자로 성공적으로 전환하여 즉흥 모션 생성을 구현했습니다.
