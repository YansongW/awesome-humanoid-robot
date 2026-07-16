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
NVIDIA Jetson Thor属于 **零部件** 类型。 所属领域包括：零部件, AI 模型与算法, 软件中间件。 价值链层级：上游, intelligence。 NVIDIA 面向人形机器人和物理 AI 机器人的旗舰边缘 AI 计算模块，基于 Blackwell 架构，支持在设备端运行多模态生成式 AI、视觉语言模型和 VLA 策略。 英文名称为 *NVIDIA Jetson Thor*。 韩文名称为 *NVIDIA Jetson Thor*。

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
作为人形机器人产业链中的关键零部件之一，NVIDIA Jetson Thor在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Introducing NVIDIA Jetson Thor, the Ultimate Platform for Physical AI](https://developer.nvidia.com/blog/introducing-nvidia-jetson-thor-the-ultimate-platform-for-physical-ai/)
- [How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf](https://arxiv.org/abs/2602.18397)

## Overview
NVIDIA's flagship edge AI computing module for humanoid robots and physical AI robots, based on the Blackwell architecture, supports running multimodal generative AI, vision-language models, and VLA policies on-device.

## Content
### Definition and Positioning of NVIDIA Jetson Thor
NVIDIA Jetson Thor belongs to the **component** category. Its fields include: components, AI models and algorithms, and software middleware. Value chain level: upstream, intelligence. NVIDIA's flagship edge AI computing module for humanoid robots and physical AI robots, based on the Blackwell architecture, supports running multimodal generative AI, vision-language models, and VLA policies on-device. English name: *NVIDIA Jetson Thor*. Korean name: *NVIDIA Jetson Thor*.

### Working Principle and Technical Architecture of NVIDIA Jetson Thor
The core mechanism of NVIDIA Jetson Thor defines its performance boundaries in humanoid robot systems. Understanding its internal structure, signal flow, and control interfaces aids in system integration and optimization.
During selection and integration, attention must be paid to its compatibility with controllers, communication buses, power systems, and mechanical structures.

### Key Parameters and Selection Points
In engineering practice, selecting NVIDIA Jetson Thor requires comprehensive consideration of performance metrics, reliability, cost, supply chain maturity, and compatibility with the overall system.
Key parameters typically include precision, bandwidth, torque, power consumption, weight, interface protocols, and environmental adaptability.
For different application scenarios, trade-offs between performance and cost may be necessary, with appropriate redundancy and safety margins reserved.

### Typical Applications and Development Trends
NVIDIA Jetson Thor has been widely used in prototype validation, academic research, and early commercial products for humanoid robots.
In the future, as the industry chain matures, its integration level, intelligence, and cost-effectiveness are expected to continue improving.

### Related Tags
- nvidia
- jetson
- edge_compute
- vla
- on_device_inference
- blackwell
- humanoid

### Role in Humanoid Robot Systems
As a key component in the humanoid robot industry chain, NVIDIA Jetson Thor plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, execution, energy, structure, and validation, collectively determining overall system performance. Related research and applications are ongoing to further enhance its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
NVIDIA는 휴머노이드 로봇과 물리적 AI 로봇을 위한 플래그십 엣지 AI 컴퓨팅 모듈로, Blackwell 아키텍처를 기반으로 하며, 디바이스에서 멀티모달 생성형 AI, 비전-언어 모델 및 VLA 정책을 실행할 수 있도록 지원합니다.

## 핵심 내용
### NVIDIA Jetson Thor의 정의 및 포지셔닝
NVIDIA Jetson Thor는 **부품** 유형에 속합니다. 관련 분야는 부품, AI 모델 및 알고리즘, 소프트웨어 미들웨어를 포함합니다. 가치 사슬 계층은 상류, 인텔리전스입니다. NVIDIA는 휴머노이드 로봇과 물리적 AI 로봇을 위한 플래그십 엣지 AI 컴퓨팅 모듈로, Blackwell 아키텍처를 기반으로 하며, 디바이스에서 멀티모달 생성형 AI, 비전-언어 모델 및 VLA 정책을 실행할 수 있도록 지원합니다. 영문 명칭은 *NVIDIA Jetson Thor*입니다. 한글 명칭은 *NVIDIA Jetson Thor*입니다.

### NVIDIA Jetson Thor의 작동 원리 및 기술 아키텍처
NVIDIA Jetson Thor의 핵심 메커니즘은 휴머노이드 로봇 시스템에서의 성능 경계를 결정합니다. 내부 구조, 신호 흐름 및 제어 인터페이스를 이해하면 시스템 통합 및 최적화에 도움이 됩니다.
선정 및 통합 과정에서는 컨트롤러, 통신 버스, 전원 시스템 및 기계 구조와의 호환성에 주의해야 합니다.

### 주요 매개변수 및 선정 포인트
엔지니어링 실무에서 NVIDIA Jetson Thor를 선택할 때는 성능 지표, 신뢰성, 비용, 공급망 성숙도 및 전체 시스템과의 호환성을 종합적으로 고려해야 합니다.
주요 매개변수에는 일반적으로 정밀도, 대역폭, 토크, 전력 소비, 무게, 인터페이스 프로토콜 및 환경 적응성 등이 포함됩니다.
다양한 응용 시나리오에 따라 성능과 비용 간의 균형을 맞추고 적절한 여유와 안전 마진을 확보해야 할 수 있습니다.

### 대표적인 응용 및 발전 동향
NVIDIA Jetson Thor는 휴머노이드 로봇의 프로토타입 검증, 학술 연구 및 초기 상용 제품에 널리 사용되고 있습니다.
향후 산업 체인의 성숙에 따라 집적도, 지능화 수준 및 비용 효율성이 지속적으로 향상될 것으로 기대됩니다.

### 관련 태그
- nvidia
- jetson
- edge_compute
- vla
- on_device_inference
- blackwell
- humanoid

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인의 핵심 부품 중 하나로서, NVIDIA Jetson Thor는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구 및 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
