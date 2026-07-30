---
$id: ent_paper_lisondra_embodied_ai_with_foundation_mo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Embodied AI with Foundation Models for Mobile Service Robots: A Systematic Review'
  zh: 面向移动服务机器人的基础模型具身智能：系统综述
  ko: '이동 서비스 로봇을 위한 파운데이션 모델 기반 구체화된 AI: 체계적 리뷰'
summary:
  en: A 2025 systematic review analyzing how large language, vision-language, multimodal, and vision-language-action models
    address language-to-action mapping, multimodal perception, uncertainty estimation, and onboard deployment challenges in
    mobile service robotics.
  zh: 本文是2025年首篇系统综述，聚焦基础模型（LLM、VLM、MLLM、VLA）在移动服务机器人中的集成。核心贡献在于分析这些模型如何解决语言到动作映射、多模态感知、不确定性估计和机载部署等关键挑战，并探讨了伦理与社会影响。
  ko: 2025년 체계적 리뷰로, 대형 언어 모델, 비전-언어 모델, 멀티모달 대형 언어 모델, 비전-언어-행동 모델이 이동 서비스 로봇의 언어-행동 매핑, 다중감각 인식, 불확실성 추정, 온보드 배포 과제를 어떻게
    해결하는지 분석함.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 12_policy_regulation_ethics
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- foundation_models
- mobile_service_robots
- vision_language_action_models
- multimodal_perception
- language_conditioned_control
- uncertainty_aware_reasoning
- human_robot_interaction
- domestic_assistance
- healthcare_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.20503v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Embodied AI with Foundation Models for Mobile Service Robots: A Systematic Review'
  url: https://arxiv.org/abs/2505.20503
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该综述系统梳理了大型语言模型、视觉-语言模型、多模态大语言模型及视觉-语言-动作模型在移动服务机器人领域的应用进展。通过结合具身智能原理，机器人能在动态真实环境中实现更灵活的理解、自适应行为和鲁棒任务执行。文章重点分析了基础模型如何通过语言条件控制、多模态传感器融合、不确定性感知推理和高效模型缩放来应对核心挑战，并考察了家庭辅助、医疗保健和服务自动化等实际应用场景。

## 核心内容
### 核心挑战与基础模型解决方案
- **语言到动作映射**：基础模型通过语言条件控制实现自然语言指令到可执行机器人动作的转换，例如LLM用于任务规划，VLA模型直接生成动作序列。
- **多模态感知**：VLM和MLLM融合视觉、语言和触觉等多模态传感器数据，提升在人类中心环境中的场景理解能力。
- **不确定性估计**：通过概率推理和贝叶斯方法，模型在决策过程中量化不确定性，确保安全操作。
- **机载部署**：采用模型缩放和轻量化技术（如知识蒸馏、量化）降低计算开销，满足实时性要求。

### 实际应用场景
- **家庭辅助**：基础模型使机器人能理解上下文指令（如“把桌上的杯子拿过来”），并适应家庭环境变化。
- **医疗保健**：在病房中执行药物递送、患者监测等任务，需兼顾社交互动和隐私保护。
- **服务自动化**：在商场、酒店等场景中提供导航、信息查询等服务，要求行为可泛化且符合社会规范。

### 伦理与社会影响
- **可靠性**：需确保模型在长期运行中保持稳定，避免因分布偏移导致故障。
- **隐私**：机载数据处理需符合隐私法规，例如通过联邦学习实现本地化推理。
- **人机交互**：设计透明决策机制，支持人类监督和干预（human-in-the-loop）。

### 未来研究方向
- **终身适应**：开发持续学习框架，使机器人能在线更新模型以适应新环境。
- **资源受限部署**：探索边缘计算和模型压缩技术，降低对云端依赖。
- **治理框架**：建立安全、可扩展且可信的监管体系，涵盖伦理审查和故障追责机制。

## Overview
Rapid advancements in foundation models, including Large Language Models, Vision-Language Models, Multimodal Large Language Models, and Vision-Language-Action Models, have opened new avenues for embodied AI in mobile service robotics. By combining foundation models with the principles of embodied AI, where intelligent systems perceive, reason, and act through physical interaction, mobile service robots can achieve more flexible understanding, adaptive behavior, and robust task execution in dynamic real-world environments. Despite this progress, embodied AI for mobile service robots continues to face fundamental challenges related to the translation of natural language instructions into executable robot actions, multimodal perception in human-centered environments, uncertainty estimation for safe decision-making, and computational constraints for real-time onboard deployment. In this paper, we present the first systematic review focused specifically on the integration of foundation models in mobile service robotics. We analyze how recent advances in foundation models address these core challenges through language-conditioned control, multimodal sensor fusion, uncertainty-aware reasoning, and efficient model scaling. We further examine real-world applications in domestic assistance, healthcare, and service automation, highlighting how foundation models enable context-aware, socially responsive, and generalizable robot behaviors. Beyond technical considerations, we discuss ethical, societal, and human-interaction implications associated with deploying foundation model-enabled service robots in human environments. Finally, we outline future research directions emphasizing reliability and lifelong adaptation, privacy-aware and resource-constrained deployment, and governance and human-in-the-loop frameworks required for safe, scalable, and trustworthy mobile service robotics.

