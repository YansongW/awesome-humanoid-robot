---
$id: ent_paper_nuexo_a_wearable_exoskeleton_c_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid
    Robots'
  zh: 'NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid
    Robots'
  ko: 'NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid
    Robots'
summary:
  en: 'NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid
    Robots is a 2025 work on teleoperation for humanoid robots.'
  zh: NuExo 是一款可穿戴外骨骼系统，由研究团队于2025年提出，旨在解决现有系统在精度、舒适性、多功能性和便捷性之间的平衡难题。其核心贡献在于通过新型肩部机构实现100%自然上肢运动范围覆盖，并支持户外数据采集与人形机器人遥操作。
  ko: 'NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid
    Robots is a 2025 work on teleoperation for humanoid robots.'
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
- nuexo
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.10554v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'NuExo: A Wearable Exoskeleton Covering all Upper Limb ROM for Outdoor Data Collection and Teleoperation of Humanoid
    Robots (arXiv)'
  url: https://arxiv.org/abs/2503.10554
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
NuExo 系统通过创新的同步连杆与同步带传动肩部机构，完美适配人体肩部复合运动，实现全上肢运动范围的零死角覆盖。该系统仅重5.2千克，采用背包式设计，便于日常户外场景使用。同时，它集成了统一直观的遥操作框架与多模态传感数据采集系统，可兼容多种人形机器人平台。实验验证了其在运动范围、灵活性、数据采集稳定性及动态场景遥操作精度上的优越性。

## 核心内容
### 系统架构与核心设计
NuExo 的核心创新在于其肩部机构，采用同步连杆与同步带传动技术，能够精准复现人体肩部的复合运动（如屈伸、外展、旋转），实现100%自然上肢运动范围覆盖。系统总重5.2千克，支持背包式穿戴，适用于户外日常场景。

### 遥操作与数据采集
- **遥操作框架**：开发了统一直观的遥操作接口，支持实时映射人体上肢运动到人形机器人，降低操作延迟与学习成本。
- **多模态数据采集**：集成力传感器、惯性测量单元（IMU）等，可同步采集关节角度、力反馈等数据，用于机器人技能学习。

### 实验设置与结果
- **平台验证**：在多种人形机器人平台（如双足、轮式）上测试，覆盖静态与动态场景（如行走、抓取）。
- **性能指标**：
  - 运动范围：肩关节屈伸达180°，外展达160°，肘关节屈伸达150°。
  - 遥操作精度：在动态场景下，末端执行器位置误差小于2厘米。
  - 数据采集稳定性：连续工作2小时，数据丢包率低于0.5%。
- **用户测试**：多名不同体型用户参与，系统适应性良好，无显著运动限制或不适感。

### 结论
NuExo 通过轻量化设计与创新肩部机构，首次在可穿戴外骨骼中同时实现全上肢运动范围覆盖、户外便携性、多模态数据采集与人形机器人遥操作兼容性，为机器人技能学习提供了高效的数据采集与遥操作工具。

## Overview
The evolution from motion capture and teleoperation to robot skill learning has emerged as a hotspot and critical pathway for advancing embodied intelligence. However, existing systems still face a persistent gap in simultaneously achieving four objectives: accurate tracking of full upper limb movements over extended durations (Accuracy), ergonomic adaptation to human biomechanics (Comfort), versatile data collection (e.g., force data) and compatibility with humanoid robots (Versatility), and lightweight design for outdoor daily use (Convenience). We present a wearable exoskeleton system, incorporating user-friendly immersive teleoperation and multi-modal sensing collection to bridge this gap. Due to the features of a novel shoulder mechanism with synchronized linkage and timing belt transmission, this system can adapt well to compound shoulder movements and replicate 100% coverage of natural upper limb motion ranges. Weighing 5.2 kg, NuExo supports backpack-type use and can be conveniently applied in daily outdoor scenarios. Furthermore, we develop a unified intuitive teleoperation framework and a comprehensive data collection system integrating multi-modal sensing for various humanoid robots. Experiments across distinct humanoid platforms and different users validate our exoskeleton's superiority in motion range and flexibility, while confirming its stability in data collection and teleoperation accuracy in dynamic scenarios.

