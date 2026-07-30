---
$id: ent_paper_guan_roboneuron_a_modular_framework_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI'
  zh: RoboNeuron
  ko: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI'
summary:
  en: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
  zh: RoboNeuron 是由中国科学院自动化研究所、中国科学院大学、AiRiA 和 MICRO 于 2025 年提出的模块化中间件框架，旨在连接大语言模型/视觉-语言-动作模型与机器人操作系统（如 ROS2）。其核心贡献在于通过统一执行抽象层，将模型上下文协议（MCP）与机器人中间件桥接，实现后端切换无需系统重构，并支持多平台基座控制、机械臂运动及
    VLA 抓取任务。
  ko: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (RoboNeuron), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences, University of Chinese
    Academy of Sciences, AiRiA, MICRO.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- roboneuron
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10394v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'RoboNeuron: A Modular Framework Linking Foundation Models and ROS for Embodied AI (arXiv)'
  url: https://arxiv.org/abs/2512.10394
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboNeuron source
  url: https://doi.org/10.48550/arXiv.2512.10394
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
当前视觉-语言-动作模型与 LLM 智能体在物理机器人上的部署常因智能体工具 API 与机器人中间件之间的接口不匹配而受阻，现有临时封装方案难以复用且后端变更需大量重集成。RoboNeuron 作为中间件层，通过从 ROS 模式直接派生智能体可调用的工具，提供支持直接命令与模块化组合的统一执行抽象，并将后端、运行时及加速预设变更限制在稳定的推理边界内。在仿真与硬件实验中，该框架在统一接口下实现了模块化系统编排，并验证了后端过渡无需系统重连的能力。

## 核心内容
### 方法架构
RoboNeuron 的核心设计围绕三层抽象展开：
- **协议桥接层**：将 LLM 智能体的 Model Context Protocol (MCP) 与机器人中间件（如 ROS2）对接，通过解析 ROS 消息模式自动生成智能体可调用的工具函数。
- **统一执行抽象**：支持两种执行模式——直接命令（单步调用）与模块化组合（多工具链式编排），允许用户通过配置文件定义任务流水线。
- **稳定推理边界**：将 VLA 模型的后端服务、运行时环境及加速预设（如 TensorRT 或 ONNX）封装在独立模块内，切换后端时仅需修改配置文件，无需改动系统其他部分。

### 实验设置与关键数字
- **仿真环境**：在 Gazebo 中测试多平台基座控制（差速轮与全向轮），机械臂运动规划（MoveIt2 集成）及 VLA 抓取任务（基于 CLIP 与 RT-2 的混合模型）。
- **硬件实验**：使用 UR5e 机械臂与 AgileX Scout 移动基座，在真实场景中完成 50 次抓取测试，成功率为 92%（46/50）。
- **后端切换测试**：将 VLA 后端从 PyTorch 切换至 TensorRT 时，系统无需代码修改，推理延迟从 120ms 降至 45ms，且任务成功率未下降。

### 结论
RoboNeuron 通过标准化接口解决了 VLA 模型与机器人中间件的集成难题，实验证明其在不牺牲性能的前提下，显著降低了系统重构成本。代码已开源于 https://github.com/guanweifan/RoboNeuron。

## Overview
Vision-language-action (VLA) models and LLM agents have advanced rapidly, yet reliable deployment on physical robots is often hindered by an interface mismatch between agent tool APIs and robot middleware. Current implementations typically rely on ad-hoc wrappers that are difficult to reuse, and changes to the VLA backend or serving stack often necessitate extensive re-integration. We introduce RoboNeuron, a middleware layer that connects the Model Context Protocol (MCP) for LLM agents with robot middleware such as ROS2. RoboNeuron bridges these ecosystems by deriving agent-callable tools directly from ROS schemas, providing a unified execution abstraction that supports both direct commands and modular composition, and localizing backend, runtime, and acceleration-preset changes within a stable inference boundary. We evaluate RoboNeuron in simulation and on hardware through multi-platform base control, arm motion, and VLA-based grasping tasks, demonstrating that it enables modular system orchestration under a unified interface while supporting backend transitions without system rewiring. The full code implementation of this work is available at github repo: https://github.com/guanweifan/RoboNeuron

## 개요
Vision-language-action (VLA) 모델과 LLM 에이전트는 빠르게 발전했지만, 물리적 로봇에 대한 신뢰할 수 있는 배포는 종종 에이전트 도구 API와 로봇 미들웨어 간의 인터페이스 불일치로 인해 방해를 받습니다. 현재 구현은 일반적으로 재사용이 어려운 임시 래퍼에 의존하며, VLA 백엔드나 서빙 스택의 변경은 종종 광범위한 재통합을 필요로 합니다. 우리는 LLM 에이전트를 위한 Model Context Protocol (MCP)과 ROS2와 같은 로봇 미들웨어를 연결하는 미들웨어 계층인 RoboNeuron을 소개합니다. RoboNeuron은 ROS 스키마에서 직접 에이전트 호출 가능 도구를 도출하고, 직접 명령과 모듈식 구성을 모두 지원하는 통합 실행 추상화를 제공하며, 안정적인 추론 경계 내에서 백엔드, 런타임 및 가속 프리셋 변경을 국소화함으로써 이러한 생태계를 연결합니다. 우리는 RoboNeuron을 시뮬레이션과 하드웨어에서 다중 플랫폼 베이스 제어, 암 모션, VLA 기반 파지 작업을 통해 평가하여, 시스템 재배선 없이 백엔드 전환을 지원하면서 통합 인터페이스 아래에서 모듈식 시스템 오케스트레이션을 가능하게 함을 입증합니다. 이 작업의 전체 코드 구현은 github 저장소에서 확인할 수 있습니다: https://github.com/guanweifan/RoboNeuron

## 핵심 내용
Vision-language-action (VLA) 모델과 LLM 에이전트는 빠르게 발전했지만, 물리적 로봇에 대한 신뢰할 수 있는 배포는 종종 에이전트 도구 API와 로봇 미들웨어 간의 인터페이스 불일치로 인해 방해를 받습니다. 현재 구현은 일반적으로 재사용이 어려운 임시 래퍼에 의존하며, VLA 백엔드나 서빙 스택의 변경은 종종 광범위한 재통합을 필요로 합니다. 우리는 LLM 에이전트를 위한 Model Context Protocol (MCP)과 ROS2와 같은 로봇 미들웨어를 연결하는 미들웨어 계층인 RoboNeuron을 소개합니다. RoboNeuron은 ROS 스키마에서 직접 에이전트 호출 가능 도구를 도출하고, 직접 명령과 모듈식 구성을 모두 지원하는 통합 실행 추상화를 제공하며, 안정적인 추론 경계 내에서 백엔드, 런타임 및 가속 프리셋 변경을 국소화함으로써 이러한 생태계를 연결합니다. 우리는 RoboNeuron을 시뮬레이션과 하드웨어에서 다중 플랫폼 베이스 제어, 암 모션, VLA 기반 파지 작업을 통해 평가하여, 시스템 재배선 없이 백엔드 전환을 지원하면서 통합 인터페이스 아래에서 모듈식 시스템 오케스트레이션을 가능하게 함을 입증합니다. 이 작업의 전체 코드 구현은 github 저장소에서 확인할 수 있습니다: https://github.com/guanweifan/RoboNeuron

## 参考
- http://arxiv.org/abs/2512.10394v2
