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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.10394v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (931 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2512.10394v2

## 개요
현재 비전-언어-행동 모델과 LLM 에이전트를 물리 로봇에 배포할 때, 에이전트 도구 API와 로봇 미들웨어 간의 인터페이스 불일치로 인해 종종 장애가 발생합니다. 기존의 임시 래퍼 솔루션은 재사용이 어렵고 백엔드 변경 시 대규모 재통합이 필요합니다. RoboNeuron은 미들웨어 계층으로서 ROS 패턴에서 직접 에이전트 호출 가능한 도구를 파생시켜, 직접 명령과 모듈식 조합을 지원하는 통합 실행 추상화를 제공하며, 백엔드, 런타임 및 가속 프리셋 변경을 안정적인 추론 경계 내로 제한합니다. 시뮬레이션 및 하드웨어 실험에서 이 프레임워크는 통합 인터페이스 하에 모듈식 시스템 오케스트레이션을 구현했으며, 백엔드 전환 시 시스템 재연결이 필요 없음을 검증했습니다.

## 핵심 내용
### 방법 아키텍처
RoboNeuron의 핵심 설계는 세 가지 추상화 계층을 중심으로 전개됩니다:
- **프로토콜 브리징 계층**: LLM 에이전트의 Model Context Protocol (MCP)을 로봇 미들웨어(예: ROS2)와 연결하며, ROS 메시지 패턴을 파싱하여 에이전트 호출 가능한 도구 함수를 자동 생성합니다.
- **통합 실행 추상화**: 직접 명령(단일 단계 호출)과 모듈식 조합(다중 도구 체인 오케스트레이션)의 두 가지 실행 모드를 지원하며, 사용자가 구성 파일을 통해 작업 파이프라인을 정의할 수 있습니다.
- **안정적인 추론 경계**: VLA 모델의 백엔드 서비스, 런타임 환경 및 가속 프리셋(예: TensorRT 또는 ONNX)을 독립 모듈로 캡슐화하여, 백엔드 전환 시 구성 파일만 수정하면 되고 시스템의 다른 부분은 변경할 필요가 없습니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 환경**: Gazebo에서 다중 플랫폼 베이스 제어(차동 휠 및 전방향 휠), 로봇 팔 운동 계획(MoveIt2 통합) 및 VLA 그리핑 작업(CLIP 및 RT-2 기반 하이브리드 모델)을 테스트했습니다.
- **하드웨어 실험**: UR5e 로봇 팔과 AgileX Scout 모바일 베이스를 사용하여 실제 환경에서 50회 그리핑 테스트를 수행했으며, 성공률은 92%(46/50)였습니다.
- **백엔드 전환 테스트**: VLA 백엔드를 PyTorch에서 TensorRT로 전환할 때 코드 수정 없이 추론 지연 시간이 120ms에서 45ms로 감소했으며, 작업 성공률은 하락하지 않았습니다.

### 결론
RoboNeuron은 표준화된 인터페이스를 통해 VLA 모델과 로봇 미들웨어 간의 통합 문제를 해결했으며, 실험을 통해 성능 저하 없이 시스템 재구성 비용을 크게 줄일 수 있음을 입증했습니다. 코드는 https://github.com/guanweifan/RoboNeuron에서 오픈소스로 공개되었습니다.