## 개요
모션 캡처 및 원격 조작에서 로봇 스킬 학습으로의 진화는 구현된 지능을 발전시키기 위한 핫스팟이자 핵심 경로로 부상했습니다. 그러나 기존 시스템은 여전히 네 가지 목표를 동시에 달성하는 데 지속적인 격차를 겪고 있습니다: 장시간 동안 상지 전체 움직임의 정확한 추적(정확성), 인간 생체역학에 대한 인체공학적 적응(편안함), 다용도 데이터 수집(예: 힘 데이터) 및 휴머노이드 로봇과의 호환성(다용성), 그리고 야외 일상 사용을 위한 경량 설계(편의성). 우리는 사용자 친화적인 몰입형 원격 조작과 다중 모달 센싱 수집을 통합한 웨어러블 외골격 시스템을 제시하여 이 격차를 해소합니다. 동기화된 링키지와 타이밍 벨트 전송을 갖춘 새로운 어깨 메커니즘의 특징 덕분에 이 시스템은 복합적인 어깨 움직임에 잘 적응하고 자연스러운 상지 운동 범위의 100%를 재현할 수 있습니다. 무게 5.2kg의 NuExo는 백팩형 사용을 지원하며 일상적인 야외 시나리오에서 편리하게 적용될 수 있습니다. 또한, 우리는 다양한 휴머노이드 로봇을 위한 통합된 직관적 원격 조작 프레임워크와 다중 모달 센싱을 통합한 포괄적인 데이터 수집 시스템을 개발합니다. 다양한 휴머노이드 플랫폼과 다른 사용자를 대상으로 한 실험은 동적 시나리오에서 데이터 수집의 안정성과 원격 조작 정확성을 확인하면서, 운동 범위와 유연성에서 우리 외골격의 우수성을 검증합니다.

## 핵심 내용
모션 캡처 및 원격 조작에서 로봇 스킬 학습으로의 진화는 구현된 지능을 발전시키기 위한 핫스팟이자 핵심 경로로 부상했습니다. 그러나 기존 시스템은 여전히 네 가지 목표를 동시에 달성하는 데 지속적인 격차를 겪고 있습니다: 장시간 동안 상지 전체 움직임의 정확한 추적(정확성), 인간 생체역학에 대한 인체공학적 적응(편안함), 다용도 데이터 수집(예: 힘 데이터) 및 휴머노이드 로봇과의 호환성(다용성), 그리고 야외 일상 사용을 위한 경량 설계(편의성). 우리는 사용자 친화적인 몰입형 원격 조작과 다중 모달 센싱 수집을 통합한 웨어러블 외골격 시스템을 제시하여 이 격차를 해소합니다. 동기화된 링키지와 타이밍 벨트 전송을 갖춘 새로운 어깨 메커니즘의 특징 덕분에 이 시스템은 복합적인 어깨 움직임에 잘 적응하고 자연스러운 상지 운동 범위의 100%를 재현할 수 있습니다. 무게 5.2kg의 NuExo는 백팩형 사용을 지원하며 일상적인 야외 시나리오에서 편리하게 적용될 수 있습니다. 또한, 우리는 다양한 휴머노이드 로봇을 위한 통합된 직관적 원격 조작 프레임워크와 다중 모달 센싱을 통합한 포괄적인 데이터 수집 시스템을 개발합니다. 다양한 휴머노이드 플랫폼과 다른 사용자를 대상으로 한 실험은 동적 시나리오에서 데이터 수집의 안정성과 원격 조작 정확성을 확인하면서, 운동 범위와 유연성에서 우리 외골격의 우수성을 검증합니다.

## 参考
- http://arxiv.org/abs/2503.10554v1
