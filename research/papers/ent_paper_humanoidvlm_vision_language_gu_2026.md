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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2601.14874v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
휴머노이드 로봇은 다양한 물체와 작업에 맞춰 접촉 행동을 적응시켜야 하지만, 대부분의 제어기는 고정되고 수동으로 조정된 임피던스 게인과 그리퍼 설정에 의존합니다. 본 논문에서는 Unitree G1 휴머노이드가 1인칭 RGB 이미지에서 직접 작업에 적합한 직교 임피던스 매개변수와 그리퍼 구성을 선택할 수 있도록 하는 비전-언어 기반 검색 프레임워크인 HumanoidVLM을 소개합니다. 이 시스템은 의미론적 작업 추론을 위한 비전-언어 모델과 FAISS 기반의 검색 증강 생성(RAG) 모듈을 결합하여, 두 개의 맞춤형 데이터베이스에서 실험적으로 검증된 강성-감쇠 쌍과 물체별 파지 각도를 검색하고, 이를 작업 공간 임피던스 제어기를 통해 순응적 조작을 실행합니다. 우리는 HumanoidVLM을 14가지 시각적 시나리오에서 평가하여 93%의 검색 정확도를 달성했습니다. 실제 실험에서는 안정적인 상호작용 동역학을 보여주었으며, z축 추적 오차는 일반적으로 1-3.5cm 이내이고 가상 힘은 작업 의존적 임피던스 설정과 일관되었습니다. 이러한 결과는 의미론적 인식과 검색 기반 제어를 연결하는 것이 적응형 휴머노이드 조작을 위한 해석 가능한 경로로서 실현 가능함을 입증합니다.

## 핵심 내용
휴머노이드 로봇은 다양한 물체와 작업에 맞춰 접촉 행동을 적응시켜야 하지만, 대부분의 제어기는 고정되고 수동으로 조정된 임피던스 게인과 그리퍼 설정에 의존합니다. 본 논문에서는 Unitree G1 휴머노이드가 1인칭 RGB 이미지에서 직접 작업에 적합한 직교 임피던스 매개변수와 그리퍼 구성을 선택할 수 있도록 하는 비전-언어 기반 검색 프레임워크인 HumanoidVLM을 소개합니다. 이 시스템은 의미론적 작업 추론을 위한 비전-언어 모델과 FAISS 기반의 검색 증강 생성(RAG) 모듈을 결합하여, 두 개의 맞춤형 데이터베이스에서 실험적으로 검증된 강성-감쇠 쌍과 물체별 파지 각도를 검색하고, 이를 작업 공간 임피던스 제어기를 통해 순응적 조작을 실행합니다. 우리는 HumanoidVLM을 14가지 시각적 시나리오에서 평가하여 93%의 검색 정확도를 달성했습니다. 실제 실험에서는 안정적인 상호작용 동역학을 보여주었으며, z축 추적 오차는 일반적으로 1-3.5cm 이내이고 가상 힘은 작업 의존적 임피던스 설정과 일관되었습니다. 이러한 결과는 의미론적 인식과 검색 기반 제어를 연결하는 것이 적응형 휴머노이드 조작을 위한 해석 가능한 경로로서 실현 가능함을 입증합니다.

## 参考
- http://arxiv.org/abs/2601.14874v1
