---
$id: ent_paper_toddlerbot_open_source_ml_comp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'
  zh: ToddlerBot｜用于移动操作的开源ML兼容人形平台
  ko: 'ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation'
summary:
  en: Learning-based robotics research driven by data demands a new approach to robot hardware design-one that serves as both
    a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a
    low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot
    enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration
    and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from
    simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection
    for learning motor skills from human demonstrations. Utilizing its data c
  zh: ToddlerBot 是一个低成本、开源的人形机器人平台，由研究团队开发，专为可扩展的策略学习和具身数据采集而设计。其核心贡献在于实现了从仿真到真实世界的零样本策略迁移，并提供了用户友好的遥操作接口，总成本低于 6,000 美元。
  ko: ToddlerBot 主要解决数据闭环：用本体状态与关节序列、遥操作/外骨骼数据、仿真交互数据采集人类操作和机器人状态，再通过ACT/行为克隆模仿学习、扩散策略/流匹配、分层技能/专家策略转成可训练、可复用的地形/场景表征。关键点是把动作生成看成条件生成问题，用扩散或流匹配在多模态动作分布里采样可执行轨迹。
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- deployment
- hardware_platform
- real_world
- sensor_suite
- toddlerbot
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: ToddlerBot: Open-Source
    ML-Compatible Humanoid Platform for Loco-Manipulation. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py
    | WP4 trilingual backfill 2026-08-10: ko body retranslated from zh deep-read (747 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: ToddlerBot project page
  url: https://toddlerbot.github.io
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
ToddlerBot 旨在满足基于学习的机器人研究对硬件的新需求，即同时作为策略执行平台和具身数据采集工具。该平台通过即插即用的零点校准和可迁移的电机系统识别，确保了高保真数字孪生，从而支持从仿真到真实世界的零样本策略迁移。其紧凑的尺寸（0.56米，3.4千克）和完全3D打印的开源设计，结合商用组件，保证了在真实环境中的安全操作和可复现性。通过遥操作接口，用户可以高效地从人类演示中收集数据，学习全身移动操作技能。

## 核心内容
### 方法
ToddlerBot 的设计强调机器学习兼容性，其硬件架构支持无缝获取高质量的仿真和真实世界数据。关键方法包括：
- **零样本策略迁移**：通过即插即用的零点校准和可迁移的电机系统识别，构建高保真数字孪生，使在仿真中训练的策略可直接应用于真实机器人。
- **数据采集**：用户友好的遥操作接口简化了从人类演示中学习运动技能的真实世界数据收集过程。

### 架构
- **尺寸与重量**：高度 0.56 米，重量 3.4 千克，适合在真实环境中安全操作。
- **成本**：总成本低于 6,000 美元，采用完全 3D 打印的开源设计和商用组件。
- **可复现性**：提供全面的文档，具备基本技术知识即可组装和维护，已通过独立复制验证。

### 实验设置与关键数字
- **性能测试**：包括臂展、有效载荷、耐久性测试，以及全身移动操作任务。
- **协作任务**：演示了长时域协作场景，其中两个机器人共同整理玩具区域。
- **独立复制**：系统成功被独立复制，验证了其可复现性。

### 结论
ToddlerBot 通过提升机器学习兼容性、能力和可复现性，为机器人研究中的可扩展学习和动态策略执行提供了一个稳健的平台。

## Overview
Learning-based robotics research driven by data demands a new approach to robot hardware design-one that serves as both a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection for learning motor skills from human demonstrations. Utilizing its data collection ability and anthropomorphic design, ToddlerBot is an ideal platform to perform whole-body loco-manipulation. Additionally, ToddlerBot's compact size (0.56m, 3.4kg) ensures safe operation in real-world environments. Reproducibility is achieved with an entirely 3D-printed, open-source design and commercially available components, keeping the total cost under 6,000 USD. Comprehensive documentation allows assembly and maintenance with basic technical expertise, as validated by a successful independent replication of the system. We demonstrate ToddlerBot's capabilities through arm span, payload, endurance tests, loco-manipulation tasks, and a collaborative long-horizon scenario where two robots tidy a toy session together. By advancing ML-compatibility, capability, and reproducibility, ToddlerBot provides a robust platform for scalable learning and dynamic policy execution in robotics research.

## Overview
Data-driven learning-based robotics research demands a new approach to robot hardware design—one that serves as both a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection for learning motor skills from human demonstrations. Utilizing its data collection ability and anthropomorphic design, ToddlerBot is an ideal platform to perform whole-body loco-manipulation. Additionally, ToddlerBot's compact size (0.56m, 3.4kg) ensures safe operation in real-world environments. Reproducibility is achieved with an entirely 3D-printed, open-source design and commercially available components, keeping the total cost under 6,000 USD. Comprehensive documentation allows assembly and maintenance with basic technical expertise, as validated by a successful independent replication of the system. We demonstrate ToddlerBot's capabilities through arm span, payload, endurance tests, loco-manipulation tasks, and a collaborative long-horizon scenario where two robots tidy a toy session together. By advancing ML-compatibility, capability, and reproducibility, ToddlerBot provides a robust platform for scalable learning and dynamic policy execution in robotics research.

## Content
Data-driven learning-based robotics research demands a new approach to robot hardware design—one that serves as both a platform for policy execution and a tool for embodied data collection to train policies. We introduce ToddlerBot, a low-cost, open-source humanoid robot platform designed for scalable policy learning and research in robotics and AI. ToddlerBot enables seamless acquisition of high-quality simulation and real-world data. The plug-and-play zero-point calibration and transferable motor system identification ensure a high-fidelity digital twin, enabling zero-shot policy transfer from simulation to the real world. A user-friendly teleoperation interface facilitates streamlined real-world data collection for learning motor skills from human demonstrations. Utilizing its data collection ability and anthropomorphic design, ToddlerBot is an ideal platform to perform whole-body loco-manipulation. Additionally, ToddlerBot's compact size (0.56m, 3.4kg) ensures safe operation in real-world environments. Reproducibility is achieved with an entirely 3D-printed, open-source design and commercially available components, keeping the total cost under 6,000 USD. Comprehensive documentation allows assembly and maintenance with basic technical expertise, as validated by a successful independent replication of the system. We demonstrate ToddlerBot's capabilities through arm span, payload, endurance tests, loco-manipulation tasks, and a collaborative long-horizon scenario where two robots tidy a toy session together. By advancing ML-compatibility, capability, and reproducibility, ToddlerBot provides a robust platform for scalable learning and dynamic policy execution in robotics research.

## 参考
- Semantic Scholar search: ToddlerBot: Open-Source ML-Compatible Humanoid Platform for Loco-Manipulation

## 개요
ToddlerBot은 학습 기반 로봇 연구의 새로운 하드웨어 요구, 즉 정책 실행 플랫폼이자 실제 데이터 수집 도구로서의 역할을 동시에 충족하기 위해 설계되었습니다. 이 플랫폼은 플러그 앤 플레이 영점 보정과 전이 가능한 모터 시스템 식별을 통해 고충실도 디지털 트윈을 보장하여, 시뮬레이션에서 실제 세계로의 제로샷 정책 전이를 지원합니다. 컴팩트한 크기(0.56m, 3.4kg)와 완전 3D 프린팅된 오픈소스 설계, 상용 부품의 결합은 실제 환경에서의 안전한 작동과 재현성을 보장합니다. 원격 조작 인터페이스를 통해 사용자는 인간 시연으로부터 데이터를 효율적으로 수집하여 전신 이동 조작 기술을 학습할 수 있습니다.

## 핵심 내용
### 방법
ToddlerBot의 설계는 머신러닝 호환성을 강조하며, 하드웨어 아키텍처는 고품질 시뮬레이션 및 실제 세계 데이터의 원활한 획득을 지원합니다. 주요 방법은 다음과 같습니다:
- **제로샷 정책 전이**: 플러그 앤 플레이 영점 보정과 전이 가능한 모터 시스템 식별을 통해 고충실도 디지털 트윈을 구축하여, 시뮬레이션에서 훈련된 정책을 실제 로봇에 직접 적용할 수 있습니다.
- **데이터 수집**: 사용자 친화적인 원격 조작 인터페이스는 인간 시연으로부터 운동 기술을 학습하기 위한 실제 세계 데이터 수집 과정을 단순화합니다.

### 아키텍처
- **크기 및 무게**: 높이 0.56m, 무게 3.4kg으로 실제 환경에서 안전한 작동에 적합합니다.
- **비용**: 총 비용은 6,000달러 미만이며, 완전 3D 프린팅된 오픈소스 설계와 상용 부품을 사용합니다.
- **재현성**: 포괄적인 문서를 제공하며, 기본 기술 지식을 갖추면 조립 및 유지보수가 가능하고, 독립적인 복제를 통해 검증되었습니다.

### 실험 설정 및 주요 수치
- **성능 테스트**: 팔 길이, 페이로드, 내구성 테스트 및 전신 이동 조작 작업을 포함합니다.
- **협업 작업**: 두 로봇이 함께 장난감 영역을 정리하는 장시간 협업 시나리오를 시연합니다.
- **독립 복제**: 시스템이 성공적으로 독립적으로 복제되어 재현성을 검증했습니다.

### 결론
ToddlerBot은 머신러닝 호환성, 성능 및 재현성을 향상시켜 로봇 연구에서 확장 가능한 학습과 동적 정책 실행을 위한 견고한 플랫폼을 제공합니다.
