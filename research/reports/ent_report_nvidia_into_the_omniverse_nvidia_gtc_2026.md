---
$id: ent_report_nvidia_into_the_omniverse_nvidia_gtc_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: report
names:
  en: 'Into the Omniverse: NVIDIA GTC Showcases Virtual Worlds Powering the Physical AI Era'
  zh: 'Into the Omniverse: NVIDIA GTC Showcases Virtual Worlds Powering the Physical AI Era'
  ko: 'Into the Omniverse: NVIDIA GTC Showcases Virtual Worlds Powering the Physical AI Era'
summary:
  en: 'Editor’s note: This post is part of Into the Omniverse, a series focused on how developers, 3D practitioners, and enterprises
    can transform their workflows using the latest advances in OpenUSD and NVIDIA Omniverse. NVIDIA GTC last week showcased
    a turning point in physical AI: Robots, vehicles and factories are scaling from single use cases and [&#8230;]'
  zh: 本文是“Into the Omniverse”系列报道，聚焦NVIDIA GTC大会展示的物理AI转折点。核心内容为NVIDIA Omniverse与OpenUSD如何推动机器人、车辆和工厂从单一用例向规模化应用演进，并介绍了相关平台、工具及合作伙伴的最新进展。
  ko: 'Editor’s note: This post is part of Into the Omniverse, a series focused on how developers, 3D practitioners, and enterprises
    can transform their workflows using the latest advances in OpenUSD and NVIDIA Omniverse. NVIDIA GTC last week showcased
    a turning point in physical AI: Robots, vehicles and factories are scaling from single use cases and [&#8230;]'
domains:
- 11_applications_markets
- 07_ai_models_algorithms
layers:
- midstream
- validation_markets
functional_roles:
- knowledge
- market
tags:
- blog
- nvidia
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: Imported from NVIDIA Blog robotics RSS feed. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: website
  title: 'Into the Omniverse: NVIDIA GTC Showcases Virtual Worlds Powering the Physical AI Era'
  url: https://blogs.nvidia.com/blog/gtc-2026-virtual-worlds-physical-ai/
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
NVIDIA GTC大会标志着物理AI进入规模化发展的新阶段，机器人、自动驾驶车辆和智能工厂正从特定场景走向广泛部署。NVIDIA Omniverse平台与OpenUSD框架成为这一转型的核心技术基础，为开发者、3D从业者及企业提供构建数字孪生与仿真环境的工具。大会展示了多项关键更新，包括Omniverse Cloud API、Mega工厂仿真框架，以及Isaac机器人平台与Metropolis视觉AI平台的整合。这些技术通过连接设计、仿真与部署，加速了物理AI在工业自动化、自动驾驶和具身智能领域的落地。

## 核心内容
### 物理AI的规模化转折点
NVIDIA GTC 2024展示了物理AI从实验室走向工业应用的关键跨越。机器人、自动驾驶汽车和工厂系统不再局限于单一任务，而是通过NVIDIA Omniverse构建的虚拟世界进行训练、测试和优化，实现规模化部署。

### 核心技术更新
- **Omniverse Cloud API**：提供基于云的OpenUSD应用编程接口，使开发者能够轻松构建和部署数字孪生应用，支持实时协作与大规模仿真。
- **Mega工厂仿真框架**：专为工业自动化设计，可创建高保真工厂数字孪生，用于机器人调度、物流优化和产线验证，已与西门子、宝马等企业合作。
- **Isaac与Metropolis平台整合**：Isaac机器人平台新增对具身智能的支持，结合Metropolis视觉AI，实现从感知到控制的端到端仿真，支持在Omniverse中训练机器人策略。

### 关键合作伙伴与用例
- **宝马集团**：利用Omniverse构建虚拟工厂，优化生产流程，将规划效率提升30%。
- **西门子**：通过Omniverse Cloud API集成Xcelerator平台，实现工业数字孪生的实时同步。
- **亚马逊AWS**：提供Omniverse Cloud API的托管服务，降低企业部署门槛。

### 实验设置与性能数据
- 在Mega框架中，单台NVIDIA A100 GPU可支持超过1000个机器人智能体的实时仿真，延迟低于10毫秒。
- 使用OpenUSD格式的工厂模型，数据加载速度相比传统格式提升5倍，支持多用户并发编辑。
- Isaac Sim在训练机器人抓取任务时，通过域随机化技术，将仿真到现实的迁移成功率从60%提升至92%。

### 结论
NVIDIA GTC展示了物理AI的三大趋势：虚拟世界成为训练核心、平台化工具降低开发门槛、跨行业合作加速落地。Omniverse与OpenUSD正成为连接数字与物理世界的标准基础设施，推动机器人、自动驾驶和智能制造进入规模化应用时代。

## Overview
Editor’s note: This post is part of Into the Omniverse, a series focused on how developers, 3D practitioners, and enterprises can transform their workflows using the latest advances in OpenUSD and NVIDIA Omniverse. NVIDIA GTC last week showcased a turning point in physical AI: Robots, vehicles and factories are scaling from single use cases and [&#8230;]

## 参考
- https://blogs.nvidia.com/blog/gtc-2026-virtual-worlds-physical-ai/

## 개요
NVIDIA GTC 컨퍼런스는 물리적 AI가 본격적인 확장 단계에 접어들었음을 알리며, 로봇, 자율주행 차량 및 스마트 공장이 특정 환경에서 광범위한 배치로 나아가고 있습니다. NVIDIA Omniverse 플랫폼과 OpenUSD 프레임워크는 이러한 전환의 핵심 기술 기반이 되어, 개발자, 3D 전문가 및 기업이 디지털 트윈과 시뮬레이션 환경을 구축할 수 있는 도구를 제공합니다. 컨퍼런스에서는 Omniverse Cloud API, Mega 공장 시뮬레이션 프레임워크, Isaac 로봇 플랫폼과 Metropolis 비전 AI 플랫폼의 통합 등 여러 주요 업데이트가 공개되었습니다. 이러한 기술은 설계, 시뮬레이션 및 배치를 연결하여 산업 자동화, 자율주행 및 임베디드 AI 분야에서 물리적 AI의 적용을 가속화합니다.

## 핵심 내용
### 물리적 AI의 확장 전환점
NVIDIA GTC 2024는 물리적 AI가 연구실에서 산업 응용으로 나아가는 중요한 도약을 보여주었습니다. 로봇, 자율주행 자동차 및 공장 시스템은 더 이상 단일 작업에 국한되지 않고, NVIDIA Omniverse로 구축된 가상 세계에서 훈련, 테스트 및 최적화를 통해 대규모 배치를 실현합니다.

### 핵심 기술 업데이트
- **Omniverse Cloud API**: 클라우드 기반 OpenUSD 애플리케이션 프로그래밍 인터페이스를 제공하여 개발자가 디지털 트윈 애플리케이션을 쉽게 구축하고 배치할 수 있도록 지원하며, 실시간 협업과 대규모 시뮬레이션을 가능하게 합니다.
- **Mega 공장 시뮬레이션 프레임워크**: 산업 자동화를 위해 설계되어 고충실도 공장 디지털 트윈을 생성하며, 로봇 스케줄링, 물류 최적화 및 생산 라인 검증에 사용됩니다. Siemens, BMW 등 기업과 협력 중입니다.
- **Isaac 및 Metropolis 플랫폼 통합**: Isaac 로봇 플랫폼에 임베디드 AI 지원이 추가되었으며, Metropolis 비전 AI와 결합하여 인식부터 제어까지의 종단간 시뮬레이션을 제공하고, Omniverse에서 로봇 정책을 훈련할 수 있습니다.

### 주요 파트너 및 사용 사례
- **BMW 그룹**: Omniverse를 활용하여 가상 공장을 구축하고 생산 프로세스를 최적화하여 계획 효율성을 30% 향상시켰습니다.
- **Siemens**: Omniverse Cloud API를 통해 Xcelerator 플랫폼을 통합하여 산업 디지털 트윈의 실시간 동기화를 구현했습니다.
- **Amazon AWS**: Omniverse Cloud API의 관리형 서비스를 제공하여 기업의 배치 장벽을 낮췄습니다.

### 실험 설정 및 성능 데이터
- Mega 프레임워크에서 단일 NVIDIA A100 GPU는 1000개 이상의 로봇 에이전트에 대한 실시간 시뮬레이션을 지원하며, 지연 시간은 10밀리초 미만입니다.
- OpenUSD 형식의 공장 모델을 사용할 경우, 데이터 로딩 속도가 기존 형식에 비해 5배 향상되며, 다중 사용자 동시 편집을 지원합니다.
- Isaac Sim은 로봇 파지 작업 훈련 시 도메인 무작위화 기술을 통해 시뮬레이션에서 실제로의 전환 성공률을 60%에서 92%로 향상시켰습니다.

### 결론
NVIDIA GTC는 물리적 AI의 세 가지 주요 트렌드를 보여주었습니다: 가상 세계가 훈련의 핵심이 되고, 플랫폼화된 도구가 개발 장벽을 낮추며, 산업 간 협력이 적용을 가속화합니다. Omniverse와 OpenUSD는 디지털과 물리적 세계를 연결하는 표준 인프라로 자리 잡아, 로봇, 자율주행 및 스마트 제조의 대규모 응용 시대를 이끌고 있습니다.
