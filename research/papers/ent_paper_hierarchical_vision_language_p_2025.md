---
$id: ent_paper_hierarchical_vision_language_p_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  zh: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
  ko: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation
summary:
  en: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
  zh: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation 是2025年提出的人形机器人操作框架，由三层结构组成：底层RL控制器、中层模仿学习技能策略、高层视觉语言规划模块。在Unitree
    G1人形机器人上执行非抓取式拾放任务，40次真实实验达到73%成功率。
  ko: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation is a 2025 work on manipulation for humanoid
    robots.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hierarchical_vision_language_p
- humanoid
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.22827v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (627 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Hierarchical Vision-Language Planning for Multi-Step Humanoid Manipulation (arXiv)
  url: https://arxiv.org/abs/2506.22827
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对人形机器人在工业和家庭环境中执行复杂多步操作任务的可靠性问题，提出分层规划与控制框架。系统底层采用基于强化学习的控制器追踪全身运动目标；中层通过模仿学习训练技能策略，为任务不同步骤生成运动目标；高层利用预训练视觉语言模型（VLMs）实时规划技能执行顺序并监控完成状态。在Unitree G1人形机器人上验证非抓取式拾放任务，40次真实世界实验显示完整操作序列成功率达73%，证实了基于VLM的技能规划与监控在多步操作场景中的有效性。

## 核心内容
### 方法架构
- **三层分层系统**：
  - **底层**：基于强化学习的控制器，负责追踪全身运动目标
  - **中层**：通过模仿学习训练的多个技能策略，为任务不同步骤生成运动目标
  - **高层**：视觉语言规划模块，使用预训练VLM决定技能执行顺序并实时监控完成状态

### 实验设置
- **机器人平台**：Unitree G1人形机器人
- **任务类型**：非抓取式拾放任务（non-prehensile pick-and-place）
- **实验规模**：40次真实世界试验

### 关键结果
- **完整操作序列成功率**：73%
- **验证结论**：分层系统在真实环境中具备可行性，VLM技能规划与监控对多步操作场景有显著提升效果

### 附加信息
- 策略演示视频见项目主页：https://vlp-humanoid.github.io/

## Overview
Enabling humanoid robots to reliably execute complex multi-step manipulation tasks is crucial for their effective deployment in industrial and household environments. This paper presents a hierarchical planning and control framework designed to achieve reliable multi-step humanoid manipulation. The proposed system comprises three layers: (1) a low-level RL-based controller responsible for tracking whole-body motion targets; (2) a mid-level set of skill policies trained via imitation learning that produce motion targets for different steps of a task; and (3) a high-level vision-language planning module that determines which skills should be executed and also monitors their completion in real-time using pretrained vision-language models (VLMs). Experimental validation is performed on a Unitree G1 humanoid robot executing a non-prehensile pick-and-place task. Over 40 real-world trials, the hierarchical system achieved a 73% success rate in completing the full manipulation sequence. These experiments confirm the feasibility of the proposed hierarchical system, highlighting the benefits of VLM-based skill planning and monitoring for multi-step manipulation scenarios. See https://vlp-humanoid.github.io/ for video demonstrations of the policy rollout.

## 参考
- http://arxiv.org/abs/2506.22827v3

## 개요
이 연구는 산업 및 가정 환경에서 휴머노이드 로봇이 복잡한 다단계 조작 작업을 수행할 때의 신뢰성 문제를 해결하기 위해 계층적 계획 및 제어 프레임워크를 제안한다. 시스템의 하위 계층은 강화 학습 기반 컨트롤러를 사용하여 전신 운동 목표를 추적하고, 중간 계층은 모방 학습을 통해 훈련된 스킬 정책을 사용하여 작업의 각 단계에 대한 운동 목표를 생성하며, 상위 계층은 사전 훈련된 비전-언어 모델(VLM)을 활용하여 스킬 실행 순서를 실시간으로 계획하고 완료 상태를 모니터링한다. Unitree G1 휴머노이드 로봇에서 비파지형 픽앤플레이스 작업을 검증했으며, 40회의 실제 세계 실험에서 전체 조작 시퀀스 성공률이 73%에 달해 VLM 기반 스킬 계획 및 모니터링이 다단계 조작 시나리오에서 효과적임을 확인했다.

## 핵심 내용
### 방법 아키텍처
- **3계층 계층적 시스템**:
  - **하위 계층**: 강화 학습 기반 컨트롤러로 전신 운동 목표 추적 담당
  - **중간 계층**: 모방 학습으로 훈련된 여러 스킬 정책으로 작업의 각 단계에 대한 운동 목표 생성
  - **상위 계층**: 비전-언어 계획 모듈로 사전 훈련된 VLM을 사용하여 스킬 실행 순서 결정 및 실시간 완료 상태 모니터링

### 실험 설정
- **로봇 플랫폼**: Unitree G1 휴머노이드 로봇
- **작업 유형**: 비파지형 픽앤플레이스 작업(non-prehensile pick-and-place)
- **실험 규모**: 40회의 실제 세계 시험

### 주요 결과
- **전체 조작 시퀀스 성공률**: 73%
- **검증 결론**: 계층적 시스템이 실제 환경에서 실현 가능하며, VLM 스킬 계획 및 모니터링이 다단계 조작 시나리오에서 상당한 성능 향상을 제공

### 추가 정보
- 정책 시연 비디오는 프로젝트 홈페이지에서 확인 가능: https://vlp-humanoid.github.io/
