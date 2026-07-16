---
$id: ent_standard_ul_fcc_ce
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: standard
names:
  en: Regional Market Certifications (UL / FCC / CE)
  zh: 区域准入认证
  ko: 지역별 시장 인증(UL/FCC/CE)
summary:
  en: The set of mandatory or voluntary certifications required to sell robots in specific regions, such as UL for North America,
    CE for Europe, and FCC for electromagnetic compatibility.
  zh: 人形机器人进入各区域市场所需的强制或自愿性认证汇总，涵盖 ISO 13482、ISO/TS 15066、ISO 13849-1、IEC 61508、IEC 62368-1、UL 1740、FCC Part 15、CE 标志、CR 认证与
    CCC 的制定机构、适用范围与核心关注点。
  ko: 특정 지역에서 로봇을 판매하기 위해 필요한 강제 또는 자발적 인증; 북미 UL, 유럽 CE, 전자기 적합성 FCC 등.
domains:
- 12_policy_regulation_ethics
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- standard
- chapter_12
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-01.md#1.13.2 主要国际与区域标准概览 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---


## 概述
区域准入认证是人形机器人领域的重要标准。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
| 标准/认证 | 制定机构 | 适用范围 | 核心关注点 |
|----------|---------|---------|-----------|
| ISO 13482:2014 | ISO | 个人护理机器人 | 机械安全、速度/力限制、接触安全 |
| ISO/TS 15066:2016 | ISO | 协作机器人 | 最大允许压力/力、安全功能 |
| ISO 13849-1:2023 | ISO | 机械安全控制系统 | 控制系统安全相关部件可靠性 |
| IEC 61508:2010 | IEC | 功能安全通用标准 | SIL 等级、安全生命周期 |
| IEC 62368-1:2018 | IEC | 信息技术设备安全 | 电气安全、火灾、能量危险 |
| UL 1740 | UL | 工业机器人安全 | 机器人系统安全评估 |
| FCC Part 15 | FCC | 美国无线电设备 | 电磁兼容与射频干扰 |
| CE 标志 | 欧盟 | 欧盟市场准入 | 符合相关指令（机械指令、低电压指令等） |
| CR 认证 | 中国机器人联盟/认监委 | 中国机器人市场准入 | 安全、EMC、性能、可靠性 |
| CCC | 中国质检总局 | 强制性产品认证 | 电气安全等 |

!!! note "术语解释：CE 标志与 CCC 认证"
    CE 标志是产品进入欧盟市场的合格声明标志，表示产品符合欧盟相关指令的基本要求。CCC（China Compulsory Certification）是中国强制性产品认证，涉及人身安全、动植物生命健康和环境保护的产品必须获得 CCC 认证方可销售。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-01.md#1.13.2 主要国际与区域标准概览