## 개요
대규모 언어 모델, 비전-언어 모델, 다중 모달 대규모 언어 모델, 비전-언어-행동 모델을 포함한 기초 모델의 급속한 발전은 모바일 서비스 로봇 분야에서 체화된 AI에 새로운 가능성을 열었습니다. 기초 모델을 체화된 AI의 원리(지능형 시스템이 물리적 상호작용을 통해 인지, 추론, 행동하는 것)와 결합함으로써, 모바일 서비스 로봇은 역동적인 실제 환경에서 더 유연한 이해, 적응적 행동, 강건한 작업 실행을 달성할 수 있습니다. 이러한 진전에도 불구하고, 모바일 서비스 로봇을 위한 체화된 AI는 자연어 명령어를 실행 가능한 로봇 동작으로 변환하는 문제, 인간 중심 환경에서의 다중 모달 인식, 안전한 의사 결정을 위한 불확실성 추정, 실시간 온보드 배치를 위한 계산 제약 등 근본적인 과제에 계속 직면하고 있습니다. 본 논문에서는 모바일 서비스 로봇 분야에서 기초 모델 통합에 초점을 맞춘 최초의 체계적 리뷰를 제시합니다. 우리는 언어 조건 제어, 다중 모달 센서 융합, 불확실성 인식 추론, 효율적인 모델 스케일링을 통해 기초 모델의 최신 발전이 이러한 핵심 과제를 어떻게 해결하는지 분석합니다. 또한 가사 지원, 의료, 서비스 자동화 분야의 실제 응용 사례를 검토하며, 기초 모델이 상황 인식, 사회적 반응성, 일반화 가능한 로봇 행동을 어떻게 가능하게 하는지 조명합니다. 기술적 고려 사항을 넘어, 인간 환경에서 기초 모델 기반 서비스 로봇을 배치하는 것과 관련된 윤리적, 사회적, 인간 상호작용 측면의 함의를 논의합니다. 마지막으로, 신뢰성과 평생 적응, 프라이버시 인식 및 자원 제약 배치, 안전하고 확장 가능하며 신뢰할 수 있는 모바일 서비스 로봇을 위해 필요한 거버넌스 및 인간-루프-인 프레임워크를 강조하는 미래 연구 방향을 제시합니다.

## 핵심 내용
대규모 언어 모델, 비전-언어 모델, 다중 모달 대규모 언어 모델, 비전-언어-행동 모델을 포함한 기초 모델의 급속한 발전은 모바일 서비스 로봇 분야에서 체화된 AI에 새로운 가능성을 열었습니다. 기초 모델을 체화된 AI의 원리(지능형 시스템이 물리적 상호작용을 통해 인지, 추론, 행동하는 것)와 결합함으로써, 모바일 서비스 로봇은 역동적인 실제 환경에서 더 유연한 이해, 적응적 행동, 강건한 작업 실행을 달성할 수 있습니다. 이러한 진전에도 불구하고, 모바일 서비스 로봇을 위한 체화된 AI는 자연어 명령어를 실행 가능한 로봇 동작으로 변환하는 문제, 인간 중심 환경에서의 다중 모달 인식, 안전한 의사 결정을 위한 불확실성 추정, 실시간 온보드 배치를 위한 계산 제약 등 근본적인 과제에 계속 직면하고 있습니다. 본 논문에서는 모바일 서비스 로봇 분야에서 기초 모델 통합에 초점을 맞춘 최초의 체계적 리뷰를 제시합니다. 우리는 언어 조건 제어, 다중 모달 센서 융합, 불확실성 인식 추론, 효율적인 모델 스케일링을 통해 기초 모델의 최신 발전이 이러한 핵심 과제를 어떻게 해결하는지 분석합니다. 또한 가사 지원, 의료, 서비스 자동화 분야의 실제 응용 사례를 검토하며, 기초 모델이 상황 인식, 사회적 반응성, 일반화 가능한 로봇 행동을 어떻게 가능하게 하는지 조명합니다. 기술적 고려 사항을 넘어, 인간 환경에서 기초 모델 기반 서비스 로봇을 배치하는 것과 관련된 윤리적, 사회적, 인간 상호작용 측면의 함의를 논의합니다. 마지막으로, 신뢰성과 평생 적응, 프라이버시 인식 및 자원 제약 배치, 안전하고 확장 가능하며 신뢰할 수 있는 모바일 서비스 로봇을 위해 필요한 거버넌스 및 인간-루프-인 프레임워크를 강조하는 미래 연구 방향을 제시합니다.

## 参考
- http://arxiv.org/abs/2505.20503v2
