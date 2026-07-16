---
$id: ent_concept_human_robot_collaboration_safety
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Human-Robot Collaboration Safety
  zh: 人机协作安全
  ko: 인간-로봇 협업 안전
summary:
  en: The set of standards, sensors, control laws, and workplace designs that ensure safe coexistence and cooperation between
    humans and robots.
  zh: 确保人与机器人安全共存与协作的标准、传感器、控制律与工作环境设计集合，涵盖 ISO 13482、ISO/TS 15066、IEC 61508、ISO 13849、IEC 62368 等核心标准及 CE、UL、FCC、CR、CCC 等区域市场准入要求。
  ko: 인간과 로봇의 안전한 공존·협력을 보장하는 표준·센서·제어법·작업장 설계 집합.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- concept
- chapter_17
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-01.md#1.4.4 合规性：从“实验室自由”到“市场准入” by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---


## 概述
人机协作安全是人形机器人领域的重要概念。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人形机器人在工作环境中与人密切互动，必须符合功能安全、电气安全、电磁兼容、机械安全等相关标准。主要标准包括：

| 标准 | 适用范围 | 核心要求 |
|------|---------|---------|
| ISO 13482:2014 | 个人护理机器人 | 速度、力、接触压力限制 |
| ISO/TS 15066 | 协作机器人 | 人机协作安全要求 |
| IEC 61508 | 功能安全 | 控制系统安全完整性等级（SIL） |
| ISO 13849 | 机械安全控制系统 | 控制系统安全相关部件 |
| IEC 62368 | 音视频与信息技术设备安全 | 电气安全、火灾风险 |

不同地区还有不同的市场准入要求：

- **欧盟**：CE 标志
- **美国**：UL 认证、FCC 电磁兼容
- **中国**：CR 认证（中国机器人认证）、CCC 等

合规性不仅影响设计选择（如最大运动速度、外壳材料、急停按钮位置），还直接影响测试成本和时间。一个完整的安全认证周期可能需要 6–18 个月，费用从数万美元到数十万美元不等。

!!! note "术语解释：功能安全（Functional Safety）"
    功能安全是指系统在故障条件下仍能保持安全状态的能力。IEC 61508 定义了安全完整性等级 SIL 1–4，SIL 4 为最高等级。实现功能安全需要危险分析、冗余设计、故障检测、安全关断机制和系统验证。

!!! note "术语解释：EMC（Electromagnetic Compatibility）"
    电磁兼容性指设备在电磁环境中正常工作且不对其他设备产生不可接受电磁干扰的能力。EMC 测试包括辐射发射（RE）、传导发射（CE）、静电放电（ESD）、电快速瞬变脉冲群（EFT）等。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-01.md#1.4.4 合规性：从“实验室自由”到“市场准入”

## Overview
Human-robot collaboration safety is a critical concept in the field of humanoid robotics. The following content is compiled from the project Wiki for in-depth reference.

## Content
Humanoid robots working in close interaction with humans in work environments must comply with relevant standards for functional safety, electrical safety, electromagnetic compatibility, and mechanical safety. Key standards include:

| Standard | Scope | Core Requirements |
|----------|-------|-------------------|
| ISO 13482:2014 | Personal care robots | Speed, force, contact pressure limits |
| ISO/TS 15066 | Collaborative robots | Human-robot collaboration safety requirements |
| IEC 61508 | Functional safety | Safety Integrity Level (SIL) for control systems |
| ISO 13849 | Safety of machinery control systems | Safety-related parts of control systems |
| IEC 62368 | Safety of audio/video and IT equipment | Electrical safety, fire risk |

Different regions also have distinct market access requirements:

- **European Union**: CE marking
- **United States**: UL certification, FCC electromagnetic compatibility
- **China**: CR certification (China Robot Certification), CCC, etc.

Compliance not only influences design choices (e.g., maximum motion speed, enclosure materials, emergency stop button placement) but also directly impacts testing costs and timelines. A full safety certification cycle may take 6–18 months, with costs ranging from tens of thousands to hundreds of thousands of dollars.

!!! note "Term Explanation: Functional Safety"
    Functional safety refers to a system's ability to maintain a safe state under fault conditions. IEC 61508 defines Safety Integrity Levels (SIL) 1–4, with SIL 4 being the highest. Achieving functional safety requires hazard analysis, redundancy design, fault detection, safety shutdown mechanisms, and system verification.

!!! note "Term Explanation: EMC (Electromagnetic Compatibility)"
    Electromagnetic compatibility refers to a device's ability to function normally in an electromagnetic environment without causing unacceptable electromagnetic interference to other devices. EMC testing includes radiated emissions (RE), conducted emissions (CE), electrostatic discharge (ESD), electrical fast transients (EFT), etc.

## 개요
인간-로봇 협업 안전은 휴머노이드 로봇 분야의 중요한 개념입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
휴머노이드 로봇은 작업 환경에서 인간과 밀접하게 상호작용하므로, 기능 안전, 전기 안전, 전자기 적합성, 기계 안전 등 관련 표준을 준수해야 합니다. 주요 표준은 다음과 같습니다:

| 표준 | 적용 범위 | 핵심 요구사항 |
|------|---------|---------|
| ISO 13482:2014 | 개인 케어 로봇 | 속도, 힘, 접촉 압력 제한 |
| ISO/TS 15066 | 협업 로봇 | 인간-로봇 협업 안전 요구사항 |
| IEC 61508 | 기능 안전 | 제어 시스템 안전 무결성 수준(SIL) |
| ISO 13849 | 기계 안전 제어 시스템 | 제어 시스템 안전 관련 부품 |
| IEC 62368 | 오디오/비디오 및 정보 기술 장비 안전 | 전기 안전, 화재 위험 |

지역별로 다른 시장 진입 요구사항이 있습니다:

- **유럽**: CE 마크
- **미국**: UL 인증, FCC 전자기 적합성
- **중국**: CR 인증(중국 로봇 인증), CCC 등

규정 준수는 설계 선택(예: 최대 운동 속도, 외장 재질, 비상 정지 버튼 위치)에 영향을 미칠 뿐만 아니라, 테스트 비용과 시간에도 직접적인 영향을 미칩니다. 완전한 안전 인증 주기는 6~18개월이 소요될 수 있으며, 비용은 수만 달러에서 수십만 달러까지 다양합니다.

!!! note "용어 설명: 기능 안전(Functional Safety)"
    기능 안전이란 시스템이 고장 조건에서도 안전 상태를 유지할 수 있는 능력을 의미합니다. IEC 61508은 안전 무결성 수준 SIL 1~4를 정의하며, SIL 4가 최고 수준입니다. 기능 안전을 구현하려면 위험 분석, 이중화 설계, 고장 감지, 안전 차단 메커니즘 및 시스템 검증이 필요합니다.

!!! note "용어 설명: EMC(Electromagnetic Compatibility)"
    전자기 적합성이란 장비가 전자기 환경에서 정상적으로 작동하면서 다른 장비에 허용할 수 없는 전자기 간섭을 발생시키지 않는 능력을 의미합니다. EMC 테스트에는 방사 방출(RE), 전도 방출(CE), 정전기 방전(ESD), 전기적 빠른 과도 현상(EFT) 등이 포함됩니다.
