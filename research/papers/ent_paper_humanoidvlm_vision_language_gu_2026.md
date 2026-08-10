---
$id: ent_paper_humanoidvlm_vision_language_gu_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
  zh: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
  ko: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation'
summary:
  en: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
  zh: HumanoidVLM 是2026年提出的一种面向人形机器人的视觉-语言引导阻抗控制框架。该系统由团队开发，核心贡献在于利用视觉语言模型与检索增强生成模块，使 Unitree G1 人形机器人能够从单张 RGB 图像中自主选择任务适配的笛卡尔阻抗参数与夹爪配置，在接触丰富的操作任务中实现93%的检索准确率。
  ko: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation is a 2026 work on manipulation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoidvlm
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.14874v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (779 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'HumanoidVLM: Vision-Language-Guided Impedance Control for Contact-Rich Humanoid Manipulation (arXiv)'
  url: https://arxiv.org/abs/2601.14874
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
HumanoidVLM 通过耦合视觉语言模型与基于 FAISS 的检索增强生成模块，解决了人形机器人接触行为自适应问题。系统从两个定制数据库中检索经过实验验证的刚度-阻尼对和物体特定抓取角度，并通过任务空间阻抗控制器执行。在14个视觉场景的测试中，系统达到93%的检索准确率，实际实验中z轴跟踪误差控制在1-3.5厘米范围内，虚拟力与任务依赖的阻抗设置保持一致。

## 核心内容
### 方法架构
HumanoidVLM 采用双模块协同架构：
- **视觉语言推理模块**：通过视觉语言模型从单目 RGB 图像中推断任务语义（如"抓取易碎玻璃杯"或"拧紧金属螺栓"）
- **检索增强生成模块**：基于 FAISS 构建的 RAG 系统，从两个专用数据库中检索：
  - 阻抗参数库：存储不同任务场景下实验验证的刚度-阻尼组合
  - 抓取角度库：包含物体特定的最优夹爪角度配置

### 实验设置
- **硬件平台**：Unitree G1 人形机器人
- **感知输入**：单目 RGB 图像（无深度信息）
- **控制器**：任务空间阻抗控制器
- **测试场景**：14种视觉操作场景（包含不同材质、形状和任务要求的物体）

### 关键实验结果
- **检索准确率**：在14个视觉场景中达到93%
- **跟踪误差**：z轴方向跟踪误差稳定在1-3.5厘米范围内
- **力控表现**：虚拟力输出与任务依赖的阻抗设置保持一致性
- **交互稳定性**：实际实验中展现出稳定的交互动力学特性

### 结论
HumanoidVLM 验证了将语义感知与检索式控制相结合作为可解释路径的可行性，为人形机器人在接触丰富操作任务中的自适应控制提供了新范式。该方法避免了传统固定阻抗增益和手动调参的局限性，通过视觉语言理解直接驱动控制参数选择。

## Overview
Humanoid robots must adapt their contact behavior to diverse objects and tasks, yet most controllers rely on fixed, hand-tuned impedance gains and gripper settings. This paper introduces HumanoidVLM, a vision-language driven retrieval framework that enables the Unitree G1 humanoid to select task-appropriate Cartesian impedance parameters and gripper configurations directly from an egocentric RGB image. The system couples a vision-language model for semantic task inference with a FAISS-based Retrieval-Augmented Generation (RAG) module that retrieves experimentally validated stiffness-damping pairs and object-specific grasp angles from two custom databases, and executes them through a task-space impedance controller for compliant manipulation. We evaluate HumanoidVLM on 14 visual scenarios and achieve a retrieval accuracy of 93%. Real-world experiments show stable interaction dynamics, with z-axis tracking errors typically within 1-3.5 cm and virtual forces consistent with task-dependent impedance settings. These results demonstrate the feasibility of linking semantic perception with retrieval-based control as an interpretable path toward adaptive humanoid manipulation.

## 参考
- http://arxiv.org/abs/2601.14874v1

## 개요
HumanoidVLM은 비전-언어 모델과 FAISS 기반 검색 증강 생성 모듈을 결합하여 휴머노이드 로봇의 접촉 행동 적응 문제를 해결합니다. 시스템은 두 개의 맞춤형 데이터베이스에서 실험적으로 검증된 강성-감쇠 쌍과 객체별 파지 각도를 검색하며, 이를 작업 공간 임피던스 제어기를 통해 실행합니다. 14개의 시각적 장면 테스트에서 시스템은 93%의 검색 정확도를 달성했으며, 실제 실험에서 z축 추적 오차는 1-3.5cm 범위 내로 제어되었고, 가상 힘은 작업 의존적 임피던스 설정과 일관성을 유지했습니다.

## 핵심 내용
### 방법 아키텍처
HumanoidVLM은 이중 모듈 협력 아키텍처를 채택합니다:
- **비전-언어 추론 모듈**: 비전-언어 모델을 통해 단안 RGB 이미지에서 작업 의미론을 추론합니다 (예: "깨지기 쉬운 유리컵 잡기" 또는 "금속 볼트 조이기")
- **검색 증강 생성 모듈**: FAISS 기반 RAG 시스템으로, 두 개의 전용 데이터베이스에서 검색합니다:
  - 임피던스 파라미터 라이브러리: 다양한 작업 시나리오에서 실험적으로 검증된 강성-감쇠 조합 저장
  - 파지 각도 라이브러리: 객체별 최적 그리퍼 각도 구성 포함

### 실험 설정
- **하드웨어 플랫폼**: Unitree G1 휴머노이드 로봇
- **지각 입력**: 단안 RGB 이미지 (깊이 정보 없음)
- **제어기**: 작업 공간 임피던스 제어기
- **테스트 시나리오**: 14가지 시각적 조작 장면 (다양한 재질, 형태 및 작업 요구사항을 가진 객체 포함)

### 주요 실험 결과
- **검색 정확도**: 14개의 시각적 장면에서 93% 달성
- **추적 오차**: z축 방향 추적 오차가 1-3.5cm 범위 내에서 안정적으로 유지
- **힘 제어 성능**: 가상 힘 출력이 작업 의존적 임피던스 설정과 일관성 유지
- **상호작용 안정성**: 실제 실험에서 안정적인 상호작용 동역학 특성 입증

### 결론
HumanoidVLM은 의미론적 인식과 검색 기반 제어를 결합한 해석 가능한 경로의 실현 가능성을 검증했으며, 접촉이 풍부한 조작 작업에서 휴머노이드 로봇의 적응형 제어를 위한 새로운 패러다임을 제시합니다. 이 방법은 기존의 고정 임피던스 이득과 수동 파라미터 튜닝의 한계를 극복하고, 비전-언어 이해를 통해 제어 파라미터 선택을 직접 구동합니다.
