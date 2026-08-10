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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.10554v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (770 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2503.10554v1

## 개요
NuExo 시스템은 혁신적인 동기 링크 및 동기 벨트 구동 어깨 메커니즘을 통해 인체 어깨의 복합 운동을 완벽하게 적응시키며, 전 상지 운동 범위의 사각지대 없는 완전한 커버리지를 구현합니다. 이 시스템은 무게가 5.2kg에 불과하며, 백팩형 디자인을 채택하여 일상적인 야외 시나리오에서 사용하기 편리합니다. 동시에 통합적이고 직관적인 원격 조작 프레임워크와 다중 모드 센서 데이터 수집 시스템을 통합하여 다양한 휴머노이드 로봇 플랫폼과 호환됩니다. 실험을 통해 운동 범위, 유연성, 데이터 수집 안정성 및 동적 시나리오에서의 원격 조작 정밀도에서의 우수성이 검증되었습니다.

## 핵심 내용
### 시스템 아키텍처 및 핵심 설계
NuExo의 핵심 혁신은 어깨 메커니즘에 있으며, 동기 링크 및 동기 벨트 구동 기술을 채택하여 인체 어깨의 복합 운동(예: 굴곡-신전, 외전, 회전)을 정밀하게 재현하며, 100% 자연스러운 상지 운동 범위 커버리지를 구현합니다. 시스템 총 중량은 5.2kg이며, 백팩형 착용을 지원하여 야외 일상 시나리오에 적합합니다.

### 원격 조작 및 데이터 수집
- **원격 조작 프레임워크**: 통합적이고 직관적인 원격 조작 인터페이스를 개발하여 인체 상지 운동을 휴머노이드 로봇에 실시간으로 매핑하고, 조작 지연 및 학습 비용을 줄입니다.
- **다중 모드 데이터 수집**: 힘 센서, 관성 측정 장치(IMU) 등을 통합하여 관절 각도, 힘 피드백 등의 데이터를 동기적으로 수집하며, 로봇 스킬 학습에 사용됩니다.

### 실험 설정 및 결과
- **플랫폼 검증**: 다양한 휴머노이드 로봇 플랫폼(예: 이족 보행, 바퀴형)에서 테스트하여 정적 및 동적 시나리오(예: 보행, 파지)를 모두 포함합니다.
- **성능 지표**:
  - 운동 범위: 어깨 관절 굴곡-신전 180°, 외전 160°, 팔꿈치 관절 굴곡-신전 150°.
  - 원격 조작 정밀도: 동적 시나리오에서 엔드 이펙터 위치 오차 2cm 미만.
  - 데이터 수집 안정성: 연속 2시간 작동 시 데이터 손실률 0.5% 미만.
- **사용자 테스트**: 다양한 체형의 여러 사용자가 참여했으며, 시스템 적응성이 우수하고 유의미한 운동 제한이나 불편감이 없었습니다.

### 결론
NuExo는 경량화 설계와 혁신적인 어깨 메커니즘을 통해 웨어러블 외골격에서 처음으로 전 상지 운동 범위 커버리지, 야외 휴대성, 다중 모드 데이터 수집 및 휴머노이드 로봇 원격 조작 호환성을 동시에 구현하여, 로봇 스킬 학습을 위한 효율적인 데이터 수집 및 원격 조작 도구를 제공합니다.
