---
$id: ent_paper_production_ramp_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Production Ramp
  zh: 产能爬坡
  ko: Production Ramp
summary:
  en: Transition from pilot-line builds to volume manufacturing while improving yield, cycle time, and cost.
  zh: 核心内容 当前人形机器人执行器供应链呈现**高端减速器与高端编码器高度集中**的特征：谐波减速器全球头部企业 Harmonic Drive、RV 减速器 Nabtesco 占据较大市场份额；高端磁编码器/光编也主要由日本、欧洲企业供应。这种集中度带来供应风险，尤其在地缘政治与产能紧张时。
  ko: 파일럿 라인에서 볼륨 제조로 전환하면서 수율, 사이클 타임 및 비용을 개선하는 과정.
domains:
- 05_mass_production
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- concept
- manufacturing
- ramp
- volume
- yield
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#国产替代与供应链韧性 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Production Ramp
  url: https://en.wikipedia.org/wiki/Ramp-up
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
产能爬坡是人形机器人领域的重要concept。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
当前人形机器人执行器供应链呈现**高端减速器与高端编码器高度集中**的特征：谐波减速器全球头部企业 Harmonic Drive、RV 减速器 Nabtesco 占据较大市场份额；高端磁编码器/光编也主要由日本、欧洲企业供应。这种集中度带来供应风险，尤其在地缘政治与产能紧张时。

国内供应链在过去十年快速进步：绿的谐波、来福谐波在谐波减速器领域已实现批量供货；汇川、禾川、雷赛等在无框电机与伺服驱动领域具备竞争力；峰岹科技、纳芯微等在栅极驱动与电流传感器芯片上取得突破。然而，在**超高精度谐波减速器、超高分辨率光编、车规级功率模块**等高端领域，国产替代仍在进行中。

提升供应链韧性的工程策略包括：

1. **双源化**：关键零部件至少认证两家供应商，避免单一来源；
2. **模块化接口**：把电机、减速器、驱动器接口标准化，便于切换供应商；
3. **安全库存与 VMI**：对长交期零件建立合理库存或供应商管理库存；
4. **垂直整合**：自研核心部件（如 Tesla 自研执行器、Optimus 电机与减速器一体化），但需权衡资本投入与产能爬坡。

!!! note "术语解释：供应链韧性、双源化、垂直整合、VMI、产能爬坡"
    - **供应链韧性（supply chain resilience）**：供应链抵抗中断并快速恢复的能力。
    - **双源化（dual sourcing）**：为同一零部件认证两个供应商。
    - **垂直整合（vertical integration）**：企业向上游零部件延伸，自主生产关键件。
    - **VMI（vendor managed inventory）**：供应商管理库存，按实际消耗补货。
    - **产能爬坡（production ramp-up）**：从试产到大批量量产的过程，良率与成本逐步优化。

---

## 参考
- [Production Ramp](https://en.wikipedia.org/wiki/Ramp-up)
- 项目 Wiki：chapter-04.md#国产替代与供应链韧性


