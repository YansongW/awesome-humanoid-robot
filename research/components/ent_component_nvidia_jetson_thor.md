---
$id: ent_component_nvidia_jetson_thor
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: NVIDIA Jetson Thor
  zh: NVIDIA Jetson Thor
  ko: NVIDIA Jetson Thor
summary:
  en: NVIDIA's flagship edge AI compute module for humanoid and physical AI robots, built on Blackwell architecture and designed
    to run multimodal generative AI, VLMs, and VLA policies on-device.
  zh: NVIDIA 面向人形机器人和物理 AI 机器人的旗舰边缘 AI 计算模块，基于 Blackwell 架构，支持在设备端运行多模态生成式 AI、视觉语言模型和 VLA 策略。
  ko: NVIDIA의 휴인oid 및 물리 AI 로봇용 플래그십 엣지 AI 컴퓨팅 모듈로, Blackwell 아키텍처 기반이며 온디바이스에서 멀티모달 생성 AI, VLM 및 VLA 정책 실행을 위해 설계됨.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- upstream
- intelligence
functional_roles:
- component
- intelligence
- tool_equipment
tags:
- nvidia
- jetson
- edge_compute
- vla
- on_device_inference
- blackwell
- humanoid
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from NVIDIA official blog and VLA-Perf paper; detailed datasheet review pending. Body backfilled from
    entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_nvidia_jetson_thor_blog
  type: website
  title: Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI
  url: https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/
  date: '2025-08-25'
  accessed_at: '2026-06-25'
- id: src_vla_perf_paper
  type: paper
  title: How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf
  url: https://arxiv.org/abs/2602.18397
  date: '2026-02-20'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
NVIDIA 面向人形机器人和物理 AI 机器人的旗舰边缘 AI 计算模块，基于 Blackwell 架构，支持在设备端运行多模态生成式 AI、视觉语言模型和 VLA 策略。

## 核心内容
### NVIDIA Jetson Thor的定义与定位
NVIDIA Jetson Thor属于 **component** 类型。 所属领域包括：02_components, 07_ai_models_algorithms, 08_software_middleware。 价值链层级：upstream, intelligence。 NVIDIA 面向人形机器人和物理 AI 机器人的旗舰边缘 AI 计算模块，基于 Blackwell 架构，支持在设备端运行多模态生成式 AI、视觉语言模型和 VLA 策略。 英文名称为 *NVIDIA Jetson Thor*。 韩文名称为 *NVIDIA Jetson Thor*。

### NVIDIA Jetson Thor的工作原理与技术架构
NVIDIA Jetson Thor的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用NVIDIA Jetson Thor需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
NVIDIA Jetson Thor已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- nvidia
- jetson
- edge_compute
- vla
- on_device_inference
- blackwell
- humanoid

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键component之一，NVIDIA Jetson Thor在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI](https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/)
- [How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf](https://arxiv.org/abs/2602.18397)

