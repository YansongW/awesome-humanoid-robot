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
人机协作安全是人形机器人领域的重要concept。以下内容整理自项目 Wiki，供深入查阅。

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


